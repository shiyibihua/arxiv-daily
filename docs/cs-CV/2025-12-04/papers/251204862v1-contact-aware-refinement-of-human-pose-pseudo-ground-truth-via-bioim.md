---
layout: default
title: Contact-Aware Refinement of Human Pose Pseudo-Ground Truth via Bioimpedance Sensing
---

# Contact-Aware Refinement of Human Pose Pseudo-Ground Truth via Bioimpedance Sensing

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.04862" target="_blank" class="toolbar-btn">arXiv: 2512.04862v1</a>
    <a href="https://arxiv.org/pdf/2512.04862.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04862v1" 
            onclick="toggleFavorite(this, '2512.04862v1', 'Contact-Aware Refinement of Human Pose Pseudo-Ground Truth via Bioimpedance Sensing')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Maria-Paola Forte, Nikos Athanasiou, Giulia Ballardini, Jan Ulrich Bartels, Katherine J. Kuchenbecker, Michael J. Black

**分类**: cs.CV

**发布日期**: 2025-12-04

**备注**: * Equal contribution. Minor figure corrections compared to the ICCV 2025 version

---

## 💡 一句话要点

**提出BioTUCH，结合生物阻抗感知优化自接触场景下的人体姿态伪标签。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `人体姿态估计` `自接触` `生物阻抗传感` `姿态优化` `可穿戴设备`

## 📋 核心要点

1. 现有基于视觉的3D人体姿态估计方法在自接触场景下表现不佳，例如手与脸部的接触。
2. BioTUCH结合视觉姿态估计器和生物阻抗传感，利用生物阻抗感知皮肤接触，优化人体姿态。
3. 实验结果表明，BioTUCH在重建精度上平均提升了11.7%，证明了该方法的有效性。

## 📝 摘要（中文）

为了获取精确的野外3D人体姿态，从而为姿态估计和动作生成方法提供有价值的数据，本文提出了一种新颖的框架。虽然基于视频的估计方法已经变得越来越精确，但它们在涉及自接触的常见场景中经常失效，例如手触摸脸部。相比之下，可穿戴生物阻抗传感可以廉价且不引人注目地测量真实的皮肤接触。因此，我们提出了一种结合视觉姿态估计器和生物阻抗传感的框架，通过考虑自接触来捕获人的3D姿态。我们的方法BioTUCH，使用现成的估计器初始化姿态，并在测量的自接触期间引入接触感知姿态优化：在强制执行顶点邻近约束的同时，最小化重投影误差和与输入估计的偏差。我们使用同步RGB视频、生物阻抗测量和3D运动捕捉的新数据集验证了我们的方法。通过使用三个输入姿态估计器进行测试，我们证明了重建精度平均提高了11.7%。我们还展示了一种微型可穿戴生物阻抗传感器，该传感器能够有效的大规模收集接触感知训练数据，从而使用BioTUCH改进姿态估计和生成。代码和数据可在biotuch.is.tue.mpg.de获得。

## 🔬 方法详解

**问题定义**：论文旨在解决在自接触场景下，基于视觉的3D人体姿态估计精度低的问题。现有的方法难以准确处理遮挡和自接触带来的歧义性，导致姿态估计误差增大。

**核心思路**：论文的核心思路是利用生物阻抗传感来获取皮肤间的接触信息，并将这些信息融入到姿态优化过程中。通过生物阻抗传感器检测皮肤接触，为姿态估计提供额外的约束，从而提高在自接触场景下的姿态估计精度。

**技术框架**：BioTUCH框架主要包含以下几个阶段：1) 使用现成的姿态估计器初始化人体姿态；2) 利用生物阻抗传感器检测皮肤间的接触；3) 基于检测到的接触信息，进行接触感知的姿态优化。姿态优化过程同时考虑了重投影误差、与初始姿态的偏差以及顶点邻近约束。

**关键创新**：该方法最重要的创新点在于将生物阻抗传感与视觉姿态估计相结合，利用生物阻抗提供的接触信息来约束姿态优化过程。这种结合方式能够有效地解决自接触场景下的歧义性问题，从而提高姿态估计的准确性。

**关键设计**：在姿态优化过程中，论文设计了包含重投影误差项、与初始姿态偏差项以及顶点邻近约束项的损失函数。重投影误差项用于保证估计的姿态与图像观测一致；偏差项用于防止姿态过度偏离初始估计；顶点邻近约束项用于保证人体结构的合理性。生物阻抗传感器采用微型可穿戴设计，方便大规模数据采集。

## 📊 实验亮点

实验结果表明，BioTUCH方法在三个不同的输入姿态估计器上均取得了显著的性能提升，平均重建精度提高了11.7%。此外，论文还展示了一种微型可穿戴生物阻抗传感器，为大规模收集接触感知训练数据提供了可能。

## 🎯 应用场景

该研究成果可应用于人机交互、虚拟现实、运动分析、医疗康复等领域。通过提高自接触场景下的人体姿态估计精度，可以改善人机交互的自然性和准确性，提升虚拟现实体验的沉浸感，为运动分析提供更可靠的数据，并为医疗康复提供更精确的姿态评估。

## 📄 摘要（原文）

> Capturing accurate 3D human pose in the wild would provide valuable data for training pose estimation and motion generation methods. While video-based estimation approaches have become increasingly accurate, they often fail in common scenarios involving self-contact, such as a hand touching the face. In contrast, wearable bioimpedance sensing can cheaply and unobtrusively measure ground-truth skin-to-skin contact. Consequently, we propose a novel framework that combines visual pose estimators with bioimpedance sensing to capture the 3D pose of people by taking self-contact into account. Our method, BioTUCH, initializes the pose using an off-the-shelf estimator and introduces contact-aware pose optimization during measured self-contact: reprojection error and deviations from the input estimate are minimized while enforcing vertex proximity constraints. We validate our approach using a new dataset of synchronized RGB video, bioimpedance measurements, and 3D motion capture. Testing with three input pose estimators, we demonstrate an average of 11.7% improvement in reconstruction accuracy. We also present a miniature wearable bioimpedance sensor that enables efficient large-scale collection of contact-aware training data for improving pose estimation and generation using BioTUCH. Code and data are available at biotuch.is.tue.mpg.de

