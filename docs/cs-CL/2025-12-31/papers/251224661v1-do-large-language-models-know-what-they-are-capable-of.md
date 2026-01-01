---
layout: default
title: Do Large Language Models Know What They Are Capable Of?
---

# Do Large Language Models Know What They Are Capable Of?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24661" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24661v1</a>
  <a href="https://arxiv.org/pdf/2512.24661.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24661v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24661v1', 'Do Large Language Models Know What They Are Capable Of?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Casey O. Barkan, Sid Black, Oliver Sourbut

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-31

**备注**: 23 pages, 8 figures

---

## 💡 一句话要点

**探讨大型语言模型的自我能力认知与决策改进**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `自我认知` `决策改进` `上下文学习` `多步骤任务`

## 📋 核心要点

1. 核心问题：现有大型语言模型在任务成功预测上普遍过度自信，缺乏对自身能力的准确评估。
2. 方法要点：研究通过多步骤任务和上下文经验，评估LLMs的自我认知与决策能力，探索改进策略。
3. 实验或效果：发现部分LLMs在经历失败后能够改善决策，但整体仍表现出过度乐观的倾向。

## 📝 摘要（中文）

本研究调查了大型语言模型（LLMs）是否能够预测其在特定任务上的成功率，以及在多步骤任务中随着进展其预测能力是否有所提升。研究发现，所有测试的LLMs普遍表现出过度自信，但大多数模型在成功预测上具有优于随机的判别能力。尽管较新和较大的LLMs通常没有更强的判别能力，但Claude模型显示出这一趋势。在多步骤任务中，部分前沿LLMs的过度自信随着任务进展而加剧，而推理型LLMs的表现与非推理型LLMs相当或更差。部分LLMs在经历失败的上下文经验后能够减少过度自信，从而显著改善决策，而其他模型则未能做到。这些结果表明，当前的LLM代理受限于对自身能力的缺乏认知。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在任务成功预测中的过度自信问题。现有方法未能有效评估模型的自我能力，导致决策失误。

**核心思路**：论文通过分析LLMs在多步骤任务中的表现，探讨其自我认知能力及如何通过上下文经验改善决策。设计的核心在于评估模型在不同任务阶段的自信程度与实际表现之间的关系。

**技术框架**：研究采用实验设计，分为任务预测、上下文经验学习和决策评估三个主要模块。每个模块通过不同的任务设置和评估标准进行验证。

**关键创新**：最重要的创新在于揭示了LLMs在多步骤任务中的过度自信现象及其对决策的影响，尤其是通过上下文学习来调整自信程度的能力。

**关键设计**：研究中采用了多种任务设置，评估模型在不同情境下的表现，关键参数包括任务复杂度、上下文信息的引入等，确保了实验的全面性与有效性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24661v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24661v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24661v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果显示，尽管所有LLMs普遍存在过度自信的问题，但大多数模型在成功预测上表现出优于随机的判别能力。部分LLMs在经历失败后能够显著改善决策，表明上下文学习对决策质量的提升具有重要作用。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化决策系统和人机交互等。通过提升LLMs的自我认知能力，可以有效减少决策失误，增强其在复杂任务中的应用价值，未来可能对AI的安全性和可靠性产生深远影响。

## 📄 摘要（原文）

> We investigate whether large language models (LLMs) can predict whether they will succeed on a given task and whether their predictions improve as they progress through multi-step tasks. We also investigate whether LLMs can learn from in-context experiences to make better decisions about whether to pursue a task in scenarios where failure is costly. All LLMs we tested are overconfident, but most predict their success with better-than-random discriminatory power. We find that newer and larger LLMs generally do not have greater discriminatory power, though Claude models do show such a trend. On multi-step agentic tasks, the overconfidence of several frontier LLMs worsens as they progress through the tasks, and reasoning LLMs perform comparably to or worse than non-reasoning LLMs. With in-context experiences of failure, some but not all LLMs reduce their overconfidence leading to significantly improved decision making, while others do not. Interestingly, all LLMs' decisions are approximately rational given their estimated probabilities of success, yet their overly-optimistic estimates result in poor decision making. These results suggest that current LLM agents are hindered by their lack of awareness of their own capabilities. We discuss the implications of LLMs' awareness of their capabilities for AI misuse and misalignment risks.

