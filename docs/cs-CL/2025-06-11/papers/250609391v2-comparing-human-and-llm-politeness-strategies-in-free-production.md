---
layout: default
title: Comparing human and LLM politeness strategies in free production
---

# Comparing human and LLM politeness strategies in free production

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09391" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09391v2</a>
  <a href="https://arxiv.org/pdf/2506.09391.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09391v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09391v2', 'Comparing human and LLM politeness strategies in free production')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoran Zhao, Robert D. Hawkins

**分类**: cs.CL

**发布日期**: 2025-06-11 (更新: 2025-10-30)

**备注**: 25 pages, 5 figures \| EMNLP 2025 camera-ready version

---

## 💡 一句话要点

**比较人类与大型语言模型的礼貌策略以解决对齐挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `礼貌策略` `人机交互` `计算语用学` `自然语言处理`

## 📋 核心要点

1. 核心问题：现有大型语言模型在礼貌语言生成中面临对齐挑战，尤其是在信息与社交目标的平衡上。
2. 方法要点：通过比较人类与LLM在不同生成任务中的响应，探讨LLM是否具备上下文敏感的礼貌策略。
3. 实验或效果：研究发现，较大的模型能够复制关键的语用偏好，人类在开放式任务中偏好LLM生成的响应。

## 📝 摘要（中文）

礼貌语言在大型语言模型（LLMs）中提出了基本的对齐挑战。人类使用丰富的语言策略来平衡信息和社交目标，包括建立关系的积极策略和减少负担的消极策略。本文通过比较人类与LLM在受限和开放式生成任务中的响应，探讨LLM是否采用类似的上下文敏感策略。研究发现，参数超过70B的模型成功复制了计算语用学文献中的关键偏好，且人类评估者在开放式上下文中意外偏好LLM生成的响应。然而，进一步的语言分析显示，模型在积极上下文中不成比例地依赖消极礼貌策略，可能导致误解。尽管现代LLM在礼貌策略上表现出色，但这些微妙的差异引发了关于AI系统中语用对齐的重要问题。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在生成礼貌语言时的对齐问题，现有方法在处理信息与社交目标的平衡上存在不足，尤其是在上下文敏感性方面。

**核心思路**：研究通过比较人类与LLM的响应，探讨LLM是否能够采用类似于人类的礼貌策略，特别是在不同的生成任务中。这样的设计旨在揭示LLM在礼貌语言生成中的潜力与局限。

**技术框架**：整体架构包括两个主要阶段：首先是受限生成任务，其次是开放式生成任务。在每个阶段中，收集人类与LLM的响应并进行比较分析。

**关键创新**：最重要的技术创新在于发现较大的LLM（参数≥70B）能够成功复制计算语用学中的关键偏好，这与现有的礼貌策略生成研究存在本质区别。

**关键设计**：在实验中，采用了多种评估指标来分析生成的响应，包括礼貌策略的使用频率和上下文适应性，确保模型在不同情境下的表现得到全面评估。

## 📊 实验亮点

实验结果显示，参数超过70B的LLM在开放式生成任务中获得了人类评估者的偏好，表明其在礼貌策略生成方面的有效性。此外，尽管LLM在某些上下文中表现出色，但其对消极礼貌策略的过度依赖可能导致误解，这一发现为未来的研究提供了重要的方向。

## 🎯 应用场景

该研究的潜在应用领域包括人机交互、智能客服和社交机器人等。通过优化LLM的礼貌策略，可以提升用户体验，增强人机沟通的自然性与有效性。未来，随着模型的进一步发展，可能会在更广泛的社交场景中应用这些策略，促进人类与AI的更好协作。

## 📄 摘要（原文）

> Polite speech poses a fundamental alignment challenge for large language models (LLMs). Humans deploy a rich repertoire of linguistic strategies to balance informational and social goals -- from positive approaches that build rapport (compliments, expressions of interest) to negative strategies that minimize imposition (hedging, indirectness). We investigate whether LLMs employ a similarly context-sensitive repertoire by comparing human and LLM responses in both constrained and open-ended production tasks. We find that larger models ($\ge$70B parameters) successfully replicate key preferences from the computational pragmatics literature, and human evaluators surprisingly prefer LLM-generated responses in open-ended contexts. However, further linguistic analyses reveal that models disproportionately rely on negative politeness strategies even in positive contexts, potentially leading to misinterpretations. While modern LLMs demonstrate an impressive handle on politeness strategies, these subtle differences raise important questions about pragmatic alignment in AI systems.

