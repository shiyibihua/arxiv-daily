---
layout: default
title: Rethinking Garment Conditioning in Diffusion-based Virtual Try-On
---

# Rethinking Garment Conditioning in Diffusion-based Virtual Try-On

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.18775" target="_blank" class="toolbar-btn">arXiv: 2511.18775v1</a>
    <a href="https://arxiv.org/pdf/2511.18775.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18775v1" 
            onclick="toggleFavorite(this, '2511.18775v1', 'Rethinking Garment Conditioning in Diffusion-based Virtual Try-On')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Kihyun Na, Jinyoung Choi, Injung Kim

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-24

**备注**: 15 pages (including references and supplementary material), 10 figures, 7 tables. Code and pretrained models will be released

---

## 💡 一句话要点

**提出Re-CatVTON，高效单UNet扩散模型实现高性能虚拟试穿**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `虚拟试穿` `扩散模型` `单UNet` `上下文特征学习` `无分类器引导` `图像合成` `深度学习`

## 📋 核心要点

1. 现有基于扩散模型的虚拟试穿方法，特别是双UNet结构，虽然效果好，但计算和内存开销巨大。
2. 论文提出Re-CatVTON，一个高效的单UNet模型，通过优化上下文特征学习和改进引导策略，提升性能。
3. 实验结果表明，Re-CatVTON在FID、KID和LPIPS指标上优于现有单UNet模型，并在效率上优于双UNet模型。

## 📝 摘要（中文）

虚拟试穿(VTON)旨在合成给定人物图像和服装图像条件下，人物穿着目标服装的图像。基于扩散模型的VTON模型，特别是采用双UNet架构的模型，相比单UNet模型展现出更高的图像保真度，但其庞大的结构导致了显著的计算和内存开销。本研究通过可视化分析和理论分析，推导了关于学习上下文特征以调节去噪过程的三个假设。基于这些假设，我们开发了Re-CatVTON，一个高效的单UNet模型，实现了高性能。我们进一步通过引入针对VTON空间拼接条件的改进的无分类器引导策略，以及直接注入从干净服装潜在变量导出的真实服装潜在变量以防止预测误差累积，来增强模型。所提出的Re-CatVTON相比其前身(CatVTON)显著提高了性能，并且比高性能双UNet模型Leffa需要更少的计算和内存。我们的结果表明，FID、KID和LPIPS分数有所提高，而SSIM略有下降，为单UNet VTON模型建立了一种新的效率-性能权衡。

## 🔬 方法详解

**问题定义**：论文旨在解决虚拟试穿任务中，基于扩散模型的双UNet结构计算和内存开销过大的问题。现有方法虽然能生成高质量的试穿图像，但其复杂的网络结构限制了其在资源受限场景下的应用。因此，需要设计一种更高效的虚拟试穿模型，在保证生成质量的同时，降低计算成本。

**核心思路**：论文的核心思路是通过深入分析上下文特征的学习过程，并基于分析结果设计更有效的网络结构和训练策略，从而在单UNet结构下实现与双UNet结构相媲美的性能。具体来说，论文提出了关于上下文特征学习的三个假设，并基于这些假设设计了Re-CatVTON模型。

**技术框架**：Re-CatVTON基于单UNet架构，整体流程如下：首先，将人物图像和服装图像进行空间拼接，作为UNet的输入。然后，UNet进行去噪过程，逐步生成试穿图像。为了提升性能，论文还引入了改进的无分类器引导策略和直接注入真实服装潜在变量的方法。

**关键创新**：论文的关键创新点在于：1) 基于可视化和理论分析，提出了关于上下文特征学习的三个假设。2) 基于这些假设，设计了Re-CatVTON模型，该模型在单UNet结构下实现了高性能。3) 提出了针对VTON空间拼接条件的改进的无分类器引导策略。4) 提出了直接注入真实服装潜在变量的方法，以防止预测误差累积。

**关键设计**：论文的关键设计包括：1) 网络结构：采用单UNet结构，并针对VTON任务进行了优化。2) 损失函数：采用标准的扩散模型损失函数。3) 训练策略：采用了改进的无分类器引导策略和直接注入真实服装潜在变量的方法。4) 参数设置：具体参数设置在论文中有详细描述，这里不再赘述。

## 📊 实验亮点

Re-CatVTON在虚拟试穿任务上取得了显著的性能提升，在FID、KID和LPIPS指标上优于其前身CatVTON，并且在计算效率上优于高性能双UNet模型Leffa。具体来说，Re-CatVTON在保证SSIM指标略微下降的情况下，显著降低了计算和内存开销，为单UNet VTON模型建立了一种新的效率-性能权衡。

## 🎯 应用场景

该研究成果可应用于在线购物、虚拟试衣间等领域，帮助用户更直观地了解服装的上身效果，提升购物体验。此外，该技术还可以应用于游戏、社交媒体等领域，为用户提供个性化的虚拟形象定制服务。未来，该研究可以进一步扩展到更复杂的服装类型和人体姿态，实现更逼真的虚拟试穿效果。

## 📄 摘要（原文）

> Virtual Try-On (VTON) is the task of synthesizing an image of a person wearing a target garment, conditioned on a person image and a garment image. While diffusion-based VTON models featuring a Dual UNet architecture demonstrate superior fidelity compared to single UNet models, they incur substantial computational and memory overhead due to their heavy structure. In this study, through visualization analysis and theoretical analysis, we derived three hypotheses regarding the learning of context features to condition the denoising process. Based on these hypotheses, we developed Re-CatVTON, an efficient single UNet model that achieves high performance. We further enhance the model by introducing a modified classifier-free guidance strategy tailored for VTON's spatial concatenation conditioning, and by directly injecting the ground-truth garment latent derived from the clean garment latent to prevent the accumulation of prediction error. The proposed Re-CatVTON significantly improves performance compared to its predecessor (CatVTON) and requires less computation and memory than the high-performance Dual UNet model, Leffa. Our results demonstrate improved FID, KID, and LPIPS scores, with only a marginal decrease in SSIM, establishing a new efficiency-performance trade-off for single UNet VTON models.

