---
layout: default
title: Learning long range dependencies through time reversal symmetry breaking
---

# Learning long range dependencies through time reversal symmetry breaking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05259" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05259v1</a>
  <a href="https://arxiv.org/pdf/2506.05259.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05259v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05259v1', 'Learning long range dependencies through time reversal symmetry breaking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guillaume Pourcel, Maxence Ernoult

**分类**: cs.LG

**发布日期**: 2025-06-05

**备注**: 45 pages

---

## 💡 一句话要点

**提出RHEL算法以解决长程依赖学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `长程依赖` `递归神经网络` `哈密顿系统` `时间序列预测` `深度学习算法`

## 📋 核心要点

1. 现有的递归神经网络（RNN）在处理长程依赖时表现不佳，尤其是在序列长度较大的情况下。
2. 论文提出的RHEL算法通过物理轨迹的有限差分计算梯度，显著减少了计算复杂度，并保持了高效性。
3. 实验结果表明，RHEL在多种时间序列任务中表现出与BPTT相当的性能，且在处理长序列时具有优势。

## 📝 摘要（中文）

深度状态空间模型（SSMs）重新点燃了基于物理的计算范式，RNN可以自然地嵌入到动态系统中。这需要遵循核心物理原则的专用学习算法，以及高效的系统模拟技术。我们提出了递归哈密顿回声学习（RHEL）算法，该算法可以证明地计算非耗散哈密顿系统物理轨迹的损失梯度。RHEL仅需三个“前向传递”，而不需要显式的雅可比计算，也不会引入梯度估计的方差。我们首先在连续时间中介绍RHEL，并证明其与连续伴随状态方法的形式等价。为了促进通过RHEL训练的哈密顿系统的模拟，我们提出了RHEL的离散时间版本，该版本在应用于我们称之为哈密顿递归单元（HRUs）的递归模块时等价于时间反向传播（BPTT）。

## 🔬 方法详解

**问题定义**：本论文旨在解决长程依赖学习中的计算效率问题，现有方法如BPTT在处理大规模模型时计算复杂度高，且在长序列上容易出现梯度消失或爆炸的问题。

**核心思路**：RHEL算法通过引入物理轨迹的有限差分计算损失梯度，避免了显式的雅可比计算，从而提高了计算效率和稳定性。

**技术框架**：RHEL的整体架构包括连续时间和离散时间两种形式，连续时间形式与伴随状态方法等价，而离散时间形式则与BPTT相对应。主要模块包括哈密顿递归单元（HRUs）和哈密顿状态空间模型（HSSMs）。

**关键创新**：RHEL的主要创新在于其通过物理原则计算梯度的能力，显著降低了计算复杂度，同时保持了模型的表达能力，与传统的反向传播方法相比具有本质区别。

**关键设计**：RHEL在参数设置上采用了物理系统的特性，损失函数设计遵循物理轨迹的变化，网络结构则基于哈密顿动力学构建，确保了模型的稳定性和可扩展性。

## 📊 实验亮点

实验结果显示，RHEL在处理序列长度达到约50k的任务中，性能与BPTT相当，且在计算效率上具有明显优势。这表明RHEL能够有效应对长程依赖问题，推动物理基础的自学习系统的发展。

## 🎯 应用场景

该研究的潜在应用领域包括时间序列预测、金融数据分析、气候模型等。通过引入RHEL算法，能够设计出更具能效的自学习系统，适用于需要处理长序列数据的场景，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Deep State Space Models (SSMs) reignite physics-grounded compute paradigms, as RNNs could natively be embodied into dynamical systems. This calls for dedicated learning algorithms obeying to core physical principles, with efficient techniques to simulate these systems and guide their design. We propose Recurrent Hamiltonian Echo Learning (RHEL), an algorithm which provably computes loss gradients as finite differences of physical trajectories of non-dissipative, Hamiltonian systems. In ML terms, RHEL only requires three "forward passes" irrespective of model size, without explicit Jacobian computation, nor incurring any variance in the gradient estimation. Motivated by the physical realization of our algorithm, we first introduce RHEL in continuous time and demonstrate its formal equivalence with the continuous adjoint state method. To facilitate the simulation of Hamiltonian systems trained by RHEL, we propose a discrete-time version of RHEL which is equivalent to Backpropagation Through Time (BPTT) when applied to a class of recurrent modules which we call Hamiltonian Recurrent Units (HRUs). This setting allows us to demonstrate the scalability of RHEL by generalizing these results to hierarchies of HRUs, which we call Hamiltonian SSMs (HSSMs). We apply RHEL to train HSSMs with linear and nonlinear dynamics on a variety of time-series tasks ranging from mid-range to long-range classification and regression with sequence length reaching $\sim 50k$. We show that RHEL consistently matches the performance of BPTT across all models and tasks. This work opens new doors for the design of scalable, energy-efficient physical systems endowed with self-learning capabilities for sequence modelling.

