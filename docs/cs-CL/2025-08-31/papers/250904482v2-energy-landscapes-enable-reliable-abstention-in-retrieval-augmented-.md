---
layout: default
title: Energy Landscapes Enable Reliable Abstention in Retrieval-Augmented Large Language Models for Healthcare
---

# Energy Landscapes Enable Reliable Abstention in Retrieval-Augmented Large Language Models for Healthcare

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04482" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04482v2</a>
  <a href="https://arxiv.org/pdf/2509.04482.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04482v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04482v2', 'Energy Landscapes Enable Reliable Abstention in Retrieval-Augmented Large Language Models for Healthcare')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ravi Shankar, Sheng Wong, Lin Li, Magdalena Bachmann, Alex Silverthorne, Beth Albert, Gabriel Davis Jones

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-31 (更新: 2025-09-08)

---

## 💡 一句话要点

**提出能量基础模型以解决医疗领域检索增强生成系统的可靠性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `能量基础模型` `检索增强生成` `医疗健康` `放弃决策` `安全关键领域` `语义理解` `机器学习`

## 📋 核心要点

1. 现有的检索增强生成系统在安全关键领域的放弃决策上存在不足，错误的回答可能导致严重后果。
2. 本文提出的能量基础模型通过学习语义语料库的能量景观，帮助系统更好地判断何时生成答案或放弃。
3. 实验结果显示，EBM在语义困难的放弃案例中表现优越，AUROC达到0.961，显著提高了放弃决策的可靠性。

## 📝 摘要（中文）

在检索增强生成（RAG）系统中，可靠的放弃决策对于安全关键领域（如女性健康）至关重要，因为错误答案可能导致伤害。本文提出了一种能量基础模型（EBM），该模型在一个包含260万条指南派生问题的密集语义语料库上学习平滑的能量景观，从而使系统能够决定何时生成答案或选择放弃。通过与经过校准的softmax基线和k近邻密度启发式方法进行基准测试，EBM在语义困难的放弃案例中表现优越，AUROC达到0.961，相较于softmax的0.950，同时在95%的假阳性率下减少了FPR（0.235对比0.331）。这些结果表明，能量基础的放弃评分提供了比基于概率的softmax更可靠的信心信号，为安全的RAG系统提供了可扩展且可解释的基础。

## 🔬 方法详解

**问题定义**：本文旨在解决检索增强生成系统在医疗领域中的放弃决策不可靠的问题。现有方法在面对复杂的语义查询时，容易产生错误的回答，导致潜在的安全隐患。

**核心思路**：论文提出的能量基础模型（EBM）通过学习一个平滑的能量景观，使系统能够在生成答案和放弃之间做出更可靠的决策。这种设计旨在提高放弃决策的准确性，尤其是在语义困难的情况下。

**技术框架**：EBM的整体架构包括能量评分头和决策模块。首先，模型通过对大量的语义问题进行训练，学习到每个问题的能量值，然后根据能量值来判断是否生成答案或选择放弃。

**关键创新**：EBM的主要创新在于其能量评分机制，相较于传统的softmax概率评分，能量评分提供了更可靠的信心信号。这一机制使得模型在处理复杂查询时，能够更好地识别何时放弃。

**关键设计**：在模型设计中，采用了特定的损失函数来优化能量评分，同时通过控制负样本采样和公平数据暴露来进行全面的消融实验。模型的参数设置和网络结构经过精心设计，以确保在语义困难的情况下仍能保持良好的泛化能力。

## 📊 实验亮点

实验结果显示，EBM在语义困难的放弃案例中表现优越，AUROC达到0.961，相较于softmax的0.950，假阳性率在95%时降低至0.235，显著提高了放弃决策的可靠性，尤其在安全关键的分布中表现突出。

## 🎯 应用场景

该研究的潜在应用领域包括医疗健康、法律咨询和其他安全关键领域。在这些领域中，系统能够通过可靠的放弃决策，避免错误信息的传播，从而提高用户的安全性和信任度。未来，该模型的可扩展性和可解释性将为更多领域的智能系统提供支持。

## 📄 摘要（原文）

> Reliable abstention is critical for retrieval-augmented generation (RAG) systems, particularly in safety-critical domains such as women's health, where incorrect answers can lead to harm. We present an energy-based model (EBM) that learns a smooth energy landscape over a dense semantic corpus of 2.6M guideline-derived questions, enabling the system to decide when to generate or abstain. We benchmark the EBM against a calibrated softmax baseline and a k-nearest neighbour (kNN) density heuristic across both easy and hard abstention splits, where hard cases are semantically challenging near-distribution queries. The EBM achieves superior abstention performance abstention on semantically hard cases, reaching AUROC 0.961 versus 0.950 for softmax, while also reducing FPR@95 (0.235 vs 0.331). On easy negatives, performance is comparable across methods, but the EBM's advantage becomes most pronounced in safety-critical hard distributions. A comprehensive ablation with controlled negative sampling and fair data exposure shows that robustness stems primarily from the energy scoring head, while the inclusion or exclusion of specific negative types (hard, easy, mixed) sharpens decision boundaries but is not essential for generalisation to hard cases. These results demonstrate that energy-based abstention scoring offers a more reliable confidence signal than probability-based softmax confidence, providing a scalable and interpretable foundation for safe RAG systems.

