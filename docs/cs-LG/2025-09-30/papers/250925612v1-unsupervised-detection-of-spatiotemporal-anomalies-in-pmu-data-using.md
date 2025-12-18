---
layout: default
title: Unsupervised Detection of Spatiotemporal Anomalies in PMU Data Using Transformer-Based BiGAN
---

# Unsupervised Detection of Spatiotemporal Anomalies in PMU Data Using Transformer-Based BiGAN

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25612" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25612v1</a>
  <a href="https://arxiv.org/pdf/2509.25612.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25612v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25612v1', 'Unsupervised Detection of Spatiotemporal Anomalies in PMU Data Using Transformer-Based BiGAN')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muhammad Imran Hossain, Jignesh Solanki, Sarika Khushlani Solanki

**分类**: cs.LG, cs.AI, eess.SY

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出T-BiGAN，用于电力系统PMU数据中时空异常的无监督检测。**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `电力系统` `同步相量数据` `异常检测` `Transformer` `BiGAN` `无监督学习` `时空数据分析`

## 📋 核心要点

1. 现有方法难以在同步相量数据中无监督地检测时空异常，尤其是在电网运行状态复杂多变的情况下。
2. T-BiGAN利用Transformer捕获时空依赖，BiGAN实现潜在空间对齐，并结合多种指标进行异常检测。
3. 在实际PMU数据上，T-BiGAN的ROC-AUC达到0.95，平均精度达到0.996，显著优于现有方法。

## 📝 摘要（中文）

为确保电网的弹性，需要及时且无监督地检测同步相量数据流中的异常。本文提出了一种名为T-BiGAN的新框架，该框架将基于窗口注意力的Transformer集成到双向生成对抗网络(BiGAN)中，以应对这一挑战。其自注意力编码器-解码器架构捕获了整个电网中复杂的时空依赖关系，而联合判别器则强制执行循环一致性，以使学习到的潜在空间与真实数据分布对齐。使用结合了重建误差、潜在空间漂移和判别器置信度的自适应分数实时标记异常。在真实的硬件在环PMU基准上进行评估，T-BiGAN实现了0.95的ROC-AUC和0.996的平均精度，显著优于领先的监督和无监督方法。它在检测细微的频率和电压偏差方面表现出特别的优势，证明了其在实时广域监控中的实际价值，而无需依赖手动标记的故障数据。

## 🔬 方法详解

**问题定义**：电力系统同步相量测量单元(PMU)数据包含丰富的电网运行信息，但从中检测异常事件面临挑战。现有方法或者依赖大量标注数据，或者难以捕捉复杂的时空依赖关系，导致检测精度不高，泛化能力不足。尤其是在电网运行状态复杂多变的情况下，细微的频率和电压偏差难以被有效检测。

**核心思路**：本文的核心思路是利用Transformer强大的时空建模能力和BiGAN的无监督学习能力，构建一个能够有效学习正常电网运行模式，并能准确识别异常事件的框架。通过Transformer捕获PMU数据中的时空依赖关系，BiGAN则用于学习潜在空间，并强制潜在空间与真实数据分布对齐，从而提高异常检测的准确性和鲁棒性。

**技术框架**：T-BiGAN的整体架构是一个双向生成对抗网络(BiGAN)，其中生成器包含一个基于窗口注意力的Transformer编码器-解码器结构。编码器将PMU数据映射到潜在空间，解码器则从潜在空间重建PMU数据。判别器用于区分真实数据和生成数据，并强制潜在空间与真实数据分布对齐。异常检测模块则基于重建误差、潜在空间漂移和判别器置信度等指标，对异常事件进行实时标记。

**关键创新**：T-BiGAN的关键创新在于将Transformer和BiGAN相结合，利用Transformer强大的时空建模能力和BiGAN的无监督学习能力。此外，本文还提出了一种自适应的异常评分机制，能够综合考虑重建误差、潜在空间漂移和判别器置信度等多个指标，从而提高异常检测的准确性和鲁棒性。

**关键设计**：Transformer编码器-解码器采用窗口注意力机制，以降低计算复杂度。BiGAN的损失函数包括对抗损失和循环一致性损失，用于强制潜在空间与真实数据分布对齐。异常评分机制采用自适应阈值，能够根据数据的动态变化调整阈值，从而提高异常检测的灵敏度。

## 📊 实验亮点

T-BiGAN在真实的硬件在环PMU基准上进行了评估，实验结果表明，T-BiGAN的ROC-AUC达到了0.95，平均精度达到了0.996，显著优于现有的监督和无监督方法。尤其是在检测细微的频率和电压偏差方面，T-BiGAN表现出特别的优势，证明了其在实际应用中的价值。

## 🎯 应用场景

该研究成果可应用于电力系统的实时广域监控，能够及时发现电网中的异常事件，提高电网的安全性、可靠性和稳定性。此外，该方法还可以扩展到其他时空数据分析领域，如交通监控、环境监测等，具有广泛的应用前景。

## 📄 摘要（原文）

> Ensuring power grid resilience requires the timely and unsupervised detection of anomalies in synchrophasor data streams. We introduce T-BiGAN, a novel framework that integrates window-attention Transformers within a bidirectional Generative Adversarial Network (BiGAN) to address this challenge. Its self-attention encoder-decoder architecture captures complex spatio-temporal dependencies across the grid, while a joint discriminator enforces cycle consistency to align the learned latent space with the true data distribution. Anomalies are flagged in real-time using an adaptive score that combines reconstruction error, latent space drift, and discriminator confidence. Evaluated on a realistic hardware-in-the-loop PMU benchmark, T-BiGAN achieves an ROC-AUC of 0.95 and an average precision of 0.996, significantly outperforming leading supervised and unsupervised methods. It shows particular strength in detecting subtle frequency and voltage deviations, demonstrating its practical value for live, wide-area monitoring without relying on manually labeled fault data.

