---
layout: default
title: Free Lunch Alignment of Text-to-Image Diffusion Models without Preference Image Pairs
---

# Free Lunch Alignment of Text-to-Image Diffusion Models without Preference Image Pairs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25771" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25771v1</a>
  <a href="https://arxiv.org/pdf/2509.25771.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25771v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25771v1', 'Free Lunch Alignment of Text-to-Image Diffusion Models without Preference Image Pairs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jia Jun Cheng Xian, Muchen Li, Haotian Yang, Xin Tao, Pengfei Wan, Leonid Sigal, Renjie Liao

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-30

**🔗 代码/项目**: [GITHUB](https://github.com/DSL-Lab/T2I-Free-Lunch-Alignment)

---

## 💡 一句话要点

**提出文本偏好优化（TPO），实现文本到图像扩散模型的免标注对齐。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到图像生成` `扩散模型` `文本偏好优化` `无监督对齐` `大型语言模型`

## 📋 核心要点

1. 现有文本到图像模型依赖人工标注的图像偏好数据进行对齐，成本高昂且限制了模型扩展。
2. TPO通过训练模型区分匹配和不匹配的文本提示，无需图像偏好数据即可实现模型对齐。
3. 实验表明，TPO框架下的TDPO和TKTO方法在多个基准测试中均优于原始DPO和KTO。

## 📝 摘要（中文）

扩散模型的文本到图像（T2I）生成取得了显著进展，但文本与生成图像的对齐仍然是一个挑战。现有方法通常采用强化学习与人类反馈（RLHF），依赖图像偏好数据或学习奖励函数，需要大量昂贵的人工标注，限制了可扩展性。本文提出了文本偏好优化（TPO）框架，无需成对图像偏好数据即可实现T2I模型的“免费午餐”对齐。TPO通过训练模型偏好匹配的提示而非不匹配的提示来实现对齐，不匹配的提示由大型语言模型扰动原始标题生成。该框架具有通用性，可与现有基于偏好的算法兼容。我们将DPO和KTO扩展到我们的设置，分别得到TDPO和TKTO。在多个基准测试上的定量和定性评估表明，我们的方法始终优于其原始对应方法，提供更好的人类偏好分数和改进的文本到图像对齐。

## 🔬 方法详解

**问题定义**：现有文本到图像扩散模型在文本和图像对齐方面存在挑战，需要借助强化学习和人类反馈（RLHF）进行优化。然而，RLHF方法依赖于大量人工标注的图像偏好数据，成本高昂，难以扩展到更大规模的数据集和模型。因此，如何在没有人工标注的情况下实现文本到图像模型的对齐是一个关键问题。

**核心思路**：本文的核心思路是利用文本信息本身作为监督信号，训练模型区分匹配和不匹配的文本提示。具体来说，对于给定的图像，模型应该更偏好与其原始文本描述相匹配的提示，而不是经过扰动后不匹配的提示。通过这种方式，模型可以学习到文本和图像之间的对应关系，从而实现对齐。

**技术框架**：TPO框架主要包含以下几个步骤：1) 使用大型语言模型（LLM）对原始文本提示进行扰动，生成不匹配的提示。2) 将原始提示和扰动后的提示输入到文本到图像扩散模型中，生成对应的图像。3) 使用偏好优化算法（如DPO或KTO）训练模型，使其偏好与原始提示对应的图像，而非与扰动提示对应的图像。4) 将DPO和KTO扩展到TPO框架，分别得到TDPO和TKTO。

**关键创新**：TPO的关键创新在于利用文本信息本身作为监督信号，避免了对人工标注的图像偏好数据的依赖，实现了“免费午餐”式的文本到图像模型对齐。与传统的RLHF方法相比，TPO具有更强的可扩展性和更低的成本。

**关键设计**：在TPO框架中，关键的设计包括：1) 如何使用LLM生成高质量的不匹配提示，以保证训练的有效性。2) 如何选择合适的偏好优化算法（如DPO或KTO），以实现最佳的对齐效果。3) 如何平衡原始提示和扰动提示之间的偏好强度，以避免模型过度拟合。

## 📊 实验亮点

实验结果表明，TPO框架下的TDPO和TKTO方法在多个基准测试中均优于原始DPO和KTO。例如，在Human Preference Score指标上，TDPO和TKTO相比DPO和KTO分别提升了X%和Y%（具体数据论文中给出）。这些结果表明，TPO能够有效提高文本到图像模型的对齐程度，并生成更符合人类偏好的图像。

## 🎯 应用场景

该研究成果可广泛应用于各种文本到图像生成场景，例如图像编辑、内容创作、虚拟现实等。通过提高文本和图像之间的对齐程度，可以生成更符合用户意图、更具创意和更高质量的图像内容。此外，该方法无需人工标注，降低了模型训练的成本，有利于推动文本到图像生成技术的普及和应用。

## 📄 摘要（原文）

> Recent advances in diffusion-based text-to-image (T2I) models have led to remarkable success in generating high-quality images from textual prompts. However, ensuring accurate alignment between the text and the generated image remains a significant challenge for state-of-the-art diffusion models. To address this, existing studies employ reinforcement learning with human feedback (RLHF) to align T2I outputs with human preferences. These methods, however, either rely directly on paired image preference data or require a learned reward function, both of which depend heavily on costly, high-quality human annotations and thus face scalability limitations. In this work, we introduce Text Preference Optimization (TPO), a framework that enables "free-lunch" alignment of T2I models, achieving alignment without the need for paired image preference data. TPO works by training the model to prefer matched prompts over mismatched prompts, which are constructed by perturbing original captions using a large language model. Our framework is general and compatible with existing preference-based algorithms. We extend both DPO and KTO to our setting, resulting in TDPO and TKTO. Quantitative and qualitative evaluations across multiple benchmarks show that our methods consistently outperform their original counterparts, delivering better human preference scores and improved text-to-image alignment. Our Open-source code is available at https://github.com/DSL-Lab/T2I-Free-Lunch-Alignment.

