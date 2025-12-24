---
layout: default
title: Generative Interfaces for Language Models
---

# Generative Interfaces for Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19227" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19227v2</a>
  <a href="https://arxiv.org/pdf/2508.19227.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19227v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19227v2', 'Generative Interfaces for Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaqi Chen, Yanzhe Zhang, Yutong Zhang, Yijia Shao, Diyi Yang

**分类**: cs.CL, cs.AI, cs.HC

**发布日期**: 2025-08-26 (更新: 2025-10-07)

**备注**: Preprint

---

## 💡 一句话要点

**提出生成接口以解决语言模型交互效率低下问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `生成接口` `语言模型` `人机交互` `用户体验` `多轮对话` `智能助手` `任务特定UI`

## 📋 核心要点

1. 现有的语言模型交互方式多为线性请求-响应，导致在复杂任务中效率低下。
2. 本文提出生成接口的概念，通过主动生成用户界面来增强语言模型的交互能力。
3. 实验结果显示，生成接口在用户偏好上优于传统对话接口，提升幅度高达72%。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越被视为助手、合作者和顾问，能够通过自然对话支持多种任务。然而，大多数系统仍然受到线性请求-响应格式的限制，这使得在多轮、信息密集和探索性任务中的交互效率低下。为了解决这些问题，本文提出了生成接口的概念，LLMs通过主动生成用户界面（UIs）来响应用户查询，从而实现更灵活和互动的参与。我们的框架利用结构化的接口特定表示和迭代优化，将用户查询转化为任务特定的UIs。为了系统评估，我们引入了一个多维评估框架，比较生成接口与传统聊天接口在多种任务、交互模式和查询类型下的表现，捕捉用户体验的功能性、互动性和情感方面。结果表明，生成接口在用户偏好上始终优于对话接口，提升幅度可达72%。这些发现阐明了用户何时以及为何偏好生成接口，为未来人机交互的进步铺平了道路。

## 🔬 方法详解

**问题定义**：本文旨在解决现有语言模型在多轮对话和信息密集型任务中的交互效率低下问题。传统的线性请求-响应格式限制了用户的探索性和互动性。

**核心思路**：提出生成接口的概念，使语言模型能够主动生成适应用户需求的用户界面，从而提升交互的灵活性和有效性。该设计旨在通过结构化的接口表示和迭代优化来实现任务特定的UI生成。

**技术框架**：整体架构包括用户查询的解析、任务特定UI的生成和用户交互的反馈循环。主要模块包括查询解析器、UI生成器和用户反馈模块，确保生成的UI能够适应用户的动态需求。

**关键创新**：最重要的技术创新在于生成接口的设计，使得语言模型不仅仅是被动响应，而是主动参与到交互中，显著提升了用户体验。与传统方法相比，生成接口能够提供更为丰富和灵活的交互形式。

**关键设计**：在技术细节上，采用了结构化的接口表示和多轮反馈机制，确保生成的UI能够实时调整以满足用户的需求。损失函数设计上，考虑了用户体验的多维度评估，以优化生成接口的质量。

## 📊 实验亮点

实验结果表明，生成接口在用户偏好上优于传统对话接口，提升幅度高达72%。这一显著的性能提升表明生成接口在多轮交互和信息密集任务中的有效性，展示了其在用户体验方面的优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、在线客服、教育辅导等场景，能够显著提升用户与AI系统的交互效率和满意度。未来，生成接口有望在更广泛的人机交互领域中发挥重要作用，推动智能系统的进一步发展。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly seen as assistants, copilots, and consultants, capable of supporting a wide range of tasks through natural conversation. However, most systems remain constrained by a linear request-response format that often makes interactions inefficient in multi-turn, information-dense, and exploratory tasks. To address these limitations, we propose Generative Interfaces for Language Models, a paradigm in which LLMs respond to user queries by proactively generating user interfaces (UIs) that enable more adaptive and interactive engagement. Our framework leverages structured interface-specific representations and iterative refinements to translate user queries into task-specific UIs. For systematic evaluation, we introduce a multidimensional assessment framework that compares generative interfaces with traditional chat-based ones across diverse tasks, interaction patterns, and query types, capturing functional, interactive, and emotional aspects of user experience. Results show that generative interfaces consistently outperform conversational ones, with up to a 72% improvement in human preference. These findings clarify when and why users favor generative interfaces, paving the way for future advancements in human-AI interaction.

