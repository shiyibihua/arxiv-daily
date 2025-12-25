---
layout: default
title: "Universal Transient Stability Analysis: A Large Language Model-Enabled Dynamics Prediction Framework"
---

# Universal Transient Stability Analysis: A Large Language Model-Enabled Dynamics Prediction Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20970" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20970v1</a>
  <a href="https://arxiv.org/pdf/2512.20970.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20970v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20970v1', 'Universal Transient Stability Analysis: A Large Language Model-Enabled Dynamics Prediction Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chao Shen, Ke Zuo, Mingyang Sun

**分类**: eess.SY

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**提出基于大语言模型的通用暂态稳定性分析框架，实现跨场景零样本泛化。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `暂态稳定性分析` `大语言模型` `动态预测` `零样本学习` `电力系统` `通用框架` `时间序列预测`

## 📋 核心要点

1. 现有暂态稳定性分析方法难以在不同运行条件和系统上泛化，需要针对特定场景进行重新训练。
2. TSA-LLM利用大语言模型，通过数据处理、参数高效微调和两阶段训练，实现跨场景的通用动态预测。
3. 实验表明，TSA-LLM在未见故障和系统上表现出色，仅需少量数据即可匹配专家性能，验证了其通用性。

## 📝 摘要（中文）

现有的暂态稳定性分析(TSA)动态预测框架难以实现多场景的“通用性”，即单个预训练架构在不同运行条件、未见故障和异构系统中的泛化能力。为了解决这个问题，本文提出了TSA-LLM，一个基于大语言模型(LLM)的通用框架，它将多变量暂态动态预测建模为单变量生成任务，具有三个关键创新：首先，一种新颖的数据处理流程，包括用于解决维度异构性的通道独立分解、用于消除独立稳定或不稳定流程的样本级归一化，以及用于高效长序列建模的时间分块；其次，一种参数高效的冻结和微调策略，该策略使用专用输入嵌入和输出投影层来增强LLM的架构，同时冻结核心Transformer块以保留通用特征提取能力；第三，一种两阶段微调方案，该方案结合了教师强制（在初始训练期间向模型提供真实数据）和计划采样（逐渐转向利用模型生成的预测），以减轻长时程迭代预测中的累积误差。全面的测试表明了该框架的通用性，因为仅在新英格兰39总线系统上训练的TSA-LLM实现了对混合稳定条件和未见故障的零样本泛化，并且仅使用5%的微调数据即可在更大的冰岛189总线系统上匹配专家性能。这种多场景的通用性验证了一个通用框架，该框架消除了特定于场景的重新训练，并通过大规模参数和跨场景训练数据实现了可扩展性。

## 🔬 方法详解

**问题定义**：现有的暂态稳定性分析(TSA)动态预测框架缺乏通用性，无法在不同的电力系统运行条件、未见过的故障类型以及异构的电力系统之间进行泛化。这意味着针对每个新的场景，都需要重新训练模型，这大大增加了计算成本和部署难度。现有方法通常依赖于特定场景的数据进行训练，缺乏跨场景的知识迁移能力。

**核心思路**：TSA-LLM的核心思路是将多变量的暂态动态预测问题转化为一个单变量的生成任务，并利用大语言模型(LLM)强大的序列建模能力来预测电力系统的动态行为。通过将多个变量解耦，并采用生成式的方式进行预测，可以有效地捕捉电力系统动态的复杂性和长期依赖关系。此外，通过冻结LLM的核心Transformer层，可以保留其通用的特征提取能力，并减少微调所需的参数量。

**技术框架**：TSA-LLM的整体框架包括三个主要阶段：数据处理、模型构建和模型训练。在数据处理阶段，首先进行通道独立分解，将多变量时间序列分解为多个单变量时间序列。然后，进行样本级归一化，消除稳定和不稳定样本之间的差异。最后，采用时间分块技术，将长序列分割成多个短序列，以提高训练效率。在模型构建阶段，使用预训练的LLM作为骨干网络，并添加专门的输入嵌入层和输出投影层。在模型训练阶段，采用两阶段微调策略，首先使用教师强制进行训练，然后使用计划采样逐渐过渡到模型生成的预测。

**关键创新**：TSA-LLM的关键创新在于其通用性。通过精心设计的数据处理流程和参数高效的微调策略，TSA-LLM能够在一个电力系统上训练，并在其他未见过的电力系统上进行零样本泛化。这种通用性大大降低了模型部署的成本和难度，并提高了模型的实用性。此外，两阶段微调策略有效地缓解了长时程迭代预测中的累积误差问题。

**关键设计**：在数据处理方面，通道独立分解将多变量问题转化为单变量问题，简化了建模的难度。样本级归一化消除了稳定和不稳定样本之间的差异，提高了模型的鲁棒性。时间分块技术提高了训练效率。在模型训练方面，两阶段微调策略结合了教师强制和计划采样的优点，有效地缓解了长时程迭代预测中的累积误差问题。具体来说，计划采样的概率随着训练的进行逐渐增加，使得模型能够逐渐适应自身生成的预测。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20970v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20970v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20970v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

TSA-LLM在New England 39总线系统上训练后，实现了对混合稳定条件和未见故障的零样本泛化。在更大的Iceland 189总线系统上，仅使用5%的微调数据，TSA-LLM的性能就能够匹配专家水平。这些结果表明，TSA-LLM具有很强的通用性和泛化能力。

## 🎯 应用场景

TSA-LLM可应用于电力系统运行的在线安全评估、控制策略优化和故障诊断。该框架能够快速准确地预测电力系统在不同运行条件下的动态行为，为电力系统的安全稳定运行提供保障。此外，TSA-LLM的通用性使其能够应用于不同的电力系统，降低了模型部署的成本和难度，具有广阔的应用前景。

## 📄 摘要（原文）

> Existing dynamics prediction frameworks for transient stability analysis (TSA) fail to achieve multi-scenario "universality"--the inherent ability of a single, pre-trained architecture to generalize across diverse operating conditions, unseen faults, and heterogeneous systems. To address this, this paper proposes TSA-LLM, a large language model (LLM)-based universal framework that models multi-variate transient dynamics prediction as a univariate generative task with three key innovations: First, a novel data processing pipeline featuring channel independence decomposition to resolve dimensional heterogeneity, sample-wise normalization to eliminate separate stable or unstable pipelines, and temporal patching for efficient long-sequence modeling; Second, a parameter-efficient freeze-and-finetune strategy that augments the LLM's architecture with dedicated input embedding and output projection layers while freezing core transformer blocks to preserve generic feature extraction capabilities; Third, a two-stage fine-tuning scheme that combines teacher forcing, which feeds the model ground-truth data during initial training, with scheduled sampling, which gradually shifts to leveraging model-generated predictions, to mitigate cumulative errors in long-horizon iterative prediction. Comprehensive testing demonstrates the framework's universality, as TSA-LLM trained solely on the New England 39-bus system achieves zero-shot generalization to mixed stability conditions and unseen faults, and matches expert performance on the larger Iceland 189-bus system with only 5% fine-tuning data. This multi-scenario versatility validates a universal framework that eliminates scenario-specific retraining and achieves scalability via large-scale parameters and cross-scenario training data.

