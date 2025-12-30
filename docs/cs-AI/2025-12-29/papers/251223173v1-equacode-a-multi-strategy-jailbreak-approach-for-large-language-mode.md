---
layout: default
title: "EquaCode: A Multi-Strategy Jailbreak Approach for Large Language Models via Equation Solving and Code Completion"
---

# EquaCode: A Multi-Strategy Jailbreak Approach for Large Language Models via Equation Solving and Code Completion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23173" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23173v1</a>
  <a href="https://arxiv.org/pdf/2512.23173.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23173v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23173v1', 'EquaCode: A Multi-Strategy Jailbreak Approach for Large Language Models via Equation Solving and Code Completion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhen Liang, Hai Huang, Zhengkui Chen

**分类**: cs.CR, cs.AI

**发布日期**: 2025-12-29

**备注**: This is a preprint. A revised version will appear in the Proceedings of AAAI 2026

---

## 💡 一句话要点

**提出 EquaCode，利用数学方程求解与代码补全实现大语言模型越狱攻击**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `越狱攻击` `方程求解` `代码补全` `多策略攻击` `安全评估` `鲁棒性`

## 📋 核心要点

1. 现有大语言模型越狱攻击主要依赖自然语言，且策略单一，难以全面评估模型的鲁棒性。
2. EquaCode 将恶意意图转化为数学问题，并要求模型通过代码求解，利用跨领域复杂性转移模型注意力。
3. 实验表明，EquaCode 在 GPT 系列和多个 SOTA LLM 上取得了超过 90% 的越狱成功率，且优于单一策略。

## 📝 摘要（中文）

大型语言模型（LLMs），如ChatGPT，在各个领域取得了显著成功。然而，它们的可靠性仍然是一个重要问题，因为它们仍然容易受到旨在引出不适当或有害响应的越狱攻击。现有的越狱攻击主要在自然语言层面操作，并依赖于单一的攻击策略，限制了其全面评估LLM鲁棒性的有效性。本文提出了一种新颖的多策略越狱方法Equacode，通过方程求解和代码补全来实现对大型语言模型的攻击。该方法将恶意意图转化为数学问题，然后要求LLM使用代码来解决它，利用跨领域任务的复杂性来转移模型对任务完成的关注，而不是安全约束。实验结果表明，Equacode在GPT系列上的平均成功率为91.19%，在3个最先进的LLM上的平均成功率为98.65%，而且只需要一次查询。此外，消融实验表明，EquaCode的性能优于单独的数学方程模块或代码模块。这表明存在强大的协同效应，从而证明了多策略方法产生的结果大于其各部分之和。

## 🔬 方法详解

**问题定义**：现有的大语言模型容易受到越狱攻击，攻击者可以通过精心设计的提示词诱导模型生成有害或不当内容。现有的攻击方法主要集中在自然语言层面，依赖于单一的攻击策略，这使得模型更容易识别和防御这些攻击。因此，如何设计一种更有效、更隐蔽的攻击方法，以全面评估和提高大语言模型的安全性，是一个亟待解决的问题。

**核心思路**：EquaCode 的核心思路是将恶意意图转化为一个复杂的数学问题，并要求大语言模型通过编写代码来解决这个问题。这种方法利用了数学和编程的跨领域复杂性，使得模型更难识别出潜在的恶意意图，从而更容易绕过模型的安全机制。通过将问题转化为代码补全任务，模型会将更多的注意力放在完成任务上，而忽略潜在的安全风险。

**技术框架**：EquaCode 的整体框架包含两个主要模块：数学方程生成模块和代码补全模块。首先，数学方程生成模块将恶意意图编码为一个复杂的数学方程。然后，将该方程作为提示词输入到大语言模型中，要求模型生成解决该方程的代码。最后，执行生成的代码，如果代码成功执行并输出了预期的结果，则认为越狱攻击成功。

**关键创新**：EquaCode 的关键创新在于其多策略攻击方法，它结合了数学方程求解和代码补全两个不同的领域，从而提高了攻击的隐蔽性和有效性。与传统的自然语言攻击方法相比，EquaCode 能够更有效地绕过模型的安全机制，因为它利用了模型在跨领域任务中的弱点。此外，EquaCode 的多策略方法也使得模型更难识别出攻击的意图，从而提高了攻击的成功率。

**关键设计**：在数学方程生成模块中，需要精心设计方程的复杂度和难度，以确保模型能够理解并尝试解决该方程，同时又不会过于简单以至于模型能够轻易识别出潜在的恶意意图。在代码补全模块中，需要选择合适的编程语言和代码框架，以便模型能够生成可执行的代码，并能够输出预期的结果。此外，还需要设置合适的执行环境和安全策略，以防止生成的代码对系统造成损害。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23173v1/equacode.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23173v1/code.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23173v1/intent.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

EquaCode 在 GPT 系列模型上取得了 91.19% 的平均越狱成功率，在三个最先进的 LLM 上达到了 98.65% 的成功率，且仅需单次查询。消融实验表明，EquaCode 的性能显著优于单独使用数学方程或代码补全模块，验证了多策略协同攻击的有效性。

## 🎯 应用场景

EquaCode 可用于评估和提高大语言模型的安全性，帮助开发者发现模型中存在的漏洞，并采取相应的措施进行修复。此外，该方法还可以用于开发更强大的安全防御机制，以防止恶意用户利用大语言模型进行有害活动。该研究对于构建更安全、更可靠的人工智能系统具有重要意义。

## 📄 摘要（原文）

> Large language models (LLMs), such as ChatGPT, have achieved remarkable success across a wide range of fields. However, their trustworthiness remains a significant concern, as they are still susceptible to jailbreak attacks aimed at eliciting inappropriate or harmful responses. However, existing jailbreak attacks mainly operate at the natural language level and rely on a single attack strategy, limiting their effectiveness in comprehensively assessing LLM robustness. In this paper, we propose Equacode, a novel multi-strategy jailbreak approach for large language models via equation-solving and code completion. This approach transforms malicious intent into a mathematical problem and then requires the LLM to solve it using code, leveraging the complexity of cross-domain tasks to divert the model's focus toward task completion rather than safety constraints. Experimental results show that Equacode achieves an average success rate of 91.19% on the GPT series and 98.65% across 3 state-of-the-art LLMs, all with only a single query. Further, ablation experiments demonstrate that EquaCode outperforms either the mathematical equation module or the code module alone. This suggests a strong synergistic effect, thereby demonstrating that multi-strategy approach yields results greater than the sum of its parts.

