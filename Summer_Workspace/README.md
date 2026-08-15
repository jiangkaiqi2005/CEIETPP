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


### 使用recon terrain dataset

#### v0.1.0：2026.8.15
2026-08-15 使用 **recon terrain dataset** 完成 YOLO26 segmentation 训练（100/100 epoch）：

- 起始权重：`yolo26n-seg.pt`（官方预训练，已移至本目录）
- 训练参数：epochs=100、batch=16、imgsz=640、cls_remap=True
- 数据划分：train 1007 / valid 126 / test 126（17 类）
- 最佳指标（epoch 80）：mask mAP50-95 = 0.32412、mask mAP50 = 0.42759、box mAP50-95 = 0.3418、box mAP50 = 0.43528
- 训练产物：`runs/recon_v0.1.0/weights/best.pt`、`runs/recon_v0.1.0/weights/last.pt`（已入库）
- 训练记录：`runs/recon_v0.1.0/results.csv`、`runs/recon_v0.1.0/args.yaml`、`runs/recon_v0.1.0/labels.jpg`、`runs/recon_v0.1.0/train_batch*.jpg`


训练结果不好，数据太少了。


## 训练目录与记录约定

训练输出统一放在 `runs/` 下（`runs` 是 YOLO 标准输出目录名，不改名），每个模块/版本一个子目录：

```text
runs/
├── recon_v0.1.0/    # 模块名_版本号
├── detect_v0.1/     # 以后新模块
└── seg_v0.2/        # 以后新版本
```

训练时通过 `project` + `name` 指定输出位置：

```bash
yolo segment train data=<data.yaml> model=<起始权重>     project=Summer_Workspace/runs name=recon_v0.1.0
```

每次训练完成后，在「训练结果」下按以下模板追加记录：

```markdown
### 使用 <数据集名>

#### v0.x.y：<日期>
- 起始权重：
- 训练参数：
- 数据划分：
- 最佳指标：
- 训练产物：`runs/<模块名_版本>/weights/best.pt`（已入库）
- 训练记录：`runs/<模块名_版本>/results.csv`、`args.yaml`
- 结论：
```

`.gitignore` 已放行整个 `Summer_Workspace/runs/`，新训练产物会自动入库，无需再改配置。
