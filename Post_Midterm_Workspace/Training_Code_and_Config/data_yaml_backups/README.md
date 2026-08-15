# data.yaml 备份

这里保存每次训练使用的 `data.yaml`。

## 历史 data.yaml

历史 7 类数据配置位于：

```text
D:\CEIETPP\Pre_Midterm_Archive\main\Dataset\yolo_format\data.yaml
D:\CEIETPP\Pre_Midterm_Archive\finish-data\Dataset\yolo_format\data.yaml
```

历史内容要点：

```yaml
path: E:\College Students' Innovative Entrepreneurial Training Plan Program\Dataset\yolo_format
train: images/train
val: images/val
test: images/test
nc: 7
```

类别：

```text
flat_ground
rough_ground
stairs
obstacle_static
obstacle_dynamic
doorway
no_pass
```

## 备份命名建议

```text
YYYYMMDD_dataset_version_data.yaml
```

不要只保存最新一份，否则以后无法复现具体训练。
