---
layout: default
title: Revisiting Visual Understanding in Multimodal Reasoning through a Lens of Image Perturbation
---

# Revisiting Visual Understanding in Multimodal Reasoning through a Lens of Image Perturbation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09736" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09736v2</a>
  <a href="https://arxiv.org/pdf/2506.09736.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09736v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09736v2', 'Revisiting Visual Understanding in Multimodal Reasoning through a Lens of Image Perturbation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuting Li, Lai Wei, Kaipeng Zheng, Jingyuan Huang, Guilin Li, Bo Wang, Linghe Kong, Lichao Sun, Weiran Huang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-11 (更新: 2025-09-28)

**备注**: Technical Report

**🔗 代码/项目**: [GITHUB](https://github.com/YutingLi0606/Vision-Matters)

---

## 💡 一句话要点

**提出视觉扰动框架以提升多模态推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `视觉扰动` `感知鲁棒性` `数学推理` `大型语言模型`

## 📋 核心要点

1. 现有多模态大型语言模型在视觉处理方面存在不足，未能有效整合视觉信息进行推理。
2. 本文提出了一种视觉扰动框架，通过三种扰动策略提升模型的感知鲁棒性，且无需额外的训练数据。
3. 实验结果显示，该方法在数学推理性能上有显著提升，尤其在与开源7B RL调优模型的比较中表现出色。

## 📝 摘要（中文）

尽管多模态大型语言模型（MLLMs）取得了快速进展，但在视觉处理方面仍存在不足。研究发现，仅使用语言模型并结合图像描述，性能可与直接处理视觉输入的MLLMs相媲美。为此，本文提出了一种简单的视觉扰动框架，通过引入三种针对性的扰动策略，增强感知鲁棒性，而无需算法修改或额外训练数据。通过在多个数据集上的广泛实验，验证了该方法在数学推理性能上的一致性提升，且与算法改进的效果相当。研究结果强调了视觉扰动在多模态数学推理中的关键作用。

## 🔬 方法详解

**问题定义**：本文旨在解决当前多模态大型语言模型在视觉信息整合和推理能力上的不足，尤其是它们在处理原始视觉输入时的局限性。现有方法往往未能有效利用视觉信息，导致推理性能不佳。

**核心思路**：论文提出的视觉扰动框架通过引入三种扰动策略（干扰物拼接、保持主导性的混合和随机旋转），增强模型的感知鲁棒性。这些策略旨在改善模型对视觉信息的理解和整合能力。

**技术框架**：整体架构包括三个主要阶段：首先，通过扰动策略对输入图像进行处理；其次，将处理后的图像与文本信息结合；最后，利用现有的后训练管道（如SFT、DPO和GRPO）进行模型的推理和评估。

**关键创新**：最重要的技术创新在于提出了视觉扰动的概念，并通过简单的扰动策略显著提升了模型的推理能力。这与传统的算法改进方法形成鲜明对比，强调了视觉信息处理的重要性。

**关键设计**：在设计上，扰动策略的选择基于对视觉信息的理解和整合需求，确保每种扰动都能针对性地提升模型的特定能力。具体的参数设置和损失函数设计未在摘要中详细说明，需参考原文获取更多技术细节。

## 📊 实验亮点

实验结果表明，采用视觉扰动框架后，模型在数学推理任务上的性能显著提升，尤其是在与开源7B RL调优模型的比较中，表现出与算法改进相当的效果，验证了视觉扰动的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、金融分析和科学研究等需要多模态推理的场景。通过提升模型的视觉理解能力，可以在更复杂的任务中实现更高的准确性和效率，未来可能推动多模态人工智能的广泛应用。

## 📄 摘要（原文）

> Despite the rapid progress of multimodal large language models (MLLMs), they have largely overlooked the importance of visual processing. In a simple yet revealing experiment, we interestingly find that language-only models, when provided with image captions, can achieve comparable or even better performance than MLLMs that consume raw visual inputs. This suggests that current MLLMs may generate accurate visual descriptions but fail to effectively integrate them during reasoning. Motivated by this, we propose a simple visual perturbation framework that enhances perceptual robustness without requiring algorithmic modifications or additional training data. Our approach introduces three targeted perturbations: distractor concatenation, dominance-preserving mixup, and random rotation, that can be easily integrated into existing post-training pipelines including SFT, DPO, and GRPO. Through extensive experiments across multiple datasets, we demonstrate consistent improvements in mathematical reasoning performance, with gains comparable to those achieved through algorithmic changes. Additionally, we achieve competitive performance among open-source 7B RL-tuned models by training Qwen2.5-VL-7B with visual perturbation. Through comprehensive ablation studies, we analyze the effectiveness of different perturbation strategies, revealing that each perturbation type contributes uniquely to different aspects of visual reasoning. Our findings highlight the critical role of visual perturbation in multimodal mathematical reasoning: better reasoning begins with better seeing. Our code is available at https://github.com/YutingLi0606/Vision-Matters.

