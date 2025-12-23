---
layout: default
title: Semantic-guided Diverse Decoding for Large Language Model
---

# Semantic-guided Diverse Decoding for Large Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23601" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23601v2</a>
  <a href="https://arxiv.org/pdf/2506.23601.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23601v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23601v2', 'Semantic-guided Diverse Decoding for Large Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weijie Shi, Yue Cui, Yaguang Wu, Jingzhi Fang, Shibo Zhang, Mengze Li, Sirui Han, Jia Zhu, Jiajie Xu, Xiaofang Zhou

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-30 (更新: 2025-09-28)

---

## 💡 一句话要点

**提出语义引导的多样解码方法以解决大语言模型的语义多样性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `多样解码` `语义引导` `强化学习` `自然语言处理`

## 📋 核心要点

1. 现有方法在实现语义多样性方面存在不足，主要集中于词汇层面的多样性，限制了多样解码的有效性。
2. 本文提出的SemDiD方法通过在嵌入空间中直接操作，结合正交引导和动态排斥等机制，实现了语义上的显著区分。
3. 实验结果显示，SemDiD在多个任务上提升了最佳选择覆盖率，并加速了训练过程，同时提高了模型的准确性。

## 📝 摘要（中文）

大语言模型的多样解码在需要多个语义上不同的响应的应用中至关重要，但现有方法主要实现词汇而非语义的多样性。这一局限性显著制约了最佳选择策略、基于组的强化学习和数据合成。本文提出了语义引导的多样解码（SemDiD），该方法直接在嵌入空间中操作，通过正交方向引导、动态组间排斥和位置去偏概率评估三种互补机制平衡质量与多样性。实验表明，SemDiD在多个任务中始终优于现有方法，最佳选择覆盖率提高了1.4-5.2%，同时加速了RLHF训练收敛15%，准确率提高了最多2.1%。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在多样解码中缺乏语义多样性的问题。现有方法主要关注词汇层面的多样性，未能有效实现语义上的显著区分，限制了其在实际应用中的效果。

**核心思路**：SemDiD方法通过在嵌入空间中直接进行操作，采用正交方向引导、动态组间排斥和位置去偏概率评估三种机制，旨在平衡生成文本的质量与多样性，从而确保语义上的显著差异。

**技术框架**：该方法的整体架构包括三个主要模块：正交方向引导用于引导生成方向，动态组间排斥用于增加生成样本之间的语义差异，位置去偏概率评估用于优化生成的概率分布。

**关键创新**：SemDiD的核心创新在于其在嵌入空间中直接操作，通过三种互补机制实现语义多样性，这与传统方法的词汇层面调整有本质区别。

**关键设计**：在设计上，SemDiD采用自适应增益函数和约束优化来协调质量和多样性目标，确保生成文本达到质量阈值并实现最大语义区分。

## 📊 实验亮点

实验结果表明，SemDiD在多个任务中表现优异，最佳选择覆盖率提高了1.4-5.2%，同时加速了RLHF训练收敛15%，并在准确性上提升了最多2.1%。这些结果显示了该方法在实际应用中的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括对话系统、内容生成和数据合成等场景，能够为需要多样化响应的应用提供更高质量的解决方案。未来，SemDiD方法可能在提升人机交互的自然性和丰富性方面发挥重要作用。

## 📄 摘要（原文）

> Diverse decoding of large language models is crucial for applications requiring multiple semantically distinct responses, yet existing methods primarily achieve lexical rather than semantic diversity. This limitation significantly constrains Best-of-N strategies, group-based reinforcement learning, and data synthesis. While temperature sampling and diverse beam search modify token distributions or apply n-gram penalties, they fail to ensure meaningful semantic differentiation. We introduce Semantic-guided Diverse Decoding (SemDiD), operating directly in embedding space that balances quality with diversity through three complementary mechanisms: orthogonal directional guidance, dynamic inter-group repulsion, and position-debiased probability assessment. SemDiD harmonizes these competing objectives using adaptive gain functions and constraint optimization, ensuring both quality thresholds and maximal semantic differentiation. Experiments show SemDiD consistently outperforms existing methods, improving Best-of-N coverage by 1.4-5.2% across diverse tasks and accelerating RLHF training convergence by 15% while increasing accuracy by up to 2.1%.

