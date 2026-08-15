# 暑期工作区（Summer Workspace）

暑期集中进行数据集调研、筛选与模型训练实验的工作区。
本目录仅保留文档，所有数据集（warehouses、ADE20K、TartanGround、recon terrain dataset 等）及训练产物均已通过 `.gitignore` 排除，不入库。

## 数据集调研记录

- **warehouses**：数据集质量很好，但为视频格式，需要转换，且没有 `stairs`（楼梯）类别，考虑更换。
- **ADE20K**：很好，但不是机器人视角下的数据。
- **TartanGround**：仿真数据集，虽是机器人视角下的，但未采用。
- **recon terrain dataset**：很好，但工业场景味道不够强。
- **lab-ws-vrin-v1**：很好，但没有 `flat_ground`（平地）类别。

## 选择结论

2026-08-15 选择 **recon terrain dataset** 数据集，使用 YOLO26 进行训练。
