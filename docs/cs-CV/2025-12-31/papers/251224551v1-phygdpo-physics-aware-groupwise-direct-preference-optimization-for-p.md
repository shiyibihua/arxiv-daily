---
layout: default
title: "PhyGDPO: Physics-Aware Groupwise Direct Preference Optimization for Physically Consistent Text-to-Video Generation"
---

# PhyGDPO: Physics-Aware Groupwise Direct Preference Optimization for Physically Consistent Text-to-Video Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24551" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24551v1</a>
  <a href="https://arxiv.org/pdf/2512.24551.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24551v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24551v1', 'PhyGDPO: Physics-Aware Groupwise Direct Preference Optimization for Physically Consistent Text-to-Video Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuanhao Cai, Kunpeng Li, Menglin Jia, Jialiang Wang, Junzhe Sun, Feng Liang, Weifeng Chen, Felix Juefei-Xu, Chu Wang, Ali Thabet, Xiaoliang Dai, Xuan Ju, Alan Yuille, Ji Hou

**分类**: cs.CV

**发布日期**: 2025-12-31

**🔗 代码/项目**: [GITHUB](https://github.com/caiyuanhao1998/Open-PhyGDPO) | [PROJECT_PAGE](https://caiyuanhao1998.github.io/project/)

---

## 💡 一句话要点

**提出PhyGDPO框架，通过物理感知的群体偏好优化实现物理一致的文本生成视频。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本生成视频` `物理一致性` `偏好优化` `视觉语言模型` `群体偏好学习`

## 📋 核心要点

1. 现有文本生成视频方法难以生成符合物理规律的视频，泛化性差，缺乏物理推理能力。
2. 提出PhyGDPO框架，利用物理增强数据和物理引导奖励，优化模型生成物理上合理的视频。
3. 实验表明，PhyGDPO在多个物理一致性测试基准上显著优于现有开源方法。

## 📝 摘要（中文）

本文旨在解决文本生成视频（T2V）领域中，生成符合物理规律的视频这一难题。现有方法主要依赖图形或提示扩展，难以泛化到复杂环境，且缺乏物理推理能力。同时，缺乏包含丰富物理交互和现象的训练数据也是一个问题。为此，本文首先提出了一个物理增强的视频数据构建流程PhyAugPipe，利用具有思维链推理能力的视觉语言模型（VLM）收集大规模训练数据集PhyVidGen-135K。然后，构建了一个基于群体Plackett-Luce概率模型的物理感知群体偏好优化框架PhyGDPO，以捕捉超越成对比较的整体偏好。在PhyGDPO中，设计了物理引导奖励（PGR）方案，嵌入基于VLM的物理奖励，引导优化过程朝着物理一致性方向发展。此外，还提出了LoRA-Switch Reference（LoRA-SR）方案，消除了内存密集型的参考复制，从而实现高效训练。实验表明，该方法在PhyGenBench和VideoPhy2上显著优于最先进的开源方法。

## 🔬 方法详解

**问题定义**：现有文本生成视频模型在生成视觉质量良好的视频方面取得了显著进展，但难以保证生成的视频内容符合物理规律，例如物体运动、碰撞等。现有方法主要依赖于图形引擎或提示词工程，难以泛化到复杂的物理场景，并且缺乏对物理规律的显式建模和推理能力。此外，缺乏大规模的、包含丰富物理交互的训练数据也是一个重要瓶颈。

**核心思路**：本文的核心思路是利用视觉语言模型（VLM）的强大能力，构建大规模的物理增强训练数据，并设计一种物理感知的偏好优化框架，引导模型学习生成符合物理规律的视频。通过物理引导的奖励机制，鼓励模型生成物理上合理的视频内容。

**技术框架**：整体框架包含两个主要阶段：数据构建阶段和模型训练阶段。在数据构建阶段，利用PhyAugPipe流程，使用VLM生成包含物理交互的视频描述，构建大规模数据集PhyVidGen-135K。在模型训练阶段，使用PhyGDPO框架，结合物理引导奖励（PGR）和LoRA-Switch Reference（LoRA-SR）方案，对文本生成视频模型进行优化。

**关键创新**：本文的关键创新在于提出了物理感知的群体偏好优化框架PhyGDPO。与传统的成对偏好优化方法不同，PhyGDPO基于群体Plackett-Luce概率模型，能够捕捉更全面的偏好信息。此外，物理引导奖励（PGR）方案利用VLM对视频的物理合理性进行评估，并将评估结果作为奖励信号，引导模型朝着物理一致性方向优化。LoRA-Switch Reference（LoRA-SR）方案则解决了训练过程中参考视频内存占用过大的问题。

**关键设计**：PhyAugPipe流程利用VLM生成视频描述，并进行思维链推理，以确保描述的准确性和丰富性。物理引导奖励（PGR）方案使用预训练的VLM模型评估视频的物理合理性，并将其转化为奖励信号。LoRA-Switch Reference（LoRA-SR）方案通过切换不同的LoRA模块，减少了参考视频的内存占用。具体的损失函数设计和网络结构细节在论文中有详细描述（未知）。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24551v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24551v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24551v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，PhyGDPO在PhyGenBench和VideoPhy2两个物理一致性测试基准上显著优于现有开源方法。具体而言，PhyGDPO在两个基准上的指标均取得了显著提升（具体数值未知），证明了其在生成物理合理视频方面的有效性。LoRA-SR方案也有效降低了训练过程中的内存占用。

## 🎯 应用场景

该研究成果可应用于虚拟现实、游戏开发、机器人仿真等领域，提升生成内容的真实感和可信度。例如，可以用于生成更逼真的游戏场景，训练更智能的机器人，或者创建更具沉浸感的虚拟现实体验。未来，该技术有望推动人工智能在物理世界的应用。

## 📄 摘要（原文）

> Recent advances in text-to-video (T2V) generation have achieved good visual quality, yet synthesizing videos that faithfully follow physical laws remains an open challenge. Existing methods mainly based on graphics or prompt extension struggle to generalize beyond simple simulated environments or learn implicit physical reasoning. The scarcity of training data with rich physics interactions and phenomena is also a problem. In this paper, we first introduce a Physics-Augmented video data construction Pipeline, PhyAugPipe, that leverages a vision-language model (VLM) with chain-of-thought reasoning to collect a large-scale training dataset, PhyVidGen-135K. Then we formulate a principled Physics-aware Groupwise Direct Preference Optimization, PhyGDPO, framework that builds upon the groupwise Plackett-Luce probabilistic model to capture holistic preferences beyond pairwise comparisons. In PhyGDPO, we design a Physics-Guided Rewarding (PGR) scheme that embeds VLM-based physics rewards to steer optimization toward physical consistency. We also propose a LoRA-Switch Reference (LoRA-SR) scheme that eliminates memory-heavy reference duplication for efficient training. Experiments show that our method significantly outperforms state-of-the-art open-source methods on PhyGenBench and VideoPhy2. Please check our project page at https://caiyuanhao1998.github.io/project/PhyGDPO for more video results. Our code, models, and data will be released at https://github.com/caiyuanhao1998/Open-PhyGDPO

