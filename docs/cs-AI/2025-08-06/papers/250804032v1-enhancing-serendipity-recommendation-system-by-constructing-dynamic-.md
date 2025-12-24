---
layout: default
title: Enhancing Serendipity Recommendation System by Constructing Dynamic User Knowledge Graphs with Large Language Models
---

# Enhancing Serendipity Recommendation System by Constructing Dynamic User Knowledge Graphs with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04032" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04032v1</a>
  <a href="https://arxiv.org/pdf/2508.04032.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04032v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04032v1', 'Enhancing Serendipity Recommendation System by Constructing Dynamic User Knowledge Graphs with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qian Yong, Yanhui Li, Jialiang Shi, Yaguang Dou, Tian Qi

**分类**: cs.IR, cs.AI

**发布日期**: 2025-08-06

**备注**: 8 pages

---

## 💡 一句话要点

**通过动态构建用户知识图谱提升推荐系统的意外性**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推荐系统` `用户知识图谱` `大型语言模型` `两跳推理` `用户体验` `意外性推荐` `电商应用`

## 📋 核心要点

1. 现有推荐系统因反馈循环导致内容同质化，用户满意度降低，形成过滤气泡效应。
2. 本文提出利用大型语言模型动态构建用户知识图谱，通过两跳推理识别用户潜在兴趣，提升推荐的意外性。
3. 在Dewu应用上的实验结果显示，该方法使曝光新颖率提升4.62%，点击新颖率提升4.85%，用户体验显著改善。

## 📝 摘要（中文）

工业推荐系统中的反馈循环强化了同质化内容，导致过滤气泡效应，降低用户满意度。近期，大型语言模型（LLMs）在意外性推荐中展现出潜力，但仍面临推理过程合理性、结果实用性及延迟要求等挑战。为此，本文提出一种利用LLM动态构建用户知识图谱的方法，以增强推荐系统的意外性。该方法包括两个阶段：第一阶段是利用用户静态资料和历史行为进行两跳兴趣推理，构建用户知识图谱；第二阶段是近线适应，提出一种用户到物品（u2i）检索模型，结合物品到物品（i2i）检索能力。在线实验表明，该方法显著提升了用户体验。

## 🔬 方法详解

**问题定义**：本文旨在解决工业推荐系统中因反馈循环导致的内容同质化和用户满意度下降的问题。现有方法在推理过程的合理性和结果的实用性方面存在不足。

**核心思路**：通过利用大型语言模型（LLM）动态构建用户知识图谱，进行两跳兴趣推理，从而识别用户潜在兴趣，增强推荐的意外性。

**技术框架**：整体方法分为两个阶段：第一阶段是两跳兴趣推理，利用用户静态资料和历史行为构建用户知识图谱；第二阶段是近线适应，提出用户到物品（u2i）检索模型，结合物品到物品（i2i）检索能力。

**关键创新**：最重要的创新在于动态构建用户知识图谱的能力，利用LLM进行两跳推理，从而提高推理结果的质量和准确性，与传统方法相比，能够更好地捕捉用户的潜在兴趣。

**关键设计**：在模型设计中，采用了用户静态资料和历史行为作为输入，设置了合理的损失函数以优化推理结果，并设计了高效的检索机制以满足工业推荐系统的延迟要求。

## 📊 实验亮点

实验结果表明，所提方法在Dewu应用中显著提升了曝光新颖率4.62%，点击新颖率4.85%，平均每人观看时长增加0.15%，独立访客点击率提升0.07%，独立访客互动渗透率提升0.30%，有效增强了用户体验。

## 🎯 应用场景

该研究的潜在应用领域包括电商平台、社交媒体和内容推荐系统等，能够有效提升用户体验和满意度。通过动态构建用户知识图谱，推荐系统可以更好地理解用户需求，提供个性化的推荐，从而增加用户粘性和转化率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The feedback loop in industrial recommendation systems reinforces homogeneous content, creates filter bubble effects, and diminishes user satisfaction. Recently, large language models(LLMs) have demonstrated potential in serendipity recommendation, thanks to their extensive world knowledge and superior reasoning capabilities. However, these models still face challenges in ensuring the rationality of the reasoning process, the usefulness of the reasoning results, and meeting the latency requirements of industrial recommendation systems (RSs). To address these challenges, we propose a method that leverages llm to dynamically construct user knowledge graphs, thereby enhancing the serendipity of recommendation systems. This method comprises a two stage framework:(1) two-hop interest reasoning, where user static profiles and historical behaviors are utilized to dynamically construct user knowledge graphs via llm. Two-hop reasoning, which can enhance the quality and accuracy of LLM reasoning results, is then performed on the constructed graphs to identify users' potential interests; and(2) Near-line adaptation, a cost-effective approach to deploying the aforementioned models in industrial recommendation systems. We propose a u2i (user-to-item) retrieval model that also incorporates i2i (item-to-item) retrieval capabilities, the retrieved items not only exhibit strong relevance to users' newly emerged interests but also retain the high conversion rate of traditional u2i retrieval. Our online experiments on the Dewu app, which has tens of millions of users, indicate that the method increased the exposure novelty rate by 4.62%, the click novelty rate by 4.85%, the average view duration per person by 0.15%, unique visitor click through rate by 0.07%, and unique visitor interaction penetration by 0.30%, enhancing user experience.

