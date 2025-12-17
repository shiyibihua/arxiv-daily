---
layout: default
title: IMSE: Efficient U-Net-based Speech Enhancement using Inception Depthwise Convolution and Amplitude-Aware Linear Attention
---

# IMSE: Efficient U-Net-based Speech Enhancement using Inception Depthwise Convolution and Amplitude-Aware Linear Attention

**arXiv**: [2511.14515v2](https://arxiv.org/abs/2511.14515) | [PDF](https://arxiv.org/pdf/2511.14515.pdf)

**作者**: Xinxin Tang, Bin Qin, Yufang Li

**分类**: cs.SD, cs.AI, cs.CV

**发布日期**: 2025-11-18 (更新: 2025-12-01)

---

## 💡 一句话要点

**IMSE：利用Inception深度可分离卷积和幅度感知线性注意力的高效U-Net语音增强**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `语音增强` `轻量化模型` `U-Net` `线性注意力` `深度可分离卷积` `幅度感知` `资源受限设备`

## 📋 核心要点

1. 现有语音增强方法在资源受限设备上难以兼顾轻量化和高性能，存在效率瓶颈。
2. IMSE通过幅度感知线性注意力和Inception深度可分离卷积，实现高效全局建模和特征提取。
3. 实验表明，IMSE在参数量显著降低的同时，保持了与现有最佳方法相当的语音增强性能。

## 📝 摘要（中文）

本文提出IMSE，一个系统优化且超轻量级的语音增强网络，旨在平衡轻量化设计和高性能。现有方法如MUSE虽然参数量仅为0.51M，但效率仍有瓶颈。MUSE中的MET模块依赖复杂的“近似-补偿”机制来缓解泰勒展开注意力的局限性，而可变形嵌入的偏移计算引入了额外的计算负担。IMSE引入了两个核心创新：1) 使用幅度感知线性注意力（MALA）替换MET模块，通过显式保留查询向量的范数信息，从根本上纠正线性注意力中“忽略幅度”的问题，实现高效的全局建模。2) 使用Inception深度可分离卷积（IDConv）替换DE模块，将大核操作分解为高效的并行分支（正方形、水平和垂直条），以极低的参数冗余捕获频谱图特征。在VoiceBank+DEMAND数据集上的实验表明，与MUSE相比，IMSE在参数量减少16.8%（从0.513M到0.427M）的同时，在PESQ指标上实现了与最先进水平相当的性能（3.373）。这项研究为超轻量级语音增强中模型大小和语音质量之间的权衡设定了新的基准。

## 🔬 方法详解

**问题定义**：论文旨在解决语音增强任务中，如何在资源受限的设备上实现高性能和低计算复杂度的平衡问题。现有方法，如MUSE，虽然参数量较小，但其MET模块和DE模块仍然存在效率瓶颈，例如MET模块需要复杂的近似补偿机制，DE模块需要额外的偏移计算，导致计算负担增加。

**核心思路**：论文的核心思路是通过改进注意力机制和卷积操作，在不损失性能的前提下，显著降低模型的参数量和计算复杂度。具体来说，使用幅度感知线性注意力（MALA）替代复杂的MET模块，解决线性注意力忽略幅度信息的问题；使用Inception深度可分离卷积（IDConv）替代DE模块，以更高效的方式提取频谱图特征。

**技术框架**：IMSE采用U-Net结构作为整体框架，编码器提取输入噪声语音的特征，解码器重建增强后的语音。MALA模块被集成到U-Net的瓶颈层，用于全局建模。IDConv模块被用于编码器和解码器的卷积层，用于高效的特征提取。整个网络结构简洁高效，易于部署到资源受限的设备上。

**关键创新**：论文的关键创新在于提出了幅度感知线性注意力（MALA）和Inception深度可分离卷积（IDConv）。MALA通过显式保留查询向量的范数信息，解决了线性注意力忽略幅度信息的问题，实现了高效的全局建模。IDConv将大核卷积分解为多个并行的深度可分离卷积分支，减少了参数冗余，提高了计算效率。

**关键设计**：MALA模块的关键设计在于在计算注意力权重时，显式地考虑了查询向量的范数信息，从而避免了信息损失。IDConv模块的关键设计在于将大核卷积分解为正方形、水平和垂直条状的深度可分离卷积，从而在不同方向上提取特征，并减少参数量。损失函数采用常用的时域或频域损失函数，例如L1损失或均方误差。

## 📊 实验亮点

实验结果表明，IMSE在VoiceBank+DEMAND数据集上，相比于MUSE基线，参数量减少了16.8%（从0.513M到0.427M），同时在PESQ指标上达到了3.373，与最先进水平相当。这表明IMSE在模型大小和语音质量之间取得了更好的平衡，为超轻量级语音增强设定了新的基准。

## 🎯 应用场景

该研究成果可应用于各种资源受限的语音增强场景，例如移动设备、嵌入式系统、智能家居设备等。通过降低模型复杂度和计算量，IMSE能够在这些设备上实现实时的语音增强，提高语音通信质量和用户体验。此外，该方法还可以应用于助听器等辅助设备，帮助听力受损人士更好地理解语音。

## 📄 摘要（原文）

> Achieving a balance between lightweight design and high performance remains a significant challenge for speech enhancement (SE) tasks on resource-constrained devices. Existing state-of-the-art methods, such as MUSE, have established a strong baseline with only 0.51M parameters by introducing a Multi-path Enhanced Taylor (MET) transformer and Deformable Embedding (DE). However, an in-depth analysis reveals that MUSE still suffers from efficiency bottlenecks: the MET module relies on a complex "approximate-compensate" mechanism to mitigate the limitations of Taylor-expansion-based attention, while the offset calculation for deformable embedding introduces additional computational burden. This paper proposes IMSE, a systematically optimized and ultra-lightweight network. We introduce two core innovations: 1) Replacing the MET module with Amplitude-Aware Linear Attention (MALA). MALA fundamentally rectifies the "amplitude-ignoring" problem in linear attention by explicitly preserving the norm information of query vectors in the attention calculation, achieving efficient global modeling without an auxiliary compensation branch. 2) Replacing the DE module with Inception Depthwise Convolution (IDConv). IDConv borrows the Inception concept, decomposing large-kernel operations into efficient parallel branches (square, horizontal, and vertical strips), thereby capturing spectrogram features with extremely low parameter redundancy. Extensive experiments on the VoiceBank+DEMAND dataset demonstrate that, compared to the MUSE baseline, IMSE significantly reduces the parameter count by 16.8\% (from 0.513M to 0.427M) while achieving competitive performance comparable to the state-of-the-art on the PESQ metric (3.373). This study sets a new benchmark for the trade-off between model size and speech quality in ultra-lightweight speech enhancement.

