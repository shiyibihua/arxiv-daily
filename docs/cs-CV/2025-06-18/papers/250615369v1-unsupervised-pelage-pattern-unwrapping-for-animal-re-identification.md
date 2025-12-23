---
layout: default
title: Unsupervised Pelage Pattern Unwrapping for Animal Re-identification
---

# Unsupervised Pelage Pattern Unwrapping for Animal Re-identification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15369" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15369v1</a>
  <a href="https://arxiv.org/pdf/2506.15369.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15369v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15369v1', 'Unsupervised Pelage Pattern Unwrapping for Animal Re-identification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aleksandr Algasov, Ekaterina Nepovinnykh, Fedor Zolotarev, Tuomas Eerola, Heikki Kälviäinen, Pavel Zemčík, Charles V. Stewart

**分类**: cs.CV

**发布日期**: 2025-06-18

---

## 💡 一句话要点

**提出几何感知纹理映射以解决动物重识别中的皮毛模式扭曲问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `动物重识别` `几何感知` `纹理映射` `自监督学习` `特征匹配` `深度学习` `生态监测`

## 📋 核心要点

1. 现有的动物重识别方法在处理皮毛图案的几何扭曲时表现不佳，导致特征匹配的准确性下降。
2. 本文提出了一种几何感知的纹理映射方法，通过将皮毛图案展开到标准UV空间来增强特征匹配的鲁棒性。
3. 在海豹和豹子的数据集上，实验结果显示重识别准确率提高了最多5.4%，验证了方法的有效性。

## 📝 摘要（中文）

现有的个体重识别方法常常面临动物皮毛或皮肤图案因身体运动和姿态变化而产生的几何扭曲问题。本文提出了一种几何感知的纹理映射方法，将动物皮毛图案展开到标准的UV空间，从而实现更稳健的特征匹配。该方法利用表面法线估计来指导展开过程，同时保持3D表面与2D纹理空间之间的几何一致性。我们专注于两种具有挑战性的物种：萨伊马环斑海豹和豹子，这两种动物都有独特但高度可变形的皮毛图案。通过将我们的模式保持UV映射与现有的重识别技术相结合，我们在不同姿态和视角下展示了准确性的提升。我们的框架不需要真实的UV标注，并且可以以自监督的方式进行训练。实验结果表明，在海豹和豹子数据集上，重识别准确率提高了最多5.4%。

## 🔬 方法详解

**问题定义**：本文旨在解决动物重识别中皮毛图案因姿态变化而导致的几何扭曲问题。现有方法在处理这些可变形图案时，常常无法保持特征的一致性，影响识别效果。

**核心思路**：提出了一种几何感知的纹理映射方法，通过将皮毛图案展开到标准的UV空间，利用表面法线估计来指导展开过程，从而保持3D表面与2D纹理空间之间的几何一致性。

**技术框架**：该方法主要包括三个模块：首先进行表面法线估计，以获取皮毛图案的几何信息；其次进行纹理展开，将图案映射到标准UV空间；最后与现有的重识别技术结合，进行特征匹配和识别。

**关键创新**：本研究的创新点在于提出了一种无需真实UV标注的自监督学习方法，能够有效处理动物皮毛图案的几何扭曲问题，与传统方法相比，显著提高了重识别的准确性。

**关键设计**：在参数设置上，采用了适应性损失函数以优化纹理展开过程，并设计了深度学习网络结构以实现高效的特征提取和匹配。

## 📊 实验亮点

实验结果表明，采用本文提出的方法在海豹和豹子数据集上，重识别准确率提高了最多5.4%。与基线方法相比，本文方法在不同姿态和视角下的表现更加稳健，验证了其有效性。

## 🎯 应用场景

该研究在动物监测、生态保护和野生动物研究等领域具有广泛的应用潜力。通过提高动物重识别的准确性，可以更好地跟踪和研究动物行为，进而为保护濒危物种提供数据支持。此外，该方法的自监督学习特性也为其他领域的图像处理任务提供了新的思路。

## 📄 摘要（原文）

> Existing individual re-identification methods often struggle with the deformable nature of animal fur or skin patterns which undergo geometric distortions due to body movement and posture changes. In this paper, we propose a geometry-aware texture mapping approach that unwarps pelage patterns, the unique markings found on an animal's skin or fur, into a canonical UV space, enabling more robust feature matching. Our method uses surface normal estimation to guide the unwrapping process while preserving the geometric consistency between the 3D surface and the 2D texture space. We focus on two challenging species: Saimaa ringed seals (Pusa hispida saimensis) and leopards (Panthera pardus). Both species have distinctive yet highly deformable fur patterns. By integrating our pattern-preserving UV mapping with existing re-identification techniques, we demonstrate improved accuracy across diverse poses and viewing angles. Our framework does not require ground truth UV annotations and can be trained in a self-supervised manner. Experiments on seal and leopard datasets show up to a 5.4% improvement in re-identification accuracy.

