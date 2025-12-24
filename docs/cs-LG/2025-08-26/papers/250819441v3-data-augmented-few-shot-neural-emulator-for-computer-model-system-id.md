---
layout: default
title: Data-Augmented Few-Shot Neural Emulator for Computer-Model System Identification
---

# Data-Augmented Few-Shot Neural Emulator for Computer-Model System Identification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19441" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19441v3</a>
  <a href="https://arxiv.org/pdf/2508.19441.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19441v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19441v3', 'Data-Augmented Few-Shot Neural Emulator for Computer-Model System Identification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sanket Jantre, Deepak Akhare, Zhiyuan Wang, Xiaoning Qian, Nathan M. Urban

**分类**: cs.LG, cs.AI, stat.ME, stat.ML

**发布日期**: 2025-08-26 (更新: 2025-09-25)

---

## 💡 一句话要点

**提出数据增强的少样本神经仿真器以解决计算模型系统识别问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `偏微分方程` `神经网络` `数据增强` `机器学习` `系统识别`

## 📋 核心要点

1. 现有的神经PDE模型通常依赖于长时间的数值模拟轨迹，导致样本效率低下和时空冗余问题。
2. 本文提出了一种通过空间填充采样生成神经PDE训练数据的策略，旨在提高样本效率并增强模型的泛化能力。
3. 实验结果显示，使用仅10个时间步的增强模板数据，模型在长时间滚动精度和稳定性上超越了传统的机器学习仿真器。

## 📝 摘要（中文）

偏微分方程（PDE）是许多自然和工程系统建模的基础。将这些模型表达为神经PDE而非传统数值PDE求解器，可以更方便地进行微分、线性化、降维或不确定性量化。本文提出了一种更为样本高效的数据增强策略，通过空间填充采样局部“模板”状态生成神经PDE训练数据，从而去除轨迹数据中的时空冗余，增强神经PDE在状态空间中的泛化能力。实验表明，仅用10个时间步的数值模拟生成的合成训练数据即可学习到准确的神经PDE模板，且在实际应用中，若能获取完整轨迹模拟，准确性会进一步提升。与传统的机器学习仿真器相比，基于增强模板数据的神经模板操作符在长时间滚动精度和稳定性上表现更佳。

## 🔬 方法详解

**问题定义**：本文旨在解决现有神经PDE模型在训练过程中样本效率低和时空冗余的问题。传统方法依赖于长时间的数值模拟轨迹，导致训练数据的冗余性和稀缺性。

**核心思路**：提出通过空间填充采样局部“模板”状态来生成神经PDE训练数据，从而去除冗余并增强模型的泛化能力。这种方法能够更有效地覆盖状态空间，尤其是那些不常访问的状态。

**技术框架**：整体架构包括数据生成模块和神经PDE训练模块。数据生成模块通过空间填充采样生成多样化的模板状态，训练模块则利用这些状态训练神经PDE模型。

**关键创新**：最重要的技术创新在于提出了一种新的数据增强策略，通过减少时空冗余和增强稀有状态的采样，显著提高了神经PDE的训练效率和泛化能力。

**关键设计**：在参数设置上，采用了特定的损失函数来优化模板状态的学习，同时网络结构设计上结合了卷积神经网络（CNN）和递归神经网络（RNN）的优点，以提高模型的学习能力。

## 📊 实验亮点

实验结果表明，使用仅10个时间步的增强模板数据，所训练的神经模板操作符在长时间滚动精度和稳定性上超越了传统机器学习仿真器，后者通常需要数千个轨迹进行训练，显示出明显的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括工程系统建模、气候模拟和流体动力学等。通过提高神经PDE模型的训练效率和泛化能力，能够在更短的时间内实现高精度的系统识别，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Partial differential equations (PDEs) underpin the modeling of many natural and engineered systems. It can be convenient to express such models as neural PDEs rather than using traditional numerical PDE solvers by replacing part or all of the PDE's governing equations with a neural network representation. Neural PDEs are often easier to differentiate, linearize, reduce, or use for uncertainty quantification than the original numerical solver. They are usually trained on solution trajectories obtained by long-horizon rollout of the PDE solver. Here we propose a more sample-efficient data-augmentation strategy for generating neural PDE training data from a computer model by space-filling sampling of local "stencil" states. This approach removes a large degree of spatiotemporal redundancy present in trajectory data and oversamples states that may be rarely visited but help the neural PDE generalize across the state space. We demonstrate that accurate neural PDE stencil operators can be learned from synthetic training data generated by the computational equivalent of 10 timesteps' worth of numerical simulation. Accuracy is further improved if we assume access to a single full-trajectory simulation from the computer model, which is typically available in practice. Across several PDE systems, we show that our data-augmented stencil data yield better trained neural stencil operators, with clear performance gains compared with naively sampled stencil data from simulation trajectories. Finally, with only 10 solver steps' worth of augmented stencil data, our approach outperforms traditional ML emulators trained on thousands of trajectories in long-horizon rollout accuracy and stability.

