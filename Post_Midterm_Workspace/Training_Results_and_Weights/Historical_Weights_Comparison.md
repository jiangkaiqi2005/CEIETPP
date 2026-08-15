# 历史权重对比

## 结果汇总

| run | 起始权重 | epochs 设置 | 实际记录 epoch 数 | 最佳 box mAP50-95 | 最佳 mask mAP50-95 | 备注 |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| coco_pretrain | yolo26n-seg.pt | 30 | 无 results.csv | 无 | 无 | 只看到 args.yaml |
| coco_pretrain2 | yolo26n-seg.pt | 30 | 30 | 0.23427 | 0.20891 | 后续 finetune 起点 |
| finetune1 | coco_pretrain2/best.pt | 100 | 94 | 0.36724 | 0.35459 | 历史最佳 mask mAP50-95 最高 |
| finetune2 | coco_pretrain2/best.pt | 150 | 107 | 0.32011 | 0.31277 | freeze 10，增强更强 |
| finetune3 | coco_pretrain2/best.pt | 150 | 87 | 0.33096 | 0.32358 | 当前 ROS 历史使用 |

## 关键结论

从 `results.csv` 指标看，`finetune1` 的最佳 mask mAP50-95 是 `0.35459`，高于 `finetune3` 的 `0.32358`。

但这不一定直接说明 `finetune1` 在仿真里更好，因为：

- 需要确认验证集是否代表机器人场景。
- 需要看实际 Gazebo / RGBD 画面识别效果。
- 需要确认不同权重在同一测试集上的输出。

## 下一步建议

把 `finetune1` 和 `finetune3` 放到同一批仿真截图或视频上跑一次，对比：

- mask 是否贴合地面、楼梯、障碍物。
- 类别是否稳定。
- 置信度是否过低或误检过多。
- 对 `/yolo/detections_3d` 是否有影响。
