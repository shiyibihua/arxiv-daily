---
layout: default
title: TiCard: Deployable EXPLAIN-only Residual Learning for Cardinality Estimation
---

# TiCard: Deployable EXPLAIN-only Residual Learning for Cardinality Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14358" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14358v1</a>
  <a href="https://arxiv.org/pdf/2512.14358.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14358v1" onclick="toggleFavorite(this, '2512.14358v1', 'TiCard: Deployable EXPLAIN-only Residual Learning for Cardinality Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qizhi Wang

**分类**: cs.AI, cs.DB

**发布日期**: 2025-12-16

**备注**: 16 pages(/wo references), 4 figures, 10 tables

---

## 💡 一句话要点

**TiCard：一种可部署的、仅使用EXPLAIN信息的基数估计残差学习框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `基数估计` `查询优化` `残差学习` `EXPLAIN信息` `低侵入性`

## 📋 核心要点

1. 现有基数估计器在处理复杂查询时精度不足，学习型方法部署成本高，难以集成到现有数据库系统中。
2. TiCard通过学习原生估计器的残差校正，仅使用EXPLAIN信息进行训练和推理，降低了侵入性。
3. 实验表明，TiCard在TPCH和Join Order Benchmark上显著提高了尾部查询的基数估计精度，P99 Q-error降低了一个数量级。

## 📝 摘要（中文）

基数估计是基于代价的查询优化的关键瓶颈，但可部署的改进仍然困难：经典估计器会遗漏相关性，而学习型估计器通常需要特定于工作负载的训练流程以及对优化器的侵入式集成。本文提出了TiCard，一个低侵入、基于校正的框架，它增强（而不是替换）数据库的原生估计器。TiCard使用仅来自EXPLAIN的特征学习乘法残差校正，并且仅使用EXPLAIN ANALYZE进行离线标签生成。我们研究了两种实际的实例化：（i）用于亚毫秒级推理的梯度提升回归器，以及（ii）TabPFN，一种通过刷新小型参考集来适应的上下文表格基础模型，无需梯度重新训练。在使用TPCH和Join Order Benchmark的TiDB上，在低跟踪设置（总共263次执行；157次用于学习）中，TiCard显着提高了算子级别的尾部精度：P90 Q-error从312.85（原生）降至13.69（TiCard-GBR），P99从37,974.37降至3,416.50（TiCard-TabPFN），而仅连接策略保持了近乎完美的中间值行为。我们将TiCard定位为专注于可部署性的AI4DB构建块：明确的范围、保守的集成策略以及从离线校正到优化器内使用的集成路线图。

## 🔬 方法详解

**问题定义**：基数估计是查询优化的核心，准确的基数估计对于选择最佳查询执行计划至关重要。然而，传统的基数估计方法难以捕捉复杂查询中的数据相关性，导致估计误差较大。现有的学习型基数估计器虽然精度较高，但通常需要大量的训练数据和复杂的训练流程，并且需要侵入式地集成到数据库优化器中，部署成本高昂。

**核心思路**：TiCard的核心思想是利用机器学习方法学习原生基数估计器的残差，即预测原生估计器与真实基数之间的差距。通过学习残差，TiCard可以在不替换原生估计器的情况下，提高基数估计的准确性。此外，TiCard仅使用EXPLAIN信息进行训练和推理，避免了对数据库内部数据的直接访问，降低了侵入性。

**技术框架**：TiCard的整体框架包括以下几个主要步骤：1）使用EXPLAIN ANALYZE获取查询的真实基数；2）使用EXPLAIN获取查询的特征信息；3）使用机器学习模型学习EXPLAIN特征与基数残差之间的映射关系；4）在查询优化过程中，首先使用原生估计器进行基数估计，然后使用TiCard预测残差，并将两者相加得到最终的基数估计值。TiCard支持多种机器学习模型，包括梯度提升回归器（GBR）和TabPFN。

**关键创新**：TiCard的关键创新在于其低侵入性的设计。通过仅使用EXPLAIN信息进行训练和推理，TiCard避免了对数据库内部数据的直接访问，降低了部署成本和风险。此外，TiCard采用残差学习的方法，可以在不替换原生估计器的情况下，提高基数估计的准确性。

**关键设计**：TiCard的关键设计包括：1）特征选择：选择与基数估计相关的EXPLAIN特征，例如算子类型、谓词条件等；2）模型选择：选择合适的机器学习模型，例如GBR或TabPFN，并进行参数调优；3）训练策略：采用合适的训练策略，例如离线训练或在线学习，以提高模型的泛化能力；4）集成策略：设计合适的集成策略，将TiCard集成到数据库优化器中，例如在查询优化过程中动态调整基数估计值。

## 📊 实验亮点

在TiDB数据库上，使用TPCH和Join Order Benchmark进行实验，结果表明TiCard显著提高了基数估计的准确性。使用梯度提升回归器（TiCard-GBR）时，P90 Q-error从原生估计器的312.85降至13.69。使用TabPFN（TiCard-TabPFN）时，P99 Q-error从原生估计器的37,974.37降至3,416.50。这些结果表明，TiCard在提高尾部查询的基数估计精度方面具有显著优势。

## 🎯 应用场景

TiCard可应用于各种数据库系统，以提高查询优化器的性能。通过提高基数估计的准确性，TiCard可以帮助优化器选择更优的查询执行计划，从而降低查询延迟，提高系统吞吐量。此外，TiCard的低侵入性设计使其易于部署和集成，降低了使用成本。

## 📄 摘要（原文）

> Cardinality estimation is a key bottleneck for cost-based query optimization, yet deployable improvements remain difficult: classical estimators miss correlations, while learned estimators often require workload-specific training pipelines and invasive integration into the optimizer. This paper presents TiCard, a low intrusion, correction-based framework that augments (rather than replaces) a database's native estimator. TiCard learns multiplicative residual corrections using EXPLAIN-only features, and uses EXPLAIN ANALYZE only for offline labels. We study two practical instantiations: (i) a Gradient Boosting Regressor for sub-millisecond inference, and (ii) TabPFN, an in-context tabular foundation model that adapts by refreshing a small reference set without gradient retraining. On TiDB with TPCH and the Join Order Benchmark, in a low-trace setting (263 executions total; 157 used for learning), TiCard improves operator-level tail accuracy substantially: P90 Q-error drops from 312.85 (native) to 13.69 (TiCard-GBR), and P99 drops from 37,974.37 to 3,416.50 (TiCard-TabPFN), while a join-only policy preserves near-perfect median behavior. We position TiCard as an AI4DB building block focused on deployability: explicit scope, conservative integration policies, and an integration roadmap from offline correction to in-optimizer use.

