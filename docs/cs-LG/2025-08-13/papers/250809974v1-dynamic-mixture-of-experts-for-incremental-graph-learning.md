---
layout: default
title: Dynamic Mixture-of-Experts for Incremental Graph Learning
---

# Dynamic Mixture-of-Experts for Incremental Graph Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09974" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09974v1</a>
  <a href="https://arxiv.org/pdf/2508.09974.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09974v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09974v1', 'Dynamic Mixture-of-Experts for Incremental Graph Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lecheng Kong, Theodore Vasiloudis, Seongjun Yun, Han Xie, Xiang Song

**分类**: cs.LG

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出动态专家混合模型以解决增量图学习问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `增量学习` `图神经网络` `混合专家` `灾难性遗忘` `机器学习` `模型适应性` `稀疏计算`

## 📋 核心要点

1. 现有图机器学习方法在增量学习中容易出现灾难性遗忘，无法有效保留先前知识。
2. 本文提出动态混合专家（DyMoE）方法，通过引入新的专家网络来适应新数据，同时保持旧专家的能力。
3. 实验结果显示，模型在类别增量学习中相较于最佳基线提高了4.92%的相对准确率，验证了其有效性。

## 📝 摘要（中文）

图增量学习是一种学习范式，旨在使训练好的模型能够适应不断增加的图和数据，而无需对完整数据集进行重新训练。然而，常规图机器学习方法在增量学习中容易出现灾难性遗忘，导致先前学习的知识被新知识覆盖。为了解决这一问题，本文提出了一种动态混合专家（DyMoE）方法，设计了定制的正则化损失函数，以帮助新专家有效学习新数据，同时保持现有专家解决旧任务的能力。实验结果表明，该模型在类别增量学习中相较于最佳基线提高了4.92%的相对准确率，展示了其卓越的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决增量图学习中的灾难性遗忘问题，现有方法未能有效保留不同时间点学习的知识，导致新旧知识冲突。

**核心思路**：提出动态混合专家（DyMoE）方法，通过引入针对新数据块的专家网络，结合定制的正则化损失函数，使得新旧专家能够协同工作。

**技术框架**：整体架构包括一个DyMoE图神经网络层，动态添加新专家，并通过稀疏MoE策略仅选择最相关的专家进行预测，从而降低计算成本。

**关键创新**：动态混合专家模型的设计使得不同时间点的知识能够被有效利用，避免了传统方法中知识的冲突和遗忘。

**关键设计**：定制的正则化损失函数利用数据序列信息，确保旧专家在学习新任务时仍能保持对旧任务的解决能力，同时引入稀疏MoE策略，仅激活前k个最相关的专家以减少计算开销。

## 📊 实验亮点

实验结果表明，DyMoE模型在类别增量学习任务中相较于最佳基线提高了4.92%的相对准确率，显示出其在处理增量数据时的优越性能和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括社交网络分析、推荐系统和智能交通等领域，能够在不断变化的数据环境中保持模型的有效性和准确性。未来，随着数据的持续增长，DyMoE方法有望在实时学习和在线推理中发挥重要作用。

## 📄 摘要（原文）

> Graph incremental learning is a learning paradigm that aims to adapt trained models to continuously incremented graphs and data over time without the need for retraining on the full dataset. However, regular graph machine learning methods suffer from catastrophic forgetting when applied to incremental learning settings, where previously learned knowledge is overridden by new knowledge. Previous approaches have tried to address this by treating the previously trained model as an inseparable unit and using techniques to maintain old behaviors while learning new knowledge. These approaches, however, do not account for the fact that previously acquired knowledge at different timestamps contributes differently to learning new tasks. Some prior patterns can be transferred to help learn new data, while others may deviate from the new data distribution and be detrimental. To address this, we propose a dynamic mixture-of-experts (DyMoE) approach for incremental learning. Specifically, a DyMoE GNN layer adds new expert networks specialized in modeling the incoming data blocks. We design a customized regularization loss that utilizes data sequence information so existing experts can maintain their ability to solve old tasks while helping the new expert learn the new data effectively. As the number of data blocks grows over time, the computational cost of the full mixture-of-experts (MoE) model increases. To address this, we introduce a sparse MoE approach, where only the top-$k$ most relevant experts make predictions, significantly reducing the computation time. Our model achieved 4.92\% relative accuracy increase compared to the best baselines on class incremental learning, showing the model's exceptional power.

