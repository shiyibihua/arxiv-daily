---
layout: default
title: HydroGEM: A Self Supervised Zero Shot Hybrid TCN Transformer Foundation Model for Continental Scale Streamflow Quality Control
---

# HydroGEM: A Self Supervised Zero Shot Hybrid TCN Transformer Foundation Model for Continental Scale Streamflow Quality Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14106" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14106v1</a>
  <a href="https://arxiv.org/pdf/2512.14106.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14106v1" onclick="toggleFavorite(this, '2512.14106v1', 'HydroGEM: A Self Supervised Zero Shot Hybrid TCN Transformer Foundation Model for Continental Scale Streamflow Quality Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ijaz Ul Haq, Byung Suk Lee, Julia N. Perdrial, David Baude

**分类**: cs.AI

**发布日期**: 2025-12-16

**备注**: Supplementary materials, datasets, and implementation code will be made publicly available upon acceptance for publication in a peer-reviewed journal

---

## 💡 一句话要点

**HydroGEM：用于洲际尺度流量质量控制的自监督零样本混合TCN-Transformer基础模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `流量质量控制` `自监督学习` `时间卷积网络` `Transformer` `水文建模` `异常检测` `零样本学习`

## 📋 核心要点

1. 现有流量监测网络数据质量维护依赖人工，成本高昂，缺乏自动化和泛化能力。
2. HydroGEM通过自监督预训练和合成异常微调，学习水文表示，实现流量质量控制的自动化。
3. 实验表明，HydroGEM在流量异常检测和重建方面显著优于现有方法，并具备跨国泛化能力。

## 📝 摘要（中文）

实时流量监测网络每年产生数百万条观测数据，但维护数千个远程传感器的数据质量仍然非常耗费人力。我们提出了HydroGEM（用于监测的水文可泛化编码器），这是一个用于洲际尺度流量质量控制的基础模型。HydroGEM使用两阶段训练：在来自3724个美国地质调查局站点的603万个序列上进行自监督预训练，以学习水文表示，然后使用合成异常进行微调，以进行检测和重建。混合TCN-Transformer架构（1420万个参数）捕获局部时间模式和长程依赖关系，而分层归一化处理六个数量级的流量。在包含799个站点和18种专家验证的异常类型的保留合成测试中，HydroGEM在检测方面实现了F1 = 0.792，重建误差降低了68.7％，比现有方法提高了36.3％。零样本迁移到100个加拿大环境与气候变化部站点，产生F1 = 0.586，超过所有基线，并证明了跨国泛化能力。该模型在校正幅度上保持一致的检测，并与运营季节性模式保持一致。HydroGEM专为人工参与的工作流程而设计——输出是需要专家审查的质量控制建议，而不是自主校正。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模流量监测网络中数据质量控制的问题。现有方法依赖人工，效率低下且难以扩展到大规模网络。此外，现有方法的泛化能力有限，难以适应不同地区和不同类型的异常。

**核心思路**：论文的核心思路是利用自监督学习和迁移学习，训练一个能够自动检测和重建流量异常的基础模型。通过在大规模无标签数据上进行预训练，模型可以学习到通用的水文表示，然后通过在合成异常数据上进行微调，模型可以学习到特定类型的异常检测能力。这种方法可以减少对人工标注数据的依赖，提高模型的泛化能力。

**技术框架**：HydroGEM采用两阶段训练框架。第一阶段是自监督预训练，使用来自美国地质调查局的大量流量数据，通过重建流量序列来学习水文表示。第二阶段是微调，使用合成的流量异常数据，训练模型检测和重建异常。模型采用混合TCN-Transformer架构，利用TCN捕获局部时间模式，利用Transformer捕获长程依赖关系。此外，模型还采用了分层归一化方法，以处理不同站点流量数量级的差异。

**关键创新**：HydroGEM的关键创新在于以下几点：1) 提出了一个用于流量质量控制的自监督学习框架，减少了对人工标注数据的依赖。2) 提出了一个混合TCN-Transformer架构，能够有效地捕获流量数据中的局部和长程时间依赖关系。3) 提出了一个分层归一化方法，能够处理不同站点流量数量级的差异。与现有方法相比，HydroGEM具有更强的泛化能力和更高的检测精度。

**关键设计**：HydroGEM的TCN部分使用了多个卷积层，每个卷积层具有不同的膨胀因子，以捕获不同时间尺度的局部模式。Transformer部分使用了多头注意力机制，以捕获长程依赖关系。损失函数包括重建损失和异常检测损失。重建损失用于衡量模型重建流量序列的能力，异常检测损失用于衡量模型检测异常的能力。分层归一化方法将流量数据分成多个层级，每个层级使用不同的归一化参数。

## 📊 实验亮点

HydroGEM在合成测试中实现了F1=0.792的异常检测精度，重建误差降低了68.7%，比现有方法提高了36.3%。在零样本迁移到加拿大站点时，F1=0.586，超过所有基线，证明了其跨国泛化能力。该模型在不同校正幅度下保持一致的检测性能，并与实际季节性模式对齐。

## 🎯 应用场景

HydroGEM可应用于大规模流量监测网络的数据质量控制，提高数据质量和可用性。该模型可用于自动检测和重建流量异常，减少人工干预，提高工作效率。此外，HydroGEM还可用于水文模型校准、水资源管理和洪水预警等领域，具有广泛的应用前景。

## 📄 摘要（原文）

> Real-time streamflow monitoring networks generate millions of observations annually, yet maintaining data quality across thousands of remote sensors remains labor-intensive. We introduce HydroGEM (Hydrological Generalizable Encoder for Monitoring), a foundation model for continental-scale streamflow quality control. HydroGEM uses two-stage training: self-supervised pretraining on 6.03 million sequences from 3,724 USGS stations learns hydrological representations, followed by fine-tuning with synthetic anomalies for detection and reconstruction. A hybrid TCN-Transformer architecture (14.2M parameters) captures local temporal patterns and long-range dependencies, while hierarchical normalization handles six orders of magnitude in discharge. On held-out synthetic tests comprising 799 stations with 18 expert-validated anomaly types, HydroGEM achieves F1 = 0.792 for detection and 68.7% reconstruction-error reduction, a 36.3% improvement over existing methods. Zero-shot transfer to 100 Environment and Climate Change Canada stations yields F1 = 0.586, exceeding all baselines and demonstrating cross-national generalization. The model maintains consistent detection across correction magnitudes and aligns with operational seasonal patterns. HydroGEM is designed for human-in-the-loop workflows - outputs are quality control suggestions requiring expert review, not autonomous corrections.

