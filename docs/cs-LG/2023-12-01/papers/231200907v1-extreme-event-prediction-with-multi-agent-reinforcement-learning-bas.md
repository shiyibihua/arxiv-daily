---
layout: default
title: Extreme Event Prediction with Multi-agent Reinforcement Learning-based Parametrization of Atmospheric and Oceanic Turbulence
---

# Extreme Event Prediction with Multi-agent Reinforcement Learning-based Parametrization of Atmospheric and Oceanic Turbulence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.00907" class="toolbar-btn" target="_blank">📄 arXiv: 2312.00907v1</a>
  <a href="https://arxiv.org/pdf/2312.00907.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.00907v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.00907v1', 'Extreme Event Prediction with Multi-agent Reinforcement Learning-based Parametrization of Atmospheric and Oceanic Turbulence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rambod Mojgani, Daniel Waelchli, Yifei Guan, Petros Koumoutsakos, Pedram Hassanzadeh

**分类**: cs.LG, cs.CE, physics.ao-ph, physics.comp-ph, physics.flu-dyn

**发布日期**: 2023-12-01

---

## 💡 一句话要点

**基于多智能体强化学习的气候极端事件预测方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `气候模型` `强化学习` `湍流闭合` `极端事件预测` `数据稀缺` `多智能体系统` `能量谱` `高保真模拟`

## 📋 核心要点

1. 现有气候模型在小尺度湍流过程的表示上存在结构不确定性，传统闭合方法的准确性不足。
2. 本文提出利用科学多智能体强化学习（SMARL）来学习气候模型的闭合，减少对高保真数据的依赖。
3. 实验结果表明，所提方法在低分辨率模拟中能够稳定地重现高保真模拟的统计特性，尤其是概率密度函数的尾部。

## 📝 摘要（中文）

全球气候模型（GCMs）是理解和预测气候变化的主要工具，但由于数值分辨率有限，这些模型在小尺度湍流过程的表示上存在重大结构不确定性。传统的闭合方法依赖于启发式和简化假设，导致在捕捉气候极端事件时的准确性不足。本文提出了一种基于科学多智能体强化学习（SMARL）的方法，通过仅使用少量高保真样本的能量谱来学习闭合模型，从而在低分辨率模拟中稳定地重现高保真模拟的统计特性，尤其是在数据稀缺的情况下展现出高潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决全球气候模型在小尺度湍流过程中的结构不确定性，现有方法依赖于大量高保真数据，导致不稳定性和准确性不足。

**核心思路**：通过科学多智能体强化学习（SMARL）来学习闭合模型，利用能量谱作为训练信号，减少对高保真样本的需求。

**技术框架**：整体架构包括数据采集、能量谱计算、SMARL训练和闭合模型应用四个主要模块，形成闭环反馈机制。

**关键创新**：采用SMARL进行闭合建模，显著降低对高保真数据的依赖，并提高了模型的稳定性和准确性。

**关键设计**：在训练过程中，使用了能量谱作为损失函数，设计了适应湍流特性的网络结构，以确保模型能够捕捉到小尺度过程的特征。

## 📊 实验亮点

实验结果显示，所提SMARL方法在低分辨率模拟中能够以较低的计算成本重现高保真模拟的统计特性，尤其是在概率密度函数的尾部表现出显著的准确性提升。与传统方法相比，模型的稳定性和准确性均有明显改善，展示了在数据稀缺情况下的高潜力。

## 🎯 应用场景

该研究的潜在应用领域包括气候变化预测、极端天气事件的预警和海洋环境监测等。通过提高气候模型的准确性和稳定性，能够为政策制定者和科学家提供更可靠的气候信息，进而推动可持续发展和环境保护。未来，该方法有望在数据稀缺的情况下广泛应用于气候科学研究。

## 📄 摘要（原文）

> Global climate models (GCMs) are the main tools for understanding and predicting climate change. However, due to limited numerical resolutions, these models suffer from major structural uncertainties; e.g., they cannot resolve critical processes such as small-scale eddies in atmospheric and oceanic turbulence. Thus, such small-scale processes have to be represented as a function of the resolved scales via closures (parametrization). The accuracy of these closures is particularly important for capturing climate extremes. Traditionally, such closures are based on heuristics and simplifying assumptions about the unresolved physics. Recently, supervised-learned closures, trained offline on high-fidelity data, have been shown to outperform the classical physics-based closures. However, this approach requires a significant amount of high-fidelity training data and can also lead to instabilities. Reinforcement learning is emerging as a potent alternative for developing such closures as it requires only low-order statistics and leads to stable closures. In Scientific Multi-Agent Reinforcement Learning (SMARL) computational elements serve a dual role of discretization points and learning agents. We leverage SMARL and fundamentals of turbulence physics to learn closures for prototypes of atmospheric and oceanic turbulence. The policy is trained using only the enstrophy spectrum, which is nearly invariant and can be estimated from a few high-fidelity samples (these few samples are far from enough for supervised/offline learning). We show that these closures lead to stable low-resolution simulations that, at a fraction of the cost, can reproduce the high-fidelity simulations' statistics, including the tails of the probability density functions. The results demonstrate the high potential of SMARL for closure modeling for GCMs, especially in the regime of scarce data and indirect observations.

