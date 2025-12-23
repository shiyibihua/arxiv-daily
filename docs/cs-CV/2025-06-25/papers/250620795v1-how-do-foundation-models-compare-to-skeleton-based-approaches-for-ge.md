---
layout: default
title: How do Foundation Models Compare to Skeleton-Based Approaches for Gesture Recognition in Human-Robot Interaction?
---

# How do Foundation Models Compare to Skeleton-Based Approaches for Gesture Recognition in Human-Robot Interaction?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20795" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20795v1</a>
  <a href="https://arxiv.org/pdf/2506.20795.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20795v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20795v1', 'How do Foundation Models Compare to Skeleton-Based Approaches for Gesture Recognition in Human-Robot Interaction?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Stephanie Käs, Anton Burenko, Louis Markert, Onur Alp Culha, Dennis Mack, Timm Linder, Bastian Leibe

**分类**: cs.CV, cs.HC, cs.RO

**发布日期**: 2025-06-25

---

## 💡 一句话要点

**比较基础模型与骨架方法在机器人交互手势识别中的应用**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `手势识别` `人机交互` `视觉基础模型` `视觉语言模型` `动态识别` `多任务学习` `数据集构建`

## 📋 核心要点

1. 现有的手势识别方法多依赖于特定任务的深度学习架构，缺乏灵活性和通用性。
2. 本文提出通过视觉基础模型和视觉语言模型来简化手势识别系统，探索其在动态全身手势识别中的应用。
3. 实验结果表明，HD-GCN在性能上表现最佳，而V-JEPA显示出作为多任务模型的潜力，Gemini在零样本设置下存在局限性。

## 📝 摘要（中文）

手势是人机交互中的重要非语言沟通方式，尤其在嘈杂的环境中。传统的手势识别方法依赖于特定任务的深度学习架构，使用图像、视频或骨架姿态估计作为输入。本文研究了如何将视觉基础模型（VFM）和视觉语言模型（VLM）应用于动态全身手势识别，并与HD-GCN这一顶尖骨架方法进行比较。我们引入了NUGGET数据集，专门用于评估人机交互中的手势识别方法。实验结果显示，HD-GCN表现最佳，而V-JEPA在使用简单的任务特定分类头时也取得了接近的效果，表明其作为共享多任务模型的潜力。相对而言，Gemini在零样本设置下仅依赖文本描述进行手势区分时表现不佳，突显了对手势输入表示的进一步研究需求。

## 🔬 方法详解

**问题定义**：本研究旨在解决传统手势识别方法在动态全身手势识别中的局限性，尤其是在复杂环境下的适应性不足。现有方法通常依赖于特定任务的架构，导致系统复杂性高且灵活性差。

**核心思路**：论文提出利用视觉基础模型（VFM）和视觉语言模型（VLM）来替代传统的任务特定模块，从而简化手势识别系统。通过比较不同模型在手势识别中的表现，探索其在动态场景下的适用性。

**技术框架**：研究中使用了NUGGET数据集进行评估，主要比较了V-JEPA、Gemini Flash 2.0和HD-GCN三种模型。实验流程包括数据预处理、模型训练和性能评估等阶段。

**关键创新**：最重要的创新在于将视觉基础模型与视觉语言模型应用于动态手势识别，展示了其在系统复杂性降低方面的潜力。与传统方法相比，这种方法能够更好地适应多任务场景。

**关键设计**：在模型设计上，V-JEPA采用了简单的任务特定分类头，优化了性能。HD-GCN则作为基线模型，表现出色，而Gemini在仅依赖文本描述进行手势识别时存在明显局限。

## 📊 实验亮点

实验结果显示，HD-GCN在手势识别任务中表现最佳，准确率高于其他模型。而V-JEPA在使用简单分类头时也取得了接近的性能，显示出作为共享多任务模型的潜力。Gemini在零样本设置下的表现较差，强调了对手势输入表示的进一步研究需求。

## 🎯 应用场景

该研究的潜在应用场景包括工业自动化、服务机器人和人机协作等领域。通过改进手势识别技术，可以提升机器人在复杂环境中的交互能力，增强人机沟通的自然性和有效性，未来可能推动智能机器人在更多实际应用中的普及。

## 📄 摘要（原文）

> Gestures enable non-verbal human-robot communication, especially in noisy environments like agile production. Traditional deep learning-based gesture recognition relies on task-specific architectures using images, videos, or skeletal pose estimates as input. Meanwhile, Vision Foundation Models (VFMs) and Vision Language Models (VLMs) with their strong generalization abilities offer potential to reduce system complexity by replacing dedicated task-specific modules. This study investigates adapting such models for dynamic, full-body gesture recognition, comparing V-JEPA (a state-of-the-art VFM), Gemini Flash 2.0 (a multimodal VLM), and HD-GCN (a top-performing skeleton-based approach). We introduce NUGGET, a dataset tailored for human-robot communication in intralogistics environments, to evaluate the different gesture recognition approaches. In our experiments, HD-GCN achieves best performance, but V-JEPA comes close with a simple, task-specific classification head - thus paving a possible way towards reducing system complexity, by using it as a shared multi-task model. In contrast, Gemini struggles to differentiate gestures based solely on textual descriptions in the zero-shot setting, highlighting the need of further research on suitable input representations for gestures.

