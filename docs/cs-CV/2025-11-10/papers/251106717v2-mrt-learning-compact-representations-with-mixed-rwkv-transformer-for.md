---
layout: default
title: MRT: Learning Compact Representations with Mixed RWKV-Transformer for Extreme Image Compression
---

# MRT: Learning Compact Representations with Mixed RWKV-Transformer for Extreme Image Compression

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.06717" target="_blank" class="toolbar-btn">arXiv: 2511.06717v2</a>
    <a href="https://arxiv.org/pdf/2511.06717.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.06717v2" 
            onclick="toggleFavorite(this, '2511.06717v2', 'MRT: Learning Compact Representations with Mixed RWKV-Transformer for Extreme Image Compression')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Han Liu, Hengyu Man, Xingtao Wang, Wenrui Li, Debin Zhao

**分类**: cs.CV

**发布日期**: 2025-11-10 (更新: 2025-11-14)

---

## 💡 一句话要点

**提出混合RWKV-Transformer的MRT模型，用于极低码率图像压缩，显著提升压缩性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `图像压缩` `极低码率` `RWKV` `Transformer` `混合架构` `表示学习` `全局依赖` `局部冗余`

## 📋 核心要点

1. 现有极低码率图像压缩方法依赖CNN或Swin Transformer，在2D潜在空间中压缩图像，空间冗余大，限制了压缩性能。
2. 提出混合RWKV-Transformer (MRT) 架构，将图像编码为更紧凑的1维潜在表示，利用RWKV捕获全局依赖，Transformer建模局部冗余。
3. 实验表明，MRT在极低码率下实现了卓越的重建质量，显著优于现有方法，在Kodak和CLIC2020数据集上实现了显著的比特率节省。

## 📝 摘要（中文）

本文提出了一种新颖的混合RWKV-Transformer (MRT) 架构，旨在通过协同整合线性注意力RWKV和自注意力Transformer模型的互补优势，将图像编码为更紧凑的1维潜在表示，从而提升极低码率图像压缩的性能。MRT将图像分割成固定大小的窗口，利用RWKV模块捕获窗口间的全局依赖关系，并使用Transformer块建模每个窗口内的局部冗余。这种分层注意力机制能够在1维域中实现更高效和紧凑的表示学习。为了进一步提高压缩效率，本文还引入了专门为MRT中间1维潜在特征的结构特性量身定制的RWKV压缩模型 (RCM)。在标准图像压缩基准上的大量实验验证了该方法的有效性。所提出的MRT框架在低于0.02 bpp的比特率下始终如一地实现了卓越的重建质量。基于DISTS指标的定量结果表明，MRT显著优于最先进的2维架构GLC，在Kodak和CLIC2020测试数据集上分别实现了43.75%和30.59%的比特率节省。

## 🔬 方法详解

**问题定义**：现有极低码率图像压缩方法，如基于CNN或Swin Transformer的方法，通常将图像压缩到2D潜在空间中。这些方法倾向于保留大量的空间冗余，从而限制了整体压缩性能。因此，如何设计一种能够更有效地去除空间冗余，生成更紧凑的图像表示的模型，是极低码率图像压缩的关键挑战。

**核心思路**：本文的核心思路是利用RWKV和Transformer的互补优势，设计一种混合架构（MRT），将图像编码为更紧凑的1维潜在表示。RWKV擅长捕获长距离依赖关系，而Transformer擅长建模局部冗余。通过将两者结合，可以更有效地去除图像中的空间冗余，从而提高压缩性能。将2D图像转化为1D序列，更利于RWKV建模全局信息。

**技术框架**：MRT框架主要包含以下几个步骤：1) 将输入图像分割成固定大小的窗口；2) 使用RWKV模块捕获窗口之间的全局依赖关系；3) 使用Transformer块建模每个窗口内的局部冗余；4) 使用RWKV压缩模型 (RCM) 对中间1维潜在特征进行压缩。整体流程是从图像像素到1D潜在表示的编码，再到压缩，最后解码重建图像。

**关键创新**：MRT的关键创新在于混合使用了RWKV和Transformer，并将其应用于图像压缩的1D潜在表示学习中。与传统的2D压缩方法相比，MRT能够更有效地去除空间冗余，生成更紧凑的图像表示。此外，RCM的设计也针对MRT的中间特征进行了优化，进一步提高了压缩效率。

**关键设计**：MRT的关键设计包括：1) 窗口大小的选择，需要平衡局部和全局信息的建模；2) RWKV和Transformer模块的层数和参数设置，需要根据具体任务进行调整；3) RCM的结构设计，需要与MRT的中间特征相匹配；4) 损失函数的设计，需要平衡重建质量和压缩率。具体参数设置和损失函数细节在论文中进行了详细描述（摘要未提及）。

## 📊 实验亮点

实验结果表明，MRT在极低码率下显著优于现有方法。在Kodak数据集上，MRT相比于最先进的2D架构GLC，实现了43.75%的比特率节省。在CLIC2020数据集上，MRT实现了30.59%的比特率节省。这些结果表明，MRT在极低码率图像压缩方面具有显著的优势。

## 🎯 应用场景

该研究成果可应用于对存储空间或传输带宽有严格限制的场景，例如移动设备上的图像存储、低带宽网络环境下的图像传输、以及遥感图像的压缩存储等。通过更高效的图像压缩，可以降低存储成本、提高传输效率，并为用户提供更好的视觉体验。未来，该技术有望在物联网、视频监控等领域发挥重要作用。

## 📄 摘要（原文）

> Recent advances in extreme image compression have revealed that mapping pixel data into highly compact latent representations can significantly improve coding efficiency. However, most existing methods compress images into 2-D latent spaces via convolutional neural networks (CNNs) or Swin Transformers, which tend to retain substantial spatial redundancy, thereby limiting overall compression performance. In this paper, we propose a novel Mixed RWKV-Transformer (MRT) architecture that encodes images into more compact 1-D latent representations by synergistically integrating the complementary strengths of linear-attention-based RWKV and self-attention-based Transformer models. Specifically, MRT partitions each image into fixed-size windows, utilizing RWKV modules to capture global dependencies across windows and Transformer blocks to model local redundancies within each window. The hierarchical attention mechanism enables more efficient and compact representation learning in the 1-D domain. To further enhance compression efficiency, we introduce a dedicated RWKV Compression Model (RCM) tailored to the structure characteristics of the intermediate 1-D latent features in MRT. Extensive experiments on standard image compression benchmarks validate the effectiveness of our approach. The proposed MRT framework consistently achieves superior reconstruction quality at bitrates below 0.02 bits per pixel (bpp). Quantitative results based on the DISTS metric show that MRT significantly outperforms the state-of-the-art 2-D architecture GLC, achieving bitrate savings of 43.75%, 30.59% on the Kodak and CLIC2020 test datasets, respectively.

