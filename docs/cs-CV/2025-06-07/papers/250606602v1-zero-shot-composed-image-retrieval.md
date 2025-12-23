---
layout: default
title: Zero Shot Composed Image Retrieval
---

# Zero Shot Composed Image Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06602" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06602v1</a>
  <a href="https://arxiv.org/pdf/2506.06602.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06602v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06602v1', 'Zero Shot Composed Image Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Santhosh Kakarla, Gautama Shastry Bulusu Venkata

**分类**: cs.CV

**发布日期**: 2025-06-07

**备注**: 8 pages, 3 figures

---

## 💡 一句话要点

**提出基于BLIP-2的零-shot复合图像检索方法以提升检索性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `复合图像检索` `零-shot学习` `多模态融合` `BLIP-2` `Q-Former` `特征融合` `检索性能提升`

## 📋 核心要点

1. 现有的零-shot复合图像检索方法在FashionIQ基准上表现不佳，仅达到20-25%的Recall@10，存在显著的性能瓶颈。
2. 本文提出通过微调BLIP-2与Q-Former的结合，进行视觉和文本特征的有效融合，从而提升检索性能。
3. 实验结果显示，经过改进后，Recall@10在不同类别上显著提升，平均Recall@50也有显著提高，验证了方法的有效性。

## 📝 摘要（中文）

复合图像检索（CIR）允许用户通过对参考图像进行细粒度文本编辑来定位目标图像。零-shot CIR在FashionIQ基准上仅达到20-25%的Recall@10。本文通过使用轻量级的Q-Former对BLIP-2进行微调，将视觉和文本特征融合为单一嵌入，Recall@10提升至45.6%（衬衫）、40.1%（裙子）和50.4%（T恤），平均Recall@50提升至67.6%。此外，本文还探讨了Retrieval-DPO方法，但由于缺乏图像-文本联合融合等问题，其性能远低于零-shot和提示调优基线。

## 🔬 方法详解

**问题定义**：本文旨在解决零-shot复合图像检索中现有方法性能不足的问题，特别是在FashionIQ基准上的低Recall@10表现。现有方法主要依赖于独立的视觉和文本编码器，缺乏有效的特征融合。

**核心思路**：论文提出通过微调BLIP-2并引入轻量级的Q-Former，将视觉和文本特征融合为单一嵌入，以提高检索的准确性和效率。这样的设计旨在克服现有方法的局限性，实现更好的多模态特征整合。

**技术框架**：整体架构包括两个主要模块：首先是BLIP-2的微调，随后是Q-Former的引入以实现视觉和文本特征的融合。整个流程从输入图像和文本开始，通过编码器生成嵌入，最后进行检索。

**关键创新**：最重要的创新在于引入Q-Former进行图像和文本的联合嵌入，解决了传统方法中图像和文本特征分离的问题，从而提升了检索性能。

**关键设计**：在参数设置上，本文对BLIP-2进行了细致的微调，并设计了适应于特定任务的损失函数。此外，Retrieval-DPO方法的实验中，尽管进行了多次调优，但由于缺乏有效的负样本和图像-文本融合，导致其性能未能达到预期。

## 📊 实验亮点

实验结果显示，经过微调的BLIP-2与Q-Former的结合，使得Recall@10在衬衫、裙子和T恤类别上分别达到了45.6%、40.1%和50.4%，平均Recall@50提升至67.6%。相比于传统的零-shot和提示调优基线，性能有显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括电子商务、社交媒体和数字内容管理等场景，用户可以通过简单的文本描述快速找到所需的图像，提升用户体验。未来，该技术有望在多模态检索、智能推荐系统等领域发挥更大作用。

## 📄 摘要（原文）

> Composed image retrieval (CIR) allows a user to locate a target image by applying a fine-grained textual edit (e.g., ``turn the dress blue'' or ``remove stripes'') to a reference image. Zero-shot CIR, which embeds the image and the text with separate pretrained vision-language encoders, reaches only 20-25\% Recall@10 on the FashionIQ benchmark. We improve this by fine-tuning BLIP-2 with a lightweight Q-Former that fuses visual and textual features into a single embedding, raising Recall@10 to 45.6\% (shirt), 40.1\% (dress), and 50.4\% (top-tee) and increasing the average Recall@50 to 67.6\%. We also examine Retrieval-DPO, which fine-tunes CLIP's text encoder with a Direct Preference Optimization loss applied to FAISS-mined hard negatives. Despite extensive tuning of the scaling factor, index, and sampling strategy, Retrieval-DPO attains only 0.02\% Recall@10 -- far below zero-shot and prompt-tuned baselines -- because it (i) lacks joint image-text fusion, (ii) uses a margin objective misaligned with top-$K$ metrics, (iii) relies on low-quality negatives, and (iv) keeps the vision and Transformer layers frozen. Our results show that effective preference-based CIR requires genuine multimodal fusion, ranking-aware objectives, and carefully curated negatives.

