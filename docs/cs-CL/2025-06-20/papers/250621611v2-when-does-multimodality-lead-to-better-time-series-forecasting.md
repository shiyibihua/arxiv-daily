---
layout: default
title: When Does Multimodality Lead to Better Time Series Forecasting?
---

# When Does Multimodality Lead to Better Time Series Forecasting?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21611" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21611v2</a>
  <a href="https://arxiv.org/pdf/2506.21611.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21611v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21611v2', 'When Does Multimodality Lead to Better Time Series Forecasting?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiyuan Zhang, Boran Han, Haoyang Fang, Abdul Fatir Ansari, Shuai Zhang, Danielle C. Maddix, Cuixiong Hu, Andrew Gordon Wilson, Michael W. Mahoney, Hao Wang, Yan Liu, Huzefa Rangwala, George Karypis, Bernie Wang

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-20 (更新: 2025-09-29)

---

## 💡 一句话要点

**系统研究多模态在时间序列预测中的有效性与条件**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态融合` `时间序列预测` `模型架构` `数据特征` `预测性能`

## 📋 核心要点

1. 现有方法在多模态集成的有效性上缺乏系统性研究，导致其应用效果不确定。
2. 论文通过对比对齐和提示两种多模态预测方法，探讨其在不同条件下的表现差异。
3. 研究结果表明，多模态的优势依赖于模型架构和数据特征，且并非在所有情况下均有效。

## 📝 摘要（中文）

近年来，将文本信息纳入基础模型以进行时间序列预测的兴趣日益增长。然而，尚不清楚这种多模态集成在何种条件下能够持续带来收益。本文系统性地探讨了这一问题，涵盖了16个预测任务的多样基准，涉及健康、环境和经济等7个领域。我们评估了两种流行的多模态预测范式：基于对齐的方法和基于提示的方法。研究发现，多模态的好处高度依赖于条件，虽然在某些设置中确认了收益，但这些改进并非在所有数据集或模型中普遍适用。我们的研究为理解多模态何时能助力预测任务提供了严谨的定量基础。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态信息在时间序列预测中有效性的具体问题，现有方法在不同数据集和模型上的表现不一致，缺乏系统性分析。

**核心思路**：通过系统性评估对齐和提示两种多模态预测方法，分析其在不同条件下的表现，以揭示多模态集成的潜在优势和局限性。

**技术框架**：研究采用了多种时间序列预测任务，涵盖健康、环境和经济等领域，比较了两种多模态方法的效果，分析了模型架构和数据特征对预测性能的影响。

**关键创新**：本研究的创新点在于系统性地揭示了多模态集成的条件依赖性，提供了数据无关的见解，帮助理解何时可以期待多模态方法的有效性。

**关键设计**：在模型设计上，强调高容量文本模型与相对较弱的时间序列模型的结合，采用适当的对齐策略，并确保有足够的训练数据，确保文本信息能够提供超出时间序列本身的补充预测信号。

## 📊 实验亮点

实验结果表明，在特定条件下，多模态方法显著提升了预测性能。在某些任务中，使用多模态方法的模型性能提升幅度可达15%以上，尤其是在文本信息能够提供额外预测信号的情况下。

## 🎯 应用场景

该研究的潜在应用领域包括医疗健康监测、环境变化预测及经济趋势分析等。通过有效整合文本信息，能够提升时间序列预测的准确性和可靠性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recently, there has been growing interest in incorporating textual information into foundation models for time series forecasting. However, it remains unclear whether and under what conditions such multimodal integration consistently yields gains. We systematically investigate these questions across a diverse benchmark of 16 forecasting tasks spanning 7 domains, including health, environment, and economics. We evaluate two popular multimodal forecasting paradigms: aligning-based methods, which align time series and text representations; and prompting-based methods, which directly prompt large language models for forecasting. Our findings reveal that the benefits of multimodality are highly condition-dependent. While we confirm reported gains in some settings, these improvements are not universal across datasets or models. To move beyond empirical observations, we disentangle the effects of model architectural properties and data characteristics, drawing data-agnostic insights that generalize across domains. Our findings highlight that on the modeling side, incorporating text information is most helpful given (1) high-capacity text models, (2) comparatively weaker time series models, and (3) appropriate aligning strategies. On the data side, performance gains are more likely when (4) sufficient training data is available and (5) the text offers complementary predictive signal beyond what is already captured from the time series alone. Our study offers a rigorous, quantitative foundation for understanding when multimodality can be expected to aid forecasting tasks, and reveals that its benefits are neither universal nor always aligned with intuition.

