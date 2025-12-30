---
layout: default
title: "The Law of Multi-Model Collaboration: Scaling Limits of Model Ensembling for Large Language Models"
---

# The Law of Multi-Model Collaboration: Scaling Limits of Model Ensembling for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23340" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23340v1</a>
  <a href="https://arxiv.org/pdf/2512.23340.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23340v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23340v1', 'The Law of Multi-Model Collaboration: Scaling Limits of Model Ensembling for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dakuan Lu, Jiaqi Zhang, Cheng Yuan, Jiawei Shao, Chi Zhang, Xuelong Li

**分类**: cs.LG, cs.AI, cs.MA

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**提出多模型协作定律，揭示大语言模型集成性能的缩放规律与极限。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模型协作` `大语言模型` `缩放定律` `模型集成` `模型多样性`

## 📋 核心要点

1. 现有大语言模型能力受限于单模型缩放，多模型集成虽有进展，但缺乏统一的性能缩放理论。
2. 论文提出多模型协作定律，基于聚合参数预算预测LLM集成性能极限，采用理想化集成oracle量化协作上限。
3. 实验表明，多模型系统性能随参数量呈幂律缩放，优于单模型，且异构模型集成效果更佳，模型多样性是关键。

## 📝 摘要（中文）

大语言模型（LLM）的最新进展主要得益于单个模型的缩放定律，该定律预测模型参数和数据量的增加会带来性能的提升。然而，任何单个LLM的能力都存在固有的界限。一种解决方案源于多个LLM之间复杂的交互，使其集体性能超过任何单个模型。尽管模型路由和事后集成等多种模型集成技术迅速普及，但仍然缺乏一个统一的多模型协作性能缩放理论框架。本文提出了多模型协作定律，该定律预测LLM集成基于其聚合参数预算的性能极限。为了量化多模型协作的内在上限，我们采用了一种与方法无关的公式，并假设一个理想化的集成oracle，其中每个样本的总交叉熵损失由模型池中任何模型的最小损失决定。实验结果表明，多模型系统遵循关于总参数计数的幂律缩放，与单模型缩放相比，表现出更显著的改进趋势和更低的理论损失下限。此外，异构模型族的集成比在单个模型族内形成的集成实现了更好的性能缩放，表明模型多样性是协作收益的主要驱动因素。这些发现表明，模型协作是扩展LLM智能前沿的关键方向。

## 🔬 方法详解

**问题定义**：论文旨在解决现有大语言模型集成方法缺乏统一理论框架的问题。现有方法主要依赖于单模型的缩放定律，但单个模型的性能存在固有上限。多模型集成是提升性能的有效途径，但缺乏对集成性能极限的理论指导，难以有效利用计算资源和模型多样性。

**核心思路**：论文的核心思路是建立一个多模型协作的缩放定律，该定律能够预测模型集成的性能上限。通过分析模型集成后的整体性能与模型参数总量的关系，揭示多模型协作的内在规律。论文假设存在一个理想化的集成oracle，该oracle能够选择模型池中对每个样本损失最小的模型，从而量化多模型协作的理论上限。

**技术框架**：论文的技术框架主要包括以下几个部分：1) 定义多模型协作的性能指标，采用交叉熵损失作为衡量标准。2) 提出多模型协作定律，建立模型集成性能与总参数量之间的关系。3) 引入理想化的集成oracle，用于量化多模型协作的理论上限。4) 通过实验验证多模型协作定律的有效性，并分析模型多样性对集成性能的影响。

**关键创新**：论文最重要的技术创新在于提出了多模型协作定律，这是首次对多模型集成的性能缩放规律进行理论建模。与以往关注单模型缩放的研究不同，该论文关注多个模型协同工作时的性能表现，并揭示了模型多样性在提升集成性能中的关键作用。

**关键设计**：论文的关键设计包括：1) 采用交叉熵损失作为性能指标，能够有效衡量模型的预测准确性。2) 假设理想化的集成oracle，能够简化问题分析，并量化多模型协作的理论上限。3) 通过实验对比不同模型集成策略的性能，验证多模型协作定律的有效性。4) 分析异构模型集成与同构模型集成的性能差异，揭示模型多样性的重要性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23340v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23340v1/x2.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，多模型系统遵循关于总参数计数的幂律缩放，与单模型缩放相比，表现出更显著的改进趋势和更低的理论损失下限。异构模型族的集成比在单个模型族内形成的集成实现了更好的性能缩放，验证了模型多样性是协作收益的主要驱动因素。

## 🎯 应用场景

该研究成果可应用于大语言模型的集成优化，指导如何选择和组合不同的模型，以在有限的计算资源下获得最佳性能。此外，该研究还可用于指导新型多模型架构的设计，例如模型路由和动态集成等，从而进一步提升大语言模型的智能水平。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) have been largely driven by scaling laws for individual models, which predict performance improvements as model parameters and data volume increase. However, the capabilities of any single LLM are inherently bounded. One solution originates from intricate interactions among multiple LLMs, rendering their collective performance surpasses that of any constituent model. Despite the rapid proliferation of multi-model integration techniques such as model routing and post-hoc ensembling, a unifying theoretical framework of performance scaling for multi-model collaboration remains absent. In this work, we propose the Law of Multi-model Collaboration, a scaling law that predicts the performance limits of LLM ensembles based on their aggregated parameter budget. To quantify the intrinsic upper bound of multi-model collaboration, we adopt a method-agnostic formulation and assume an idealized integration oracle where the total cross-entropy loss of each sample is determined by the minimum loss of any model in the model pool. Experimental results reveal that multi-model systems follow a power-law scaling with respect to the total parameter count, exhibiting a more significant improvement trend and a lower theoretical loss floor compared to single model scaling. Moreover, ensembles of heterogeneous model families achieve better performance scaling than those formed within a single model family, indicating that model diversity is a primary driver of collaboration gains. These findings suggest that model collaboration represents a critical axis for extending the intelligence frontier of LLMs.

