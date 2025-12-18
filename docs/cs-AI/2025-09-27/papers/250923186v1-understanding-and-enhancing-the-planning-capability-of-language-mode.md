---
layout: default
title: Understanding and Enhancing the Planning Capability of Language Models via Multi-Token Prediction
---

# Understanding and Enhancing the Planning Capability of Language Models via Multi-Token Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23186" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23186v1</a>
  <a href="https://arxiv.org/pdf/2509.23186.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23186v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23186v1', 'Understanding and Enhancing the Planning Capability of Language Models via Multi-Token Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qimin Zhong, Hao Liao, Siwei Wang, Mingyang Zhou, Xiaoqun Wu, Rui Mao, Wei Chen

**分类**: cs.AI, cs.LG

**发布日期**: 2025-09-27

---

## 💡 一句话要点

**通过多Token预测增强语言模型在复杂规划中的推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `复杂规划` `传递关系学习` `多Token预测` `Transformer` `路径规划` `Next-Token Injection`

## 📋 核心要点

1. 现有大型语言模型在复杂规划任务中，难以有效学习传递关系，限制了其规划能力。
2. 论文提出通过多Token预测范式，利用Transformer架构中的传递层学习多步邻接信息，从而提升模型对传递关系的推理能力。
3. 实验结果表明，所提出的Next-Token Injection和Transformer-based传递层能够显著增强模型在路径规划任务中的性能。

## 📝 摘要（中文）

大型语言模型(LLMs)在各种任务中表现出色，但在学习传递关系方面仍然存在困难，而传递关系是复杂规划的基石。为了解决这个问题，我们研究了多Token预测(MTP)范式及其对传递关系学习的影响。我们使用由共享输出头和传递层组成的Transformer架构，从理论上分析了MTP范式。我们的分析表明，传递层逐渐学习多步邻接信息，从而使骨干模型能够捕获未观察到的传递可达关系，即使这些关系并非直接存在于训练数据中，但邻接估计中存在一些不可避免的噪声。在此基础上，我们提出了两种策略来增强传递层和整体学习质量：Next-Token Injection (NTI)和基于Transformer的传递层。我们在合成图和Blocksworld规划基准上的实验验证了我们的理论发现，并表明这些改进显著增强了模型的路径规划能力。这些发现加深了我们对具有MTP的Transformer如何在复杂规划任务中学习的理解，并提供了克服传递瓶颈的实用策略，为结构感知和通用规划模型铺平了道路。

## 🔬 方法详解

**问题定义**：大型语言模型在处理需要传递推理的复杂规划任务时，例如路径规划，表现不佳。现有的语言模型难以从有限的训练数据中泛化到未见过的传递关系，这主要是因为它们难以学习和利用数据中隐含的传递性信息。

**核心思路**：论文的核心思路是利用多Token预测（MTP）范式，通过预测多个后续token，迫使模型学习数据中的多步邻接关系。具体来说，论文认为Transformer架构中的传递层能够逐步学习多步邻接信息，从而使模型能够推断出训练数据中未直接观察到的传递可达关系。

**技术框架**：论文使用一个Transformer架构，该架构包含一个共享输出头和一个传递层。传递层负责学习多步邻接信息，而共享输出头则负责预测下一个token。论文提出了两种增强传递层和整体学习质量的策略：Next-Token Injection (NTI) 和 Transformer-based 传递层。NTI通过在训练过程中注入下一个token的信息来帮助传递层更好地学习邻接关系。Transformer-based传递层则使用一个Transformer结构来建模传递层，从而提高其学习能力。

**关键创新**：论文的关键创新在于理论分析了MTP范式在传递关系学习中的作用，并提出了两种增强传递层学习能力的策略。与现有方法相比，论文的方法更加关注如何利用Transformer架构的特性来学习和利用数据中的传递性信息。

**关键设计**：论文的关键设计包括：1) 使用Transformer架构作为基础模型；2) 设计传递层来学习多步邻接信息；3) 提出Next-Token Injection (NTI)策略，通过注入下一个token的信息来帮助传递层学习；4) 使用Transformer-based传递层来提高传递层的学习能力。具体的参数设置和损失函数等细节在论文中有详细描述。

## 📊 实验亮点

论文在合成图和Blocksworld规划基准上进行了实验。实验结果表明，所提出的Next-Token Injection (NTI)和Transformer-based传递层能够显著增强模型的路径规划能力。例如，在Blocksworld数据集上，模型的规划成功率得到了显著提升，验证了理论分析的正确性。

## 🎯 应用场景

该研究成果可应用于各种需要复杂规划和推理的领域，例如机器人导航、任务调度、供应链管理和游戏AI。通过提升语言模型在传递关系学习方面的能力，可以构建更智能、更通用的规划模型，从而在实际应用中实现更高效、更可靠的决策。

## 📄 摘要（原文）

> Large Language Models (LLMs) have achieved impressive performance across diverse tasks but continue to struggle with learning transitive relations, a cornerstone for complex planning. To address this issue, we investigate the Multi-Token Prediction (MTP) paradigm and its impact to transitive relation learning. We theoretically analyze the MTP paradigm using a Transformer architecture composed of a shared output head and a transfer layer. Our analysis reveals that the transfer layer gradually learns the multi-step adjacency information, which in turn enables the backbone model to capture unobserved transitive reachability relations beyond those directly present in the training data, albeit with some inevitable noise in adjacency estimation. Building on this foundation, we propose two strategies to enhance the transfer layer and overall learning quality: Next-Token Injection (NTI) and a Transformer-based transfer layer. Our experiments on both synthetic graphs and the Blocksworld planning benchmark validate our theoretical findings and demonstrate that the improvements significantly enhance the model's path-planning capability. These findings deepen our understanding of how Transformers with MTP learn in complex planning tasks, and provide practical strategies to overcome the transitivity bottleneck, paving the way toward structurally aware and general-purpose planning models.

