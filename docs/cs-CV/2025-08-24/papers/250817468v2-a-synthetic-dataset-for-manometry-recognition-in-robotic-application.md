---
layout: default
title: A Synthetic Dataset for Manometry Recognition in Robotic Applications
---

# A Synthetic Dataset for Manometry Recognition in Robotic Applications

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17468" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17468v2</a>
  <a href="https://arxiv.org/pdf/2508.17468.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17468v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17468v2', 'A Synthetic Dataset for Manometry Recognition in Robotic Applications')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pedro Antonio Rabelo Saraiva, Enzo Ferreira de Souza, Joao Manoel Herrera Pinheiro, Thiago H. Segreto, Ricardo V. Godoy, Marcelo Becker

**分类**: cs.CV, cs.AI, cs.LG, cs.RO

**发布日期**: 2025-08-24 (更新: 2025-10-11)

**期刊**: 2025 Latin American Robotics Symposium (LARS)

**DOI**: [10.1109/LARS69345.2025.11272958](https://doi.org/10.1109/LARS69345.2025.11272958)

---

## 💡 一句话要点

**提出混合数据合成方法以解决工业环境数据稀缺问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `数据合成` `物体检测` `程序渲染` `AI视频生成` `工业应用` `YOLO检测器` `安全监控`

## 📋 核心要点

1. 现有方法在复杂工业环境中面临数据稀缺和高成本的问题，限制了自主检测系统的发展。
2. 论文提出了一种混合数据合成管道，结合程序渲染和AI驱动的视频生成，以生成高质量的合成数据。
3. 实验结果表明，基于合成数据集训练的YOLO检测器在准确性上优于仅使用真实数据训练的模型，1:1的样本比例实现了最佳效果。

## 📝 摘要（中文）

本文针对复杂工业环境（如海上油气平台）中数据稀缺和高获取成本的问题，提出了一种混合数据合成管道，结合了程序渲染和AI驱动的视频生成。该方法使用BlenderProc生成具有领域随机化的逼真图像，并利用NVIDIA的Cosmos-Predict2生成具有时间变化的物理一致视频序列。通过在合成数据集上训练基于YOLO的检测器，结果显示与仅使用真实图像训练的模型相比，合成数据集的检测器表现更佳。1:1的真实与合成样本比例达到了最高的准确率，表明合成数据生成是一种可行、经济且安全的策略，适用于安全关键和资源受限的工业应用。

## 🔬 方法详解

**问题定义**：本文旨在解决在复杂工业环境中，尤其是海上油气平台，数据稀缺和高获取成本的问题。现有方法在这些危险环境中数据收集受限，导致自主检测系统的发展受到阻碍。

**核心思路**：论文提出的核心思路是通过混合数据合成管道，结合程序渲染和AI驱动的视频生成，来生成高质量的合成数据，从而提高模型的检测性能。

**技术框架**：整体架构包括两个主要模块：首先使用BlenderProc进行程序渲染，生成具有领域随机化的逼真图像；其次利用NVIDIA的Cosmos-Predict2生成具有时间变化的物理一致视频序列。这两个模块共同构成了合成数据的生成流程。

**关键创新**：最重要的技术创新在于将程序渲染与AI视频生成相结合，形成了一种新的数据合成策略。这种方法与传统的仅依赖真实数据的训练方式本质上不同，能够有效克服数据稀缺的问题。

**关键设计**：在参数设置上，研究者通过调整合成数据与真实数据的比例，发现1:1的比例能够实现最佳的检测准确率。此外，采用YOLO作为检测器，结合合成数据集进行训练，显著提升了模型的性能。

## 📊 实验亮点

实验结果显示，基于合成数据集训练的YOLO检测器在准确性上超越了仅使用真实数据的模型，1:1的真实与合成样本比例达到了最高的检测准确率。这表明合成数据生成在工业应用中的有效性和可行性。

## 🎯 应用场景

该研究的潜在应用领域包括工业自动化、机器人检测和安全监控等。通过生成合成数据，能够在资源受限和高风险环境中有效训练检测模型，从而提高自主检测系统的可靠性和安全性。未来，这种方法可能会在其他复杂环境中得到推广，推动相关技术的发展。

## 📄 摘要（原文）

> This paper addresses the challenges of data scarcity and high acquisition costs in training robust object detection models for complex industrial environments, such as offshore oil platforms. Data collection in these hazardous settings often limits the development of autonomous inspection systems. To mitigate this issue, we propose a hybrid data synthesis pipeline that integrates procedural rendering and AI-driven video generation. The approach uses BlenderProc to produce photorealistic images with domain randomization and NVIDIA's Cosmos-Predict2 to generate physically consistent video sequences with temporal variation. A YOLO-based detector trained on a composite dataset, combining real and synthetic data, outperformed models trained solely on real images. A 1:1 ratio between real and synthetic samples achieved the highest accuracy. The results demonstrate that synthetic data generation is a viable, cost-effective, and safe strategy for developing reliable perception systems in safety-critical and resource-constrained industrial applications.

