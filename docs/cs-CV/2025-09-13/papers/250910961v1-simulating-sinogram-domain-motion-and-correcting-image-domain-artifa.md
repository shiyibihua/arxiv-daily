---
layout: default
title: Simulating Sinogram-Domain Motion and Correcting Image-Domain Artifacts Using Deep Learning in HR-pQCT Bone Imaging
---

# Simulating Sinogram-Domain Motion and Correcting Image-Domain Artifacts Using Deep Learning in HR-pQCT Bone Imaging

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10961" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10961v1</a>
  <a href="https://arxiv.org/pdf/2509.10961.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10961v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10961v1', 'Simulating Sinogram-Domain Motion and Correcting Image-Domain Artifacts Using Deep Learning in HR-pQCT Bone Imaging')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Farhan Sadik, Christopher L. Newman, Stuart J. Warden, Rachel K. Surowiec

**分类**: cs.CV

**发布日期**: 2025-09-13

---

## 💡 一句话要点

**提出ESWGAN-GP模型，用于HR-pQCT骨骼成像中运动伪影的模拟与图像域校正**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `HR-pQCT` `运动伪影校正` `深度学习` `生成对抗网络` `骨骼成像`

## 📋 核心要点

1. HR-pQCT成像易受运动伪影影响，导致骨骼微结构评估不准确，缺乏有效的运动校正方法。
2. 提出ESWGAN-GP模型，利用正弦图模拟运动伪影，构建配对数据集，实现监督学习的运动校正。
3. 实验结果表明，ESWGAN-GP在模拟和真实数据集上均表现出良好的运动伪影校正效果，提高了图像质量。

## 📝 摘要（中文）

刚性运动伪影，如皮质骨条纹和骨小梁模糊，阻碍了高分辨率外周定量计算机断层扫描(HR-pQCT)对骨骼微结构的体内评估。尽管有各种运动分级技术，但由于缺乏标准化的退化模型，目前还没有运动校正方法。本文优化了一种传统的基于正弦图的方法来模拟HR-pQCT图像中的运动伪影，创建了运动损坏图像及其对应ground truth的配对数据集，从而能够无缝集成到监督学习框架中进行运动校正。因此，我们提出了一种边缘增强的自注意力Wasserstein生成对抗网络与梯度惩罚(ESWGAN-GP)来解决模拟(源)和真实(目标)数据集中的运动伪影。该模型结合了边缘增强跳跃连接以保留骨小梁边缘，并结合了自注意力机制以捕获长程依赖关系，从而促进运动校正。使用基于视觉几何组(VGG)的感知损失来重建精细的微结构特征。ESWGAN-GP在源数据集上实现了26.78的平均信噪比(SNR)、0.81的结构相似性指数(SSIM)和0.76的视觉信息保真度(VIF)，同时在目标数据集上表现出更高的性能，SNR为29.31，SSIM为0.87，VIF为0.81。所提出的方法解决了一种简化的真实运动表示，可能无法完全捕捉体内运动伪影的复杂性。尽管如此，由于运动伪影是该模式更广泛应用的主要挑战之一，这些方法代表了在HR-pQCT中实施基于深度学习的运动校正的重要初步步骤。

## 🔬 方法详解

**问题定义**：HR-pQCT成像中，患者的微小移动会导致图像出现伪影，例如皮质骨条纹和骨小梁模糊，严重影响骨骼微结构的准确评估。现有方法主要集中在运动分级，缺乏有效的运动校正方法，原因是缺乏标准化的运动退化模型，难以进行有效的校正。

**核心思路**：论文的核心思路是首先通过优化传统的基于正弦图的方法来模拟HR-pQCT图像中的运动伪影，从而生成带有ground truth的配对数据集。然后，利用这些配对数据训练一个深度学习模型，使其能够学习如何从运动伪影图像中恢复出清晰的图像。这种方法将运动校正问题转化为一个监督学习问题，从而可以利用深度学习的强大能力。

**技术框架**：整体框架包括两个主要阶段：运动伪影模拟阶段和运动校正阶段。在运动伪影模拟阶段，使用优化的正弦图方法生成带有运动伪影的图像及其对应的ground truth。在运动校正阶段，使用ESWGAN-GP模型对带有运动伪影的图像进行处理，以恢复出清晰的图像。ESWGAN-GP模型是一个生成对抗网络，包含生成器和判别器，生成器负责生成清晰的图像，判别器负责区分生成的图像和真实的图像。

**关键创新**：论文的关键创新在于以下几个方面：1) 提出了一种优化的正弦图方法来模拟HR-pQCT图像中的运动伪影，从而生成了带有ground truth的配对数据集。2) 提出了ESWGAN-GP模型，该模型结合了边缘增强跳跃连接和自注意力机制，能够更好地保留骨小梁边缘并捕获长程依赖关系。3) 使用了基于VGG的感知损失来重建精细的微结构特征。

**关键设计**：ESWGAN-GP模型中，边缘增强跳跃连接通过在跳跃连接中加入边缘检测算子来增强对骨小梁边缘的保留。自注意力机制通过计算图像中不同区域之间的相关性来捕获长程依赖关系。基于VGG的感知损失通过比较生成图像和真实图像在VGG网络中的特征表示来重建精细的微结构特征。梯度惩罚被用于稳定GAN的训练过程。具体的网络结构和参数设置在论文中有详细描述。

## 📊 实验亮点

ESWGAN-GP模型在模拟数据集上取得了显著的性能提升，信噪比(SNR)达到26.78，结构相似性指数(SSIM)为0.81，视觉信息保真度(VIF)为0.76。更重要的是，该模型在真实数据集上也表现出优异的性能，SNR达到29.31，SSIM为0.87，VIF为0.81，表明该模型具有良好的泛化能力，能够有效校正真实HR-pQCT图像中的运动伪影。

## 🎯 应用场景

该研究成果可应用于HR-pQCT骨骼成像领域，提高骨骼微结构评估的准确性和可靠性。通过校正运动伪影，可以更准确地诊断骨质疏松症等骨骼疾病，并为药物研发和临床试验提供更可靠的数据。该方法还可推广到其他医学成像领域，用于校正各种运动伪影，提高图像质量。

## 📄 摘要（原文）

> Rigid-motion artifacts, such as cortical bone streaking and trabecular smearing, hinder in vivo assessment of bone microstructures in high-resolution peripheral quantitative computed tomography (HR-pQCT). Despite various motion grading techniques, no motion correction methods exist due to the lack of standardized degradation models. We optimize a conventional sinogram-based method to simulate motion artifacts in HR-pQCT images, creating paired datasets of motion-corrupted images and their corresponding ground truth, which enables seamless integration into supervised learning frameworks for motion correction. As such, we propose an Edge-enhanced Self-attention Wasserstein Generative Adversarial Network with Gradient Penalty (ESWGAN-GP) to address motion artifacts in both simulated (source) and real-world (target) datasets. The model incorporates edge-enhancing skip connections to preserve trabecular edges and self-attention mechanisms to capture long-range dependencies, facilitating motion correction. A visual geometry group (VGG)-based perceptual loss is used to reconstruct fine micro-structural features. The ESWGAN-GP achieves a mean signal-to-noise ratio (SNR) of 26.78, structural similarity index measure (SSIM) of 0.81, and visual information fidelity (VIF) of 0.76 for the source dataset, while showing improved performance on the target dataset with an SNR of 29.31, SSIM of 0.87, and VIF of 0.81. The proposed methods address a simplified representation of real-world motion that may not fully capture the complexity of in vivo motion artifacts. Nevertheless, because motion artifacts present one of the foremost challenges to more widespread adoption of this modality, these methods represent an important initial step toward implementing deep learning-based motion correction in HR-pQCT.

