---
layout: default
title: Scaling Learned Image Compression Models up to 1 Billion
---

# Scaling Learned Image Compression Models up to 1 Billion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09075" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09075v1</a>
  <a href="https://arxiv.org/pdf/2508.09075.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09075v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09075v1', 'Scaling Learned Image Compression Models up to 1 Billion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuqi Li, Haotian Zhang, Li Li, Dong Liu, Feng Wu

**分类**: cs.CV

**发布日期**: 2025-08-12

**备注**: 11 pages, technical report

---

## 💡 一句话要点

**提出大规模学习图像压缩模型以提升压缩性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `学习图像压缩` `模型扩展` `压缩性能` `深度学习` `率失真优化`

## 📋 核心要点

1. 现有学习图像压缩模型规模有限，导致表示能力不足，影响压缩性能的提升。
2. 本文提出通过扩展模型参数规模，探索模型大小与压缩性能之间的关系，揭示缩放法则。
3. 实验表明，HPCM-1B模型在率失真性能上达到了最新的最优水平，展示了大规模模型的潜力。

## 📝 摘要（中文）

近年来，学习图像压缩作为现代数据压缩的基础任务取得了显著进展。然而，现有模型的规模有限，限制了其表示能力，且如何通过扩大模型规模来影响压缩性能尚未被深入探讨。本文首次研究了学习图像压缩模型的规模扩展，并通过缩放法则揭示了性能趋势。以最新的HPCM模型为基线，将模型参数从6850万扩展至10亿，并拟合测试损失与模型规模及最佳训练计算等关键缩放变量之间的幂律关系。实验结果表明，扩展后的HPCM-1B模型在率失真性能上达到了最新的最优水平。希望本研究能激励未来对大规模压缩模型的探索及压缩与智能之间关系的深入研究。

## 🔬 方法详解

**问题定义**：本文旨在解决当前学习图像压缩模型规模限制的问题，现有方法在表示能力和压缩性能上存在不足。

**核心思路**：通过将模型参数从6850万扩展至10亿，探索模型规模对压缩性能的影响，并拟合幂律关系，以揭示性能趋势。

**技术框架**：研究以HPCM模型为基线，采用逐步扩展模型参数的方式，分析测试损失与模型规模、训练计算之间的关系，整体流程包括模型设计、训练和性能评估。

**关键创新**：首次系统性地研究了学习图像压缩模型的规模扩展，揭示了模型规模与压缩性能之间的缩放法则，推动了该领域的研究进展。

**关键设计**：在模型设计中，采用了适应性损失函数和优化算法，确保在扩展过程中保持训练效率和压缩性能的平衡。

## 📊 实验亮点

实验结果显示，扩展后的HPCM-1B模型在率失真性能上超越了现有最优模型，具体性能数据表明其在压缩效率上提升显著，展示了大规模学习模型的有效性和潜力。

## 🎯 应用场景

该研究的潜在应用领域包括图像和视频压缩、流媒体传输、存储优化等。通过提升压缩性能，能够有效减少带宽需求和存储成本，具有重要的实际价值。此外，未来可能推动更大规模的压缩模型研究，深化对压缩与智能之间关系的理解。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) highlight a strong connection between intelligence and compression. Learned image compression, a fundamental task in modern data compression, has made significant progress in recent years. However, current models remain limited in scale, restricting their representation capacity, and how scaling model size influences compression performance remains unexplored. In this work, we present a pioneering study on scaling up learned image compression models and revealing the performance trends through scaling laws. Using the recent state-of-the-art HPCM model as baseline, we scale model parameters from 68.5 millions to 1 billion and fit power-law relations between test loss and key scaling variables, including model size and optimal training compute. The results reveal a scaling trend, enabling extrapolation to larger scale models. Experimental results demonstrate that the scaled-up HPCM-1B model achieves state-of-the-art rate-distortion performance. We hope this work inspires future exploration of large-scale compression models and deeper investigations into the connection between compression and intelligence.

