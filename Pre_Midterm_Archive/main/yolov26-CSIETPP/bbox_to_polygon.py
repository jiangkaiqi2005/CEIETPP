import os

def bbox_to_polygon(xc, yc, w, h):
    x1 = xc - w / 2
    y1 = yc - h / 2

    x2 = xc + w / 2
    y2 = yc - h / 2

    x3 = xc + w / 2
    y3 = yc + h / 2

    x4 = xc - w / 2
    y4 = yc + h / 2

    return [x1, y1, x2, y2, x3, y3, x4, y4]


def process_label_file(file_path):
    new_lines = []

    with open(file_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        parts = list(map(float, line.strip().split()))

        cls = int(parts[0])
        coords = parts[1:]

        # 判断是 bbox 还是 polygon
        if len(coords) == 4:
            # bbox → polygon
            xc, yc, w, h = coords
            poly = bbox_to_polygon(xc, yc, w, h)
            new_line = [cls] + poly
        else:
            # 已经是 polygon，保持不变
            new_line = [cls] + coords

        # 转成字符串
        new_lines.append(" ".join(map(str, new_line)))

    # 覆盖写回
    with open(file_path, 'w') as f:
        f.write("\n".join(new_lines))


def process_folder(label_dir):
    for root, _, files in os.walk(label_dir):
        for file in files:
            if file.endswith(".txt"):
                path = os.path.join(root, file)
                print(f"Processing: {path}")
                process_label_file(path)


if __name__ == "__main__":
    label_dir = r"E:\College Students' Innovative Entrepreneurial Training Plan Program\Dataset\yolo_format\labels"
    process_folder(label_dir)

    print("✅ 转换完成！")