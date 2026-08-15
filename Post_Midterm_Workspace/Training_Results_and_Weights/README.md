# 训练结果与权重

这个目录用于保存中期答辩后的训练输出、权重和权重对比。

## 历史结果位置

```text
D:\CEIETPP\Pre_Midterm_Archive\runs\segment
```

包含：

```text
coco_pretrain
coco_pretrain2
finetune1
finetune2
finetune3
```

## 当前判断

- `coco_pretrain2` 是 YOLO26 segmentation 的公开数据/COCO 风格预训练结果。
- `finetune1`、`finetune2`、`finetune3` 是基于 `coco_pretrain2\weights\best.pt` 的后续微调。
- 当前 ROS 历史使用的是 `finetune3\weights\best.pt`。
- 但从历史结果看，`finetune1` 的最佳 mask mAP50-95 更高。

## 后续规则

- 新训练结果放 `New_Training_Results`。
- 当前准备给 ROS 使用的权重放 `Current_ROS_Weight`。
- 每个权重必须写清楚来源数据、训练参数、验证指标和仿真表现。
