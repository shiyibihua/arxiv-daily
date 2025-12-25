---
layout: default
title: "ReaSeq: Unleashing World Knowledge via Reasoning for Sequential Modeling"
---

# ReaSeq: Unleashing World Knowledge via Reasoning for Sequential Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21257" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21257v1</a>
  <a href="https://arxiv.org/pdf/2512.21257.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21257v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21257v1', 'ReaSeq: Unleashing World Knowledge via Reasoning for Sequential Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chuan Wang, Gaoming Yang, Han Wu, Jiakai Tang, Jiahao Yu, Jian Wu, Jianwu Hu, Junjun Zheng, Shuwen Xiao, Yeqiu Yang, Yuning Jiang, Ahjol Nurlanbek, Binbin Cao, Bo Zheng, Fangmei Zhu, Gaoming Zhou, Huimin Yi, Huiping Chu, Jin Huang, Jinzhe Shan, Kenan Cui, Longbin Li, Silu Zhou, Wen Chen, Xia Ming, Xiang Gao, Xin Yao, Xingyu Wen, Yan Zhang, Yiwen Hu, Yulin Wang, Ziheng Bao, Zongyuan Wu

**分类**: cs.IR, cs.CL

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**ReaSeq：通过推理释放世界知识，用于序列建模，提升淘宝推荐系统性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推荐系统` `大型语言模型` `世界知识` `推理` `序列建模`

## 📋 核心要点

1. 现有推荐系统依赖日志数据，忽略了产品语义和跨领域行为模式等世界知识，导致模型在数据稀疏时表现不佳，且难以发现用户的新兴趣。
2. ReaSeq框架利用大型语言模型中的世界知识，通过显式思维链推理和隐式扩散模型推理，增强物品表示并推断用户行为。
3. 在淘宝推荐系统上的实验表明，ReaSeq在IPV、CTR、订单和GMV等指标上均取得了显著提升，验证了其有效性。

## 📝 摘要（中文）

工业推荐系统在日志驱动的范式下面临两个根本限制：（1）基于ID的物品表示缺乏知识，导致数据稀疏时兴趣建模脆弱；（2）对超出日志范围的用户兴趣的系统性盲视，将模型性能限制在平台边界内。这些限制源于过度依赖浅层交互统计和闭环反馈，而忽略了大型语言模型从海量语料库中学习到的关于产品语义和跨领域行为模式的丰富世界知识。为了解决这些挑战，我们引入了ReaSeq，这是一个推理增强框架，它利用大型语言模型中的世界知识，通过显式和隐式推理来解决这两个限制。具体来说，ReaSeq采用通过多智能体协作的显式思维链推理，将结构化产品知识提炼为语义丰富的物品表示，并通过扩散大型语言模型进行潜在推理，以推断合理的超出日志范围的行为。ReaSeq部署在为数亿用户提供服务的淘宝排名系统上，取得了显著的收益：IPV和CTR>6.0%，订单>2.9%，GMV>2.5%，验证了世界知识增强推理相对于纯日志驱动方法的有效性。

## 🔬 方法详解

**问题定义**：现有工业推荐系统过度依赖用户行为日志，导致两个主要问题：一是物品表示缺乏语义知识，难以应对数据稀疏性；二是模型无法有效探索用户在平台之外的潜在兴趣，限制了推荐效果的提升。现有方法难以充分利用大型语言模型中蕴含的丰富世界知识。

**核心思路**：ReaSeq的核心思路是利用大型语言模型（LLM）中蕴含的世界知识，通过显式和隐式推理来增强推荐系统的性能。显式推理用于丰富物品的语义表示，隐式推理用于推断用户在平台之外的潜在行为，从而克服现有方法的局限性。

**技术框架**：ReaSeq框架包含两个主要模块：
1. **显式推理模块**：采用多智能体协作的思维链（Chain-of-Thought）推理，从LLM中提取结构化的产品知识，并将其融入到物品的表示中，从而增强物品的语义信息。
2. **隐式推理模块**：利用扩散大型语言模型（Diffusion Large Language Models）来推断用户可能存在的超出日志范围的行为，从而扩展用户兴趣的覆盖范围。

**关键创新**：ReaSeq的关键创新在于将大型语言模型中的世界知识引入到推荐系统中，并设计了显式和隐式推理机制来有效利用这些知识。与传统的日志驱动方法相比，ReaSeq能够更好地理解物品的语义信息，并探索用户的潜在兴趣。

**关键设计**：
* **显式推理**：设计了多智能体协作的推理流程，每个智能体负责提取不同方面的产品知识，并通过协作来生成全面的物品表示。
* **隐式推理**：利用扩散模型生成用户可能感兴趣但未在日志中体现的行为序列，并将其作为增强数据来训练推荐模型。
* **损失函数**：采用了结合日志数据和生成数据的混合损失函数，以平衡模型在已知行为和潜在行为之间的学习。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21257v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21257v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21257v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

ReaSeq在淘宝推荐系统上进行了部署，并取得了显著的性能提升。实验结果表明，ReaSeq在IPV和CTR上提升了>6.0%，在订单上提升了>2.9%，在GMV上提升了>2.5%。这些数据表明，ReaSeq能够有效利用世界知识来增强推荐系统的性能，并显著提升用户体验和商业价值。

## 🎯 应用场景

ReaSeq具有广泛的应用前景，可应用于电商、新闻、视频等各种推荐系统。通过引入世界知识和推理能力，ReaSeq能够提升推荐系统的准确性、多样性和用户满意度，尤其是在数据稀疏或需要探索用户潜在兴趣的场景下，具有重要的实际价值和商业潜力。未来，ReaSeq可以进一步扩展到跨领域推荐、个性化搜索等领域。

## 📄 摘要（原文）

> Industrial recommender systems face two fundamental limitations under the log-driven paradigm: (1) knowledge poverty in ID-based item representations that causes brittle interest modeling under data sparsity, and (2) systemic blindness to beyond-log user interests that constrains model performance within platform boundaries. These limitations stem from an over-reliance on shallow interaction statistics and close-looped feedback while neglecting the rich world knowledge about product semantics and cross-domain behavioral patterns that Large Language Models have learned from vast corpora.
>   To address these challenges, we introduce ReaSeq, a reasoning-enhanced framework that leverages world knowledge in Large Language Models to address both limitations through explicit and implicit reasoning. Specifically, ReaSeq employs explicit Chain-of-Thought reasoning via multi-agent collaboration to distill structured product knowledge into semantically enriched item representations, and latent reasoning via Diffusion Large Language Models to infer plausible beyond-log behaviors. Deployed on Taobao's ranking system serving hundreds of millions of users, ReaSeq achieves substantial gains: >6.0% in IPV and CTR, >2.9% in Orders, and >2.5% in GMV, validating the effectiveness of world-knowledge-enhanced reasoning over purely log-driven approaches.

