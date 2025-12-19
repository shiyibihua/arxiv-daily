---
layout: default
title: REGLUE Your Latents with Global and Local Semantics for Entangled Diffusion
---

# REGLUE Your Latents with Global and Local Semantics for Entangled Diffusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16636" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16636v1</a>
  <a href="https://arxiv.org/pdf/2512.16636.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16636v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16636v1', 'REGLUE Your Latents with Global and Local Semantics for Entangled Diffusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Giorgos Petsangourakis, Christos Sgouropoulos, Bill Psomas, Theodoros Giannakopoulos, Giorgos Sfikas, Ioannis Kakogeorgiou

**分类**: cs.CV

**发布日期**: 2025-12-18

**🔗 代码/项目**: [GITHUB](https://github.com/giorgospets/reglue)

---

## 💡 一句话要点

**REGLUE：融合全局与局部语义的解耦扩散模型，提升图像合成质量与收敛速度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `潜在扩散模型` `图像合成` `视觉基础模型` `语义融合` `全局局部语义`

## 📋 核心要点

1. 现有潜在扩散模型语义监督不足，导致训练缓慢和样本质量受限，未能充分利用视觉基础模型(VFMs)的丰富语义信息。
2. REGLUE通过联合建模VAE潜在变量、局部VFM语义和全局[CLS] token，在扩散过程中融合全局和局部语义信息，实现更有效的语义监督。
3. 实验表明，REGLUE在ImageNet 256x256上显著提升了FID，并加速了收敛速度，优于现有方法，验证了空间VFM语义和非线性压缩的重要性。

## 📝 摘要（中文）

潜在扩散模型(LDMs)在图像合成方面取得了最先进的成果，但其重建式去噪目标仅提供间接的语义监督：高层语义出现缓慢，需要更长的训练时间，并限制了样本质量。现有工作通过表征对齐从视觉基础模型(VFMs)外部注入语义，或者仅在扩散过程中对VFM特征的一小部分进行联合建模，未能充分利用可用的丰富、非线性、多层空间语义。我们提出了REGLUE（Representation Entanglement with Global-Local Unified Encoding），一个统一的潜在扩散框架，它在单个SiT骨干网络中联合建模(i)VAE图像潜在变量，(ii)紧凑的局部(patch级别)VFM语义，以及(iii)全局(图像级别)[CLS]token。一个轻量级的卷积语义压缩器将多层VFM特征非线性地聚合为低维、空间结构化的表示，并在扩散过程中与VAE潜在变量纠缠。外部对齐损失进一步将内部表示正则化到冻结的VFM目标。在ImageNet 256x256上，REGLUE始终如一地提高了FID，并加速了SiT-B/2和SiT-XL/2基线以及REPA、ReDi和REG的收敛速度。大量实验表明，(a)空间VFM语义至关重要，(b)非线性压缩是充分发挥其优势的关键，以及(c)全局token和外部对齐在我们全局-局部-潜在联合建模框架中充当互补的、轻量级的增强。

## 🔬 方法详解

**问题定义**：现有潜在扩散模型在图像合成任务中，依赖重建式的去噪目标进行训练，这种方式提供的语义监督是间接的，导致模型学习高层语义的速度较慢，需要更长的训练时间和更大的计算资源。此外，现有方法未能充分利用视觉基础模型（VFMs）中蕴含的丰富、非线性、多层空间语义信息，限制了生成图像的质量。

**核心思路**：REGLUE的核心思路是通过联合建模VAE图像潜在变量、局部（patch级别）VFM语义和全局（图像级别）[CLS] token，在扩散过程中显式地注入全局和局部语义信息，从而增强模型的语义理解能力，加速训练过程，并提升生成图像的质量。这种联合建模的方式允许模型更好地利用VFM提供的多层次语义信息，从而生成更逼真、更符合语义的图像。

**技术框架**：REGLUE的整体框架包含以下几个主要模块：1) VAE编码器：将输入图像编码为潜在变量。2) 视觉基础模型（VFM）：提取图像的局部（patch级别）和全局（图像级别）语义特征。3) 语义压缩器：使用轻量级的卷积神经网络将多层VFM特征非线性地压缩为低维、空间结构化的表示。4) SiT骨干网络：作为扩散模型的去噪器，联合建模VAE潜在变量、压缩后的局部VFM语义和全局[CLS] token。5) 外部对齐损失：正则化内部表示，使其与冻结的VFM目标对齐。

**关键创新**：REGLUE的关键创新在于其全局-局部-潜在联合建模框架，该框架能够有效地融合来自视觉基础模型的全局和局部语义信息，并将其注入到扩散过程中。此外，使用非线性语义压缩器来处理VFM特征也是一个重要的创新点，它可以有效地降低VFM特征的维度，并保留关键的语义信息。

**关键设计**：REGLUE的关键设计包括：1) 使用轻量级的卷积神经网络作为语义压缩器，以降低计算成本。2) 使用SiT（未知）作为扩散模型的骨干网络，以提高模型的表达能力。3) 使用外部对齐损失来正则化内部表示，使其与VFM目标对齐，从而进一步提高生成图像的质量。具体参数设置和损失函数细节在论文中未明确说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16636v1/figs/training_steps_photos/50k_steps/000343.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16636v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16636v1/figs/cfg/golden_retriever_207/000444.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

REGLUE在ImageNet 256x256数据集上的实验结果表明，该方法能够显著提升FID指标，并加速收敛速度。与SiT-B/2和SiT-XL/2基线相比，REGLUE取得了明显的性能提升。此外，REGLUE还优于REPA、ReDi和REG等现有方法，验证了其有效性。实验结果还表明，空间VFM语义和非线性压缩是提升性能的关键因素。

## 🎯 应用场景

REGLUE具有广泛的应用前景，包括图像生成、图像编辑、图像修复、视频生成等领域。该方法可以用于生成高质量、高逼真度的图像和视频内容，例如用于游戏开发、电影制作、广告设计等。此外，REGLUE还可以应用于医学图像分析、遥感图像处理等领域，为这些领域提供更准确、更可靠的图像分析结果。

## 📄 摘要（原文）

> Latent diffusion models (LDMs) achieve state-of-the-art image synthesis, yet their reconstruction-style denoising objective provides only indirect semantic supervision: high-level semantics emerge slowly, requiring longer training and limiting sample quality. Recent works inject semantics from Vision Foundation Models (VFMs) either externally via representation alignment or internally by jointly modeling only a narrow slice of VFM features inside the diffusion process, under-utilizing the rich, nonlinear, multi-layer spatial semantics available. We introduce REGLUE (Representation Entanglement with Global-Local Unified Encoding), a unified latent diffusion framework that jointly models (i) VAE image latents, (ii) compact local (patch-level) VFM semantics, and (iii) a global (image-level) [CLS] token within a single SiT backbone. A lightweight convolutional semantic compressor nonlinearly aggregates multi-layer VFM features into a low-dimensional, spatially structured representation, which is entangled with the VAE latents in the diffusion process. An external alignment loss further regularizes internal representations toward frozen VFM targets. On ImageNet 256x256, REGLUE consistently improves FID and accelerates convergence over SiT-B/2 and SiT-XL/2 baselines, as well as over REPA, ReDi, and REG. Extensive experiments show that (a) spatial VFM semantics are crucial, (b) non-linear compression is key to unlocking their full benefit, and (c) global tokens and external alignment act as complementary, lightweight enhancements within our global-local-latent joint modeling framework. The code is available at https://github.com/giorgospets/reglue .

