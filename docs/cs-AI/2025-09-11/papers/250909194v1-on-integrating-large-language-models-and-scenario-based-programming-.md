---
layout: default
title: On Integrating Large Language Models and Scenario-Based Programming for Improving Software Reliability
---

# On Integrating Large Language Models and Scenario-Based Programming for Improving Software Reliability

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09194" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09194v1</a>
  <a href="https://arxiv.org/pdf/2509.09194.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09194v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09194v1', 'On Integrating Large Language Models and Scenario-Based Programming for Improving Software Reliability')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ayelet Berzack, Guy Katz

**分类**: cs.SE, cs.AI

**发布日期**: 2025-09-11

---

## 💡 一句话要点

**结合大语言模型与场景编程提升软件可靠性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `场景编程` `软件可靠性` `软件工程` `形式化验证`

## 📋 核心要点

1. 大语言模型在软件开发中存在可靠性问题，可能产生错误代码并误导开发者。
2. 提出结合大语言模型与场景编程的方法，利用场景编程的结构化特性来指导和验证LLM的输出。
3. 通过Connect4游戏案例研究验证了该方法，成功创建了能击败现有智能体的强大智能体，并进行了形式化验证。

## 📝 摘要（中文）

大语言模型(LLMs)正迅速成为软件开发者的重要工具，协助甚至合作编写复杂程序。LLMs能显著缩短开发时间，生成组织良好且易于理解的代码，并偶尔提出开发者可能无法想到的创新想法。然而，尽管LLMs具有优势，但它们常常会引入重大错误，并以令人信服的自信呈现不正确的代码，可能误导开发者接受有缺陷的解决方案。为了以更可靠的方式将LLMs引入软件开发周期，我们提出了一种将LLMs与“传统”软件工程技术以结构化方式相结合的方法，旨在简化开发过程，减少错误，并使用户能够更有信心地验证关键程序属性。具体来说，我们专注于基于场景的编程(SBP)范例——一种事件驱动的、基于场景的软件工程方法——以允许人类开发者将其专业知识注入LLM，并检查和验证其输出。

## 🔬 方法详解

**问题定义**：论文旨在解决大语言模型在软件开发中产生的不可靠代码问题。现有方法依赖于LLM的生成能力，但缺乏有效的验证和控制机制，导致错误代码难以发现和纠正。这使得开发者难以信任LLM生成的代码，阻碍了LLM在软件开发中的广泛应用。

**核心思路**：论文的核心思路是将大语言模型与场景编程（Scenario-Based Programming, SBP）相结合。SBP是一种事件驱动的编程范式，允许开发者通过定义场景来描述系统的行为。通过将LLM生成的代码与预定义的场景进行匹配和验证，可以有效地检测和纠正错误，提高代码的可靠性。

**技术框架**：该方法的技术框架包含以下几个主要步骤：1) 使用LLM生成代码；2) 使用SBP定义系统的期望行为场景；3) 将LLM生成的代码与SBP场景进行匹配和验证；4) 根据验证结果对LLM生成的代码进行修改和优化。整个流程形成一个迭代循环，直到代码满足所有场景的要求。

**关键创新**：该方法最重要的技术创新点在于将LLM的生成能力与SBP的验证能力相结合。与传统的软件开发方法相比，该方法能够更有效地利用LLM的优势，同时避免其潜在的风险。与直接使用LLM生成代码相比，该方法能够显著提高代码的可靠性和可维护性。

**关键设计**：在Connect4游戏案例中，关键设计包括：1) 使用LLM生成游戏逻辑代码，例如判断胜负、落子等；2) 使用SBP定义游戏规则和策略，例如防止非法落子、优先占据中心位置等；3) 设计匹配算法，将LLM生成的代码与SBP场景进行匹配，检测是否存在违反规则或策略的行为；4) 设计反馈机制，根据匹配结果对LLM生成的代码进行修改和优化。

## 📊 实验亮点

该研究通过Connect4游戏案例验证了所提出方法的有效性。实验结果表明，结合LLM和SBP创建的智能体能够击败各种强大的现有智能体。在某些情况下，研究人员还能够对智能体的正确性进行形式化验证，进一步证明了该方法的可靠性。案例研究的代码将在论文最终版本中公开。

## 🎯 应用场景

该研究成果可应用于各种软件开发场景，尤其是在需要高可靠性和安全性的领域，如金融、医疗和航空航天等。通过结合大语言模型和场景编程，可以提高软件开发的效率和质量，降低开发成本和风险。未来，该方法有望成为一种主流的软件开发范式。

## 📄 摘要（原文）

> Large Language Models (LLMs) are fast becoming indispensable tools for software developers, assisting or even partnering with them in crafting complex programs. The advantages are evident -- LLMs can significantly reduce development time, generate well-organized and comprehensible code, and occasionally suggest innovative ideas that developers might not conceive on their own. However, despite their strengths, LLMs will often introduce significant errors and present incorrect code with persuasive confidence, potentially misleading developers into accepting flawed solutions.
>   In order to bring LLMs into the software development cycle in a more reliable manner, we propose a methodology for combining them with ``traditional'' software engineering techniques in a structured way, with the goal of streamlining the development process, reducing errors, and enabling users to verify crucial program properties with increased confidence. Specifically, we focus on the Scenario-Based Programming (SBP) paradigm -- an event-driven, scenario-based approach for software engineering -- to allow human developers to pour their expert knowledge into the LLM, as well as to inspect and verify its outputs.
>   To evaluate our methodology, we conducted a significant case study, and used it to design and implement the Connect4 game. By combining LLMs and SBP we were able to create a highly-capable agent, which could defeat various strong existing agents. Further, in some cases, we were able to formally verify the correctness of our agent. Finally, our experience reveals interesting insights regarding the ease-of-use of our proposed approach. The full code of our case-study will be made publicly available with the final version of this paper.

