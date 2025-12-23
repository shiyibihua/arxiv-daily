---
layout: default
title: Towards foundational LiDAR world models with efficient latent flow matching
---

# Towards foundational LiDAR world models with efficient latent flow matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23434" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23434v2</a>
  <a href="https://arxiv.org/pdf/2506.23434.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23434v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23434v2', 'Towards foundational LiDAR world models with efficient latent flow matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianran Liu, Shengwen Zhao, Nicholas Rhinehart

**分类**: cs.CV, cs.RO

**发布日期**: 2025-06-30 (更新: 2025-10-21)

**备注**: Accepted to the Thirty-Ninth Conference on Neural Information Processing Systems (NeurIPS 2025), 25 pages, 13 figures

---

## 💡 一句话要点

**提出基于潜在条件流匹配的LiDAR世界模型以解决领域迁移问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `LiDAR世界模型` `领域迁移` `潜在条件流匹配` `语义占用预测` `计算效率` `自动驾驶` `机器人导航`

## 📋 核心要点

1. 现有的LiDAR世界模型通常只能在特定领域内有效，缺乏跨领域的迁移能力，限制了其应用范围。
2. 本文提出了一种基于潜在条件流匹配的框架，旨在提高LiDAR世界模型的迁移能力和训练效率。
3. 实验结果显示，预训练模型在多个领域的迁移中实现了最高11%的绝对提升，并在语义占用预测中减少了95%的标注数据需求。

## 📝 摘要（中文）

基于LiDAR的世界模型提供了比图像模型更结构化和几何感知的表示。然而，现有的LiDAR世界模型训练范围狭窄，通常只能在特定领域内表现良好。本文首次系统地研究了跨多个领域的迁移能力，展示了单一预训练模型在不同场景下的有效性。实验结果表明，该模型在多个比较中超越了从头训练的效果，并在语义占用预测中显著减少了对手动标注数据的依赖。我们提出的潜在条件流匹配框架在数据压缩和训练效率上表现出色，达到了最新的重建精度和计算效率。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LiDAR世界模型在不同领域间迁移能力不足的问题，现有方法在数据利用和训练效率上存在低效现象。

**核心思路**：提出了一种潜在条件流匹配（CFM）框架，通过有效利用预训练模型和少量标注数据，提升模型在不同场景下的表现。

**技术框架**：该框架包括数据预处理、模型预训练、领域适应和性能评估四个主要模块，旨在实现高效的迁移学习。

**关键创新**：最重要的创新在于引入潜在条件流匹配技术，显著提高了重建精度和计算效率，与传统方法相比，压缩比提高了6倍。

**关键设计**：在模型设计中，采用了新的损失函数和网络结构，优化了训练过程中的数据利用率，确保在仅使用一半训练数据的情况下仍能达到最优性能。

## 📊 实验亮点

实验结果表明，预训练模型在多个领域的迁移中实现了最高11%的绝对提升，并在30/36的比较中超越了从头训练的效果。此外，该模型在语义占用预测中仅需5%的标注数据，且在计算效率上实现了23倍的提升。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人导航和智能城市建设等。通过提高LiDAR模型的迁移能力和训练效率，可以在不同环境中实现更高效的空间理解和决策支持，推动相关技术的实际应用和发展。

## 📄 摘要（原文）

> LiDAR-based world models offer more structured and geometry-aware representations than their image-based counterparts. However, existing LiDAR world models are narrowly trained; each model excels only in the domain for which it was built. Can we develop LiDAR world models that exhibit strong transferability across multiple domains? We conduct the first systematic domain transfer study across three demanding scenarios: (i) outdoor to indoor generalization, (ii) sparse-beam & dense-beam adaptation, and (iii) non-semantic to semantic transfer. Given different amounts of fine-tuning data, our experiments show that a single pre-trained model can achieve up to 11% absolute improvement (83% relative) over training from scratch and outperforms training from scratch in 30/36 of our comparisons. This transferability of dynamic learning significantly reduces the reliance on manually annotated data for semantic occupancy forecasting: our method exceed the previous semantic occupancy forecasting models with only 5% of the labeled training data required by prior models. We also observed inefficiencies of current LiDAR world models, mainly through their under-compression of LiDAR data and inefficient training objectives. To address this, we propose a latent conditional flow matching (CFM)-based frameworks that achieves state-of-the-art reconstruction accuracy using only half the training data and a compression ratio 6 times higher than that of prior methods. Our model achieves SOTA performance on future-trajectory-conditioned semantic occupancy forecasting while being 23x more computationally efficient (a 28x FPS speedup); and achieves SOTA performance on semantic occupancy forecasting while being 2x more computationally efficient (a 1.1x FPS speedup).

