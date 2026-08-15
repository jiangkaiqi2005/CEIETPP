# 训练环境记录

## 已从历史文件确认

历史训练参数中均出现：

```text
device: 0
batch: 16
imgsz: 640
task: segment
```

这说明 YOLO26 segmentation 主线使用了第 0 块 GPU 训练。

## 当前缺失

历史文件中没有完整记录以下信息：

- 实验室电脑显卡型号。
- NVIDIA Driver 版本。
- CUDA 版本。
- cuDNN 版本。
- PyTorch 版本。
- ultralytics 版本。
- Python 环境名。

## 下次去实验室电脑需要补

建议执行只读检查命令，并把输出粘贴到这里：

```powershell
nvidia-smi
python --version
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available()); print(torch.version.cuda)"
python -c "import ultralytics; print(ultralytics.__version__)"
```
