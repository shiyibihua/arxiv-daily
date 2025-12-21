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

**REGLUE：利用全局和局部语义增强潜在扩散模型，提升图像合成质量。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `潜在扩散模型` `图像合成` `视觉基础模型` `语义编码` `全局局部语义` `非线性压缩` `表征对齐`

## 📋 核心要点

1. 现有潜在扩散模型语义监督不足，高层语义学习缓慢，限制了图像生成质量和训练效率。
2. REGLUE通过联合建模VAE潜在变量、局部VFM语义和全局[CLS] token，实现全局-局部语义的统一编码。
3. 实验表明，REGLUE在ImageNet 256x256上显著提升了FID，并加速了收敛，优于现有方法。

## 📝 摘要（中文）

潜在扩散模型(LDMs)在图像合成方面取得了最先进的成果，但其重建式去噪目标仅提供间接的语义监督：高层语义出现缓慢，需要更长的训练时间，并限制了样本质量。最近的工作通过表征对齐从视觉基础模型(VFMs)外部注入语义，或者通过在扩散过程中联合建模VFM特征的一小部分来内部注入语义，未能充分利用可用的丰富、非线性、多层空间语义。我们引入了REGLUE（Representation Entanglement with Global-Local Unified Encoding），一个统一的潜在扩散框架，它在单个SiT骨干网络中联合建模(i)VAE图像潜在变量，(ii)紧凑的局部（patch级别）VFM语义，以及(iii)全局（图像级别）[CLS]token。一个轻量级的卷积语义压缩器将多层VFM特征非线性地聚合为低维、空间结构化的表示，并在扩散过程中与VAE潜在变量纠缠。外部对齐损失进一步将内部表示正则化到冻结的VFM目标。在ImageNet 256x256上，REGLUE始终优于SiT-B/2和SiT-XL/2基线，以及REPA、ReDi和REG，在FID指标上有所改进并加速了收敛。大量实验表明，(a)空间VFM语义至关重要，(b)非线性压缩是充分利用其优势的关键，以及(c)全局token和外部对齐在我们全局-局部-潜在联合建模框架中充当互补的、轻量级的增强。

## 🔬 方法详解

**问题定义**：现有潜在扩散模型在图像合成任务中，由于其重建式的去噪目标，语义信息的学习效率较低，导致生成图像质量受限，且需要更长的训练时间。现有方法要么未能充分利用视觉基础模型(VFM)提供的丰富语义信息，要么仅使用了VFM特征的有限部分，无法有效提升图像合成效果。

**核心思路**：REGLUE的核心思路是将VAE图像潜在变量、局部VFM语义和全局[CLS] token在一个统一的框架中进行联合建模。通过这种方式，模型能够同时学习图像的全局语义信息和局部细节信息，从而更有效地指导图像生成过程。利用轻量级的卷积语义压缩器，将多层VFM特征非线性地聚合为低维、空间结构化的表示，并将其与VAE潜在变量进行融合。

**技术框架**：REGLUE的整体框架包含以下几个主要模块：1) VAE编码器：将输入图像编码为潜在变量。2) VFM特征提取器：提取图像的局部和全局语义特征。3) 语义压缩器：将VFM特征压缩为低维表示。4) SiT骨干网络：用于联合建模VAE潜在变量、局部VFM语义和全局[CLS] token，并进行扩散过程。5) 外部对齐模块：通过外部对齐损失，正则化内部表示，使其与冻结的VFM目标对齐。

**关键创新**：REGLUE的关键创新在于其全局-局部语义的统一编码方式。通过同时建模VAE潜在变量、局部VFM语义和全局[CLS] token，模型能够更全面地理解图像内容，从而生成更高质量的图像。此外，非线性语义压缩器的设计也是一个重要的创新点，它能够有效地提取和压缩VFM特征，避免了信息冗余。

**关键设计**：REGLUE的关键设计包括：1) 使用SiT作为骨干网络，以实现高效的特征融合和扩散过程。2) 设计轻量级的卷积语义压缩器，以非线性方式聚合多层VFM特征。3) 引入外部对齐损失，以正则化内部表示，使其与VFM目标对齐。4) 使用全局[CLS] token，以捕捉图像的全局语义信息。具体参数设置和损失函数细节在论文中有详细描述，此处不再赘述。

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

实验结果表明，REGLUE在ImageNet 256x256数据集上显著提升了图像生成质量，FID指标优于SiT-B/2和SiT-XL/2基线，以及REPA、ReDi和REG等现有方法。此外，REGLUE还加速了训练过程的收敛，表明其具有更高的训练效率。实验还验证了空间VFM语义的重要性，以及非线性压缩对提升性能的关键作用。

## 🎯 应用场景

REGLUE在图像生成、图像编辑、图像修复等领域具有广泛的应用前景。它可以用于生成逼真度更高的图像，编辑图像内容，修复图像中的缺失部分。此外，REGLUE还可以应用于艺术创作、游戏开发、虚拟现实等领域，为这些领域带来更丰富的可能性。该研究的未来影响在于推动图像生成技术的发展，并为相关应用领域提供更强大的工具。

## 📄 摘要（原文）

> Latent diffusion models (LDMs) achieve state-of-the-art image synthesis, yet their reconstruction-style denoising objective provides only indirect semantic supervision: high-level semantics emerge slowly, requiring longer training and limiting sample quality. Recent works inject semantics from Vision Foundation Models (VFMs) either externally via representation alignment or internally by jointly modeling only a narrow slice of VFM features inside the diffusion process, under-utilizing the rich, nonlinear, multi-layer spatial semantics available. We introduce REGLUE (Representation Entanglement with Global-Local Unified Encoding), a unified latent diffusion framework that jointly models (i) VAE image latents, (ii) compact local (patch-level) VFM semantics, and (iii) a global (image-level) [CLS] token within a single SiT backbone. A lightweight convolutional semantic compressor nonlinearly aggregates multi-layer VFM features into a low-dimensional, spatially structured representation, which is entangled with the VAE latents in the diffusion process. An external alignment loss further regularizes internal representations toward frozen VFM targets. On ImageNet 256x256, REGLUE consistently improves FID and accelerates convergence over SiT-B/2 and SiT-XL/2 baselines, as well as over REPA, ReDi, and REG. Extensive experiments show that (a) spatial VFM semantics are crucial, (b) non-linear compression is key to unlocking their full benefit, and (c) global tokens and external alignment act as complementary, lightweight enhancements within our global-local-latent joint modeling framework. The code is available at https://github.com/giorgospets/reglue .

