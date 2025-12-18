---
layout: default
title: Expanding Reasoning Potential in Foundation Model by Learning Diverse Chains of Thought Patterns
---

# Expanding Reasoning Potential in Foundation Model by Learning Diverse Chains of Thought Patterns

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21124" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21124v2</a>
  <a href="https://arxiv.org/pdf/2509.21124.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21124v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21124v2', 'Expanding Reasoning Potential in Foundation Model by Learning Diverse Chains of Thought Patterns')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuemiao Zhang, Can Ren, Chengying Tu, Rongxiang Weng, Shuo Wang, Hongfei Yan, Jingang Wang, Xunliang Cai

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-25 (更新: 2025-09-26)

---

## 💡 一句话要点

**通过学习多样化思维链模式，提升基础模型推理潜力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `思维链` `推理潜力` `原子推理模式` `混合专家模型` `强化学习` `数据选择` `双粒度算法`

## 📋 核心要点

1. 现有方法在利用思维链数据时缺乏选择性，未能明确哪些数据类型能最有效地提升模型推理能力。
2. 论文提出通过学习多样化的、富含高价值推理模式的思维链数据来扩展基础模型的推理潜力。
3. 实验结果表明，仅使用10B token的精选思维链数据，MoE模型在AIME数据集上提升了9.58%，RL性能上限提升了7.81%。

## 📝 摘要（中文）

大型推理模型在复杂数学推理方面的最新进展得益于强化学习(RL)。在中期训练中加入长思维链(CoT)数据也被证明能显著提高推理深度。然而，当前的方法通常不加区分地使用CoT数据，留下了一个关键问题：哪种数据类型最有效地增强模型推理能力？本文首次将基础模型的推理潜力定义为正确回答问题所需的独立尝试次数的倒数，这与最终模型性能密切相关。然后，我们提出利用富含高价值推理模式的多样化数据来扩展推理潜力。具体来说，我们从CoT序列中提取原子推理模式，这些模式具有共性和归纳能力，并使用它们构建一个富含宝贵推理模式的核心参考集。此外，我们提出了一种双粒度算法，涉及推理模式链和token熵，有效地从数据池中选择与核心集对齐的高价值CoT数据(CoTP)，从而训练模型有效地掌握推理。仅10B token的CoTP数据就使85A6B混合专家(MoE)模型在具有挑战性的AIME 2024和2025上提高了9.58%，并将下游RL性能的上限提高了7.81%。

## 🔬 方法详解

**问题定义**：论文旨在解决如何更有效地利用思维链(CoT)数据来提升大型语言模型(LLM)的推理能力。现有方法通常不加区分地使用CoT数据，导致训练效率低下，且未能充分挖掘CoT数据中蕴含的推理模式。因此，如何选择和利用高价值的CoT数据成为一个关键问题。

**核心思路**：论文的核心思路是通过学习多样化的推理模式来扩展基础模型的推理潜力。具体来说，首先从CoT数据中提取原子推理模式，构建一个核心参考集。然后，利用双粒度算法，基于推理模式链和token熵，从数据池中选择与核心集对齐的高价值CoT数据(CoTP)进行训练。这种方法旨在让模型学习到更有效、更通用的推理策略。

**技术框架**：整体框架包含以下几个主要步骤：1) 从CoT数据中抽象原子推理模式；2) 构建包含高价值推理模式的核心参考集；3) 使用双粒度算法（推理模式链和token熵）从数据池中选择高价值CoTP数据；4) 使用选择的CoTP数据训练模型。双粒度算法同时考虑了推理模式的匹配程度和token级别的信息量，以更精确地选择有价值的CoT数据。

**关键创新**：论文的关键创新在于：1) 首次提出了“推理潜力”的概念，并将其定义为正确回答问题所需的独立尝试次数的倒数；2) 提出了基于原子推理模式的CoT数据选择方法，能够更有效地选择高价值的CoT数据；3) 提出了双粒度算法，结合了推理模式链和token熵，提高了CoT数据选择的准确性。

**关键设计**：在原子推理模式的提取上，论文可能采用了一些启发式规则或聚类算法来识别CoT序列中的常见模式。在双粒度算法中，推理模式链的匹配程度可能通过计算相似度或使用预训练模型进行编码来实现。Token熵则用于衡量CoT序列中每个token的信息量，高熵的token可能包含更重要的推理信息。具体的参数设置和损失函数细节在论文中可能有所描述，但摘要中未提及。

## 📊 实验亮点

实验结果显示，仅使用10B token的精选CoTP数据，85A6B MoE模型在具有挑战性的AIME 2024和2025数据集上取得了9.58%的性能提升，并且将下游强化学习性能的上限提高了7.81%。这些结果表明，该方法能够有效地提升模型的推理能力，并为后续研究提供了有力的支持。

## 🎯 应用场景

该研究成果可应用于各种需要复杂推理能力的场景，例如数学问题求解、代码生成、知识图谱推理等。通过提升基础模型的推理能力，可以提高这些应用场景的性能和效率，并为开发更智能的AI系统奠定基础。此外，该方法还可以用于提升其他类型任务的模型性能，具有广泛的应用前景。

## 📄 摘要（原文）

> Recent progress in large reasoning models for challenging mathematical reasoning has been driven by reinforcement learning (RL). Incorporating long chain-of-thought (CoT) data during mid-training has also been shown to substantially improve reasoning depth. However, current approaches often utilize CoT data indiscriminately, leaving open the critical question of which data types most effectively enhance model reasoning capabilities. In this paper, we define the foundation model's reasoning potential for the first time as the inverse of the number of independent attempts required to correctly answer the question, which is strongly correlated with the final model performance. We then propose utilizing diverse data enriched with high-value reasoning patterns to expand the reasoning potential. Specifically, we abstract atomic reasoning patterns from CoT sequences, characterized by commonality and inductive capabilities, and use them to construct a core reference set enriched with valuable reasoning patterns. Furthermore, we propose a dual-granularity algorithm involving chains of reasoning patterns and token entropy, efficiently selecting high-value CoT data (CoTP) from the data pool that aligns with the core set, thereby training models to master reasoning effectively. Only 10B-token CoTP data enables the 85A6B Mixture-of-Experts (MoE) model to improve by 9.58% on the challenging AIME 2024 and 2025, and to raise the upper bound of downstream RL performance by 7.81%.

