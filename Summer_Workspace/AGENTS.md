# Summer Workspace 训练规范

本目录是暑期集中进行数据集调研、筛选与模型训练实验的工作区。

## 训练输出目录

- 训练输出统一放在 `Summer_Workspace/runs/` 下；`runs` 是 YOLO 标准输出目录名，**不要改名**。
- 每个模块/版本一个子目录，命名 `模块名_版本号`，如 `recon_v0.1.0`、`detect_v0.1`、`seg_v0.2`。
- 训练时用 `project=Summer_Workspace/runs name=<模块名_版本>` 指定输出位置。

## 训练记录

- 每次训练完成后，必须在 `Summer_Workspace/README.md` 的「训练结果」下按模板追加记录（版本号、日期、起始权重、训练参数、数据划分、最佳指标、产物路径、结论）。

## 入库与忽略

- 训练产物（权重、results.csv、args.yaml、曲线图等）入库；`.gitignore` 已放行 `Summer_Workspace/runs/**`，新训练产物会自动入库，不要新增忽略规则。
- 数据集不入库（.gitignore 排除），通过百度网盘分享获取（链接与提取码见 `Summer_Workspace/README.md`）。
