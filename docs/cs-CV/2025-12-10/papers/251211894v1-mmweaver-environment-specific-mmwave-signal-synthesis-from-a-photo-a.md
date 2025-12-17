---
layout: default
title: mmWEAVER: Environment-Specific mmWave Signal Synthesis from a Photo and Activity Description
---

# mmWEAVER: Environment-Specific mmWave Signal Synthesis from a Photo and Activity Description

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.11894" target="_blank" class="toolbar-btn">arXiv: 2512.11894v1</a>
    <a href="https://arxiv.org/pdf/2512.11894.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.11894v1" 
            onclick="toggleFavorite(this, '2512.11894v1', 'mmWEAVER: Environment-Specific mmWave Signal Synthesis from a Photo and Activity Description')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Mahathir Monjur, Shahriar Nirjon

**分类**: cs.CV, cs.LG

**发布日期**: 2025-12-10

**备注**: Accepted at the IEEE/CVF Winter Conference on Applications of Computer Vision 2026 (WACV 2026)

---

## 💡 一句话要点

**mmWeaver：利用照片和活动描述合成环境特定的毫米波信号**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `毫米波雷达` `信号合成` `隐式神经表示` `超网络` `活动识别` `姿态估计` `数据增强` `环境感知`

## 📋 核心要点

1. 毫米波雷达应用依赖于环境特定的信号数据集，但物理仿真计算成本高昂，难以满足需求。
2. mmWeaver利用隐式神经表示和超网络，根据环境和人体运动特征动态生成毫米波信号。
3. 实验表明，mmWeaver在信号真实性、活动识别和姿态估计方面均优于现有方法，且速度更快。

## 📝 摘要（中文）

为了推进毫米波雷达在活动识别和姿态估计等应用中的发展，逼真的信号生成和数据集增强至关重要，这些应用严重依赖于多样化且环境特定的信号数据集。然而，毫米波信号本质上是复杂、稀疏和高维的，使得物理仿真在计算上非常昂贵。本文提出了mmWeaver，这是一个新颖的框架，通过使用隐式神经表示（INRs）将毫米波信号建模为连续函数，从而合成逼真的、环境特定的复杂毫米波信号，实现了高达49倍的压缩。mmWeaver结合了超网络，这些超网络基于环境上下文（从RGB-D图像中提取）和人体运动特征（通过MotionGPT从文本到姿势生成）动态生成INR参数，从而实现高效和自适应的信号合成。通过以这些语义和几何先验为条件，mmWeaver生成多种分辨率的I/Q信号，保留了对点云估计和活动分类等下游任务至关重要的相位信息。大量实验表明，mmWeaver实现了0.88的复数SSIM和35 dB的PSNR，在信号真实性方面优于现有方法，同时将活动识别准确率提高了高达7%，并将人体姿态估计误差降低了高达15%，所有这些都比基于仿真的方法快6-35倍。

## 🔬 方法详解

**问题定义**：现有的毫米波信号生成方法，特别是基于物理仿真的方法，计算复杂度高，难以快速生成大量环境相关的训练数据。这限制了毫米波雷达在活动识别、姿态估计等领域的应用，因为这些应用需要大量多样化的数据进行训练。现有方法难以兼顾信号的真实性和生成效率。

**核心思路**：mmWeaver的核心思路是将毫米波信号建模为连续函数，并使用隐式神经表示（INR）来表示这些函数。通过使用超网络动态生成INR的参数，可以根据环境上下文（RGB-D图像）和人体运动特征（文本描述）自适应地生成信号。这种方法避免了昂贵的物理仿真，并允许高效地生成环境特定的信号。

**技术框架**：mmWeaver框架包含以下主要模块：1) 环境编码器：从RGB-D图像中提取环境特征。2) 运动编码器：使用MotionGPT从文本描述中生成人体姿势序列，并提取运动特征。3) 超网络：根据环境和运动特征生成INR的参数。4) INR：使用生成的参数将坐标映射到复数I/Q信号值。整体流程是，给定环境图像和活动描述，首先提取环境和运动特征，然后使用超网络生成INR参数，最后使用INR生成毫米波信号。

**关键创新**：mmWeaver的关键创新在于使用超网络动态生成INR参数，从而实现环境特定的信号合成。与传统的基于仿真的方法相比，mmWeaver避免了昂贵的物理仿真，并允许高效地生成多样化的信号。此外，mmWeaver通过以环境和运动特征为条件，可以生成更逼真的信号，并保留了对下游任务至关重要的相位信息。

**关键设计**：超网络的设计至关重要，它需要能够有效地将环境和运动特征映射到INR参数。论文中使用了多层感知机（MLP）作为超网络，并使用ReLU激活函数。INR也使用MLP实现，其输入是坐标，输出是复数I/Q信号值。损失函数包括复数SSIM损失和L1损失，用于衡量生成信号与真实信号之间的差异。为了保证信号的相位信息，特别关注了复数域的信号处理。

## 📊 实验亮点

mmWeaver在信号真实性方面优于现有方法，实现了0.88的复数SSIM和35 dB的PSNR。在活动识别任务中，mmWeaver将准确率提高了高达7%。在人体姿态估计任务中，mmWeaver将误差降低了高达15%。此外，mmWeaver的运行速度比基于仿真的方法快6-35倍，大大提高了信号生成的效率。

## 🎯 应用场景

mmWeaver可应用于毫米波雷达相关的各种领域，如智能家居、自动驾驶、安防监控等。通过生成大量逼真的训练数据，可以提高活动识别、姿态估计等任务的准确性和鲁棒性。此外，mmWeaver还可以用于评估毫米波雷达系统的性能，并优化雷达的设计。

## 📄 摘要（原文）

> Realistic signal generation and dataset augmentation are essential for advancing mmWave radar applications such as activity recognition and pose estimation, which rely heavily on diverse, and environment-specific signal datasets. However, mmWave signals are inherently complex, sparse, and high-dimensional, making physical simulation computationally expensive. This paper presents mmWeaver, a novel framework that synthesizes realistic, environment-specific complex mmWave signals by modeling them as continuous functions using Implicit Neural Representations (INRs), achieving up to 49-fold compression. mmWeaver incorporates hypernetworks that dynamically generate INR parameters based on environmental context (extracted from RGB-D images) and human motion features (derived from text-to-pose generation via MotionGPT), enabling efficient and adaptive signal synthesis. By conditioning on these semantic and geometric priors, mmWeaver generates diverse I/Q signals at multiple resolutions, preserving phase information critical for downstream tasks such as point cloud estimation and activity classification. Extensive experiments show that mmWeaver achieves a complex SSIM of 0.88 and a PSNR of 35 dB, outperforming existing methods in signal realism while improving activity recognition accuracy by up to 7% and reducing human pose estimation error by up to 15%, all while operating 6-35 times faster than simulation-based approaches.

