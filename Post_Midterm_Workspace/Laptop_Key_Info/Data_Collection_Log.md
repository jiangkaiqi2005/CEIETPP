# 数据采集记录

## 已从历史文件确认的内容

历史数据集最终进入了 YOLO 格式目录：

```text
D:\CEIETPP\Pre_Midterm_Archive\main\Dataset\yolo_format
D:\CEIETPP\Pre_Midterm_Archive\finish-data\Dataset\yolo_format
```

两份目录内容规模一致：

| split | images | labels | objects |
| --- | ---: | ---: | ---: |
| train | 1217 | 1217 | 5487 |
| val | 38 | 38 | 244 |
| test | 216 | 216 | 770 |
| total | 1471 | 1471 | 6501 |

## 当前不能完全确认的内容

- 哪些图片是你自己拍的。
- 哪些图片是公开数据。
- 哪些图片是 Roboflow 导出或增强后的图片。
- 原始采集日期和地点。

## 后续补充方式

以后新增自己采集数据时，建议按这个格式记录：

| 日期 | 地点 | 设备 | 原始路径 | 场景 | 是否标注 | 是否进入训练 |
| --- | --- | --- | --- | --- | --- | --- |
| 待补 | 待补 | 待补 | 待补 | 待补 | 待补 | 待补 |
