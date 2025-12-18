---
layout: default
title: Semi-Supervised Synthetic Data Generation with Fine-Grained Relevance Control for Short Video Search Relevance Modeling
---

# Semi-Supervised Synthetic Data Generation with Fine-Grained Relevance Control for Short Video Search Relevance Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16717" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16717v2</a>
  <a href="https://arxiv.org/pdf/2509.16717.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16717v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16717v2', 'Semi-Supervised Synthetic Data Generation with Fine-Grained Relevance Control for Short Video Search Relevance Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoran Li, Zhiming Su, Junyan Yao, Enwei Zhang, Yang Ji, Yan Chen, Kan Zhou, Chao Feng, Jiao Ran

**分类**: cs.CL

**发布日期**: 2025-09-20 (更新: 2025-12-04)

**备注**: Submitted to AAAI 2026

---

## 💡 一句话要点

**提出半监督合成数据生成方法，解决短视频搜索相关性建模中数据稀缺和细粒度相关性不足问题。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `短视频搜索` `相关性建模` `半监督学习` `合成数据生成` `细粒度相关性` `embedding模型` `数据增强`

## 📋 核心要点

1. 现有基于prompt的合成数据方法难以捕捉短视频领域特定数据分布，尤其缺乏细粒度相关性多样性。
2. 提出半监督合成数据pipeline，通过协同训练模型生成可控相关性标签的领域自适应短视频数据，提升数据多样性。
3. 实验表明，该方法显著提升了embedding模型在短视频搜索相关性建模中的性能，并在抖音推荐系统中取得实际收益。

## 📝 摘要（中文）

合成数据被广泛应用于embedding模型中，以确保训练数据分布在难度、长度和语言等维度上的多样性。然而，现有的基于prompt的合成方法难以捕捉特定领域的数据分布，尤其是在数据稀缺的领域，并且常常忽略细粒度的相关性多样性。本文提出了一个中文短视频数据集，具有4级相关性标注，填补了关键的资源空白。此外，我们提出了一种半监督合成数据pipeline，其中两个协同训练的模型生成具有可控相关性标签的领域自适应短视频数据。我们的方法通过为代表性不足的中间相关性标签合成样本来增强相关性级别的多样性，从而产生更平衡和语义更丰富的训练数据集。大量的离线实验表明，在我们的合成数据上训练的embedding模型优于使用基于prompt或vanilla监督微调(SFT)生成的数据训练的模型。此外，我们证明了在训练数据中加入更多样化的细粒度相关性级别可以增强模型对细微语义差异的敏感性，突出了细粒度相关性监督在embedding学习中的价值。在抖音双列场景的搜索增强推荐pipeline中，通过在线A/B测试，所提出的模型点击率(CTR)提高了1.45%，强相关比例(SRR)提高了4.9%，图像用户渗透率(IUPR)提高了0.1054%。

## 🔬 方法详解

**问题定义**：论文旨在解决短视频搜索相关性建模中训练数据不足以及现有合成数据方法无法有效捕捉细粒度相关性信息的问题。现有方法要么依赖人工标注，成本高昂，要么使用prompt生成数据，但prompt难以覆盖领域特定知识，且忽略了不同相关性等级之间的细微差别。

**核心思路**：论文的核心思路是利用半监督学习，协同训练两个模型：一个负责生成高质量的合成数据，另一个负责评估和筛选生成的数据，从而构建一个更平衡、更具语义信息量的训练数据集。通过控制生成数据的相关性标签，特别是增加中间相关性等级的数据，来提升模型对细粒度语义差异的敏感性。

**技术框架**：该方法包含以下主要阶段：1) 构建包含4级相关性标注的中文短视频数据集；2) 设计半监督合成数据pipeline，包含两个协同训练的模型（生成模型和评估模型）；3) 使用合成数据训练embedding模型；4) 离线实验评估和在线A/B测试。生成模型负责根据给定的prompt生成短视频数据，评估模型负责评估生成数据的质量和相关性。

**关键创新**：该方法最重要的创新点在于半监督的合成数据生成pipeline，它能够自适应地学习领域特定知识，并生成具有可控相关性标签的数据。与传统的prompt方法相比，该方法能够更好地捕捉细粒度的相关性信息，从而提升模型的性能。

**关键设计**：关键设计包括：1) 设计合适的prompt，引导生成模型生成高质量的短视频数据；2) 设计评估模型，用于评估生成数据的质量和相关性；3) 设计损失函数，用于协同训练生成模型和评估模型；4) 通过控制生成数据的相关性标签分布，特别是增加中间相关性等级的数据，来提升模型对细粒度语义差异的敏感性。具体参数设置和网络结构等细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

离线实验表明，使用该方法生成的合成数据训练的embedding模型优于基于prompt或监督微调的模型。在线A/B测试显示，在抖音双列场景的搜索增强推荐pipeline中，该模型点击率(CTR)提高了1.45%，强相关比例(SRR)提高了4.9%，图像用户渗透率(IUPR)提高了0.1054%。

## 🎯 应用场景

该研究成果可应用于短视频搜索、推荐系统等领域，提升用户搜索和浏览体验。通过生成高质量的合成数据，可以有效解决数据稀缺问题，降低人工标注成本，并提升模型对细粒度语义信息的理解能力。该方法具有较强的通用性，可推广到其他数据稀缺的领域。

## 📄 摘要（原文）

> Synthetic data is widely adopted in embedding models to ensure diversity in training data distributions across dimensions such as difficulty, length, and language. However, existing prompt-based synthesis methods struggle to capture domain-specific data distributions, particularly in data-scarce domains, and often overlook fine-grained relevance diversity. In this paper, we present a Chinese short video dataset with 4-level relevance annotations, filling a critical resource void. Further, we propose a semi-supervised synthetic data pipeline where two collaboratively trained models generate domain-adaptive short video data with controllable relevance labels. Our method enhances relevance-level diversity by synthesizing samples for underrepresented intermediate relevance labels, resulting in a more balanced and semantically rich training data set. Extensive offline experiments show that the embedding model trained on our synthesized data outperforms those using data generated based on prompting or vanilla supervised fine-tuning(SFT). Moreover, we demonstrate that incorporating more diverse fine-grained relevance levels in training data enhances the model's sensitivity to subtle semantic distinctions, highlighting the value of fine-grained relevance supervision in embedding learning. In the search enhanced recommendation pipeline of Douyin's dual-column scenario, through online A/B testing, the proposed model increased click-through rate(CTR) by 1.45%, raised the proportion of Strong Relevance Ratio (SRR) by 4.9%, and improved the Image User Penetration Rate (IUPR) by 0.1054%.

