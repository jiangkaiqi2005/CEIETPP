# ROS 仿真部署

这个目录记录 WF_TRON1A + Gazebo + RGBD Camera + yolo_ros 的部署过程。

## 当前项目约束

- 机器人型号：`WF_TRON1A`。
- 主体坐标系：`base_Link`，注意大小写。
- YOLO debug 图像话题：`/yolo/dbg_image`。
- 当前权重是 YOLO segmentation 权重。

## 当前重点

`/yolo/detections` 和 `/yolo/tracking` 历史上已有真实输出，当前主要问题是：

```text
/yolo/detections_3d 不输出
```

修复方向必须保留 mask 精度：

```text
segmentation mask -> mask 内 depth 像素 -> 3D 检测结果
```

不要退化成：

```text
2D bbox -> bbox 内 depth 像素 -> 粗略 3D 检测结果
```
