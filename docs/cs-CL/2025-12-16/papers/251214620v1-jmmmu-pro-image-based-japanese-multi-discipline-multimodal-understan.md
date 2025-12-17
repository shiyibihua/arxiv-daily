---
layout: default
title: JMMMU-Pro: Image-based Japanese Multi-discipline Multimodal Understanding Benchmark via Vibe Benchmark Construction
---

# JMMMU-Pro: Image-based Japanese Multi-discipline Multimodal Understanding Benchmark via Vibe Benchmark Construction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14620" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14620v1</a>
  <a href="https://arxiv.org/pdf/2512.14620.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14620v1" onclick="toggleFavorite(this, '2512.14620v1', 'JMMMU-Pro: Image-based Japanese Multi-discipline Multimodal Understanding Benchmark via Vibe Benchmark Construction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Atsuyuki Miyai, Shota Onohara, Jeonghun Baek, Kiyoharu Aizawa

**分类**: cs.CL, cs.AI, cs.CV

**发布日期**: 2025-12-16

**备注**: Project page: https://mmmu-japanese-benchmark.github.io/JMMMU_Pro/

---

## 💡 一句话要点

**提出JMMMU-Pro基准测试，用于评估日语多学科多模态理解能力，并提出Vibe基准构建方法。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态理解` `视觉问答` `日语处理` `基准测试` `图像生成` `大型语言模型` `视觉-文本融合`

## 📋 核心要点

1. 现有基准测试在评估大型语言模型（LMM）的日语多模态理解能力方面存在不足，尤其是在视觉-文本融合理解方面。
2. 提出Vibe基准构建方法，利用图像生成模型自动生成候选问题，并通过人工验证和调整提示来保证基准质量。
3. 实验表明，开源LMM在JMMMU-Pro基准测试上表现显著不足，验证了该基准的挑战性和价值。

## 📝 摘要（中文）

本文介绍了JMMMU-Pro，一个基于图像的日语多学科多模态理解基准测试，以及Vibe基准构建方法，一种可扩展的构建方法。JMMMU-Pro延续了从MMMU到MMMU-Pro的演进，通过将问题图像和问题文本组合成单个图像来扩展JMMMU，从而创建了一个需要通过视觉感知进行综合视觉-文本理解的基准。为了构建JMMMU-Pro，我们提出了Vibe基准构建方法，该方法利用图像生成模型（例如Nano Banana Pro）生成候选视觉问题，然后由人工验证输出，并在必要时使用调整后的提示重新生成，以确保质量。通过利用Nano Banana Pro的高度逼真的图像生成能力及其嵌入清晰日语文本的能力，我们以低成本构建了一个高质量的基准，涵盖了广泛的背景和布局设计。实验结果表明，所有开源LMM在JMMMU-Pro上都表现不佳，这突显了JMMMU-Pro作为指导开源社区未来工作的重要基准。我们相信JMMMU-Pro为评估LMM的日语能力提供了一个更严格的评估工具，并且我们的Vibe基准构建方法也为未来基于图像的VQA基准的开发提供了有效的指导。

## 🔬 方法详解

**问题定义**：论文旨在解决现有日语多模态理解基准的不足，特别是缺乏对视觉和文本信息进行深度融合理解的测试。现有方法要么侧重于简单的视觉问答，要么无法有效评估模型在复杂场景下的日语理解能力。

**核心思路**：论文的核心思路是构建一个更具挑战性的基准测试，该基准测试要求模型能够同时理解图像中的视觉信息和嵌入在图像中的日语文本信息。通过将问题图像和问题文本融合到同一图像中，迫使模型进行更深层次的视觉-文本融合。

**技术框架**：整体框架包含两个主要部分：1) 使用图像生成模型（如Nano Banana Pro）自动生成候选视觉问题，包括图像和嵌入的日语文本；2) 人工验证和调整生成的视觉问题，以确保其质量和难度。该流程迭代进行，直到生成足够数量的高质量测试样本。

**关键创新**：关键创新在于Vibe基准构建方法，该方法结合了图像生成模型的自动化能力和人工验证的质量控制，从而能够高效地构建大规模、高质量的视觉-文本融合理解基准。与传统的手动标注方法相比，Vibe方法大大降低了成本，并提高了基准构建的效率。

**关键设计**：Vibe方法的关键设计包括：1) 使用Nano Banana Pro等图像生成模型，该模型能够生成逼真的图像并嵌入清晰的日语文本；2) 设计清晰的提示语，指导图像生成模型生成符合要求的视觉问题；3) 建立严格的人工验证流程，包括对图像质量、文本清晰度、问题难度等方面的评估；4) 迭代优化提示语和验证流程，以提高基准构建的效率和质量。

## 📊 实验亮点

实验结果表明，现有的开源LMM在JMMMU-Pro基准测试上表现显著不足，这表明JMMMU-Pro是一个具有挑战性的基准，能够有效区分不同LMM的日语多模态理解能力。具体性能数据未知，但论文强调了所有开源模型都难以达到令人满意的水平，突显了该基准的价值。

## 🎯 应用场景

该研究成果可应用于评估和提升大型语言模型在日语多模态场景下的理解能力，尤其是在需要视觉-文本融合的复杂任务中。例如，可以用于开发更智能的日语图像搜索引擎、日语视觉辅助工具和日语多模态对话系统。此外，Vibe基准构建方法可以推广到其他语言和模态，为构建更广泛的多模态理解基准提供参考。

## 📄 摘要（原文）

> This paper introduces JMMMU-Pro, an image-based Japanese Multi-discipline Multimodal Understanding Benchmark, and Vibe Benchmark Construction, a scalable construction method. Following the evolution from MMMU to MMMU-Pro, JMMMU-Pro extends JMMMU by composing the question image and question text into a single image, thereby creating a benchmark that requires integrated visual-textual understanding through visual perception. To build JMMMU-Pro, we propose Vibe Benchmark Construction, a methodology in which an image generative model (e.g., Nano Banana Pro) produces candidate visual questions, and humans verify the outputs and, when necessary, regenerate with adjusted prompts to ensure quality. By leveraging Nano Banana Pro's highly realistic image generation capabilities and its ability to embed clean Japanese text, we construct a high-quality benchmark at low cost, covering a wide range of background and layout designs. Experimental results show that all open-source LMMs struggle substantially with JMMMU-Pro, underscoring JMMMU-Pro as an important benchmark for guiding future efforts in the open-source community. We believe that JMMMU-Pro provides a more rigorous evaluation tool for assessing the Japanese capabilities of LMMs and that our Vibe Benchmark Construction also offers an efficient guideline for future development of image-based VQA benchmarks.

