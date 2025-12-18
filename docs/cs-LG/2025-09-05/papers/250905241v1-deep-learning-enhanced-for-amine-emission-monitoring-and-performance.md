---
layout: default
title: Deep Learning-Enhanced for Amine Emission Monitoring and Performance Analysis in Industrial Carbon Capture Plants
---

# Deep Learning-Enhanced for Amine Emission Monitoring and Performance Analysis in Industrial Carbon Capture Plants

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05241" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05241v1</a>
  <a href="https://arxiv.org/pdf/2509.05241.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05241v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05241v1', 'Deep Learning-Enhanced for Amine Emission Monitoring and Performance Analysis in Industrial Carbon Capture Plants')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lokendra Poudel, David Tincher, Duy-Nhat Phan, Rahul Bhowmik

**分类**: cs.LG

**发布日期**: 2025-09-05

---

## 💡 一句话要点

**利用深度学习预测胺排放与性能，优化工业碳捕获**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `碳捕获` `胺排放` `深度学习` `LSTM` `性能预测`

## 📋 核心要点

1. 胺排放监控是碳捕获的关键，但传统方法难以应对复杂动态工况，预测精度不足。
2. 利用深度学习模型，捕捉碳捕获过程的时序依赖关系，实现胺排放和系统性能的精准预测。
3. 实验表明，该模型预测精度超过99%，并通过因果分析优化操作参数，降低胺排放。

## 📝 摘要（中文）

本文提出了一种数据驱动的深度学习模型，用于预测和监控胺基后燃烧碳捕获系统中的胺排放和关键性能参数。利用Technology Center Mongstad的CESAR1溶剂实验的运行数据，开发了四种深度学习架构，包括基本长短期记忆网络（LSTM）、堆叠LSTM、双向LSTM和卷积LSTM，以捕捉随时间变化的过程行为。针对排放预测，模型设计用于预测通过FTIR和IMR-MS方法测量的2-氨基-2-甲基-1-丙醇（AMP）和哌嗪排放。系统性能模型针对四个关键参数：CO₂产品流量、吸收器出口温度、贫化烟气出口温度和RFCC汽提塔底部温度。这些模型实现了超过99%的高预测精度，并有效跟踪了稳定趋势和突发波动。此外，我们进行了因果影响分析，以评估操作变量如何影响排放和系统性能。通过在标称值的±20%范围内系统地扰动八个输入变量来模拟偏差并评估其影响。该分析表明，调整特定的操作参数，如贫溶剂温度和水洗条件，可以显著减少胺排放并提高系统性能。这项研究强调了机器学习不仅是一种预测工具，而且是一种决策支持系统，用于优化稳态和动态条件下的碳捕获操作。通过实现实时监控、情景测试和操作优化，开发的机器学习框架为减轻环境影响提供了一条切实可行的途径。这项工作代表了朝着智能化、数据驱动的控制策略迈出的一步，这些策略可以提高碳捕获和储存技术的效率、稳定性和可持续性。

## 🔬 方法详解

**问题定义**：论文旨在解决胺基碳捕获过程中胺排放难以精确预测和监控的问题。现有方法，如传统的控制策略和基于物理模型的预测方法，难以有效处理碳捕获过程的复杂非线性动态特性，导致预测精度不足，无法及时响应工况变化，从而影响碳捕获效率和环境安全。

**核心思路**：论文的核心思路是利用深度学习模型强大的非线性拟合能力和时序数据处理能力，直接从历史运行数据中学习胺排放和关键性能参数的变化规律。通过构建不同的深度学习架构，捕捉碳捕获过程中的复杂时序依赖关系，从而实现对胺排放和系统性能的精准预测和实时监控。

**技术框架**：整体框架包括数据预处理、模型构建、模型训练和模型评估四个主要阶段。首先，对从碳捕获工厂收集的运行数据进行清洗、标准化等预处理操作。然后，构建四种不同的深度学习模型，包括Basic LSTM、Stacked LSTM、Bi-directional LSTM和Convolutional LSTM。接着，使用历史运行数据对模型进行训练，优化模型参数。最后，使用测试数据评估模型的预测精度和泛化能力。

**关键创新**：论文的关键创新在于将深度学习技术应用于胺基碳捕获过程的胺排放预测和性能监控。与传统的基于物理模型的预测方法相比，深度学习模型能够直接从数据中学习复杂的过程动态，无需人工建模，具有更高的预测精度和更好的适应性。此外，论文还通过因果影响分析，评估了不同操作变量对胺排放和系统性能的影响，为优化碳捕获过程提供了决策支持。

**关键设计**：论文中，选择了四种不同的LSTM变体，以捕捉碳捕获过程中的不同时序特征。Basic LSTM用于捕捉基本的时序依赖关系，Stacked LSTM通过增加网络深度提高模型的表达能力，Bi-directional LSTM考虑了过去和未来的信息，Convolutional LSTM则利用卷积操作提取时序特征。此外，论文还设计了合适的损失函数，如均方误差（MSE），用于优化模型参数。输入变量包括lean solvent temperature和water wash conditions等操作参数。

## 📊 实验亮点

实验结果表明，所提出的深度学习模型能够以超过99%的精度预测胺排放和关键性能参数。通过因果影响分析，发现调整贫溶剂温度和水洗条件可以显著降低胺排放并提高系统性能。与传统方法相比，该模型具有更高的预测精度和更好的适应性，能够有效应对碳捕获过程中的复杂动态工况。

## 🎯 应用场景

该研究成果可应用于工业碳捕获工厂的胺排放监控和性能优化。通过实时预测胺排放和关键性能参数，可以及时发现异常工况，采取相应的控制措施，降低胺排放，提高碳捕获效率。此外，该模型还可以用于情景测试，评估不同操作参数对胺排放和系统性能的影响，为优化碳捕获过程提供决策支持。未来，该技术有望推广到其他类型的碳捕获系统，助力实现碳中和目标。

## 📄 摘要（原文）

> We present data driven deep learning models for forecasting and monitoring amine emissions and key performance parameters in amine-based post-combustion carbon capture systems. Using operational data from the CESAR1 solvent campaign at Technology Center Mongstad, four DL architectures such as Basic Long Short-Term Memory (LSTM), Stacked LSTM, Bi-directional LSTM, and Convolutional LSTM were developed to capture time-dependent process behavior. For emission prediction, models were designed for 2-amino-2-methyl-1-propanol (AMP) and Piperazine emissions measured via FTIR and IMR-MS methods. System performance models target four critical parameters: CO$_2$ product flow, absorber outlet temperature, depleted flue gas outlet temperature, and RFCC stripper bottom temperature. These models achieved high predictive accuracy exceeding 99% and effectively tracked both steady trends and abrupt fluctuations. Additionally, we conducted causal impact analysis to evaluate how operational variables influence emissions and system performance. Eight input variables were systematically perturbed within $\pm$20% of nominal values to simulate deviations and assess their impact. This analysis revealed that adjusting specific operational parameters, such as lean solvent temperature and water wash conditions, can significantly reduce amine emissions and enhance system performance. This study highlights ML not only as a predictive tool but also as a decision support system for optimizing carbon capture operations under steady state and dynamic conditions. By enabling real time monitoring, scenario testing, and operational optimization, the developed ML framework offers a practical pathway for mitigating environmental impacts. This work represents a step toward intelligent, data-driven control strategies that enhance the efficiency, stability, and sustainability of carbon capture and storage technologies.

