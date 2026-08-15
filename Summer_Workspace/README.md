# 暑期工作区（Summer Workspace）

暑期集中进行数据集调研、筛选与模型训练实验的工作区。
本目录仅保留文档，所有数据集（warehouses、ADE20K、TartanGround、recon terrain dataset 等）及训练产物均已通过 `.gitignore` 排除，不入库。

## 数据集获取（网盘分享）

数据集 `Datasets` 已通过百度网盘分享：

- 链接：https://pan.baidu.com/s/1wpakcQsQiVQkwPQZ15H12A?pwd=uptm
- 提取码：uptm

## 数据集调研记录

- **warehouses**：数据集质量很好，但为视频格式，需要转换，且没有 `stairs`（楼梯）类别，考虑更换。
- **ADE20K**：很好，但不是机器人视角下的数据。
- **TartanGround**：仿真数据集，虽是机器人视角下的，但未采用。
- **recon terrain dataset**：很好，但工业场景味道不够强。
- **lab-ws-vrin-v1**：很好，但没有 `flat_ground`（平地）类别。

## 选择结论

2026-08-15 选择 **recon terrain dataset** 数据集，使用 YOLO26 进行训练。

## 训练结果

2026-08-15 使用 **recon terrain dataset** 完成 YOLO26 segmentation 训练（100/100 epoch）：

- 起始权重：`yolo26n-seg.pt`（官方预训练，已移至本目录）
- 训练参数：epochs=100、batch=16、imgsz=640、cls_remap=True
- 数据划分：train 1007 / valid 126 / test 126（17 类）
- 最佳指标（epoch 80）：mask mAP50-95 = 0.32412、mask mAP50 = 0.42759、box mAP50-95 = 0.3418、box mAP50 = 0.43528
- 训练产物：`runs/train/weights/best.pt`、`runs/train/weights/last.pt`（已入库）
- 训练记录：`runs/train/results.csv`、`runs/train/args.yaml`、`runs/train/labels.jpg`、`runs/train/train_batch*.jpg`
