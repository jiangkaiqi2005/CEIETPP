# 当前目标

## 近期目标

1. 保留中期答辩前资料，不再在历史目录里继续修改数据和训练结果。
2. 用 `Post_Midterm_Workspace` 重新建立下一次训练的数据、配置和结果记录。
3. 明确区分自己标注数据和公开数据。
4. 重新训练 YOLO segmentation，并对比历史 `finetune1`、`finetune3` 权重。
5. 在 ROS 仿真中继续使用 segmentation mask 做 3D 检测，不退化成 bbox 深度估计。

## 下一次训练前必须确认

- `v2_Next_Training` 里到底放哪些图片和标签。
- `data.yaml` 使用真实存在的路径。
- 公开数据是否只进入 train。
- 自己标注数据是否单独作为 val/test。
- 是否继续使用 7 类：`flat_ground`、`rough_ground`、`stairs`、`obstacle_static`、`obstacle_dynamic`、`doorway`、`no_pass`。
- 哪些类必须重新做精细 polygon mask。

## 当前权重参考

历史 ROS 权重归档路径：

```text
D:\CEIETPP\Pre_Midterm_Archive\runs\segment\finetune3\weights\best.pt
```

历史结果提示：`finetune1` 的最佳 mask mAP50-95 高于 `finetune3`，下一次不要只凭“现在 ROS 在用 finetune3”来判断哪个权重更好。
