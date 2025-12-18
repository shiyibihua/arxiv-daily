---
layout: default
title: Improving constraint-based discovery with robust propagation and reliable LLM priors
---

# Improving constraint-based discovery with robust propagation and reliable LLM priors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23570" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23570v1</a>
  <a href="https://arxiv.org/pdf/2509.23570.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23570v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23570v1', 'Improving constraint-based discovery with robust propagation and reliable LLM priors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruiqi Lyu, Alistair Turcan, Martin Jinye Zhang, Bryan Wilder

**分类**: cs.LG

**发布日期**: 2025-09-28

---

## 💡 一句话要点

**MosaCD：结合鲁棒传播与可靠LLM先验改进基于约束的因果发现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `因果发现` `条件独立性测试` `大型语言模型` `边缘方向传播` `鲁棒性` `置信度下降` `图结构学习`

## 📋 核心要点

1. 传统基于约束的因果发现方法依赖于完美的条件独立性测试，易受误差累积的影响。
2. MosaCD结合条件独立性测试和LLM先验知识，通过高置信度种子进行边缘方向传播。
3. 实验表明，MosaCD在真实世界图上比现有方法具有更高的图结构恢复准确率。

## 📝 摘要（中文）

从观测数据中学习因果结构是科学建模和决策制定的核心。基于约束的方法旨在恢复因果有向无环图(DAG)中的条件独立(CI)关系。传统的PC算法及其后续方法首先确定v结构，然后从这些种子传播边缘方向，但它们假设完美的CI测试和分离子集的穷举搜索。这些假设在实践中经常被违反，导致最终图中的级联错误。最近的研究探索了使用大型语言模型(LLM)作为专家，提示节点集合以确定边缘方向，这可以在假设不满足时增强边缘方向的确定。然而，这些方法隐含地假设了完美的专家，这对于容易产生幻觉的LLM来说是不现实的。我们提出了MosaCD，一种因果发现方法，它从CI测试和LLM注释中获得的高置信度种子集合传播边缘。为了过滤幻觉，我们引入了利用LLM位置偏差的洗牌查询，仅保留高置信度的种子。然后，我们应用一种新颖的置信度下降传播策略，该策略首先确定最可靠的边缘方向，并且可以与任何基于骨架的发现方法集成。在多个真实世界的图上，MosaCD在最终图构建中实现了比现有基于约束的方法更高的准确性，这主要归功于初始种子的改进可靠性和鲁棒的传播策略。

## 🔬 方法详解

**问题定义**：论文旨在解决基于约束的因果发现方法中，由于条件独立性测试不准确和误差传播导致的图结构恢复精度低的问题。现有方法依赖于完美的条件独立性测试和分离子集的穷举搜索，但在实际应用中这些假设往往不成立，导致级联错误。

**核心思路**：论文的核心思路是结合条件独立性测试和大型语言模型（LLM）的先验知识，利用两者提供的信息来更准确地确定因果图的结构。通过筛选LLM的输出，选择高置信度的种子边缘，并使用鲁棒的传播策略来减少误差累积。

**技术框架**：MosaCD方法主要包含以下几个阶段：1) 使用条件独立性测试初步构建图的骨架；2) 使用LLM对可能的边缘方向进行推断，并引入洗牌查询来过滤LLM的幻觉；3) 结合条件独立性测试和LLM的输出，选择高置信度的种子边缘；4) 使用置信度下降的传播策略，从高置信度的种子边缘开始，逐步确定剩余边缘的方向。

**关键创新**：MosaCD的关键创新在于：1) 结合了条件独立性测试和LLM的先验知识，利用LLM来弥补传统方法的不足；2) 提出了洗牌查询的方法来过滤LLM的幻觉，提高了LLM输出的可靠性；3) 采用了置信度下降的传播策略，优先确定高置信度的边缘方向，减少了误差传播。

**关键设计**：洗牌查询通过改变输入LLM的节点顺序，利用LLM的位置偏差来判断其输出的可靠性。只有在不同顺序下LLM输出一致的边缘方向才会被认为是高置信度的。置信度下降的传播策略则根据边缘方向的置信度进行排序，优先传播置信度高的边缘方向，避免低置信度的边缘方向影响其他边缘的确定。

## 📊 实验亮点

MosaCD在多个真实世界图上的实验结果表明，其在图结构恢复方面优于现有的基于约束的方法。具体来说，MosaCD在SHD（Structural Hamming Distance）指标上取得了显著的提升，表明其能够更准确地恢复因果图的结构。实验结果验证了MosaCD在提高初始种子可靠性和鲁棒传播策略方面的有效性。

## 🎯 应用场景

MosaCD可应用于多个领域，包括生物医学、社会科学和经济学等，在这些领域中，从观测数据中推断因果关系至关重要。例如，在生物医学中，可以用于发现基因之间的调控关系；在社会科学中，可以用于研究社会因素对个体行为的影响；在经济学中，可以用于分析经济政策对市场的影响。该方法能够提高因果推断的准确性，从而为决策提供更可靠的依据。

## 📄 摘要（原文）

> Learning causal structure from observational data is central to scientific modeling and decision-making. Constraint-based methods aim to recover conditional independence (CI) relations in a causal directed acyclic graph (DAG). Classical approaches such as PC and subsequent methods orient v-structures first and then propagate edge directions from these seeds, assuming perfect CI tests and exhaustive search of separating subsets -- assumptions often violated in practice, leading to cascading errors in the final graph. Recent work has explored using large language models (LLMs) as experts, prompting sets of nodes for edge directions, and could augment edge orientation when assumptions are not met. However, such methods implicitly assume perfect experts, which is unrealistic for hallucination-prone LLMs. We propose MosaCD, a causal discovery method that propagates edges from a high-confidence set of seeds derived from both CI tests and LLM annotations. To filter hallucinations, we introduce shuffled queries that exploit LLMs' positional bias, retaining only high-confidence seeds. We then apply a novel confidence-down propagation strategy that orients the most reliable edges first, and can be integrated with any skeleton-based discovery method. Across multiple real-world graphs, MosaCD achieves higher accuracy in final graph construction than existing constraint-based methods, largely due to the improved reliability of initial seeds and robust propagation strategies.

