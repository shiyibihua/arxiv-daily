---
layout: default
title: Dynamic Double Space Tower
---

# Dynamic Double Space Tower

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11394" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11394v1</a>
  <a href="https://arxiv.org/pdf/2506.11394.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11394v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11394v1', 'Dynamic Double Space Tower')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weikai Sun, Shijie Song, Han Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-13

---

## 💡 一句话要点

**提出动态双空间塔以解决视觉问答中的推理不足问题**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉问答` `多模态学习` `空间关系` `推理能力` `动态双向空间塔` `图像理解` `人机交互`

## 📋 核心要点

1. 现有视觉问答方法在复杂推理场景中表现不佳，主要由于跨模态交互不足和空间关系捕捉能力弱。
2. 论文提出了一种动态双向空间塔结构，旨在通过替代注意力机制来增强模型的推理能力和空间关系理解。
3. 实验结果显示，该方法在多模态视觉问答模型July中取得了最先进的结果，仅使用3B参数，尤其在空间关系问答数据集上表现突出。

## 📝 摘要（中文）

视觉问答（VQA）任务需要同时理解图像内容和问题语义。然而，现有方法在处理复杂推理场景时常常面临跨模态交互不足和图像中实体空间关系捕捉不力的问题。为此，我们提出了一种全新的动态双向空间塔结构，旨在替代传统的注意力机制，以增强模型的推理能力和空间关系理解。该结构分为四层，依据人类格式塔视觉原理观察图像，从而为实体间的空间组织提供强大的结构先验。大量实验表明，我们的模块可应用于任何多模态模型，并取得了优异的效果，尤其在空间关系问答数据集上表现出色。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有视觉问答模型在复杂推理场景下的不足，特别是跨模态交互和空间关系捕捉的能力弱。

**核心思路**：提出动态双向空间塔结构，依据人类格式塔视觉原理，增强模型对图像内容的理解和推理能力，避免盲目像素关系搜索。

**技术框架**：整体架构分为四层，分别观察图像的不同方面，形成对实体间空间关系的有效组织。主要模块包括动态空间塔和多模态交互模块。

**关键创新**：动态双向空间塔是本研究的核心创新，与传统注意力机制相比，能够更好地捕捉空间关系，提升推理能力。

**关键设计**：设计中采用了特定的层数和结构，以适应不同的视觉输入，同时优化了损失函数以增强模型的学习效果。

## 📊 实验亮点

实验结果表明，使用动态双向空间塔的多模态视觉问答模型July在空间关系问答数据集上取得了最先进的结果，性能显著优于基线模型，尤其在参数仅为3B的情况下，展示了良好的效率和效果。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、图像理解和人机交互等。通过提升视觉问答模型的推理能力，能够在教育、医疗、安防等多个行业中实现更高效的信息检索和决策支持，未来可能推动相关技术的广泛应用。

## 📄 摘要（原文）

> The Visual Question Answering (VQA) task requires the simultaneous understanding of image content and question semantics. However, existing methods often have difficulty handling complex reasoning scenarios due to insufficient cross-modal interaction and capturing the entity spatial relationships in the image.\cite{huang2023adaptive}\cite{liu2021comparing}\cite{guibas2021adaptive}\cite{zhang2022vsa}We studied a brand-new approach to replace the attention mechanism in order to enhance the reasoning ability of the model and its understanding of spatial relationships.Specifically, we propose a dynamic bidirectional spatial tower, which is divided into four layers to observe the image according to the principle of human gestalt vision. This naturally provides a powerful structural prior for the spatial organization between entities, enabling the model to no longer blindly search for relationships between pixels but make judgments based on more meaningful perceptual units. Change from "seeing images" to "perceiving and organizing image content".A large number of experiments have shown that our module can be used in any other multimodal model and achieve advanced results, demonstrating its potential in spatial relationship processing.Meanwhile, the multimodal visual question-answering model July trained by our method has achieved state-of-the-art results with only 3B parameters, especially on the question-answering dataset of spatial relations.

