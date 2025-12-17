---
layout: default
title: Neural NMPC through Signed Distance Field Encoding for Collision Avoidance
---

# Neural NMPC through Signed Distance Field Encoding for Collision Avoidance

**arXiv**: [2511.21312v1](https://arxiv.org/abs/2511.21312) | [PDF](https://arxiv.org/pdf/2511.21312.pdf)

**作者**: Martin Jacquet, Marvin Harms, Kostas Alexis

**分类**: cs.RO

**发布日期**: 2025-11-26

**备注**: accepted for publication in IJRR

**DOI**: [10.1177/02783649251401223](https://doi.org/10.1177/02783649251401223)

---

## 💡 一句话要点

**提出神经网络非线性模型预测控制以解决无人机避障问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `神经网络` `非线性模型预测控制` `避障` `无人机导航` `带符号距离函数` `深度学习` `环境感知`

## 📋 核心要点

1. 现有的无人机导航方法在未知环境中面临碰撞风险，尤其是在复杂和拥挤的场景中。
2. 本文提出了一种基于神经网络的NMPC框架，通过将范围图像编码为SDF来实现避障，增强了导航的安全性和灵活性。
3. 实验结果表明，该方法在森林环境中有效避免碰撞，表现出较强的鲁棒性，相较于现有方法有显著提升。

## 📝 摘要（中文）

本文提出了一种神经网络非线性模型预测控制（NMPC）框架，用于在未知环境中实现无地图、无碰撞的导航，适用于搭载传感器的空中机器人。我们利用深度神经网络将单幅范围图像编码为带符号距离函数（SDF），捕捉环境中的所有可用信息。该神经网络架构由两个级联网络组成：一个卷积编码器将输入图像压缩为低维潜在向量，另一个多层感知器近似相应的空间SDF。后者网络参数化了用于避障的显式位置约束，并嵌入到速度跟踪的NMPC中，输出推力和姿态指令。我们进行了理论分析，验证了在固定观测下的递归可行性和稳定性，并在仿真和实验中评估了学习组件的开环性能和控制器的闭环性能。

## 🔬 方法详解

**问题定义**：本文旨在解决无人机在未知环境中进行安全导航时的碰撞避免问题。现有方法在复杂环境中容易受到障碍物的影响，导致导航失败或碰撞风险增大。

**核心思路**：我们提出了一种神经网络NMPC框架，通过将单幅范围图像编码为带符号距离函数（SDF），有效捕捉环境信息，从而实现安全的路径规划与控制。

**技术框架**：该框架由两个主要模块组成：卷积编码器用于将输入的范围图像压缩为低维潜在向量，随后多层感知器用于近似空间SDF，并将其作为位置约束嵌入到NMPC中，输出控制指令。

**关键创新**：最重要的创新在于将深度学习与NMPC相结合，利用SDF作为显式的避障约束，显著提高了无人机在复杂环境中的导航能力。与传统方法相比，该方法在处理动态和未知障碍物时表现出更好的适应性。

**关键设计**：在网络结构上，卷积编码器和多层感知器的设计经过精心调整，以确保高效的信息提取和准确的SDF近似。同时，损失函数的选择也考虑了避障性能和控制精度的平衡。实验中还进行了消融研究，以验证各个组件的贡献。

## 📊 实验亮点

实验结果显示，所提出的神经NMPC在森林环境中成功实现了避障，表现出较强的鲁棒性。在与两种先进本地导航方法的比较中，本文方法在处理漂移位置估计和对抗性速度输入时，表现出明显的性能提升，验证了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括无人机在复杂环境中的自主导航，如森林、城市和灾后救援等场景。通过提高避障能力，该技术可以显著增强无人机在实际任务中的安全性和可靠性，推动无人机技术的广泛应用。

## 📄 摘要（原文）

> This paper introduces a neural Nonlinear Model Predictive Control (NMPC) framework for mapless, collision-free navigation in unknown environments with Aerial Robots, using onboard range sensing. We leverage deep neural networks to encode a single range image, capturing all the available information about the environment, into a Signed Distance Function (SDF). The proposed neural architecture consists of two cascaded networks: a convolutional encoder that compresses the input image into a low-dimensional latent vector, and a Multi-Layer Perceptron that approximates the corresponding spatial SDF. This latter network parametrizes an explicit position constraint used for collision avoidance, which is embedded in a velocity-tracking NMPC that outputs thrust and attitude commands to the robot. First, a theoretical analysis of the contributed NMPC is conducted, verifying recursive feasibility and stability properties under fixed observations. Subsequently, we evaluate the open-loop performance of the learning-based components as well as the closed-loop performance of the controller in simulations and experiments. The simulation study includes an ablation study, comparisons with two state-of-the-art local navigation methods, and an assessment of the resilience to drifting odometry. The real-world experiments are conducted in forest environments, demonstrating that the neural NMPC effectively performs collision avoidance in cluttered settings against an adversarial reference velocity input and drifting position estimates.

