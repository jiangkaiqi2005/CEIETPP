# CEIETPP 总说明

这个目录分为两部分：

```text
D:\CEIETPP
├─ Pre_Midterm_Archive\
└─ Post_Midterm_Workspace\
```

`Pre_Midterm_Archive` 用来保留中期答辩前的历史资料，包括旧数据、旧训练结果、旧脚本和流程总结。

`Post_Midterm_Workspace` 用来放中期答辩后的统一资料。之后新的数据整理、YOLO 训练、权重对比和 ROS 仿真部署都放这里。

根目录下的 `.codex`、`.agents`、`AGENTS.md` 是工程和工具相关文件，不作为资料目录整理。
```text
D:\CEIETPP  # 项目根目录
├─ Pre_Midterm_Archive\  # 中期答辩前资料，原样保留，不直接修改
│  ├─ Pre_Midterm_Workflow.md  # 中期答辩前大致流程
│  ├─ main\  # 原 main 文件夹
│  ├─ finish-data\  # 原 finish-data 文件夹
│  ├─ yolo-cocostuff\  # 原公开数据/COCO 相关文件夹
│  ├─ runs\  # 原训练结果与权重
│  └─ README_Do_Not_Edit_Directly.md  # 说明这部分只做历史保留
│
├─ Post_Midterm_Workspace\  # 中期答辩后统一工作区
│  ├─ Project_Overview\  # 项目总览
│  │  ├─ README.md  # 总说明
│  │  ├─ Current_Goals.md  # 当前目标
│  │  ├─ Class_Definitions.md  # 类别定义
│  │  └─ Path_Conventions.md  # 路径约定
│  │
│  ├─ Laptop_Key_Info\  # 笔记本关键信息
│  │  ├─ README.md  # 本目录说明
│  │  ├─ Data_Collection_Log.md  # 数据采集记录
│  │  ├─ Annotation_Log.md  # 数据标注记录
│  │  ├─ LabelMe_to_YOLO_Log.md  # LabelMe 转 YOLO 记录
│  │  └─ Laptop_Environment_and_Paths.md  # 本机环境与路径
│  │
│  ├─ Lab_PC_Key_Info\  # 实验室电脑关键信息
│  │  ├─ README.md  # 本目录说明
│  │  ├─ Training_Environment.md  # 训练环境记录
│  │  ├─ Training_Commands.md  # 训练命令记录
│  │  ├─ GPU_CUDA_Python.md  # 显卡、CUDA、Python 记录
│  │  └─ Lab_PC_Paths.md  # 实验室电脑路径
│  │
│  ├─ Datasets\  # 数据集
│  │  ├─ README.md  # 数据集总说明
│  │  ├─ v1_Pre_Midterm_Reproduction\  # 中期答辩前复现版
│  │  ├─ v2_Next_Training\  # 下一次训练版
│  │  ├─ Self_Annotated_Data\  # 自己标注数据
│  │  ├─ Public_Datasets\  # 网上公开数据
│  │  └─ Dataset_Split.md  # 数据划分说明
│  │
│  ├─ Training_Code_and_Config\  # 训练代码与配置
│  │  ├─ README.md  # 本目录说明
│  │  ├─ data_yaml_backups\  # data.yaml 备份
│  │  └─ command_backups\  # 训练命令备份
│  │
│  ├─ Training_Results_and_Weights\  # 训练结果与权重
│  │  ├─ README.md  # 本目录说明
│  │  ├─ Historical_Weights_Comparison.md  # 历史权重对比
│  │  ├─ New_Training_Results\  # 新训练结果
│  │  └─ Current_ROS_Weight\  # 当前 ROS 使用权重
│  │
│  ├─ ROS_Simulation_Deployment\  # ROS 仿真部署
│  │  ├─ README.md  # 本目录说明
│  │  ├─ WSL_Paths.md  # WSL 路径记录
│  │  ├─ yolo_ros_Launch_Commands.md  # yolo_ros 启动命令
│  │  ├─ Topic_Check_Log.md  # topic 检查记录
│  │  └─ detect_3d_node_Issues.md  # detect_3d_node 问题记录
│
└─ README_Overview.md  # 总说明
```
