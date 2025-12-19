---
layout: default
title: Sketch-in-Latents: Eliciting Unified Reasoning in MLLMs
---

# Sketch-in-Latents: Eliciting Unified Reasoning in MLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16584" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16584v1</a>
  <a href="https://arxiv.org/pdf/2512.16584.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16584v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16584v1', 'Sketch-in-Latents: Eliciting Unified Reasoning in MLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jintao Tong, Jiaqi Gu, Yujing Lou, Lubin Fan, Yixiong Zou, Yue Wu, Jieping Ye, Ruixuan Li

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: 14 pages, 11 figures

**🔗 代码/项目**: [GITHUB](https://github.com/TungChintao/SkiLa)

---

## 💡 一句话要点

**提出Sketch-in-Latents (SkiLa)，实现MLLM中统一的多模态推理与视觉想象。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `视觉想象` `统一推理` `潜在空间` `草图生成`

## 📋 核心要点

1. 现有MLLM在视觉想象方面存在不足，无法像人类一样灵活地进行视觉-文本交互。
2. SkiLa通过在MLLM的潜在空间中生成连续的视觉嵌入（潜在草图token）来实现统一的多模态推理。
3. 实验表明，SkiLa在视觉任务上表现优异，并对通用多模态基准具有良好的泛化能力。

## 📝 摘要（中文）

多模态大型语言模型(MLLM)擅长通过文本推理进行视觉理解任务，但在需要视觉想象的场景中表现不佳。与采用预定义外部工具包或在思考过程中生成图像的现有方法不同，人类可以在思考过程中形成灵活的视觉-文本想象和交互，而无需预定义的工具包，其中一个重要原因是人类在大脑内部的统一空间中构建视觉-文本思考过程。受此能力的启发，鉴于当前的MLLM已经将视觉和文本信息编码在相同的特征空间中，我们认为视觉token可以无缝地插入到文本token所携带的推理过程中，理想情况下，所有的视觉想象过程都可以由潜在特征编码。为了实现这个目标，我们提出Sketch-in-Latents (SkiLa)，这是一种用于统一多模态推理的新范式，它扩展了MLLM的自回归能力，以原生生成连续的视觉嵌入，称为潜在草图token，作为视觉思考。在多步推理过程中，模型在生成文本思考token的文本思考模式和生成潜在草图token的视觉草图模式之间动态切换。提出了一种潜在的视觉语义重建机制，以确保这些潜在的草图token在语义上是接地的。大量的实验表明，SkiLa在以视觉为中心的任务上取得了优异的性能，同时对各种通用多模态基准表现出强大的泛化能力。

## 🔬 方法详解

**问题定义**：现有MLLM在处理需要视觉想象的任务时，依赖于预定义的外部工具或在推理过程中生成图像，这限制了模型的灵活性和效率。人类可以在大脑内部的统一空间中进行视觉-文本思考，而MLLM缺乏这种能力。因此，需要一种方法使MLLM能够像人类一样进行灵活的视觉-文本推理和想象。

**核心思路**：SkiLa的核心思路是将视觉信息直接嵌入到MLLM的潜在空间中，作为推理过程的一部分。通过生成“潜在草图token”，模型可以在文本推理的同时进行视觉想象，从而实现统一的多模态推理。这种方法避免了对外部工具的依赖，并允许模型在潜在空间中灵活地操作视觉信息。

**技术框架**：SkiLa的整体框架包括文本思考模式和视觉草图模式。在文本思考模式下，模型生成文本token进行推理；在视觉草图模式下，模型生成潜在草图token进行视觉想象。模型在这两种模式之间动态切换，以完成多步推理任务。为了确保潜在草图token的语义一致性，SkiLa还引入了一种潜在视觉语义重建机制。

**关键创新**：SkiLa的关键创新在于将视觉想象过程融入到MLLM的自回归生成过程中。通过直接在潜在空间中生成视觉token，SkiLa实现了视觉和文本信息的统一表示和推理。这种方法与现有方法（依赖外部工具或生成图像）的本质区别在于，它允许模型在内部进行视觉想象，而无需额外的步骤或模块。

**关键设计**：SkiLa的关键设计包括：1) 潜在草图token的生成方式，可能涉及特定的网络结构或损失函数，以确保生成的token具有语义意义；2) 文本思考模式和视觉草图模式之间的切换机制，可能基于某种策略或控制信号；3) 潜在视觉语义重建机制，用于将潜在草图token映射回视觉空间，并确保其与原始视觉信息的一致性。具体的参数设置、损失函数和网络结构等细节需要在论文中进一步查找。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16584v1/img/method.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16584v1/img/hyper.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16584v1/img/case_geo.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，SkiLa在以视觉为中心的任务上取得了优异的性能，超过了现有的MLLM方法。此外，SkiLa在各种通用多模态基准上表现出强大的泛化能力，表明其具有良好的鲁棒性和适应性。具体的性能数据和提升幅度需要在论文中进一步查找。

## 🎯 应用场景

SkiLa具有广泛的应用前景，例如视觉问答、图像描述生成、机器人导航和人机交互等领域。它可以帮助机器更好地理解和推理视觉信息，并生成更自然和连贯的多模态内容。未来，SkiLa有望应用于更复杂的视觉任务，例如视频理解、三维重建和虚拟现实。

## 📄 摘要（原文）

> While Multimodal Large Language Models (MLLMs) excel at visual understanding tasks through text reasoning, they often fall short in scenarios requiring visual imagination. Unlike current works that take predefined external toolkits or generate images during thinking, however, humans can form flexible visual-text imagination and interactions during thinking without predefined toolkits, where one important reason is that humans construct the visual-text thinking process in a unified space inside the brain. Inspired by this capability, given that current MLLMs already encode visual and text information in the same feature space, we hold that visual tokens can be seamlessly inserted into the reasoning process carried by text tokens, where ideally, all visual imagination processes can be encoded by the latent features. To achieve this goal, we propose Sketch-in-Latents (SkiLa), a novel paradigm for unified multi-modal reasoning that expands the auto-regressive capabilities of MLLMs to natively generate continuous visual embeddings, termed latent sketch tokens, as visual thoughts. During multi-step reasoning, the model dynamically alternates between textual thinking mode for generating textual think tokens and visual sketching mode for generating latent sketch tokens. A latent visual semantics reconstruction mechanism is proposed to ensure these latent sketch tokens are semantically grounded. Extensive experiments demonstrate that SkiLa achieves superior performance on vision-centric tasks while exhibiting strong generalization to diverse general multi-modal benchmarks. Codes will be released at https://github.com/TungChintao/SkiLa.

