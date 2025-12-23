---
layout: default
title: Generalization or Hallucination? Understanding Out-of-Context Reasoning in Transformers
---

# Generalization or Hallucination? Understanding Out-of-Context Reasoning in Transformers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10887" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10887v3</a>
  <a href="https://arxiv.org/pdf/2506.10887.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10887v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10887v3', 'Generalization or Hallucination? Understanding Out-of-Context Reasoning in Transformers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yixiao Huang, Hanlin Zhu, Tianyu Guo, Jiantao Jiao, Somayeh Sojoudi, Michael I. Jordan, Stuart Russell, Song Mei

**分类**: cs.CL, cs.LG

**发布日期**: 2025-06-12 (更新: 2025-10-25)

**备注**: NeurIPS 2025, first three authors contributed equally

---

## 💡 一句话要点

**提出统一机制以理解变换器中的上下文推理现象**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `上下文外推理` `知识注入` `矩阵分解` `推理能力` `合成事实回忆` `梯度下降`

## 📋 核心要点

1. 现有大型语言模型在知识注入时表现出泛化与幻觉的双重性，原因尚不明确。
2. 本文提出上下文外推理（OCR）作为统一机制，解释模型如何通过概念关联进行推理。
3. 实验结果表明，单层单头注意力变换器能够有效解决OCR任务，展示了矩阵分解的关键作用。

## 📝 摘要（中文）

大型语言模型（LLMs）能够通过微调获取新知识，但这一过程表现出令人困惑的双重性：模型能够从新事实中显著泛化，但也容易产生错误信息的幻觉。本文提出，这两种行为源于一种称为上下文外推理（OCR）的单一机制，即通过关联概念推导含义的能力。我们在五个主要LLM上的实验确认，OCR确实驱动了泛化和幻觉，具体取决于关联概念是否存在因果关系。我们将OCR形式化为一种合成事实回忆任务，并展示了单层单头注意力变换器在此任务上的学习能力，强调了矩阵分解的重要性。我们的理论分析表明，OCR能力源于梯度下降的隐性偏差，解释了模型如何高效地学习关联事实和含义。最终，我们的工作为理解OCR现象提供了理论基础，并为分析和减轻知识注入带来的不良行为提供了新视角。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在知识注入过程中泛化与幻觉现象的原因，现有方法未能有效解释这一双重性。

**核心思路**：提出上下文外推理（OCR）作为统一机制，强调通过概念关联进行推理的能力，尤其是在因果关系不明确的情况下。

**技术框架**：研究中构建了一个单层单头注意力变换器，采用分解的输出和价值矩阵，进行合成事实回忆任务的学习。

**关键创新**：最重要的创新在于将OCR形式化为合成事实回忆任务，并展示了矩阵分解在学习过程中的重要性，与传统模型的结合权重方法形成鲜明对比。

**关键设计**：模型采用单层单头注意力机制，输出和价值矩阵进行分解，损失函数设计为最小化合并输出-价值矩阵的核范数，以此促进模型的高效学习。

## 📊 实验亮点

实验结果显示，单层单头注意力变换器在合成事实回忆任务中表现优异，成功学习到OCR能力，且在样本效率上显著优于结合权重的模型，展示了矩阵分解的关键作用。

## 🎯 应用场景

该研究为理解大型语言模型的推理能力提供了新的理论框架，潜在应用于改进知识注入技术，提升模型的推理准确性和可靠性。未来可在自然语言处理、知识图谱构建等领域发挥重要作用。

## 📄 摘要（原文）

> Large language models (LLMs) can acquire new knowledge through fine-tuning, but this process exhibits a puzzling duality: models can generalize remarkably from new facts, yet are also prone to hallucinating incorrect information. However, the reasons for this phenomenon remain poorly understood. In this work, we argue that both behaviors stem from a single mechanism known as out-of-context reasoning (OCR): the ability to deduce implications by associating concepts, even those without a causal link. Our experiments across five prominent LLMs confirm that OCR indeed drives both generalization and hallucination, depending on whether the associated concepts are causally related. To build a rigorous theoretical understanding of this phenomenon, we then formalize OCR as a synthetic factual recall task. We empirically show that a one-layer single-head attention-only transformer with factorized output and value matrices can learn to solve this task, while a model with combined weights cannot, highlighting the crucial role of matrix factorization. Our theoretical analysis shows that the OCR capability can be attributed to the implicit bias of gradient descent, which favors solutions that minimize the nuclear norm of the combined output-value matrix. This mathematical structure explains why the model learns to associate facts and implications with high sample efficiency, regardless of whether the correlation is causal or merely spurious. Ultimately, our work provides a theoretical foundation for understanding the OCR phenomenon, offering a new lens for analyzing and mitigating undesirable behaviors from knowledge injection.

