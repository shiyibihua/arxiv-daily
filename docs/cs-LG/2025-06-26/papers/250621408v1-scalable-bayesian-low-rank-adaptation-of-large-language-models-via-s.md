---
layout: default
title: Scalable Bayesian Low-Rank Adaptation of Large Language Models via Stochastic Variational Subspace Inference
---

# Scalable Bayesian Low-Rank Adaptation of Large Language Models via Stochastic Variational Subspace Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21408" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21408v1</a>
  <a href="https://arxiv.org/pdf/2506.21408.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21408v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21408v1', 'Scalable Bayesian Low-Rank Adaptation of Large Language Models via Stochastic Variational Subspace Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Colin Samplawski, Adam D. Cobb, Manoj Acharya, Ramneet Kaur, Susmit Jha

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-26

**备注**: Accepted at UAI 2025

---

## 💡 一句话要点

**提出ScalaBL以解决大语言模型的不确定性量化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `贝叶斯深度学习` `低秩适应` `语言模型` `不确定性量化` `高风险领域` `参数效率` `模型扩展`

## 📋 核心要点

1. 现有的贝叶斯深度学习方法在处理大型语言模型时面临参数扩展的挑战，导致性能受限。
2. 本研究提出ScalaBL，通过在低秩适应的子空间中进行贝叶斯推断，显著减少了所需参数数量。
3. 实验结果表明，ScalaBL在性能上与最先进的方法相当，同时能够处理更大规模的模型。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）被广泛使用，但它们常常会产生错误信息并且校准效果不佳。因此，对这些模型的不确定性量化至关重要，尤其是在自主系统和医疗等高风险领域。以往的研究通过对微调模型的低秩适应（LoRA）参数进行推断，使得基于贝叶斯深度学习的方法更为可行。然而，这些方法在扩展到更大规模的LLMs时面临挑战，因为它们需要比LoRA更多的额外参数。本研究提出了可扩展的贝叶斯低秩适应方法（ScalaBL），通过在r维子空间中进行贝叶斯推断，利用LoRA参数作为投影矩阵，将样本映射到LLM的全权重空间。尽管子空间维度较低，我们仍能在仅需约1000个额外参数的情况下，取得与最先进方法相当的性能，并能够扩展到迄今为止最大的贝叶斯LLM。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在不确定性量化方面的不足，尤其是在高风险领域的应用中，现有方法在扩展性和参数效率上存在痛点。

**核心思路**：论文提出的ScalaBL方法通过在低秩适应的子空间中进行贝叶斯推断，利用LoRA参数作为投影矩阵，从而有效地将样本映射到LLM的全权重空间，减少了额外参数的需求。

**技术框架**：ScalaBL的整体架构包括低秩适应的子空间推断模块和全权重空间映射模块。首先，在r维子空间中进行贝叶斯推断，然后通过投影矩阵将结果映射到完整的模型权重中。

**关键创新**：ScalaBL的主要创新在于通过低维子空间的贝叶斯推断实现了对大型语言模型的有效适应，显著降低了所需的额外参数数量，与传统方法相比具有本质区别。

**关键设计**：在参数设置上，ScalaBL仅需约1000个额外参数，损失函数设计上采用了适应性贝叶斯推断策略，确保了模型的有效性和稳定性。整体网络结构保持了高效性，适应了大规模模型的需求。

## 📊 实验亮点

实验结果显示，ScalaBL在仅需约1000个额外参数的情况下，能够与当前最先进的贝叶斯方法相媲美，且成功扩展到拥有四倍于以往基线参数的最大贝叶斯LLM，展现出优越的性能和扩展能力。

## 🎯 应用场景

该研究的潜在应用领域包括自主系统、医疗健康、金融决策等高风险场景，能够为这些领域提供更为可靠的模型不确定性量化，提升决策的安全性和有效性。未来，ScalaBL有望推动大型语言模型在更多实际应用中的落地，尤其是在需要高可靠性的任务中。

## 📄 摘要（原文）

> Despite their widespread use, large language models (LLMs) are known to hallucinate incorrect information and be poorly calibrated. This makes the uncertainty quantification of these models of critical importance, especially in high-stakes domains, such as autonomy and healthcare. Prior work has made Bayesian deep learning-based approaches to this problem more tractable by performing inference over the low-rank adaptation (LoRA) parameters of a fine-tuned model. While effective, these approaches struggle to scale to larger LLMs due to requiring further additional parameters compared to LoRA. In this work we present $\textbf{Scala}$ble $\textbf{B}$ayesian $\textbf{L}$ow-Rank Adaptation via Stochastic Variational Subspace Inference (ScalaBL). We perform Bayesian inference in an $r$-dimensional subspace, for LoRA rank $r$. By repurposing the LoRA parameters as projection matrices, we are able to map samples from this subspace into the full weight space of the LLM. This allows us to learn all the parameters of our approach using stochastic variational inference. Despite the low dimensionality of our subspace, we are able to achieve competitive performance with state-of-the-art approaches while only requiring ${\sim}1000$ additional parameters. Furthermore, it allows us to scale up to the largest Bayesian LLM to date, with four times as a many base parameters as prior work.

