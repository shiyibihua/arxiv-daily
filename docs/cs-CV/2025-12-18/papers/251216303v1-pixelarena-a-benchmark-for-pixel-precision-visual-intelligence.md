---
layout: default
title: PixelArena: A benchmark for Pixel-Precision Visual Intelligence
---

# PixelArena: A benchmark for Pixel-Precision Visual Intelligence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16303" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16303v1</a>
  <a href="https://arxiv.org/pdf/2512.16303.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16303v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16303v1', 'PixelArena: A benchmark for Pixel-Precision Visual Intelligence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Feng Liang, Sizhe Cheng, Chenqi Yi

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-18

**备注**: 7 pages, 11 figures, project page: https://pixelarena.reify.ing/project

---

## 💡 一句话要点

**PixelArena：提出像素级视觉智能评测基准，评估多模态大模型图像生成能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大模型` `图像生成` `语义分割` `视觉智能` `评测基准`

## 📋 核心要点

1. 现有图像生成评测侧重美学，缺乏对模型细粒度生成能力的客观评估。
2. PixelArena利用语义分割任务，以像素精度评估多模态大模型的图像生成智能。
3. 实验表明Gemini 3 Pro Image在零样本语义分割任务中表现出卓越的生成能力。

## 📝 摘要（中文）

本文提出了PixelArena，一个用于像素精度视觉智能的评测基准。随着具备图像输出能力的多模态大型语言模型不断涌现，现有的图像生成基准更多关注美学，而忽略了细粒度的生成能力。PixelArena利用语义分割任务，以客观地检验模型在像素级别的生成智能。研究发现，最新的Gemini 3 Pro Image在零样本设置下展现出卓越的图像生成能力，能够高保真地生成语义掩码，体现了前所未见的视觉智能以及在新图像生成任务中的真正泛化能力。进一步分析了实验结果，并与其他模型进行了定性和定量的比较，同时展示了失败案例。这些发现不仅标志着该领域令人兴奋的进展，也为多模态、推理、可解释性和基准测试等相关领域的未来研究提供了见解。

## 🔬 方法详解

**问题定义**：现有图像生成基准主要关注生成图像的美学质量，缺乏对模型在像素级别上理解和生成图像细节能力的评估。这使得我们难以客观地衡量多模态大模型在细粒度图像生成方面的智能水平，阻碍了相关技术的发展。

**核心思路**：PixelArena的核心思路是利用语义分割任务作为评估多模态大模型图像生成能力的标准。语义分割需要模型理解图像中每个像素的语义信息，并准确地将其划分到不同的类别中。通过评估模型生成的语义分割结果的准确性，可以客观地衡量其在像素级别上的视觉智能。

**技术框架**：PixelArena基准测试主要包含以下几个阶段：1) 输入图像和相应的语义分割任务描述；2) 多模态大模型根据输入生成语义分割掩码；3) 将生成的掩码与真实标签进行比较，计算评估指标，如像素精度和平均交并比（mIoU）。整个流程旨在量化模型在理解和生成像素级细节方面的能力。

**关键创新**：PixelArena的关键创新在于它将语义分割任务引入到多模态大模型的图像生成能力评估中。与传统的图像生成基准不同，PixelArena关注的是模型对图像内容的理解和精确生成能力，而不仅仅是生成图像的美观程度。这使得PixelArena能够更全面、客观地评估多模态大模型的视觉智能。

**关键设计**：PixelArena的关键设计包括：1) 选择合适的语义分割数据集，例如包含丰富场景和对象的Cityscapes或ADE20K；2) 设计清晰明确的任务描述，指导模型生成准确的语义分割掩码；3) 采用标准的语义分割评估指标，如像素精度和mIoU，以量化模型生成的掩码的准确性；4) 针对不同类型的多模态大模型，设计合理的输入格式和提示语，以充分发挥模型的生成能力。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16303v1/images/celeb/label-color-palette.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16303v1/images/celeb/model-comparison-celeb.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16303v1/images/celeb/best-f1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Gemini 3 Pro Image在零样本语义分割任务中表现出卓越的生成能力，能够高保真地生成语义掩码。相较于其他模型，Gemini 3 Pro Image在像素精度和平均交并比（mIoU）等指标上均取得了显著提升，展现了其强大的视觉智能和泛化能力。

## 🎯 应用场景

PixelArena可应用于评估和提升多模态大模型在图像生成、图像编辑、机器人视觉等领域的性能。通过客观评估模型在像素级别的理解和生成能力，可以推动模型在自动驾驶、医疗影像分析、遥感图像处理等实际应用中的发展，并促进更智能、更可靠的视觉系统的构建。

## 📄 摘要（原文）

> Multi-modal large language models that have image output are emerging. Many image generation benchmarks focus on aesthetics instead of fine-grained generation capabilities. In PixelArena, we propose using semantic segmentation tasks to objectively examine their fine-grained generative intelligence with pixel precision. We find the latest Gemini 3 Pro Image has emergent image generation capabilities that generate semantic masks with high fidelity under zero-shot settings, showcasing visual intelligence unseen before and true generalization in new image generation tasks. We further investigate its results, compare them qualitatively and quantitatively with those of other models, and present failure cases. The findings not only signal exciting progress in the field but also provide insights into future research related to multimodality, reasoning, interpretability and benchmarking.

