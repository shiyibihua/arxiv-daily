---
layout: default
title: User-centric Subjective Leaderboard by Customizable Reward Modeling
---

# User-centric Subjective Leaderboard by Customizable Reward Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09463" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09463v1</a>
  <a href="https://arxiv.org/pdf/2508.09463.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09463v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09463v1', 'User-centric Subjective Leaderboard by Customizable Reward Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qi Jia, Xiujie Song, Zicheng Zhang, Yijin Guo, Kaiwei Zhang, Zijian Chen, Guangtao Zhai

**分类**: cs.CL

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出用户中心的主观排行榜以解决LLM选择难题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `用户中心` `主观排行榜` `可定制奖励模型` `大型语言模型` `个性化推荐` `人类偏好分析` `动态排名`

## 📋 核心要点

1. 现有的LLM基准主要依赖于可验证任务，难以满足用户的个性化需求，导致模型选择困难。
2. 提出用户中心的主观排行榜（USL），通过对人类偏好的深入分析，提供动态的模型排名。
3. 可定制奖励模型（CRMs）在仅有40亿参数的情况下，超越了现有领先模型，展现出优异的泛化能力。

## 📝 摘要（中文）

现有的大型语言模型（LLMs）基准主要通过可验证任务评估其能力，这种客观静态的基准在实际模型选择中效用有限，难以满足用户个性化需求。为此，我们提出了首个用户中心的主观排行榜（USL），提供基于偏好的动态排名，涵盖多种现实场景。我们的研究基于对超过1万条主观查询的深入调查，揭示了人类偏好的显著多样性和矛盾性，这限制了现有奖励模型的有效性。为了解决这一问题，我们引入了可定制奖励模型（CRMs），其参数量仅为40亿，性能超越了GPT-4.1和Gemini-2.5-pro，展现出在新主题和标准上的卓越泛化能力。USL依托CRMs，显示出与矛盾偏好的强负相关性。

## 🔬 方法详解

**问题定义**：现有的大型语言模型基准主要集中在可验证任务的评估上，这种方法无法有效反映用户的个性化需求，导致用户在选择合适模型时面临困难。

**核心思路**：本研究提出用户中心的主观排行榜（USL），通过分析真实的人类偏好数据，构建动态的模型排名系统，以更好地满足用户需求。

**技术框架**：USL的构建基于对超过1万条主观查询的调查，结合可定制奖励模型（CRMs），形成一个包含数据收集、模型训练和排名生成的完整流程。

**关键创新**：引入可定制奖励模型（CRMs），其参数量为40亿，超越了现有的领先模型，展现出在新主题和标准上的卓越泛化能力。与传统的静态奖励模型相比，CRMs能够更好地适应用户的多样化偏好。

**关键设计**：CRMs的设计包括特定的损失函数和网络结构，以优化对用户偏好的响应能力，同时确保模型在不同任务上的泛化性能。

## 📊 实验亮点

实验结果表明，CRMs在多个任务上超越了GPT-4.1和Gemini-2.5-pro，展现出显著的性能提升。具体而言，CRMs在新主题和标准上的泛化能力表现优异，与矛盾偏好的强负相关性进一步验证了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、内容生成和个性化推荐系统等。通过提供用户中心的模型选择工具，能够显著提升用户体验，帮助用户找到最符合其需求的语言模型，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Existing benchmarks for large language models (LLMs) predominantely focus on assessing their capabilities through verifiable tasks. Such objective and static benchmarks offer limited utility for practical LLM selection, making it difficult for users to find suitable models for their individual needs. To bridge this gap, we present the first User-Centric Subjective Leaderboard (USL), which provides a preference-driven, dynamic ranking of LLMs across diverse real-world scenarios. Our work is built upon a thorough investigation of real human preference data, involving more than 10K subjective queries. Our investigation reveals significant diversity and contradictions in human preferences, which limit the effectiveness of state-of-the-art reward models. To address this, we introduce Customizable Reward Models (CRMs). With only 4B parameters, our CRM surpasses the performance of leading models such as GPT-4.1 and Gemini-2.5-pro, showing exceptional generalization capabilities across new topics and criteria. The USL, powered by CRMs, exhibits strong negative correlations to contradictory preferences.

