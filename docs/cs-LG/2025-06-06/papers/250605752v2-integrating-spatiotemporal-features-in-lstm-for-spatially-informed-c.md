---
layout: default
title: Integrating Spatiotemporal Features in LSTM for Spatially Informed COVID-19 Hospitalization Forecasting
---

# Integrating Spatiotemporal Features in LSTM for Spatially Informed COVID-19 Hospitalization Forecasting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05752" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05752v2</a>
  <a href="https://arxiv.org/pdf/2506.05752.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05752v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05752v2', 'Integrating Spatiotemporal Features in LSTM for Spatially Informed COVID-19 Hospitalization Forecasting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhongying Wang, Thoai D. Ngo, Hamidreza Zoraghein, Benjamin Lucas, Morteza Karimzadeh

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-06 (更新: 2025-07-07)

**备注**: 36 pages, 12 figures. This is the accepted version of the article published in International Journal of Geographical Information Science. DOI will be added upon publication

**期刊**: Int. J. Geogr. Inf. Sci. (2025) 1-38

**DOI**: [10.1080/13658816.2025.2527266](https://doi.org/10.1080/13658816.2025.2527266)

---

## 💡 一句话要点

**提出并行流LSTM框架以提升COVID-19住院预测准确性**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `长短期记忆` `COVID-19预测` `空间时间特征` `社会接近度` `医疗资源规划`

## 📋 核心要点

1. 现有的COVID-19住院预测模型在变异株激增期间表现不佳，缺乏准确性和及时性。
2. 本研究提出了一种并行流LSTM框架，结合社会接近度特征以提升预测效果，捕捉传播动态。
3. 实验结果表明，该模型在Omicron激增期间的预测能力显著优于现有集成模型，提升幅度达到69个住院病例。

## 📝 摘要（中文）

COVID-19疫情的严重影响凸显了准确及时的住院预测对有效医疗规划的重要性。然而，大多数预测模型在变异株激增期间表现不佳。本研究提出了一种新颖的并行流长短期记忆（LSTM）框架，用于预测美国各州的每日住院人数。该框架引入了来自Meta的社会连通性指数的空间时间特征——社会接近度（SPH），以改善预测效果。SPH作为州际人口互动的代理，捕捉了跨空间和时间的传播动态。我们的架构能够捕获短期和长期的时间依赖性，并通过多视角集成策略平衡预测一致性和误差。与COVID-19预测中心的集成模型进行评估时，结果显示我们的模型在Omicron激增期间的表现优于集成模型，平均超出27、42、54和69个住院病例。数据消融实验确认了SPH的预测能力，强调了其在增强预测模型中的有效性。

## 🔬 方法详解

**问题定义**：本研究旨在解决COVID-19住院预测的准确性不足，尤其是在变异株激增期间，现有模型无法有效应对人口流动和传播动态的复杂性。

**核心思路**：论文提出的并行流LSTM框架通过引入社会接近度（SPH）特征，增强了模型对空间和时间传播动态的捕捉能力，从而提高预测的准确性。

**技术框架**：整体架构包括数据预处理、特征提取、LSTM网络模块和多视角集成策略。数据预处理阶段提取SPH特征，LSTM模块负责捕捉时间依赖性，集成策略则用于优化预测结果。

**关键创新**：最重要的技术创新在于将SPH特征引入LSTM框架，使得模型能够更好地反映州际人口互动和传播动态，这一设计与传统模型的单一时间序列预测方法形成鲜明对比。

**关键设计**：模型采用了多层LSTM结构，损失函数为均方误差（MSE），并通过交叉验证优化超参数设置，确保模型在不同时间范围内的预测能力。

## 📊 实验亮点

实验结果显示，在Omicron激增期间，提出的模型在7、14、21和28天的预测中，平均超出COVID-19预测中心集成模型27、42、54和69个住院病例，验证了SPH特征的有效性和模型的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括公共卫生管理、疫情应对策略制定和医疗资源规划。通过提高住院预测的准确性，能够帮助决策者更有效地分配医疗资源，优化医院运营，降低疫情对社会的影响。未来，该方法还可扩展应用于其他传染病的预测和控制。

## 📄 摘要（原文）

> The COVID-19 pandemic's severe impact highlighted the need for accurate and timely hospitalization forecasting to support effective healthcare planning. However, most forecasting models struggled, particularly during variant surges, when they were most needed. This study introduces a novel parallel-stream Long Short-Term Memory (LSTM) framework to forecast daily state-level incident hospitalizations in the United States. Our framework incorporates a spatiotemporal feature, Social Proximity to Hospitalizations (SPH), derived from Meta's Social Connectedness Index, to improve forecasts. SPH serves as a proxy for interstate population interaction, capturing transmission dynamics across space and time. Our architecture captures both short- and long-term temporal dependencies, and a multi-horizon ensembling strategy balances forecasting consistency and error. An evaluation against the COVID-19 Forecast Hub ensemble models during the Delta and Omicron surges reveals the superiority of our model. On average, our model surpasses the ensemble by 27, 42, 54, and 69 hospitalizations per state at the 7-, 14-, 21-, and 28-day horizons, respectively, during the Omicron surge. Data-ablation experiments confirm SPH's predictive power, highlighting its effectiveness in enhancing forecasting models. This research not only advances hospitalization forecasting but also underscores the significance of spatiotemporal features, such as SPH, in modeling the complex dynamics of infectious disease spread.

