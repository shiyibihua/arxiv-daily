---
layout: default
title: Dual Enhancement on 3D Vision-Language Perception for Monocular 3D Visual Grounding
---

# Dual Enhancement on 3D Vision-Language Perception for Monocular 3D Visual Grounding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19165" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19165v1</a>
  <a href="https://arxiv.org/pdf/2508.19165.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19165v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19165v1', 'Dual Enhancement on 3D Vision-Language Perception for Monocular 3D Visual Grounding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuzhen Li, Min Liu, Yuan Bian, Xueping Wang, Zhaoyang Li, Gen Li, Yaonan Wang

**分类**: cs.CV

**发布日期**: 2025-08-26

**备注**: 10 pages

---

## 💡 一句话要点

**提出双重增强方法以解决单目3D视觉定位问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `单目3D视觉` `视觉定位` `多模态学习` `文本增强` `几何感知`

## 📋 核心要点

1. 现有方法在处理文本描述中的数值单位时存在显著不足，导致3D感知能力弱。
2. 论文提出3D文本增强和文本引导几何增强两种方法，以改善文本嵌入对几何信息的理解。
3. 实验结果显示，所提方法在Mono3DRefer数据集上取得了新的最优结果，准确率提升显著。

## 📝 摘要（中文）

单目3D视觉定位是一项新兴任务，旨在利用带有几何信息的文本描述在RGB图像中定位3D物体。尽管文本中包含几何细节，但我们发现文本嵌入对数值大小敏感，却忽视了测量单位的影响。为此，本文提出了两种有效的方法来增强模型对文本嵌入和几何特征的3D感知。首先，提出了3D文本增强（3DTE）方法，通过增加文本查询中距离描述符的多样性来改善单位之间的映射关系理解。其次，提出了文本引导几何增强（TGE）模块，将基本文本特征投影到几何一致的空间中，从而进一步增强3D文本信息。实验结果表明，该方法在Mono3DRefer数据集上显著提升了性能，尤其在“远”场景下提高了11.94%的准确率。

## 🔬 方法详解

**问题定义**：本文旨在解决单目3D视觉定位中，文本描述对数值单位敏感而忽视其影响的问题。现有方法在处理不同单位时，容易导致3D感知的误导。

**核心思路**：通过引入3D文本增强（3DTE）和文本引导几何增强（TGE）模块，增强模型对文本嵌入和几何特征的理解，从而提高3D定位的准确性。

**技术框架**：整体架构包括两个主要模块：3D文本增强模块用于丰富文本描述的多样性，文本引导几何增强模块用于将文本特征投影到几何一致的空间中。

**关键创新**：最重要的创新在于提出了3D文本增强和文本引导几何增强两个模块，显著改善了文本特征对几何信息的引导能力，与现有方法相比，增强了3D理解能力。

**关键设计**：在3D文本增强中，通过多样化距离描述符来增强单位映射关系；在文本引导几何增强中，设计了特征投影机制，以确保文本特征与几何特征的一致性。具体的损失函数和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，所提出的方法在Mono3DRefer数据集上实现了新的最优结果，特别是在“远”场景下，准确率提升了11.94%。与之前的方法相比，性能显著提高，验证了所提方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人视觉、自动驾驶、增强现实等，能够提升计算机对环境的理解能力，进而改善人机交互和自动化决策的效果。未来，随着技术的进步，该方法可能会在更多实际场景中得到应用，推动相关领域的发展。

## 📄 摘要（原文）

> Monocular 3D visual grounding is a novel task that aims to locate 3D objects in RGB images using text descriptions with explicit geometry information. Despite the inclusion of geometry details in the text, we observe that the text embeddings are sensitive to the magnitude of numerical values but largely ignore the associated measurement units. For example, simply equidistant mapping the length with unit "meter" to "decimeters" or "centimeters" leads to severe performance degradation, even though the physical length remains equivalent. This observation signifies the weak 3D comprehension of pre-trained language model, which generates misguiding text features to hinder 3D perception. Therefore, we propose to enhance the 3D perception of model on text embeddings and geometry features with two simple and effective methods. Firstly, we introduce a pre-processing method named 3D-text Enhancement (3DTE), which enhances the comprehension of mapping relationships between different units by augmenting the diversity of distance descriptors in text queries. Next, we propose a Text-Guided Geometry Enhancement (TGE) module to further enhance the 3D-text information by projecting the basic text features into geometrically consistent space. These 3D-enhanced text features are then leveraged to precisely guide the attention of geometry features. We evaluate the proposed method through extensive comparisons and ablation studies on the Mono3DRefer dataset. Experimental results demonstrate substantial improvements over previous methods, achieving new state-of-the-art results with a notable accuracy gain of 11.94\% in the "Far" scenario. Our code will be made publicly available.

