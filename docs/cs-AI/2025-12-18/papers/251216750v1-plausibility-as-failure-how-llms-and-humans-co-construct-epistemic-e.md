---
layout: default
title: Plausibility as Failure: How LLMs and Humans Co-Construct Epistemic Error
---

# Plausibility as Failure: How LLMs and Humans Co-Construct Epistemic Error

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16750" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16750v1</a>
  <a href="https://arxiv.org/pdf/2512.16750.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16750v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16750v1', 'Plausibility as Failure: How LLMs and Humans Co-Construct Epistemic Error')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Claudia Vale Oliveira, Nelson Zagalo, Filipe Silva, Anabela Brandao, Syeda Faryal Hussain Khurrum, Joaquim Santos

**分类**: cs.HC, cs.AI

**发布日期**: 2025-12-18

**备注**: 19 pages, 2 tables, 77 references, 6 appendices

---

## 💡 一句话要点

**揭示LLM与人类交互中认知错误的共建机制，强调评估的解释性视角**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `人机交互` `认知错误` `可信度` `解释性评估`

## 📋 核心要点

1. 现有LLM错误分析侧重于预测指标，忽略了其对人类判断的解释性影响，导致对人机交互中认知错误的理解不足。
2. 该研究将LLM错误视为一种关系破裂，由模型生成的可信度和人类的解释性判断共同塑造，强调评估的解释性视角。
3. 通过多轮评估发现，LLM错误会从预测形式转变为解释形式，且人类评估易受表面线索影响，导致认知漂移。

## 📝 摘要（中文）

大型语言模型（LLM）日益成为日常推理中的认知伙伴，但对其错误的分析主要集中在预测指标上，而非其对人类判断的解释性影响。本研究考察了在人机交互中，不同形式的认知失败如何产生、被掩盖和被容忍。这里的失败被理解为一种关系破裂，由模型生成的可信度和人类的解释性判断共同塑造。我们进行了三轮多LLM评估，使用跨学科任务和逐步区分的评估框架，观察评估者如何解释模型在语言、认知和可信度维度上的响应。研究结果表明，LLM的错误从预测形式转变为解释形式，其中语言流畅性、结构连贯性和表面上可信的引用掩盖了更深层次的意义扭曲。评估者经常混淆正确性、相关性、偏差、依据性和一致性等标准，表明人类判断将分析区分简化为受形式和流畅性影响的直觉启发式。在整个过程中，我们观察到系统的验证负担和认知漂移。随着任务变得更加密集，评估者越来越依赖表面线索，允许错误但形式良好的答案被认为是可信的。这些结果表明，错误不仅仅是模型行为的属性，而是生成可信度和人类解释性捷径共同构建的结果。因此，理解AI的认知失败需要将评估重新定义为一个关系解释过程，其中系统失败和人类校准错误之间的界限变得模糊。该研究为LLM评估、数字素养和可信的人机通信设计提供了启示。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLM）的错误评估主要集中在预测准确性等指标上，忽略了LLM的输出如何影响人类的理解和判断。这种片面的评估方式无法充分揭示人机交互中认知错误的复杂性，尤其是在LLM生成看似合理但实际上错误的答案时，人类可能会受到误导。因此，需要更深入地理解LLM的错误如何被人类感知和解释，以及这种交互如何共同构建认知错误。

**核心思路**：该研究的核心思路是将LLM的错误视为一种“关系破裂”，即LLM的输出与人类的理解之间出现偏差。这种偏差并非仅仅由LLM的预测错误引起，而是由LLM生成内容的可信度（plausibility）和人类的解释性判断共同塑造。通过考察人类如何解释和容忍LLM的错误，可以更好地理解人机交互中认知错误的产生机制。

**技术框架**：该研究采用了一个三轮的多LLM评估框架。第一轮使用跨学科任务，旨在识别不同类型的LLM错误。第二轮和第三轮逐步细化评估框架，更加关注评估者如何解释LLM的响应，并考察语言、认知和可信度等维度。评估者需要对LLM的输出进行多方面的评估，包括正确性、相关性、偏差、依据性和一致性等。研究者通过分析评估者的反馈，揭示人类判断中的认知偏差和启发式方法。

**关键创新**：该研究的关键创新在于将LLM的错误评估从单纯的预测准确性转向了对人机交互的解释性分析。它强调了LLM生成内容的可信度对人类判断的影响，并揭示了人类在评估LLM输出时存在的认知偏差。这种新的评估视角有助于更全面地理解人机交互中认知错误的产生机制。

**关键设计**：在评估过程中，研究者设计了跨学科的任务，以考察LLM在不同领域的表现。同时，他们逐步细化评估框架，更加关注评估者对LLM输出的解释。此外，研究者还采用了多种LLM，以考察不同模型的错误模式。通过这些设计，研究者能够更全面地了解LLM的错误以及人类对这些错误的反应。

## 📊 实验亮点

研究发现，LLM的错误会从预测形式转变为解释形式，即语言流畅、结构连贯但意义扭曲。评估者易受表面线索影响，导致认知漂移，使得错误答案被误认为可信。这表明错误并非仅是模型属性，而是人机交互的共建结果。

## 🎯 应用场景

该研究成果可应用于LLM评估体系的改进，提升数字素养教育，并指导更值得信赖的人机交互系统设计。通过理解LLM认知错误的共建机制，可以帮助用户更理性地使用LLM，避免盲目信任，从而减少误导信息的传播。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly used as epistemic partners in everyday reasoning, yet their errors remain predominantly analyzed through predictive metrics rather than through their interpretive effects on human judgment. This study examines how different forms of epistemic failure emerge, are masked, and are tolerated in human AI interaction, where failure is understood as a relational breakdown shaped by model-generated plausibility and human interpretive judgment. We conducted a three round, multi LLM evaluation using interdisciplinary tasks and progressively differentiated assessment frameworks to observe how evaluators interpret model responses across linguistic, epistemic, and credibility dimensions. Our findings show that LLM errors shift from predictive to hermeneutic forms, where linguistic fluency, structural coherence, and superficially plausible citations conceal deeper distortions of meaning. Evaluators frequently conflated criteria such as correctness, relevance, bias, groundedness, and consistency, indicating that human judgment collapses analytical distinctions into intuitive heuristics shaped by form and fluency. Across rounds, we observed a systematic verification burden and cognitive drift. As tasks became denser, evaluators increasingly relied on surface cues, allowing erroneous yet well formed answers to pass as credible. These results suggest that error is not solely a property of model behavior but a co-constructed outcome of generative plausibility and human interpretive shortcuts. Understanding AI epistemic failure therefore requires reframing evaluation as a relational interpretive process, where the boundary between system failure and human miscalibration becomes porous. The study provides implications for LLM assessment, digital literacy, and the design of trustworthy human AI communication.

