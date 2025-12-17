---
layout: default
title: Mr. Virgil: Learning Multi-robot Visual-range Relative Localization
---

# Mr. Virgil: Learning Multi-robot Visual-range Relative Localization

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.10540" target="_blank" class="toolbar-btn">arXiv: 2512.10540v1</a>
    <a href="https://arxiv.org/pdf/2512.10540.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.10540v1" 
            onclick="toggleFavorite(this, '2512.10540v1', 'Mr. Virgil: Learning Multi-robot Visual-range Relative Localization')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Si Wang, Zhehan Li, Jiadong Lu, Rong Xiong, Yanjun Cao, Yue Wang

**分类**: cs.RO

**发布日期**: 2025-12-11

**备注**: Accepted by 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)

**🔗 代码/项目**: [GITHUB](https://github.com/HiOnes/Mr-Virgil)

---

## 💡 一句话要点

**Mr. Virgil：提出一种基于学习的多机器人视觉相对定位方法**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `多机器人定位` `相对定位` `视觉定位` `图神经网络` `姿态图优化` `数据关联` `UWB融合`

## 📋 核心要点

1. 现有UWB-视觉融合定位方法依赖身份编码硬件或精细调参算法，且易受错误匹配影响。
2. Mr. Virgil采用图神经网络进行数据关联，并结合可微姿态图优化，实现端到端的相对定位。
3. 实验表明，该方法在不同场景下均表现出稳定性和准确性，优于传统方法。

## 📝 摘要（中文）

本文提出了一种名为Mr. Virgil的端到端学习多机器人视觉范围相对定位框架。该框架包含一个图神经网络，用于超宽带(UWB)测距和视觉检测之间的数据关联，以及一个可微的姿态图优化(PGO)后端。基于图的前端提供鲁棒的匹配结果、准确的初始位置预测和可靠的不确定性估计，这些信息被集成到PGO后端，以提高最终姿态估计的准确性。此外，还实现了一个去中心化系统用于实际应用。实验涵盖了不同数量的机器人、模拟和真实环境、遮挡和非遮挡条件，结果表明，与传统方法相比，该方法在各种场景下都具有稳定性和准确性。

## 🔬 方法详解

**问题定义**：多机器人相对定位是多智能体协作的关键。现有的UWB-视觉融合方法在机器人和视觉检测之间的匹配问题上存在挑战，依赖于特定的硬件或需要繁琐的参数调整。此外，错误的匹配会导致定位系统出现不可逆的损害。

**核心思路**：本文的核心思路是利用图神经网络学习UWB测距和视觉检测之间的关联关系，从而实现更鲁棒的数据匹配。通过图神经网络预测初始位置和不确定性，并将其融入到姿态图优化中，进一步提高定位精度。

**技术框架**：Mr. Virgil框架包含两个主要模块：基于图神经网络的前端和可微姿态图优化(PGO)后端。前端负责处理UWB测距和视觉检测数据，利用图神经网络进行数据关联，并预测初始位置和不确定性。后端则利用前端的输出，通过PGO优化最终的机器人姿态。整个系统采用端到端的方式进行训练。

**关键创新**：该方法的主要创新在于使用图神经网络进行UWB测距和视觉检测之间的数据关联。与传统方法相比，图神经网络能够学习更复杂的关联模式，从而提高匹配的鲁棒性。此外，可微的PGO后端允许端到端训练，进一步优化定位性能。

**关键设计**：图神经网络的输入包括UWB测距和视觉检测数据，输出是机器人之间的匹配关系、初始位置预测和不确定性估计。损失函数包括匹配损失、位置损失和不确定性损失。PGO后端使用可微的因子图表示，允许梯度反向传播到前端，从而实现端到端训练。

## 📊 实验亮点

实验结果表明，Mr. Virgil在不同数量的机器人、模拟和真实环境、遮挡和非遮挡条件下均表现出优异的性能。与传统方法相比，该方法在定位精度和鲁棒性方面均有显著提升。具体性能数据未知，但论文强调了其在各种场景下的稳定性和准确性。

## 🎯 应用场景

该研究成果可应用于多机器人协同作业、无人机编队飞行、智能仓储物流等领域。通过提供准确可靠的相对定位信息，可以提升多智能体系统的协作效率和安全性，降低对外部环境的依赖，具有重要的实际应用价值和广阔的发展前景。

## 📄 摘要（原文）

> Ultra-wideband (UWB)-vision fusion localization has achieved extensive applications in the domain of multi-agent relative localization. The challenging matching problem between robots and visual detection renders existing methods highly dependent on identity-encoded hardware or delicate tuning algorithms. Overconfident yet erroneous matches may bring about irreversible damage to the localization system. To address this issue, we introduce Mr. Virgil, an end-to-end learning multi-robot visual-range relative localization framework, consisting of a graph neural network for data association between UWB rangings and visual detections, and a differentiable pose graph optimization (PGO) back-end. The graph-based front-end supplies robust matching results, accurate initial position predictions, and credible uncertainty estimates, which are subsequently integrated into the PGO back-end to elevate the accuracy of the final pose estimation. Additionally, a decentralized system is implemented for real-world applications. Experiments spanning varying robot numbers, simulation and real-world, occlusion and non-occlusion conditions showcase the stability and exactitude under various scenes compared to conventional methods. Our code is available at: https://github.com/HiOnes/Mr-Virgil.

