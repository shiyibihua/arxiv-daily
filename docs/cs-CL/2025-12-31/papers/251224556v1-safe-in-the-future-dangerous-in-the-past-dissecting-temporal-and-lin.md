---
layout: default
title: "Safe in the Future, Dangerous in the Past: Dissecting Temporal and Linguistic Vulnerabilities in LLMs"
---

# Safe in the Future, Dangerous in the Past: Dissecting Temporal and Linguistic Vulnerabilities in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24556" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24556v1</a>
  <a href="https://arxiv.org/pdf/2512.24556.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24556v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24556v1', 'Safe in the Future, Dangerous in the Past: Dissecting Temporal and Linguistic Vulnerabilities in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muhammad Abdullahi Said, Muhammad Sammani Sani

**分类**: cs.CL

**发布日期**: 2025-12-31

---

## 💡 一句话要点

**揭示大语言模型在语言和时间维度上的安全漏洞，提出不变对齐方法。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `安全对齐` `对抗性攻击` `时间推理` `多语言` `不变对齐` `豪萨语` `安全漏洞`

## 📋 核心要点

1. 现有大语言模型在安全对齐方面存在漏洞，尤其是在非英语语境和时间推理上。
2. 论文提出通过不变对齐方法，增强模型在不同语言和时间框架下的安全稳定性。
3. 实验表明，模型在过去时框架下更容易被攻击，未来时框架下则过于保守，安全性能波动大。

## 📝 摘要（中文）

随着大型语言模型（LLMs）集成到关键的全球基础设施中，英语安全对齐能够零样本迁移到其他语言的假设仍然是一个危险的盲点。本研究使用HausaSafety（一个基于西非威胁场景（例如，Yahoo-Yahoo欺诈、Dane枪支制造）的新型对抗数据集），对三个最先进的模型（GPT-5.1、Gemini 3 Pro和Claude 4.5 Opus）进行了系统审计。通过跨1,440次评估的2 x 4因子设计，我们测试了语言（英语vs.豪萨语）和时间框架之间的非线性交互。我们的结果挑战了当前的多语言安全差距叙事。我们没有发现低资源环境下的简单退化，而是发现了一种复杂的干扰机制，其中安全性由变量的交集决定。虽然模型表现出一种反向语言现象，即Claude 4.5 Opus在豪萨语中比在英语中更安全（分别为45.0%和36.7%），原因是其不确定性驱动的拒绝，但它们在时间推理方面遭受了灾难性的失败。我们报告了一种深刻的时间不对称性，其中过去时框架绕过了防御（15.6%安全），而将来时场景触发了过度保守的拒绝（57.2%安全）。最安全和最脆弱配置之间存在9.2倍的差异，证明安全性不是一个固定属性，而是一个上下文相关的状态。我们得出结论，当前的模型依赖于肤浅的启发式方法，而不是强大的语义理解，从而创建了安全口袋，使全球南方用户面临本地化的危害。我们提出不变对齐作为一种必要的范式转变，以确保跨语言和时间转变的安全稳定性。

## 🔬 方法详解

**问题定义**：现有的大语言模型在安全对齐方面存在严重的跨语言和时间泛化问题。具体来说，模型在英语环境下训练的安全策略，无法有效地迁移到其他语言（如豪萨语），并且模型对过去和未来的事件的安全性判断存在显著差异。现有方法依赖于肤浅的启发式规则，缺乏对语义的深入理解，导致模型在特定语境下出现安全漏洞。

**核心思路**：论文的核心思路是揭示大语言模型在语言和时间维度上的安全脆弱性，并提出一种“不变对齐”的范式，旨在使模型的安全策略在不同的语言和时间框架下保持一致性。通过对抗性测试，发现模型在不同语言和时间框架下的安全性能差异，从而指导模型的改进。

**技术框架**：论文采用2 x 4因子设计，评估了三个最先进的模型（GPT-5.1、Gemini 3 Pro和Claude 4.5 Opus）在英语和豪萨语两种语言，以及不同时间框架下的安全性能。使用HausaSafety数据集，该数据集包含基于西非威胁场景的对抗性示例。通过分析模型在不同配置下的安全响应，揭示了模型在语言和时间维度上的安全漏洞。

**关键创新**：论文的关键创新在于发现了大语言模型在时间推理上的“时间不对称性”，即模型对过去时和将来时事件的安全判断存在显著差异。此外，论文还提出了“不变对齐”的概念，强调模型安全策略在不同语境下的稳定性，这与传统的安全对齐方法有所不同。

**关键设计**：论文的关键设计包括：1）HausaSafety对抗数据集，用于评估模型在西非特定威胁场景下的安全性能；2）2 x 4因子实验设计，用于系统地评估语言和时间框架对模型安全性的影响；3）对模型响应的安全性进行量化评估，并分析模型在不同配置下的安全性能差异。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24556v1/plots/01_ASR_Comparison.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24556v1/plots/04_Temporal_Vulnerability.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24556v1/plots/06_Category_Analysis.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Claude 4.5 Opus在豪萨语中的安全性高于英语（45.0% vs. 36.7%），但所有模型都表现出显著的时间不对称性，过去时框架下的安全性仅为15.6%，而将来时框架下则高达57.2%。最安全和最脆弱配置之间存在9.2倍的安全性差异。

## 🎯 应用场景

该研究成果可应用于提升大语言模型在全球范围内的安全性，尤其是在低资源语言和文化背景下的应用。通过不变对齐，可以减少模型在不同语境下的安全漏洞，降低模型被恶意利用的风险，从而促进人工智能技术的安全可靠发展。

## 📄 摘要（原文）

> As Large Language Models (LLMs) integrate into critical global infrastructure, the assumption that safety alignment transfers zero-shot from English to other languages remains a dangerous blind spot. This study presents a systematic audit of three state of the art models (GPT-5.1, Gemini 3 Pro, and Claude 4.5 Opus) using HausaSafety, a novel adversarial dataset grounded in West African threat scenarios (e.g., Yahoo-Yahoo fraud, Dane gun manufacturing). Employing a 2 x 4 factorial design across 1,440 evaluations, we tested the non-linear interaction between language (English vs. Hausa) and temporal framing. Our results challenge the prevailing multilingual safety gap narrative. Instead of a simple degradation in low-resource settings, we identified a mechanism of Complex Interference where safety is determined by the intersection of variables. While models exhibited a Reverse Linguistic with Claude 4.5 Opus proving significantly safer in Hausa (45.0%) than in English (36.7%) due to uncertainty-driven refusal they suffered catastrophic failures in temporal reasoning. We report a profound Temporal Asymmetry, where past-tense framing bypassed defenses (15.6% safe) while future-tense scenarios triggered hyper-conservative refusals (57.2% safe). The magnitude of this volatility is illustrated by a 9.2x disparity between the safest and most vulnerable configurations, proving that safety is not a fixed property but a context-dependent state. We conclude that current models rely on superficial heuristics rather than robust semantic understanding, creating Safety Pockets that leave Global South users exposed to localized harms. We propose Invariant Alignment as a necessary paradigm shift to ensure safety stability across linguistic and temporal shifts.

