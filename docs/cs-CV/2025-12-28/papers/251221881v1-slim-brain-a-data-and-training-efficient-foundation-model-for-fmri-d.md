---
layout: default
title: "SLIM-Brain: A Data- and Training-Efficient Foundation Model for fMRI Data Analysis"
---

# SLIM-Brain: A Data- and Training-Efficient Foundation Model for fMRI Data Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21881" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21881v1</a>
  <a href="https://arxiv.org/pdf/2512.21881.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21881v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21881v1', 'SLIM-Brain: A Data- and Training-Efficient Foundation Model for fMRI Data Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mo Wang, Junfeng Xia, Wenhao Ye, Enyu Liu, Kaining Peng, Jianfeng Feng, Quanying Liu, Hongkai Wen

**分类**: cs.CV, q-bio.NC

**发布日期**: 2025-12-26

**备注**: The code will be released after review

---

## 💡 一句话要点

**SLIM-Brain：一种数据和训练高效的fMRI分析基础模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `fMRI分析` `基础模型` `自监督学习` `脑科学` `时间序列分析`

## 📋 核心要点

1. 现有fMRI分析基础模型面临数据和训练效率的挑战，基于图谱的方法损失空间细节，无图谱的方法计算成本过高。
2. SLIM-Brain通过两阶段自适应设计，利用轻量级时间提取器和4D分层编码器，选择性地学习显著性窗口的体素级表示。
3. 实验结果表明，SLIM-Brain在多个基准测试中取得了state-of-the-art的性能，同时显著降低了预训练所需的数据量和计算资源。

## 📝 摘要（中文）

基础模型正在成为fMRI分析的强大范例，但当前方法面临数据和训练效率的双重瓶颈。基于图谱的方法将体素信号聚合到固定的感兴趣区域，降低了数据维度，但丢弃了细粒度的空间细节，并且需要极大的样本量才能有效地训练为通用基础模型。另一方面，无图谱方法直接在体素级别的信息上操作，保留了空间保真度，但对内存和计算要求极高，使得大规模预训练不可行。我们引入了SLIM-Brain（Sample-efficient, Low-memory fMRI Foundation Model for Human Brain），一种新的无图谱基础模型，可同时提高数据和训练效率。SLIM-Brain采用两阶段自适应设计：（i）轻量级时间提取器捕获整个序列的全局上下文，并通过显著性对数据窗口进行排序；（ii）4D分层编码器（Hiera-JEPA）仅从前k个选定的窗口学习细粒度的体素级表示，同时删除约70%的掩码补丁。在七个公共基准上的大量实验表明，SLIM-Brain在各种任务上建立了新的最先进的性能，同时与传统的体素级方法相比，仅需要4千个预训练会话和大约30%的GPU内存。

## 🔬 方法详解

**问题定义**：当前fMRI分析的基础模型，要么依赖于图谱导致空间信息损失，要么直接处理体素数据导致计算量过大，难以进行大规模预训练。因此，如何在保证空间分辨率的同时，降低数据和计算复杂度，是本文要解决的核心问题。

**核心思路**：SLIM-Brain的核心思路是自适应地选择对任务有用的数据窗口，并仅在这些窗口上学习细粒度的体素级表示。通过轻量级的时间提取器筛选出显著性高的窗口，并利用分层编码器高效地学习这些窗口的特征，从而在降低计算量的同时，保留重要的空间信息。

**技术框架**：SLIM-Brain包含两个主要阶段：1) 时间提取器：使用轻量级网络（具体结构未知）处理整个fMRI序列，提取全局上下文信息，并根据显著性对数据窗口进行排序。2) 4D分层编码器（Hiera-JEPA）：仅从前k个显著性最高的窗口中学习体素级表示。该编码器采用分层结构，逐步提取特征，并使用掩码策略（删除约70%的掩码补丁）进一步降低计算量。

**关键创新**：SLIM-Brain的关键创新在于其自适应的数据选择机制和高效的4D分层编码器。通过时间提取器选择性地处理数据，避免了对所有体素和时间点进行计算，显著降低了计算复杂度。Hiera-JEPA编码器则在选定的窗口上学习细粒度的体素级表示，保留了重要的空间信息。

**关键设计**：时间提取器的具体网络结构未知。Hiera-JEPA编码器的具体分层结构和掩码策略细节未知。损失函数的设计也未知，但推测可能包含对比学习或重建损失，以学习有效的体素级表示。top-k的选择策略也需要进一步研究。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21881v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21881v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21881v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SLIM-Brain在七个公共基准测试中取得了state-of-the-art的性能，超越了现有的fMRI分析方法。更重要的是，SLIM-Brain仅需要4千个预训练会话，并且与传统的体素级方法相比，仅需约30%的GPU内存。这表明SLIM-Brain在数据和训练效率方面具有显著优势。

## 🎯 应用场景

SLIM-Brain可应用于多种fMRI数据分析任务，如疾病诊断、认知功能预测、脑活动模式识别等。其高效的数据和训练特性使其能够利用更大规模的数据集进行预训练，从而提升模型在各种下游任务上的泛化能力。该研究有望推动脑科学和神经科学领域的发展，为理解人类大脑功能提供更强大的工具。

## 📄 摘要（原文）

> Foundation models are emerging as a powerful paradigm for fMRI analysis, but current approaches face a dual bottleneck of data- and training-efficiency. Atlas-based methods aggregate voxel signals into fixed regions of interest, reducing data dimensionality but discarding fine-grained spatial details, and requiring extremely large cohorts to train effectively as general-purpose foundation models. Atlas-free methods, on the other hand, operate directly on voxel-level information - preserving spatial fidelity but are prohibitively memory- and compute-intensive, making large-scale pre-training infeasible. We introduce SLIM-Brain (Sample-efficient, Low-memory fMRI Foundation Model for Human Brain), a new atlas-free foundation model that simultaneously improves both data- and training-efficiency. SLIM-Brain adopts a two-stage adaptive design: (i) a lightweight temporal extractor captures global context across full sequences and ranks data windows by saliency, and (ii) a 4D hierarchical encoder (Hiera-JEPA) learns fine-grained voxel-level representations only from the top-$k$ selected windows, while deleting about 70% masked patches. Extensive experiments across seven public benchmarks show that SLIM-Brain establishes new state-of-the-art performance on diverse tasks, while requiring only 4 thousand pre-training sessions and approximately 30% of GPU memory comparing to traditional voxel-level methods.

