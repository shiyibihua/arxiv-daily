---
layout: default
title: SeaLLMs -- Large Language Models for Southeast Asia
---

# SeaLLMs -- Large Language Models for Southeast Asia

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.00738" class="toolbar-btn" target="_blank">📄 arXiv: 2312.00738v2</a>
  <a href="https://arxiv.org/pdf/2312.00738.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.00738v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.00738v2', 'SeaLLMs -- Large Language Models for Southeast Asia')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuan-Phi Nguyen, Wenxuan Zhang, Xin Li, Mahani Aljunied, Zhiqiang Hu, Chenhui Shen, Yew Ken Chia, Xingxuan Li, Jianyu Wang, Qingyu Tan, Liying Cheng, Guanzheng Chen, Yue Deng, Sen Yang, Chaoqun Liu, Hang Zhang, Lidong Bing

**分类**: cs.CL

**发布日期**: 2023-12-01 (更新: 2024-07-01)

**备注**: Technical report, ACL 2024 DEMO TRACK

---

## 💡 一句话要点

**提出SeaLLMs以解决东南亚语言资源不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `东南亚语言` `语言偏见` `模型调优` `文化适应性` `自然语言处理` `低资源语言` `机器学习`

## 📋 核心要点

1. 现有大型语言模型在处理低资源和区域语言时存在显著的语言偏见，导致这些语言的使用受到限制。
2. 论文提出的SeaLLMs系列模型专注于东南亚语言，通过扩展词汇和专门的调优方法，增强了对区域语言的理解和生成能力。
3. 实验结果显示，SeaLLM-13b在多种语言任务中表现优异，尤其在非拉丁语言上超越了ChatGPT-3.5，具有更好的实用性。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）在多种任务中取得了显著成就，但仍存在对高资源语言的偏见，低资源和区域语言常常被忽视。为了解决这一不平衡问题，我们提出了SeaLLMs，这是一系列专注于东南亚语言的创新语言模型。SeaLLMs基于Llama-2模型，经过扩展词汇的持续预训练、专门的指令和对齐调优，能够更好地捕捉区域语言的复杂性。我们的综合评估表明，SeaLLM-13b模型在多种语言任务和助手风格的指令跟随能力上，相较于可比的开源模型表现出色，尤其在泰语、柬埔寨语、老挝语和缅甸语等非拉丁语言中，性能大幅超越ChatGPT-3.5，同时保持轻量和成本效益。

## 🔬 方法详解

**问题定义**：论文要解决的具体问题是大型语言模型在低资源和区域语言上的表现不足，现有方法往往偏向高资源语言，导致东南亚语言的使用受到限制。

**核心思路**：论文的核心解决思路是构建SeaLLMs系列模型，专注于东南亚语言，通过扩展词汇和针对性的调优，提升模型对这些语言的理解和生成能力。

**技术框架**：SeaLLMs的整体架构基于Llama-2模型，经过持续的预训练和对齐调优，主要模块包括扩展词汇、指令调优和文化适应性调整。

**关键创新**：最重要的技术创新点在于针对东南亚语言的专门设计，使得模型能够更好地反映当地文化、习俗和语言特征，这与现有方法的通用性设计形成鲜明对比。

**关键设计**：在关键设计方面，SeaLLMs采用了扩展的词汇表，结合特定的损失函数和网络结构，以确保模型在处理区域语言时的准确性和流畅性。具体的参数设置和调优策略也经过精心设计，以适应不同语言的特性。

## 📊 实验亮点

实验结果显示，SeaLLM-13b模型在多种语言任务中表现优异，尤其在非拉丁语言（如泰语、柬埔寨语、老挝语和缅甸语）上，相较于ChatGPT-3.5，性能提升幅度显著，展示了其在低资源语言处理上的优势。

## 🎯 应用场景

该研究的潜在应用领域包括教育、翻译、文化传播和智能助手等。SeaLLMs能够为东南亚地区的用户提供更为精准和自然的语言服务，促进当地语言的数字化和应用，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> Despite the remarkable achievements of large language models (LLMs) in various tasks, there remains a linguistic bias that favors high-resource languages, such as English, often at the expense of low-resource and regional languages. To address this imbalance, we introduce SeaLLMs, an innovative series of language models that specifically focuses on Southeast Asian (SEA) languages. SeaLLMs are built upon the Llama-2 model and further advanced through continued pre-training with an extended vocabulary, specialized instruction and alignment tuning to better capture the intricacies of regional languages. This allows them to respect and reflect local cultural norms, customs, stylistic preferences, and legal considerations. Our comprehensive evaluation demonstrates that SeaLLM-13b models exhibit superior performance across a wide spectrum of linguistic tasks and assistant-style instruction-following capabilities relative to comparable open-source models. Moreover, they outperform ChatGPT-3.5 in non-Latin languages, such as Thai, Khmer, Lao, and Burmese, by large margins while remaining lightweight and cost-effective to operate.

