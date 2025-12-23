---
layout: default
title: Early Stopping Tabular In-Context Learning
---

# Early Stopping Tabular In-Context Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21387" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21387v2</a>
  <a href="https://arxiv.org/pdf/2506.21387.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21387v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21387v2', 'Early Stopping Tabular In-Context Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jaris Küken, Lennart Purucker, Frank Hutter

**分类**: cs.LG

**发布日期**: 2025-06-26 (更新: 2025-06-28)

**备注**: ICML Workshop Paper

---

## 💡 一句话要点

**提出早停机制以提升表格上下文学习的推理效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `表格学习` `上下文学习` `早停机制` `推理效率` `Transformer`

## 📋 核心要点

1. 现有表格基础模型在推理时成本较高，尤其是面对大规模数据集时，效率亟待提升。
2. 本文提出在上下文学习过程中动态评估是否早停，从而减少不必要的计算，提高推理速度。
3. 实验结果显示，早停机制在小型分类任务中加速推理最高可达1.3倍，在大型任务中可达2.2倍，且预测性能保持稳定。

## 📝 摘要（中文）

表格基础模型在多种表格学习任务中通过上下文学习展现了强大的性能，且无需下游微调即可实现稳健的泛化。然而，其推理时间成本仍然较高，尤其是在处理较大数据集时。为了解决这一问题，本文提出在上下文学习过程中实施早停机制，通过动态评估在每个Transformer编码器层后是否停止学习。一旦停止，利用预训练的逐层解码器解码嵌入。实验结果表明，早停机制在34个小型分类任务中加速推理速度最高可达1.3倍，且预测性能几乎没有下降。在五个较大分类任务上的评估显示，速度提升可达2.2倍，证明了早停作为提高表格上下文学习效率的有效实用策略的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决表格基础模型在推理时的高时间成本问题，尤其是在处理大规模数据集时，现有方法的效率不足以满足实际需求。

**核心思路**：通过在上下文学习过程中实施早停机制，动态评估每个Transformer编码器层后是否继续学习，从而减少不必要的计算，提高推理效率。

**技术框架**：整体架构包括Transformer编码器和逐层解码器。首先，输入数据经过多个编码器层处理，随后在每层后进行动态评估，决定是否停止学习。一旦决定停止，使用预训练的解码器对嵌入进行解码，输出最终结果。

**关键创新**：最重要的创新点在于引入了动态早停机制，使得模型能够在推理过程中根据当前状态决定是否继续计算，这与传统方法的固定计算流程形成鲜明对比。

**关键设计**：在设计中，动态评估机制的实现依赖于对每个编码器层输出的实时分析，确保在保持预测性能的同时，最大限度地减少计算资源的消耗。

## 📊 实验亮点

实验结果显示，早停机制在34个小型分类任务中加速推理速度最高可达1.3倍，且预测性能几乎没有下降。在五个较大分类任务上的评估中，速度提升可达2.2倍，展示了该方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括金融、医疗和市场分析等需要处理大量表格数据的行业。通过提高推理效率，能够加速决策过程，提升业务响应速度，具有显著的实际价值和未来影响。

## 📄 摘要（原文）

> Tabular foundation models have shown strong performance across various tabular learning tasks via in-context learning, offering robust generalization without any downstream finetuning. However, their inference-time costs remain high, particularly for larger datasets. To address this, we propose early-stopping the in-context learning process. We achieve this by dynamically evaluating whether to stop in-context learning after each Transformer encoder layer. Once stopped, we decode the embedding using a pre-trained layer-wise decoder. Experiments across 34 small classification tasks size show that early stopping in-context learning accelerates inference by up to x1.3 with negligible degradation in predictive performance. To assess scalability, we further evaluate our method on five larger classification tasks, achieving speedups of up to x2.2. Our results demonstrate the potential of early exiting as an effective and practical strategy for improving the efficiency of tabular in-context learning.

