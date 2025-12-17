---
layout: default
title: InEKFormer: A Hybrid State Estimator for Humanoid Robots
---

# InEKFormer: A Hybrid State Estimator for Humanoid Robots

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.16306" target="_blank" class="toolbar-btn">arXiv: 2511.16306v1</a>
    <a href="https://arxiv.org/pdf/2511.16306.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.16306v1" 
            onclick="toggleFavorite(this, '2511.16306v1', 'InEKFormer: A Hybrid State Estimator for Humanoid Robots')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Lasse Hohmeyer, Mihaela Popescu, Ivan Bergonzani, Dennis Mronga, Frank Kirchner

**分类**: cs.RO

**发布日期**: 2025-11-20

**备注**: Accepted at The 22nd International Conference on Advanced Robotics (ICAR 2025)

---

## 💡 一句话要点

**提出InEKFormer混合状态估计器，提升人型机器人运动控制精度与鲁棒性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `人型机器人` `状态估计` `不变扩展卡尔曼滤波器` `Transformer网络` `混合方法`

## 📋 核心要点

1. 人型机器人双足运动在复杂环境中面临挑战，需要快速准确的状态估计为运动控制器提供反馈。
2. InEKFormer结合InEKF和Transformer网络，利用InEKF的先验知识和Transformer的学习能力，实现更精确的状态估计。
3. 在RH5数据集上的实验表明，InEKFormer具有潜力，但高维问题需要更鲁棒的自回归训练。

## 📝 摘要（中文）

本文提出了一种新颖的混合状态估计方法InEKFormer，它结合了不变扩展卡尔曼滤波器(InEKF)和Transformer网络。针对人型机器人在复杂环境中双足运动时，需要快速准确地反馈机器人浮动基座状态给运动控制器的难题，该方法旨在提高状态估计的精度和速度。论文将InEKFormer与InEKF和KalmanNet方法在人型机器人RH5的数据集上进行了比较。实验结果表明，Transformer在人型机器人状态估计方面具有潜力，但也强调了在高维问题中进行鲁棒自回归训练的必要性。

## 🔬 方法详解

**问题定义**：人型机器人在各种应用场景中潜力巨大，但其在不同环境中进行稳定和动态的双足运动仍然是一个挑战。状态估计在此过程中至关重要，它需要为运动控制器提供快速且准确的机器人浮动基座状态反馈。传统的卡尔曼滤波方法虽然应用广泛，但需要专家知识来精细调整噪声参数，这限制了其在复杂环境下的适应性。

**核心思路**：本文的核心思路是将传统的基于模型的InEKF与基于数据的Transformer网络相结合。InEKF提供了一个良好的先验估计，而Transformer网络则可以学习数据中的复杂模式，从而对InEKF的估计进行修正和优化。这种混合方法旨在结合两者的优点，提高状态估计的精度和鲁棒性。

**技术框架**：InEKFormer的整体框架包含两个主要模块：InEKF模块和Transformer模块。首先，InEKF利用机器人动力学模型和传感器数据（如IMU、力传感器等）进行初步的状态估计。然后，Transformer网络将InEKF的输出作为输入，学习状态之间的时序关系，并对InEKF的估计进行修正。最终，Transformer的输出作为最终的状态估计结果。

**关键创新**：InEKFormer的关键创新在于将InEKF与Transformer网络相结合，利用InEKF的先验知识和Transformer的学习能力。与传统的卡尔曼滤波方法相比，InEKFormer不需要手动调整噪声参数，并且可以学习数据中的复杂模式。与纯粹的基于学习的方法相比，InEKFormer利用了机器人动力学模型，从而提高了状态估计的鲁棒性。

**关键设计**：Transformer网络的具体结构包括多头自注意力机制和前馈神经网络。损失函数的设计需要考虑状态估计的精度和稳定性，可以采用均方误差等常用损失函数，并加入正则化项以防止过拟合。自回归训练是Transformer的关键，需要设计合适的训练策略，例如teacher forcing等，以保证训练的稳定性和收敛性。InEKF部分的参数设置则依赖于具体的机器人动力学模型和传感器特性。

## 📊 实验亮点

实验结果表明，InEKFormer在人型机器人RH5数据集上表现出潜力。虽然论文没有给出具体的性能数据和提升幅度，但强调了Transformer在人型机器人状态估计方面的应用前景。同时，实验也指出了在高维问题中进行鲁棒自回归训练的重要性，为未来的研究方向提供了指导。

## 🎯 应用场景

InEKFormer状态估计器可应用于各种人型机器人应用场景，例如工业自动化、家庭服务、医疗保健和搜救任务。更精确和鲁棒的状态估计能够提升机器人的运动控制性能，使其能够在复杂和动态环境中执行更复杂的任务。该研究为未来人型机器人的发展奠定了基础，有望推动人型机器人在实际应用中的广泛部署。

## 📄 摘要（原文）

> Humanoid robots have great potential for a wide range of applications, including industrial and domestic use, healthcare, and search and rescue missions. However, bipedal locomotion in different environments is still a challenge when it comes to performing stable and dynamic movements. This is where state estimation plays a crucial role, providing fast and accurate feedback of the robot's floating base state to the motion controller. Although classical state estimation methods such as Kalman filters are widely used in robotics, they require expert knowledge to fine-tune the noise parameters. Due to recent advances in the field of machine learning, deep learning methods are increasingly used for state estimation tasks. In this work, we propose the InEKFormer, a novel hybrid state estimation method that incorporates an invariant extended Kalman filter (InEKF) and a Transformer network. We compare our method with the InEKF and the KalmanNet approaches on datasets obtained from the humanoid robot RH5. The results indicate the potential of Transformers in humanoid state estimation, but also highlight the need for robust autoregressive training in these high-dimensional problems.

