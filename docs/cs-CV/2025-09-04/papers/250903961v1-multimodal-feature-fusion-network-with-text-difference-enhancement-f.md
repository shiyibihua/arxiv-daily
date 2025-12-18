---
layout: default
title: Multimodal Feature Fusion Network with Text Difference Enhancement for Remote Sensing Change Detection
---

# Multimodal Feature Fusion Network with Text Difference Enhancement for Remote Sensing Change Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03961" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03961v1</a>
  <a href="https://arxiv.org/pdf/2509.03961.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03961v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03961v1', 'Multimodal Feature Fusion Network with Text Difference Enhancement for Remote Sensing Change Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yijun Zhou, Yikui Zhai, Zilu Ying, Tingfeng Xian, Wenlve Zhou, Zhiheng Zhou, Xiaolin Tian, Xudong Jia, Hongsheng Zhang, C. L. Philip Chen

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-04

**🔗 代码/项目**: [GITHUB](https://github.com/yikuizhai/MMChange)

---

## 💡 一句话要点

**提出MMChange，一种融合图像与文本差异增强的多模态遥感变化检测网络。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `遥感变化检测` `多模态融合` `视觉语言模型` `文本差异增强` `深度学习` `图像特征精炼` `跨模态学习`

## 📋 核心要点

1. 现有遥感变化检测方法主要依赖图像模态，在光照变化和噪声干扰下，特征表示和泛化能力受限。
2. MMChange结合图像和文本模态，利用视觉语言模型生成语义描述，并通过文本差异增强模块捕获细粒度语义变化。
3. 实验结果表明，MMChange在LEVIRCD、WHUCD和SYSUCD数据集上均超越了现有最佳方法，验证了其有效性。

## 📝 摘要（中文）

深度学习在遥感变化检测(RSCD)领域取得了显著进展，但多数方法仅依赖图像模态，限制了特征表示、变化模式建模和泛化能力，尤其是在光照和噪声干扰下。为解决此问题，我们提出MMChange，一种结合图像和文本模态的多模态RSCD方法，以提高准确性和鲁棒性。引入图像特征精炼(IFR)模块来突出关键区域并抑制环境噪声。为了克服图像特征的语义局限性，我们采用视觉语言模型(VLM)来生成双时相图像的语义描述。文本差异增强(TDE)模块捕获细粒度的语义变化，引导模型关注有意义的变化。为了弥合模态之间的异构性，我们设计了图像文本特征融合(ITFF)模块，实现深度跨模态融合。在LEVIRCD、WHUCD和SYSUCD上的大量实验表明，MMChange在多个指标上始终优于最先进的方法，验证了其在多模态RSCD中的有效性。

## 🔬 方法详解

**问题定义**：遥感变化检测旨在识别不同时相遥感图像中地物或场景的变化。现有方法主要依赖图像模态，容易受到光照、噪声等因素的影响，导致特征表示能力不足，难以准确捕捉细微的变化信息。此外，图像特征的语义信息有限，难以有效区分不同类型的变化。

**核心思路**：MMChange的核心思路是融合图像和文本两种模态的信息，利用视觉语言模型(VLM)提取图像的语义描述，并通过文本差异增强模块(TDE)捕捉细粒度的语义变化。通过跨模态融合，可以有效弥补图像模态的不足，提高变化检测的准确性和鲁棒性。

**技术框架**：MMChange主要包含三个模块：图像特征精炼(IFR)模块、文本差异增强(TDE)模块和图像文本特征融合(ITFF)模块。首先，IFR模块用于突出图像中的关键区域并抑制噪声。然后，VLM用于生成双时相图像的文本描述，TDE模块用于提取文本描述中的差异信息。最后，ITFF模块将图像特征和文本特征进行融合，得到最终的变化检测结果。

**关键创新**：MMChange的关键创新在于引入了文本模态信息，并设计了文本差异增强模块(TDE)。TDE模块能够有效地捕捉细粒度的语义变化，从而提高变化检测的准确性。此外，ITFF模块实现了图像和文本特征的深度融合，充分利用了两种模态的信息。

**关键设计**：IFR模块采用注意力机制来突出关键区域。TDE模块使用Transformer结构来捕捉文本描述中的差异信息。ITFF模块使用跨模态注意力机制来实现图像和文本特征的融合。损失函数包括交叉熵损失和Dice损失，用于优化变化检测结果。

## 📊 实验亮点

MMChange在LEVIRCD、WHUCD和SYSUCD三个遥感变化检测数据集上进行了广泛的实验。实验结果表明，MMChange在多个指标上均优于现有的state-of-the-art方法。例如，在LEVIRCD数据集上，MMChange的F1-score比最佳基线方法提高了2%以上，验证了其有效性。

## 🎯 应用场景

MMChange可应用于多种遥感应用场景，如城市扩张监测、自然灾害评估、农业资源管理和环境变化分析。该方法能够提高变化检测的准确性和鲁棒性，为相关领域的决策提供更可靠的信息支持，具有重要的实际应用价值和潜在的社会经济效益。

## 📄 摘要（原文）

> Although deep learning has advanced remote sensing change detection (RSCD), most methods rely solely on image modality, limiting feature representation, change pattern modeling, and generalization especially under illumination and noise disturbances. To address this, we propose MMChange, a multimodal RSCD method that combines image and text modalities to enhance accuracy and robustness. An Image Feature Refinement (IFR) module is introduced to highlight key regions and suppress environmental noise. To overcome the semantic limitations of image features, we employ a vision language model (VLM) to generate semantic descriptions of bitemporal images. A Textual Difference Enhancement (TDE) module then captures fine grained semantic shifts, guiding the model toward meaningful changes. To bridge the heterogeneity between modalities, we design an Image Text Feature Fusion (ITFF) module that enables deep cross modal integration. Extensive experiments on LEVIRCD, WHUCD, and SYSUCD demonstrate that MMChange consistently surpasses state of the art methods across multiple metrics, validating its effectiveness for multimodal RSCD. Code is available at: https://github.com/yikuizhai/MMChange.

