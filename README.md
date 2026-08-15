# CEIETPP (大学生创新训练项目 - 轮足机器人视觉感知系统)

本项目为大学生创新训练计划（大创）项目——**面向轮足机器人的视觉识别与环境感知系统**。  
核心任务是基于 **YOLO 实例分割（Segmentation）** 与 **RGB-D 深度相机**，实现高精度的可通行区域分割、地面地形识别以及 3D 目标与障碍物检测，为后续自主导航堆栈（如 Nav2）提供语义与几何感知支撑。

---

## 📌 目录与工作区架构

仓库采用清晰的阶段化归档与工作区划分：

```text
CEIETPP/
├── Pre_Midterm_Archive/              # 中期答辩前历史资料归档（基线模型、历史脚本与流程记录）
│   ├── finish-data/                  # 前期标注与数据转换工具
│   ├── main/                         # 前期训练与数据集汇总
│   ├── Pre_Midterm_Workflow.md       # 中期答辩前完整流程梳理
│   └── README_Do_Not_Edit_Directly.md
│
├── Post_Midterm_Workspace/           # 中期答辩后规范化统一工作区
│   ├── Project_Overview/             # 项目总览、目标规划、类别定义与路径约定
│   ├── Datasets/                     # 数据集管理（公开数据集、自建标注、划分规范）
│   ├── Training_Code_and_Config/     # YOLO 训练脚本与 data.yaml 备份
│   ├── Training_Results_and_Weights/ # 模型权重对比与 ROS 部署权重记录
│   ├── ROS_Simulation_Deployment/    # ROS 2 仿真部署、节点调试与 Topic 验证记录
│   ├── Laptop_Key_Info/              # 本机采集与标注记录
│   └── Lab_PC_Key_Info/              # 实验室 GPU 训练环境与命令记录
│
├── AGENTS.md                         # AI 协作与关键开发约束配置
├── README_Overview.md                # 目录整理总览
├── .gitignore                        # 数据集、模型权重及大型媒介忽略配置
└── README.md                         # 项目主说明文档
```

> **说明**：为了保证 Git 仓库的轻量与高效，所有原始大图、公开数据集切片、训练产物及模型权重（`*.pt`）均已通过 `.gitignore` 排除，仅保留核心源码、配置文件与文档。

---

## 🎯 语义感知类别定义

当前视觉模型采用 7 类语义目标检测与实例分割（保持统一类别顺序）：

| Class ID | 类别名称 (`Class`) | 语义说明 | 推荐标注形式 |
| :---: | :--- | :--- | :--- |
| **0** | `flat_ground` | 平地（走廊、大厅、通道等平坦地面） | 精细 Polygon |
| **1** | `rough_ground` | 粗糙地面（草地、碎石等非平整路面） | 精细 Polygon |
| **2** | `stairs` | 楼梯（台阶、台阶边缘） | 精细 Polygon |
| **3** | `obstacle_static` | 静态障碍（箱子、设备、货架、桌椅、立柱等） | BBox / Polygon |
| **4** | `obstacle_dynamic` | 动态障碍（行人、移动推车等） | BBox / Polygon |
| **5** | `doorway` | 门口 / 通道入口 | BBox / Polygon |
| **6** | `no_pass` | 不可通过区域（坑洞、断崖、危险边界等） | 精细 Polygon |

---

## 🤖 机器人与仿真环境

| 组件 | 规范与版本 | 说明 |
| :--- | :--- | :--- |
| **机器人型号** | `WF_TRON1A` | 轮足机器人（环境变量必须配置为 `export ROBOT_TYPE=WF_TRON1A`） |
| **主体坐标系** | `base_Link` | 机器人基座坐标系（严格区分大小写） |
| **仿真平台** | Gazebo Classic | 机器人动力学与场景仿真 |
| **操作系统** | Ubuntu 22.04 (WSL) | 仿真与 ROS 运行主环境 |
| **ROS 版本** | ROS 2 Iron | 中间件通信与节点调度 |
| **视觉节点** | `yolo_ros` | 加载 YOLO segmentation 权重并输出感知数据 |

### 核心感知 Topic
* `/yolo/detections`：2D 目标检测与实例分割 Mask
* `/yolo/tracking`：目标多帧跟踪
* `/yolo/detections_3d`：结合 Mask 像素与深度相机输出的 3D 边界与空间坐标
* `/yolo/dbg_image`：带分割渲染的 Debug 图像流

---

## 🚀 快速使用指南

### 1. 数据标注与格式转换
使用 LabelMe 进行多边形标注后，通过脚本批量转换为 YOLO 分割格式：
```bash
# 转换 LabelMe json 为 YOLO segmentation 格式
python Pre_Midterm_Archive/main/labelme_to_yolo.py --json_dir <path_to_json> --output_dir <path_to_yolo>
```

### 2. YOLO Segmentation 模型训练
```bash
# 基于 ultralytics 进行微调训练示例
yolo segment train data=Post_Midterm_Workspace/Training_Code_and_Config/data_yaml_backups/data.yaml \
    model=yolov8n-seg.pt \
    epochs=100 \
    imgsz=640 \
    batch=16
```

### 3. ROS 2 仿真部署启动
进入 ROS 工作区并激活环境：
```bash
# 1. 启动 Gazebo 机器人仿真
source ~/limx_ws/install/setup.bash
export ROBOT_TYPE=WF_TRON1A
ros2 launch tron1_gazebo tron1_gazebo.launch.py

# 2. 启动 yolo_ros 视觉检测节点（在 YOLO 虚拟环境下）
source ~/yolo_ws/src/yolo_ros/.venv/bin/activate
export PYTHONPATH=~/yolo_ws/src/yolo_ros/.venv/lib/python3.10/site-packages:$PYTHONPATH
source ~/yolo_ws/install/setup.bash
ros2 launch yolo_bringup yolo.launch.py model_path:=/mnt/d/CEIETPP/runs/segment/finetune3/weights/best.pt
```

---

## 📄 项目文档导航

* 详细项目总览：[`Post_Midterm_Workspace/Project_Overview/README.md`](./Post_Midterm_Workspace/Project_Overview/README.md)
* 路径与环境约定：[`Post_Midterm_Workspace/Project_Overview/Path_Conventions.md`](./Post_Midterm_Workspace/Project_Overview/Path_Conventions.md)
* ROS 仿真与 3D 检测记录：[`Post_Midterm_Workspace/ROS_Simulation_Deployment/README.md`](./Post_Midterm_Workspace/ROS_Simulation_Deployment/README.md)
* 历史答辩流程归档：[`Pre_Midterm_Archive/Pre_Midterm_Workflow.md`](./Pre_Midterm_Archive/Pre_Midterm_Workflow.md)
