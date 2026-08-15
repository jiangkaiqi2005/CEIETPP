# 中期答辩前大致流程

结论：上次不是单纯“YOLOv8 直接训练”，而是经历了几条线，最后真正用于 ROS 的是 YOLO26 segmentation 权重。

## 大致流程

1. 你先在 `E:\College Students' Innovative Entrepreneurial Training Plan Program\Dataset` 这套目录里整理/标注数据，再用 [labelme_to_yolo.py](D:/CEIETPP/main/labelme_to_yolo.py:30) 把 LabelMe 的 JSON 转成 YOLO 格式。

   当前副本在 [main/Dataset/yolo_format/data.yaml](D:/CEIETPP/main/Dataset/yolo_format/data.yaml:18)，类别是 7 类：`flat_ground`、`rough_ground`、`stairs`、`obstacle_static`、`obstacle_dynamic`、`doorway`、`no_pass`。

2. `main/Dataset/yolo_format` 和 `finish-data/Dataset/yolo_format` 完全一样：

   训练集 1217 张，验证集 38 张，测试集 216 张，共 6501 个标注对象。

3. 网上数据线索主要来自两个 Word 文档：Roboflow 的 Terrain Detection、Land Cover Classification YOLO，以及 COCO。磁盘上也确实有 `yolo-cocostuff`，大约 14587 张 train、5000 张 val、28093 个标签文件，111216 个对象。

4. 早期 `main/yolov8` 里有 YOLOv8 检测实验，但那是 VOC 20 类检测：`weights/yolov8s.pt`、`VOC-test.yaml`、`C:\Users\Administrator\Desktop\yolov8...`。这条线不像最终项目权重。

5. 最终训练在 [runs/segment](D:/CEIETPP/runs/segment) 下：

   `yolo26n-seg.pt` 先做 `coco_pretrain2` 30 epoch，然后用 `runs/segment/coco_pretrain2/weights/best.pt` 做 `finetune1/2/3`。当前 ROS 用的是 [finetune3/best.pt](D:/CEIETPP/runs/segment/finetune3/weights/best.pt)。

## 两台电脑协作的推断

你的笔记本更像是“标注/整理数据”的机器，因为脚本和 `data.yaml` 都硬编码到 `E:\College Students' Innovative Entrepreneurial Training Plan Program\...`。

实验室电脑更像是“训练”的机器，因为训练输出里出现了 `D:\CEIETPP\yolo-cocostuff\...`，旧 YOLOv8 线还出现了 `C:\Users\Administrator\Desktop\yolov8` 和 `E:\Yolo\YoloStudy\...`。

## 几个重要问题

- 现在缺了当时 `finetune` 用的 `D:\CEIETPP\yolo-cocostuff\yolo_format\data.yaml`，所以不能 100% 复刻当时训练集。
- 当前文件夹也没有 `yolo26n-seg.pt` 原始 segmentation 权重，只看到 `yolo26n.pt` 检测权重。
- [bbox_to_polygon.py](D:/CEIETPP/main/yolov26-CSIETPP/bbox_to_polygon.py:59) 会把 bbox 变成矩形 polygon。当前标签里大量对象是 8 坐标矩形 mask，这能让 segmentation 训练跑起来，但很多 mask 其实不是精细轮廓。
- 从结果看，`finetune1` 的最佳 mask mAP50-95 是 `0.35459`，`finetune3` 是 `0.32358`。如果没有别的取舍理由，`finetune1` 反而值得重新拿出来对比。

## 下一次训练前建议

下一次训练前，建议先重建一个明确的数据版本：

- 公开数据只放 train。
- 你自己标注的数据单独做 val/test。
- 把 `data.yaml` 改成当前真实路径。
- 确认哪些类必须要精细 mask，别再无差别把框转矩形 mask。
