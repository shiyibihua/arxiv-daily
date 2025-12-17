---
layout: default
title: Multi-Context Fusion Transformer for Pedestrian Crossing Intention Prediction in Urban Environments
---

# Multi-Context Fusion Transformer for Pedestrian Crossing Intention Prediction in Urban Environments

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.20011" target="_blank" class="toolbar-btn">arXiv: 2511.20011v1</a>
    <a href="https://arxiv.org/pdf/2511.20011.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.20011v1" 
            onclick="toggleFavorite(this, '2511.20011v1', 'Multi-Context Fusion Transformer for Pedestrian Crossing Intention Prediction in Urban Environments')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yuanzhe Li, Hang Zhong, Steffen Müller

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-25

**🔗 代码/项目**: [GITHUB](https://github.com/ZhongHang0307/Multi-Context-Fusion-Transformer)

---

## 💡 一句话要点

**提出多上下文融合Transformer（MFT）用于城市环境中行人意图预测。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `行人意图预测` `多上下文融合` `Transformer` `注意力机制` `自动驾驶`

## 📋 核心要点

1. 城市环境中行人意图预测面临诸多挑战，现有方法难以有效融合多维度上下文信息。
2. MFT通过渐进式注意力机制，在上下文内和上下文间进行特征融合，提取更鲁棒的行人意图表示。
3. 实验表明，MFT在多个数据集上显著优于现有方法，验证了其有效性和优越性。

## 📝 摘要（中文）

行人意图预测对于自动驾驶车辆至关重要，能够提高行人安全并减少交通事故。然而，由于影响行人行为的因素众多，在城市环境中准确预测行人意图仍然具有挑战性。本文提出了一种多上下文融合Transformer（MFT），它利用四个关键维度上的各种数值上下文属性，包括行人行为上下文、环境上下文、行人定位上下文和车辆运动上下文，以实现准确的行人意图预测。MFT采用渐进式融合策略，其中互上下文内注意力能够实现每个上下文内的相互交互，从而促进特征序列融合并产生上下文token作为上下文特定的表示。随后是互上下文间注意力，它通过全局CLS token集成跨上下文的特征，该token充当紧凑的多上下文表示。最后，引导的上下文内注意力通过定向交互来细化每个上下文内的上下文token，而引导的跨上下文注意力则加强全局CLS token，以通过引导的信息传播来促进多上下文融合，从而产生更深入、更有效的集成。实验结果验证了MFT优于最先进的方法，在JAADbeh、JAADall和PIE数据集上分别实现了73%、93%和90%的准确率。此外，还进行了广泛的消融研究，以研究网络架构的有效性和不同输入上下文的贡献。代码已开源。

## 🔬 方法详解

**问题定义**：论文旨在解决城市环境中准确预测行人意图的问题。现有方法难以有效融合行人行为、环境、定位和车辆运动等多方面的上下文信息，导致预测精度不高。这些方法通常无法充分捕捉不同上下文之间的复杂关系，限制了模型的性能。

**核心思路**：论文的核心思路是利用Transformer架构，通过多层注意力机制，逐步融合不同上下文的信息。首先在每个上下文内部进行特征提取和融合，然后跨上下文进行信息交互，最后通过引导机制进一步优化融合结果。这种渐进式的融合策略能够更有效地捕捉不同上下文之间的依赖关系，提高预测精度。

**技术框架**：MFT的整体架构包含以下几个主要模块：1) 上下文特征提取模块：提取行人行为、环境、定位和车辆运动等上下文的特征序列。2) 互上下文内注意力模块：在每个上下文内部进行自注意力计算，增强上下文内部的特征表示。3) 互上下文间注意力模块：利用全局CLS token，将不同上下文的特征进行融合，捕捉上下文之间的关系。4) 引导的上下文内注意力模块：利用全局CLS token引导，进一步优化每个上下文内部的特征表示。5) 引导的上下文间注意力模块：利用全局CLS token引导，进一步加强不同上下文之间的信息交互。

**关键创新**：MFT的关键创新在于其渐进式的多上下文融合策略。通过互上下文内注意力、互上下文间注意力和引导的注意力机制，MFT能够更有效地融合不同上下文的信息，捕捉上下文之间的复杂关系。与现有方法相比，MFT能够更充分地利用多维度的上下文信息，提高行人意图预测的精度。

**关键设计**：MFT的关键设计包括：1) 使用Transformer架构作为基础模型，利用其强大的特征提取和融合能力。2) 采用渐进式的注意力机制，逐步融合不同上下文的信息。3) 引入全局CLS token，作为多上下文信息的紧凑表示，并用于引导注意力计算。4) 设计了互上下文内注意力、互上下文间注意力和引导的注意力机制，分别用于增强上下文内部的特征表示、捕捉上下文之间的关系和优化融合结果。

## 📊 实验亮点

实验结果表明，MFT在JAADbeh、JAADall和PIE数据集上分别取得了73%、93%和90%的准确率，显著优于现有最先进的方法。消融实验进一步验证了MFT各个模块的有效性，以及不同上下文信息对预测结果的贡献。

## 🎯 应用场景

该研究成果可应用于自动驾驶车辆、高级驾驶辅助系统（ADAS）等领域，提高车辆对行人意图的理解能力，从而减少交通事故，提升行人安全。此外，该方法也可应用于智能监控、机器人导航等场景，实现更智能、更安全的交互。

## 📄 摘要（原文）

> Pedestrian crossing intention prediction is essential for autonomous vehicles to improve pedestrian safety and reduce traffic accidents. However, accurate pedestrian intention prediction in urban environments remains challenging due to the multitude of factors affecting pedestrian behavior. In this paper, we propose a multi-context fusion Transformer (MFT) that leverages diverse numerical contextual attributes across four key dimensions, encompassing pedestrian behavior context, environmental context, pedestrian localization context and vehicle motion context, to enable accurate pedestrian intention prediction. MFT employs a progressive fusion strategy, where mutual intra-context attention enables reciprocal interactions within each context, thereby facilitating feature sequence fusion and yielding a context token as a context-specific representation. This is followed by mutual cross-context attention, which integrates features across contexts with a global CLS token serving as a compact multi-context representation. Finally, guided intra-context attention refines context tokens within each context through directed interactions, while guided cross-context attention strengthens the global CLS token to promote multi-context fusion via guided information propagation, yielding deeper and more efficient integration. Experimental results validate the superiority of MFT over state-of-the-art methods, achieving accuracy rates of 73%, 93%, and 90% on the JAADbeh, JAADall, and PIE datasets, respectively. Extensive ablation studies are further conducted to investigate the effectiveness of the network architecture and contribution of different input context. Our code is open-source: https://github.com/ZhongHang0307/Multi-Context-Fusion-Transformer.

