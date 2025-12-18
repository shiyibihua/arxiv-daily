---
layout: default
title: Physically Plausible Multi-System Trajectory Generation and Symmetry Discovery
---

# Physically Plausible Multi-System Trajectory Generation and Symmetry Discovery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23003" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23003v1</a>
  <a href="https://arxiv.org/pdf/2509.23003.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23003v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23003v1', 'Physically Plausible Multi-System Trajectory Generation and Symmetry Discovery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiayin Liu, Yulong Yang, Vineet Bansal, Christine Allen-Blanchette

**分类**: cs.LG, cs.AI, eess.SY

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出SPS-GAN，用于多系统轨迹生成和对称性发现，无需先验知识并泛化到未见参数。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `辛几何神经网络` `生成对抗网络` `多系统动力学` `轨迹预测` `视频生成` `对称性发现` `物理仿真`

## 📋 核心要点

1. 现有模型通常针对具有固定物理参数的单个系统，难以泛化到多个系统和未知参数。
2. SPS-GAN 将 Hamiltonian 神经网络嵌入条件 GAN 中，利用物理先验知识和对抗训练生成轨迹。
3. 实验表明，SPS-GAN 在多个任务上表现出色，且能发现系统配置空间的结构，无需先验知识。

## 📝 摘要（中文）

本文提出了一种名为Symplectic Phase Space GAN (SPS-GAN) 的模型，用于捕获多个系统的动力学，并推广到未见过的物理参数。与以往模型不同，SPS-GAN不需要系统配置空间的先验知识，而是可以从任意测量类型（如状态空间测量、视频帧）中发现配置空间的结构。该模型通过将 Hamiltonian 神经网络循环模块嵌入到条件 GAN 骨干网络中，实现物理上合理的生成。为了发现配置空间的结构，本文优化了条件时间序列 GAN 目标，并添加了一个物理驱动的项，以鼓励配置空间的稀疏表示。实验证明，SPS-GAN 在轨迹预测、视频生成和对称性发现方面具有有效性，并且在捕获多个系统方面达到了与为单个系统设计的监督模型相当的性能。

## 🔬 方法详解

**问题定义**：现有基于神经网络的动力学模型通常只能处理单个系统，并且需要预先知道系统的配置空间。这些模型难以泛化到具有不同物理参数的多个系统，也无法从任意类型的测量数据中学习系统的动力学规律。因此，如何设计一个能够处理多个系统、泛化到未知参数，并且能够从任意测量数据中发现系统配置空间的动力学模型是一个重要的挑战。

**核心思路**：SPS-GAN 的核心思路是将 Hamiltonian 神经网络作为生成器的循环模块，并将其嵌入到条件 GAN 的框架中。 Hamiltonian 神经网络能够保证生成轨迹的物理合理性，而条件 GAN 则能够学习多个系统的动力学分布。通过优化一个包含物理驱动项的损失函数，SPS-GAN 能够学习到配置空间的稀疏表示，从而发现系统的配置空间结构。

**技术框架**：SPS-GAN 的整体架构是一个条件 GAN，其中生成器是一个 Hamiltonian 神经网络循环模块，判别器用于区分生成的轨迹和真实的轨迹。生成器的输入是系统的初始状态和物理参数，输出是系统的未来轨迹。判别器的输入是轨迹，输出是轨迹是真实轨迹的概率。为了发现配置空间结构，SPS-GAN 优化了一个包含物理驱动项的条件时间序列 GAN 目标。

**关键创新**：SPS-GAN 的关键创新在于以下几个方面：1) 能够处理多个系统，并泛化到未见过的物理参数；2) 不需要系统配置空间的先验知识，而是可以从任意测量类型中发现配置空间的结构；3) 将 Hamiltonian 神经网络嵌入到条件 GAN 中，保证了生成轨迹的物理合理性。

**关键设计**：SPS-GAN 的关键设计包括：1) 使用 Hamiltonian 神经网络作为生成器的循环模块，保证生成轨迹的辛结构；2) 使用条件 GAN 框架，学习多个系统的动力学分布；3) 优化一个包含物理驱动项的损失函数，鼓励配置空间的稀疏表示，从而发现系统的配置空间结构。具体的损失函数包括 GAN 损失、物理损失和稀疏损失。物理损失用于约束生成轨迹满足 Hamiltonian 动力学方程，稀疏损失用于鼓励配置空间的稀疏表示。

## 📊 实验亮点

SPS-GAN 在轨迹预测、视频生成和对称性发现方面取得了显著成果。在多个系统的数据集上，SPS-GAN 的性能与为单个系统设计的监督模型相当，并且能够泛化到未见过的物理参数。此外，SPS-GAN 能够从任意测量类型中发现系统配置空间的结构，无需先验知识。

## 🎯 应用场景

SPS-GAN 可应用于机器人运动规划、物理仿真、视频生成等领域。例如，可以用于生成机器人在复杂环境中的运动轨迹，模拟物理系统的演化过程，或者生成具有物理合理性的视频内容。该研究有助于提升人工智能模型在物理世界的理解和预测能力，为相关应用提供更可靠的基础。

## 📄 摘要（原文）

> From metronomes to celestial bodies, mechanics underpins how the world evolves in time and space. With consideration of this, a number of recent neural network models leverage inductive biases from classical mechanics to encourage model interpretability and ensure forecasted states are physical. However, in general, these models are designed to capture the dynamics of a single system with fixed physical parameters, from state-space measurements of a known configuration space. In this paper we introduce Symplectic Phase Space GAN (SPS-GAN) which can capture the dynamics of multiple systems, and generalize to unseen physical parameters from. Moreover, SPS-GAN does not require prior knowledge of the system configuration space. In fact, SPS-GAN can discover the configuration space structure of the system from arbitrary measurement types (e.g., state-space measurements, video frames). To achieve physically plausible generation, we introduce a novel architecture which embeds a Hamiltonian neural network recurrent module in a conditional GAN backbone. To discover the structure of the configuration space, we optimize the conditional time-series GAN objective with an additional physically motivated term to encourages a sparse representation of the configuration space. We demonstrate the utility of SPS-GAN for trajectory prediction, video generation and symmetry discovery. Our approach captures multiple systems and achieves performance on par with supervised models designed for single systems.

