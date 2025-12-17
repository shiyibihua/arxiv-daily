---
layout: default
title: Weakly Supervised Pneumonia Localization from Chest X-Rays Using Deep Neural Network and Grad-CAM Explanations
---

# Weakly Supervised Pneumonia Localization from Chest X-Rays Using Deep Neural Network and Grad-CAM Explanations

**arXiv**: [2511.00456v4](https://arxiv.org/abs/2511.00456) | [PDF](https://arxiv.org/pdf/2511.00456.pdf)

**作者**: Kiran Shahi, Anup Bagale

**分类**: cs.CV

**发布日期**: 2025-11-01 (更新: 2025-12-16)

**备注**: https://github.com/kiranshahi/pneumonia-analysis

---

## 💡 一句话要点

**提出基于弱监督深度学习和Grad-CAM的肺炎定位方法，提升胸部X光片诊断效率。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `弱监督学习` `肺炎定位` `胸部X光片` `深度学习` `Grad-CAM` `可解释AI` `医学影像分析`

## 📋 核心要点

1. 胸部X光片肺炎定位依赖像素级标注，成本高昂且耗时，限制了诊断效率。
2. 利用图像级标签和Grad-CAM，生成肺炎感染区域热图，实现弱监督肺炎定位。
3. 实验表明，多种模型准确率达96-98%，Grad-CAM热图关注临床相关肺部区域。

## 📝 摘要（中文）

本研究提出了一种基于弱监督深度学习框架，结合梯度加权类激活映射(Grad-CAM)的肺炎分类和定位方法。该方法无需像素级标注，仅利用图像级标签生成具有临床意义的热图，突出显示肺炎感染区域。研究评估了七种预训练深度学习模型，包括Vision Transformer，在相同的训练条件下，使用focal loss和患者级划分以防止数据泄露。实验结果表明，所有模型均达到较高的准确率(96-98%)，其中ResNet-18和EfficientNet-B0表现最佳，MobileNet-V2提供了一种高效的轻量级替代方案。Grad-CAM热图可视化结果证实，该方法关注于临床相关的肺部区域，支持使用可解释AI进行放射诊断。总而言之，这项工作突出了弱监督、可解释模型在增强AI辅助肺炎筛查的透明度和临床信任方面的潜力。

## 🔬 方法详解

**问题定义**：该论文旨在解决胸部X光片中肺炎病灶的精确定位问题。现有方法通常依赖于耗时且昂贵的像素级标注数据进行训练，这限制了其在实际临床应用中的可扩展性。因此，如何仅利用图像级别的标签信息，实现对肺炎病灶的有效定位，是本研究要解决的核心问题。

**核心思路**：论文的核心思路是利用弱监督学习方法，结合深度学习模型和可解释性技术Grad-CAM，实现肺炎病灶的定位。通过图像级别的标签信息训练深度学习模型，然后利用Grad-CAM生成热图，突出显示图像中与肺炎相关的区域。这种方法无需像素级别的标注，降低了数据标注成本，同时提高了模型的实用性。

**技术框架**：该框架主要包含以下几个步骤：1) 数据预处理：对胸部X光片进行预处理，例如调整大小、归一化等。2) 模型训练：使用图像级别的标签信息训练深度学习模型，例如ResNet、EfficientNet等。3) 热图生成：利用训练好的模型和Grad-CAM技术，生成热图，突出显示图像中与肺炎相关的区域。4) 结果评估：通过可视化热图和计算相关指标，评估模型的定位性能。

**关键创新**：该论文的关键创新在于将弱监督学习和可解释性技术Grad-CAM相结合，用于肺炎病灶的定位。与传统的需要像素级别标注的方法相比，该方法只需要图像级别的标签信息，大大降低了数据标注成本。同时，Grad-CAM生成的热图可以提供模型预测的可解释性，有助于医生理解模型的决策过程，增强对模型的信任。

**关键设计**：论文中使用了focal loss作为损失函数，以解决类别不平衡问题。同时，为了防止数据泄露，采用了患者级别的划分方式，确保训练集和测试集来自不同的患者。此外，论文还评估了多种预训练深度学习模型，包括ResNet、EfficientNet和Vision Transformer，并比较了它们的性能。

## 📊 实验亮点

实验结果表明，所有模型均达到较高的准确率(96-98%)，其中ResNet-18和EfficientNet-B0表现最佳。Grad-CAM热图可视化结果证实，该方法关注于临床相关的肺部区域。该研究验证了弱监督学习和可解释性技术在肺炎定位中的有效性。

## 🎯 应用场景

该研究成果可应用于AI辅助的肺炎筛查和诊断，帮助医生快速准确地定位病灶区域，提高诊断效率和准确性。此外，该方法还可推广到其他医学影像分析任务中，例如肺结节检测、肿瘤分割等，具有广泛的应用前景和临床价值。

## 📄 摘要（原文）

> Chest X-ray imaging is commonly used to diagnose pneumonia, but accurately localizing the pneumonia affected regions typically requires detailed pixel-level annotations, which are costly and time consuming to obtain. To address this limitation, this study proposes a weakly supervised deep learning framework for pneumonia classification and localization using Gradient-weighted Class Activation Mapping (Grad-CAM). Instead of relying on costly pixel-level annotations, the proposed method utilizes image-level labels to generate clinically meaningful heatmaps that highlight pneumonia affected regions. Furthermore, we evaluate seven pre-trained deep learning models including a Vision Transformer under identical training conditions, using focal loss and patient-wise splits to prevent data leakage. Experimental results suggest that all models achieved high accuracy (96-98%), with ResNet-18 and EfficientNet-B0 showing the best overall performance and MobileNet-V2 providing an efficient lightweight alternative. Grad-CAM heatmap visualizations in this study confirm that the proposed methods focus on clinically relevant lung regions, supporting the use of explainable AI for radiological diagnostics. Overall, this work highlights the potential of weakly supervised, explainable models that enhance transparency and clinical trust in AI-assisted pneumonia screening.

