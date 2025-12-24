---
layout: default
title: A Case Study on the Effectiveness of LLMs in Verification with Proof Assistants
---

# A Case Study on the Effectiveness of LLMs in Verification with Proof Assistants

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18587" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18587v1</a>
  <a href="https://arxiv.org/pdf/2508.18587.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18587v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18587v1', 'A Case Study on the Effectiveness of LLMs in Verification with Proof Assistants')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Barış Bayazıt, Yao Li, Xujie Si

**分类**: cs.PL, cs.AI

**发布日期**: 2025-08-26

**备注**: Accepted by LMPL 2025

**DOI**: [10.1145/3759425.3763391](https://doi.org/10.1145/3759425.3763391)

---

## 💡 一句话要点

**研究大型语言模型在证明助手中的验证效果**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `证明助手` `形式化验证` `自动化证明` `Rocq项目`

## 📋 核心要点

1. 现有方法在验证过程中对大型语言模型的有效性缺乏系统评估，尤其是在不同项目中的表现差异未被充分探讨。
2. 本文通过案例研究，分析LLMs在生成证明中的作用，特别关注外部依赖和上下文对证明生成的影响。
3. 研究结果表明，LLMs在小型和大型证明生成中均有良好表现，但在不同项目中效果存在显著差异，且可能出现错误。

## 📝 摘要（中文）

大型语言模型（LLMs）有潜力通过自动化证明来帮助验证，但其在此任务中的有效性尚不明确。本文基于两个成熟的Rocq项目：hs-to-coq工具和Verdi，进行案例研究，评估LLMs在生成证明方面的有效性。研究发现：外部依赖和同一源文件中的上下文可以显著帮助证明生成；LLMs在小型证明上表现出色，也能生成大型证明；不同验证项目上LLMs的表现差异明显；LLMs能够生成简洁且智能的证明，应用经典技术于新定义，但也可能出现奇怪的错误。

## 🔬 方法详解

**问题定义**：本文旨在评估大型语言模型在使用证明助手进行验证时的有效性，现有方法未能充分探讨LLMs在不同项目中的表现差异及其影响因素。

**核心思路**：通过对两个成熟的Rocq项目进行案例研究，分析外部依赖和上下文对证明生成的影响，以此评估LLMs的实际应用效果。

**技术框架**：研究采用定量与定性分析相结合的方法，首先收集和整理项目数据，然后通过LLMs生成证明，最后对生成结果进行评估和比较。

**关键创新**：本研究首次系统性地探讨了LLMs在不同验证项目中的表现差异，揭示了外部依赖和上下文对证明生成的重要性。

**关键设计**：在实验中，设置了不同的上下文和依赖条件，使用了多种评估指标来量化证明的质量和生成效率。

## 📊 实验亮点

实验结果显示，LLMs在小型证明生成中表现优异，且在大型证明生成方面也取得了显著进展。研究发现，外部依赖和上下文的有效利用显著提升了证明生成的质量，LLMs在不同项目中的表现差异为后续研究提供了新的方向。

## 🎯 应用场景

该研究为大型语言模型在形式化验证领域的应用提供了实证支持，具有重要的实际价值。通过优化证明生成过程，LLMs可以在软件验证、形式化方法和自动化推理等领域发挥更大作用，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Large language models (LLMs) can potentially help with verification using proof assistants by automating proofs. However, it is unclear how effective LLMs are in this task. In this paper, we perform a case study based on two mature Rocq projects: the hs-to-coq tool and Verdi. We evaluate the effectiveness of LLMs in generating proofs by both quantitative and qualitative analysis. Our study finds that: (1) external dependencies and context in the same source file can significantly help proof generation; (2) LLMs perform great on small proofs but can also generate large proofs; (3) LLMs perform differently on different verification projects; and (4) LLMs can generate concise and smart proofs, apply classical techniques to new definitions, but can also make odd mistakes.

