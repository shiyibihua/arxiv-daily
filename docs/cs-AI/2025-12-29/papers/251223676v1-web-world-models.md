---
layout: default
title: Web World Models
---

# Web World Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23676" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23676v1</a>
  <a href="https://arxiv.org/pdf/2512.23676.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23676v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23676v1', 'Web World Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jichen Feng, Yifan Zhang, Chenggong Zhang, Yifu Lu, Shilong Liu, Mengdi Wang

**分类**: cs.AI, cs.CL, cs.CV

**发布日期**: 2025-12-29

**备注**: Project Page: https://github.com/Princeton-AI2-Lab/Web-World-Models

**🔗 代码/项目**: [GITHUB](https://github.com/Princeton-AI2-Lab/Web-World-Models)

---

## 💡 一句话要点

**提出Web World Model，结合Web代码的逻辑一致性和LLM的生成能力，构建可控且开放的Agent环境。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `世界模型` `语言Agent` `大型语言模型` `Web技术栈` `可控生成`

## 📋 核心要点

1. 现有语言Agent环境构建方法要么依赖固定Web框架，缺乏开放性；要么完全依赖生成模型，难以控制和保证逻辑一致性。
2. Web World Model (WWM) 结合Web代码的逻辑性和LLM的生成能力，在结构化潜在状态上生成上下文和决策，实现可控且开放的环境。
3. 通过在多种Web环境中的实验，验证了WWM的设计原则，证明了Web技术栈作为世界模型可扩展基底的潜力。

## 📝 摘要（中文）

语言Agent越来越需要在持久的世界中行动、记忆和学习。现有方法处于两个极端：传统的Web框架提供可靠但固定的上下文，由数据库支持；而完全生成的世界模型旨在实现无限的环境，但牺牲了可控性和实际工程性。本文提出了Web World Model (WWM)，这是一种中间方案，其中世界状态和“物理”规则在普通的Web代码中实现，以确保逻辑一致性，而大型语言模型在此结构化的潜在状态之上生成上下文、叙事和高层决策。我们在一个真实的Web堆栈上构建了一套WWM，包括一个基于真实地理的无限旅行地图集、虚构的星系探险者、Web规模的百科全书和叙事世界，以及模拟和游戏类环境。通过这些系统，我们确定了WWM的实用设计原则：将代码定义的规则与模型驱动的想象力分离，将潜在状态表示为类型化的Web接口，并利用确定性生成来实现无限但结构化的探索。结果表明，Web堆栈本身可以作为世界模型的可扩展基底，从而实现可控但开放的环境。

## 🔬 方法详解

**问题定义**：现有语言Agent环境构建方法存在局限性。传统Web框架依赖数据库，环境固定，缺乏开放性和探索性。完全生成的世界模型虽然开放，但难以控制，容易出现逻辑不一致和幻觉问题，难以实际工程化应用。

**核心思路**：Web World Model (WWM) 的核心思路是将世界状态和基本规则用Web代码实现，保证逻辑一致性和可控性，同时利用大型语言模型 (LLM) 在此基础上生成上下文、叙事和高层决策，实现开放性和创造性。这种混合方法旨在弥合传统Web框架和完全生成模型之间的差距。

**技术框架**：WWM的整体架构包含以下几个关键模块：1) **Web代码层**：定义世界的基本状态和规则，例如地理位置、物理定律等，使用标准的Web技术栈实现。2) **LLM层**：负责生成上下文、叙事和高层决策，例如Agent的行动计划、对话内容等。3) **接口层**：定义Web代码层和LLM层之间的接口，例如Agent可以查询哪些信息、可以执行哪些操作。通过这些接口，LLM可以与Web世界进行交互。

**关键创新**：WWM的关键创新在于将Web技术栈作为世界模型的基础，并结合LLM的生成能力。这种混合方法既保证了逻辑一致性和可控性，又实现了开放性和创造性。与现有方法相比，WWM更易于工程化实现，并且可以构建更复杂、更真实的世界模型。

**关键设计**：WWM的关键设计原则包括：1) **代码定义的规则与模型驱动的想象力分离**：Web代码负责定义世界的物理规则和基本状态，LLM负责生成上下文和叙事。2) **潜在状态表示为类型化的Web接口**：通过定义清晰的Web接口，LLM可以方便地访问和操作世界状态。3) **利用确定性生成实现无限但结构化的探索**：通过控制LLM的生成过程，可以实现对世界的结构化探索，避免出现逻辑不一致和幻觉问题。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23676v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23676v1/images/Teaser2.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23676v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文在多个Web环境中进行了实验，包括无限旅行地图集、星系探险、Web规模的百科全书和叙事世界，以及模拟和游戏类环境。实验结果表明，WWM可以有效地构建可控且开放的世界模型，并且易于工程化实现。论文还总结了WWM的实用设计原则，为未来的研究提供了指导。

## 🎯 应用场景

Web World Model 有广泛的应用前景，包括：1) 游戏开发：可以用于构建更真实、更开放的游戏世界。2) 教育：可以用于创建交互式学习环境，让学生在虚拟世界中学习知识。3) 科研：可以用于模拟复杂的系统，例如经济系统、社会系统等。4) 智能助手：可以用于构建更智能的助手，让助手能够更好地理解用户的需求并提供帮助。

## 📄 摘要（原文）

> Language agents increasingly require persistent worlds in which they can act, remember, and learn. Existing approaches sit at two extremes: conventional web frameworks provide reliable but fixed contexts backed by databases, while fully generative world models aim for unlimited environments at the expense of controllability and practical engineering. In this work, we introduce the Web World Model (WWM), a middle ground where world state and ``physics'' are implemented in ordinary web code to ensure logical consistency, while large language models generate context, narratives, and high-level decisions on top of this structured latent state. We build a suite of WWMs on a realistic web stack, including an infinite travel atlas grounded in real geography, fictional galaxy explorers, web-scale encyclopedic and narrative worlds, and simulation- and game-like environments. Across these systems, we identify practical design principles for WWMs: separating code-defined rules from model-driven imagination, representing latent state as typed web interfaces, and utilizing deterministic generation to achieve unlimited but structured exploration. Our results suggest that web stacks themselves can serve as a scalable substrate for world models, enabling controllable yet open-ended environments. Project Page: https://github.com/Princeton-AI2-Lab/Web-World-Models.

