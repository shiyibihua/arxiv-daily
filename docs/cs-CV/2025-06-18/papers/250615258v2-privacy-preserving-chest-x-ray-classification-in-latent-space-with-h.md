---
layout: default
title: Privacy-Preserving Chest X-ray Classification in Latent Space with Homomorphically Encrypted Neural Inference
---

# Privacy-Preserving Chest X-ray Classification in Latent Space with Homomorphically Encrypted Neural Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15258" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15258v2</a>
  <a href="https://arxiv.org/pdf/2506.15258.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15258v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15258v2', 'Privacy-Preserving Chest X-ray Classification in Latent Space with Homomorphically Encrypted Neural Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jonghun Kim, Gyeongdeok Jo, Sinyoung Ra, Hyunjin Park

**分类**: eess.IV, cs.CV

**发布日期**: 2025-06-18 (更新: 2025-06-20)

**备注**: 11 pages, 5 figures

---

## 💡 一句话要点

**提出同态加密神经推理框架以保护胸部X光图像隐私**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `同态加密` `医疗影像` `隐私保护` `深度学习` `图像压缩` `多标签分类`

## 📋 核心要点

1. 现有的同态加密推理方法计算开销大，尤其是在处理大型医疗图像时，难以满足实时应用需求。
2. 本研究提出了一种通过VQGAN压缩图像为潜在表示的HE推理框架，显著降低了计算负担。
3. 在两个胸部X光数据集上进行的多标签分类任务中，尽管HE推理速度较慢，但显示出良好的实际应用潜力。

## 📝 摘要（中文）

医疗影像数据包含敏感的患者信息，需要强有力的隐私保护。许多分析设置要求将数据发送到服务器进行推理。同态加密（HE）提供了一种解决方案，允许在加密数据上进行计算而不暴露原始信息。然而，HE推理计算开销较大，尤其是对于大型图像（如胸部X光）。本研究提出了一种HE推理框架，通过使用VQGAN将图像压缩为潜在表示，显著降低计算负担，同时保持图像质量。我们用低阶多项式近似激活函数，以平衡准确性和效率。实验表明，压缩的下采样因子为八时，性能与计算成本之间达到了最佳平衡。我们还改进了已知能提升传统CNN的挤压与激励模块，以增强HE框架。尽管HE推理仍然相对较慢，并且与未加密推理相比引入了轻微的性能差异，但我们的方法在医疗图像中显示出强大的实际应用潜力。

## 🔬 方法详解

**问题定义**：本研究旨在解决医疗影像数据在推理过程中隐私保护不足的问题。现有的同态加密推理方法在处理大型图像时计算开销过大，难以应用于实际场景。

**核心思路**：提出一种同态加密推理框架，通过VQGAN将图像压缩为潜在表示，从而降低计算负担，同时保持图像质量。采用低阶多项式近似激活函数，以平衡准确性与效率。

**技术框架**：整体架构包括图像压缩模块（VQGAN）、同态加密推理模块和分类模块。首先使用VQGAN对图像进行压缩，然后在加密状态下进行推理，最后进行多标签分类。

**关键创新**：最重要的技术创新在于结合了VQGAN与同态加密推理，显著降低了计算复杂度，同时保持了图像的有效信息。与传统方法相比，该框架在隐私保护与计算效率之间取得了更好的平衡。

**关键设计**：在设计中，采用了压缩下采样因子为八的策略，以优化性能与计算成本的平衡。此外，改进了挤压与激励模块，以增强CNN的表现，确保在HE框架下的有效性。

## 📊 实验亮点

实验结果表明，采用压缩下采样因子为八的策略，能够在性能与计算成本之间实现最佳平衡。尽管HE推理速度较慢，但在两个胸部X光数据集上的多标签分类任务中，表现出良好的分类能力，显示出该方法的实际应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括医疗影像分析、远程医疗和数据隐私保护等。通过在不暴露患者敏感信息的情况下进行有效推理，该方法为医疗行业提供了一种安全的解决方案，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Medical imaging data contain sensitive patient information requiring strong privacy protection. Many analytical setups require data to be sent to a server for inference purposes. Homomorphic encryption (HE) provides a solution by allowing computations to be performed on encrypted data without revealing the original information. However, HE inference is computationally expensive, particularly for large images (e.g., chest X-rays). In this study, we propose an HE inference framework for medical images that uses VQGAN to compress images into latent representations, thereby significantly reducing the computational burden while preserving image quality. We approximate the activation functions with lower-degree polynomials to balance the accuracy and efficiency in compliance with HE requirements. We observed that a downsampling factor of eight for compression achieved an optimal balance between performance and computational cost. We further adapted the squeeze and excitation module, which is known to improve traditional CNNs, to enhance the HE framework. Our method was tested on two chest X-ray datasets for multi-label classification tasks using vanilla CNN backbones. Although HE inference remains relatively slow and introduces minor performance differences compared with unencrypted inference, our approach shows strong potential for practical use in medical images

