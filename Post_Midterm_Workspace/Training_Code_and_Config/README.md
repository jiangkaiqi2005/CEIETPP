# 训练代码与配置

这个目录用于放中期答辩后的训练脚本、验证脚本、`data.yaml` 备份和训练命令备份。

## 历史训练脚本

YOLO26 segmentation 历史脚本：

```text
D:\CEIETPP\Pre_Midterm_Archive\main\yolov26-CSIETPP\main.py
```

核心逻辑：

```python
model = YOLO("yolo26n-seg.pt")
model.train(
    data=r"E:/College Students' Innovative Entrepreneurial Training Plan Program/Dataset/yolo_format/data.yaml",
    epochs=100,
    imgsz=640,
    batch=16,
    device=0,
    degrees=5,
    mixup=0.2,
    shear=2,
    patience=30,
)
```

## 历史辅助脚本

```text
D:\CEIETPP\Pre_Midterm_Archive\main\labelme_to_yolo.py
D:\CEIETPP\Pre_Midterm_Archive\main\yolov26-CSIETPP\bbox_to_polygon.py
```

`bbox_to_polygon.py` 会覆盖写回 label 文件。以后使用前必须先备份标签。

## 下一次训练脚本原则

- 不再硬编码旧的 `E:\College Students' Innovative Entrepreneurial Training Plan Program`。
- `data.yaml` 使用当前 `Post_Midterm_Workspace\Datasets\v2_Next_Training`。
- 每次训练前把完整命令写入 `command_backups`。
- 每次训练使用的 `data.yaml` 复制到 `data_yaml_backups`。
