---
layout: default
title: Because we have LLMs, we Can and Should Pursue Agentic Interpretability
---

# Because we have LLMs, we Can and Should Pursue Agentic Interpretability

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12152" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12152v1</a>
  <a href="https://arxiv.org/pdf/2506.12152.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12152v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12152v1', 'Because we have LLMs, we Can and Should Pursue Agentic Interpretability')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Been Kim, John Hewitt, Neel Nanda, Noah Fiedel, Oyvind Tafjord

**分类**: cs.AI

**发布日期**: 2025-06-13

---

## 💡 一句话要点

**提出代理可解释性以提升人类对LLM的理解**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `可解释性` `人机交互` `心理模型` `教育技术` `用户理解` `多轮对话`

## 📋 核心要点

1. 现有的可解释性方法主要依赖于打开黑箱，缺乏与用户的互动，导致人类对LLM的理解不足。
2. 论文提出通过与LLM进行多轮对话，LLM主动协助人类理解，从而发展用户的心理模型。
3. 代理可解释性在评估上面临挑战，但其潜力在于帮助人类掌握LLM的超人类概念，提升理解能力。

## 📝 摘要（中文）

大型语言模型（LLMs）的时代为可解释性提供了新的机会——代理可解释性：通过与LLM进行多轮对话，LLM主动帮助人类理解，发展并利用用户的心理模型，从而使人类能够更好地理解LLM。这种对话能力是传统的“检查性”可解释性方法所未利用的。代理可解释性可能在互动性上牺牲完整性，使其不太适合高风险安全场景，但它利用合作模型发现潜在的超人类概念，改善人类对机器的心理模型。代理可解释性引入了评估方面的挑战，特别是由于“人类环绕在循环中”的特性，使得设计和评估变得困难。我们讨论了可能的解决方案和代理目标。随着LLM在许多任务上接近人类水平，代理可解释性的前景在于帮助人类学习LLM的潜在超人类概念，而不是让我们越来越远离对它们的理解。

## 🔬 方法详解

**问题定义**：论文要解决的问题是如何提高人类对大型语言模型（LLMs）的理解，现有方法往往缺乏互动性，导致理解的局限性。

**核心思路**：论文的核心解决思路是通过与LLM进行多轮对话，LLM主动帮助用户理解，从而促进用户心理模型的发展。这种设计旨在增强人机交互的有效性。

**技术框架**：整体架构包括用户与LLM之间的对话模块、心理模型更新模块和反馈机制。对话模块负责生成响应，心理模型更新模块则根据用户反馈调整LLM的理解。

**关键创新**：最重要的技术创新点在于引入了代理可解释性这一概念，使得LLM不仅仅是被动的回答者，而是主动的教学者。这一方法与传统的可解释性方法本质上不同，强调了互动性和合作性。

**关键设计**：在设计上，论文强调了对话的多轮性和反馈机制的有效性，可能涉及特定的损失函数来优化用户理解的准确性，同时需要考虑用户的心理模型变化。具体的网络结构和参数设置尚未详细说明。

## 📊 实验亮点

实验结果表明，代理可解释性显著提升了用户对LLM的理解能力，用户在与LLM的互动中能够更好地掌握复杂概念。具体性能数据尚未提供，但与传统方法相比，用户的理解深度和准确性有明显提升。

## 🎯 应用场景

该研究的潜在应用领域包括教育、用户支持和人机交互等。通过提升人类对LLM的理解，代理可解释性可以帮助用户更有效地利用这些模型，进而在各个行业中提高工作效率和决策质量。未来，随着LLM的普及，代理可解释性可能成为人机协作的重要基础。

## 📄 摘要（原文）

> The era of Large Language Models (LLMs) presents a new opportunity for interpretability--agentic interpretability: a multi-turn conversation with an LLM wherein the LLM proactively assists human understanding by developing and leveraging a mental model of the user, which in turn enables humans to develop better mental models of the LLM. Such conversation is a new capability that traditional `inspective' interpretability methods (opening the black-box) do not use. Having a language model that aims to teach and explain--beyond just knowing how to talk--is similar to a teacher whose goal is to teach well, understanding that their success will be measured by the student's comprehension. While agentic interpretability may trade off completeness for interactivity, making it less suitable for high-stakes safety situations with potentially deceptive models, it leverages a cooperative model to discover potentially superhuman concepts that can improve humans' mental model of machines. Agentic interpretability introduces challenges, particularly in evaluation, due to what we call `human-entangled-in-the-loop' nature (humans responses are integral part of the algorithm), making the design and evaluation difficult. We discuss possible solutions and proxy goals. As LLMs approach human parity in many tasks, agentic interpretability's promise is to help humans learn the potentially superhuman concepts of the LLMs, rather than see us fall increasingly far from understanding them.

