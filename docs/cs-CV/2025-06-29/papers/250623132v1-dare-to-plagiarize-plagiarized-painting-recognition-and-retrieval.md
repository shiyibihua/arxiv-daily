---
layout: default
title: Dare to Plagiarize? Plagiarized Painting Recognition and Retrieval
---

# Dare to Plagiarize? Plagiarized Painting Recognition and Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23132" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23132v1</a>
  <a href="https://arxiv.org/pdf/2506.23132.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23132v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23132v1', 'Dare to Plagiarize? Plagiarized Painting Recognition and Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sophie Zhou, Shu Kong

**分类**: cs.CV

**发布日期**: 2025-06-29

**备注**: to appear at AVSS'25

---

## 💡 一句话要点

**提出艺术作品抄袭检测方法以保护版权**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `艺术抄袭检测` `知识产权保护` `生成性AI` `DINOv2` `度量学习` `图像检索` `视觉相似性` `法医分析`

## 📋 核心要点

1. 艺术抄袭检测在现有方法中面临高识别准确率与低检索精度之间的矛盾。
2. 本文提出通过微调DINOv2模型，结合度量学习损失来提高抄袭作品的检索质量。
3. 实验结果显示，微调模型的平均精度提高了12%，但识别准确率略有下降，达到92.7%。

## 📝 摘要（中文）

艺术抄袭检测在保护艺术家版权和知识产权方面至关重要，但在法医分析中仍然是一个具有挑战性的问题。本文旨在识别抄袭的绘画作品，并通过检索视觉上相似的真实艺术作品来解释检测到的抄袭行为。为支持本研究，我们构建了一个数据集，通过收集绘画照片并使用生成性AI合成特定艺术家风格的抄袭版本。我们首先使用视觉基础模型DINOv2的现成特征建立基线方法，以检索数据库中最相似的图像，并基于相似性阈值进行抄袭分类。尽管这一非学习方法的识别准确率高达97.2%，但检索精度较低，平均精度为29.0%。为提高检索质量，我们通过使用数据库中采样的正负样本对对DINOv2进行微调，微调后的模型在基线之上提高了12%的平均精度，尽管识别准确率意外下降至92.7%。最后，我们进行了深入讨论，并概述了未来研究的方向。

## 🔬 方法详解

**问题定义**：本文解决艺术作品抄袭检测问题，现有方法在识别准确率与检索精度之间存在矛盾，导致实际应用效果不佳。

**核心思路**：通过构建一个包含真实与合成抄袭作品的数据集，利用DINOv2模型的特征进行图像检索，并通过微调提升检索性能。

**技术框架**：整体流程包括数据集构建、基线模型建立、特征提取、相似性计算和模型微调五个主要模块。

**关键创新**：在于通过度量学习损失对DINOv2进行微调，显著提升了检索精度，这是与现有方法的本质区别。

**关键设计**：采用正负样本对进行微调，设置相似性阈值进行抄袭分类，确保模型在检索与识别之间的平衡。实验中，基线模型的平均精度为29.0%，微调后提升至41.0%。

## 📊 实验亮点

实验结果表明，基线模型的识别准确率为97.2%，但检索精度仅为29.0%。经过微调后，模型的平均精度提高了12%，达到41.0%，尽管识别准确率下降至92.7%。这一结果突显了模型在检索性能上的显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括艺术品市场、版权保护机构以及法医艺术分析等。通过提高抄袭检测的准确性和效率，可以有效保护艺术家的知识产权，促进艺术创作的健康发展。未来，该方法还可扩展至其他领域，如设计、文学等的抄袭检测。

## 📄 摘要（原文）

> Art plagiarism detection plays a crucial role in protecting artists' copyrights and intellectual property, yet it remains a challenging problem in forensic analysis. In this paper, we address the task of recognizing plagiarized paintings and explaining the detected plagarisms by retrieving visually similar authentic artworks. To support this study, we construct a dataset by collecting painting photos and synthesizing plagiarized versions using generative AI, tailored to specific artists' styles. We first establish a baseline approach using off-the-shelf features from the visual foundation model DINOv2 to retrieve the most similar images in the database and classify plagiarism based on a similarity threshold. Surprisingly, this non-learned method achieves a high recognition accuracy of 97.2\% but suffers from low retrieval precision 29.0\% average precision (AP). To improve retrieval quality, we finetune DINOv2 with a metric learning loss using positive and negative sample pairs sampled in the database. The finetuned model greatly improves retrieval performance by 12\% AP over the baseline, though it unexpectedly results in a lower recognition accuracy (92.7\%). We conclude with insightful discussions and outline directions for future research.

