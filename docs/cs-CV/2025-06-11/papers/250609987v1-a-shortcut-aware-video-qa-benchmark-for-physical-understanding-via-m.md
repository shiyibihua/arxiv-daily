---
layout: default
title: A Shortcut-aware Video-QA Benchmark for Physical Understanding via Minimal Video Pairs
---

# A Shortcut-aware Video-QA Benchmark for Physical Understanding via Minimal Video Pairs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09987" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09987v1</a>
  <a href="https://arxiv.org/pdf/2506.09987.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09987v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09987v1', 'A Shortcut-aware Video-QA Benchmark for Physical Understanding via Minimal Video Pairs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Benno Krojer, Mojtaba Komeili, Candace Ross, Quentin Garrido, Koustuv Sinha, Nicolas Ballas, Mahmoud Assran

**分类**: cs.CV, cs.LG

**发布日期**: 2025-06-11

---

## 💡 一句话要点

**提出最小视频对基准以解决视频语言模型的物理理解问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `视频问答` `物理理解` `捷径感知` `多模态学习` `模型评估`

## 📋 核心要点

1. 现有基准测试容易受到表面线索的影响，导致模型性能评估不准确。
2. 提出最小视频对基准，通过引入视觉相似但答案相反的视频对，增强模型的物理理解能力评估。
3. 人类在MVP基准上的表现为92.9%，而最佳开源视频语言模型的表现为40.2%，显著高于随机表现的25%。

## 📝 摘要（中文）

现有的基准测试在评估视频语言模型的时空理解和推理能力时，容易受到基于表面视觉或文本线索的捷径解决方案的影响。本文通过引入最小视频对（MVP）基准，提出了一种简单的捷径感知视频问答基准，以评估视频语言模型的物理理解能力。该基准包含55K个高质量的多项选择视频问答示例，专注于物理世界的理解。每个示例都有一个最小变化对，要求模型在两个视觉相似但答案相反的视频中都给出正确答案，从而有效避免了依赖视觉或文本偏见的捷径解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视频语言模型评估中由于捷径解决方案导致的性能虚高问题。现有方法往往依赖于表面视觉或文本线索，无法真实反映模型的理解能力。

**核心思路**：论文提出的最小视频对基准通过引入视觉相似但答案相反的视频对，迫使模型在理解物理世界时进行更深层次的推理，而非依赖表面特征。

**技术框架**：MVP基准包含55K个多项选择视频问答示例，分为多个模块，包括数据收集、样本设计和评估机制。每个样本都有一个最小变化对，确保模型必须在两个视频中都给出正确答案。

**关键创新**：最重要的创新在于引入最小变化对的设计，使得模型无法仅依赖视觉或文本偏见，从而提高了评估的准确性和可靠性。

**关键设计**：在样本设计中，确保每个视频对在视觉上相似但在答案上相反，采用高质量的多项选择题设计，确保问题的多样性和挑战性。

## 📊 实验亮点

在MVP基准测试中，人类的表现达到92.9%，而最佳开源视频语言模型的表现仅为40.2%，显著高于随机表现的25%。这一结果表明，MVP基准有效地评估了模型的物理理解能力，并揭示了现有模型的局限性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、机器人交互和智能视频分析等。通过提高视频语言模型的物理理解能力，可以在自动驾驶、智能监控和人机交互等领域实现更高效的应用，推动相关技术的发展与创新。

## 📄 摘要（原文）

> Existing benchmarks for assessing the spatio-temporal understanding and reasoning abilities of video language models are susceptible to score inflation due to the presence of shortcut solutions based on superficial visual or textual cues. This paper mitigates the challenges in accurately assessing model performance by introducing the Minimal Video Pairs (MVP) benchmark, a simple shortcut-aware video QA benchmark for assessing the physical understanding of video language models. The benchmark is comprised of 55K high-quality multiple-choice video QA examples focusing on physical world understanding. Examples are curated from nine video data sources, spanning first-person egocentric and exocentric videos, robotic interaction data, and cognitive science intuitive physics benchmarks. To mitigate shortcut solutions that rely on superficial visual or textual cues and biases, each sample in MVP has a minimal-change pair -- a visually similar video accompanied by an identical question but an opposing answer. To answer a question correctly, a model must provide correct answers for both examples in the minimal-change pair; as such, models that solely rely on visual or textual biases would achieve below random performance. Human performance on MVP is 92.9\%, while the best open-source state-of-the-art video-language model achieves 40.2\% compared to random performance at 25\%.

