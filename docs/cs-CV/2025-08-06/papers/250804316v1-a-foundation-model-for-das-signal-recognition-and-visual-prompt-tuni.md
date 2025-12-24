---
layout: default
title: A Foundation Model for DAS Signal Recognition and Visual Prompt Tuning of the Pre-trained Model for Downstream Tasks
---

# A Foundation Model for DAS Signal Recognition and Visual Prompt Tuning of the Pre-trained Model for Downstream Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04316" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04316v1</a>
  <a href="https://arxiv.org/pdf/2508.04316.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04316v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04316v1', 'A Foundation Model for DAS Signal Recognition and Visual Prompt Tuning of the Pre-trained Model for Downstream Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kun Gui, Hongliang Ren, Shang Shi, Jin Lu, Changqiu Yu, Quanjun Cao, Guomin Gu, Qi Xuan

**分类**: cs.CV, eess.SP

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出MAEPD模型以解决DAS信号识别中的数据分布不均问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `分布式声学传感` `信号识别` `自监督学习` `视觉提示调优` `深度学习` `模型微调` `跨域泛化` `管道泄漏检测`

## 📋 核心要点

1. 现有DAS信号识别模型面临数据分布不均和标注数据不足的问题，限制了其跨域泛化能力。
2. 本研究提出MAEPD模型，通过Masked Autoencoder进行预训练，并结合视觉提示调优方法，提升模型在下游任务中的表现。
3. 实验结果显示，MAEPD在室内步态识别中取得96.94%的准确率，且训练时间减少45%，展示了其高效性和可扩展性。

## 📝 摘要（中文）

分布式声学传感（DAS）技术在多个领域的应用日益增长。然而，由于异构传感环境导致的数据分布差异，数据驱动的人工智能模型面临跨域泛化能力不足和标注训练数据短缺的挑战。为了解决这些问题，本研究提出了一种基于Masked Autoencoder的DAS信号识别基础模型MAEPD。该模型在635,860个样本的数据集上进行预训练，涵盖了DAS步态时空信号、用于周界安全的2D GASF图像、管道泄漏的2D时频图像，以及包括鲸鱼叫声和地震活动的开放数据集信号，利用自监督掩码重建任务捕捉DAS信号的深层语义特征。通过视觉提示调优（VPT）方法用于下游识别任务，实验结果表明该模型在室内步态识别任务中达到了96.94%的分类准确率，且仅微调了0.322%的参数，训练时间减少了45%。

## 🔬 方法详解

**问题定义**：本研究旨在解决分布式声学传感（DAS）信号识别中的数据分布不均和标注数据短缺问题。现有方法在异构环境下的泛化能力不足，限制了其应用。

**核心思路**：论文提出的MAEPD模型通过Masked Autoencoder进行预训练，利用自监督学习捕捉深层语义特征，随后通过视觉提示调优（VPT）方法进行下游任务的微调，旨在提高模型的适应性和效率。

**技术框架**：MAEPD模型的整体架构包括预训练阶段和微调阶段。在预训练阶段，模型在多种DAS信号数据集上进行自监督学习；在微调阶段，冻结主干网络参数，仅调整插入Transformer编码器层的少量可学习视觉提示向量。

**关键创新**：MAEPD模型的主要创新在于结合了Masked Autoencoder和视觉提示调优方法，显著提高了模型在下游任务中的性能，同时减少了需要微调的参数数量，与传统的全微调方法相比，具有更高的效率。

**关键设计**：在模型设计中，采用了自监督掩码重建任务作为预训练目标，确保模型能够有效捕捉DAS信号的深层特征。同时，VPT方法的引入使得模型在微调时只需调整少量参数，显著降低了训练时间和计算资源的消耗。

## 📊 实验亮点

在实验中，MAEPD模型在室内步态识别任务中达到了96.94%的分类准确率，仅微调了0.322%的参数，相比传统的全微调方法提高了0.61%的准确率，并且训练时间减少了45%，展示了其优越的性能和效率。

## 🎯 应用场景

该研究的MAEPD模型在分布式声学传感领域具有广泛的应用潜力，能够有效提升信号识别的准确性和效率。其方法不仅适用于步态识别，还可扩展到管道泄漏检测、环境监测等多个领域，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Distributed Acoustic Sensing (DAS) technology finds growing applications across various domains. However, data distribution disparities due to heterogeneous sensing environments pose challenges for data-driven artificial intelligence (AI) models, limiting cross-domain generalization and facing a shortage of labeled training data. To address these issues, this study proposes a foundational model for DAS signal recognition based on a Masked Autoencoder, named MAEPD. The MAEPD model is pretrained on a dataset of 635,860 samples, encompassing DAS gait spatiotemporal signals, 2D GASF images for perimeter security, 2D time-frequency images for pipeline leakage, and open-dataset signals including whale vocalizations and seismic activities, using a self-supervised mask reconstruction task to capture deep semantic features of DAS signals. Visual Prompt Tuning (VPT) is employed for downstream recognition tasks. This method freezes the pretrained backbone parameters and fine-tunes only a small set of learnable visual prompt vectors inserted into the Transformer encoder layers. Experiments on the NVIDIA GeForce RTX 4080 Super platform validate MAEPD using indoor gait recognition as a downstream task. The VPT-Deep approach achieves a classification accuracy of 96.94% with just 0.322% of parameters fine-tuned, surpassing the traditional Full Fine Tuning (FFT) method by 0.61% and reducing training time by 45%. The model also exhibits robust performance in pipeline leakage detection, confirming the generality, efficiency, and scalability of MAEPD as a foundational model. This approach offers a novel paradigm for addressing the limited generalization of signal recognition models in the DAS domain.

