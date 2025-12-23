---
layout: default
title: Test-Time Consistency in Vision Language Models
---

# Test-Time Consistency in Vision Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22395" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22395v1</a>
  <a href="https://arxiv.org/pdf/2506.22395.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22395v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22395v1', 'Test-Time Consistency in Vision Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shih-Han Chou, Shivam Chandhok, James J. Little, Leonid Sigal

**分类**: cs.CV

**发布日期**: 2025-06-27

---

## 💡 一句话要点

**提出测试时一致性框架以解决视觉语言模型的不一致性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `一致性框架` `多模态学习` `后处理方法` `语义等价输入`

## 📋 核心要点

1. 现有的视觉语言模型在处理语义等价输入时表现出不一致性，影响了模型的可靠性。
2. 本文提出了一种测试时一致性框架，通过后处理方式增强模型的语义一致性，无需重新训练。
3. 在MM-R3基准测试中，所提方法显著提升了模型的一致性，开辟了多模态学习推理时适应的新方向。

## 📝 摘要（中文）

视觉语言模型（VLMs）在多模态任务中表现出色，但在面对语义等价输入时常常出现不一致的行为，影响其可靠性和稳健性。近期的基准测试显示，即使是最先进的VLMs在语义等价输入上也可能产生不同的预测。本文提出了一种简单有效的测试时一致性框架，通过后处理方式增强语义一致性，而无需监督再训练。该方法适用于任何具有权重的VLM，通过两个互补目标来强制一致预测，从而在MM-R3基准测试中显著提高了一致性。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉语言模型在面对语义等价输入时产生不一致预测的问题。现有方法通常依赖于修改模型架构或进行大规模微调，存在一定的局限性。

**核心思路**：提出了一种后处理的测试时一致性框架，通过两个互补的损失函数来增强模型的预测一致性，避免了重新训练的复杂性。

**技术框架**：整体方法包括两个主要模块：交叉熵一致性损失（Cross-Entropy Agreement Loss）和伪标签一致性损失（Pseudo-Label Consistency Loss）。前者对齐语义等价输入的预测分布，后者则将输出拉向自我平均的一致性。

**关键创新**：最重要的创新点在于提出了一种完全后处理、模型无关的方法，能够在不改变模型结构的情况下提升一致性。与现有方法相比，本方法更为灵活和高效。

**关键设计**：采用了交叉熵损失和伪标签损失作为主要损失函数，确保模型在单个测试输入上进行一致性预测。该方法的设计使其能够直接利用输入信息进行优化。

## 📊 实验亮点

实验结果表明，所提框架在MM-R3基准测试中显著提升了一致性，具体表现为在多个模型上均实现了显著的性能提升，尤其是在处理语义等价输入时，表现出更高的预测稳定性。

## 🎯 应用场景

该研究的潜在应用领域包括多模态学习、自然语言处理与计算机视觉的结合等。通过提升视觉语言模型的一致性，能够增强其在实际应用中的可靠性，尤其是在需要高精度预测的场景，如自动驾驶、智能助手等。未来，该方法可能推动更多模型在推理时的适应性改进。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) have achieved impressive performance across a wide range of multimodal tasks, yet they often exhibit inconsistent behavior when faced with semantically equivalent inputs, undermining their reliability and robustness. Recent benchmarks, such as MM-R3, highlight that even state-of-the-art VLMs can produce divergent predictions across semantically equivalent inputs, despite maintaining high average accuracy. Prior work addresses this issue by modifying model architectures or conducting large-scale fine-tuning on curated datasets. In contrast, we propose a simple and effective test-time consistency framework that enhances semantic consistency without supervised re-training. Our method is entirely post-hoc, model-agnostic, and applicable to any VLM with access to its weights. Given a single test point, we enforce consistent predictions via two complementary objectives: (i) a Cross-Entropy Agreement Loss that aligns predictive distributions across semantically equivalent inputs, and (ii) a Pseudo-Label Consistency Loss that draws outputs toward a self-averaged consensus. Our method is plug-and-play and leverages information from a single test input itself to improve consistency. Experiments on the MM-R3 benchmark show that our framework yields substantial gains in consistency across state-of-the-art models, establishing a new direction for inference-time adaptation in multimodal learning.

