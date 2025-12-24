---
layout: default
title: Learning Robust Satellite Attitude Dynamics with Physics-Informed Normalising Flow
---

# Learning Robust Satellite Attitude Dynamics with Physics-Informed Normalising Flow

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07841" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07841v3</a>
  <a href="https://arxiv.org/pdf/2508.07841.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07841v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07841v3', 'Learning Robust Satellite Attitude Dynamics with Physics-Informed Normalising Flow')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Carlo Cena, Mauro Martini, Marcello Chiaberge

**分类**: cs.LG, eess.SY

**发布日期**: 2025-08-11 (更新: 2025-10-27)

---

## 💡 一句话要点

**提出基于物理信息的神经网络以提升卫星姿态控制的鲁棒性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `卫星姿态控制` `模型预测控制` `物理信息神经网络` `深度学习` `鲁棒性` `数据驱动模型` `自注意力机制`

## 📋 核心要点

1. 现有的纯数据驱动模型在面对训练域外输入时，泛化能力和稳定性较差，难以满足航天器姿态控制的需求。
2. 本文提出将物理信息神经网络（PINNs）与航天器姿态动态学习相结合，以提高模型的鲁棒性和稳定性。
3. 实验结果表明，物理信息的引入使得模型的平均相对误差降低了27.08%，并在MPC框架中显著提升了控制精度和收敛速度。

## 📝 摘要（中文）

姿态控制是航天器操作的基本方面。模型预测控制（MPC）作为一种强大的策略，依赖于准确的系统动态模型来优化控制动作。然而，在物理模型不完整或难以推导的情况下，纯数据驱动模型在泛化和稳定性方面存在挑战。为了解决这些问题，本文探讨了将物理信息神经网络（PINNs）与航天器姿态动态学习相结合的优势。通过使用具有自注意力机制的Real NVP神经网络架构，训练了多种模型，并比较了纯数据驱动方法和物理信息变体的性能。结果显示，物理信息的引入显著提高了模型的性能，尤其是在MPC框架中，PINN模型在控制精度和鲁棒性方面优于纯数据驱动模型，收敛时间改善高达62%。

## 🔬 方法详解

**问题定义**：本文旨在解决航天器姿态控制中，现有纯数据驱动模型在泛化和稳定性方面的不足，尤其是在面对训练域外输入时的表现不佳。

**核心思路**：通过将物理信息神经网络（PINNs）与数据驱动学习相结合，利用物理模型的知识来增强模型的鲁棒性和稳定性，从而提升姿态控制的效果。

**技术框架**：整体架构包括使用Real NVP神经网络，结合自注意力机制进行训练，分为两种训练策略：纯数据驱动基线和物理信息变体。

**关键创新**：最重要的创新在于将物理信息与深度学习相结合，显著提高了模型在控制任务中的表现，尤其是在面对噪声和摩擦等不确定性时的鲁棒性。

**关键设计**：在网络结构上，采用了Real NVP架构，并设计了适应性损失函数以平衡物理信息与数据驱动学习的贡献，确保模型在训练过程中的稳定性和准确性。

## 📊 实验亮点

实验结果显示，物理信息的引入使得模型的平均相对误差降低了27.08%。在MPC框架中，PINN模型在控制精度和鲁棒性方面优于纯数据驱动模型，收敛时间改善高达62%。

## 🎯 应用场景

该研究的潜在应用领域包括航天器的自主控制、卫星姿态调整以及其他需要高精度控制的机器人系统。通过提升模型的鲁棒性和稳定性，能够在复杂环境中实现更可靠的操作，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Attitude control is a fundamental aspect of spacecraft operations. Model Predictive Control (MPC) has emerged as a powerful strategy for these tasks, relying on accurate models of the system dynamics to optimize control actions over a prediction horizon. In scenarios where physics models are incomplete, difficult to derive, or computationally expensive, machine learning offers a flexible alternative by learning the system behavior directly from data. However, purely data-driven models often struggle with generalization and stability, especially when applied to inputs outside their training domain. To address these limitations, we investigate the benefits of incorporating Physics-Informed Neural Networks (PINNs) into the learning of spacecraft attitude dynamics, comparing their performance with that of purely data-driven approaches. Using a Real-valued Non-Volume Preserving (Real NVP) neural network architecture with a self-attention mechanism, we trained several models on simulated data generated with the Basilisk simulator. Two training strategies were considered: a purely data-driven baseline and a physics-informed variant to improve robustness and stability. Our results demonstrate that the inclusion of physics-based information significantly enhances the performance in terms of the mean relative error with the best architectures found by 27.08%. These advantages are particularly evident when the learned models are integrated into an MPC framework, where PINN-based models consistently outperform their purely data-driven counterparts in terms of control accuracy and robustness, and achieve improved settling times when compared to traditional MPC approaches, yielding improvements of up to 62%, when subject to observation noise and RWs friction.

