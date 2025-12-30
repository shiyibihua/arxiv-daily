---
layout: default
title: Stochastic Siamese MAE Pretraining for Longitudinal Medical Images
---

# Stochastic Siamese MAE Pretraining for Longitudinal Medical Images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23441" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23441v1</a>
  <a href="https://arxiv.org/pdf/2512.23441.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23441v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23441v1', 'Stochastic Siamese MAE Pretraining for Longitudinal Medical Images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Taha Emre, Arunava Chakravarty, Thomas Pinetz, Dmitrii Lachinov, Martin J. Menten, Hendrik Scholl, Sobha Sivaprasad, Daniel Rueckert, Andrew Lotery, Stefan Sacu, Ursula Schmidt-Erfurth, Hrvoje Bogunović

**分类**: cs.LG, cs.CV

**发布日期**: 2025-12-29

**备注**: Under review. Code is available in https://github.com/EmreTaha/STAMP

---

## 💡 一句话要点

**提出STAMP：一种用于纵向医学图像的随机Siamese MAE预训练框架**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `纵向医学图像` `自监督学习` `掩码自编码器` `Siamese网络` `时间序列分析`

## 📋 核心要点

1. 现有MAE方法在表征学习方面表现出色，但缺乏对纵向医学图像时间信息的有效建模能力，无法捕捉疾病进展的不确定性。
2. STAMP通过引入随机Siamese MAE框架，利用时间差作为条件，将重建损失转化为条件变分推断目标，从而学习非确定性的时间动态。
3. 在OCT和MRI数据集上的实验表明，STAMP预训练的ViT模型在疾病进展预测任务中，显著优于现有方法和基础模型。

## 📝 摘要（中文）

本文提出了一种名为STAMP（具有掩码预训练的随机时间自编码器）的Siamese MAE框架，用于编码纵向医学数据集3D体积中的时间信息，这对于捕捉疾病进展至关重要。与现有的掩码自编码器（MAE）方法不同，STAMP通过一个随机过程，以两个输入体积之间的时间差为条件，来编码时间信息。与确定性的Siamese方法不同，STAMP将MAE重建损失重新定义为条件变分推断目标，从而随机地学习时间动态，解决了确定性方法无法解释疾病演变中固有不确定性的问题。在多个患者多次就诊的OCT和MRI数据集上进行的评估表明，STAMP预训练的ViT模型在预测晚期年龄相关性黄斑变性和阿尔茨海默病进展方面，优于现有的时间MAE方法和基础模型，这些预测任务需要模型学习疾病潜在的非确定性时间动态。

## 🔬 方法详解

**问题定义**：纵向医学图像分析的关键在于捕捉疾病随时间变化的进展。现有的自监督学习方法，如MAE，虽然擅长图像表征学习，但缺乏对时间信息的有效建模，无法准确预测疾病的演变过程，尤其是在疾病进展具有不确定性的情况下。确定性的Siamese网络虽然可以比较不同时间点的扫描结果，但无法解释疾病演变中固有的不确定性。

**核心思路**：STAMP的核心思路是通过引入随机性来建模疾病进展的不确定性。具体来说，它使用Siamese MAE框架，并以两个输入体积之间的时间差为条件，通过随机过程编码时间信息。这种方法将MAE的重建损失重新定义为条件变分推断目标，从而允许模型学习时间动态的概率分布，而不是单一的确定性映射。

**技术框架**：STAMP采用Siamese网络结构，包含两个共享权重的MAE编码器。输入是同一患者在不同时间点的两张医学图像。这两个图像分别经过MAE编码器，然后通过一个条件变分自编码器（CVAE）进行处理，CVAE以两张图像的时间差作为条件，生成一个潜在变量。最后，解码器利用这个潜在变量重建被mask的图像块。整个框架通过最小化重建误差和CVAE的KL散度进行训练。

**关键创新**：STAMP的关键创新在于将确定性的Siamese MAE框架扩展到随机框架，从而能够建模疾病进展的不确定性。通过将重建损失重新定义为条件变分推断目标，STAMP可以学习时间动态的概率分布，而不是单一的确定性映射。这使得模型能够更好地预测疾病的演变过程，尤其是在疾病进展具有不确定性的情况下。

**关键设计**：STAMP的关键设计包括：1) 使用ViT作为MAE的编码器和解码器；2) 使用时间差作为CVAE的条件输入；3) 使用KL散度作为正则化项，鼓励潜在变量服从标准正态分布；4) 通过调整mask比例和CVAE的参数来控制模型的随机性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23441v1/visivis_v7.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23441v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23441v1/double.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

STAMP在三个医学图像数据集（两个OCT数据集和一个MRI数据集）上进行了评估，实验结果表明，STAMP预训练的ViT模型在预测晚期年龄相关性黄斑变性和阿尔茨海默病进展方面，显著优于现有的时间MAE方法和基础模型。例如，在AMD进展预测任务中，STAMP相比于基线方法取得了显著的性能提升（具体数值未在摘要中给出，属于未知信息）。

## 🎯 应用场景

STAMP在纵向医学图像分析领域具有广泛的应用前景，例如疾病进展预测、个性化治疗方案制定、药物疗效评估等。通过学习疾病演变的非确定性时间动态，STAMP可以帮助医生更准确地预测患者的病情发展，从而制定更有效的治疗策略，并评估药物的疗效。此外，STAMP还可以用于辅助诊断，帮助医生识别早期病变，从而实现疾病的早期干预。

## 📄 摘要（原文）

> Temporally aware image representations are crucial for capturing disease progression in 3D volumes of longitudinal medical datasets. However, recent state-of-the-art self-supervised learning approaches like Masked Autoencoding (MAE), despite their strong representation learning capabilities, lack temporal awareness. In this paper, we propose STAMP (Stochastic Temporal Autoencoder with Masked Pretraining), a Siamese MAE framework that encodes temporal information through a stochastic process by conditioning on the time difference between the 2 input volumes. Unlike deterministic Siamese approaches, which compare scans from different time points but fail to account for the inherent uncertainty in disease evolution, STAMP learns temporal dynamics stochastically by reframing the MAE reconstruction loss as a conditional variational inference objective. We evaluated STAMP on two OCT and one MRI datasets with multiple visits per patient. STAMP pretrained ViT models outperformed both existing temporal MAE methods and foundation models on different late stage Age-Related Macular Degeneration and Alzheimer's Disease progression prediction which require models to learn the underlying non-deterministic temporal dynamics of the diseases.

