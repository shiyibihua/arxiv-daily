---
layout: default
title: CNN-Based Camera Pose Estimation and Localisation of Scan Images for Aircraft Visual Inspection
---

# CNN-Based Camera Pose Estimation and Localisation of Scan Images for Aircraft Visual Inspection

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.18702" target="_blank" class="toolbar-btn">arXiv: 2511.18702v1</a>
    <a href="https://arxiv.org/pdf/2511.18702.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18702v1" 
            onclick="toggleFavorite(this, '2511.18702v1', 'CNN-Based Camera Pose Estimation and Localisation of Scan Images for Aircraft Visual Inspection')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Xueyan Oh, Leonard Loh, Shaohui Foong, Zhong Bao Andy Koh, Kow Leong Ng, Poh Kang Tan, Pei Lin Pearlin Toh, U-Xuan Tan

**分类**: cs.RO, cs.CV

**发布日期**: 2025-11-24

**备注**: 12 pages, 12 figures

**期刊**: X. Oh et al., "CNN-Based Camera Pose Estimation and Localization of Scan Images for Aircraft Visual Inspection," in IEEE Transactions on Intelligent Transportation Systems, vol. 25, no. 8, pp. 8629-8640, Aug. 2024

**DOI**: [10.1109/TITS.2024.3369653](https://doi.org/10.1109/TITS.2024.3369653)

---

## 💡 一句话要点

**提出基于CNN的飞机视觉检测相机位姿估计与定位方法，无需额外基础设施。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `相机位姿估计` `飞机视觉检测` `深度学习` `领域随机化` `卷积神经网络`

## 📋 核心要点

1. 传统飞机视觉检测依赖人工，耗时且易出错，在机场停机坪环境下自动化检测面临基础设施依赖和时间限制等挑战。
2. 该方法利用深度学习，通过在合成数据上训练CNN来估计相机位姿，无需额外标记或物理接触飞机表面，降低了部署难度。
3. 实验结果表明，该方法在真实飞机场景中实现了精确的相机位姿估计，为自动化飞机检测提供了可行的解决方案。

## 📝 摘要（中文）

本文提出了一种无需基础设施且易于部署的现场方法，用于估计平移-倾斜-变焦（PTZ）相机的位姿并定位扫描图像，旨在实现飞机外部损伤的自动化视觉检测。该方法利用深度卷积神经网络，仅在合成图像上进行微调，以预测相机自身位姿。通过应用领域随机化生成数据集，并利用飞机几何结构修改损失函数以提高精度。此外，还提出了初始化、扫描路径规划和PTZ相机图像精确定位的完整工作流程。通过真实飞机实验验证了该方法，相机位姿估计的均方根误差小于0.24米和2度。

## 🔬 方法详解

**问题定义**：论文旨在解决飞机视觉检测中相机位姿估计和图像定位的问题。现有方法通常依赖于基础设施，如标记点或预先构建的3D模型，这在机场停机坪等不受控的户外环境中难以实现。此外，许多航空公司和机场不允许接触飞机表面或使用无人机进行检测，进一步限制了现有方法的应用。因此，需要一种无需基础设施、易于部署且能在现场使用的相机位姿估计方法。

**核心思路**：论文的核心思路是利用深度学习，通过训练一个卷积神经网络（CNN）来直接从图像中预测相机的位姿。为了解决真实数据获取困难的问题，论文采用领域随机化技术生成大量的合成训练数据。此外，论文还利用飞机的几何结构信息来改进损失函数，从而提高位姿估计的精度。

**技术框架**：该方法包含以下几个主要步骤：1) 使用PTZ相机捕获飞机图像；2) 使用领域随机化技术生成合成训练数据；3) 使用合成数据微调一个预训练的CNN模型，使其能够预测相机的位姿；4) 利用飞机几何结构信息修改损失函数，进一步提高位姿估计精度；5) 结合初始化、扫描路径规划和精确定位，实现完整的飞机视觉检测流程。

**关键创新**：该方法最重要的技术创新点在于，它提出了一种完全基于深度学习的相机位姿估计方法，无需任何额外基础设施。通过领域随机化技术，该方法能够仅使用合成数据训练模型，并在真实场景中取得良好的效果。此外，利用飞机几何结构信息改进损失函数也是一个重要的创新点，能够显著提高位姿估计的精度。

**关键设计**：论文使用深度卷积神经网络作为位姿估计器，具体网络结构未知。关键设计包括：1) 领域随机化策略，用于生成多样化的合成训练数据，包括光照、纹理、背景等方面的随机变化；2) 基于飞机几何结构的损失函数，例如，可以利用飞机表面的法向量信息来约束位姿估计结果；3) 扫描路径规划算法，用于指导PTZ相机进行高效的图像采集。

## 📊 实验亮点

实验结果表明，该方法在真实飞机场景中实现了精确的相机位姿估计，相机位姿估计的均方根误差小于0.24米和2度。由于论文中没有明确指出对比的基线方法，因此无法给出具体的提升幅度。但该结果表明，即使仅使用合成数据进行训练，该方法也能在真实场景中取得良好的效果。

## 🎯 应用场景

该研究成果可应用于自动化飞机视觉检测，减少对人工的依赖，缩短飞机停机时间，提高检测效率和准确性。此外，该方法也可推广到其他需要进行相机位姿估计和定位的场景，如桥梁检测、建筑物巡检等，具有广泛的应用前景。

## 📄 摘要（原文）

> General Visual Inspection is a manual inspection process regularly used to detect and localise obvious damage on the exterior of commercial aircraft. There has been increasing demand to perform this process at the boarding gate to minimise the downtime of the aircraft and automating this process is desired to reduce the reliance on human labour. Automating this typically requires estimating a camera's pose with respect to the aircraft for initialisation but most existing localisation methods require infrastructure, which is very challenging in uncontrolled outdoor environments and within the limited turnover time (approximately 2 hours) on an airport tarmac. Additionally, many airlines and airports do not allow contact with the aircraft's surface or using UAVs for inspection between flights, and restrict access to commercial aircraft. Hence, this paper proposes an on-site method that is infrastructure-free and easy to deploy for estimating a pan-tilt-zoom camera's pose and localising scan images. This method initialises using the same pan-tilt-zoom camera used for the inspection task by utilising a Deep Convolutional Neural Network fine-tuned on only synthetic images to predict its own pose. We apply domain randomisation to generate the dataset for fine-tuning the network and modify its loss function by leveraging aircraft geometry to improve accuracy. We also propose a workflow for initialisation, scan path planning, and precise localisation of images captured from a pan-tilt-zoom camera. We evaluate and demonstrate our approach through experiments with real aircraft, achieving root-mean-square camera pose estimation errors of less than 0.24 m and 2 degrees for all real scenes.

