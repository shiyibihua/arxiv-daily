---
layout: default
title: Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model
---

# Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15220" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15220v1</a>
  <a href="https://arxiv.org/pdf/2509.15220.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15220v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15220v1', 'Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fangjinhua Wang, Qingshan Xu, Yew-Soon Ong, Marc Pollefeys

**分类**: cs.CV

**发布日期**: 2025-09-18

**备注**: Accepted to IEEE T-PAMI 2025. Code: https://github.com/cvg/diffmvs

**DOI**: [10.1109/TPAMI.2025.3597148](https://doi.org/10.1109/TPAMI.2025.3597148)

**🔗 代码/项目**: [GITHUB](https://github.com/cvg/diffmvs)

---

## 💡 一句话要点

**提出基于置信度感知扩散模型的高效轻量多视图立体方法**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `多视图立体` `三维重建` `扩散模型` `深度估计` `条件生成`

## 📋 核心要点

1. 现有基于学习的MVS方法计算效率较低，难以在资源受限的场景中应用。
2. 论文提出将扩散模型引入MVS，通过条件扩散过程进行深度图细化，并设计置信度引导的采样策略。
3. 实验表明，提出的DiffMVS在效率上具有竞争力，CasDiffMVS在多个数据集上取得了SOTA性能。

## 📝 摘要（中文）

本文提出了一种新颖的多视图立体（MVS）框架，该框架将扩散模型引入MVS中，用于从校准图像重建3D几何体。该方法将深度细化建模为条件扩散过程，并设计了一个条件编码器来指导扩散过程，从而利用深度估计的判别特性。为了提高效率，设计了一种结合轻量级2D U-Net和卷积GRU的新型扩散网络。此外，提出了一种基于置信度的新型采样策略，以基于扩散模型估计的置信度自适应地采样深度假设。基于此框架，提出了两种新的MVS方法：DiffMVS和CasDiffMVS。DiffMVS在运行时间和GPU内存方面实现了与最先进方法相当的性能。CasDiffMVS在DTU、Tanks & Temples和ETH3D上实现了最先进的性能。

## 🔬 方法详解

**问题定义**：多视图立体（MVS）旨在从多张校准图像中重建三维几何结构。现有的基于学习的MVS方法通常先进行多视图深度估计，然后将深度图融合为网格或点云。为了提高计算效率，许多方法首先初始化一个粗糙的深度图，然后在更高的分辨率下逐步细化它。然而，这些方法在计算效率和精度之间往往需要权衡，难以同时满足轻量化和高精度的需求。

**核心思路**：本文的核心思路是将深度图的细化过程建模为一个条件扩散过程。扩散模型在生成任务中表现出色，它从随机噪声开始，通过迭代去噪过程逐步恢复样本。通过将深度图细化视为一个条件生成问题，可以利用扩散模型的强大生成能力来提升深度图的质量。同时，为了提高效率，设计轻量级的网络结构和采样策略。

**技术框架**：该MVS框架主要包含以下几个模块：1) 条件编码器：用于提取输入图像的特征，并将其作为条件信息输入到扩散模型中。2) 扩散模型：采用轻量级的2D U-Net和卷积GRU相结合的网络结构，用于逐步细化深度图。3) 置信度估计模块：基于扩散模型的输出，估计每个深度假设的置信度。4) 采样策略：根据置信度自适应地采样深度假设，以提高效率。整体流程是从粗糙的深度图开始，通过条件编码器提取图像特征，然后利用扩散模型逐步细化深度图，并使用置信度引导的采样策略来提高效率。

**关键创新**：该论文的关键创新点在于将扩散模型引入到MVS中，并将其用于深度图的细化。与传统的深度图细化方法相比，扩散模型具有更强的生成能力，可以生成更精细、更准确的深度图。此外，提出的置信度引导的采样策略可以有效地提高计算效率，并减少内存占用。

**关键设计**：在网络结构方面，采用了轻量级的2D U-Net和卷积GRU相结合的方式，以减少计算量和内存占用。在损失函数方面，使用了L1损失和感知损失相结合的方式，以提高深度图的质量。在采样策略方面，根据置信度自适应地采样深度假设，以平衡精度和效率。具体的参数设置和网络结构细节可以在论文的实验部分找到。

## 📊 实验亮点

DiffMVS在运行时间和GPU内存方面实现了与最先进方法相当的性能，表明了该方法的效率优势。CasDiffMVS在DTU、Tanks & Temples和ETH3D等多个数据集上取得了state-of-the-art的性能，验证了该方法的有效性和泛化能力。代码已开源，方便研究人员复现和进一步研究。

## 🎯 应用场景

该研究成果可应用于三维重建、自动驾驶、机器人导航、虚拟现实等领域。轻量化的设计使得该方法能够在移动设备或嵌入式系统上部署，从而实现实时的三维重建和场景理解。高精度的重建结果可以为自动驾驶系统提供更准确的环境信息，提高其安全性和可靠性。

## 📄 摘要（原文）

> To reconstruct the 3D geometry from calibrated images, learning-based multi-view stereo (MVS) methods typically perform multi-view depth estimation and then fuse depth maps into a mesh or point cloud. To improve the computational efficiency, many methods initialize a coarse depth map and then gradually refine it in higher resolutions. Recently, diffusion models achieve great success in generation tasks. Starting from a random noise, diffusion models gradually recover the sample with an iterative denoising process. In this paper, we propose a novel MVS framework, which introduces diffusion models in MVS. Specifically, we formulate depth refinement as a conditional diffusion process. Considering the discriminative characteristic of depth estimation, we design a condition encoder to guide the diffusion process. To improve efficiency, we propose a novel diffusion network combining lightweight 2D U-Net and convolutional GRU. Moreover, we propose a novel confidence-based sampling strategy to adaptively sample depth hypotheses based on the confidence estimated by diffusion model. Based on our novel MVS framework, we propose two novel MVS methods, DiffMVS and CasDiffMVS. DiffMVS achieves competitive performance with state-of-the-art efficiency in run-time and GPU memory. CasDiffMVS achieves state-of-the-art performance on DTU, Tanks & Temples and ETH3D. Code is available at: https://github.com/cvg/diffmvs.

