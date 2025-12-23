---
layout: default
title: Resisting Contextual Interference in RAG via Parametric-Knowledge Reinforcement
---

# Resisting Contextual Interference in RAG via Parametric-Knowledge Reinforcement

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05154" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05154v3</a>
  <a href="https://arxiv.org/pdf/2506.05154.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05154v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05154v3', 'Resisting Contextual Interference in RAG via Parametric-Knowledge Reinforcement')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenyu Lin, Yilin Wen, Du Su, Hexiang Tan, Fei Sun, Muhan Chen, Chenfu Bao, Zhonghou Lyu

**分类**: cs.CL, cs.AI, cs.IR

**发布日期**: 2025-06-05 (更新: 2025-09-29)

**🔗 代码/项目**: [GITHUB](https://github.com/lcy80366872/knowledgeable-R1)

---

## 💡 一句话要点

**提出Knowledgeable-R1以解决RAG中的上下文干扰问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `上下文干扰` `强化学习` `参数知识` `知识冲突` `推理准确性` `模型鲁棒性`

## 📋 核心要点

1. 现有的RAG方法在面对错误或冲突的检索文本时，容易导致模型产生级联错误，影响推理准确性。
2. 本文提出Knowledgeable-R1，通过强化学习框架训练模型使用参数知识抵抗上下文干扰，同时有效利用可靠的外部上下文。
3. 实验结果显示，Knowledgeable-R1在知识冲突场景中提高了鲁棒性和推理准确性，超越最先进基线23%，且在检索上下文准确时无性能下降。

## 📝 摘要（中文）

检索增强生成（RAG）在知识密集型任务中提升了性能，但错误、无关或冲突的检索文本可能导致模型依赖不准确的证据，从而引发级联错误。本文提出Knowledgeable-R1，一个强化学习框架，明确训练大型语言模型利用参数知识（PK）抵抗上下文干扰，同时在可靠的外部上下文中进行有效利用。Knowledgeable-R1引入了一种联合采样方案，生成有检索和无检索的配对响应，学习在相同输入下忽略误导性上下文与采纳它的时机。实验表明，Knowledgeable-R1在知识冲突场景和一般RAG场景中显著提高了鲁棒性和推理准确性，尤其在反事实场景中超越了最先进基线23%，且在检索上下文完全准确时没有性能下降。

## 🔬 方法详解

**问题定义**：本文旨在解决RAG模型在面对错误或冲突检索文本时的上下文干扰问题。现有方法容易导致模型依赖不准确的证据，从而引发级联错误，影响推理效果。

**核心思路**：提出Knowledgeable-R1框架，通过强化学习显式训练模型利用参数知识（PK）抵抗上下文干扰，同时在外部上下文有助时进行有效利用。

**技术框架**：Knowledgeable-R1采用联合采样方案，生成有检索和无检索的配对响应，学习在相同输入下的局部优势与全局优势，以量化何时忽略误导性上下文或采纳它。

**关键创新**：引入不对称优势转化，增强模型对参数知识的探索性行为，这是与现有方法的本质区别。

**关键设计**：在参数设置上，采用特定的损失函数和网络结构，以优化模型在不同解码模式下的表现，确保在知识冲突场景中提升推理准确性。

## 📊 实验亮点

实验结果表明，Knowledgeable-R1在知识冲突场景中显著提高了鲁棒性和推理准确性，超越最先进基线23%。在检索上下文完全准确的情况下，模型性能没有下降，显示出其优越的稳定性。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、对话生成和知识检索等场景。通过提高模型在知识冲突情况下的鲁棒性和推理能力，Knowledgeable-R1能够在实际应用中提供更准确的信息支持，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Retrieval-augmented generation (RAG) improves performance on knowledge-intensive tasks but can be derailed by wrong, irrelevant, or conflicting retrieved text, causing models to rely on inaccurate evidence and cascade errors. We propose Knowledgeable-R1, a reinforcement-learning framework that explicitly trains large language models to use parametric knowledge (PK) to resist contextual interference while still exploiting external context when it is reliably helpful. Knowledgeable-R1 introduces a joint sampling scheme that generates paired responses with and without retrieval, and learns both local advantages (within each decoding regime) and global advantages under the same input to quantify when to ignore misleading context versus adopt it. We employ an asymmetric advantage transformation that amplifies exploratory behaviors toward parametric knowledge. Experiments show that \method significantly improves robustness and reasoning accuracy in knowledge conflict scenarios and general RAG scenarios, outperforming SOTA baselines by 23% in counterfactual scenarios, and without degradation when the retrieved context is fully accurate.Our code are available at https://github.com/lcy80366872/knowledgeable-R1.

