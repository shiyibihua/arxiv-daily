---
layout: default
title: Parameter-Efficient Adaptation of mPLUG-Owl2 via Pixel-Level Visual Prompts for NR-IQA
---

# Parameter-Efficient Adaptation of mPLUG-Owl2 via Pixel-Level Visual Prompts for NR-IQA

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03494" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03494v2</a>
  <a href="https://arxiv.org/pdf/2509.03494.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03494v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03494v2', 'Parameter-Efficient Adaptation of mPLUG-Owl2 via Pixel-Level Visual Prompts for NR-IQA')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yahya Benmahane, Mohammed El Hassouni

**分类**: cs.CV

**发布日期**: 2025-09-03 (更新: 2025-09-06)

---

## 💡 一句话要点

**提出基于像素级视觉提示的mPLUG-Owl2参数高效微调方法，用于无参考图像质量评估**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无参考图像质量评估` `视觉提示` `参数高效微调` `多模态大语言模型` `mPLUG-Owl2`

## 📋 核心要点

1. 现有NR-IQA方法通常需要大量参数微调，计算成本高昂，难以适应资源受限场景。
2. 该论文提出利用像素级视觉提示，仅需训练少量参数即可有效调整mPLUG-Owl2模型。
3. 实验表明，该方法在多个数据集上取得了与全参数微调方法相当甚至更优的性能。

## 📝 摘要（中文）

本文提出了一种新颖的参数高效的无参考图像质量评估（NR-IQA）自适应方法，该方法使用在像素空间中优化的视觉提示。与多模态大型语言模型（MLLM）的完全微调不同，我们的方法最多仅训练60万个参数（<0.01%的基础模型），同时保持底层模型完全冻结。在推理过程中，这些视觉提示通过加法与图像结合，并通过mPLUG-Owl2处理，文本查询为“评估图像的技术质量”。在KADID-10k、KonIQ-10k和AGIQA-3k上对失真类型（合成、真实、AI生成）的评估表明，与完全微调方法和专门的NR-IQA模型相比，该方法具有竞争力的性能，在KADID-10k上实现了0.93的SRCC。据我们所知，这是第一项利用像素空间视觉提示进行NR-IQA的工作，从而实现了MLLM对低级视觉任务的有效适应。源代码可在https://github.com/yahya-ben/mplug2-vp-for-nriqa公开获取。

## 🔬 方法详解

**问题定义**：论文旨在解决无参考图像质量评估（NR-IQA）任务中，现有方法参数量大、计算成本高的问题。传统方法通常需要对整个模型进行微调，这在计算资源有限的情况下是不可行的。此外，现有方法可能难以泛化到不同类型的图像失真上。

**核心思路**：论文的核心思路是利用视觉提示（Visual Prompts）来引导预训练的多模态大语言模型（MLLM）进行NR-IQA。通过在像素空间中优化这些视觉提示，可以在不修改底层模型参数的情况下，使模型适应特定的任务。这种方法显著降低了计算成本，并提高了模型的泛化能力。

**技术框架**：整体框架包括以下几个步骤：1) 输入图像与优化的视觉提示进行像素级别的加法融合。2) 将融合后的图像输入到冻结的mPLUG-Owl2模型中。3) 使用文本查询“评估图像的技术质量”作为模型的输入。4) 模型输出图像质量评分。整个过程中，只有视觉提示的参数被训练，而mPLUG-Owl2模型的参数保持不变。

**关键创新**：该论文的关键创新在于首次将像素空间视觉提示应用于NR-IQA任务。与传统的特征空间提示相比，像素空间提示更直接地作用于输入图像，能够更好地捕捉图像的低级视觉特征。此外，该方法实现了参数高效的MLLM自适应，仅需训练少量参数即可达到与全参数微调相当的性能。

**关键设计**：视觉提示被设计为与输入图像尺寸相同的可学习参数矩阵。训练过程中，使用均方误差（MSE）损失函数来优化视觉提示，目标是使模型的输出评分与真实评分之间的差距最小化。mPLUG-Owl2模型采用冻结策略，以保证参数效率。实验中，视觉提示的参数量被限制在600K以内，仅占基础模型的0.01%。

## 📊 实验亮点

该方法在KADID-10k数据集上实现了0.93的SRCC，与全参数微调方法和专门的NR-IQA模型相比，具有竞争力的性能。该方法仅训练600K参数，远小于基础模型的参数量，实现了参数高效的MLLM自适应。实验结果表明，该方法在合成、真实和AI生成的图像上均表现良好，具有较强的泛化能力。

## 🎯 应用场景

该研究成果可应用于图像质量监控、图像增强算法评估、图像压缩算法优化等领域。通过高效的图像质量评估，可以提升用户体验，优化图像处理流程，并为AI生成图像的质量控制提供技术支持。未来，该方法有望扩展到其他低级视觉任务，例如图像去噪、图像超分辨率等。

## 📄 摘要（原文）

> In this paper, we propose a novel parameter-efficient adaptation method for No- Reference Image Quality Assessment (NR-IQA) using visual prompts optimized in pixel-space. Unlike full fine-tuning of Multimodal Large Language Models (MLLMs), our approach trains only 600K parameters at most (< 0.01% of the base model), while keeping the underlying model fully frozen. During inference, these visual prompts are combined with images via addition and processed by mPLUG-Owl2 with the textual query "Rate the technical quality of the image." Evaluations across distortion types (synthetic, realistic, AI-generated) on KADID- 10k, KonIQ-10k, and AGIQA-3k demonstrate competitive performance against full finetuned methods and specialized NR-IQA models, achieving 0.93 SRCC on KADID-10k. To our knowledge, this is the first work to leverage pixel-space visual prompts for NR-IQA, enabling efficient MLLM adaptation for low-level vision tasks. The source code is publicly available at https: // github. com/ yahya-ben/ mplug2-vp-for-nriqa.

