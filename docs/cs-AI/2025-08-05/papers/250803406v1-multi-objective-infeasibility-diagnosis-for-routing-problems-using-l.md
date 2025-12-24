---
layout: default
title: Multi-Objective Infeasibility Diagnosis for Routing Problems Using Large Language Models
---

# Multi-Objective Infeasibility Diagnosis for Routing Problems Using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03406" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03406v1</a>
  <a href="https://arxiv.org/pdf/2508.03406.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03406v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03406v1', 'Multi-Objective Infeasibility Diagnosis for Routing Problems Using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kai Li, Ruihao Zheng, Xinye Hao, Zhenkun Wang

**分类**: cs.AI

**发布日期**: 2025-08-05

---

## 💡 一句话要点

**提出多目标不可行性诊断方法以解决路由问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多目标优化` `不可行性诊断` `大型语言模型` `路由问题` `决策支持`

## 📋 核心要点

1. 现有方法在处理用户提出的矛盾需求时，难以有效诊断和调整不可行的优化模型，导致解决方案缺乏多样性。
2. 本文提出的MOID方法结合了LLM代理与多目标优化，能够生成多种可操作的解决方案，帮助用户理解和调整模型。
3. 实验结果显示，MOID在50种不可行路由问题上表现优越，能够在一次运行中提供多项实用的诊断建议，显著提升了模型可行性恢复的效率。

## 📝 摘要（中文）

在实际路由问题中，用户常常提出相互矛盾或不合理的需求，导致优化模型不可行，形成空的可行解集。现有基于大型语言模型（LLM）的方法尝试诊断不可行模型，但在修改这些模型时往往未考虑多种潜在调整。为填补这一空白，本文提出了多目标不可行性诊断（MOID），结合LLM代理和多目标优化，提供一系列具有代表性的可操作建议。MOID通过多目标优化同时考虑路径成本和约束违反，生成一组权衡解决方案，并利用LLM代理生成解决方案分析函数，分析这些解决方案以诊断原始不可行模型。最后，MOID在50种不可行路由问题上与多种LLM方法进行了比较，结果表明MOID在一次运行中自动生成多项诊断建议，为恢复模型可行性和决策提供了更实用的见解。

## 🔬 方法详解

**问题定义**：本文旨在解决用户提出的矛盾或不合理需求导致的路由优化模型不可行问题。现有方法未能充分考虑多种调整方案，限制了模型的可行性恢复。

**核心思路**：MOID方法通过结合LLM代理与多目标优化，生成多种权衡解决方案，帮助用户理解不同调整对模型可行性的影响，从而提供更全面的诊断建议。

**技术框架**：MOID的整体架构包括数据输入、LLM代理、优化模块和解决方案分析。首先，输入用户需求和约束条件，然后通过多目标优化生成解决方案，最后利用LLM代理分析这些解决方案并提供反馈。

**关键创新**：MOID的主要创新在于其结合了多目标优化与LLM代理，能够在一次运行中生成多项可操作的建议，显著提升了现有方法的诊断能力和实用性。

**关键设计**：在技术细节上，MOID设置了多目标优化的权重参数，以平衡路径成本与约束违反，同时设计了适应性强的损失函数，以确保生成的解决方案具有实际可操作性。

## 📊 实验亮点

实验结果表明，MOID在50种不可行路由问题上相较于现有LLM方法，能够在一次运行中自动生成多项诊断建议，提升了模型可行性恢复的效率，提供了更实用的决策支持。

## 🎯 应用场景

该研究的潜在应用领域包括物流调度、交通管理和供应链优化等场景，能够帮助决策者在面对复杂约束时更有效地恢复模型的可行性。未来，MOID方法有望在智能交通系统和自动化调度系统中发挥重要作用，提升整体效率和决策质量。

## 📄 摘要（原文）

> In real-world routing problems, users often propose conflicting or unreasonable requirements, which result in infeasible optimization models due to overly restrictive or contradictory constraints, leading to an empty feasible solution set. Existing Large Language Model (LLM)-based methods attempt to diagnose infeasible models, but modifying such models often involves multiple potential adjustments that these methods do not consider. To fill this gap, we introduce Multi-Objective Infeasibility Diagnosis (MOID), which combines LLM agents and multi-objective optimization within an automatic routing solver, to provide a set of representative actionable suggestions. Specifically, MOID employs multi-objective optimization to consider both path cost and constraint violation, generating a set of trade-off solutions, each encompassing varying degrees of model adjustments. To extract practical insights from these solutions, MOID utilizes LLM agents to generate a solution analysis function for the infeasible model. This function analyzes these distinct solutions to diagnose the original infeasible model, providing users with diverse diagnostic insights and suggestions. Finally, we compare MOID with several LLM-based methods on 50 types of infeasible routing problems. The results indicate that MOID automatically generates multiple diagnostic suggestions in a single run, providing more practical insights for restoring model feasibility and decision-making compared to existing methods.

