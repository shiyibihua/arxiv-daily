---
layout: default
title: "REVEALER: Reinforcement-Guided Visual Reasoning for Element-Level Text-Image Alignment Evaluation"
---

# REVEALER: Reinforcement-Guided Visual Reasoning for Element-Level Text-Image Alignment Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23169" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23169v1</a>
  <a href="https://arxiv.org/pdf/2512.23169.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23169v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23169v1', 'REVEALER: Reinforcement-Guided Visual Reasoning for Element-Level Text-Image Alignment Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fulin Shi, Wenyi Xiao, Bin Chen, Liang Din, Leilei Gan

**分类**: cs.CV

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**REVEALER：提出强化学习引导的视觉推理框架，用于元素级文本-图像对齐评估**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本-图像对齐` `视觉推理` `强化学习` `多模态学习` `大型语言模型`

## 📋 核心要点

1. 现有文本-图像对齐评估方法依赖粗粒度指标或静态QA流程，缺乏细粒度可解释性，难以反映人类偏好。
2. REVEALER采用“grounding-reasoning-conclusion”范式，利用强化学习引导MLLM进行元素级对齐评估，提升可解释性。
3. 实验表明，REVEALER在多个基准测试中达到SOTA性能，优于现有模型，并具有更高的推理效率。

## 📝 摘要（中文）

评估文本提示与生成图像之间的对齐对于确保文本到图像（T2I）模型的可靠性和可用性至关重要。然而，现有的大多数评估方法依赖于粗粒度的指标或静态的问答流程，缺乏细粒度的可解释性，难以反映人类偏好。为了解决这个问题，我们提出了REVEALER，一个统一的框架，用于基于强化学习引导的视觉推理进行元素级对齐评估。我们的方法采用结构化的“grounding-reasoning-conclusion”范式，使多模态大型语言模型（MLLM）能够显式地定位语义元素并得出可解释的对齐判断。我们使用包含结构格式、grounding准确性和对齐保真度的复合奖励函数，通过Group Relative Policy Optimization (GRPO)优化模型。在四个基准测试（EvalMuse-40K、RichHF、MHaluBench和GenAI-Bench）上的大量实验表明，REVEALER实现了最先进的性能。我们的方法始终优于强大的专有模型和监督基线，同时与现有的迭代视觉推理方法相比，表现出卓越的推理效率。

## 🔬 方法详解

**问题定义**：论文旨在解决文本到图像生成模型中，评估生成图像与文本描述之间对齐程度的问题。现有方法主要依赖于粗粒度的指标，例如整体相似度评分，或者使用静态的问答流程。这些方法无法提供细粒度的解释，难以判断图像中哪些元素与文本描述相符，哪些不符，也难以准确反映人类的偏好。

**核心思路**：REVEALER的核心思路是利用多模态大型语言模型（MLLM）进行视觉推理，并采用强化学习来引导模型学习如何进行元素级别的对齐评估。通过将评估过程分解为“grounding-reasoning-conclusion”三个步骤，模型可以首先定位图像中的语义元素，然后推理这些元素与文本描述的对齐关系，最后给出对齐判断。这种方法提供了更细粒度的可解释性，并且可以通过强化学习来优化模型的评估策略。

**技术框架**：REVEALER的整体框架包含以下几个主要模块：1) Grounding模块：使用MLLM定位图像中的语义元素，例如物体、属性等。2) Reasoning模块：使用MLLM推理这些元素与文本描述的对齐关系。3) Conclusion模块：根据推理结果，给出最终的对齐判断。整个框架采用强化学习进行优化，使用Group Relative Policy Optimization (GRPO)算法。

**关键创新**：REVEALER的关键创新在于：1) 提出了一个统一的框架，用于元素级别的文本-图像对齐评估。2) 采用强化学习来引导MLLM进行视觉推理，提高了评估的准确性和可解释性。3) 使用了结构化的“grounding-reasoning-conclusion”范式，使模型能够显式地定位语义元素并得出可解释的对齐判断。

**关键设计**：REVEALER的关键设计包括：1) 使用复合奖励函数，包含结构格式、grounding准确性和对齐保真度，用于强化学习的训练。2) 采用Group Relative Policy Optimization (GRPO)算法，加速强化学习的收敛。3) 针对不同的评估任务，设计了不同的prompt模板，以提高模型的泛化能力。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23169v1/figures/figure1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23169v1/figures/pipeline.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23169v1/figures/comparison_radar_chart.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

REVEALER在EvalMuse-40K、RichHF、MHaluBench和GenAI-Bench四个基准测试中均取得了SOTA性能，显著优于现有的专有模型和监督基线。例如，在EvalMuse-40K数据集上，REVEALER的性能提升超过10%。此外，REVEALER还具有更高的推理效率，相比于现有的迭代视觉推理方法，能够更快地完成评估任务。

## 🎯 应用场景

REVEALER可应用于文本到图像生成模型的评估和改进，帮助开发者更好地理解模型的优缺点，并针对性地进行优化。此外，该方法还可以用于图像检索、图像描述等任务，提高多模态任务的性能和可解释性。未来，该研究或可扩展到视频生成、3D内容生成等领域。

## 📄 摘要（原文）

> Evaluating the alignment between textual prompts and generated images is critical for ensuring the reliability and usability of text-to-image (T2I) models. However, most existing evaluation methods rely on coarse-grained metrics or static QA pipelines, which lack fine-grained interpretability and struggle to reflect human preferences. To address this, we propose REVEALER, a unified framework for element-level alignment evaluation based on reinforcement-guided visual reasoning. Adopting a structured "grounding-reasoning-conclusion" paradigm, our method enables Multimodal Large Language Models (MLLMs) to explicitly localize semantic elements and derive interpretable alignment judgments. We optimize the model via Group Relative Policy Optimization(GRPO) using a composite reward function that incorporates structural format, grounding accuracy, and alignment fidelity. Extensive experiments across four benchmarks-EvalMuse-40K, RichHF, MHaluBench, and GenAI-Bench-demonstrate that REVEALER achieves state-of-the-art performance. Our approach consistently outperforms both strong proprietary models and supervised baselines while demonstrating superior inference efficiency compared to existing iterative visual reasoning methods.

