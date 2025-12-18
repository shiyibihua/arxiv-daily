---
layout: default
title: Open-vocabulary object 6D pose estimation
---

# Open-vocabulary object 6D pose estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.00690" class="toolbar-btn" target="_blank">📄 arXiv: 2312.00690v4</a>
  <a href="https://arxiv.org/pdf/2312.00690.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.00690v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.00690v4', 'Open-vocabulary object 6D pose estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jaime Corsetti, Davide Boscaini, Changjae Oh, Andrea Cavallaro, Fabio Poiesi

**分类**: cs.CV

**发布日期**: 2023-12-01 (更新: 2024-06-25)

**备注**: Camera ready version (CVPR 2024, poster highlight). New Oryon version: arXiv:2406.16384

**🔗 代码/项目**: [PROJECT_PAGE](https://jcorsetti.github.io/oryon)

---

## 💡 一句话要点

**提出开放词汇对象6D姿态估计以解决传统方法的局限性**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `开放词汇` `对象姿态估计` `视觉-语言模型` `深度学习` `图像分割` `机器人视觉` `增强现实`

## 📋 核心要点

1. 现有的6D姿态估计方法通常依赖于对象模型，限制了其在开放词汇场景中的应用。
2. 本研究提出了一种新方法，利用视觉-语言模型通过文本提示来分割对象并估计其姿态。
3. 实验结果显示，该方法在REAL275和Toyota-Light数据集上表现优异，超越了传统手工方法和深度学习基线。

## 📝 摘要（中文）

我们引入了开放词汇对象6D姿态估计的新设置，其中使用文本提示来指定感兴趣的对象。与现有方法相比，在我们的设置中，(i) 感兴趣的对象仅通过文本提示指定，(ii) 推理时不需要对象模型（如CAD或视频序列），(iii) 对象从不同场景的两个RGBD视角进行成像。为在此设置中操作，我们提出了一种新方法，利用视觉-语言模型从场景中分割感兴趣的对象并估计其相对6D姿态。我们的方法的关键在于精心设计的策略，将提示提供的对象级信息与局部图像特征融合，从而形成一个能够推广到新概念的特征空间。我们在基于两个流行数据集REAL275和Toyota-Light的新基准上验证了我们的方法，结果表明我们的方法在不同场景中估计对象的相对6D姿态方面优于成熟的手工方法和最近的深度学习基线。

## 🔬 方法详解

**问题定义**：本论文旨在解决开放词汇对象6D姿态估计的问题，现有方法通常依赖于具体的对象模型，限制了其灵活性和适应性。

**核心思路**：我们的方法通过文本提示来指定对象，利用视觉-语言模型进行对象分割和姿态估计，从而消除了对对象模型的依赖。

**技术框架**：整体架构包括文本提示输入、视觉-语言模型处理、对象分割模块和姿态估计模块，形成一个完整的处理流程。

**关键创新**：最重要的创新在于将文本提示与局部图像特征有效融合，形成一个能够处理新概念的特征空间，这与传统方法的依赖对象模型形成鲜明对比。

**关键设计**：在技术细节上，我们设计了特定的损失函数以优化分割和姿态估计的精度，同时采用了适应性网络结构以增强模型的泛化能力。

## 📊 实验亮点

实验结果表明，我们的方法在REAL275和Toyota-Light数据集上相较于传统手工方法和深度学习基线，姿态估计精度提升显著，具体性能数据未提供，但整体表现优于现有技术。

## 🎯 应用场景

该研究的潜在应用领域包括机器人视觉、增强现实和自动驾驶等，能够在没有具体对象模型的情况下，实现对新对象的快速识别和姿态估计，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We introduce the new setting of open-vocabulary object 6D pose estimation, in which a textual prompt is used to specify the object of interest. In contrast to existing approaches, in our setting (i) the object of interest is specified solely through the textual prompt, (ii) no object model (e.g., CAD or video sequence) is required at inference, and (iii) the object is imaged from two RGBD viewpoints of different scenes. To operate in this setting, we introduce a novel approach that leverages a Vision-Language Model to segment the object of interest from the scenes and to estimate its relative 6D pose. The key of our approach is a carefully devised strategy to fuse object-level information provided by the prompt with local image features, resulting in a feature space that can generalize to novel concepts. We validate our approach on a new benchmark based on two popular datasets, REAL275 and Toyota-Light, which collectively encompass 34 object instances appearing in four thousand image pairs. The results demonstrate that our approach outperforms both a well-established hand-crafted method and a recent deep learning-based baseline in estimating the relative 6D pose of objects in different scenes. Code and dataset are available at https://jcorsetti.github.io/oryon.

