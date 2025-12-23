---
layout: default
title: Aligning Large Language Models with Implicit Preferences from User-Generated Content
---

# Aligning Large Language Models with Implicit Preferences from User-Generated Content

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04463" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04463v1</a>
  <a href="https://arxiv.org/pdf/2506.04463.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04463v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04463v1', 'Aligning Large Language Models with Implicit Preferences from User-Generated Content')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaoxuan Tan, Zheng Li, Tianyi Liu, Haodong Wang, Hyokun Yun, Ming Zeng, Pei Chen, Zhihan Zhang, Yifan Gao, Ruijie Wang, Priyanka Nigam, Bing Yin, Meng Jiang

**分类**: cs.CL

**发布日期**: 2025-06-04

**备注**: Accepted to ACL 2025 Main Conference

---

## 💡 一句话要点

**提出PUGC框架以利用用户生成内容隐式偏好改善LLM对齐问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `用户生成内容` `隐式偏好` `大型语言模型` `偏好学习` `响应生成`

## 📋 核心要点

1. 现有的偏好学习方法过于依赖人工或高级LLMs的策划数据，导致成本高且难以扩展。
2. 本文提出的PUGC框架利用未标记的用户生成内容中的隐式偏好生成偏好数据，提升了对齐效果。
3. 实验结果显示，使用DPO和PUGC训练的模型在性能上提高了9.37%，并在长度控制上达到了35.93%的胜率。

## 📝 摘要（中文）

学习偏好反馈对于将大型语言模型（LLMs）与人类价值观对齐以及提高生成响应的质量至关重要。然而，现有的偏好学习方法过于依赖人工或先进LLMs的策划数据，成本高且难以扩展。本文提出了一种新颖的框架PUGC，利用未标记的用户生成内容（UGC）中的隐式人类偏好生成偏好数据。尽管UGC并非专门为指导LLMs生成符合人类偏好的响应而创建，但它通常反映了创作者的宝贵见解和隐式偏好。PUGC将UGC转化为用户查询，并从策略模型生成响应，随后利用UGC作为响应评分的参考文本，从而使模型与这些隐式偏好对齐。实验结果表明，使用DPO和PUGC训练的模型在Alpaca Eval 2上比传统方法提高了9.37%的性能，达到了35.93%的最先进的长度控制胜率。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型与人类偏好对齐的挑战，现有方法依赖于人工策划数据，难以扩展且成本高昂。

**核心思路**：提出PUGC框架，利用用户生成内容中的隐式偏好生成偏好数据，避免了对策划数据的依赖，从而实现更高效的对齐。

**技术框架**：PUGC框架包括三个主要模块：首先，将UGC转化为用户查询；其次，从策略模型生成响应；最后，利用UGC作为参考文本进行响应评分，以实现模型与隐式偏好的对齐。

**关键创新**：PUGC的核心创新在于利用UGC中的隐式偏好，而非依赖于人工标注的数据，从而提高了偏好数据的质量和可扩展性。

**关键设计**：在模型训练中，采用了特定的损失函数来优化响应评分，并设计了适应UGC特性的网络结构，以增强模型的对齐能力。

## 📊 实验亮点

实验结果表明，使用DPO和PUGC训练的模型在Alpaca Eval 2上实现了9.37%的性能提升，并在长度控制上达到了35.93%的胜率，显著优于传统方法，展示了该方法在偏好学习中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能客服、内容推荐和人机交互等。通过利用用户生成内容的隐式偏好，PUGC框架能够在多个领域实现更高质量的响应生成，提升用户体验，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Learning from preference feedback is essential for aligning large language models (LLMs) with human values and improving the quality of generated responses. However, existing preference learning methods rely heavily on curated data from humans or advanced LLMs, which is costly and difficult to scale. In this work, we present PUGC, a novel framework that leverages implicit human Preferences in unlabeled User-Generated Content (UGC) to generate preference data. Although UGC is not explicitly created to guide LLMs in generating human-preferred responses, it often reflects valuable insights and implicit preferences from its creators that has the potential to address readers' questions. PUGC transforms UGC into user queries and generates responses from the policy model. The UGC is then leveraged as a reference text for response scoring, aligning the model with these implicit preferences. This approach improves the quality of preference data while enabling scalable, domain-specific alignment. Experimental results on Alpaca Eval 2 show that models trained with DPO and PUGC achieve a 9.37% performance improvement over traditional methods, setting a 35.93% state-of-the-art length-controlled win rate using Mistral-7B-Instruct. Further studies highlight gains in reward quality, domain-specific alignment effectiveness, robustness against UGC quality, and theory of mind capabilities. Our code and dataset are available at https://zhaoxuan.info/PUGC.github.io/

