---
layout: default
title: Hyperspectral Adapter for Semantic Segmentation with Vision Foundation Models
---

# Hyperspectral Adapter for Semantic Segmentation with Vision Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20107" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20107v2</a>
  <a href="https://arxiv.org/pdf/2509.20107.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20107v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20107v2', 'Hyperspectral Adapter for Semantic Segmentation with Vision Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Juana Valeria Hurtado, Rohit Mohan, Abhinav Valada

**分类**: cs.CV, cs.AI, cs.LG, cs.RO

**发布日期**: 2025-09-24 (更新: 2025-09-25)

---

## 💡 一句话要点

**提出基于视觉基础模型的超光谱适配器，提升语义分割性能**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `高光谱图像` `语义分割` `视觉基础模型` `Transformer` `自动驾驶`

## 📋 核心要点

1. 现有高光谱语义分割方法依赖为RGB图像设计的架构，无法充分利用高光谱数据的丰富信息。
2. 提出一种高光谱适配器，利用预训练的视觉基础模型，结合光谱Transformer和空间先验模块提取特征。
3. 实验表明，该方法在自动驾驶数据集上实现了最先进的语义分割性能，优于现有方法。

## 📝 摘要（中文）

高光谱成像(HSI)捕获空间信息以及跨多个窄波段的密集光谱测量。这种丰富的光谱内容有潜力促进鲁棒的机器人感知，尤其是在具有复杂材料组成、变化的光照或其他视觉挑战性条件的环境中。然而，当前的HSI语义分割方法由于依赖于针对RGB输入优化的架构和学习框架而表现不佳。在这项工作中，我们提出了一种新的高光谱适配器，它利用预训练的视觉基础模型来有效地从高光谱数据中学习。我们的架构包含一个光谱Transformer和一个频谱感知空间先验模块，以提取丰富的空间-光谱特征。此外，我们引入了一个模态感知交互块，通过专用的提取和注入机制，促进高光谱表示和冻结的视觉Transformer特征的有效集成。在三个基准自动驾驶数据集上的广泛评估表明，我们的架构实现了最先进的语义分割性能，同时直接使用HSI输入，优于基于视觉和高光谱的分割方法。代码已开源。

## 🔬 方法详解

**问题定义**：论文旨在解决高光谱图像（HSI）的语义分割问题。现有方法主要存在两个痛点：一是直接将RGB图像的分割模型应用于HSI数据，忽略了HSI数据的光谱特性；二是缺乏利用大规模预训练视觉模型的能力，导致模型泛化能力不足。

**核心思路**：论文的核心思路是设计一个高光谱适配器，将预训练的视觉基础模型与高光谱数据相结合。通过专门设计的模块，提取并融合高光谱数据的空间和光谱特征，同时利用预训练模型的强大表征能力，从而提升语义分割的性能。

**技术框架**：整体架构包含以下几个主要模块：1) **光谱Transformer**：用于提取高光谱数据的光谱特征。2) **频谱感知空间先验模块**：用于提取空间信息，并结合光谱信息。3) **模态感知交互块**：用于融合高光谱特征和预训练视觉Transformer的特征。整个流程是先分别提取高光谱和视觉特征，然后通过交互块进行融合，最后进行语义分割。

**关键创新**：最重要的技术创新点在于模态感知交互块的设计。该模块通过专用的提取和注入机制，能够有效地将高光谱数据的特征融入到预训练的视觉Transformer中，避免了简单拼接或加权融合导致的信息损失。这种设计使得模型能够更好地利用高光谱数据的特性，同时保持预训练模型的泛化能力。

**关键设计**：光谱Transformer采用标准的Transformer结构，但输入是高光谱数据的光谱向量。频谱感知空间先验模块通过卷积操作提取空间特征，并利用注意力机制将空间特征与光谱特征进行融合。模态感知交互块包含提取模块和注入模块，分别用于提取高光谱特征和将高光谱特征注入到视觉Transformer的中间层。损失函数采用标准的交叉熵损失函数。

## 📊 实验亮点

该方法在三个自动驾驶数据集上进行了评估，实验结果表明，该方法在语义分割任务上取得了state-of-the-art的性能。与现有的基于视觉和高光谱的分割方法相比，该方法在mIoU等指标上均有显著提升，证明了该方法的有效性。

## 🎯 应用场景

该研究成果可应用于自动驾驶、遥感图像分析、农业监测、环境监测等领域。通过高光谱图像的语义分割，可以更准确地识别道路场景中的物体、农作物的种类和健康状况、以及环境污染的程度，为相关领域的决策提供更可靠的依据。未来，该方法有望进一步扩展到其他高光谱图像处理任务中。

## 📄 摘要（原文）

> Hyperspectral imaging (HSI) captures spatial information along with dense spectral measurements across numerous narrow wavelength bands. This rich spectral content has the potential to facilitate robust robotic perception, particularly in environments with complex material compositions, varying illumination, or other visually challenging conditions. However, current HSI semantic segmentation methods underperform due to their reliance on architectures and learning frameworks optimized for RGB inputs. In this work, we propose a novel hyperspectral adapter that leverages pretrained vision foundation models to effectively learn from hyperspectral data. Our architecture incorporates a spectral transformer and a spectrum-aware spatial prior module to extract rich spatial-spectral features. Additionally, we introduce a modality-aware interaction block that facilitates effective integration of hyperspectral representations and frozen vision Transformer features through dedicated extraction and injection mechanisms. Extensive evaluations on three benchmark autonomous driving datasets demonstrate that our architecture achieves state-of-the-art semantic segmentation performance while directly using HSI inputs, outperforming both vision-based and hyperspectral segmentation methods. We make the code available at https://hsi-adapter.cs.uni-freiburg.de.

