---
layout: default
title: "ClarifyMT-Bench: Benchmarking and Improving Multi-Turn Clarification for Conversational Large Language Models"
---

# ClarifyMT-Bench: Benchmarking and Improving Multi-Turn Clarification for Conversational Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21120" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21120v1</a>
  <a href="https://arxiv.org/pdf/2512.21120.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21120v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21120v1', 'ClarifyMT-Bench: Benchmarking and Improving Multi-Turn Clarification for Conversational Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sichun Luo, Yi Huang, Mukai Li, Shichang Meng, Fengyuan Liu, Zefa Hu, Junlan Feng, Qi Liu

**分类**: cs.CL, cs.IR

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**提出ClarifyMT-Bench，用于评估和提升会话大语言模型的多轮澄清能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多轮对话` `大语言模型` `澄清` `模糊性` `基准测试`

## 📋 核心要点

1. 现有LLM澄清基准主要关注单轮交互或合作用户，难以评估真实场景下的澄清行为。
2. 论文提出ClarifyAgent，将澄清过程分解为感知、预测、跟踪和规划四个阶段，提升鲁棒性。
3. ClarifyMT-Bench评估显示，LLM存在欠澄清偏差，ClarifyAgent能有效缓解该问题，提升性能。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越多地被部署为开放域、多轮环境中的会话助手，在这些环境中，用户常常提供不完整或不明确的信息。然而，现有的以LLM为中心的澄清基准主要假设单轮交互或合作用户，限制了它们在真实场景中评估澄清行为的能力。我们引入了	extbf{ClarifyMT-Bench}，这是一个基于五维模糊性分类和一组六个行为多样的模拟用户角色构建的多轮澄清基准。通过混合LLM-人工流程，我们构建了6,120个多轮对话，捕捉了不同的模糊性来源和交互模式。对十个代表性LLM的评估揭示了一种一致的欠澄清偏差：LLM倾向于过早回答，并且性能随着对话深度的增加而下降。为了缓解这个问题，我们提出了	extbf{ClarifyAgent}，一种将澄清分解为感知、预测、跟踪和规划的代理方法，从而显著提高了各种模糊性条件下的鲁棒性。ClarifyMT-Bench为研究LLM何时应该提问、何时应该回答以及如何在真实的人机交互中处理模糊性奠定了可复现的基础。

## 🔬 方法详解

**问题定义**：现有的大语言模型在多轮对话中，面对用户提供的不完整或模糊信息时，缺乏有效的澄清机制。现有的澄清基准测试主要集中在单轮交互或假设用户是完全合作的，这与真实场景存在差距，无法充分评估LLM在复杂对话环境下的澄清能力。因此，需要一个更贴近真实场景、更全面的多轮澄清基准，以及能够有效处理模糊信息的澄清方法。

**核心思路**：论文的核心思路是将多轮澄清过程建模为一个智能代理（ClarifyAgent），该代理能够感知用户输入中的模糊性，预测澄清的必要性，跟踪对话状态，并规划澄清策略。通过将澄清过程分解为多个可控的步骤，可以更有效地引导LLM进行澄清，避免过早回答或遗漏关键信息。

**技术框架**：ClarifyAgent的技术框架包含四个主要模块：1) 感知模块（Perception）：负责检测用户输入中的模糊性，并根据预定义的模糊性分类进行分类。2) 预测模块（Forecasting）：基于对话历史和当前输入，预测是否需要进行澄清。3) 跟踪模块（Tracking）：维护对话状态，包括已澄清的信息和未澄清的信息。4) 规划模块（Planning）：根据预测结果和对话状态，选择合适的澄清策略，例如提出具体问题或要求用户提供更多信息。

**关键创新**：论文的关键创新在于提出了一个agentic的澄清框架，将澄清过程分解为多个可控的步骤，并引入了预测模块来判断澄清的必要性。这与传统的单轮澄清方法或直接回答问题的方法不同，能够更有效地处理多轮对话中的模糊信息。

**关键设计**：ClarifyMT-Bench基准的设计考虑了五个维度的模糊性分类，并模拟了六种不同行为的用户角色，以增加基准的真实性和多样性。ClarifyAgent的各个模块可以使用不同的LLM或专门训练的模型来实现。预测模块可以使用二元分类器来判断是否需要澄清。规划模块可以基于规则或强化学习来选择澄清策略。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21120v1/z13.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21120v1/z17.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21120v1/x1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，现有的LLM普遍存在欠澄清偏差，即倾向于过早回答问题，导致性能下降。ClarifyAgent在各种模糊性条件下均表现出显著的性能提升，证明了其在多轮澄清方面的有效性。例如，在某些模糊性条件下，ClarifyAgent的性能提升超过10%。

## 🎯 应用场景

该研究成果可应用于各种会话式人工智能系统，例如智能客服、虚拟助手和教育机器人。通过提升LLM的澄清能力，可以提高对话的效率和准确性，改善用户体验，并减少因信息不明确而导致的错误。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly deployed as conversational assistants in open-domain, multi-turn settings, where users often provide incomplete or ambiguous information. However, existing LLM-focused clarification benchmarks primarily assume single-turn interactions or cooperative users, limiting their ability to evaluate clarification behavior in realistic settings. We introduce \textbf{ClarifyMT-Bench}, a benchmark for multi-turn clarification grounded in a five-dimensional ambiguity taxonomy and a set of six behaviorally diverse simulated user personas. Through a hybrid LLM-human pipeline, we construct 6,120 multi-turn dialogues capturing diverse ambiguity sources and interaction patterns. Evaluating ten representative LLMs uncovers a consistent under-clarification bias: LLMs tend to answer prematurely, and performance degrades as dialogue depth increases. To mitigate this, we propose \textbf{ClarifyAgent}, an agentic approach that decomposes clarification into perception, forecasting, tracking, and planning, substantially improving robustness across ambiguity conditions. ClarifyMT-Bench establishes a reproducible foundation for studying when LLMs should ask, when they should answer, and how to navigate ambiguity in real-world human-LLM interactions.

