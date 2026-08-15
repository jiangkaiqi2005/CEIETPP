# 训练命令记录

## YOLO26 segmentation 主线

历史训练输出位于：

```text
D:\CEIETPP\Pre_Midterm_Archive\runs\segment
```

### coco_pretrain

```text
task: segment
model: yolo26n-seg.pt
data: coco_converted.yaml
epochs: 30
batch: 16
imgsz: 640
device: 0
save_dir: D:\CEIETPP\yolo-cocostuff\runs\segment\coco_pretrain
```

当前归档中只看到 `args.yaml`，没有对应 `results.csv`。

### coco_pretrain2

```text
task: segment
model: yolo26n-seg.pt
data: data.yaml
epochs: 30
batch: 16
imgsz: 640
device: 0
save_dir: D:\CEIETPP\yolo-cocostuff\runs\segment\coco_pretrain2
```

最佳结果：

| 指标 | 最佳值 | epoch |
| --- | ---: | ---: |
| box mAP50 | 0.34789 | 30 |
| box mAP50-95 | 0.23427 | 30 |
| mask mAP50 | 0.33803 | 30 |
| mask mAP50-95 | 0.20891 | 30 |

### finetune1

```text
task: segment
model: runs/segment/coco_pretrain2/weights/best.pt
data: D:\CEIETPP\yolo-cocostuff\yolo_format\data.yaml
epochs: 100
patience: 30
batch: 16
imgsz: 640
device: 0
degrees: 10
translate: 0.1
scale: 0.5
shear: 2
mixup: 0.2
copy_paste: 0.0
save_dir: D:\CEIETPP\yolo-cocostuff\runs\segment\finetune
```

最佳结果：

| 指标 | 最佳值 | epoch |
| --- | ---: | ---: |
| box mAP50 | 0.57311 | 20 |
| box mAP50-95 | 0.36724 | 64 |
| mask mAP50 | 0.57559 | 20 |
| mask mAP50-95 | 0.35459 | 64 |

### finetune2

```text
task: segment
model: runs/segment/coco_pretrain2/weights/best.pt
data: D:\CEIETPP\yolo-cocostuff\yolo_format\data.yaml
epochs: 150
patience: 30
batch: 16
imgsz: 640
device: 0
freeze: 10
degrees: 10
translate: 0.2
scale: 0.7
shear: 2
mixup: 0.3
copy_paste: 0.3
save_dir: D:\CEIETPP\yolo-cocostuff\runs\segment\finetune2
```

最佳 mask mAP50-95：`0.31277`，epoch `107`。

### finetune3

```text
task: segment
model: runs/segment/coco_pretrain2/weights/best.pt
data: D:\CEIETPP\yolo-cocostuff\yolo_format\data.yaml
epochs: 150
patience: 30
batch: 16
imgsz: 640
device: 0
freeze: 10
degrees: 10
translate: 0.1
scale: 0.5
shear: 2
mixup: 0.2
copy_paste: 0.2
save_dir: D:\CEIETPP\yolo-cocostuff\runs\segment\finetune3
```

最佳 mask mAP50-95：`0.32358`，epoch `86`。

## 早期 YOLOv8 detection 线

这条线不像最终 ROS 权重来源。

```text
task: detect
model: weights/yolov8s.pt
data: ultralytics/cfg/datasets/VOC-test.yaml
epochs: 100
```

`train`：batch 8，imgsz 320，save_dir 为 `E:\Yolo\YoloStudy\src\yolov8\runs\detect\train`。

`train3`：batch 32，imgsz 640，save_dir 为 `runs\detect\train3`。
