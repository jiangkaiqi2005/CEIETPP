# LabelMe 转 YOLO 格式使用教程

## 📁 脚本位置
```
E:\College Students' Innovative Entrepreneurial Training Plan Program\labelme_to_yolo.py
```

---

## 📋 类别定义（固定 7 个）

| ID | 类别名 | 类型 | 说明 | 标注建议 |
|----|--------|------|------|---------|
| 0 | `flat_ground` | 语义分割 | 平地（走廊/厂房/通道地面） | 多边形 |
| 1 | `rough_ground` | 语义分割 | 粗糙地面 | 多边形 |
| 2 | `stairs` | 语义分割 | 楼梯 | 多边形 |
| 3 | `obstacle_static` | 目标检测 | 静态障碍（箱子/设备/货架等） | 矩形框 |
| 4 | `obstacle_dynamic` | 目标检测 | 动态障碍（行人/移动物体） | 矩形框 |
| 5 | `doorway` | 目标检测 | 门口 | 矩形框 |
| 6 | `no_pass` | 语义分割 | 不可通过区域（坑洞/危险区） | 多边形 |

---

## 📖 类别详细说明

### 语义分割类（用多边形标注）

#### 0: flat_ground - 平地
**包括：**
- ✅ 走廊地面
- ✅ 厂房地面
- ✅ 通道地面
- ✅ 货架下方的地面（如果可见）
- ✅ 大厅地面
- ✅ 楼梯底部的平地

**不包括：**
- ❌ 楼梯本身 → 标为 `stairs`
- ❌ 坑洞/危险区 → 标为 `no_pass`
- ❌ 粗糙地面 → 标为 `rough_ground`

---

#### 1: rough_ground - 粗糙地面
- 不平整的地面
- 需要特殊通过的地形

---

#### 2: stairs - 楼梯
- 所有楼梯区域
- 台阶

---

#### 6: no_pass - 不可通过区域
- 坑洞
- 危险区
- 禁止通行区域

---

### 目标检测类（用矩形框标注）

#### 3: obstacle_static - 静态障碍物
**包含：**
- ✅ 箱子、货箱、托盘
- ✅ 设备、机器、货架
- ✅ 桌椅、家具
- ✅ 柱子、立柱
- ✅ 垃圾桶、杂物
- ✅ 建筑材料（砖堆、沙袋）

---

#### 4: obstacle_dynamic - 动态障碍物
- 行人
- 移动的车辆/机器人
- 其他移动物体

---

#### 5: doorway - 门口
- 门框
- 出入口

---

## 🚀 快速开始

### 步骤 1：直接运行脚本

```bash
python "E:\College Students' Innovative Entrepreneurial Training Plan Program\labelme_to_yolo.py"
```

或**双击** `labelme_to_yolo.py`

---

### 步骤 2：查看类别验证

运行时会显示：
```
📋 类别定义（固定）:
======================================================================
   [0] flat_ground         # 语义分割 - 平地（走廊/厂房/通道地面）
   [1] rough_ground        # 语义分割 - 粗糙地面
   [2] stairs              # 语义分割 - 楼梯
   [3] obstacle_static     # 目标检测 - 静态障碍
   [4] obstacle_dynamic    # 目标检测 - 动态障碍
   [5] doorway             # 目标检测 - 门口
   [6] no_pass             # 语义分割 - 不可通过区域
======================================================================
```

---

### 步骤 3：等待转换完成

脚本会自动：
1. ✅ 读取所有 JSON 标注文件
2. ✅ 验证标签名是否在 7 个类别中
3. ✅ 复制对应图片
4. ✅ 转换标注为 YOLO 格式
5. ✅ 生成 `data.yaml` 配置文件

输出位置：
```
E:\College Students' Innovative Entrepreneurial Training Plan Program\Dataset\yolo_format\
├── images/
│   ├── train/
│   ├── val/
│   └── test/
├── labels/
│   ├── train/
│   ├── val/
│   └── test/
└── data.yaml
```

---

### 步骤 4：开始训练

```python
from ultralytics import YOLO

# 使用分割模型（推荐，支持检测和分割混合）
model = YOLO("yolo26n-seg.pt")

# 训练
model.train(
    data="E:/College Students' Innovative Entrepreneurial Training Plan Program/Dataset/yolo_format/data.yaml",
    epochs=100,
    imgsz=640,
    batch=16,
    device=0,  # GPU 设备，CPU 改为 'cpu'
)

# 验证
metrics = model.val()
print(f"mAP50-95: {metrics.box.map:.4f}")

# 预测
results = model.predict(
    source="测试图片.jpg",
    show=True,
    save=True
)
```

---

## ⚠️ 重要提示

### 标签名必须完全匹配！

**正确：**
```
flat_ground
rough_ground
stairs
obstacle_static
obstacle_dynamic
doorway
no_pass
```

**错误（会被跳过并警告）：**
```
flatground      ❌ 缺少下划线
Flat_Ground     ❌ 大小写不匹配
obstacle        ❌ 不完整
ground          ❌ 错误的标签名
```

---

## 🔧 常见问题

### ❌ 问题 1：发现未定义类别
```
⚠️  发现未定义类别（不在 7 个类别中）: flatground, obstacle
    请检查标注标签名是否正确！
```

**解决：** 检查 LabelMe 中的标签名，确保与 7 个固定类别完全一致

---

### ❌ 问题 2：找不到图片
```
⚠️  未找到图片：xxx.json
```

**解决：** 检查 `img-train/` 等目录中是否有对应图片

---

### ❌ 问题 3：标注统计为 0
```
[0] flat_ground: 0 个
```

**可能原因：**
1. 还没有标注这个类别
2. 标签名拼写错误
3. 标注文件未放在正确的目录

---

### ❌ 问题 4：显存不足
```
RuntimeError: CUDA out of memory
```

**解决：**
```python
# 减小 batch size
model.train(batch=8)

# 或减小图片尺寸
model.train(imgsz=320)
```

---

## 📊 训练技巧

### 1. 选择模型

| 模型 | 适用场景 | 速度 | 精度 |
|------|---------|------|------|
| `yolo26n-seg.pt` | 实时检测 + 分割 | ⚡⚡⚡ | ⭐⭐⭐ |
| `yolo26s-seg.pt` | 平衡速度与精度 | ⚡⚡ | ⭐⭐⭐⭐ |
| `yolo26m-seg.pt` | 高精度需求 | ⚡ | ⭐⭐⭐⭐⭐ |

### 2. 针对不同类别的训练建议

| 类别 | 建议 |
|------|------|
| `flat_ground` | 标注时注意避开障碍物遮挡区域 |
| `obstacle_static` | 数据量通常最多，确保多样性 |
| `obstacle_dynamic` | 可能需要更多样本（行人姿态多样） |
| `doorway` | 关键导航点，确保标注准确 |
| `no_pass` | 安全关键，宁可多标不可漏标 |

---

## 📝 输出格式说明

### 语义分割（多边形）
```
# class_id x1 y1 x2 y2 x3 y3 ...
0 0.5 0.3 0.6 0.3 0.65 0.5 0.6 0.7 0.5 0.7 0.4 0.5  # flat_ground
```

### 目标检测（矩形框）
```
# class_id x_center y_center width height
3 0.523456 0.456789 0.123456 0.234567  # obstacle_static
```

---

## 📞 需要帮助？

检查以下文件：
1. ✅ `data.yaml` - 查看类别配置
2. ✅ 转换日志 - 查看哪些文件转换失败
3. ✅ 标注统计 - 确认各类别标注数量

---

**最后更新：** 2026-03-24  
**作者：** CoPaw  
**项目：** 面向复杂工业环境的轮足机器人自主巡检和物资搬运系统
