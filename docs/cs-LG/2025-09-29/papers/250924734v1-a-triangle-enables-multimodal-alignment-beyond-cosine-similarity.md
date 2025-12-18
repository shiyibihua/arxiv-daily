---
layout: default
title: A TRIANGLE Enables Multimodal Alignment Beyond Cosine Similarity
---

# A TRIANGLE Enables Multimodal Alignment Beyond Cosine Similarity

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24734" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24734v1</a>
  <a href="https://arxiv.org/pdf/2509.24734.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24734v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24734v1', 'A TRIANGLE Enables Multimodal Alignment Beyond Cosine Similarity')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Giordano Cicchetti, Eleonora Grassucci, Danilo Comminiello

**分类**: cs.LG, cs.AI, cs.CV

**发布日期**: 2025-09-29

**备注**: NeurIPS 2025

---

## 💡 一句话要点

**提出TRIANGLE以解决多模态对齐问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `模态对齐` `三角形相似度` `神经网络` `信息检索` `音频分类` `视频理解`

## 📋 核心要点

1. 现有的多模态学习方法在模态对齐方面存在显著不足，导致模型无法有效利用多模态信息。
2. 本文提出TRIANGLE，通过三角形面积相似度在高维空间中计算模态对齐，避免了额外的融合层和成对相似度计算。
3. 实验结果表明，TRIANGLE在多模态任务中表现优异，提升了Recall@1指标，最高可达9个百分点。

## 📝 摘要（中文）

多模态学习在推动人工智能系统发展中扮演着重要角色，通过整合多种模态的信息以构建更全面的表示。然而，现有的最先进模型仍存在严重的局限性，无法有效实现多模态的对齐，导致模型在下游任务中未能充分利用多模态信息。本文提出了TRIANGLE：三模态神经几何学习，采用三角形面积相似度直接在模态嵌入的高维空间中计算，从而改善三种模态的联合对齐。TRIANGLE在替代余弦相似度的对比损失中显著提升了多模态建模的性能，并提供了可解释的对齐理由。通过在视频-文本、音频-文本检索及音频-视频分类等三模态任务中的广泛评估，TRIANGLE在不同数据集上实现了最先进的结果，提升了基于余弦的方法的Recall@1性能，最高可达9个百分点。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态学习方法在模态对齐方面的不足，尤其是在下游任务中未能有效利用所有模态信息的问题。现有方法往往依赖于余弦相似度，无法提供有效的对齐指示，导致某些模态未能充分对齐。

**核心思路**：TRIANGLE的核心思路是通过三角形面积相似度来实现三种模态的联合对齐，直接在模态嵌入的高维空间中计算相似度。这种设计避免了传统方法中常见的额外融合层和成对相似度计算，从而提高了对齐的效率和效果。

**技术框架**：TRIANGLE的整体架构包括模态嵌入生成、三角形相似度计算和对比损失优化三个主要模块。首先，输入数据通过各自的模态嵌入网络生成嵌入向量；然后，计算三角形的面积相似度以评估模态之间的对齐程度；最后，利用对比损失函数优化模型性能。

**关键创新**：TRIANGLE的最重要创新在于其独特的三角形面积相似度计算方法，这与传统的余弦相似度计算方法本质上不同。通过在高维空间中直接计算相似度，TRIANGLE能够更好地捕捉模态之间的关系。

**关键设计**：在关键设计方面，TRIANGLE采用了特定的损失函数来优化模态对齐，确保模型在训练过程中能够有效学习到模态之间的相互关系。此外，网络结构经过精心设计，以支持高维嵌入的计算和相似度评估。具体的参数设置和网络层次结构在实验部分进行了详细描述。

## 📊 实验亮点

实验结果显示，TRIANGLE在视频-文本和音频-文本检索等三模态任务中表现优异，提升了Recall@1指标，最高可达9个百分点，相较于传统的余弦相似度方法，显著提高了模型的性能，展示了其在多模态学习中的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括视频检索、音频分类及多模态信息融合等。通过提高多模态模型的对齐效果，TRIANGLE能够在实际应用中显著提升信息检索和分类的准确性，具有重要的实际价值和广泛的应用前景。未来，TRIANGLE的设计理念也可能被扩展到其他多模态学习任务中，推动相关领域的发展。

## 📄 摘要（原文）

> Multimodal learning plays a pivotal role in advancing artificial intelligence systems by incorporating information from multiple modalities to build a more comprehensive representation. Despite its importance, current state-of-the-art models still suffer from severe limitations that prevent the successful development of a fully multimodal model. Such methods may not provide indicators that all the involved modalities are effectively aligned. As a result, some modalities may not be aligned, undermining the effectiveness of the model in downstream tasks where multiple modalities should provide additional information that the model fails to exploit. In this paper, we present TRIANGLE: TRI-modAl Neural Geometric LEarning, the novel proposed similarity measure that is directly computed in the higher-dimensional space spanned by the modality embeddings. TRIANGLE improves the joint alignment of three modalities via a triangle-area similarity, avoiding additional fusion layers or pairwise similarities. When incorporated in contrastive losses replacing cosine similarity, TRIANGLE significantly boosts the performance of multimodal modeling, while yielding interpretable alignment rationales. Extensive evaluation in three-modal tasks such as video-text and audio-text retrieval or audio-video classification, demonstrates that TRIANGLE achieves state-of-the-art results across different datasets improving the performance of cosine-based methods up to 9 points of Recall@1.

