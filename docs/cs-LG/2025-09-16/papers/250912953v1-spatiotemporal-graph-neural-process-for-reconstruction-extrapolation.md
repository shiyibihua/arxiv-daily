---
layout: default
title: Spatiotemporal graph neural process for reconstruction, extrapolation, and classification of cardiac trajectories
---

# Spatiotemporal graph neural process for reconstruction, extrapolation, and classification of cardiac trajectories

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.12953" class="toolbar-btn" target="_blank">📄 arXiv: 2509.12953v1</a>
  <a href="https://arxiv.org/pdf/2509.12953.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.12953v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.12953v1', 'Spatiotemporal graph neural process for reconstruction, extrapolation, and classification of cardiac trajectories')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jaume Banus, Augustin C. Ogier, Roger Hullin, Philippe Meyer, Ruud B. van Heeswijk, Jonas Richiardi

**分类**: cs.LG, eess.SY, q-bio.QM

**发布日期**: 2025-09-16

---

## 💡 一句话要点

**提出时空图神经网络过程，用于心脏轨迹的重建、外推和分类**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `时空图神经网络` `神经过程` `神经常微分方程` `心脏运动分析` `疾病分类`

## 📋 核心要点

1. 现有心脏运动分析方法难以有效处理稀疏观测数据，且缺乏对不确定性和解剖结构的建模能力。
2. 该论文提出一种基于时空图神经网络过程的概率框架，利用GNN建模心脏运动的潜在轨迹，并结合神经过程处理不确定性。
3. 实验表明，该方法在心脏轨迹重建、外推和疾病分类任务上表现出色，并在ACDC数据集上达到99%的分类准确率。

## 📝 摘要（中文）

本文提出了一种概率框架，用于建模来自稀疏观测的结构化时空动态，重点关注心脏运动。该方法集成了神经常微分方程（NODEs）、图神经网络（GNNs）和神经过程，形成一个统一的模型，能够捕捉不确定性、时间连续性和解剖结构。我们将动态系统表示为时空多路图，并使用GNN参数化的向量场来建模其潜在轨迹。给定节点和边级别的稀疏上下文观测，该模型推断潜在初始状态和控制变量的分布，从而实现轨迹的插值和外推。我们在三个合成动态系统（耦合摆、洛伦兹吸引子和Kuramoto振荡器）和两个真实世界的心脏成像数据集ACDC（N=150）和UK Biobank（N=526）上验证了该方法，证明了其准确的重建、外推和疾病分类能力。该模型能够从单个观测周期准确地重建轨迹并外推未来的心脏周期。它在ACDC分类任务上取得了最先进的结果（高达99%的准确率），并在UK Biobank受试者中检测心房颤动，性能具有竞争力（高达67%的准确率）。这项工作引入了一种灵活的方法来分析心脏运动，并为基于图的学习在结构化生物医学时空时间序列数据中提供了基础。

## 🔬 方法详解

**问题定义**：论文旨在解决从稀疏的心脏运动观测数据中准确重建、外推和分类心脏轨迹的问题。现有方法通常难以处理数据稀疏性，无法有效捕捉心脏运动的不确定性，并且缺乏对心脏解剖结构的有效建模，导致性能受限。

**核心思路**：论文的核心思路是将心脏运动建模为时空图上的动态过程，利用图神经网络（GNN）学习节点和边之间的关系，从而捕捉心脏的解剖结构和运动模式。同时，结合神经过程（Neural Processes）来处理观测数据的不确定性，并利用神经常微分方程（NODEs）建模时间连续性。

**技术框架**：整体框架包含以下几个主要模块：1) **图构建模块**：将心脏表示为时空多路图，节点代表心脏的不同区域，边代表区域之间的关系。2) **GNN编码器**：利用GNN对图结构数据进行编码，提取节点和边的特征表示。3) **神经过程模块**：利用神经过程学习潜在变量的分布，从而处理观测数据的不确定性。4) **NODE解码器**：利用神经常微分方程对潜在变量进行解码，生成连续的时间轨迹。

**关键创新**：最重要的技术创新点在于将GNN、神经过程和NODE集成到一个统一的框架中，从而能够同时捕捉心脏的解剖结构、运动模式和时间连续性，并处理观测数据的不确定性。与现有方法相比，该方法能够更有效地利用稀疏观测数据，并生成更准确的心脏轨迹。

**关键设计**：论文中一些关键的设计包括：1) 使用GNN来建模心脏的解剖结构，允许模型学习节点和边之间的复杂关系。2) 使用神经过程来处理观测数据的不确定性，从而提高模型的鲁棒性。3) 使用NODE来建模时间连续性，从而生成平滑的心脏轨迹。4) 损失函数包括重建损失、外推损失和分类损失，用于优化模型的各个部分。

## 📊 实验亮点

该模型在ACDC数据集上实现了高达99%的分类准确率，超越了现有方法。在UK Biobank数据集上，该模型在检测心房颤动方面取得了具有竞争力的性能，准确率高达67%。此外，该模型还能够从单个观测周期准确地重建和外推未来的心脏周期，展示了其强大的建模能力。

## 🎯 应用场景

该研究成果可应用于心脏疾病的诊断和治疗，例如通过重建和外推心脏轨迹，可以预测心脏疾病的发生和发展，并为临床医生提供决策支持。此外，该方法还可以应用于其他生物医学时空时间序列数据的分析，例如脑电图（EEG）和肌电图（EMG）。

## 📄 摘要（原文）

> We present a probabilistic framework for modeling structured spatiotemporal dynamics from sparse observations, focusing on cardiac motion. Our approach integrates neural ordinary differential equations (NODEs), graph neural networks (GNNs), and neural processes into a unified model that captures uncertainty, temporal continuity, and anatomical structure. We represent dynamic systems as spatiotemporal multiplex graphs and model their latent trajectories using a GNN-parameterized vector field. Given the sparse context observations at node and edge levels, the model infers a distribution over latent initial states and control variables, enabling both interpolation and extrapolation of trajectories. We validate the method on three synthetic dynamical systems (coupled pendulum, Lorenz attractor, and Kuramoto oscillators) and two real-world cardiac imaging datasets - ACDC (N=150) and UK Biobank (N=526) - demonstrating accurate reconstruction, extrapolation, and disease classification capabilities. The model accurately reconstructs trajectories and extrapolates future cardiac cycles from a single observed cycle. It achieves state-of-the-art results on the ACDC classification task (up to 99% accuracy), and detects atrial fibrillation in UK Biobank subjects with competitive performance (up to 67% accuracy). This work introduces a flexible approach for analyzing cardiac motion and offers a foundation for graph-based learning in structured biomedical spatiotemporal time-series data.

