---
layout: default
title: Spatial-Frequency Enhanced Mamba for Multi-Modal Image Fusion
---

# Spatial-Frequency Enhanced Mamba for Multi-Modal Image Fusion

**arXiv**: [2511.06593v1](https://arxiv.org/abs/2511.06593) | [PDF](https://arxiv.org/pdf/2511.06593.pdf)

**作者**: Hui Sun, Long Lv, Pingping Zhang, Tongdan Tang, Feng Tian, Weibing Sun, Huchuan Lu

**分类**: cs.CV

**发布日期**: 2025-11-10

**备注**: This work is accepted by IEEE Transactions on Image Processing. More modifications may be performed

**🔗 代码/项目**: [GITHUB](https://github.com/SunHui1216/SFMFusion)

---

## 💡 一句话要点

**提出空间-频率增强Mamba融合网络，提升多模态图像融合性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多模态图像融合` `Mamba模型` `空间频率增强` `动态特征融合` `图像重建` `深度学习`

## 📋 核心要点

1. 现有MMIF方法受限于CNN的感受野和Transformer的计算复杂度，难以充分提取多模态图像的互补信息。
2. SFMFusion框架通过空间-频率增强Mamba块和动态融合机制，提升Mamba模型在多模态图像融合中的特征提取和融合能力。
3. 实验结果表明，SFMFusion在多个数据集上超越了现有SOTA方法，验证了其有效性。

## 📝 摘要（中文）

多模态图像融合（MMIF）旨在整合来自不同模态的互补图像信息，以生成信息丰富的图像。以往基于深度学习的MMIF方法通常采用卷积神经网络（CNN）或Transformer进行特征提取。然而，由于CNN感受野有限和Transformer计算成本高昂，这些方法表现不尽如人意。最近，Mamba展示了在线性复杂度下建模长程依赖关系的强大潜力，为MMIF提供了一个有希望的解决方案。不幸的是，Mamba缺乏完整的空间和频率感知，这对于MMIF非常重要。此外，采用图像重建（IR）作为辅助任务已被证明对MMIF有益。然而，一个主要的挑战是如何有效利用IR。为了解决上述问题，我们提出了一种名为空间-频率增强Mamba融合（SFMFusion）的新型MMIF框架。更具体地说，我们首先提出了一个三分支结构来耦合MMIF和IR，这可以保留来自源图像的完整内容。然后，我们提出了空间-频率增强Mamba块（SFMB），它可以增强Mamba在空间和频率域中的能力，以进行全面的特征提取。最后，我们提出了动态融合Mamba块（DFMB），它可以部署在不同的分支中以进行动态特征融合。大量实验表明，我们的方法在六个MMIF数据集上取得了比大多数最先进方法更好的结果。源代码可在https://github.com/SunHui1216/SFMFusion获得。

## 🔬 方法详解

**问题定义**：多模态图像融合旨在将来自不同模态的图像信息（如红外和可见光图像）进行有效融合，生成包含更多信息的图像。现有方法，如基于CNN和Transformer的方法，存在感受野不足或计算复杂度过高的问题，难以充分提取和利用多模态图像的互补信息，导致融合效果不佳。

**核心思路**：论文的核心思路是利用Mamba模型建模长程依赖关系的能力，并针对Mamba在空间和频率感知方面的不足，进行增强。同时，引入图像重建作为辅助任务，并设计三分支结构，以保留源图像的完整内容。通过动态融合机制，实现不同分支之间的信息交互，从而提升融合效果。

**技术框架**：SFMFusion框架包含三个主要分支：两个分支分别处理来自不同模态的源图像，第三个分支用于图像重建。每个分支都包含多个空间-频率增强Mamba块（SFMB）。此外，还设计了动态融合Mamba块（DFMB），用于在不同分支之间进行动态特征融合。最终，通过融合后的特征重建出融合图像。

**关键创新**：论文的关键创新在于提出了空间-频率增强Mamba块（SFMB）和动态融合Mamba块（DFMB）。SFMB通过引入空间和频率域的增强机制，弥补了Mamba模型在空间和频率感知方面的不足。DFMB则实现了不同分支之间的动态特征融合，从而更好地利用了多模态图像的互补信息。与现有方法相比，SFMFusion能够更有效地提取和融合多模态图像的特征，从而获得更好的融合效果。

**关键设计**：SFMB的设计包括空间注意力机制和频率注意力机制，用于增强Mamba模型在空间和频率域的感知能力。DFMB的设计则基于注意力机制，用于动态地调整不同分支特征的权重，从而实现更有效的特征融合。此外，论文还采用了L1损失和结构相似性损失（SSIM）作为损失函数，用于优化网络参数。

## 📊 实验亮点

实验结果表明，SFMFusion在六个公开的多模态图像融合数据集上均取得了优于现有SOTA方法的结果。例如，在VVIF数据集上，SFMFusion在多种评价指标上均取得了显著提升，如在NIQE指标上优于第二名方法超过0.1。这些结果验证了SFMFusion在多模态图像融合方面的有效性和优越性。

## 🎯 应用场景

该研究成果可应用于医学图像融合（如CT和MRI图像融合）、遥感图像融合（如可见光和红外图像融合）、以及自动驾驶等领域。通过融合不同模态的图像信息，可以提高图像的清晰度和信息量，从而为后续的图像分析、目标检测和决策提供更可靠的基础。未来，该方法有望在更多多模态图像处理任务中发挥重要作用。

## 📄 摘要（原文）

> Multi-Modal Image Fusion (MMIF) aims to integrate complementary image information from different modalities to produce informative images. Previous deep learning-based MMIF methods generally adopt Convolutional Neural Networks (CNNs) or Transformers for feature extraction. However, these methods deliver unsatisfactory performances due to the limited receptive field of CNNs and the high computational cost of Transformers. Recently, Mamba has demonstrated a powerful potential for modeling long-range dependencies with linear complexity, providing a promising solution to MMIF. Unfortunately, Mamba lacks full spatial and frequency perceptions, which are very important for MMIF. Moreover, employing Image Reconstruction (IR) as an auxiliary task has been proven beneficial for MMIF. However, a primary challenge is how to leverage IR efficiently and effectively. To address the above issues, we propose a novel framework named Spatial-Frequency Enhanced Mamba Fusion (SFMFusion) for MMIF. More specifically, we first propose a three-branch structure to couple MMIF and IR, which can retain complete contents from source images. Then, we propose the Spatial-Frequency Enhanced Mamba Block (SFMB), which can enhance Mamba in both spatial and frequency domains for comprehensive feature extraction. Finally, we propose the Dynamic Fusion Mamba Block (DFMB), which can be deployed across different branches for dynamic feature fusion. Extensive experiments show that our method achieves better results than most state-of-the-art methods on six MMIF datasets. The source code is available at https://github.com/SunHui1216/SFMFusion.

