---
layout: default
title: A Metric for MLLM Alignment in Large-scale Recommendation
---

# A Metric for MLLM Alignment in Large-scale Recommendation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04963" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04963v1</a>
  <a href="https://arxiv.org/pdf/2508.04963.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04963v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04963v1', 'A Metric for MLLM Alignment in Large-scale Recommendation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yubin Zhang, Yanhua Huang, Haiming Xu, Mingliang Qi, Chang Wang, Jiarui Jin, Xiangyuan Ren, Xiaodan Wang, Ruiwen Xu

**分类**: cs.IR, cs.LG

**发布日期**: 2025-08-07

**备注**: Pre-print.Under Review

---

## 💡 一句话要点

**提出泄漏影响评分以解决多模态推荐系统对齐问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推荐` `大语言模型` `对齐评估` `泄漏影响评分` `用户体验` `广告效果` `推荐系统`

## 📋 核心要点

1. 现有方法在评估多模态大语言模型（MLLM）与推荐系统的对齐时面临静态基准不准确、在线评估成本高和传统指标缺乏可操作性等挑战。
2. 本文提出泄漏影响评分（LIS），该指标通过高效测量偏好数据的上限，解决了MLLM对齐评估中的主要问题。
3. 在小红书的内容推荐和展示广告的在线A/B测试中，LIS方法显著提高了用户停留时间和广告商价值，验证了其有效性。

## 📝 摘要（中文）

多模态推荐已成为现代推荐系统中的关键技术，利用先进的多模态大语言模型（MLLM）进行内容表示。为了确保这些表示的良好适应性，与推荐系统的对齐至关重要。然而，评估MLLM在推荐中的对齐存在显著挑战，包括静态基准不准确、在线系统评估成本高昂以及传统指标无法提供可操作的见解。为此，本文提出了一种新颖的多模态推荐指标——泄漏影响评分（LIS），该指标高效地测量偏好数据的上限。我们还分享了在实际场景中使用LIS部署MLLM的实用见解。在线A/B测试结果表明，该方法在用户停留时间和广告价值方面显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态推荐系统中MLLM对齐评估的困难，现有方法在动态应用场景中表现不佳，且在线评估成本高昂。

**核心思路**：提出泄漏影响评分（LIS），该指标通过测量偏好数据的上限，间接评估MLLM的对齐效果，避免了直接评估的复杂性和成本。

**技术框架**：LIS的整体架构包括数据收集、偏好数据分析和评分计算三个主要模块。首先收集用户交互数据，然后分析偏好数据以计算LIS，最后将评分应用于推荐系统优化。

**关键创新**：LIS作为一种新颖的评估指标，突破了传统评估方法的局限，能够在动态环境中提供更准确的对齐评估，具有更高的实用性。

**关键设计**：在LIS的设计中，重点考虑了偏好数据的动态变化，采用了适应性算法来实时更新评分，确保评估结果的准确性和时效性。具体的参数设置和损失函数设计尚未详细披露，需进一步研究。

## 📊 实验亮点

在小红书的在线A/B测试中，使用LIS方法显著提高了用户停留时间和广告商价值，具体提升幅度未详细披露，但结果表明该方法在实际应用中具有显著效果。

## 🎯 应用场景

该研究的潜在应用领域包括电商平台、社交媒体和内容推荐系统等，能够帮助这些系统更好地利用多模态大语言模型，提高用户体验和广告效果。未来，LIS的应用可能推动推荐系统的智能化发展，提升个性化推荐的准确性和效率。

## 📄 摘要（原文）

> Multimodal recommendation has emerged as a critical technique in modern recommender systems, leveraging content representations from advanced multimodal large language models (MLLMs). To ensure these representations are well-adapted, alignment with the recommender system is essential. However, evaluating the alignment of MLLMs for recommendation presents significant challenges due to three key issues: (1) static benchmarks are inaccurate because of the dynamism in real-world applications, (2) evaluations with online system, while accurate, are prohibitively expensive at scale, and (3) conventional metrics fail to provide actionable insights when learned representations underperform. To address these challenges, we propose the Leakage Impact Score (LIS), a novel metric for multimodal recommendation. Rather than directly assessing MLLMs, LIS efficiently measures the upper bound of preference data. We also share practical insights on deploying MLLMs with LIS in real-world scenarios. Online A/B tests on both Content Feed and Display Ads of Xiaohongshu's Explore Feed production demonstrate the effectiveness of our proposed method, showing significant improvements in user spent time and advertiser value.

