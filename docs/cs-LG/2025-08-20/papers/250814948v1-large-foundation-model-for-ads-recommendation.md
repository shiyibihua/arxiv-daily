---
layout: default
title: Large Foundation Model for Ads Recommendation
---

# Large Foundation Model for Ads Recommendation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14948" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14948v1</a>
  <a href="https://arxiv.org/pdf/2508.14948.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14948v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14948v1', 'Large Foundation Model for Ads Recommendation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shangyu Zhang, Shijie Quan, Zhongren Wang, Junwei Pan, Tianqu Zhuang, Bo Fu, Yilong Sun, Jieying Lin, Jushuo Chen, Xiaotian Li, Zhixiang Feng, Xian Hu, Huiting Deng, Hua Lu, Jinpeng Wang, Boqi Dai, Xiaoyu Chen, Bin Hu, Lili Huang, Yanwen Wu, Yeshou Cai, Qi Zhou, Huang Tang, Chunfeng Yang, Chengguo Yin, Tingyu Jiang, Lifeng Wang, Shudong Huang, Dapeng Liu, Lei Xiao, Haijie Gu, Shu-Tao Xia, Jie Jiang

**分类**: cs.LG

**发布日期**: 2025-08-20

---

## 💡 一句话要点

**提出LFM4Ads框架以解决广告推荐中的多表示转移问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `广告推荐` `基础模型` `多表示转移` `用户表示` `物品表示` `交叉表示` `深度学习` `在线广告`

## 📋 核心要点

1. 现有广告推荐方法仅关注用户表示，忽略了物品表示和用户-物品交叉表示，导致信息转移不足。
2. 本文提出LFM4Ads框架，全面转移用户、物品及交叉表示，利用多粒度机制提升转移能力。
3. LFM4Ads在腾讯广告平台成功部署，处理数十亿样本，实现2.45%的GMV提升，显著增加年收入。

## 📝 摘要（中文）

在线广告依赖于准确的推荐模型，近期的研究利用预训练的大规模基础模型（LFM）捕捉用户在多场景和任务中的一般兴趣。然而，现有方法存在关键局限性：仅提取和转移用户表示（UR），忽视了有价值的物品表示（IR）和用户-物品交叉表示（CR）。本文提出LFM4Ads，一个全表示多粒度转移框架，全面转移UR、IR和CR。通过识别最优提取层并将CR聚合为可转移的粗粒度形式，增强了转移能力。LFM4Ads已成功部署于腾讯的工业广告平台，处理每日数十亿样本，取得了2.45%的整体GMV提升，年收入预计增加数亿美元。

## 🔬 方法详解

**问题定义**：本文旨在解决广告推荐中现有方法仅提取用户表示而忽视物品表示和用户-物品交叉表示的问题。这导致了信息转移的不足，无法有效提升推荐效果。

**核心思路**：LFM4Ads框架的核心思路是全面转移用户表示、物品表示和交叉表示，利用多粒度机制提高转移的有效性。通过识别最优提取层并聚合交叉表示，增强了模型的转移能力。

**技术框架**：LFM4Ads的整体架构包括三个主要模块：非线性适配器用于特征级转移，同构交互模块用于模块级转移，独立检索用于模型级转移。该框架通过多层次的转移机制实现了信息的全面利用。

**关键创新**：LFM4Ads的主要创新在于全面转移所有可用表示，并通过多粒度机制提升转移能力。这与现有方法的本质区别在于不再仅依赖用户表示，而是综合考虑所有相关表示。

**关键设计**：在设计上，LFM4Ads采用了非线性适配器和同构交互模块等关键技术，确保了不同层次的信息能够有效转移。此外，模型参数设置和损失函数设计也经过精心调整，以优化推荐效果。

## 📊 实验亮点

LFM4Ads在腾讯广告平台的实际应用中，处理了每日数十亿样本，并实现了2.45%的整体GMV提升。与基线模型相比，该框架在多个广告场景中取得了显著的性能提升，预计年收入增加数亿美元，展示了其强大的实际价值。

## 🎯 应用场景

LFM4Ads框架具有广泛的应用潜力，特别是在在线广告推荐领域。其全面的表示转移能力可以提升广告投放的精准度和效果，帮助企业实现更高的投资回报率。未来，该框架还可以扩展到其他推荐系统和个性化服务中，推动相关领域的发展。

## 📄 摘要（原文）

> Online advertising relies on accurate recommendation models, with recent advances using pre-trained large-scale foundation models (LFMs) to capture users' general interests across multiple scenarios and tasks. However, existing methods have critical limitations: they extract and transfer only user representations (URs), ignoring valuable item representations (IRs) and user-item cross representations (CRs); and they simply use a UR as a feature in downstream applications, which fails to bridge upstream-downstream gaps and overlooks more transfer granularities. In this paper, we propose LFM4Ads, an All-Representation Multi-Granularity transfer framework for ads recommendation. It first comprehensively transfers URs, IRs, and CRs, i.e., all available representations in the pre-trained foundation model. To effectively utilize the CRs, it identifies the optimal extraction layer and aggregates them into transferable coarse-grained forms. Furthermore, we enhance the transferability via multi-granularity mechanisms: non-linear adapters for feature-level transfer, an Isomorphic Interaction Module for module-level transfer, and Standalone Retrieval for model-level transfer. LFM4Ads has been successfully deployed in Tencent's industrial-scale advertising platform, processing tens of billions of daily samples while maintaining terabyte-scale model parameters with billions of sparse embedding keys across approximately two thousand features. Since its production deployment in Q4 2024, LFM4Ads has achieved 10+ successful production launches across various advertising scenarios, including primary ones like Weixin Moments and Channels. These launches achieve an overall GMV lift of 2.45% across the entire platform, translating to estimated annual revenue increases in the hundreds of millions of dollars.

