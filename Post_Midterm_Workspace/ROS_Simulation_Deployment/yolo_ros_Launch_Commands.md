# yolo_ros 启动命令

这里记录 yolo_ros 相关启动命令。

## 环境注意

启动 YOLO 节点前需要：

```bash
source ~/yolo_ws/src/yolo_ros/.venv/bin/activate
```

并把 `.venv` 的 site-packages 加进 `PYTHONPATH`，否则可能找不到 `torch` 或 `ultralytics`。

运行 `rqt_image_view`、`rviz2` 时不要激活 YOLO venv，也不要保留 YOLO 的 `PYTHONPATH`。

## 需要后续补充

这里还缺实际可复用的启动命令。下次成功启动后建议记录：

- Gazebo 启动命令。
- RGBD Camera topic 检查命令。
- yolo_ros 启动命令。
- 使用的权重路径。
- 成功输出的 topic。
