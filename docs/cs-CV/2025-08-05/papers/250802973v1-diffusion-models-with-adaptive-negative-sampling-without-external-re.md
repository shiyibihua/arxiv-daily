---
layout: default
title: Diffusion Models with Adaptive Negative Sampling Without External Resources
---

# Diffusion Models with Adaptive Negative Sampling Without External Resources

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02973" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02973v1</a>
  <a href="https://arxiv.org/pdf/2508.02973.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02973v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02973v1', 'Diffusion Models with Adaptive Negative Sampling Without External Resources')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alakh Desai, Nuno Vasconcelos

**分类**: cs.CV

**发布日期**: 2025-08-05

---

## 💡 一句话要点

**提出自适应负采样方法以提升扩散模型的图像生成质量**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `扩散模型` `负采样` `图像生成` `无分类器引导` `自然语言处理` `计算机视觉`

## 📋 核心要点

1. 现有扩散模型在生成图像时，提示遵循性和图像质量存在显著差异，影响了生成效果。
2. 本文提出自适应负采样方法（ANSWER），通过结合正负条件，提升图像生成的提示一致性。
3. 实验结果显示，ANSWER在多个基准测试中超越了现有方法，且人类偏好度提高了两倍。

## 📝 摘要（中文）

扩散模型（DMs）在根据文本提示生成多样化和高保真图像方面表现出色，但在提示遵循性和质量上存在显著差异。为改善这一问题，负提示被引入以指定图像中不应包含的内容。本文探讨了负提示与无分类器引导（CFG）之间的关系，提出了一种名为自适应负采样无外部资源（ANSWER）的采样程序，该程序利用扩散模型对否定的内部理解，增强生成图像与提示的一致性。ANSWER是一种无训练的技术，适用于任何支持CFG的模型，能够在没有显式负提示的情况下实现图像概念的负向基础。实验表明，将ANSWER应用于现有DMs在多个基准测试中优于基线，并且被人类偏好程度提高了2倍。

## 🔬 方法详解

**问题定义**：本文旨在解决扩散模型在图像生成过程中提示遵循性和质量不一致的问题。现有方法在使用负提示时，往往依赖外部资源，导致信息损失和不完整性。

**核心思路**：提出的ANSWER方法通过结合正负条件，利用扩散模型对否定的内部理解，增强生成图像与提示的一致性，避免了显式负提示的不足。

**技术框架**：ANSWER方法的整体框架包括从单一提示中提取正负条件，利用无分类器引导（CFG）进行图像生成。该方法不需要额外的训练过程，适用于多种扩散模型。

**关键创新**：最重要的创新在于提出了一种无训练的自适应负采样技术，能够在没有显式负提示的情况下实现图像概念的负向基础，这与现有方法的依赖外部资源形成鲜明对比。

**关键设计**：在设计中，ANSWER方法通过调整采样策略和优化生成过程中的正负条件，确保生成图像更符合提示要求，具体的参数设置和损失函数设计未在摘要中详细说明。

## 📊 实验亮点

实验结果表明，添加ANSWER方法的扩散模型在多个基准测试中表现优于现有基线，具体性能提升幅度达到显著水平。此外，用户偏好调查显示，使用ANSWER生成的图像被人类偏好程度提高了两倍，验证了其有效性。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在图像生成、计算机视觉和自然语言处理等领域。通过提高扩散模型的提示遵循性，ANSWER方法可以在艺术创作、广告设计和虚拟现实等场景中实现更高质量的图像生成，推动相关技术的发展和应用。

## 📄 摘要（原文）

> Diffusion models (DMs) have demonstrated an unparalleled ability to create diverse and high-fidelity images from text prompts. However, they are also well-known to vary substantially regarding both prompt adherence and quality. Negative prompting was introduced to improve prompt compliance by specifying what an image must not contain. Previous works have shown the existence of an ideal negative prompt that can maximize the odds of the positive prompt. In this work, we explore relations between negative prompting and classifier-free guidance (CFG) to develop a sampling procedure, {\it Adaptive Negative Sampling Without External Resources} (ANSWER), that accounts for both positive and negative conditions from a single prompt. This leverages the internal understanding of negation by the diffusion model to increase the odds of generating images faithful to the prompt. ANSWER is a training-free technique, applicable to any model that supports CFG, and allows for negative grounding of image concepts without an explicit negative prompts, which are lossy and incomplete. Experiments show that adding ANSWER to existing DMs outperforms the baselines on multiple benchmarks and is preferred by humans 2x more over the other methods.

