# 笔记本关键信息

这个目录记录当前这台笔记本和历史上疑似在笔记本完成的数据整理工作。

## 当前这台电脑

只读检查结果：

| 项目 | 值 |
| --- | --- |
| 用户名 | `25330` |
| 机器名 | `JIANGKAIQI` |
| 用户目录 | `C:\Users\25330` |
| 当前项目目录 | `D:\CEIETPP` |
| 系统 | `Microsoft Windows 11 家庭版 中文版` |
| 系统版本 | `10.0.26200` |
| PowerShell | `5.1.26100.8655` |
| 时区 | `China Standard Time` |
| 可见 Python 命令 | `C:\Users\25330\AppData\Local\Microsoft\WindowsApps\python.exe`; `E:\Anaconda\python.exe` |
| 可见 Git 命令 | `D:\Git\Git\cmd\git.exe` |

以上只是记录当前环境信息，没有修改系统环境。

## 历史推断

笔记本更像承担了“数据标注和整理”的工作，依据是：

- `labelme_to_yolo.py` 和 `data.yaml` 都硬编码到 `E:\College Students' Innovative Entrepreneurial Training Plan Program\Dataset`。
- 历史数据目录中存在 LabelMe 到 YOLO 的转换脚本和使用教程。
- `main\Dataset\yolo_format` 和 `finish-data\Dataset\yolo_format` 都是整理好的 7 类 YOLO 数据集。

这个推断不是百分百事实；实验室电脑上也可能拷贝过同一套数据。
