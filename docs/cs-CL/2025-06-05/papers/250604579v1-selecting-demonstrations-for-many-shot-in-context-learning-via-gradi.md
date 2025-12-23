---
layout: default
title: Selecting Demonstrations for Many-Shot In-Context Learning via Gradient Matching
---

# Selecting Demonstrations for Many-Shot In-Context Learning via Gradient Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04579" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04579v1</a>
  <a href="https://arxiv.org/pdf/2506.04579.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04579v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04579v1', 'Selecting Demonstrations for Many-Shot In-Context Learning via Gradient Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianfei Zhang, Bei Li, Jun Bai, Rumei Li, Yanmeng Wang, Chenghua Lin, Wenge Rong

**分类**: cs.CL

**发布日期**: 2025-06-05

**备注**: accepted to the ACL2025 Findings

---

## 💡 一句话要点

**提出梯度匹配方法以优化多示例上下文学习的演示选择**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `上下文学习` `梯度匹配` `演示选择` `大型语言模型` `机器学习`

## 📋 核心要点

1. 现有的多示例上下文学习方法主要依赖随机选择演示，缺乏有效的选择机制，限制了其性能。
2. 本文提出了一种基于梯度匹配的演示选择方法，通过对齐微调梯度来优化示例选择。
3. 实验结果显示，该方法在多个数据集上优于随机选择，尤其在较大模型上提升显著，验证了其有效性。

## 📝 摘要（中文）

上下文学习（ICL）使大型语言模型（LLMs）能够快速适应任务，但演示选择的依赖性仍然是一个关键挑战。现有的多示例ICL方法主要依赖随机选择演示，缺乏有效的选择机制。本文提出了一种新颖的梯度匹配方法，通过对齐目标任务的整个训练集与所选示例之间的微调梯度，从而在所选示例中接近整个训练集的学习效果。实验结果表明，该方法在多个数据集上显著优于随机选择，尤其在较大的LLMs上表现出4%至2%的提升，推动了多示例ICL的可靠性和有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决多示例上下文学习中演示选择的有效性问题。现有方法主要依赖随机选择，无法充分利用数据的潜在信息，导致性能不足。

**核心思路**：提出了一种梯度匹配的方法，通过对齐目标任务的微调梯度与所选示例的梯度，优化演示选择，从而在小样本上接近全样本的学习效果。

**技术框架**：该方法的整体架构包括数据预处理、梯度计算、演示选择和模型评估四个主要模块。首先，对目标任务的训练集进行梯度计算，然后通过梯度匹配选择最优演示，最后在模型上进行评估。

**关键创新**：最重要的创新在于通过梯度匹配实现演示选择的优化，这与传统的随机选择方法有本质区别，能够更有效地利用训练数据。

**关键设计**：在技术细节上，设置了特定的损失函数来衡量梯度对齐程度，并在小型模型（如Qwen2.5-3B和Llama3-8B）上进行实验验证，确保方法的有效性和可扩展性。

## 📊 实验亮点

实验结果表明，所提出的梯度匹配方法在多个数据集上均优于随机选择，特别是在Qwen2.5-72B和Llama3-70B模型上，提升幅度达到4%。此外，在5个闭源LLM上也实现了约2%的性能提升，验证了方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、机器翻译和对话系统等。通过优化演示选择，能够提升大型语言模型在多样化任务中的适应能力和性能，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> In-Context Learning (ICL) empowers Large Language Models (LLMs) for rapid task adaptation without Fine-Tuning (FT), but its reliance on demonstration selection remains a critical challenge. While many-shot ICL shows promising performance through scaled demonstrations, the selection method for many-shot demonstrations remains limited to random selection in existing work. Since the conventional instance-level retrieval is not suitable for many-shot scenarios, we hypothesize that the data requirements for in-context learning and fine-tuning are analogous. To this end, we introduce a novel gradient matching approach that selects demonstrations by aligning fine-tuning gradients between the entire training set of the target task and the selected examples, so as to approach the learning effect on the entire training set within the selected examples. Through gradient matching on relatively small models, e.g., Qwen2.5-3B or Llama3-8B, our method consistently outperforms random selection on larger LLMs from 4-shot to 128-shot scenarios across 9 diverse datasets. For instance, it surpasses random selection by 4% on Qwen2.5-72B and Llama3-70B, and by around 2% on 5 closed-source LLMs. This work unlocks more reliable and effective many-shot ICL, paving the way for its broader application.

