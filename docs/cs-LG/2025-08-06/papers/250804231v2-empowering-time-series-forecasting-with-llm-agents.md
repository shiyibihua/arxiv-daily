---
layout: default
title: Empowering Time Series Forecasting with LLM-Agents
---

# Empowering Time Series Forecasting with LLM-Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04231" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04231v2</a>
  <a href="https://arxiv.org/pdf/2508.04231.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04231v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04231v2', 'Empowering Time Series Forecasting with LLM-Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chin-Chia Michael Yeh, Vivian Lai, Uday Singh Saini, Xiran Fan, Yujie Fan, Junpeng Wang, Xin Dai, Yan Zheng

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-06 (更新: 2025-11-26)

---

## 💡 一句话要点

**提出DCATS以提升时间序列预测的数据质量**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列预测` `数据中心方法` `自动化机器学习` `大型语言模型` `数据清洗` `元数据利用` `模型优化`

## 📋 核心要点

1. 现有的AutoML方法主要关注特征工程和模型架构搜索，忽视了数据质量对预测性能的影响。
2. DCATS通过利用时间序列的元数据来清洗数据，从而提升预测性能，强调数据质量的重要性。
3. 在大规模交通流量预测数据集上，DCATS在所有测试模型上平均降低了6%的预测误差，显示出其有效性。

## 📝 摘要（中文）

大型语言模型（LLM）驱动的智能体已成为自动化机器学习（AutoML）系统中的有效规划者。现有的AutoML方法多集中于特征工程和模型架构搜索，而在时间序列预测中，轻量级模型往往能实现最先进的性能。基于这一观察，我们探索了提升数据质量而非模型架构的方向。我们提出了DCATS，一个用于时间序列的数据中心智能体，利用时间序列的元数据清洗数据，同时优化预测性能。通过在大规模交通流量预测数据集上评估DCATS，结果显示其在所有测试模型和时间范围内平均降低了6%的误差，突显了数据中心方法在时间序列预测AutoML中的潜力。

## 🔬 方法详解

**问题定义**：本论文旨在解决时间序列预测中数据质量不足的问题。现有方法往往忽视数据清洗的重要性，导致预测性能受限。

**核心思路**：论文提出DCATS，通过利用时间序列的元数据进行数据清洗，优化预测性能，强调数据质量在AutoML中的重要性。

**技术框架**：DCATS的整体架构包括数据清洗模块和预测模型优化模块。数据清洗模块利用元数据识别和修正数据中的噪声和缺失值，预测模型优化模块则基于清洗后的数据进行训练和评估。

**关键创新**：DCATS的核心创新在于将数据中心方法引入时间序列预测，强调数据质量而非模型架构的优化。这一思路与传统的AutoML方法形成鲜明对比。

**关键设计**：在DCATS中，关键设计包括元数据的选择和处理策略，以及针对不同时间序列模型的适配性调整。这些设计确保了数据清洗的有效性和预测模型的性能提升。

## 📊 实验亮点

实验结果表明，DCATS在所有测试的时间序列预测模型上平均降低了6%的预测误差，显示出其在提升数据质量方面的显著效果。这一成果为未来的AutoML研究提供了新的思路和方向。

## 🎯 应用场景

该研究的潜在应用领域包括交通流量预测、金融市场分析和气候变化监测等。通过提升数据质量，DCATS能够为各类时间序列预测任务提供更准确的结果，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Large Language Model (LLM) powered agents have emerged as effective planners for Automated Machine Learning (AutoML) systems. While most existing AutoML approaches focus on automating feature engineering and model architecture search, recent studies in time series forecasting suggest that lightweight models can often achieve state-of-the-art performance. This observation led us to explore improving data quality, rather than model architecture, as a potentially fruitful direction for AutoML on time series data. We propose DCATS, a Data-Centric Agent for Time Series. DCATS leverages metadata accompanying time series to clean data while optimizing forecasting performance. We evaluated DCATS using four time series forecasting models on a large-scale traffic volume forecasting dataset. Results demonstrate that DCATS achieves an average 6% error reduction across all tested models and time horizons, highlighting the potential of data-centric approaches in AutoML for time series forecasting.

