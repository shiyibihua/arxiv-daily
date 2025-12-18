---
layout: default
title: Muon Outperforms Adam in Tail-End Associative Memory Learning
---

# Muon Outperforms Adam in Tail-End Associative Memory Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26030" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26030v2</a>
  <a href="https://arxiv.org/pdf/2509.26030.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26030v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26030v2', 'Muon Outperforms Adam in Tail-End Associative Memory Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuche Wang, Fengzhuo Zhang, Jiaxiang Li, Cunxiao Du, Chao Du, Tianyu Pang, Zhuoran Yang, Mingyi Hong, Vincent Y. F. Tan

**分类**: cs.LG, cs.AI, math.OC

**发布日期**: 2025-09-30 (更新: 2025-10-05)

---

## 💡 一句话要点

**Muon优化器在长尾关联记忆学习中优于Adam，通过奇异谱分析揭示其优势**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Muon优化器` `Adam优化器` `长尾学习` `关联记忆` `奇异谱分析`

## 📋 核心要点

1. 大型语言模型训练中，Muon优化器表现优于Adam，但其内在机制尚不明确。
2. 论文从关联记忆角度出发，发现Muon的优势主要体现在对Value/Output注意力权重和前馈网络的优化上。
3. 理论分析表明，Muon在处理类别不平衡数据时，能更有效地优化尾部类别，实现更平衡的学习。

## 📝 摘要（中文）

Muon优化器在训练大型语言模型（LLMs）时始终比Adam更快，但其成功机制尚不清楚。本文通过关联记忆的视角揭示了这一机制。通过消融Muon优化的Transformer组件，我们发现LLM的关联记忆参数，即Value和Output（VO）注意力权重以及前馈网络（FFN），是Muon优越性的主要贡献者。受这种关联记忆观点的启发，我们解释了Muon在真实语料库上的优越性，这些语料库本质上是重尾的：一些类别（尾部类别）出现的频率远低于其他类别。这种优越性可以通过两个关键属性来解释：（i）它的更新规则始终产生比Adam更各向同性的奇异谱；因此，（ii）在重尾数据上，它比Adam更有效地优化尾部类别。除了经验证据外，我们通过分析类不平衡数据下的单层关联记忆模型，从理论上证实了这些发现。我们证明，无论特征嵌入如何，Muon始终实现跨类别的平衡学习，而Adam可能会根据嵌入属性导致学习误差的巨大差异。总而言之，我们的经验观察和理论分析揭示了Muon的核心优势：它的更新规则与线性关联记忆的外积结构对齐，从而能够比Adam更平衡和有效地学习重尾分布中的尾部类别。

## 🔬 方法详解

**问题定义**：现有的大型语言模型训练中，Adam优化器被广泛使用，但在某些情况下，Muon优化器表现出更快的收敛速度。然而，Muon优化器优于Adam的原因尚不明确，尤其是在处理具有长尾分布的数据时，尾部类别的学习效果往往不佳。因此，论文旨在揭示Muon优化器在长尾数据上的优势机制，并从理论上进行验证。

**核心思路**：论文的核心思路是将大型语言模型中的关键组件（Value/Output注意力权重和前馈网络）视为关联记忆，并分析Muon优化器在更新这些关联记忆参数时的行为。通过奇异谱分析，发现Muon优化器能够产生更各向同性的奇异谱，从而更有效地学习尾部类别。

**技术框架**：论文的技术框架主要包括以下几个部分：1) 通过消融实验确定Muon优化器优势的关键组件；2) 对比Muon和Adam优化器在更新关联记忆参数时的奇异谱；3) 在真实语料库上验证Muon优化器在长尾数据上的性能；4) 建立单层关联记忆模型，从理论上分析Muon和Adam优化器在处理类别不平衡数据时的学习行为。

**关键创新**：论文最重要的技术创新点在于从关联记忆的角度解释了Muon优化器的优势，并揭示了其在处理长尾数据时的有效性。通过奇异谱分析，发现Muon优化器能够产生更各向同性的奇异谱，从而更有效地学习尾部类别。此外，论文还通过理论分析验证了Muon优化器在处理类别不平衡数据时的优越性。

**关键设计**：论文的关键设计包括：1) 使用消融实验来确定Muon优化器优势的关键组件；2) 使用奇异谱分析来比较Muon和Adam优化器在更新关联记忆参数时的行为；3) 建立单层关联记忆模型，并推导Muon和Adam优化器在处理类别不平衡数据时的学习误差。在理论分析中，论文假设数据具有类别不平衡的特性，并分析了不同特征嵌入对学习误差的影响。

## 📊 实验亮点

实验结果表明，Muon优化器在处理长尾数据时，能够更有效地优化尾部类别，从而提高模型的整体性能。理论分析表明，Muon优化器能够产生更各向同性的奇异谱，从而更有效地学习尾部类别。在单层关联记忆模型中，Muon优化器始终实现跨类别的平衡学习，而Adam优化器可能会根据嵌入属性导致学习误差的巨大差异。

## 🎯 应用场景

该研究成果可应用于各种需要处理长尾数据的机器学习任务，例如自然语言处理、图像识别和推荐系统。通过使用Muon优化器，可以更有效地学习尾部类别，提高模型的整体性能和泛化能力。此外，该研究也为优化器设计提供了新的思路，即考虑优化器与模型结构的匹配性。

## 📄 摘要（原文）

> The Muon optimizer is consistently faster than Adam in training Large Language Models (LLMs), yet the mechanism underlying its success remains unclear. This paper demystifies this mechanism through the lens of associative memory. By ablating the transformer components optimized by Muon, we reveal that the associative memory parameters of LLMs, namely the Value and Output (VO) attention weights and Feed-Forward Networks (FFNs), are the primary contributors to Muon's superiority. Motivated by this associative memory view, we then explain Muon's superiority on real-world corpora, which are intrinsically heavy-tailed: a few classes (tail classes) appear far less frequently than others. The superiority is explained through two key properties: (i) its update rule consistently yields a more isotropic singular spectrum than Adam; and as a result, (ii) on heavy-tailed data, it optimizes tail classes more effectively than Adam. Beyond empirical evidence, we theoretically confirm these findings by analyzing a one-layer associative memory model under class-imbalanced data. We prove that Muon consistently achieves balanced learning across classes regardless of feature embeddings, whereas Adam can induce large disparities in learning errors depending on embedding properties. In summary, our empirical observations and theoretical analyses reveal Muon's core advantage: its update rule aligns with the outer-product structure of linear associative memories, enabling more balanced and effective learning of tail classes in heavy-tailed distributions than Adam.

