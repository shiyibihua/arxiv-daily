---
layout: default
title: AdaTooler-V: Adaptive Tool-Use for Images and Videos
---

# AdaTooler-V: Adaptive Tool-Use for Images and Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16918" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16918v1</a>
  <a href="https://arxiv.org/pdf/2512.16918.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16918v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16918v1', 'AdaTooler-V: Adaptive Tool-Use for Images and Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chaoyang Wang, Kaituo Feng, Dongyang Chen, Zhongyu Wang, Zhixun Li, Sicheng Gao, Meng Meng, Xu Zhou, Manyuan Zhang, Yuzhang Shang, Xiangyu Yue

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: Project page: https://github.com/CYWang735/AdaTooler-V

---

## 💡 一句话要点

**提出AdaTooler-V，通过自适应工具使用提升多模态大语言模型在图像和视频任务中的推理效率和性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `自适应工具使用` `强化学习` `视觉推理` `图像视频处理`

## 📋 核心要点

1. 现有开源多模态大语言模型存在盲目使用工具的推理模式，即使不必要也会调用视觉工具，导致推理开销增加和性能下降。
2. AdaTooler-V通过判断视觉问题是否真正需要工具，执行自适应工具使用，从而避免不必要的工具调用。
3. 提出的AT-GRPO强化学习算法根据工具效益评分自适应调整奖励，鼓励模型仅在工具带来改进时才使用，实验表明性能超越GPT-4o和Gemini 1.5 Pro。

## 📝 摘要（中文）

本文提出AdaTooler-V，一种多模态大语言模型(MLLM)，通过确定视觉问题是否真正需要工具来执行自适应工具使用。为了实现这一目标，我们引入了AT-GRPO，一种强化学习算法，它基于每个样本的工具效益评分自适应地调整奖励尺度，鼓励模型仅在工具提供真正的改进时才调用它们。此外，我们构建了两个数据集来支持训练：AdaTooler-V-CoT-100k用于SFT冷启动，AdaTooler-V-300k用于具有可验证奖励的RL，涵盖单图像、多图像和视频数据。在十二个基准测试上的实验表明，AdaTooler-V具有强大的推理能力，在各种视觉推理任务中优于现有方法。值得注意的是，AdaTooler-V-7B在高分辨率基准V*上实现了89.8%的准确率，超过了商业专有模型GPT-4o和Gemini 1.5 Pro。所有代码、模型和数据均已发布。

## 🔬 方法详解

**问题定义**：现有开源多模态大语言模型(MLLMs)在处理视觉任务时，常常不加区分地调用视觉工具，即使问题本身并不需要这些工具。这种“盲目”的工具使用方式导致了不必要的计算开销，降低了推理效率，并且在某些情况下还会损害模型的性能。因此，如何让MLLMs学会自适应地判断何时应该使用工具，何时应该避免使用工具，成为了一个亟待解决的问题。

**核心思路**：AdaTooler-V的核心思路是让模型能够根据输入数据的特点和任务的需求，自适应地决定是否需要调用视觉工具。具体来说，模型会首先对输入进行初步分析，评估使用工具可能带来的收益（Tool Benefit Score），然后根据这个收益来决定是否调用工具。这种自适应的工具使用策略可以有效地避免不必要的计算开销，提高推理效率，并且在某些情况下还可以提升模型的性能。

**技术框架**：AdaTooler-V的整体框架主要包括以下几个部分：1) 多模态输入编码器：用于将图像、视频和文本等多种模态的输入数据编码成统一的特征表示。2) 工具使用决策模块：根据编码后的特征，评估使用各种视觉工具可能带来的收益，并决定是否调用这些工具。3) 视觉工具模块：包含各种视觉处理工具，例如目标检测、图像分割、OCR等。4) 语言模型：用于生成最终的输出结果。5) 强化学习训练模块：使用AT-GRPO算法对模型进行训练，使其能够更好地学习自适应工具使用策略。

**关键创新**：AdaTooler-V最重要的技术创新点在于AT-GRPO（Adaptive Tool-use with Gradient-based Reward Policy Optimization）强化学习算法。该算法能够根据每个样本的工具效益评分自适应地调整奖励尺度，从而鼓励模型仅在工具提供真正的改进时才调用它们。与传统的强化学习算法相比，AT-GRPO能够更有效地学习自适应工具使用策略，并且能够更好地平衡工具使用的收益和成本。

**关键设计**：AT-GRPO算法的关键设计在于奖励函数的自适应调整。具体来说，算法会首先计算每个样本的工具效益评分（Tool Benefit Score），该评分反映了使用工具可能带来的性能提升。然后，算法会根据这个评分来调整奖励函数的尺度，对于工具效益评分较高的样本，算法会给予更高的奖励，从而鼓励模型调用工具；对于工具效益评分较低的样本，算法会给予较低的奖励，从而鼓励模型避免使用工具。此外，为了支持模型的训练，作者还构建了两个大规模数据集：AdaTooler-V-CoT-100k和AdaTooler-V-300k，分别用于SFT冷启动和RL训练。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16918v1/x3.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16918v1/x4.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16918v1/x5.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

AdaTooler-V在十二个基准测试上表现出强大的推理能力，超越了现有方法。尤其值得注意的是，AdaTooler-V-7B在高分辨率基准V*上达到了89.8%的准确率，超过了商业专有模型GPT-4o和Gemini 1.5 Pro，证明了其在复杂视觉推理任务上的卓越性能。

## 🎯 应用场景

AdaTooler-V在多个领域具有广泛的应用前景，例如智能客服、自动驾驶、视频监控、医疗诊断等。它可以帮助这些应用更高效、更准确地理解和处理视觉信息，从而提升用户体验和工作效率。未来，该研究可以进一步扩展到更多的模态和任务，例如语音、文本等，从而构建更加通用和强大的多模态智能系统。

## 📄 摘要（原文）

> Recent advances have shown that multimodal large language models (MLLMs) benefit from multimodal interleaved chain-of-thought (CoT) with vision tool interactions. However, existing open-source models often exhibit blind tool-use reasoning patterns, invoking vision tools even when they are unnecessary, which significantly increases inference overhead and degrades model performance. To this end, we propose AdaTooler-V, an MLLM that performs adaptive tool-use by determining whether a visual problem truly requires tools. First, we introduce AT-GRPO, a reinforcement learning algorithm that adaptively adjusts reward scales based on the Tool Benefit Score of each sample, encouraging the model to invoke tools only when they provide genuine improvements. Moreover, we construct two datasets to support training: AdaTooler-V-CoT-100k for SFT cold start and AdaTooler-V-300k for RL with verifiable rewards across single-image, multi-image, and video data. Experiments across twelve benchmarks demonstrate the strong reasoning capability of AdaTooler-V, outperforming existing methods in diverse visual reasoning tasks. Notably, AdaTooler-V-7B achieves an accuracy of 89.8\% on the high-resolution benchmark V*, surpassing the commercial proprietary model GPT-4o and Gemini 1.5 Pro. All code, models, and data are released.

