---
layout: default
title: "Yume-1.5: A Text-Controlled Interactive World Generation Model"
---

# Yume-1.5: A Text-Controlled Interactive World Generation Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.22096" class="toolbar-btn" target="_blank">📄 arXiv: 2512.22096v1</a>
  <a href="https://arxiv.org/pdf/2512.22096.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.22096v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.22096v1', 'Yume-1.5: A Text-Controlled Interactive World Generation Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaofeng Mao, Zhen Li, Chuanhao Li, Xiaojie Xu, Kaining Ying, Tong He, Jiangmiao Pang, Yu Qiao, Kaipeng Zhang

**分类**: cs.CV

**发布日期**: 2025-12-26

---

## 💡 一句话要点

**Yume-1.5：一种文本控制的交互式世界生成模型，提升实时性和可控性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `交互式世界生成` `文本控制` `长视频生成` `注意力蒸馏` `实时渲染` `线性注意力` `上下文压缩`

## 📋 核心要点

1. 现有交互式世界生成方法参数量巨大、推理步骤繁琐、历史上下文增长迅速，严重限制了实时性能和文本控制能力。
2. Yume-1.5通过精心设计的框架，支持从单张图像或文本提示生成可交互、连续的世界，并支持键盘探索。
3. 该方法包含长视频生成框架、实时流加速策略和文本控制的世界事件生成方法，提升了生成速度和可控性。

## 📝 摘要（中文）

本文提出Yume-1.5，一个新颖的框架，旨在从单张图像或文本提示中生成逼真、交互式和连续的世界。该框架支持基于键盘对生成世界的探索。Yume-1.5包含三个核心组件：（1）一个集成了统一上下文压缩和线性注意力的长视频生成框架；（2）一种由双向注意力蒸馏和增强的文本嵌入方案驱动的实时流加速策略；（3）一种用于生成世界事件的文本控制方法。代码库已在补充材料中提供。

## 🔬 方法详解

**问题定义**：现有交互式世界生成模型面临参数量过大、推理速度慢、难以进行文本控制等问题。这些问题限制了其在实时交互应用中的潜力，用户难以根据自身意愿定制生成的世界。

**核心思路**：Yume-1.5的核心思路是通过优化模型结构和推理流程，在保证生成质量的前提下，显著提升生成速度和文本控制能力。具体而言，采用上下文压缩、线性注意力等技术降低计算复杂度，利用注意力蒸馏加速推理，并引入文本嵌入方案实现文本控制。

**技术框架**：Yume-1.5框架包含三个主要模块：（1）**长视频生成框架**：负责生成连续的世界场景，采用统一上下文压缩和线性注意力机制，降低计算量。（2）**实时流加速策略**：通过双向注意力蒸馏和增强的文本嵌入方案，加速推理过程，实现实时渲染。（3）**文本控制模块**：允许用户通过文本提示控制世界事件的生成，增强交互性。

**关键创新**：Yume-1.5的关键创新在于其综合运用了多种技术，实现了实时、可控的交互式世界生成。与现有方法相比，Yume-1.5在模型大小、推理速度和文本控制能力方面都有显著提升。双向注意力蒸馏和增强的文本嵌入方案是实现这些提升的关键。

**关键设计**：在长视频生成框架中，线性注意力机制的使用降低了计算复杂度，使得模型能够处理更长的上下文。双向注意力蒸馏通过将大型模型的知识迁移到小型模型，加速了推理过程。增强的文本嵌入方案则允许模型更好地理解文本提示，从而实现更精确的文本控制。具体的参数设置、损失函数和网络结构等细节在补充材料中提供。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22096v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22096v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22096v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文重点在于框架设计和技术创新，具体实验数据未知，但摘要强调了在实时性能和文本控制能力方面的提升。代码库已开源，方便研究者复现和进一步研究。

## 🎯 应用场景

Yume-1.5具有广泛的应用前景，包括游戏开发、虚拟现实、教育娱乐等领域。它可以用于快速生成游戏场景、创建沉浸式虚拟体验、以及提供个性化的学习环境。未来，该技术有望进一步发展，实现更复杂、更逼真的交互式世界生成。

## 📄 摘要（原文）

> Recent approaches have demonstrated the promise of using diffusion models to generate interactive and explorable worlds. However, most of these methods face critical challenges such as excessively large parameter sizes, reliance on lengthy inference steps, and rapidly growing historical context, which severely limit real-time performance and lack text-controlled generation capabilities. To address these challenges, we propose \method, a novel framework designed to generate realistic, interactive, and continuous worlds from a single image or text prompt. \method achieves this through a carefully designed framework that supports keyboard-based exploration of the generated worlds. The framework comprises three core components: (1) a long-video generation framework integrating unified context compression with linear attention; (2) a real-time streaming acceleration strategy powered by bidirectional attention distillation and an enhanced text embedding scheme; (3) a text-controlled method for generating world events. We have provided the codebase in the supplementary material.

