# 当前 ROS 使用权重

## 历史权重

中期答辩前项目上下文记录的 ROS 权重是：

```text
D:\CEIETPP\runs\segment\finetune3\weights\best.pt
```

文件整理后，历史权重归档位置是：

```text
D:\CEIETPP\Pre_Midterm_Archive\runs\segment\finetune3\weights\best.pt
```

对应 WSL 路径应为：

```text
/mnt/d/CEIETPP/Pre_Midterm_Archive/runs/segment/finetune3/weights/best.pt
```

## 注意

如果 ROS 启动文件或命令仍然引用旧路径：

```text
/mnt/d/CEIETPP/runs/segment/finetune3/weights/best.pt
```

整理目录后这个路径可能已经不存在。后续运行仿真前需要单独检查权重路径。

## 候选权重

- `finetune3/best.pt`：当前 ROS 历史使用。
- `finetune1/best.pt`：历史指标更好，建议重新对比。
