---
layout: default
title: CoMA: Complementary Masking and Hierarchical Dynamic Multi-Window Self-Attention in a Unified Pre-training Framework
---

# CoMA: Complementary Masking and Hierarchical Dynamic Multi-Window Self-Attention in a Unified Pre-training Framework

**arXiv**: [2511.05929v1](https://arxiv.org/abs/2511.05929) | [PDF](https://arxiv.org/pdf/2511.05929.pdf)

**作者**: Jiaxuan Li, Qing Xu, Xiangjian He, Ziyu Liu, Chang Xing, Zhen Chen, Daokun Zhang, Rong Qu, Chang Wen Chen

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-08

**备注**: 9 pages, 5 figures

---

## 💡 一句话要点

**CoMA：互补掩码与分层动态多窗口自注意力，提升MAE预训练效率。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自监督学习` `掩码自编码器` `视觉Transformer` `互补掩码` `动态多窗口自注意力`

## 📋 核心要点

1. MAE及其变体依赖随机掩码，需更多预训练轮次以保证适应性，且ViT在MAE中参数利用率低。
2. CoMA采用互补掩码策略，确保像素均匀采样，提升特征学习效率和模型适应性。
3. DyViT引入动态多窗口自注意力，减少参数和计算量，同时提升细粒度特征学习能力。

## 📝 摘要（中文）

本文提出了互补掩码自编码器（CoMA），旨在提升掩码自编码器（MAE）的预训练效率和下游任务的适应性。CoMA采用互补掩码策略，确保所有像素的均匀采样，从而更有效地学习所有特征。此外，引入了DyViT，一种分层视觉Transformer，它采用动态多窗口自注意力（DM-MSA），显著减少参数和FLOPs，同时改进了细粒度特征学习。在ImageNet-1K上使用CoMA进行预训练后，DyViT仅使用MAE预训练epoch的12%即可达到与其相当的下游性能，展示了更有效的学习。每个epoch的预训练时间也减少了10%，进一步突出了其卓越的预训练效率。

## 🔬 方法详解

**问题定义**：现有的MAE方法依赖于随机掩码策略，导致训练效率较低，需要大量的预训练epoch才能获得良好的下游任务性能。此外，标准的ViT结构在MAE中应用时，由于各层空间分辨率固定，存在参数利用率不高的问题。因此，论文旨在解决MAE预训练效率低和参数利用率不高的问题。

**核心思路**：论文的核心思路是通过互补掩码策略来保证所有像素的均匀采样，从而更有效地学习图像的各种特征，提高模型的适应性。同时，通过引入动态多窗口自注意力机制，减少模型的参数量和计算复杂度，提升细粒度特征的学习能力。

**技术框架**：CoMA的整体框架包括两个主要组成部分：互补掩码策略和DyViT。互补掩码策略用于生成掩码，确保每个像素都有相同的概率被掩盖。DyViT是一个分层视觉Transformer，它使用动态多窗口自注意力机制来提取图像特征。预训练阶段，模型通过重建被掩盖的图像区域进行学习。在下游任务中，可以使用预训练好的模型进行微调。

**关键创新**：论文的关键创新在于提出了互补掩码策略和动态多窗口自注意力机制。互补掩码策略与随机掩码策略不同，它保证了所有像素的均匀采样，从而避免了某些像素被过度采样而另一些像素被忽略的问题。动态多窗口自注意力机制允许模型在不同的窗口大小上进行自注意力计算，从而更好地捕捉图像的局部和全局信息。

**关键设计**：互补掩码策略通过将图像划分为多个互补的掩码集合来实现，每个集合中的掩码覆盖图像的不同区域，确保所有像素在所有集合中都被覆盖一次。动态多窗口自注意力机制通过在不同的窗口大小上并行计算自注意力，并将结果进行融合来实现。具体的窗口大小设置和融合方式需要根据具体的任务进行调整。

## 📊 实验亮点

实验结果表明，使用CoMA预训练的DyViT仅使用MAE预训练epoch的12%即可达到与其相当的下游性能。此外，每个epoch的预训练时间也减少了10%。这些结果表明，CoMA能够显著提高MAE的预训练效率，并提升模型的下游任务性能。

## 🎯 应用场景

CoMA具有广泛的应用前景，可应用于图像分类、目标检测、语义分割等多种计算机视觉任务。其高效的预训练能力可以降低模型训练成本，加速模型开发周期。该研究对于推动自监督学习在计算机视觉领域的应用具有重要意义，并可能促进相关技术在自动驾驶、智能安防等领域的应用。

## 📄 摘要（原文）

> Masked Autoencoders (MAE) achieve self-supervised learning of image representations by randomly removing a portion of visual tokens and reconstructing the original image as a pretext task, thereby significantly enhancing pretraining efficiency and yielding excellent adaptability across downstream tasks. However, MAE and other MAE-style paradigms that adopt random masking generally require more pre-training epochs to maintain adaptability. Meanwhile, ViT in MAE suffers from inefficient parameter use due to fixed spatial resolution across layers. To overcome these limitations, we propose the Complementary Masked Autoencoders (CoMA), which employ a complementary masking strategy to ensure uniform sampling across all pixels, thereby improving effective learning of all features and enhancing the model's adaptability. Furthermore, we introduce DyViT, a hierarchical vision transformer that employs a Dynamic Multi-Window Self-Attention (DM-MSA), significantly reducing the parameters and FLOPs while improving fine-grained feature learning. Pre-trained on ImageNet-1K with CoMA, DyViT matches the downstream performance of MAE using only 12% of the pre-training epochs, demonstrating more effective learning. It also attains a 10% reduction in pre-training time per epoch, further underscoring its superior pre-training efficiency.

