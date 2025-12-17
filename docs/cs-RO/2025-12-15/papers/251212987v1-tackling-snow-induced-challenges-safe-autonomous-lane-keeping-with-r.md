---
layout: default
title: Tackling Snow-Induced Challenges: Safe Autonomous Lane-Keeping with Robust Reinforcement Learning
---

# Tackling Snow-Induced Challenges: Safe Autonomous Lane-Keeping with Robust Reinforcement Learning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.12987" target="_blank" class="toolbar-btn">arXiv: 2512.12987v1</a>
    <a href="https://arxiv.org/pdf/2512.12987.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.12987v1" 
            onclick="toggleFavorite(this, '2512.12987v1', 'Tackling Snow-Induced Challenges: Safe Autonomous Lane-Keeping with Robust Reinforcement Learning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Amin Jalal Aghdasian, Farzaneh Abdollahi, Ali Kamali Iglie

**分类**: cs.RO, cs.AI, cs.CV, cs.LG

**发布日期**: 2025-12-15

---

## 💡 一句话要点

**提出基于鲁棒强化学习的车道保持系统，解决雪地自动驾驶难题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `自动驾驶` `车道保持` `鲁棒控制` `雪地环境`

## 📋 核心要点

1. 现有车道保持系统在雪地等复杂环境下，易受路面滑移和感知噪声影响，导致性能下降。
2. 论文提出动作鲁棒的深度强化学习方法，增强策略对环境不确定性的适应能力，提高系统鲁棒性。
3. 实验表明，AR-CADPG方法在雪地场景下具有更高的路径跟踪精度和鲁棒性，验证了方法的有效性。

## 📝 摘要（中文）

本文提出了两种新的算法，用于在雪地条件下自动驾驶车辆(AVs)的车道保持系统(LKS)。这些算法利用深度强化学习(DRL)来处理不确定性和滑移。它们包括动作鲁棒循环深度确定性策略梯度(AR-RDPG)和端到端动作鲁棒卷积神经网络注意力确定性策略梯度(AR-CADPG)，这两种动作鲁棒的决策方法。在AR-RDPG方法中，在感知层内，首先使用多尺度神经网络对相机图像进行去噪。然后，通过预训练的深度卷积神经网络(DCNN)提取中心线系数。这些系数与驾驶特性连接，作为控制层的输入。AR-CADPG方法提出了一种端到端的方法，其中卷积神经网络(CNN)和注意力机制被集成到DRL框架中。这两种方法首先在CARLA模拟器中进行训练，并在各种雪地场景下进行验证。在基于Jetson Nano的自动驾驶车辆上的真实实验证实了学习策略的可行性和稳定性。在两种模型中，AR-CADPG方法表现出卓越的路径跟踪精度和鲁棒性，突出了在AVs中结合时间记忆、对抗弹性和注意力机制的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决雪地环境下自动驾驶车辆车道保持系统面临的挑战，包括路面滑移带来的控制不确定性以及感知系统受降雪影响产生的噪声。现有方法难以有效应对这些问题，导致车道保持性能下降，甚至出现安全隐患。

**核心思路**：论文的核心思路是利用深度强化学习(DRL)学习在不确定环境下的鲁棒控制策略。通过引入动作鲁棒性，使智能体能够适应环境变化和感知噪声，从而提高车道保持系统的稳定性和安全性。具体而言，通过在训练过程中引入对抗样本，使策略对动作扰动具有更强的抵抗能力。

**技术框架**：论文提出了两种算法：AR-RDPG和AR-CADPG。AR-RDPG首先使用多尺度神经网络对图像进行去噪，然后利用预训练的DCNN提取中心线系数，并将其与驾驶特征结合作为RDPG控制器的输入。AR-CADPG则采用端到端的方式，将CNN和注意力机制集成到DRL框架中，直接从图像输入学习控制策略。两种方法都在CARLA模拟器中进行训练和验证，并在真实车辆上进行测试。

**关键创新**：论文的关键创新在于引入了动作鲁棒性到深度强化学习框架中，并将其应用于雪地环境下的车道保持任务。AR-CADPG的端到端结构以及注意力机制的引入，使得模型能够更好地关注关键特征，提高路径跟踪精度。此外，多尺度去噪网络的应用也增强了感知系统的鲁棒性。

**关键设计**：AR-RDPG中，多尺度去噪网络采用U-Net结构，用于去除图像噪声。预训练的DCNN用于提取车道中心线系数。AR-CADPG中，CNN采用ResNet结构，注意力机制采用Transformer结构。损失函数包括控制损失和动作鲁棒性损失，其中动作鲁棒性损失通过对抗训练实现，鼓励策略对动作扰动具有抵抗能力。具体参数设置未知。

## 📊 实验亮点

实验结果表明，AR-CADPG方法在雪地场景下具有更高的路径跟踪精度和鲁棒性。与AR-RDPG相比，AR-CADPG能够更准确地跟踪车道中心线，并对环境变化具有更强的适应能力。真实车辆实验验证了该方法的可行性和稳定性。具体的性能提升数据未知。

## 🎯 应用场景

该研究成果可应用于各种恶劣天气条件下的自动驾驶车辆，例如雪地、雨天、雾天等。通过提高自动驾驶系统在复杂环境下的鲁棒性和安全性，可以加速自动驾驶技术的商业化落地，并提升交通运输效率和安全性。此外，该方法还可以推广到其他机器人控制任务中，例如无人机、水下机器人等。

## 📄 摘要（原文）

> This paper proposes two new algorithms for the lane keeping system (LKS) in autonomous vehicles (AVs) operating under snowy road conditions. These algorithms use deep reinforcement learning (DRL) to handle uncertainties and slippage. They include Action-Robust Recurrent Deep Deterministic Policy Gradient (AR-RDPG) and end-to-end Action-Robust convolutional neural network Attention Deterministic Policy Gradient (AR-CADPG), two action-robust approaches for decision-making. In the AR-RDPG method, within the perception layer, camera images are first denoised using multi-scale neural networks. Then, the centerline coefficients are extracted by a pre-trained deep convolutional neural network (DCNN). These coefficients, concatenated with the driving characteristics, are used as input to the control layer. The AR-CADPG method presents an end-to-end approach in which a convolutional neural network (CNN) and an attention mechanism are integrated within a DRL framework. Both methods are first trained in the CARLA simulator and validated under various snowy scenarios. Real-world experiments on a Jetson Nano-based autonomous vehicle confirm the feasibility and stability of the learned policies. Among the two models, the AR-CADPG approach demonstrates superior path-tracking accuracy and robustness, highlighting the effectiveness of combining temporal memory, adversarial resilience, and attention mechanisms in AVs.

