---
layout: default
title: Odyssey: An Automotive Lidar-Inertial Odometry Dataset for GNSS-denied situations
---

# Odyssey: An Automotive Lidar-Inertial Odometry Dataset for GNSS-denied situations

**arXiv**: [2512.14428v1](https://arxiv.org/abs/2512.14428) | [PDF](https://arxiv.org/pdf/2512.14428.pdf)

**作者**: Aaron Kurda, Simon Steuernagel, Lukas Jung, Marcus Baum

**分类**: cs.RO

**发布日期**: 2025-12-16

**备注**: 9 pages, 4 figures, submitted to International Journal of Robotics Research (IJRR)

---

## 💡 一句话要点

**Odyssey：为GNSS拒止环境提供高精度激光雷达惯性里程计数据集**

🎯 **匹配领域**: **视觉里程计 (Visual Odometry)**

**关键词**: `激光雷达惯性里程计` `GNSS拒止环境` `环形激光陀螺仪` `惯性导航系统` `自动驾驶` `同步定位与地图构建` `数据集` `地面真值`

## 📋 核心要点

1. 现有LIO/SLAM系统依赖GNSS提供地面真值，但在GNSS拒止环境中，信号不稳定导致性能下降。
2. Odyssey数据集使用配备环形激光陀螺仪(RLG)的导航级INS，提供高精度地面真值，尤其适用于GNSS拒止环境。
3. 数据集包含隧道、停车场、拥堵交通等多种场景，并提供三重重复轨迹和精确地理坐标，支持LIO、地点识别等任务。

## 📝 摘要（中文）

激光雷达惯性里程计(LIO)和同步定位与地图构建(SLAM)系统的开发和评估需要精确的地面真值。全球导航卫星系统(GNSS)通常被用作基础，但在受阻环境中，由于多径效应或信号丢失，其信号可能不可靠。现有数据集通过结合惯性测量单元(IMU)测量来补偿GNSS信号的偶发性丢失，但常用的基于微机电系统(MEMS)或光纤陀螺仪(FOG)的系统不允许对GNSS拒止环境进行长期研究。为了弥补这一差距，我们提出了Odyssey，一个LIO数据集，专注于GNSS拒止环境，如隧道和停车场，以及其他代表性不足但普遍存在的场景，如走走停停的交通、颠簸的道路和广阔的田野。我们的地面真值来自配备环形激光陀螺仪(RLG)的导航级惯性导航系统(INS)，与现有数据集中使用的IMU相比，具有卓越的偏置稳定性，能够对GNSS拒止环境进行长期准确的研究。这使得Odyssey成为第一个公开提供的基于RLG的INS数据集。除了为LIO提供数据外，我们还通过所有轨迹的三重重复以及通过提供精确的地理坐标来整合外部地图数据，来支持其他任务，如地点识别。所有数据、数据加载器和其他材料都可以在https://odyssey.uni-goettingen.de/上在线获取。

## 🔬 方法详解

**问题定义**：现有LIO和SLAM系统在GNSS信号良好的环境下表现出色，但在隧道、停车场等GNSS拒止或信号受干扰的环境中，由于缺乏可靠的地面真值，系统性能显著下降。常用的MEMS或FOG IMU在长时间GNSS信号缺失的情况下，漂移误差累积严重，无法提供准确的姿态估计，限制了LIO/SLAM系统在这些场景下的应用。

**核心思路**：Odyssey数据集的核心思路是利用高精度的导航级惯性导航系统(INS)来生成可靠的地面真值，即使在长时间的GNSS信号缺失情况下也能保证姿态估计的准确性。通过配备环形激光陀螺仪(RLG)的INS，可以获得比传统MEMS或FOG IMU更高的偏置稳定性，从而减少长时间运行中的漂移误差。

**技术框架**：Odyssey数据集的构建流程主要包括数据采集和地面真值生成两个阶段。数据采集阶段使用配备激光雷达、相机和导航级INS的车辆在各种场景下进行数据采集，包括GNSS拒止环境（如隧道、停车场）以及其他具有挑战性的场景（如拥堵交通、颠簸道路）。地面真值生成阶段利用导航级INS的数据，结合GNSS数据（在可用时）进行紧耦合的姿态估计，生成高精度的地面真值轨迹。

**关键创新**：Odyssey数据集的关键创新在于使用了配备环形激光陀螺仪(RLG)的导航级INS来生成地面真值。这是第一个公开可用的包含RLG-based INS的数据集。与现有数据集常用的MEMS或FOG IMU相比，RLG具有更高的精度和更低的漂移，能够提供更可靠的地面真值，尤其是在长时间的GNSS拒止环境中。

**关键设计**：Odyssey数据集的关键设计包括：1) 使用导航级INS生成高精度地面真值；2) 包含多种具有挑战性的场景，特别是GNSS拒止环境；3) 提供三重重复轨迹，方便进行地点识别等任务的研究；4) 提供精确的地理坐标，方便整合外部地图数据。

## 📊 实验亮点

Odyssey数据集是首个公开的包含RLG-based INS的数据集，其地面真值精度显著高于使用MEMS或FOG IMU的数据集。通过在GNSS拒止环境中进行长时间的测试，验证了RLG-based INS的优越性能。数据集包含多种具有挑战性的场景，并提供三重重复轨迹和精确地理坐标，为LIO、SLAM和地点识别等任务的研究提供了丰富的数据支持。

## 🎯 应用场景

Odyssey数据集可广泛应用于自动驾驶、机器人导航、无人机等领域，尤其是在GNSS信号受限或不可用的场景下。该数据集能够促进LIO/SLAM算法在隧道、停车场、室内环境等复杂环境中的研究和应用，提高定位和建图的精度和鲁棒性，为智能交通、物流、安防等行业带来实际价值。

## 📄 摘要（原文）

> The development and evaluation of Lidar-Inertial Odometry (LIO) and Simultaneous Localization and Mapping (SLAM) systems requires a precise ground truth. The Global Navigation Satellite System (GNSS) is often used as a foundation for this, but its signals can be unreliable in obstructed environments due to multi-path effects or loss-of-signal. While existing datasets compensate for the sporadic loss of GNSS signals by incorporating Inertial Measurement Unit (IMU) measurements, the commonly used Micro-Electro-Mechanical Systems (MEMS) or Fiber Optic Gyroscope (FOG)-based systems do not permit the prolonged study of GNSS-denied environments. To close this gap, we present Odyssey, a LIO dataset with a focus on GNSS-denied environments such as tunnels and parking garages as well as other underrepresented, yet ubiquitous situations such as stop-and-go-traffic, bumpy roads and wide open fields. Our ground truth is derived from a navigation-grade Inertial Navigation System (INS) equipped with a Ring Laser Gyroscope (RLG), offering exceptional bias stability characteristics compared to IMUs used in existing datasets and enabling the prolonged and accurate study of GNSS-denied environments. This makes Odyssey the first publicly available dataset featuring a RLG-based INS. Besides providing data for LIO, we also support other tasks, such as place recognition, through the threefold repetition of all trajectories as well as the integration of external mapping data by providing precise geodetic coordinates. All data, dataloader and other material is available online at https://odyssey.uni-goettingen.de/ .

