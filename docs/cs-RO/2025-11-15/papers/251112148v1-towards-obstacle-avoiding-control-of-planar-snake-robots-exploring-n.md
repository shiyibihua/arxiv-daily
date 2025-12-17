---
layout: default
title: Towards Obstacle-Avoiding Control of Planar Snake Robots Exploring Neuro-Evolution of Augmenting Topologies
---

# Towards Obstacle-Avoiding Control of Planar Snake Robots Exploring Neuro-Evolution of Augmenting Topologies

**arXiv**: [2511.12148v1](https://arxiv.org/abs/2511.12148) | [PDF](https://arxiv.org/pdf/2511.12148.pdf)

**作者**: Advik Sinha, Akshay Arjun, Abhijit Das, Joyjit Mukherjee

**分类**: cs.RO

**发布日期**: 2025-11-15

**备注**: 9 pages, 6 figures

---

## 💡 一句话要点

**利用神经进化拓扑结构，实现平面蛇形机器人在复杂环境下的避障控制**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `蛇形机器人` `避障控制` `神经进化拓扑` `NEAT算法` `运动规划` `强化学习` `机器人控制` `动态步态`

## 📋 核心要点

1. 现有方法在复杂环境下蛇形机器人避障控制方面存在计算资源消耗大的问题。
2. 利用神经进化拓扑结构（NEAT）优化蛇形运动参数，直接控制关节角度，实现动态避障。
3. 实验表明，该方法计算效率高，尤其适用于大型复杂环境，性能优于现有方法。

## 📝 摘要（中文）

本研究旨在为平面蛇形机器人在高密度障碍物环境中的避障跟踪控制开发一种资源高效的解决方案。具体而言，采用神经进化拓扑结构（NEAT）为蛇形运动函数生成动态步态参数，该函数作用于蛇形机器人的关节角度，从而控制机器人在期望的动态路径上运动。NEAT是一种基于单神经网络的进化算法，特别适用于输入层维度远高于输出层维度的情况。对于平面蛇形机器人，输入层包括关节角度、连杆位置、头部连杆位置以及附近的障碍物位置。而输出层仅包含控制机器人速度和方向的蛇形运动的频率和偏移角度。来自激光雷达的障碍物数据、来自各种传感器的机器人数据，以及目标位置和时间，被用于参数化奖励函数，通过选择性传播优秀的神经网络来最大化该函数。实施和实验结果表明，所提出的方法在计算上是高效的，尤其是在具有许多障碍物的大型环境中。该框架已通过PyBullet上的物理引擎仿真研究进行了验证。结果表明，该方法优于现有的最先进方法，并且以显著降低的计算开销获得了与最新的CBRL方法相当的结果。

## 🔬 方法详解

**问题定义**：论文旨在解决平面蛇形机器人在复杂、高密度障碍物环境中进行避障跟踪控制的问题。现有方法通常计算资源消耗大，难以在实际应用中部署。

**核心思路**：论文的核心思路是利用神经进化拓扑结构（NEAT）自动生成蛇形机器人的运动参数，直接控制关节角度，从而实现动态避障。这种方法避免了传统方法中复杂的运动规划和控制算法，降低了计算复杂度。

**技术框架**：整体框架包括以下几个主要模块：1) 环境感知模块，通过LiDAR等传感器获取障碍物信息；2) 机器人状态感知模块，获取关节角度、连杆位置等信息；3) NEAT进化算法模块，根据环境和机器人状态，进化神经网络，输出蛇形运动的频率和偏移角度；4) 运动控制模块，将NEAT输出的参数作用于关节角度，控制机器人运动；5) 奖励函数评估模块，根据机器人是否成功避障并接近目标，计算奖励值，用于指导NEAT进化。

**关键创新**：最重要的技术创新点在于将NEAT应用于蛇形机器人的运动控制。NEAT能够自动搜索最优的网络结构和参数，无需人工设计复杂的控制策略。此外，论文针对蛇形机器人的特点，设计了合适的输入输出层和奖励函数，使得NEAT能够有效地学习到避障策略。

**关键设计**：输入层包括关节角度、连杆位置、头部连杆位置以及附近的障碍物位置，输出层包括蛇形运动的频率和偏移角度。奖励函数综合考虑了机器人与障碍物的距离、与目标的距离以及时间消耗。NEAT算法采用选择性传播策略，保留优秀的神经网络，加速进化过程。

## 📊 实验亮点

实验结果表明，所提出的方法在计算效率上优于现有的最先进方法，并且以显著降低的计算开销获得了与最新的CBRL方法相当的结果。该方法在PyBullet物理引擎仿真中进行了验证，证明了其在复杂环境下的有效性和鲁棒性。具体的性能数据和对比基线可在论文中找到。

## 🎯 应用场景

该研究成果可应用于灾难救援、管道检测、医疗机器人等领域。蛇形机器人具有良好的地形适应性和灵活性，能够在复杂、狭窄的环境中执行任务。通过NEAT自动生成控制策略，可以降低开发成本，提高机器人的自主性和适应性，使其更好地服务于人类。

## 📄 摘要（原文）

> This work aims to develop a resource-efficient solution for obstacle-avoiding tracking control of a planar snake robot in a densely cluttered environment with obstacles. Particularly, Neuro-Evolution of Augmenting Topologies (NEAT) has been employed to generate dynamic gait parameters for the serpenoid gait function, which is implemented on the joint angles of the snake robot, thus controlling the robot on a desired dynamic path. NEAT is a single neural-network based evolutionary algorithm that is known to work extremely well when the input layer is of significantly higher dimension and the output layer is of a smaller size. For the planar snake robot, the input layer consists of the joint angles, link positions, head link position as well as obstacle positions in the vicinity. However, the output layer consists of only the frequency and offset angle of the serpenoid gait that control the speed and heading of the robot, respectively. Obstacle data from a LiDAR and the robot data from various sensors, along with the location of the end goal and time, are employed to parametrize a reward function that is maximized over iterations by selective propagation of superior neural networks. The implementation and experimental results showcase that the proposed approach is computationally efficient, especially for large environments with many obstacles. The proposed framework has been verified through a physics engine simulation study on PyBullet. The approach shows superior results to existing state-of-the-art methodologies and comparable results to the very recent CBRL approach with significantly lower computational overhead. The video of the simulation can be found here: https://sites.google.com/view/neatsnakerobot

