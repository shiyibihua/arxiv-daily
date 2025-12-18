---
layout: default
title: Improve Supervised Representation Learning with Masked Image Modeling
---

# Improve Supervised Representation Learning with Masked Image Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.00950" class="toolbar-btn" target="_blank">📄 arXiv: 2312.00950v1</a>
  <a href="https://arxiv.org/pdf/2312.00950.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.00950v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.00950v1', 'Improve Supervised Representation Learning with Masked Image Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaifeng Chen, Daniel Salz, Huiwen Chang, Kihyuk Sohn, Dilip Krishnan, Mojtaba Seyedhosseini

**分类**: cs.CV

**发布日期**: 2023-12-01

---

## 💡 一句话要点

**提出一种简单有效的掩码图像建模以提升监督表示学习**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `掩码图像建模` `监督表示学习` `视觉变换器` `图像分类` `图像检索` `语义分割` `深度学习`

## 📋 核心要点

1. 现有的监督表示学习方法在利用标记数据时存在一定的局限性，难以充分挖掘数据中的潜在信息。
2. 本文提出了一种将掩码图像建模（MIM）集成到监督训练中的新方法，通过增加解码器和MIM任务来增强表示学习。
3. 实验结果表明，所提方法在ImageNet-1k上实现了81.72%的验证准确率，相较于基线模型提升了2.01%。

## 📝 摘要（中文）

在计算机视觉中，使用标记数据进行视觉嵌入训练已成为表示学习的常规设置。受最近掩码图像建模（MIM）在自监督表示学习中成功应用的启发，本文提出了一种简单而有效的设置，可以轻松将MIM集成到现有的监督训练范式中。我们在视觉变换器图像编码器上增加了一个浅层变换器解码器，并引入了MIM任务，以根据掩码图像输入重建图像标记。实验表明，经过最小的架构更改和无推理开销，该设置能够提高下游任务（如分类、图像检索和语义分割）中学习到的表示质量。我们在公共基准上进行了全面的研究和评估，结果显示在ImageNet-1k上，ViT-B/14模型的验证准确率达到81.72%，比基线模型高出2.01%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有监督表示学习方法在利用标记数据时的不足，特别是如何更有效地挖掘图像数据中的信息。现有方法往往未能充分利用未标记数据的潜力，导致表示学习效果不佳。

**核心思路**：论文的核心思路是将掩码图像建模（MIM）引入到监督学习框架中，通过在视觉变换器编码器上增加一个浅层解码器，并引入MIM任务，以重建掩码图像输入，从而提升学习到的表示质量。

**技术框架**：整体架构包括一个视觉变换器图像编码器和一个浅层变换器解码器。编码器负责提取图像特征，而解码器则通过MIM任务重建图像标记，形成一个端到端的训练流程。

**关键创新**：最重要的技术创新在于将MIM与监督学习相结合，形成了一种新的训练范式。这种方法不仅提高了表示学习的效果，而且在推理时没有增加额外的计算开销。

**关键设计**：在设计中，采用了特定的损失函数来优化重建任务，同时保持了原有分类任务的结构。网络结构上，解码器的设计较为简单，旨在减少计算复杂度并提高训练效率。通过这种设计，模型能够在保持高效性的同时，提升表示的质量。

## 📊 实验亮点

实验结果显示，所提ViT-B/14模型在ImageNet-1k上达到了81.72%的验证准确率，比基线模型提升了2.01%。在K-Nearest-Neighbor图像检索评估中，该模型同样超越了基线，提升幅度为1.32%。这些结果表明该方法在多个下游任务中均具有显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉中的图像分类、图像检索和语义分割等任务。通过提升表示学习的质量，能够在实际应用中提高模型的准确性和鲁棒性，进而推动智能视觉系统的发展。未来，该方法有望扩展到更大规模的数据集和更复杂的模型中，进一步提升性能。

## 📄 摘要（原文）

> Training visual embeddings with labeled data supervision has been the de facto setup for representation learning in computer vision. Inspired by recent success of adopting masked image modeling (MIM) in self-supervised representation learning, we propose a simple yet effective setup that can easily integrate MIM into existing supervised training paradigms. In our design, in addition to the original classification task applied to a vision transformer image encoder, we add a shallow transformer-based decoder on top of the encoder and introduce an MIM task which tries to reconstruct image tokens based on masked image inputs. We show with minimal change in architecture and no overhead in inference that this setup is able to improve the quality of the learned representations for downstream tasks such as classification, image retrieval, and semantic segmentation. We conduct a comprehensive study and evaluation of our setup on public benchmarks. On ImageNet-1k, our ViT-B/14 model achieves 81.72% validation accuracy, 2.01% higher than the baseline model. On K-Nearest-Neighbor image retrieval evaluation with ImageNet-1k, the same model outperforms the baseline by 1.32%. We also show that this setup can be easily scaled to larger models and datasets. Code and checkpoints will be released.

