# LabelMe 转 YOLO 记录

## 历史转换脚本

```text
D:\CEIETPP\Pre_Midterm_Archive\main\labelme_to_yolo.py
D:\CEIETPP\Pre_Midterm_Archive\finish-data\labelme_to_yolo.py
```

两处脚本看起来是同一套用途：把 LabelMe JSON 转成 YOLO 格式。

## 转换逻辑

脚本支持：

- LabelMe `rectangle` 转 YOLO bbox：`class x_center y_center width height`
- LabelMe `polygon` 转 YOLO segmentation polygon：`class x1 y1 x2 y2 ...`
- 生成 `data.yaml`
- 复制图片到 `images/train`、`images/val`、`images/test`
- 生成标签到 `labels/train`、`labels/val`、`labels/test`

## 固定类别映射

| ID | Class |
| --- | --- |
| 0 | flat_ground |
| 1 | rough_ground |
| 2 | stairs |
| 3 | obstacle_static |
| 4 | obstacle_dynamic |
| 5 | doorway |
| 6 | no_pass |

## 额外脚本

历史中还有：

```text
D:\CEIETPP\Pre_Midterm_Archive\main\yolov26-CSIETPP\bbox_to_polygon.py
```

它会把 YOLO bbox 转成 4 点矩形 polygon，并覆盖写回 label 文件。这个脚本解释了为什么历史标签里有大量 8 坐标 polygon。

注意：这个脚本适合让 segmentation 训练能跑起来，但不等于生成了真实精细 mask。
