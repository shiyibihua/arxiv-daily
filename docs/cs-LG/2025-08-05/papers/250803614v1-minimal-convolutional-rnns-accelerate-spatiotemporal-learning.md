---
layout: default
title: Minimal Convolutional RNNs Accelerate Spatiotemporal Learning
---

# Minimal Convolutional RNNs Accelerate Spatiotemporal Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03614" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03614v1</a>
  <a href="https://arxiv.org/pdf/2508.03614.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03614v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03614v1', 'Minimal Convolutional RNNs Accelerate Spatiotemporal Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Coşku Can Horuz, Sebastian Otte, Martin V. Butz, Matthias Karlbauer

**分类**: cs.LG, cs.NE

**发布日期**: 2025-08-05

**备注**: Accepted at ICANN 2025

---

## 💡 一句话要点

**提出MinConvLSTM和MinConvGRU以加速时空学习**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `卷积递归网络` `时空序列建模` `最小化递归神经网络` `并行训练` `预测精度`

## 📋 核心要点

1. 现有的卷积递归神经网络在训练效率和空间建模能力上存在瓶颈，尤其是在处理时空序列时。
2. 提出的MinConvLSTM和MinConvGRU通过结合卷积和最小化递归结构，实现了高效的并行训练，同时保持了局部空间特征的建模能力。
3. 实验结果表明，所提模型在Navier-Stokes动力学和地势数据预测任务中，训练速度和预测精度均显著优于传统的ConvLSTM和ConvGRU。

## 📝 摘要（中文）

本文提出了MinConvLSTM和MinConvGRU两种新颖的时空模型，结合了卷积递归网络的空间归纳偏差与最小化、可并行化递归神经网络的训练效率。该方法将MinLSTM和MinGRU的对数域前缀和公式扩展到卷积架构，实现了完全并行的训练，同时保持了局部空间建模。这消除了在教师强制过程中对隐藏状态的顺序更新需求，解决了传统卷积递归网络模型的主要瓶颈。此外，我们在MinConvLSTM中引入了受xLSTM架构启发的指数门控机制，进一步简化了对数域计算。我们的模型结构简约、计算高效，参数数量减少且可扩展性提高。通过在Navier-Stokes动力学和实际地势数据的时空预测任务中评估，我们的模型在训练速度上显著优于标准的ConvLSTM和ConvGRU，并在闭环自回归模式下也实现了更低的预测误差。这些发现表明，最小递归结构与卷积输入聚合相结合，为时空序列建模提供了一个有效的替代方案，弥合了递归简单性与空间复杂性之间的差距。

## 🔬 方法详解

**问题定义**：本文旨在解决现有卷积递归神经网络在时空序列建模中的训练效率低和空间建模能力不足的问题，尤其是在教师强制过程中存在的隐藏状态更新瓶颈。

**核心思路**：通过引入MinConvLSTM和MinConvGRU，结合卷积网络的空间特性和最小化递归结构的并行化优势，简化了训练过程并提高了模型的效率。

**技术框架**：模型的整体架构包括卷积层和最小化递归单元，采用对数域前缀和计算方法，支持完全并行的训练过程。主要模块包括输入层、卷积层、递归单元和输出层。

**关键创新**：最重要的技术创新在于将对数域前缀和方法扩展到卷积架构，并引入指数门控机制，显著提高了计算效率和模型的可扩展性。

**关键设计**：模型在参数设置上进行了优化，减少了参数数量，同时采用了适应性损失函数以提高训练效果，确保了在不同任务中的良好表现。

## 📊 实验亮点

在实验中，MinConvLSTM和MinConvGRU在Navier-Stokes动力学和地势数据预测任务上，训练速度显著提升，分别比标准ConvLSTM和ConvGRU快了多个数量级。同时，在闭环自回归模式下，预测误差也显著降低，展示了模型的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括气象预测、交通流量预测和其他需要时空序列建模的领域。通过提高模型的训练效率和预测精度，能够为实际应用提供更快速和准确的决策支持，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We introduce MinConvLSTM and MinConvGRU, two novel spatiotemporal models that combine the spatial inductive biases of convolutional recurrent networks with the training efficiency of minimal, parallelizable RNNs. Our approach extends the log-domain prefix-sum formulation of MinLSTM and MinGRU to convolutional architectures, enabling fully parallel training while retaining localized spatial modeling. This eliminates the need for sequential hidden state updates during teacher forcing - a major bottleneck in conventional ConvRNN models. In addition, we incorporate an exponential gating mechanism inspired by the xLSTM architecture into the MinConvLSTM, which further simplifies the log-domain computation. Our models are structurally minimal and computationally efficient, with reduced parameter count and improved scalability. We evaluate our models on two spatiotemporal forecasting tasks: Navier-Stokes dynamics and real-world geopotential data. In terms of training speed, our architectures significantly outperform standard ConvLSTMs and ConvGRUs. Moreover, our models also achieve lower prediction errors in both domains, even in closed-loop autoregressive mode. These findings demonstrate that minimal recurrent structures, when combined with convolutional input aggregation, offer a compelling and efficient alternative for spatiotemporal sequence modeling, bridging the gap between recurrent simplicity and spatial complexity.

