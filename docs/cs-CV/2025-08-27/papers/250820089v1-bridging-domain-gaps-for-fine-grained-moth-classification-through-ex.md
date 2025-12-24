---
layout: default
title: Bridging Domain Gaps for Fine-Grained Moth Classification Through Expert-Informed Adaptation and Foundation Model Priors
---

# Bridging Domain Gaps for Fine-Grained Moth Classification Through Expert-Informed Adaptation and Foundation Model Priors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20089" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20089v1</a>
  <a href="https://arxiv.org/pdf/2508.20089.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20089v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20089v1', 'Bridging Domain Gaps for Fine-Grained Moth Classification Through Expert-Informed Adaptation and Foundation Model Priors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ross J Gardiner, Guillaume Mougeot, Sareh Rowlands, Benno I Simmons, Flemming Helsing, Toke Thomas Høye

**分类**: cs.CV

**发布日期**: 2025-08-27

---

## 💡 一句话要点

**提出轻量级分类方法以解决蛾类细粒度识别问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `蛾类识别` `知识蒸馏` `轻量级模型` `领域适应` `生物监测` `计算机视觉` `生态保护`

## 📋 核心要点

1. 现有方法在蛾类物种识别中面临领域转移问题，导致准确性下降。
2. 本文提出结合专家标注数据与BioCLIP2知识蒸馏的轻量级分类方法，旨在提高识别准确性。
3. 实验结果显示，BioCLIP2模型性能优越，蒸馏模型在降低计算成本的同时保持了高准确性。

## 📝 摘要（中文）

对自动摄像系统拍摄的鳞翅目（蛾类）图像进行标注对于理解昆虫数量下降至关重要。然而，由于精心策划的图像与噪声较大的现场图像之间存在领域转移，准确的物种识别面临挑战。本文提出了一种轻量级分类方法，结合有限的专家标注现场数据与高性能BioCLIP2基础模型的知识蒸馏，应用于ConvNeXt-tiny架构。对来自AMI摄像系统的101种丹麦蛾类的实验表明，BioCLIP2显著优于其他方法，而我们蒸馏的轻量级模型在计算成本显著降低的情况下实现了可比的准确性。这些发现为高效昆虫监测系统的开发和细粒度分类的领域间差距弥合提供了实用指导。

## 🔬 方法详解

**问题定义**：本文旨在解决蛾类物种识别中的领域转移问题，现有方法在处理噪声较大的现场图像时准确性不足，导致物种识别困难。

**核心思路**：论文提出了一种轻量级的分类方法，通过结合有限的专家标注数据与高性能的BioCLIP2基础模型进行知识蒸馏，旨在提高模型在不同领域图像上的适应能力。

**技术框架**：整体架构包括数据收集、知识蒸馏和模型训练三个主要阶段。首先，收集专家标注的现场数据；其次，利用BioCLIP2模型进行知识蒸馏；最后，基于ConvNeXt-tiny架构进行模型训练与优化。

**关键创新**：最重要的创新点在于将知识蒸馏与有限的专家标注数据相结合，形成了一种新颖的轻量级模型，显著提高了在领域转移情况下的分类性能。

**关键设计**：在模型设计中，采用了ConvNeXt-tiny架构，设置了适当的损失函数以优化蒸馏过程，并通过实验验证了模型在计算效率和准确性上的平衡。

## 📊 实验亮点

实验结果表明，BioCLIP2模型在101种丹麦蛾类的识别中显著优于其他方法，蒸馏后的轻量级模型在计算成本降低的同时，准确性与BioCLIP2相当，展示了高效的分类能力。

## 🎯 应用场景

该研究的潜在应用领域包括生态监测、农业害虫管理和生物多样性保护等。通过提高蛾类物种的识别准确性，能够为昆虫数量变化的研究提供重要数据支持，进而推动相关领域的科学研究和政策制定。

## 📄 摘要（原文）

> Labelling images of Lepidoptera (moths) from automated camera systems is vital for understanding insect declines. However, accurate species identification is challenging due to domain shifts between curated images and noisy field imagery. We propose a lightweight classification approach, combining limited expert-labelled field data with knowledge distillation from the high-performance BioCLIP2 foundation model into a ConvNeXt-tiny architecture. Experiments on 101 Danish moth species from AMI camera systems demonstrate that BioCLIP2 substantially outperforms other methods and that our distilled lightweight model achieves comparable accuracy with significantly reduced computational cost. These insights offer practical guidelines for the development of efficient insect monitoring systems and bridging domain gaps for fine-grained classification.

