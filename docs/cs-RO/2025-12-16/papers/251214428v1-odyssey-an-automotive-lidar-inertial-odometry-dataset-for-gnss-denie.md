---
layout: default
title: Odyssey: An Automotive Lidar-Inertial Odometry Dataset for GNSS-denied situations
---

# Odyssey: An Automotive Lidar-Inertial Odometry Dataset for GNSS-denied situations

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.14428" target="_blank" class="toolbar-btn">arXiv: 2512.14428v1</a>
    <a href="https://arxiv.org/pdf/2512.14428.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14428v1" 
            onclick="toggleFavorite(this, '2512.14428v1', 'Odyssey: An Automotive Lidar-Inertial Odometry Dataset for GNSS-denied situations')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Aaron Kurda, Simon Steuernagel, Lukas Jung, Marcus Baum

**分类**: cs.RO

**发布日期**: 2025-12-16

**备注**: 9 pages, 4 figures, submitted to International Journal of Robotics Research (IJRR)

---

## 💡 一句话要点

**Odyssey：为GNSS拒止环境提供高精度激光雷达惯性里程计数据集**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `激光雷达惯性里程计` `LIO` `SLAM` `GNSS拒止` `环形激光陀螺仪` `RLG` `自动驾驶` `数据集`

## 📋 核心要点

1. 现有LIO/SLAM数据集在GNSS拒止环境下精度不足，常用MEMS/FOG IMU无法支持长时间高精度定位。
2. Odyssey数据集使用导航级RLG-INS提供高精度地面真值，专注于隧道、停车场等GNSS拒止场景。
3. 数据集包含三重重复轨迹和精确地理坐标，支持LIO、地点识别等任务，并可整合外部地图数据。

## 📝 摘要（中文）

激光雷达惯性里程计(LIO)和同步定位与地图构建(SLAM)系统的开发和评估需要精确的地面真值。全球导航卫星系统(GNSS)通常被用作基础，但在受阻环境中，由于多径效应或信号丢失，其信号可能不可靠。现有数据集通过结合惯性测量单元(IMU)的测量来补偿GNSS信号的偶发性丢失，但常用的基于微机电系统(MEMS)或光纤陀螺仪(FOG)的系统不允许对GNSS拒止环境进行长期研究。为了弥补这一差距，我们提出了Odyssey，一个LIO数据集，专注于GNSS拒止环境，如隧道和停车场，以及其他代表性不足但普遍存在的情况，如走走停停的交通、颠簸的道路和广阔的田野。我们的地面真值来自配备环形激光陀螺仪(RLG)的导航级惯性导航系统(INS)，与现有数据集中使用的IMU相比，它具有卓越的偏置稳定性，能够对GNSS拒止环境进行长期准确的研究。这使得Odyssey成为第一个公开提供的基于RLG的INS数据集。除了为LIO提供数据外，我们还通过所有轨迹的三重重复以及通过提供精确的地理坐标来整合外部地图数据，来支持其他任务，如地点识别。所有数据、数据加载器和其他材料都可以在https://odyssey.uni-goettingen.de/上在线获取。

## 🔬 方法详解

**问题定义**：现有Lidar-Inertial Odometry (LIO) 和 Simultaneous Localization and Mapping (SLAM) 数据集在GNSS信号弱或缺失的环境中，由于依赖MEMS或FOG IMU，其定位精度和长期稳定性受到限制。这些IMU的偏置漂移较大，难以提供长时间可靠的地面真值，阻碍了对GNSS拒止环境下的LIO/SLAM算法的深入研究和评估。

**核心思路**：Odyssey数据集的核心思路是利用导航级的惯性导航系统(INS)，特别是配备环形激光陀螺仪(RLG)的INS，来生成高精度的地面真值。RLG相比MEMS和FOG具有更高的精度和更低的偏置漂移，能够在GNSS拒止环境下提供更长时间的可靠定位信息。通过这种方式，Odyssey数据集旨在为LIO/SLAM算法在复杂环境下的性能评估和改进提供坚实的基础。

**技术框架**：Odyssey数据集的构建主要包括数据采集和地面真值生成两个阶段。数据采集使用配备激光雷达和导航级INS的车辆，在各种具有挑战性的环境中进行轨迹记录，包括隧道、停车场、城市街道和开放区域。地面真值生成则依赖于RLG-INS提供的高精度惯性数据，并结合GNSS数据（在可用时）进行融合，以进一步提高定位精度。此外，数据集还包含精确的地理坐标，方便与外部地图数据进行整合。

**关键创新**：Odyssey数据集最关键的创新在于其使用了基于环形激光陀螺仪(RLG)的导航级INS来生成地面真值。这是首个公开可用的包含RLG-INS数据的LIO数据集。相比于以往依赖MEMS或FOG IMU的数据集，Odyssey能够提供更高精度、更长时间的地面真值，尤其是在GNSS拒止环境中。

**关键设计**：Odyssey数据集的关键设计包括：1) 使用导航级RLG-INS以确保高精度地面真值；2) 在各种具有挑战性的环境中采集数据，包括GNSS拒止环境和代表性不足的场景；3) 提供三重重复轨迹以支持地点识别等任务；4) 提供精确的地理坐标以方便与外部地图数据整合；5) 提供数据加载器和其他相关材料，方便用户使用。

## 📊 实验亮点

Odyssey数据集的关键亮点在于其高精度的地面真值，由导航级RLG-INS提供，显著优于传统MEMS/FOG IMU。该数据集在GNSS拒止环境中表现出色，为LIO/SLAM算法的长期性能评估提供了可能。此外，三重重复轨迹和精确地理坐标的提供，也为地点识别和地图融合等任务提供了便利。

## 🎯 应用场景

Odyssey数据集可广泛应用于自动驾驶、机器人导航、无人机等领域，尤其是在GNSS信号受限或不可用的环境中。该数据集能够促进LIO/SLAM算法的开发和评估，提高定位精度和鲁棒性，从而提升自动驾驶车辆在隧道、停车场等复杂环境下的安全性和可靠性。此外，该数据集还可用于研究地点识别、地图构建等相关问题。

## 📄 摘要（原文）

> The development and evaluation of Lidar-Inertial Odometry (LIO) and Simultaneous Localization and Mapping (SLAM) systems requires a precise ground truth. The Global Navigation Satellite System (GNSS) is often used as a foundation for this, but its signals can be unreliable in obstructed environments due to multi-path effects or loss-of-signal. While existing datasets compensate for the sporadic loss of GNSS signals by incorporating Inertial Measurement Unit (IMU) measurements, the commonly used Micro-Electro-Mechanical Systems (MEMS) or Fiber Optic Gyroscope (FOG)-based systems do not permit the prolonged study of GNSS-denied environments. To close this gap, we present Odyssey, a LIO dataset with a focus on GNSS-denied environments such as tunnels and parking garages as well as other underrepresented, yet ubiquitous situations such as stop-and-go-traffic, bumpy roads and wide open fields. Our ground truth is derived from a navigation-grade Inertial Navigation System (INS) equipped with a Ring Laser Gyroscope (RLG), offering exceptional bias stability characteristics compared to IMUs used in existing datasets and enabling the prolonged and accurate study of GNSS-denied environments. This makes Odyssey the first publicly available dataset featuring a RLG-based INS. Besides providing data for LIO, we also support other tasks, such as place recognition, through the threefold repetition of all trajectories as well as the integration of external mapping data by providing precise geodetic coordinates. All data, dataloader and other material is available online at https://odyssey.uni-goettingen.de/ .

