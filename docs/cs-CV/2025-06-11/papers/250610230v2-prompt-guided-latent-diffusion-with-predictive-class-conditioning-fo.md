---
layout: default
title: Prompt-Guided Latent Diffusion with Predictive Class Conditioning for 3D Prostate MRI Generation
---

# Prompt-Guided Latent Diffusion with Predictive Class Conditioning for 3D Prostate MRI Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10230" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10230v2</a>
  <a href="https://arxiv.org/pdf/2506.10230.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10230v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10230v2', 'Prompt-Guided Latent Diffusion with Predictive Class Conditioning for 3D Prostate MRI Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Emerson P. Grabke, Masoom A. Haider, Babak Taati

**分类**: eess.IV, cs.CV

**发布日期**: 2025-06-11 (更新: 2025-07-01)

**备注**: MAH and BT are co-senior authors on the work. This work has been submitted to the IEEE for possible publication

**🔗 代码/项目**: [GITHUB](https://github.com/grabkeem/CCELLA)

---

## 💡 一句话要点

**提出CCELLA以解决医学影像数据稀缺问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `潜在扩散模型` `医学影像` `数据稀缺` `条件化模型` `图像合成` `分类器训练` `深度学习`

## 📋 核心要点

1. 现有医学LDM方法通常依赖短文本编码器或大量数据，限制了性能和科学可及性。
2. 提出CCELLA，一种双头条件化方法，结合临床报告和放射学分类以提升LDM性能。
3. 在3D前列腺MRI数据集上，方法获得0.025的FID分数，分类器准确率从69%提升至74%。

## 📝 摘要（中文）

本研究旨在通过提出一种新颖的条件化潜在扩散模型（LDM）方法，解决医学影像领域中数据稀缺所带来的挑战。现有的医学LDM策略通常依赖于短文本编码器或大量数据，这限制了其性能和科学可及性。我们提出的类条件高效大型语言模型适配器（CCELLA）能够同时利用自由文本临床报告和放射学分类进行条件化，从而提高医学图像合成的质量和下游分类器的性能。实验结果表明，该方法在3D前列腺MRI数据集上显著优于现有基础模型，并在分类器训练中提升了准确率。

## 🔬 方法详解

**问题定义**：本研究旨在解决医学影像生成中的数据稀缺问题，现有方法往往依赖于短文本编码器或大量数据，导致性能受限和科学可及性降低。

**核心思路**：提出类条件高效大型语言模型适配器（CCELLA），通过同时利用自由文本临床报告和放射学分类信息来条件化潜在扩散模型，从而提高生成图像的质量和下游任务的性能。

**技术框架**：该方法的整体架构包括一个双头的条件化模块，分别处理临床报告和分类信息，并通过联合损失函数进行优化。LDM的U-Net结构在此框架下进行训练，以生成高质量的医学图像。

**关键创新**：CCELLA的双头条件化设计是本研究的主要创新点，与传统方法相比，它能够更全面地利用临床信息，提升生成图像的相关性和质量。

**关键设计**：在损失函数设计上，采用了联合损失函数以平衡生成图像的质量和分类准确性，同时在网络结构上，优化了U-Net以适应医学图像的特性。具体参数设置和训练策略在实验中进行了详细验证。

## 📊 实验亮点

实验结果显示，所提方法在3D前列腺MRI数据集上获得了0.025的FID分数，显著优于最近的基础模型（FID 0.071）。此外，在前列腺癌预测的分类器训练中，使用合成图像提高了分类器的准确率，从69%提升至74%。

## 🎯 应用场景

该研究的潜在应用领域包括医学影像生成、疾病预测和临床决策支持等。通过提高医学图像的合成质量和分类器的性能，该方法能够在数据稀缺的情况下，支持医生的诊断和治疗决策，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Objective: Latent diffusion models (LDM) could alleviate data scarcity challenges affecting machine learning development for medical imaging. However, medical LDM strategies typically rely on short-prompt text encoders, non-medical LDMs, or large data volumes. These strategies can limit performance and scientific accessibility. We propose a novel LDM conditioning approach to address these limitations. Methods: We propose Class-Conditioned Efficient Large Language model Adapter (CCELLA), a novel dual-head conditioning approach that simultaneously conditions the LDM U-Net with free-text clinical reports and radiology classification. We also propose a data-efficient LDM framework centered around CCELLA and a proposed joint loss function. We first evaluate our method on 3D prostate MRI against state-of-the-art. We then augment a downstream classifier model training dataset with synthetic images from our method. Results: Our method achieves a 3D FID score of 0.025 on a size-limited 3D prostate MRI dataset, significantly outperforming a recent foundation model with FID 0.071. When training a classifier for prostate cancer prediction, adding synthetic images generated by our method during training improves classifier accuracy from 69% to 74%. Training a classifier solely on our method's synthetic images achieved comparable performance to training on real images alone. Conclusion: We show that our method improved both synthetic image quality and downstream classifier performance using limited data and minimal human annotation. Significance: The proposed CCELLA-centric framework enables radiology report and class-conditioned LDM training for high-quality medical image synthesis given limited data volume and human data annotation, improving LDM performance and scientific accessibility. Code from this study will be available at https://github.com/grabkeem/CCELLA

