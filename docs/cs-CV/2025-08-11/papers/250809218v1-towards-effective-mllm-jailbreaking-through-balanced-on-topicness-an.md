---
layout: default
title: Towards Effective MLLM Jailbreaking Through Balanced On-Topicness and OOD-Intensity
---

# Towards Effective MLLM Jailbreaking Through Balanced On-Topicness and OOD-Intensity

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09218" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09218v1</a>
  <a href="https://arxiv.org/pdf/2508.09218.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09218v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09218v1', 'Towards Effective MLLM Jailbreaking Through Balanced On-Topicness and OOD-Intensity')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zuoou Li, Weitong Zhang, Jingyuan Wang, Shuyuan Zhang, Wenjia Bai, Bernhard Kainz, Mengyun Qiao

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-11

---

## 💡 一句话要点

**提出四轴评估框架与BSD策略以提升MLLM越狱效果**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大型语言模型` `越狱策略` `安全机制` `对抗性提示` `评估框架` `平衡结构分解` `有害输出` `网络安全`

## 📋 核心要点

1. 现有的多模态大型语言模型在面对对抗性提示时存在显著脆弱性，安全机制无法有效阻止有害输出。
2. 本文提出了一种四轴评估框架，并开发了平衡结构分解（BSD）策略，以优化恶意提示的结构，增强其有效性。
3. 在对13种商业和开源MLLM的实验中，BSD策略使攻击成功率提高67%，有害性提升21%，显著改善了现有方法的不足。

## 📝 摘要（中文）

多模态大型语言模型（MLLM）在视觉语言推理任务中广泛应用，但其对对抗性提示的脆弱性令人担忧。现有的越狱策略虽然成功率高，但许多被认为“成功”的响应实际上是良性、模糊或与恶意目标无关的。为了解决这一问题，本文提出了一个四轴评估框架，考虑输入的主题相关性、分布外强度、输出的有害性和拒绝率。通过实证研究，发现高相关性提示常被安全过滤器阻挡，而过于分布外的提示虽然逃避检测却无法产生有害内容。基于此，本文开发了一种名为平衡结构分解（BSD）的递归重写策略，旨在平衡相关性与新颖性，从而提高攻击成功率和有害输出。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大型语言模型（MLLM）在面对对抗性提示时的脆弱性，现有的越狱策略往往高估了其有效性，导致许多“成功”响应并未真正实现恶意目标。

**核心思路**：提出四轴评估框架，考虑输入的主题相关性、分布外强度、输出的有害性和拒绝率，识别真正有效的越狱。同时，开发平衡结构分解（BSD）策略，通过重构提示来平衡相关性与新颖性。

**技术框架**：整体流程包括四个主要模块：输入评估（分析提示的主题相关性和分布外强度）、输出评估（检测输出的有害性和拒绝率）、提示重构（应用BSD策略进行递归重写）、以及效果验证（评估攻击成功率和输出质量）。

**关键创新**：最重要的创新在于引入了四轴评估框架和BSD策略，前者提供了更全面的评估标准，后者通过结构化重写提高了恶意提示的有效性，与现有方法相比，显著提升了攻击成功率和输出有害性。

**关键设计**：在BSD策略中，提示被重构为语义对齐的子任务，同时引入微妙的分布外信号和视觉线索，以增加输入的隐蔽性。实验中对参数设置进行了优化，以确保在不同MLLM上均能实现最佳效果。

## 📊 实验亮点

实验结果显示，平衡结构分解（BSD）策略在13种MLLM上实现了67%的攻击成功率提升和21%的有害性提升，显著优于以往方法，揭示了当前多模态安全系统的潜在弱点。

## 🎯 应用场景

该研究的潜在应用领域包括网络安全、内容审查和对抗性机器学习等。通过提升对多模态大型语言模型的攻击能力，能够更好地理解和改进现有的安全机制，从而在实际应用中降低有害内容生成的风险，增强系统的鲁棒性。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) are widely used in vision-language reasoning tasks. However, their vulnerability to adversarial prompts remains a serious concern, as safety mechanisms often fail to prevent the generation of harmful outputs. Although recent jailbreak strategies report high success rates, many responses classified as "successful" are actually benign, vague, or unrelated to the intended malicious goal. This mismatch suggests that current evaluation standards may overestimate the effectiveness of such attacks. To address this issue, we introduce a four-axis evaluation framework that considers input on-topicness, input out-of-distribution (OOD) intensity, output harmfulness, and output refusal rate. This framework identifies truly effective jailbreaks. In a substantial empirical study, we reveal a structural trade-off: highly on-topic prompts are frequently blocked by safety filters, whereas those that are too OOD often evade detection but fail to produce harmful content. However, prompts that balance relevance and novelty are more likely to evade filters and trigger dangerous output. Building on this insight, we develop a recursive rewriting strategy called Balanced Structural Decomposition (BSD). The approach restructures malicious prompts into semantically aligned sub-tasks, while introducing subtle OOD signals and visual cues that make the inputs harder to detect. BSD was tested across 13 commercial and open-source MLLMs, where it consistently led to higher attack success rates, more harmful outputs, and fewer refusals. Compared to previous methods, it improves success rates by $67\%$ and harmfulness by $21\%$, revealing a previously underappreciated weakness in current multimodal safety systems.

