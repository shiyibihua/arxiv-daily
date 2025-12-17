---
layout: default
title: Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs
---

# Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs

**arXiv**: [2511.14315v1](https://arxiv.org/abs/2511.14315) | [PDF](https://arxiv.org/pdf/2511.14315.pdf)

**作者**: Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su

**分类**: cs.CV

**发布日期**: 2025-11-18

---

## 💡 一句话要点

**Dental3R：针对稀疏视角口腔照片，提出几何感知配对的3D重建方法**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `口腔3D重建` `稀疏视角重建` `几何感知配对` `3D高斯溅射` `小波正则化`

## 📋 核心要点

1. 传统口内扫描在远程正畸中受限，而基于稀疏图像的3D重建面临姿态估计不稳定和重建过度平滑的挑战。
2. Dental3R提出几何感知配对策略(GAPS)选择高质量图像对，并结合小波正则化3DGS模型，实现高保真重建。
3. 实验表明，Dental3R在稀疏、无姿态输入下表现出色，重建质量优于现有方法，尤其在牙齿咬合可视化方面。

## 📝 摘要（中文）

口腔内3D重建是数字化正畸的基础，但传统的口内扫描方法难以应用于远程正畸，后者通常依赖于稀疏的智能手机图像。虽然3D高斯溅射(3DGS)在novel view synthesis方面显示出潜力，但将其应用于标准的临床三元组（无姿势的前牙和双侧颊侧照片）具有挑战性。口腔环境中常见的大视角基线、不一致的照明和镜面反射表面会破坏同步姿势和几何估计的稳定性。此外，稀疏视角的光度监督通常会引入频率偏差，导致过度平滑的重建，从而丢失关键的诊断细节。为了解决这些限制，我们提出Dental3R，一种无需姿势、图引导的流程，用于从稀疏的口腔照片中进行鲁棒、高保真的重建。我们的方法首先构建几何感知配对策略(GAPS)，以智能地选择一个紧凑的、高价值图像对的子图。GAPS专注于对应匹配，从而提高了几何初始化的稳定性并减少了内存使用。在恢复的姿势和点云的基础上，我们使用小波正则化目标训练3DGS模型。通过使用离散小波变换强制执行带限保真度，我们的方法保留了精细的牙釉质边界和邻间边缘，同时抑制了高频伪影。我们在一个包含950个临床病例的大规模数据集和一个包含195个病例的基于视频的测试集上验证了我们的方法。实验结果表明，Dental3R有效地处理了稀疏的、无姿势的输入，并实现了卓越的novel view synthesis质量，用于牙齿咬合可视化，优于最先进的方法。

## 🔬 方法详解

**问题定义**：论文旨在解决从稀疏的、无姿态的口腔内照片中进行高精度3D重建的问题。现有方法，如直接应用3DGS，在面对口腔环境特有的挑战（大视角基线、光照不一致、镜面反射）时，姿态估计不稳定，且重建结果容易过度平滑，丢失牙齿表面的精细结构，影响诊断准确性。

**核心思路**：Dental3R的核心思路是利用几何信息指导图像配对，选择高质量的图像对进行初始几何估计，从而提高姿态估计的鲁棒性。同时，通过小波正则化约束3DGS模型的训练，在保留牙齿表面细节的同时抑制高频噪声，实现高保真重建。

**技术框架**：Dental3R包含两个主要阶段：1) 几何感知配对策略(GAPS)：构建图像对的图结构，并根据几何一致性指标选择高质量的图像对子集，用于初始姿态估计和点云重建。2) 小波正则化3DGS：利用初始姿态和点云，训练3DGS模型，并引入小波正则化项，约束重建结果的频率成分，防止过度平滑。

**关键创新**：Dental3R的关键创新在于：1) 提出了GAPS，通过几何信息指导图像配对，提高了稀疏视角下姿态估计的鲁棒性。2) 引入小波正则化，在3DGS训练过程中约束重建结果的频率成分，有效抑制了高频噪声，同时保留了牙齿表面的精细结构。与现有方法相比，Dental3R更有效地利用了图像间的几何信息，并针对口腔重建的特点进行了优化。

**关键设计**：GAPS中，几何一致性指标包括视角差异、特征匹配质量等。小波正则化项基于离散小波变换，对3DGS模型输出的密度场进行分解，并对高频分量进行惩罚。具体的损失函数包括光度损失、深度损失和小波正则化损失。论文中没有明确给出具体的参数设置，这部分信息可能在补充材料中。

## 📊 实验亮点

Dental3R在包含950个临床病例的大规模数据集和195个基于视频的测试集上进行了验证。实验结果表明，Dental3R在稀疏、无姿态输入下表现出色，实现了卓越的novel view synthesis质量，优于现有方法。具体性能数据和对比基线的信息未在摘要中明确给出，可能在论文正文中。

## 🎯 应用场景

Dental3R技术可应用于远程正畸、数字化牙科诊断和治疗规划等领域。通过智能手机拍摄的稀疏口腔照片，即可重建高精度的3D模型，方便医生进行远程诊断和制定个性化治疗方案，降低患者就医成本，提高医疗效率。该技术还有潜力应用于口腔健康监测、牙科教育等领域。

## 📄 摘要（原文）

> Intraoral 3D reconstruction is fundamental to digital orthodontics, yet conventional methods like intraoral scanning are inaccessible for remote tele-orthodontics, which typically relies on sparse smartphone imagery. While 3D Gaussian Splatting (3DGS) shows promise for novel view synthesis, its application to the standard clinical triad of unposed anterior and bilateral buccal photographs is challenging. The large view baselines, inconsistent illumination, and specular surfaces common in intraoral settings can destabilize simultaneous pose and geometry estimation. Furthermore, sparse-view photometric supervision often induces a frequency bias, leading to over-smoothed reconstructions that lose critical diagnostic details. To address these limitations, we propose \textbf{Dental3R}, a pose-free, graph-guided pipeline for robust, high-fidelity reconstruction from sparse intraoral photographs. Our method first constructs a Geometry-Aware Pairing Strategy (GAPS) to intelligently select a compact subgraph of high-value image pairs. The GAPS focuses on correspondence matching, thereby improving the stability of the geometry initialization and reducing memory usage. Building on the recovered poses and point cloud, we train the 3DGS model with a wavelet-regularized objective. By enforcing band-limited fidelity using a discrete wavelet transform, our approach preserves fine enamel boundaries and interproximal edges while suppressing high-frequency artifacts. We validate our approach on a large-scale dataset of 950 clinical cases and an additional video-based test set of 195 cases. Experimental results demonstrate that Dental3R effectively handles sparse, unposed inputs and achieves superior novel view synthesis quality for dental occlusion visualization, outperforming state-of-the-art methods.

