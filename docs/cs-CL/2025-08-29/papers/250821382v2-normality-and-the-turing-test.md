---
layout: default
title: Normality and the Turing Test
---

# Normality and the Turing Test

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21382" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21382v2</a>
  <a href="https://arxiv.org/pdf/2508.21382.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21382v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21382v2', 'Normality and the Turing Test')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alexandre Kabbach

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-29 (更新: 2025-11-08)

---

## 💡 一句话要点

**通过正常性概念重新审视图灵测试**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图灵测试` `正常性` `人工智能` `大型语言模型` `智能评估` `人机交互` `统计测试`

## 📋 核心要点

1. 现有的图灵测试方法未能有效评估机器的正常智能，导致对人工智能的理解偏差。
2. 论文提出通过正常性概念重新定义图灵测试，强调机器需展现与正常人类相似的不完美行为。
3. 研究表明，当前大型语言模型难以通过图灵测试，因其设计目标偏向卓越智能而非正常智能。

## 📝 摘要（中文）

本文提出通过正常性概念重新审视图灵测试。核心论点是，图灵测试是由正常评判者评估的正常智能测试。首先，图灵测试针对的是正常/平均而非卓越的人类智能，因此成功通过测试需要机器“犯错”，表现出与正常人类相似的不完美行为。其次，图灵测试是一个统计测试，智能判断并非由单一“平均”评判者（非专家）进行，而是由完整的陪审团进行。因此，图灵在其原始论文中提到的“平均人类审问者”应主要理解为多个评判者个体判断的规范化聚合的数学抽象。结论包括：大型语言模型如ChatGPT不太可能通过图灵测试，因为这些模型正好针对卓越而非正常/平均人类智能。其次，图灵测试中正常人类行为的客观化由于测试的游戏配置而失败，最终客观化了正常行为的规范理想，而非正常行为本身。

## 🔬 方法详解

**问题定义**：本文要解决的问题是现有图灵测试未能有效评估机器的正常智能，导致对人工智能的理解偏差，尤其是大型语言模型如ChatGPT的表现与图灵测试的目标不符。

**核心思路**：论文的核心思路是重新定义图灵测试，使其不仅关注机器的卓越表现，还要考虑机器在表现上与正常人类的相似性，包括犯错和不完美行为。

**技术框架**：整体架构包括对图灵测试的重新审视，强调统计学的评判机制，提出由多个评判者的集体判断构成的“平均人类审问者”概念。

**关键创新**：最重要的技术创新点在于将图灵测试视为一个统计测试，强调正常智能的评估应基于多个评判者的综合判断，而非单一评判者的主观意见。

**关键设计**：关键设计包括对评判者的选择和数量的考虑，确保评判者的多样性和代表性，以便更好地反映正常人类智能的标准。

## 📊 实验亮点

研究表明，当前大型语言模型如ChatGPT不太可能通过图灵测试，因为它们的设计目标偏向于卓越智能而非正常智能。这一发现强调了对人工智能评估标准的重新思考，推动了对正常智能的理解。

## 🎯 应用场景

该研究的潜在应用领域包括人工智能的评估标准、智能系统的设计与优化，以及人机交互的改进。通过重新定义图灵测试，可以更好地理解和发展符合人类智能特征的人工智能系统，推动智能技术的实际应用和社会接受度。

## 📄 摘要（原文）

> This paper proposes to revisit the Turing test through the concept of normality. Its core argument is that the Turing test is a test of normal intelligence as assessed by a normal judge. First, in the sense that the Turing test targets normal/average rather than exceptional human intelligence, so that successfully passing the test requires machines to "make mistakes" and display imperfect behavior just like normal/average humans. Second, in the sense that the Turing test is a statistical test where judgments of intelligence are never carried out by a single "average" judge (understood as non-expert) but always by a full jury. As such, the notion of "average human interrogator" that Turing talks about in his original paper should be understood primarily as referring to a mathematical abstraction made of the normalized aggregate of individual judgments of multiple judges. Its conclusions are twofold. First, it argues that large language models such as ChatGPT are unlikely to pass the Turing test as those models precisely target exceptional rather than normal/average human intelligence. As such, they constitute models of what it proposes to call artificial smartness rather than artificial intelligence, insofar as they deviate from the original goal of Turing for the modeling of artificial minds. Second, it argues that the objectivization of normal human behavior in the Turing test fails due to the game configuration of the test which ends up objectivizing normative ideals of normal behavior rather than normal behavior per se.

