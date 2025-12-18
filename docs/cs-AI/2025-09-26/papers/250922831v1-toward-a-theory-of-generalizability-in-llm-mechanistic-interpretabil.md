---
layout: default
title: Toward a Theory of Generalizability in LLM Mechanistic Interpretability Research
---

# Toward a Theory of Generalizability in LLM Mechanistic Interpretability Research

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22831" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22831v1</a>
  <a href="https://arxiv.org/pdf/2509.22831.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22831v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22831v1', 'Toward a Theory of Generalizability in LLM Mechanistic Interpretability Research')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sean Trott

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出LLM可解释性研究中的泛化性理论框架，并验证1-back注意力头的泛化能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM可解释性` `泛化性` `机制解释` `注意力头` `预训练`

## 📋 核心要点

1. 当前LLM可解释性研究缺乏明确的泛化性原则，难以确定从一个模型获得的结论能否推广到其他模型。
2. 论文提出五个泛化轴：功能性、发展性、位置性、关系性和配置性，用于评估机制性声明在不同LLM间的泛化能力。
3. 通过对Pythia模型中1-back注意力头的分析，验证了发展性泛化具有较强一致性，而位置性泛化则相对有限。

## 📝 摘要（中文）

大型语言模型（LLM）的研究越来越关注于识别其行为的机制性解释，但该领域缺乏明确的原则来确定从一个模型实例中获得的发现何时（以及如何）推广到另一个模型。本文旨在解决一个根本性的认识论挑战：给定关于特定模型的机制性声明，有什么理由将这一发现外推到其他LLM？以及这种泛化可能沿着哪些维度进行？我提出了五个潜在的对应轴，机制性声明可能沿着这些轴泛化，包括：功能性（是否满足相同的功能标准），发展性（是否在预训练的相似时间点发展），位置性（是否占据相似的绝对或相对位置），关系性（是否以类似的方式与其他模型组件交互）和配置性（是否对应于权重空间中的特定区域或结构）。为了实证验证这个框架，我分析了Pythia模型（14M，70M，160M，410M）的随机种子在预训练过程中的“1-back注意力头”（关注先前token的组件）。结果表明，模型间1-back注意力的发展轨迹具有显著的一致性，而位置一致性则较为有限。此外，较大模型的种子系统地显示出1-back注意力的更早出现、更陡峭的斜率和更高的峰值。我还讨论了对本文提出的论点和建议的可能异议。最后，我总结认为，在机制可解释性研究的泛化性方面取得进展将包括将LLM的构成性设计属性映射到其涌现行为和机制。

## 🔬 方法详解

**问题定义**：当前LLM可解释性研究主要集中在特定模型的机制解释，缺乏一套系统性的理论框架来评估这些解释在不同模型间的泛化能力。这导致研究结果难以推广，限制了我们对LLM通用行为的理解。现有方法缺乏对泛化维度的明确定义和评估标准，使得研究结论的可靠性和适用范围难以确定。

**核心思路**：论文的核心思路是将LLM的机制性解释的泛化问题分解为多个可评估的维度，并提出五个潜在的泛化轴：功能性、发展性、位置性、关系性和配置性。通过分析这些轴上的对应关系，可以更系统地评估一个模型中发现的机制是否能在其他模型中找到类似的对应。这种分解有助于更精确地理解泛化的边界和条件。

**技术框架**：论文首先提出了五个泛化轴的概念框架。然后，选择1-back注意力头作为案例研究对象，在不同大小的Pythia模型上进行实验。实验流程包括：1) 训练多个随机种子的Pythia模型；2) 监测预训练过程中1-back注意力头的激活情况；3) 分析不同模型和种子之间1-back注意力头的发展轨迹、位置和功能；4) 评估不同泛化轴上的一致性。

**关键创新**：论文最重要的创新在于提出了一个多维度的泛化性评估框架，将LLM机制性解释的泛化问题分解为五个可操作的轴。这为未来的可解释性研究提供了一个更系统、更严谨的评估方法。此外，论文还通过实证研究验证了该框架的有效性，并揭示了不同泛化轴上的差异。

**关键设计**：论文的关键设计包括：1) 选择1-back注意力头作为案例研究对象，因为它是一个相对简单但重要的机制；2) 使用Pythia模型，因为它是一个开源的、易于复现的模型系列；3) 采用多个随机种子，以减少偶然因素的影响；4) 采用定量指标来评估不同泛化轴上的一致性，例如，使用激活峰值、出现时间和斜率来衡量发展性泛化。

## 📊 实验亮点

实验结果表明，1-back注意力头在不同大小的Pythia模型中展现出显著的发展性一致性，即它们在预训练过程中以相似的模式出现和演化。然而，位置一致性相对较弱，表明相同功能的机制可能位于模型中的不同位置。此外，较大模型的种子通常表现出更早的激活、更陡峭的斜率和更高的峰值。

## 🎯 应用场景

该研究成果可应用于指导LLM的架构设计和训练策略，提升模型的可解释性和泛化能力。通过理解不同模型间机制的对应关系，可以更好地迁移知识和优化模型性能。此外，该框架也有助于评估不同可解释性方法的有效性和可靠性，推动可解释性研究的标准化和规范化。

## 📄 摘要（原文）

> Research on Large Language Models (LLMs) increasingly focuses on identifying mechanistic explanations for their behaviors, yet the field lacks clear principles for determining when (and how) findings from one model instance generalize to another. This paper addresses a fundamental epistemological challenge: given a mechanistic claim about a particular model, what justifies extrapolating this finding to other LLMs -- and along which dimensions might such generalizations hold? I propose five potential axes of correspondence along which mechanistic claims might generalize, including: functional (whether they satisfy the same functional criteria), developmental (whether they develop at similar points during pretraining), positional (whether they occupy similar absolute or relative positions), relational (whether they interact with other model components in similar ways), and configurational (whether they correspond to particular regions or structures in weight-space). To empirically validate this framework, I analyze "1-back attention heads" (components attending to previous tokens) across pretraining in random seeds of the Pythia models (14M, 70M, 160M, 410M). The results reveal striking consistency in the developmental trajectories of 1-back attention across models, while positional consistency is more limited. Moreover, seeds of larger models systematically show earlier onsets, steeper slopes, and higher peaks of 1-back attention. I also address possible objections to the arguments and proposals outlined here. Finally, I conclude by arguing that progress on the generalizability of mechanistic interpretability research will consist in mapping constitutive design properties of LLMs to their emergent behaviors and mechanisms.

