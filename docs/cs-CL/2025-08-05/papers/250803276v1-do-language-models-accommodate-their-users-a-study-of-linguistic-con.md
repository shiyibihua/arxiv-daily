---
layout: default
title: Do language models accommodate their users? A study of linguistic convergence
---

# Do language models accommodate their users? A study of linguistic convergence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03276" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03276v1</a>
  <a href="https://arxiv.org/pdf/2508.03276.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03276v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03276v1', 'Do language models accommodate their users? A study of linguistic convergence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Terra Blevins, Susanne Schmalwieser, Benjamin Roth

**分类**: cs.CL

**发布日期**: 2025-08-05

---

## 💡 一句话要点

**研究语言模型的语言适应性，揭示其与用户的语言趋同现象**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `语言趋同` `人机交互` `对话系统` `适应性研究` `模型比较` `语用元素`

## 📋 核心要点

1. 现有研究对大型语言模型与人类语言使用的相似性关注不足，缺乏对模型是否会适应用户语言模式的系统性研究。
2. 论文通过比较十六种语言模型在对话中的生成结果与人类响应，探讨模型的语言趋同现象，揭示其适应性。
3. 研究结果表明，模型在对话风格上强烈趋同，且不同模型的趋同程度存在显著差异，尤其是指令调优模型趋同较少。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）在生成语言方面被普遍认为是熟练的，但它们的语言使用与人类的相似程度仍然未得到充分研究。本文测试了模型是否表现出语言趋同这一人类语言交流的核心语用元素，探讨模型是否会适应或趋同于用户的语言模式。通过系统比较十六种语言模型在三种对话语料库中的生成结果与原始人类响应，发现模型在对话风格上强烈趋同，且往往相对于人类基线显著过拟合。尽管趋同模式通常是特征特定的，但在不同建模设置中观察到趋同的一致性变化，指令调优和更大模型的趋同程度低于其预训练对应物。基于人类与模型趋同模式的差异，假设其背后的机制可能截然不同。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在语言生成中是否会趋同于用户语言模式的问题。现有方法未能系统性地探讨模型与人类语言使用的相似性，导致对模型适应性的理解不足。

**核心思路**：论文的核心思路是通过系统比较模型生成的对话与人类响应，分析模型在语言使用上的趋同现象，探讨其适应性和特征特定性。

**技术框架**：研究采用了十六种语言模型，结合三种对话语料库，分析了多种风格特征。整体流程包括数据收集、模型生成、特征提取和比较分析。

**关键创新**：最重要的技术创新在于系统性地比较不同模型的语言趋同现象，揭示了指令调优和更大模型在趋同程度上的显著差异，这与现有研究的单一模型分析形成对比。

**关键设计**：研究中使用了多种风格特征进行分析，模型的选择涵盖了不同规模和训练方式，确保了结果的全面性和可靠性。

## 📊 实验亮点

实验结果显示，模型在对话风格上表现出强烈的趋同现象，相较于人类基线，模型的过拟合程度显著。特别是指令调优和更大模型的趋同程度低于预训练模型，表明模型的适应性存在显著差异。

## 🎯 应用场景

该研究的潜在应用领域包括人机交互、对话系统和个性化推荐等。通过理解语言模型的适应性，可以优化模型在实际应用中的表现，提高用户体验和交互质量，未来可能推动更自然的对话系统发展。

## 📄 摘要（原文）

> While large language models (LLMs) are generally considered proficient in generating language, how similar their language usage is to that of humans remains understudied. In this paper, we test whether models exhibit linguistic convergence, a core pragmatic element of human language communication, asking: do models adapt, or converge, to the linguistic patterns of their user? To answer this, we systematically compare model completions of exisiting dialogues to the original human responses across sixteen language models, three dialogue corpora, and a variety of stylometric features. We find that models strongly converge to the conversation's style, often significantly overfitting relative to the human baseline. While convergence patterns are often feature-specific, we observe consistent shifts in convergence across modeling settings, with instruction-tuned and larger models converging less than their pretrained counterparts. Given the differences between human and model convergence patterns, we hypothesize that the underlying mechanisms for these behaviors are very different.

