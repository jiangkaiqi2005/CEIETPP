# 类别定义

历史数据集使用 7 类。类别顺序来自：

```text
D:\CEIETPP\Pre_Midterm_Archive\main\Dataset\yolo_format\data.yaml
D:\CEIETPP\Pre_Midterm_Archive\main\labelme_to_yolo.py
```

| ID | Class | 历史说明 | 推荐标注方式 |
| --- | --- | --- | --- |
| 0 | flat_ground | 平地，走廊、厂房、通道地面等 | polygon |
| 1 | rough_ground | 粗糙地面 | polygon |
| 2 | stairs | 楼梯 | polygon |
| 3 | obstacle_static | 箱子、设备、货架、桌椅、柱子、杂物等静态障碍 | bbox 或 polygon |
| 4 | obstacle_dynamic | 行人、移动物体等动态障碍 | bbox 或 polygon |
| 5 | doorway | 门口 | bbox 或 polygon |
| 6 | no_pass | 坑洞、危险区等不可通过区域 | polygon |

## 注意

- 类别顺序不能随便变。只要训练集、验证集、测试集或 ROS 侧使用旧权重，就必须保持这个顺序。
- 历史数据里很多对象是 8 坐标 polygon，通常表示矩形 mask。它能让 segmentation 训练跑起来，但不等于精细轮廓。
- 下一次训练如果强调 3D 检测和可通行区域，`flat_ground`、`rough_ground`、`stairs`、`no_pass` 更应该使用精细 polygon。
