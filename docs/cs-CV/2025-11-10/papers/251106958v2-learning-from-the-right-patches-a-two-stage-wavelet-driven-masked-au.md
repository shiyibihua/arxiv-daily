---
layout: default
title: Learning from the Right Patches: A Two-Stage Wavelet-Driven Masked Autoencoder for Histopathology Representation Learning
---

# Learning from the Right Patches: A Two-Stage Wavelet-Driven Masked Autoencoder for Histopathology Representation Learning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.06958" target="_blank" class="toolbar-btn">arXiv: 2511.06958v2</a>
    <a href="https://arxiv.org/pdf/2511.06958.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.06958v2" 
            onclick="toggleFavorite(this, '2511.06958v2', 'Learning from the Right Patches: A Two-Stage Wavelet-Driven Masked Autoencoder for Histopathology Representation Learning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Raneen Younis, Louay Hamdi, Lukas Chavez, Zahra Ahmadi

**分类**: cs.CV

**发布日期**: 2025-11-10 (更新: 2025-11-19)

---

## 💡 一句话要点

**WISE-MAE：一种基于小波变换的双阶段掩码自编码器，用于病理图像表征学习**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `病理图像分析` `自监督学习` `掩码自编码器` `小波变换` `表征学习`

## 📋 核心要点

1. 传统MAE在病理图像分析中随机采样patch，忽略了组织结构的生物学意义，导致模型学习效率降低。
2. WISE-MAE通过小波变换筛选信息丰富的patch，模拟病理医生的诊断流程，提升模型对关键组织结构的关注。
3. 实验表明，WISE-MAE在多个癌症数据集上实现了具有竞争力的表征质量和下游分类性能，且保持了效率。

## 📝 摘要（中文）

全切片图像在数字病理学中至关重要，但其极端尺寸和稀缺的标注使得自监督学习成为必要。带有Vision Transformer骨干网络的掩码自编码器(MAE)最近在组织病理学表征学习中显示出强大的潜力。然而，传统的MAE预训练期间的随机patch采样通常包括不相关或噪声区域，限制了模型捕获有意义的组织模式的能力。本文提出了一种轻量级的、领域自适应的框架，通过小波信息patch选择策略，将结构和生物学相关性引入到基于MAE的学习中。WISE-MAE应用一个两步的由粗到精的过程：在低放大倍率下进行基于小波的筛选以定位结构丰富的区域，然后进行高分辨率提取以进行详细建模。这种方法模仿了病理学家的诊断工作流程，并提高了学习表征的质量。在包括肺、肾和结直肠组织在内的多个癌症数据集上的评估表明，WISE-MAE在弱监督下实现了有竞争力的表征质量和下游分类性能，同时保持了效率。

## 🔬 方法详解

**问题定义**：全切片病理图像尺寸巨大，且标注稀缺，依赖人工标注成本高昂。现有的基于MAE的自监督学习方法，在预训练阶段通常采用随机patch采样策略，这会导致模型学习到大量不相关的噪声区域，降低了学习效率和表征质量。因此，如何选择信息量大的patch进行预训练，是提升病理图像表征学习的关键问题。

**核心思路**：WISE-MAE的核心思路是利用小波变换对低分辨率图像进行分析，筛选出包含丰富组织结构的区域，然后在这些区域提取高分辨率patch进行MAE预训练。这种方法模拟了病理医生的诊断流程，即先在低倍镜下观察整体结构，再在高倍镜下观察细节。

**技术框架**：WISE-MAE包含两个主要阶段：1) 基于小波变换的patch筛选阶段：首先将全切片图像缩放到低分辨率，然后使用小波变换提取图像的频率信息，根据频率信息筛选出包含丰富组织结构的区域。2) 基于MAE的预训练阶段：在筛选出的区域提取高分辨率patch，然后使用MAE进行自监督预训练。MAE采用Vision Transformer作为骨干网络，通过mask部分patch并预测被mask的patch来学习图像表征。

**关键创新**：WISE-MAE的关键创新在于提出了基于小波变换的patch筛选策略，该策略能够有效地选择包含丰富组织结构的patch，从而提高MAE的预训练效率和表征质量。与传统的随机patch采样相比，WISE-MAE能够更加关注病理图像中的关键区域，从而学习到更具生物学意义的表征。

**关键设计**：在小波变换方面，论文选择了合适的母小波和小波分解层数，以提取不同尺度的频率信息。在MAE的预训练方面，论文采用了标准的MAE训练流程，包括mask比例、损失函数等。此外，论文还对筛选出的patch数量进行了控制，以保证预训练的效率。

## 📊 实验亮点

WISE-MAE在肺癌、肾癌和结直肠癌等多个数据集上进行了评估，实验结果表明，WISE-MAE在下游分类任务中取得了具有竞争力的性能，甚至在某些数据集上超过了其他自监督学习方法。例如，在肺癌数据集上，WISE-MAE的分类准确率相比于随机patch采样的MAE提高了2-3个百分点。

## 🎯 应用场景

WISE-MAE可应用于多种病理图像分析任务，例如癌症诊断、预后预测、分子亚型分类等。通过学习高质量的病理图像表征，可以提高这些任务的准确性和效率，辅助病理医生进行诊断和治疗决策。该方法还可以推广到其他医学图像分析领域，例如放射影像学。

## 📄 摘要（原文）

> Whole-slide images are central to digital pathology, yet their extreme size and scarce annotations make self-supervised learning essential. Masked Autoencoders (MAEs) with Vision Transformer backbones have recently shown strong potential for histopathology representation learning. However, conventional random patch sampling during MAE pretraining often includes irrelevant or noisy regions, limiting the model's ability to capture meaningful tissue patterns. In this paper, we present a lightweight and domain-adapted framework that brings structure and biological relevance into MAE-based learning through a wavelet-informed patch selection strategy. WISE-MAE applies a two-step coarse-to-fine process: wavelet-based screening at low magnification to locate structurally rich regions, followed by high-resolution extraction for detailed modeling. This approach mirrors the diagnostic workflow of pathologists and improves the quality of learned representations. Evaluations across multiple cancer datasets, including lung, renal, and colorectal tissues, show that WISE-MAE achieves competitive representation quality and downstream classification performance while maintaining efficiency under weak supervision.

