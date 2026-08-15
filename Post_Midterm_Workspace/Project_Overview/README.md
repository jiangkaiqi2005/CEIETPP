# 项目总览

这个目录记录中期答辩后的统一项目状态。以后如果需要快速恢复思路，先看这里。

## 当前整理结果

项目现在分为两块：

```text
D:\CEIETPP\Pre_Midterm_Archive
D:\CEIETPP\Post_Midterm_Workspace
```

`Pre_Midterm_Archive` 是中期答辩前资料归档，里面保留了历史数据、历史脚本和历史训练输出。

`Post_Midterm_Workspace` 是中期答辩后的统一工作区。之后新的数据整理、训练命令、训练结果和 ROS 部署记录都应该放这里。

## 已确认的主线

中期答辩前的视觉识别主线不是单纯 YOLOv8 detection，而是：

```text
LabelMe 标注数据
-> labelme_to_yolo.py 转 YOLO 格式
-> YOLO26 segmentation 训练
-> coco_pretrain2
-> finetune1 / finetune2 / finetune3
-> ROS 使用 finetune3/best.pt
```

早期 `main\yolov8` 目录中确实有 YOLOv8 训练痕迹，但那条线使用的是 VOC 20 类 detection，不像最终项目权重来源。

## 当前需要注意

- 历史 `data.yaml` 仍然硬编码到旧路径 `E:\College Students' Innovative Entrepreneurial Training Plan Program\Dataset\yolo_format`。
- 历史 `finetune` 的 `data.yaml` 路径指向 `D:\CEIETPP\yolo-cocostuff\yolo_format\data.yaml`，但当前归档中没有看到这份文件。
- 历史标签里大量对象是 8 坐标 polygon，说明很多 segmentation mask 可能来自 bbox 转矩形 polygon。
- 当前文件整理后，历史权重位于 `D:\CEIETPP\Pre_Midterm_Archive\runs\segment\finetune3\weights\best.pt`。如果 ROS 配置仍然指向旧的 `D:\CEIETPP\runs\segment\finetune3\weights\best.pt`，需要后续单独处理。
