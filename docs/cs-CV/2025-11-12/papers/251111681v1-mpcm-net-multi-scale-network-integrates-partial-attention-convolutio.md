---
layout: default
title: MPCM-Net: Multi-scale network integrates partial attention convolution with Mamba for ground-based cloud image segmentation
---

# MPCM-Net: Multi-scale network integrates partial attention convolution with Mamba for ground-based cloud image segmentation

**arXiv**: [2511.11681v1](https://arxiv.org/abs/2511.11681) | [PDF](https://arxiv.org/pdf/2511.11681.pdf)

**作者**: Penghui Niu, Jiashuai She, Taotao Cai, Yajuan Zhang, Ping Zhang, Junhua Gu, Jianxin Li

**分类**: cs.LG, cs.CV

**发布日期**: 2025-11-12

**🔗 代码/项目**: [GITHUB](https://github.com/she1110/CSRC)

---

## 💡 一句话要点

**提出MPCM-Net，融合部分注意力卷积与Mamba，用于地基云图像分割，提升精度与效率。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `地基云图像分割` `多尺度网络` `部分注意力卷积` `Mamba架构` `光伏发电预测`

## 📋 核心要点

1. 现有云图像分割方法依赖扩张卷积，缺乏通道间互操作性，且注意力机制忽略了精度与效率的平衡。
2. MPCM-Net通过集成部分注意力卷积和Mamba架构，在编码器和解码器端分别进行优化，提升分割精度和效率。
3. 论文提出了新的云图像分割数据集CSRC，实验表明MPCM-Net在CSRC数据集上优于现有方法，实现了精度和速度的平衡。

## 📝 摘要（中文）

地基云图像分割是光伏发电预测的关键研究领域。现有的深度学习方法主要集中在编码器-解码器架构的改进上。然而，现有方法存在一些局限性：(1)它们依赖于扩张卷积进行多尺度上下文提取，缺乏部分特征的有效性和通道间的互操作性；(2)基于注意力的特征增强实现忽略了精度-吞吐量平衡；(3)解码器的修改未能建立分层局部特征之间的全局相互依赖关系，限制了推理效率。为了解决这些挑战，我们提出了MPCM-Net，一个多尺度网络，它集成了部分注意力卷积与Mamba架构，以提高分割精度和计算效率。具体来说，编码器包含MPAC，它包括：(1)一个具有ParCM和ParSM的MPC块，能够实现跨多尺度云层的全局空间交互，以及(2)一个MPA块，结合ParAM和ParSM，以降低的计算复杂度提取判别性特征。在解码器端，采用M2B通过SSHD来减轻上下文损失，SSHD保持线性复杂度，同时实现跨空间和尺度维度上的深度特征聚合。作为对社区的关键贡献，我们还引入并发布了一个数据集CSRC，这是一个清晰标签、细粒度分割基准，旨在克服现有公共数据集的关键局限性。在CSRC上的大量实验表明，MPCM-Net优于最先进的方法，在分割精度和推理速度之间实现了最佳平衡。数据集和源代码将在https://github.com/she1110/CSRC上提供。

## 🔬 方法详解

**问题定义**：现有地基云图像分割方法依赖扩张卷积提取多尺度上下文信息，但缺乏通道间的有效信息交互。同时，基于注意力机制的特征增强方法往往忽略了精度和计算效率之间的平衡。此外，解码器无法有效建立分层局部特征之间的全局依赖关系，限制了推理效率。

**核心思路**：MPCM-Net的核心思路是结合部分注意力卷积和Mamba架构，在编码器端增强特征提取能力，在解码器端建立全局依赖关系，从而在保证分割精度的同时提高计算效率。通过设计特定的模块，例如MPAC和M2B，来克服现有方法的局限性。

**技术框架**：MPCM-Net采用编码器-解码器结构。编码器部分包含MPAC模块，该模块由MPC块和MPA块组成。MPC块利用ParCM和ParSM实现跨多尺度云层的全局空间交互。MPA块结合ParAM和ParSM，以降低的计算复杂度提取判别性特征。解码器部分采用M2B模块，通过SSHD来减轻上下文损失，并实现跨空间和尺度维度上的深度特征聚合。

**关键创新**：MPCM-Net的关键创新在于：(1)提出了MPAC模块，该模块通过部分注意力机制和空间混合机制，有效地提取了多尺度云图像的特征，并降低了计算复杂度。(2)设计了M2B模块，该模块利用Mamba架构建立了全局依赖关系，并减轻了上下文损失。(3)提出了CSRC数据集，该数据集为地基云图像分割提供了高质量的基准。与现有方法相比，MPCM-Net在精度和效率上都取得了显著提升。

**关键设计**：MPAC模块中的ParCM和ParSM的具体实现细节未知，需要参考论文或代码。M2B模块中的SSHD的具体实现细节也未知，需要参考论文或代码。损失函数和优化器的选择也需要在论文或代码中查找。CSRC数据集的标注细节和数据增强方法也需要在论文或代码中查找。

## 📊 实验亮点

MPCM-Net在自建数据集CSRC上进行了实验，结果表明，MPCM-Net优于现有的分割方法，在分割精度和推理速度之间取得了较好的平衡。具体的性能数据和对比基线需要在论文中查找，但摘要中明确指出MPCM-Net取得了优于state-of-the-art方法的效果。

## 🎯 应用场景

MPCM-Net可应用于光伏发电功率预测，通过准确分割云图像，提高光伏发电预测的准确性，从而优化电力系统的调度和运行。此外，该方法还可应用于气象研究、气候建模等领域，为相关研究提供技术支持。

## 📄 摘要（原文）

> Ground-based cloud image segmentation is a critical research domain for photovoltaic power forecasting. Current deep learning approaches primarily focus on encoder-decoder architectural refinements. However, existing methodologies exhibit several limitations:(1)they rely on dilated convolutions for multi-scale context extraction, lacking the partial feature effectiveness and interoperability of inter-channel;(2)attention-based feature enhancement implementations neglect accuracy-throughput balance; and (3)the decoder modifications fail to establish global interdependencies among hierarchical local features, limiting inference efficiency. To address these challenges, we propose MPCM-Net, a Multi-scale network that integrates Partial attention Convolutions with Mamba architectures to enhance segmentation accuracy and computational efficiency. Specifically, the encoder incorporates MPAC, which comprises:(1)a MPC block with ParCM and ParSM that enables global spatial interaction across multi-scale cloud formations, and (2)a MPA block combining ParAM and ParSM to extract discriminative features with reduced computational complexity. On the decoder side, a M2B is employed to mitigate contextual loss through a SSHD that maintains linear complexity while enabling deep feature aggregation across spatial and scale dimensions. As a key contribution to the community, we also introduce and release a dataset CSRC, which is a clear-label, fine-grained segmentation benchmark designed to overcome the critical limitations of existing public datasets. Extensive experiments on CSRC demonstrate the superior performance of MPCM-Net over state-of-the-art methods, achieving an optimal balance between segmentation accuracy and inference speed. The dataset and source code will be available at https://github.com/she1110/CSRC.

