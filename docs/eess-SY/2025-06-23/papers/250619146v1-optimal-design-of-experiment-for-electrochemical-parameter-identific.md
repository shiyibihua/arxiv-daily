---
layout: default
title: Optimal Design of Experiment for Electrochemical Parameter Identification of Li-ion Battery via Deep Reinforcement Learning
---

# Optimal Design of Experiment for Electrochemical Parameter Identification of Li-ion Battery via Deep Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19146" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19146v1</a>
  <a href="https://arxiv.org/pdf/2506.19146.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19146v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19146v1', 'Optimal Design of Experiment for Electrochemical Parameter Identification of Li-ion Battery via Deep Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mehmet Fatih Ozkan, Samuel Filgueira da Silva, Faissal El Idrissi, Prashanth Ramesh, Marcello Canova

**分类**: eess.SY

**发布日期**: 2025-06-23

---

## 💡 一句话要点

**提出深度强化学习优化实验设计以识别锂离子电池电化学参数**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `锂离子电池` `电化学参数` `深度强化学习` `最优实验设计` `TD3算法` `参数估计` `信息内容` `实验效率`

## 📋 核心要点

1. 现有方法在电化学参数估计中存在准确性不足和效率低下的问题，限制了锂离子电池性能的监测与评估。
2. 本文提出的解决方案结合深度强化学习与最优实验设计，通过TD3算法优化输入激励，提高系统对电化学参数的敏感性。
3. 实验结果显示，DRL方法在信息内容和参数估计精度上优于NMPC设计和传统测试，且显著减少了实验时间和计算资源消耗。

## 📝 摘要（中文）

准确的电化学参数估计对于锂离子电池（LiB）的性能监测和评估至关重要。本文提出了一种新颖的方法，将深度强化学习（DRL）与最优实验设计（OED）框架结合，以识别LiB电池模型的关键电化学参数。该方法利用双延迟深度确定性策略梯度（TD3）算法优化输入激励，从而提高系统响应对电化学参数的敏感性。与非线性模型预测控制（NMPC）方法及传统测试相比，DRL方法在信息内容上表现优越，体现在更高的Fisher信息（FI）值和更低的参数估计误差。此外，DRL方法在实验时间和计算资源上也显著减少。

## 🔬 方法详解

**问题定义**：本文旨在解决锂离子电池电化学参数估计的准确性和效率问题。现有方法在实验设计上存在不足，导致参数估计误差较大，影响电池性能评估。

**核心思路**：论文提出的核心思路是将深度强化学习（DRL）与最优实验设计（OED）结合，通过TD3算法优化输入激励，以提高系统响应对电化学参数的敏感性，从而实现更准确的参数估计。

**技术框架**：整体架构包括数据采集、DRL模型训练和参数估计三个主要模块。首先，通过实验获取电池数据，然后利用DRL模型进行训练，最后进行参数估计和性能评估。

**关键创新**：最重要的技术创新点在于将TD3算法应用于电化学参数识别的实验设计中，显著提高了信息内容和参数估计的准确性。这一方法与传统的NMPC方法相比，具有更高的灵活性和效率。

**关键设计**：在关键设计方面，论文详细描述了TD3算法的参数设置、损失函数的选择以及网络结构的设计，确保了模型在训练过程中的稳定性和收敛性。

## 📊 实验亮点

实验结果表明，DRL方法在Fisher信息（FI）值上显著高于NMPC设计，参数估计误差降低，实验时间和计算资源消耗也显著减少。这些结果表明，DRL方法在电化学参数识别中的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括电池管理系统、智能电网和电动汽车等。通过提高锂离子电池电化学参数的估计精度，可以更好地监测电池性能，延长电池寿命，提升电动汽车的续航能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Accurate parameter estimation in electrochemical battery models is essential for monitoring and assessing the performance of lithium-ion batteries (LiBs). This paper presents a novel approach that combines deep reinforcement learning (DRL) with an optimal experimental design (OED) framework to identify key electrochemical parameters of LiB cell models. The proposed method utilizes the twin delayed deep deterministic policy gradient (TD3) algorithm to optimize input excitation, thereby increasing the sensitivity of the system response to electrochemical parameters. The performance of this DRL-based approach is evaluated against a nonlinear model predictive control (NMPC) method and conventional tests. Results indicate that the DRL-based method provides superior information content, reflected in higher Fisher information (FI) values and lower parameter estimation errors compared to the NMPC design and conventional test practices. Additionally, the DRL approach offers a substantial reduction in experimental time and computational resources.

