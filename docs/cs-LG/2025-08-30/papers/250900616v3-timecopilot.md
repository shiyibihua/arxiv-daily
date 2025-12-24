---
layout: default
title: TimeCopilot
---

# TimeCopilot

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00616" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00616v3</a>
  <a href="https://arxiv.org/pdf/2509.00616.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00616v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00616v3', 'TimeCopilot')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Azul Garza, Renée Rosillo

**分类**: cs.LG, cs.AI, cs.HC

**发布日期**: 2025-08-30 (更新: 2025-11-07)

---

## 💡 一句话要点

**提出TimeCopilot框架以实现高效的时间序列预测**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列预测` `开源框架` `大型语言模型` `自动化` `可解释性` `概率预测` `模型集成`

## 📋 核心要点

1. 现有的时间序列预测方法通常缺乏自动化和可解释性，难以满足复杂的业务需求。
2. TimeCopilot通过整合多种时间序列基础模型与大型语言模型，提供统一的API，自动化整个预测流程。
3. 在GIFT-Eval基准测试中，TimeCopilot实现了低成本的最先进概率预测性能，展示了其有效性。

## 📝 摘要（中文）

我们介绍了TimeCopilot，这是第一个开源的代理框架，用于预测，结合了多种时间序列基础模型（TSFMs）和大型语言模型（LLMs），通过统一的API进行交互。TimeCopilot自动化了预测流程，包括特征分析、模型选择、交叉验证和预测生成，同时提供自然语言解释，并支持对未来的直接查询。该框架与LLM无关，兼容商业和开源模型，并支持多种预测家族的集成。GIFT-Eval基准测试的结果表明，TimeCopilot以低成本实现了最先进的概率预测性能。我们的框架为可重复、可解释和可访问的代理预测系统提供了实用基础。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有时间序列预测方法在自动化和可解释性方面的不足，现有方法往往需要手动干预，且缺乏对预测结果的清晰解释。

**核心思路**：TimeCopilot的核心思路是将多种时间序列基础模型与大型语言模型结合，通过统一的API实现自动化预测流程，提升预测的效率和可解释性。

**技术框架**：TimeCopilot的整体架构包括特征分析、模型选择、交叉验证和预测生成四个主要模块。用户可以通过自然语言与系统交互，获取预测结果和解释。

**关键创新**：TimeCopilot的最大创新在于其LLM无关性和对多种预测家族的支持，使得用户能够灵活选择模型并进行集成，显著提升了预测的准确性和效率。

**关键设计**：在设计上，TimeCopilot采用了灵活的参数设置，支持多种损失函数和网络结构，以适应不同的预测任务和数据特征。

## 📊 实验亮点

在GIFT-Eval基准测试中，TimeCopilot展示了其卓越的性能，达到了最先进的概率预测水平，且成本显著低于现有方法。这一成果表明TimeCopilot在时间序列预测领域的有效性和实用性，具有重要的应用前景。

## 🎯 应用场景

TimeCopilot框架可广泛应用于金融、气象、供应链管理等领域，帮助企业实现高效的时间序列预测。其自动化和可解释性特征使得用户能够更好地理解预测结果，从而做出更为精准的决策。未来，该框架有潜力推动智能决策系统的发展，提升各行业的预测能力。

## 📄 摘要（原文）

> We introduce TimeCopilot, the first open-source agentic framework for forecasting that combines multiple Time Series Foundation Models (TSFMs) with Large Language Models (LLMs) through a single unified API. TimeCopilot automates the forecasting pipeline: feature analysis, model selection, cross-validation, and forecast generation, while providing natural language explanations and supporting direct queries about the future. The framework is LLM-agnostic, compatible with both commercial and open-source models, and supports ensembles across diverse forecasting families. Results on the large-scale GIFT-Eval benchmark show that TimeCopilot achieves state-of-the-art probabilistic forecasting performance at low cost. Our framework provides a practical foundation for reproducible, explainable, and accessible agentic forecasting systems.

