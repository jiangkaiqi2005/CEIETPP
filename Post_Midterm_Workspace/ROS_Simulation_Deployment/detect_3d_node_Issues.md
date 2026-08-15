# detect_3d_node 问题记录

## 当前问题

```text
/yolo/detections_3d 不输出
```

历史上下文判断：`/yolo/detect_3d_node` 会崩溃，depth 图像和 depth camera info 已确认正常，问题优先看 mask + depth 处理逻辑。

## 正确方向

当前权重是 YOLO segmentation，3D 检测应该使用 mask 内部的 depth 像素：

```text
segmentation mask -> mask 内 depth 像素 -> 3D 检测结果
```

推荐处理思路：

```python
roi = depth_image[y_coords, x_coords]
pixel_coords = np.column_stack([x_coords, y_coords])
```

## 不建议的方向

不要为了让 3D 结果出来而禁用 mask 分支，例如不要改成：

```python
if False and detection.mask.data:
```

也不要退化成：

```text
2D bbox -> bbox 内 depth 像素 -> 粗略 3D 检测结果
```

这样会损失 segmentation 在地面、楼梯、不可通行区域上的精度。
