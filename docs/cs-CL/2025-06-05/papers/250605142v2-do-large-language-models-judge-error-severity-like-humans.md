---
layout: default
title: Do Large Language Models Judge Error Severity Like Humans?
---

# Do Large Language Models Judge Error Severity Like Humans?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05142" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05142v2</a>
  <a href="https://arxiv.org/pdf/2506.05142.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05142v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05142v2', 'Do Large Language Models Judge Error Severity Like Humans?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Diege Sun, Guanyi Chen, Zhao Fan, Xiaorong Cheng, Tingting He

**分类**: cs.CL

**发布日期**: 2025-06-05 (更新: 2025-06-09)

---

## 💡 一句话要点

**比较人类与大型语言模型在错误严重性判断上的差异**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `错误严重性` `多模态评估` `人类判断` `自动评估工具`

## 📋 核心要点

1. 现有的自动评估工具在判断错误严重性时，往往无法准确反映人类的判断标准，尤其是在多模态场景中。
2. 本研究通过扩展实验框架，系统比较人类与LLMs在不同错误类型下的评估，探讨其判断差异。
3. 实验结果显示，DeepSeek-V3在单模态和多模态条件下与人类判断的对齐度最高，表现优于其他模型。

## 📝 摘要（中文）

大型语言模型（LLMs）在自然语言生成中被广泛用作自动评估工具，但它们是否能准确复制人类对错误严重性的判断仍不明确。本研究系统比较了人类与LLMs对包含控制语义错误的图像描述的评估。我们扩展了van Miltenburg等（2020）的实验框架，评估了四种错误类型：年龄、性别、服装类型和颜色。研究发现，人类对不同错误类型赋予不同的严重性等级，视觉上下文显著增强了对颜色和类型错误的感知严重性。大多数LLMs对性别错误评分较低，但对颜色错误评分却异常高，这与人类的判断存在显著差异。这表明这些模型可能内化了影响性别判断的社会规范，但缺乏模拟人类对颜色敏感性的感知基础。仅有一个LLM（Doubao）在错误严重性排名上接近人类，但未能如人类般清晰地区分错误类型。令人惊讶的是，DeepSeek-V3作为单模态LLM在单模态和多模态条件下与人类判断的对齐度最高，甚至超过了最先进的多模态模型。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在评估图像描述错误严重性时与人类判断不一致的问题。现有方法在多模态评估中存在明显不足，无法准确反映人类的判断标准。

**核心思路**：通过系统比较人类与LLMs对不同类型错误的评估，探索模型在性别和颜色错误判断上的差异，进而分析其背后的原因。

**技术框架**：研究采用了扩展的实验框架，涵盖了单模态（仅文本）和多模态（文本+图像）设置，评估了四种错误类型。主要模块包括错误类型定义、评估标准设定和模型比较分析。

**关键创新**：本研究的创新点在于系统性地揭示了LLMs在错误严重性判断上的局限性，尤其是在性别和颜色错误的评估上，提供了对比分析的实证数据。

**关键设计**：实验中采用了控制语义错误的图像描述，设置了多种评估标准，并对不同模型的输出进行了详细分析，确保了实验的严谨性和结果的可靠性。

## 📊 实验亮点

实验结果显示，DeepSeek-V3在单模态和多模态条件下与人类判断的对齐度最高，超越了其他最先进的多模态模型。特别是在颜色错误的评估上，LLMs表现出与人类判断的显著差异，揭示了模型在社会规范内化与感知能力上的局限性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的自动评估系统、教育领域的自动评分工具以及社交媒体内容审核等。通过提高模型对错误严重性的判断能力，可以增强其在实际应用中的有效性和可靠性，未来可能推动更智能的内容生成和评估技术的发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly used as automated evaluators in natural language generation, yet it remains unclear whether they can accurately replicate human judgments of error severity. In this study, we systematically compare human and LLM assessments of image descriptions containing controlled semantic errors. We extend the experimental framework of van Miltenburg et al. (2020) to both unimodal (text-only) and multimodal (text + image) settings, evaluating four error types: age, gender, clothing type, and clothing colour. Our findings reveal that humans assign varying levels of severity to different error types, with visual context significantly amplifying perceived severity for colour and type errors. Notably, most LLMs assign low scores to gender errors but disproportionately high scores to colour errors, unlike humans, who judge both as highly severe but for different reasons. This suggests that these models may have internalised social norms influencing gender judgments but lack the perceptual grounding to emulate human sensitivity to colour, which is shaped by distinct neural mechanisms. Only one of the evaluated LLMs, Doubao, replicates the human-like ranking of error severity, but it fails to distinguish between error types as clearly as humans. Surprisingly, DeepSeek-V3, a unimodal LLM, achieves the highest alignment with human judgments across both unimodal and multimodal conditions, outperforming even state-of-the-art multimodal models.

