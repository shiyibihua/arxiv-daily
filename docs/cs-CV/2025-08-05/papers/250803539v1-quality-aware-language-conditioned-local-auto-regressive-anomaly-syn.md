---
layout: default
title: Quality-Aware Language-Conditioned Local Auto-Regressive Anomaly Synthesis and Detection
---

# Quality-Aware Language-Conditioned Local Auto-Regressive Anomaly Synthesis and Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03539" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03539v1</a>
  <a href="https://arxiv.org/pdf/2508.03539.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03539v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03539v1', 'Quality-Aware Language-Conditioned Local Auto-Regressive Anomaly Synthesis and Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Long Qian, Bingke Zhu, Yingying Chen, Ming Tang, Jinqiao Wang

**分类**: cs.CV

**发布日期**: 2025-08-05

---

## 💡 一句话要点

**提出ARAS方法以解决现有异常合成的结构缺陷问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `异常合成` `自回归模型` `语言条件` `图像处理` `深度学习` `异常检测` `质量控制`

## 📋 核心要点

1. 现有的异常合成方法在结构上存在缺陷，如微结构不连续和语义控制能力不足，影响了生成效果。
2. 本文提出ARAS方法，通过语言条件和自回归机制，精确注入局部缺陷，提升合成异常的真实感和语义控制能力。
3. 在MVTec AD、VisA和BTAD等数据集上，QARAD在图像和像素级异常检测任务中表现优异，准确性和鲁棒性显著提升，合成速度提高了5倍。

## 📝 摘要（中文）

尽管异常合成方法取得了显著进展，但现有的基于扩散和粗糙修复的流程常常存在微结构不连续、语义可控性有限和生成效率低等结构缺陷。为克服这些局限性，本文提出了一种语言条件的自回归异常合成方法ARAS，该方法通过基于标记的潜在编辑精确地将局部文本指定的缺陷注入正常图像中。ARAS利用硬门控自回归算子和无训练的上下文保持掩蔽采样核，显著增强了缺陷的真实感，保留了细粒度的材料纹理，并提供了对合成异常的连续语义控制。通过动态加权策略，QARAD框架强调高质量合成样本，计算图像-文本相似度得分。实验结果表明，QARAD在多个基准数据集上超越了现有最先进的方法。

## 🔬 方法详解

**问题定义**：本文旨在解决现有异常合成方法在结构和语义控制方面的不足，特别是微结构不连续和生成效率低的问题。

**核心思路**：ARAS方法通过语言条件的自回归机制，结合局部缺陷注入技术，能够在正常图像中精确合成异常，提升合成的真实感和语义可控性。

**技术框架**：ARAS的整体架构包括语言条件输入、局部缺陷注入模块和自回归生成模块，采用硬门控机制和上下文保持的掩蔽采样策略，确保生成过程中的细节保留。

**关键创新**：ARAS的主要创新在于引入了基于标记的潜在编辑和动态加权策略，显著提高了合成异常的质量和生成效率，与传统的扩散方法相比，具有本质上的区别。

**关键设计**：在设计中，采用了无训练的上下文保持掩蔽采样核，确保生成过程中上下文信息的保留，同时通过双编码器模型计算图像-文本相似度得分，以动态调整合成样本的权重。

## 📊 实验亮点

实验结果表明，QARAD在MVTec AD、VisA和BTAD数据集上超越了现有最先进的方法，尤其在图像和像素级异常检测任务中，准确性和鲁棒性显著提升，合成速度较扩散方法提高了5倍，展示了其优越的性能。

## 🎯 应用场景

该研究的潜在应用领域包括工业缺陷检测、医疗影像分析和安全监控等。通过提高异常合成的质量和效率，ARAS方法能够在实际应用中提供更为精准的异常检测，进而提升相关领域的自动化水平和智能化决策能力。

## 📄 摘要（原文）

> Despite substantial progress in anomaly synthesis methods, existing diffusion-based and coarse inpainting pipelines commonly suffer from structural deficiencies such as micro-structural discontinuities, limited semantic controllability, and inefficient generation. To overcome these limitations, we introduce ARAS, a language-conditioned, auto-regressive anomaly synthesis approach that precisely injects local, text-specified defects into normal images via token-anchored latent editing. Leveraging a hard-gated auto-regressive operator and a training-free, context-preserving masked sampling kernel, ARAS significantly enhances defect realism, preserves fine-grained material textures, and provides continuous semantic control over synthesized anomalies. Integrated within our Quality-Aware Re-weighted Anomaly Detection (QARAD) framework, we further propose a dynamic weighting strategy that emphasizes high-quality synthetic samples by computing an image-text similarity score with a dual-encoder model. Extensive experiments across three benchmark datasets-MVTec AD, VisA, and BTAD, demonstrate that our QARAD outperforms SOTA methods in both image- and pixel-level anomaly detection tasks, achieving improved accuracy, robustness, and a 5 times synthesis speedup compared to diffusion-based alternatives. Our complete code and synthesized dataset will be publicly available.

