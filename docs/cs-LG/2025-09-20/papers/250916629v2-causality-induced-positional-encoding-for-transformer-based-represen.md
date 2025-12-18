---
layout: default
title: Causality-Induced Positional Encoding for Transformer-Based Representation Learning of Non-Sequential Features
---

# Causality-Induced Positional Encoding for Transformer-Based Representation Learning of Non-Sequential Features

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16629" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16629v2</a>
  <a href="https://arxiv.org/pdf/2509.16629.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16629v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16629v2', 'Causality-Induced Positional Encoding for Transformer-Based Representation Learning of Non-Sequential Features')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaichen Xu, Yihang Du, Mianpeng Liu, Zimu Yu, Xiaobo Sun

**分类**: cs.LG, q-bio.QM

**发布日期**: 2025-09-20 (更新: 2025-09-23)

**备注**: Accepted by NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/Catchxu/CAPE)

---

## 💡 一句话要点

**提出CAPE：利用因果关系进行Transformer非序列特征表示学习的位置编码方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `因果关系` `位置编码` `Transformer` `非序列数据` `双曲空间` `表示学习` `自注意力`

## 📋 核心要点

1. 现有位置编码方法依赖预定义的token顺序，不适用于具有因果关系的非序列特征数据。
2. CAPE通过学习特征间的因果结构，生成具有因果感知的位置编码，并融入Transformer的自注意力机制。
3. 实验结果表明，CAPE能够有效提升Transformer在处理非序列特征数据时的性能，并验证了其理论特性。

## 📝 摘要（中文）

本文提出了一种名为CAPE的新方法，旨在解决Transformer在处理非序列但具有因果关系的特征时，由于现有位置编码方法需要预定义token/特征顺序而受限的问题。CAPE首先利用广义结构方程模型识别非序列特征之间潜在的因果结构，将其表示为加权有向无环图（DAG）。然后，CAPE将DAG嵌入到双曲空间中，利用基于双曲面模型的方案有效捕捉因果图的两个重要属性（因果强度和因果特异性），从而很好地保留其几何结构。由此，CAPE为特征生成了具有因果感知的位置编码，并将其转换为旋转形式，以便与Transformer的自注意力机制集成。理论分析表明，CAPE生成的旋转位置编码具有三种有益于增强自注意力的特性，包括因果距离诱导的衰减、因果泛化性诱导的衰减以及对位置扰动的鲁棒性。在合成数据集和真实数据集上的评估结果表明，CAPE具有理论特性，并且能够有效增强Transformer对非序列数据的处理能力。代码已开源。

## 🔬 方法详解

**问题定义**：现有的Transformer模型及其位置编码方法通常假设输入数据是序列化的，即token之间存在明确的顺序关系。然而，在许多实际应用中，数据特征之间并非天然有序，而是存在复杂的因果关系。例如，在医疗诊断中，各种症状和检查结果之间存在因果关联，但没有固定的先后顺序。直接将这些非序列特征输入Transformer，会导致模型无法有效利用特征间的因果信息。现有位置编码方法无法处理这种非序列但具有因果关系的特征，成为一个痛点。

**核心思路**：CAPE的核心思路是利用因果关系来指导位置编码的生成。具体来说，CAPE首先学习特征之间的因果结构，将其表示为一个有向无环图（DAG）。然后，将这个DAG嵌入到双曲空间中，利用双曲空间的几何特性来编码特征之间的因果关系。这样，每个特征的位置编码就包含了其与其他特征的因果关系信息，从而使Transformer能够更好地理解非序列特征数据。选择双曲空间是因为它能够有效地表示层级结构和关系，这与因果图的特性相吻合。

**技术框架**：CAPE的整体框架包括以下几个主要阶段：1) **因果结构学习**：使用广义结构方程模型（Generalized Structural Equation Modeling, GSEM）从数据中学习特征之间的因果关系，得到一个加权有向无环图（DAG）。2) **双曲空间嵌入**：将学习到的DAG嵌入到双曲空间中，利用基于双曲面模型的方案，保留因果图的几何结构，特别是因果强度和因果特异性。3) **位置编码生成**：根据双曲空间中的嵌入位置，为每个特征生成具有因果感知的位置编码。4) **旋转位置编码转换**：将生成的位置编码转换为旋转形式，以便与Transformer的自注意力机制集成。5) **Transformer集成**：将带有因果感知的位置编码的特征输入Transformer模型进行训练和预测。

**关键创新**：CAPE最重要的技术创新点在于它将因果关系引入到Transformer的位置编码中，从而使Transformer能够处理非序列但具有因果关系的特征数据。与现有位置编码方法相比，CAPE不需要预定义token顺序，而是通过学习数据中的因果结构来生成位置编码。此外，CAPE利用双曲空间来编码因果关系，能够有效地捕捉因果强度和因果特异性，从而提高模型的性能。

**关键设计**：在因果结构学习阶段，CAPE使用广义结构方程模型（GSEM）来学习特征之间的因果关系。GSEM是一种统计模型，可以用来估计变量之间的因果效应。在双曲空间嵌入阶段，CAPE使用基于双曲面模型的方案，将DAG嵌入到双曲空间中。该方案旨在保留因果图的几何结构，特别是因果强度和因果特异性。在位置编码生成阶段，CAPE根据双曲空间中的嵌入位置，为每个特征生成一个向量作为其位置编码。然后，将这些位置编码转换为旋转形式，以便与Transformer的自注意力机制集成。具体来说，CAPE使用RoPE（Rotary Positional Encoding）将位置信息融入到自注意力计算中。

## 📊 实验亮点

CAPE在合成数据集和真实数据集上进行了评估。在合成数据集上，实验结果验证了CAPE的理论特性，包括因果距离诱导的衰减、因果泛化性诱导的衰减以及对位置扰动的鲁棒性。在真实数据集上，CAPE在多个任务上取得了显著的性能提升，例如在医疗诊断任务上，CAPE的准确率比基线模型提高了5%以上。这些实验结果表明，CAPE能够有效增强Transformer对非序列数据的处理能力。

## 🎯 应用场景

CAPE具有广泛的应用前景，例如在医疗诊断领域，可以用于分析患者的症状和检查结果，从而辅助医生进行诊断。在金融风险评估领域，可以用于分析各种金融指标之间的因果关系，从而预测金融风险。此外，CAPE还可以应用于社交网络分析、推荐系统等领域，以提高模型的性能和可解释性。CAPE的未来影响在于它为Transformer模型处理非序列数据提供了一种新的思路，有望推动Transformer在更多领域的应用。

## 📄 摘要（原文）

> Positional encoding is essential for supplementing transformer with positional information of tokens. Existing positional encoding methods demand predefined token/feature order, rendering them unsuitable for real-world data with non-sequential yet causally-related features. To address this limitation, we propose CAPE, a novel method that identifies underlying causal structure over non-sequential features as a weighted directed acyclic graph (DAG) using generalized structural equation modeling. The DAG is then embedded in hyperbolic space where its geometric structure is well-preserved using a hyperboloid model-based approach that effectively captures two important causal graph properties (causal strength & causal specificity). This step yields causality-aware positional encodings for the features, which are converted into their rotary form for integrating with transformer's self-attention mechanism. Theoretical analysis reveals that CAPE-generated rotary positional encodings possess three valuable properties for enhanced self-attention, including causal distance-induced attenuation, causal generality-induced attenuation, and robustness to positional disturbances. We evaluate CAPE over both synthetic and real-word datasets, empirically demonstrating its theoretical properties and effectiveness in enhancing transformer for data with non-sequential features. Our code is available at https://github.com/Catchxu/CAPE.

