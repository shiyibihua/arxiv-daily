---
layout: default
title: "Holi-DETR: Holistic Fashion Item Detection Leveraging Contextual Information"
---

# Holi-DETR: Holistic Fashion Item Detection Leveraging Contextual Information

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23221" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23221v1</a>
  <a href="https://arxiv.org/pdf/2512.23221.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23221v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23221v1', 'Holi-DETR: Holistic Fashion Item Detection Leveraging Contextual Information')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Youngchae Kwon, Jinyoung Choi, Injung Kim

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-29

**备注**: 20 pages, 6 figures

---

## 💡 一句话要点

**提出Holi-DETR，利用上下文信息进行整体时尚单品检测，提升检测精度。**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `时尚单品检测` `上下文信息` `Detection Transformer` `目标检测` `服装搭配`

## 📋 核心要点

1. 时尚单品检测面临外观多样性和类别相似性挑战，传统方法忽略了单品间的上下文关系。
2. Holi-DETR利用单品共现关系、相对位置大小和与人体关键点关系三种上下文信息，实现整体检测。
3. 实验结果表明，Holi-DETR在平均精度上优于DETR和Co-DETR，分别提升了3.6和1.1个百分点。

## 📝 摘要（中文）

时尚单品检测面临着时尚单品外观高度多样性和子类别之间相似性带来的挑战。为了解决这个问题，我们提出了一种新颖的整体检测Transformer（Holi-DETR），通过利用上下文信息来整体地检测服装图像中的时尚单品。时尚单品通常具有有意义的关系，因为它们被组合起来以创建特定的风格。与独立检测每个单品的传统检测器不同，Holi-DETR通过利用三种不同的上下文信息来检测多个单品，同时减少歧义：（1）时尚单品之间的共现关系，（2）基于单品间空间排列的相对位置和大小，以及（3）单品与人体关键点之间的空间关系。实验表明，所提出的方法在平均精度（AP）方面分别将原始DETR和最近开发的Co-DETR的性能提高了3.6个百分点（pp）和1.1个百分点（pp）。

## 🔬 方法详解

**问题定义**：论文旨在解决时尚单品检测中由于单品外观多样性和子类别相似性导致的歧义性问题。现有方法通常独立检测每个单品，忽略了单品之间的上下文关系，导致检测精度不高。

**核心思路**：论文的核心思路是利用时尚单品之间的上下文信息来减少检测歧义。具体来说，论文考虑了三种类型的上下文信息：单品共现关系、单品间的相对位置和大小关系，以及单品与人体关键点之间的空间关系。通过整合这些上下文信息，模型可以更准确地识别和定位时尚单品。

**技术框架**：Holi-DETR基于Detection Transformer (DETR) 架构。整体流程包括：首先，提取图像特征；然后，利用Transformer编码器-解码器结构进行目标检测；最后，将三种上下文信息融入到DETR中，以提高检测精度。具体来说，论文设计了一个模块来显式地建模单品共现概率，并利用单品间的空间关系和单品与人体关键点之间的关系来约束检测结果。

**关键创新**：论文的关键创新在于将三种异构的上下文信息（单品共现关系、单品间的相对位置和大小关系，以及单品与人体关键点之间的空间关系）有效地整合到DETR框架中。这种整合方式使得模型能够更好地理解图像中的时尚搭配，从而提高检测精度。与现有方法相比，Holi-DETR不再孤立地检测每个单品，而是从整体上考虑单品之间的关系。

**关键设计**：论文在DETR的基础上，引入了三个关键的设计：1) 共现概率建模模块，用于学习单品之间的共现关系；2) 相对位置和大小编码模块，用于编码单品之间的空间关系；3) 人体关键点对齐模块，用于对齐单品与人体关键点之间的空间关系。损失函数方面，除了DETR原有的损失函数外，可能还引入了额外的损失函数来约束上下文信息的学习。具体的网络结构细节和参数设置在论文中应该有更详细的描述（未知）。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23221v1/Fig1_arxiv.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23221v1/Fig2_arxiv.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23221v1/Fig3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Holi-DETR在时尚单品检测任务上取得了显著的性能提升。与原始DETR相比，Holi-DETR的平均精度（AP）提高了3.6个百分点。与最近提出的Co-DETR相比，Holi-DETR的平均精度也提高了1.1个百分点。这些结果表明，利用上下文信息可以有效地提高时尚单品检测的精度。

## 🎯 应用场景

该研究成果可应用于智能穿搭推荐、电商平台服装检索、虚拟试衣等领域。通过准确检测时尚单品，可以为用户提供个性化的搭配建议，提高购物体验。未来，该技术还可扩展到其他商品检测领域，例如家居用品、电子产品等。

## 📄 摘要（原文）

> Fashion item detection is challenging due to the ambiguities introduced by the highly diverse appearances of fashion items and the similarities among item subcategories. To address this challenge, we propose a novel Holistic Detection Transformer (Holi-DETR) that detects fashion items in outfit images holistically, by leveraging contextual information. Fashion items often have meaningful relationships as they are combined to create specific styles. Unlike conventional detectors that detect each item independently, Holi-DETR detects multiple items while reducing ambiguities by leveraging three distinct types of contextual information: (1) the co-occurrence relationship between fashion items, (2) the relative position and size based on inter-item spatial arrangements, and (3) the spatial relationships between items and human body key-points. %Holi-DETR explicitly incorporates three types of contextual information: (1) the co-occurrence probability between fashion items, (2) the relative position and size based on inter-item spatial arrangements, and (3) the spatial relationships between items and human body key-points. To this end, we propose a novel architecture that integrates these three types of heterogeneous contextual information into the Detection Transformer (DETR) and its subsequent models. In experiments, the proposed methods improved the performance of the vanilla DETR and the more recently developed Co-DETR by 3.6 percent points (pp) and 1.1 pp, respectively, in terms of average precision (AP).

