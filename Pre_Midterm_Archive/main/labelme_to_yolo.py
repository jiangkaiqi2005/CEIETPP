"""
LabelMe 标注转 YOLO 格式转换脚本
支持：矩形框（检测） + 多边形（分割）

项目：面向复杂工业环境的轮足机器人自主巡检和物资搬运系统
深度学习部分：环境感知与地形分析

类别定义（固定）:
0: flat_ground        # 语义分割 - 平地
1: rough_ground       # 语义分割 - 粗糙地面
2: stairs             # 语义分割 - 楼梯
3: obstacle_static    # 目标检测 - 静态障碍
4: obstacle_dynamic   # 目标检测 - 动态障碍
5: doorway            # 目标检测 - 门口
6: no_pass            # 语义分割 - 不可通过区域

作者：CoPaw
日期：2026-03-24
"""

import json
import os
import shutil
from pathlib import Path
from PIL import Image

# ==================== 配置区域 ====================

# 数据集根目录
DATASET_ROOT = Path(r"E:\College Students' Innovative Entrepreneurial Training Plan Program\Dataset")

# 输入目录
IMG_DIRS = {
    "train": DATASET_ROOT / "img" / "img-train",
    "val": DATASET_ROOT / "img" / "img-val",
    "test": DATASET_ROOT / "img" / "img-test",
}

LABEL_DIRS = {
    "train": DATASET_ROOT / "label" / "label-train",
    "val": DATASET_ROOT / "label" / "label-val",
    "test": DATASET_ROOT / "label" / "label-test",
}

# 输出 YOLO 数据集目录
YOLO_DATASET_DIR = DATASET_ROOT / "yolo_format"

# ==================== 类别定义（固定，不自动提取） ====================

CLASSES = {
    "flat_ground": 0,        # 语义分割 - 平地（走廊、厂房、通道、货架下方、大厅、楼梯底部）
    "rough_ground": 1,       # 语义分割 - 粗糙地面
    "stairs": 2,             # 语义分割 - 楼梯
    "obstacle_static": 3,    # 目标检测 - 静态障碍（箱子、设备、货架、桌椅、柱子、垃圾桶、建筑材料）
    "obstacle_dynamic": 4,   # 目标检测 - 动态障碍（行人、移动物体）
    "doorway": 5,            # 目标检测 - 门口
    "no_pass": 6,            # 语义分割 - 不可通过区域（坑洞、危险区）
}

# 类别说明（用于输出）
CLASS_DESCRIPTIONS = {
    "flat_ground": "语义分割 - 平地（走廊/厂房/通道地面，不包括楼梯、坑洞、粗糙地面）",
    "rough_ground": "语义分割 - 粗糙地面",
    "stairs": "语义分割 - 楼梯",
    "obstacle_static": "目标检测 - 静态障碍（箱子/设备/货架/桌椅/柱子/垃圾桶/建筑材料）",
    "obstacle_dynamic": "目标检测 - 动态障碍（行人/移动物体）",
    "doorway": "目标检测 - 门口",
    "no_pass": "语义分割 - 不可通过区域（坑洞/危险区）",
}

# ==================== 不要修改下面的代码 ====================

def validate_and_show_classes():
    """
    验证并显示类别定义
    """
    print("\n📋 类别定义（固定）:")
    print("=" * 70)
    
    for name, id in sorted(CLASSES.items(), key=lambda x: x[1]):
        desc = CLASS_DESCRIPTIONS.get(name, "")
        print(f"   [{id}] {name:20s} # {desc}")
    
    print("=" * 70)
    print(f"   总计：{len(CLASSES)} 个类别")
    print("=" * 70)
    
    return CLASSES


def convert_rectangle_to_yolo(rect_points, img_width, img_height):
    """
    将 LabelMe 矩形框转换为 YOLO 检测格式
    输入：rect_points = [[xmin,ymin], [xmax,ymax]]
    输出：x_center y_center width height (归一化)
    """
    xmin = min(rect_points[0][0], rect_points[1][0])
    ymin = min(rect_points[0][1], rect_points[1][1])
    xmax = max(rect_points[0][0], rect_points[1][0])
    ymax = max(rect_points[0][1], rect_points[1][1])
    
    x_center = (xmin + xmax) / 2.0 / img_width
    y_center = (ymin + ymax) / 2.0 / img_height
    width = (xmax - xmin) / img_width
    height = (ymax - ymin) / img_height
    
    x_center = max(0, min(1, x_center))
    y_center = max(0, min(1, y_center))
    width = max(0, min(1, width))
    height = max(0, min(1, height))
    
    return f"{x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"


def convert_polygon_to_yolo(points, img_width, img_height):
    """
    将 LabelMe 多边形转换为 YOLO 分割格式
    输入：points = [[x1,y1], [x2,y2], ...]
    输出：x1 y1 x2 y2 x3 y3 ... (归一化)
    """
    normalized = []
    for point in points:
        x = point[0] / img_width
        y = point[1] / img_height
        normalized.extend([x, y])
    
    return " ".join(f"{p:.6f}" for p in normalized)


def convert_labelme_to_yolo(json_file, img_width, img_height, classes):
    """
    转换单个 LabelMe JSON 文件
    返回：YOLO 格式的行列表，未知类别列表，类别统计
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    yolo_objects = []
    unknown_labels = []
    label_counts = {}
    
    for shape in data.get('shapes', []):
        label = shape.get('label', '')
        shape_type = shape.get('shape_type', '')
        points = shape.get('points', [])
        
        # 统计标注
        if label:
            label_counts[label] = label_counts.get(label, 0) + 1
        
        # 检查类别是否在定义中
        if label not in classes:
            if label and label not in unknown_labels:
                unknown_labels.append(label)
            continue
        
        class_id = classes[label]
        
        try:
            if shape_type == 'rectangle':
                if len(points) >= 2:
                    bbox = convert_rectangle_to_yolo(points, img_width, img_height)
                    yolo_objects.append(f"{class_id} {bbox}")
            
            elif shape_type == 'polygon':
                polygon = convert_polygon_to_yolo(points, img_width, img_height)
                yolo_objects.append(f"{class_id} {polygon}")
            
            elif shape_type == 'circle':
                if len(points) >= 2:
                    center_x, center_y = points[0]
                    edge_x, edge_y = points[1]
                    radius = ((edge_x - center_x)**2 + **(edge_y - center_y)2) ** 0.5
                    xmin = center_x - radius
                    ymin = center_y - radius
                    xmax = center_x + radius
                    ymax = center_y + radius
                    bbox = convert_rectangle_to_yolo([[xmin, ymin], [xmax, ymax]], img_width, img_height)
                    yolo_objects.append(f"{class_id} {bbox}")
        
        except Exception as e:
            print(f"  ✗ 转换形状失败：{e}")
            continue
    
    return yolo_objects, unknown_labels, label_counts


def get_image_size(json_file, img_dir):
    """
    从 JSON 文件或图片文件获取图片尺寸
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if 'imageWidth' in data and 'imageHeight' in data:
        return data['imageWidth'], data['imageHeight']
    
    img_filename = data.get('imagePath', '')
    if img_filename:
        img_path = Path(img_dir) / img_filename
        if img_path.exists():
            with Image.open(img_path) as img:
                return img.size
    
    json_stem = json_file.stem
    for suffix in ['_jpg', '_png', '_jpeg', '_bmp']:
        if json_stem.endswith(suffix):
            base_name = json_stem[:-len(suffix)]
            for ext in ['.jpg', '.jpeg', '.png', '.bmp', '.JPG', '.JPEG', '.PNG', '.BMP']:
                img_path = Path(img_dir) / (base_name + ext)
                if img_path.exists():
                    with Image.open(img_path) as img:
                        return img.size
    
    for ext in ['.jpg', '.jpeg', '.png', '.bmp', '.JPG', '.JPEG', '.PNG', '.BMP']:
        img_path = Path(img_dir) / (json_stem + ext)
        if img_path.exists():
            with Image.open(img_path) as img:
                return img.size
    
    for ext in ['.jpg', '.jpeg', '.png', '.bmp', '.JPG', '.JPEG', '.PNG', '.BMP']:
        img_path = json_file.parent / (json_stem + ext)
        if img_path.exists():
            with Image.open(img_path) as img:
                return img.size
    
    raise FileNotFoundError(f"未找到对应的图片文件：{json_file.name}")


def find_matching_image(json_file, img_dir):
    """
    查找与 JSON 文件匹配的图片文件
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    img_filename = data.get('imagePath', '')
    if img_filename:
        img_path = Path(img_dir) / img_filename
        if img_path.exists():
            return img_path
    
    json_stem = json_file.stem
    for suffix in ['_jpg', '_png', '_jpeg', '_bmp']:
        if json_stem.endswith(suffix):
            base_name = json_stem[:-len(suffix)]
            for ext in ['.jpg', '.jpeg', '.png', '.bmp', '.JPG', '.JPEG', '.PNG', '.BMP']:
                img_path = Path(img_dir) / (base_name + ext)
                if img_path.exists():
                    return img_path
    
    for ext in ['.jpg', '.jpeg', '.png', '.bmp', '.JPG', '.JPEG', '.PNG', '.BMP']:
        img_path = Path(img_dir) / (json_stem + ext)
        if img_path.exists():
            return img_path
    
    return None


def process_split(json_files, img_dir, split_name, classes):
    """
    处理一个数据划分（train/val/test）
    """
    if split_name == 'train':
        img_dest_dir = YOLO_DATASET_DIR / "images" / "train"
        label_dest_dir = YOLO_DATASET_DIR / "labels" / "train"
    elif split_name == 'val':
        img_dest_dir = YOLO_DATASET_DIR / "images" / "val"
        label_dest_dir = YOLO_DATASET_DIR / "labels" / "val"
    else:
        img_dest_dir = YOLO_DATASET_DIR / "images" / "test"
        label_dest_dir = YOLO_DATASET_DIR / "labels" / "test"
    
    img_dest_dir.mkdir(parents=True, exist_ok=True)
    label_dest_dir.mkdir(parents=True, exist_ok=True)
    
    success_count = 0
    total_objects = 0
    failed_files = []
    all_unknown_labels = set()
    total_label_counts = {}
    
    for json_file in json_files:
        try:
            img_src = find_matching_image(json_file, img_dir)
            
            if not img_src:
                print(f"⚠️  未找到图片：{json_file.name}")
                failed_files.append((json_file.name, "图片未找到"))
                continue
            
            with Image.open(img_src) as img:
                img_width, img_height = img.size
            
            yolo_objects, unknown_labels, label_counts = convert_labelme_to_yolo(json_file, img_width, img_height, classes)
            
            all_unknown_labels.update(unknown_labels)
            
            # 合并类别统计
            for label, count in label_counts.items():
                total_label_counts[label] = total_label_counts.get(label, 0) + count
            
            img_dest = img_dest_dir / img_src.name
            shutil.copy2(img_src, img_dest)
            
            txt_file = label_dest_dir / (json_file.stem + ".txt")
            with open(txt_file, 'w', encoding='utf-8') as f:
                for obj in yolo_objects:
                    f.write(obj + "\n")
            
            success_count += 1
            total_objects += len(yolo_objects)
            
            if success_count % 50 == 0 or success_count == len(json_files):
                print(f"  已处理：{success_count}/{len(json_files)} (共 {total_objects} 个物体)")
            
        except Exception as e:
            print(f"✗ 处理失败 {json_file.name}: {e}")
            failed_files.append((json_file.name, str(e)))
    
    print(f"✓ {split_name} 完成：{success_count}/{len(json_files)} 个文件，{total_objects} 个物体")
    
    if all_unknown_labels:
        print(f"  ⚠️  发现未定义类别（不在 7 个类别中）: {', '.join(all_unknown_labels)}")
        print(f"      请检查标注标签名是否正确！")
    
    if failed_files:
        print(f"  失败 {len(failed_files)} 个文件:")
        for fname, reason in failed_files[:10]:
            print(f"    - {fname}: {reason}")
        if len(failed_files) > 10:
            print(f"    ... 还有 {len(failed_files) - 10} 个")
    
    return total_label_counts


def create_data_yaml(classes):
    """
    生成 YOLO 数据集配置文件
    """
    yaml_content = f"""# YOLO 数据集配置文件
# 由 labelme_to_yolo.py 自动生成
# 日期：2026-03-24
# 
# 项目：面向复杂工业环境的轮足机器人自主巡检和物资搬运系统
# 深度学习部分：环境感知与地形分析
#
# 类别定义:
#   0: flat_ground      - 语义分割 - 平地（走廊/厂房/通道地面）
#   1: rough_ground     - 语义分割 - 粗糙地面
#   2: stairs           - 语义分割 - 楼梯
#   3: obstacle_static  - 目标检测 - 静态障碍（箱子/设备/货架等）
#   4: obstacle_dynamic - 目标检测 - 动态障碍（行人/移动物体）
#   5: doorway          - 目标检测 - 门口
#   6: no_pass          - 语义分割 - 不可通过区域（坑洞/危险区）

# 数据集根目录
path: {YOLO_DATASET_DIR}

# 训练集和验证集路径
train: images/train
val: images/val
test: images/test

# 类别数量
nc: {len(classes)}

# 类别名称（按 ID 顺序排列）
names:
"""
    
    for name, id in sorted(classes.items(), key=lambda x: x[1]):
        yaml_content += f"  - {name}\n"
    
    yaml_content += f"""
# ==================== 使用说明 ====================
# 
# 训练分割模型（推荐，支持检测和分割混合）:
#   from ultralytics import YOLO
#   model = YOLO("yolo26n-seg.pt")
#   model.train(data="data.yaml", epochs=100)
#
# 训练检测模型（只检测矩形框目标）:
#   model = YOLO("yolo26n.pt")
#   model.train(data="data.yaml", epochs=100)
#
# 验证模型:
#   metrics = model.val()
#   print(f"mAP50-95: {{metrics.box.map:.4f}}")
#
# 预测:
#   results = model.predict(source="测试图片.jpg", show=True)
#
# ==================== 类别详细说明 ====================
#
# 语义分割类（建议用多边形标注）:
#   - flat_ground: 平地（走廊地面、厂房地面、通道地面、货架下方地面、大厅地面、楼梯底部平地）
#                  注意：不包括楼梯、坑洞、粗糙地面
#   - rough_ground: 粗糙地面
#   - stairs: 楼梯
#   - no_pass: 不可通过区域（坑洞、危险区）
#
# 目标检测类（建议用矩形框标注）:
#   - obstacle_static: 静态障碍（箱子/货箱/托盘、设备/机器/货架、桌椅/家具、柱子/立柱、
#                                  垃圾桶/杂物、建筑材料）
#   - obstacle_dynamic: 动态障碍（行人、移动物体）
#   - doorway: 门口
"""
    
    yaml_file = YOLO_DATASET_DIR / "data.yaml"
    with open(yaml_file, 'w', encoding='utf-8') as f:
        f.write(yaml_content)
    
    print(f"\n✓ data.yaml 已生成：{yaml_file}")


def verify_dataset():
    """
    验证数据集结构
    """
    print("\n" + "=" * 60)
    print("📊 数据集验证：\n")
    
    all_ok = True
    
    for split in ['train', 'val', 'test']:
        img_dir = YOLO_DATASET_DIR / "images" / split
        label_dir = YOLO_DATASET_DIR / "labels" / split
        
        if not img_dir.exists():
            print(f"  ⚠️ {split}: 图片目录不存在")
            continue
        
        img_files = set(f.stem for f in img_dir.iterdir() if f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.bmp'])
        label_files = set(f.stem for f in label_dir.iterdir() if f.suffix == '.txt')
        
        img_count = len(img_files)
        label_count = len(label_files)
        
        missing_labels = img_files - label_files
        missing_imgs = label_files - img_files
        
        if img_count == label_count and not missing_labels and not missing_imgs:
            print(f"  ✓ {split}: {img_count} 张图片，{label_count} 个标注")
        else:
            print(f"  ⚠️ {split}: {img_count} 张图片，{label_count} 个标注")
            all_ok = False
            
            if missing_labels:
                print(f"     缺少标注：{list(missing_labels)[:5]}...")
            if missing_imgs:
                print(f"     缺少图片：{list(missing_imgs)[:5]}...")
    
    yaml_file = YOLO_DATASET_DIR / "data.yaml"
    if yaml_file.exists():
        print(f"  ✓ data.yaml 存在")
    else:
        print(f"  ✗ data.yaml 缺失")
        all_ok = False
    
    if all_ok:
        print("\n  ✅ 数据集结构正确！")
    else:
        print("\n  ⚠️  数据集存在问题，请检查！")


def process_dataset():
    """
    主处理流程
    """
    print("=" * 70)
    print("LabelMe 转 YOLO 格式转换工具")
    print("项目：面向复杂工业环境的轮足机器人自主巡检和物资搬运系统")
    print("=" * 70)
    print(f"\n📂 数据集根目录：{DATASET_ROOT}")
    print(f"📂 输出目录：{YOLO_DATASET_DIR}")
    print("=" * 70)
    
    # 验证并显示类别定义
    classes = validate_and_show_classes()
    
    # 创建输出目录结构
    for split in ['train', 'val', 'test']:
        (YOLO_DATASET_DIR / "images" / split).mkdir(parents=True, exist_ok=True)
        (YOLO_DATASET_DIR / "labels" / split).mkdir(parents=True, exist_ok=True)
    print("\n✓ 目录结构创建完成")
    
    train_json_files = list(LABEL_DIRS["train"].glob("*.json")) if LABEL_DIRS["train"].exists() else []
    val_json_files = list(LABEL_DIRS["val"].glob("*.json")) if LABEL_DIRS["val"].exists() else []
    test_json_files = list(LABEL_DIRS["test"].glob("*.json")) if LABEL_DIRS["test"].exists() else []
    
    if not train_json_files and not val_json_files and not test_json_files:
        print(f"\n✗ 未找到任何 JSON 文件！")
        input("\n按回车键退出...")
        return
    
    print(f"\n📄 找到 JSON 文件:")
    print(f"   训练集：{len(train_json_files)} 个")
    print(f"   验证集：{len(val_json_files)} 个")
    print(f"   测试集：{len(test_json_files)} 个")
    print(f"   总计：{len(train_json_files) + len(val_json_files) + len(test_json_files)} 个")
    print("=" * 70)
    
    # 处理训练集
    print("\n" + "-" * 70)
    print("处理训练集...")
    print("-" * 70)
    train_counts = process_split(train_json_files, IMG_DIRS["train"], "train", classes)
    
    # 处理验证集
    print("\n" + "-" * 70)
    print("处理验证集...")
    print("-" * 70)
    val_counts = process_split(val_json_files, IMG_DIRS["val"], "val", classes)
    
    # 处理测试集
    print("\n" + "-" * 70)
    print("处理测试集...")
    print("-" * 70)
    test_counts = process_split(test_json_files, IMG_DIRS["test"], "test", classes)
    
    # 统计总标注
    print("\n" + "=" * 70)
    print("📊 标注统计：")
    total_counts = {}
    for counts in [train_counts, val_counts, test_counts]:
        for label, count in counts.items():
            total_counts[label] = total_counts.get(label, 0) + count
    
    for name, id in sorted(CLASSES.items(), key=lambda x: x[1]):
        count = total_counts.get(name, 0)
        desc = CLASS_DESCRIPTIONS.get(name, "").split(" - ")[0]
        print(f"   [{id}] {name:20s}: {count:5d} 个  ({desc})")
    
    print("=" * 70)
    
    # 生成 data.yaml
    print("\n" + "-" * 70)
    create_data_yaml(classes)
    
    # 验证数据集
    print("\n" + "-" * 70)
    verify_dataset()
    
    print("\n" + "=" * 70)
    print("🎉 转换完成！可以开始训练了！")
    print("=" * 70)
    print("\n下一步:")
    print("1. 检查 data.yaml 配置")
    print("2. 运行训练:")
    print("   from ultralytics import YOLO")
    print("   model = YOLO('yolo26n-seg.pt')  # 分割模型（推荐）")
    print("   model.train(data='data.yaml', epochs=100)")
    print("=" * 70)
    input("\n按回车键退出...")


if __name__ == "__main__":
    missing_dirs = []
    for dir_path in [IMG_DIRS["train"], LABEL_DIRS["train"]]:
        if not dir_path.exists():
            missing_dirs.append(str(dir_path))
    
    if missing_dirs:
        print("\n✗ 错误：以下目录不存在：")
        for d in missing_dirs:
            print(f"   {d}")
        print("\n请检查数据集路径是否正确！")
        input("\n按回车键退出...")
        exit(1)
    
    process_dataset()
