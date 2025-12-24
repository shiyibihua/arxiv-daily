---
layout: default
title: Investigating Intersectional Bias in Large Language Models using Confidence Disparities in Coreference Resolution
---

# Investigating Intersectional Bias in Large Language Models using Confidence Disparities in Coreference Resolution

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07111" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07111v1</a>
  <a href="https://arxiv.org/pdf/2508.07111.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07111v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07111v1', 'Investigating Intersectional Bias in Large Language Models using Confidence Disparities in Coreference Resolution')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Falaah Arif Khan, Nivedha Sivakumar, Yinong Oliver Wang, Katherine Metcalf, Cezanne Camacho, Barry-John Theobald, Luca Zappella, Nicholas Apostoloff

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-09

---

## 💡 一句话要点

**提出WinoIdentity基准以解决大型语言模型中的交叉偏见问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `交叉偏见` `大型语言模型` `公平性评估` `WinoIdentity` `核心指代信心差异` `社会属性` `AI伦理`

## 📋 核心要点

1. 现有大型语言模型在处理交叉偏见时存在不足，未能充分考虑多重身份交叉带来的复杂性。
2. 本文提出WinoIdentity基准，通过增加多达25个社会属性，评估模型在不同交叉身份下的信心差异。
3. 实验结果显示，模型在某些身份下的信心差异高达40%，尤其对双重劣势身份表现出较低的信心，反映出模型的潜在偏见。

## 📝 摘要（中文）

大型语言模型（LLMs）在多个领域取得了显著的性能，然而它们可能反映并加剧社会偏见，尤其是在招聘和招生等关键社会场景中。本文扩展了单一轴线的公平性评估，探讨交叉偏见，提出了新的基准WinoIdentity，通过增加25个与性别交叉的社会属性，生成245,700个提示以评估50种偏见模式。研究发现，模型在不同人口属性下的信心差异高达40%，尤其在反刻板印象的环境中，对双重劣势身份的信心最低。这表明LLMs的优异表现可能源于记忆而非逻辑推理，揭示了价值对齐和有效性方面的独立失败，可能导致社会伤害。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在处理交叉偏见时的不足，现有方法主要关注单一轴线的公平性，未能考虑多重身份交叉所带来的独特劣势模式。

**核心思路**：通过构建WinoIdentity基准，增加多个社会属性与性别的交叉，评估模型在不同身份下的信心差异，以揭示潜在的交叉偏见。

**技术框架**：研究首先扩展了WinoBias数据集，增加了25个与性别交叉的属性，生成245,700个提示。接着，通过核心指代信心差异指标评估模型在不同身份下的表现。

**关键创新**：提出了核心指代信心差异这一新指标，能够量化模型对不同交叉身份的信心差异，揭示了模型在处理复杂身份时的不足。

**关键设计**：在实验中，采用了多种人口属性进行交叉分析，重点关注模型在反刻板印象环境中的表现，设计了相应的评估流程和指标。

## 📊 实验亮点

实验结果显示，五种大型语言模型在不同人口属性下的信心差异高达40%。特别是在反刻板印象的环境中，模型对双重劣势身份的信心最低，表明模型在处理复杂身份时存在显著的偏见。这些发现揭示了当前模型在价值对齐和有效性方面的独立失败。

## 🎯 应用场景

该研究的潜在应用领域包括招聘、招生、法律和医疗等社会决策场景。通过识别和量化交叉偏见，能够帮助开发更公平的AI系统，减少社会身份基础的伤害，推动社会公正。未来，研究结果可为政策制定和AI伦理提供重要参考。

## 📄 摘要（原文）

> Large language models (LLMs) have achieved impressive performance, leading to their widespread adoption as decision-support tools in resource-constrained contexts like hiring and admissions. There is, however, scientific consensus that AI systems can reflect and exacerbate societal biases, raising concerns about identity-based harm when used in critical social contexts. Prior work has laid a solid foundation for assessing bias in LLMs by evaluating demographic disparities in different language reasoning tasks. In this work, we extend single-axis fairness evaluations to examine intersectional bias, recognizing that when multiple axes of discrimination intersect, they create distinct patterns of disadvantage. We create a new benchmark called WinoIdentity by augmenting the WinoBias dataset with 25 demographic markers across 10 attributes, including age, nationality, and race, intersected with binary gender, yielding 245,700 prompts to evaluate 50 distinct bias patterns. Focusing on harms of omission due to underrepresentation, we investigate bias through the lens of uncertainty and propose a group (un)fairness metric called Coreference Confidence Disparity which measures whether models are more or less confident for some intersectional identities than others. We evaluate five recently published LLMs and find confidence disparities as high as 40% along various demographic attributes including body type, sexual orientation and socio-economic status, with models being most uncertain about doubly-disadvantaged identities in anti-stereotypical settings. Surprisingly, coreference confidence decreases even for hegemonic or privileged markers, indicating that the recent impressive performance of LLMs is more likely due to memorization than logical reasoning. Notably, these are two independent failures in value alignment and validity that can compound to cause social harm.

