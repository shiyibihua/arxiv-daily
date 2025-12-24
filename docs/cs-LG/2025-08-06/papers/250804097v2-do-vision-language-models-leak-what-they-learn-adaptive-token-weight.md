---
layout: default
title: Do Vision-Language Models Leak What They Learn? Adaptive Token-Weighted Model Inversion Attacks
---

# Do Vision-Language Models Leak What They Learn? Adaptive Token-Weighted Model Inversion Attacks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04097" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04097v2</a>
  <a href="https://arxiv.org/pdf/2508.04097.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04097v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04097v2', 'Do Vision-Language Models Leak What They Learn? Adaptive Token-Weighted Model Inversion Attacks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ngoc-Bao Nguyen, Sy-Tuyen Ho, Koh Jun Hao, Ngai-Man Cheung

**分类**: cs.LG

**发布日期**: 2025-08-06 (更新: 2025-12-01)

**备注**: Under review

---

## 💡 一句话要点

**提出自适应令牌加权模型反演攻击以解决视觉语言模型隐私泄露问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `模型反演` `视觉语言模型` `隐私保护` `自适应加权` `深度学习` `数据泄露` `图像重构`

## 📋 核心要点

1. 现有研究主要集中于单模态深度网络，视觉语言模型的隐私泄露问题尚未得到充分探讨。
2. 本文提出了一套针对VLM的模型反演攻击策略，并引入自适应令牌加权机制以提升重构效果。
3. 实验结果显示，VLM在多种数据集上均存在训练数据泄露风险，重构图像的攻击准确率为61.21%。

## 📝 摘要（中文）

模型反演（MI）攻击通过重构训练数据对隐私构成重大风险。尽管以往研究主要集中在单模态深度网络上，但视觉语言模型（VLM）的脆弱性仍未得到充分探讨。本文首次系统研究了VLM的MI攻击，提出了一套基于令牌和序列的反演策略，并引入自适应令牌加权的序列模型反演（SMI-AW），以动态调整每个令牌的损失梯度，聚焦于视觉信息丰富的令牌，从而更有效地指导私密图像的重构。实验表明，VLM对训练数据泄露存在显著脆弱性，重构图像的攻击准确率达到61.21%。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉语言模型（VLM）在模型反演攻击中的隐私泄露问题。现有方法主要针对单模态网络，未能有效评估VLM的脆弱性。

**核心思路**：提出了一种基于令牌的模型反演策略，结合自适应令牌加权机制，动态调整每个令牌的损失梯度，以聚焦于视觉信息丰富的令牌，从而提高重构效果。

**技术框架**：整体框架包括数据预处理、令牌生成、损失计算和图像重构四个主要模块。首先，通过VLM生成令牌，然后计算每个令牌的损失，最后进行图像重构。

**关键创新**：引入自适应令牌加权机制，使得模型能够根据每个令牌的视觉基础动态调整其重要性。这一创新显著提升了重构图像的质量，与传统方法相比，能够更有效地利用视觉信息。

**关键设计**：在损失函数中，采用了基于视觉基础的动态加权策略，确保在优化过程中更加关注那些对图像重构贡献较大的令牌。同时，网络结构采用了适合VLM的生成模型架构，以提高反演效果。

## 📊 实验亮点

实验结果表明，视觉语言模型在多种数据集上均存在显著的训练数据泄露风险，重构图像的攻击准确率达到61.21%。这一结果强调了VLM在实际应用中的隐私风险，尤其是在敏感领域的应用场景中。

## 🎯 应用场景

该研究的潜在应用领域包括医疗、金融等敏感领域，随着视觉语言模型的广泛应用，保护用户隐私变得尤为重要。通过识别和缓解VLM的隐私风险，可以为这些领域提供更安全的技术解决方案，确保用户数据的安全性和隐私性。

## 📄 摘要（原文）

> Model inversion (MI) attacks pose significant privacy risks by reconstructing private training data from trained neural networks. While prior studies have primarily examined unimodal deep networks, the vulnerability of vision-language models (VLMs) remains largely unexplored. In this work, we present the first systematic study of MI attacks on VLMs to understand their susceptibility to leaking private visual training data. Our work makes two main contributions. First, tailored to the token-generative nature of VLMs, we introduce a suite of token-based and sequence-based model inversion strategies, providing a comprehensive analysis of VLMs' vulnerability under different attack formulations. Second, based on the observation that tokens vary in their visual grounding, and hence their gradients differ in informativeness for image reconstruction, we propose Sequence-based Model Inversion with Adaptive Token Weighting (SMI-AW) as a novel MI for VLMs. SMI-AW dynamically reweights each token's loss gradient according to its visual grounding, enabling the optimization to focus on visually informative tokens and more effectively guide the reconstruction of private images. Through extensive experiments and human evaluations on a range of state-of-the-art VLMs across multiple datasets, we show that VLMs are susceptible to training data leakage. Human evaluation of the reconstructed images yields an attack accuracy of 61.21%, underscoring the severity of these privacy risks. Notably, we demonstrate that publicly released VLMs are vulnerable to such attacks. Our study highlights the urgent need for privacy safeguards as VLMs become increasingly deployed in sensitive domains such as healthcare and finance. Additional experiments are provided in Supp.

