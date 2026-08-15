# 新训练结果

这里放中期答辩后的新训练输出。

## 建议目录命名

```text
YYYYMMDD_yolo26_seg_coco_pretrain
YYYYMMDD_yolo26_seg_finetune_v2
```

## 每次训练建议保留

- `args.yaml`
- `results.csv`
- `weights\best.pt`
- `weights\last.pt`
- 训练曲线图片
- 验证 batch 图片
- 混淆矩阵
- 自己写的训练说明 Markdown

## 训练说明至少写清楚

- 数据集版本。
- 训练机器。
- 起始权重。
- 训练命令。
- 主要指标。
- 为什么选择这个 `best.pt`。
- 是否已经在 ROS / Gazebo 里测试。
