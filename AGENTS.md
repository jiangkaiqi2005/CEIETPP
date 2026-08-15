# 项目背景

我在做大创项目。团队任务是开发一个轮足机器人，我负责视觉识别部分。

## 当前任务

- 使用已经训练好的 YOLO segmentation 权重做仿真识别。
- 权重路径：`D:\CEIETPP\runs\segment\finetune3\weights\best.pt`
- WSL 路径：`/mnt/d/CEIETPP/runs/segment/finetune3/weights/best.pt`
- 当前主线：在 WF_TRON1A + Gazebo + RGBD Camera 中运行 `yolo_ros`，输出 `/yolo/detections`、`/yolo/tracking`、`/yolo/detections_3d`。
- 后续目标：`/yolo/detections_3d` 稳定后，再接 Nav2 adapter。

## 环境

- 主机：Windows
- WSL：Ubuntu 22.04、Ubuntu 24.04
- 当前仿真优先用：Ubuntu 22.04 WSL
- ROS：ROS 2 Iron
- 仿真：Gazebo Classic
- 机器人型号：`WF_TRON1A`
- limx 工作区：`~/limx_ws`
- YOLO ROS 工作区：`~/yolo_ws`

## 关键约束

- 使用 `export ROBOT_TYPE=WF_TRON1A`，不要用 `PF_TRON1A`。
- 主体坐标系是 `base_Link`，不是 `base_link`，大小写不能错。
- YOLO debug 图像话题是 `/yolo/dbg_image`，不是 `/yolo/debug_image`。
- 运行 `rqt_image_view`、`rviz2` 时不要激活 YOLO venv，也不要保留 YOLO 的 `PYTHONPATH`。
- 启动 YOLO 节点前必须激活 `~/yolo_ws/src/yolo_ros/.venv`，并把 `.venv` 的 site-packages 加进 `PYTHONPATH`，否则可能找不到 `torch` 或 `ultralytics`。

## 提交规范

- 提交信息（标题与描述）一律用中文书写。
- 提交与推送时不得添加 `Co-Authored-By` 等协助者署名。

## 当前状态

已完成：

- Gazebo 能启动 WF_TRON1A。
- RGBD 相机已接入，RGB、Depth、CameraInfo、PointCloud 话题存在。
- `yolo_ros` 已能加载 segmentation 权重。
- `/yolo/detections` 和 `/yolo/tracking` 已有真实输出。
- segmentation mask 已经正常输出。

当前问题：

- `/yolo/detections_3d` 不输出。
- 主要原因是 `/yolo/detect_3d_node` 会崩溃。
- depth 图像和 depth camera info 已确认正常，问题优先看 `detect_3d_node.py` 的 mask + depth 处理逻辑。

## 修复方向

当前权重是 YOLO segmentation，修 3D 检测时要保留 mask 精度：

```text
segmentation mask -> mask 内 depth 像素 -> 3D 检测结果
```

不要退化成：

```text
2D bbox -> bbox 内 depth 像素 -> 粗略 3D 检测结果
```

不要通过禁用 mask 分支来绕过问题，例如不要改成 `if False and detection.mask.data:`。

推荐方向：让 `detect_3d_node.py` 的 mask 分支只取 mask 内部 depth，并保证 depth 值数组和像素坐标长度一致：

```python
roi = depth_image[y_coords, x_coords]
pixel_coords = np.column_stack([x_coords, y_coords])
```

详细运行手册和长版项目上下文在：

```text
E:\Backup\Note\大创\WF_TRON1A_Gazebo_YOLO_ROS_项目上下文.md
```
