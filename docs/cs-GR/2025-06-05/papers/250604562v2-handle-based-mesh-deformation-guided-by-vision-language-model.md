---
layout: default
title: Handle-based Mesh Deformation Guided By Vision Language Model
---

# Handle-based Mesh Deformation Guided By Vision Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04562" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04562v2</a>
  <a href="https://arxiv.org/pdf/2506.04562.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04562v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04562v2', 'Handle-based Mesh Deformation Guided By Vision Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xingpeng Sun, Shiyang Jia, Zherong Pan, Kui Wu, Aniket Bera

**分类**: cs.GR, cs.CV

**发布日期**: 2025-06-05 (更新: 2025-08-20)

**备注**: 19 pages

---

## 💡 一句话要点

**提出基于视觉语言模型的无训练手柄网格变形方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `网格变形` `视觉语言模型` `无训练方法` `3D内容操作` `用户意图对齐` `多视角投票` `自动化设计`

## 📋 核心要点

1. 现有网格变形方法输出质量低，需大量手动调优，且依赖数据密集型训练。
2. 提出一种无训练的手柄网格变形方法，利用视觉语言模型进行提示工程以实现自动化操作。
3. 实验结果显示，该方法在用户意图对齐和低失真方面优于现有基线，表现出色。

## 📝 摘要（中文）

网格变形是3D内容操作中的基本工具。尽管已有大量研究，现有方法常常输出质量低、需要大量手动调优或依赖数据密集型训练。为了解决这些问题，本文提出了一种无训练的手柄网格变形方法。核心思想是利用视觉语言模型（VLM）通过提示工程来解释和操作基于手柄的界面。我们首先应用锥形奇点检测来识别一组稀疏的潜在手柄。然后，VLM被提示选择与用户指令最一致的可变形子部分和手柄。最后，我们在屏幕空间查询所选手柄的期望变形位置。通过多视角投票方案减少VLM预测中的不确定性。实验结果表明，该方法在用户意图对齐和低失真方面表现优异。

## 🔬 方法详解

**问题定义**：本文旨在解决现有网格变形方法在输出质量、手动调优需求和数据依赖性方面的不足。现有方法常常无法满足用户的具体需求，导致变形效果不理想。

**核心思路**：提出了一种基于视觉语言模型的手柄网格变形方法，通过提示工程使得用户可以更直观地操控网格变形，避免了传统方法的训练需求。

**技术框架**：整体流程包括锥形奇点检测以识别潜在手柄，利用视觉语言模型选择可变形子部分和手柄，并通过多视角投票方案来确定最终的变形位置。

**关键创新**：最重要的创新在于引入视觉语言模型进行无训练的网格变形，显著提高了用户交互的灵活性和变形的准确性。与传统方法相比，减少了对训练数据的依赖。

**关键设计**：在手柄识别和选择过程中，采用了锥形奇点检测算法，VLM的提示设计也经过精心调整，以确保其能够准确理解用户意图。多视角投票方案则有效降低了预测的不确定性。

## 📊 实验亮点

实验结果表明，提出的方法在CLIP和GPTEval3D评分上显著优于现有基线，用户意图对齐度更高，同时引入的膜能量量化显示出低失真特性，整体变形效果更佳。

## 🎯 应用场景

该研究的潜在应用领域包括游戏开发、动画制作和虚拟现实等3D内容创作场景。通过提供一种高效、自动化的网格变形工具，能够显著提升创作者的工作效率和创作质量，未来可能对3D设计行业产生深远影响。

## 📄 摘要（原文）

> Mesh deformation is a fundamental tool in 3D content manipulation. Despite extensive prior research, existing approaches often suffer from low output quality, require significant manual tuning, or depend on data-intensive training. To address these limitations, we introduce a training-free, handle-based mesh deformation method. % Our core idea is to leverage a Vision-Language Model (VLM) to interpret and manipulate a handle-based interface through prompt engineering. We begin by applying cone singularity detection to identify a sparse set of potential handles. The VLM is then prompted to select both the deformable sub-parts of the mesh and the handles that best align with user instructions. Subsequently, we query the desired deformed positions of the selected handles in screen space. To reduce uncertainty inherent in VLM predictions, we aggregate the results from multiple camera views using a novel multi-view voting scheme. % Across a suite of benchmarks, our method produces deformations that align more closely with user intent, as measured by CLIP and GPTEval3D scores, while introducing low distortion -- quantified via membrane energy. In summary, our approach is training-free, highly automated, and consistently delivers high-quality mesh deformations.

