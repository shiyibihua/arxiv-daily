---
layout: default
title: Which Cultural Lens Do Models Adopt? On Cultural Positioning Bias and Agentic Mitigation in LLMs
---

# Which Cultural Lens Do Models Adopt? On Cultural Positioning Bias and Agentic Mitigation in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21080" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21080v1</a>
  <a href="https://arxiv.org/pdf/2509.21080.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21080v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21080v1', 'Which Cultural Lens Do Models Adopt? On Cultural Positioning Bias and Agentic Mitigation in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yixin Wan, Xingrun Chen, Kai-Wei Chang

**分类**: cs.CL, cs.AI, cs.CY

**发布日期**: 2025-09-25

---

## 💡 一句话要点

**揭示LLM文化定位偏差并提出基于Agent的偏见缓解方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `文化定位偏差` `公平性` `代理` `偏见缓解` `生成式模型` `多智能体系统`

## 📋 核心要点

1. 现有大型语言模型在生成内容时，存在以主流文化视角看待世界的文化定位偏差问题。
2. 论文提出通过构建公平代理，进行自我反思和重写，或通过多代理协作来缓解文化定位偏差。
3. 实验表明，基于代理的方法能够有效缓解LLM在生成内容时表现出的文化偏见。

## 📝 摘要（中文）

大型语言模型（LLM）在生成式应用中展现了巨大潜力。然而，本文发现LLM存在文化相关的微妙公平性问题，其生成内容倾向于主流美国文化的视角，对非主流文化表现出显著的外部性。本文识别并系统研究了这种新型的文化定位偏差，即LLM的默认生成立场与主流观点一致，并将其他文化视为局外人。为此，本文提出了CultureLens基准，包含4000个生成提示和3个评估指标，通过文化情境下的访谈脚本生成任务来量化这种偏差，其中LLM扮演记者采访10种不同文化的当地人。对5个先进LLM的评估揭示了一个明显的模式：模型在美国语境下平均采用超过88%的内部人士语气，但在较不占主导地位的文化中，不成比例地采用外部人士立场。为了解决这些偏差，本文提出了两种推理时缓解方法：基于提示的公平干预支柱（FIP）基线方法，以及一个结构化的通过公平代理缓解（MFA）框架，该框架包含两个流程：（1）MFA-SA（单代理）引入了一个基于公平性指南的自我反思和重写循环。（2）MFA-MA（多代理）将该过程构建成一个专业代理的层级结构：规划代理（初始脚本生成）、评论代理（根据公平性支柱评估初始脚本）和改进代理（整合反馈以生成润色后的无偏脚本）。实验结果表明，基于代理的方法是缓解生成式LLM中偏见的一个有希望的方向。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在生成内容时存在的文化定位偏差问题。具体而言，LLM倾向于以主流文化（如美国文化）的视角进行生成，而将其他文化视为“局外人”，从而导致不公平的现象。现有方法缺乏对这种偏差的有效识别和缓解机制。

**核心思路**：论文的核心思路是利用代理（Agent）来模拟人类的自我反思和协作过程，从而引导LLM生成更加公平和客观的内容。通过让代理根据预定义的公平性原则对生成内容进行评估和改进，可以有效地减少文化定位偏差。

**技术框架**：论文提出了两种基于代理的缓解方法：MFA-SA（单代理）和MFA-MA（多代理）。MFA-SA采用单代理的自我反思和重写循环，代理根据公平性指南评估初始生成脚本，并进行迭代改进。MFA-MA则构建了一个多代理层级结构，包括规划代理（负责初始脚本生成）、评论代理（负责根据公平性支柱评估脚本）和改进代理（负责整合反馈并生成最终脚本）。

**关键创新**：论文的关键创新在于将代理的概念引入到LLM的偏见缓解中，并提出了两种不同的代理架构（单代理和多代理）。与传统的基于提示的方法相比，基于代理的方法能够更有效地捕捉和纠正LLM中的文化定位偏差。多代理架构通过明确分工，使得偏见检测和缓解过程更加结构化和可控。

**关键设计**：在MFA-SA中，关键在于公平性指南的设计，它指导代理进行自我评估和重写。在MFA-MA中，关键在于各个代理之间的协作机制，以及评论代理所使用的公平性支柱。论文没有详细说明具体的参数设置、损失函数或网络结构，这些可能依赖于底层LLM的实现。

## 📊 实验亮点

实验结果表明，基于代理的方法能够显著降低LLM中的文化定位偏差。例如，在CultureLens基准测试中，MFA-MA方法在多个文化背景下都取得了优于基线方法的性能，尤其是在非主流文化背景下，其改进效果更为明显。与FIP基线方法相比，MFA方法能够更有效地提高生成内容的公平性和客观性。

## 🎯 应用场景

该研究成果可应用于各种需要生成文化敏感内容的场景，例如跨文化交流、教育、新闻报道等。通过缓解LLM中的文化定位偏差，可以提高生成内容的公平性和客观性，避免对特定文化群体的歧视或偏见。未来，该方法可以推广到其他类型的偏见缓解任务中，例如性别偏见、种族偏见等。

## 📄 摘要（原文）

> Large language models (LLMs) have unlocked a wide range of downstream generative applications. However, we found that they also risk perpetuating subtle fairness issues tied to culture, positioning their generations from the perspectives of the mainstream US culture while demonstrating salient externality towards non-mainstream ones. In this work, we identify and systematically investigate this novel culture positioning bias, in which an LLM's default generative stance aligns with a mainstream view and treats other cultures as outsiders. We propose the CultureLens benchmark with 4000 generation prompts and 3 evaluation metrics for quantifying this bias through the lens of a culturally situated interview script generation task, in which an LLM is positioned as an onsite reporter interviewing local people across 10 diverse cultures. Empirical evaluation on 5 state-of-the-art LLMs reveals a stark pattern: while models adopt insider tones in over 88 percent of US-contexted scripts on average, they disproportionately adopt mainly outsider stances for less dominant cultures. To resolve these biases, we propose 2 inference-time mitigation methods: a baseline prompt-based Fairness Intervention Pillars (FIP) method, and a structured Mitigation via Fairness Agents (MFA) framework consisting of 2 pipelines: (1) MFA-SA (Single-Agent) introduces a self-reflection and rewriting loop based on fairness guidelines. (2) MFA-MA (Multi-Agent) structures the process into a hierarchy of specialized agents: a Planner Agent(initial script generation), a Critique Agent (evaluates initial script against fairness pillars), and a Refinement Agent (incorporates feedback to produce a polished, unbiased script). Empirical results showcase the effectiveness of agent-based methods as a promising direction for mitigating biases in generative LLMs.

