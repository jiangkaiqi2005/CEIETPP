# 数据标注记录

## 历史标注方式

历史资料显示使用 LabelMe 标注，再转成 YOLO 格式。

历史输入目录写在转换脚本里：

```text
E:\College Students' Innovative Entrepreneurial Training Plan Program\Dataset\img\img-train
E:\College Students' Innovative Entrepreneurial Training Plan Program\Dataset\img\img-val
E:\College Students' Innovative Entrepreneurial Training Plan Program\Dataset\img\img-test

E:\College Students' Innovative Entrepreneurial Training Plan Program\Dataset\label\label-train
E:\College Students' Innovative Entrepreneurial Training Plan Program\Dataset\label\label-val
E:\College Students' Innovative Entrepreneurial Training Plan Program\Dataset\label\label-test
```

历史输出目录：

```text
E:\College Students' Innovative Entrepreneurial Training Plan Program\Dataset\yolo_format
```

## 历史类别

使用固定 7 类：

```text
flat_ground
rough_ground
stairs
obstacle_static
obstacle_dynamic
doorway
no_pass
```

## 标注质量提醒

历史标签中 8 坐标 polygon 数量最多，共 4370 个对象。这通常表示矩形 polygon，说明很多 segmentation mask 可能不是精细轮廓。

下一次训练前建议重点检查：

- `flat_ground`
- `rough_ground`
- `stairs`
- `no_pass`

这些类更影响机器人可通行判断，最好优先使用精细 polygon。
