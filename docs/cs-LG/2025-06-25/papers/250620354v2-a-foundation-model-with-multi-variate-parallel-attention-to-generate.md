---
layout: default
title: A foundation model with multi-variate parallel attention to generate neuronal activity
---

# A foundation model with multi-variate parallel attention to generate neuronal activity

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20354" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20354v2</a>
  <a href="https://arxiv.org/pdf/2506.20354.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20354v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20354v2', 'A foundation model with multi-variate parallel attention to generate neuronal activity')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Francesco Carzaniga, Michael Hersche, Abu Sebastian, Kaspar Schindler, Abbas Rahimi

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-25 (更新: 2025-08-25)

**备注**: The code is available at https://github.com/IBM/multi-variate-parallel-transformer. The SWEC iEEG dataset is available at https://huggingface.co/datasets/NeuroTec/SWEC_iEEG_Dataset

**🔗 代码/项目**: [GITHUB](https://github.com/IBM/multi-variate-parallel-transformer) | [HUGGINGFACE](https://huggingface.co/datasets/NeuroTec)

---

## 💡 一句话要点

**提出多变量并行注意力机制以解决iEEG信号预测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多变量时间序列` `并行注意力` `深度学习` `颅内脑电图` `生成模型` `临床应用` `数据集发布`

## 📋 核心要点

1. 现有方法在处理具有异构通道配置的多变量时间序列时，面临着灵活性和可泛化性不足的问题。
2. 本文提出的MVPA机制通过解耦内容、时间和空间注意力，提供了一种高效的时间序列建模方法。
3. MVPFormer在多个iEEG任务中表现优异，超越了多个基准数据集的现有最先进模型，展示了强大的泛化能力。

## 📝 摘要（中文）

从具有异构通道配置的多变量时间序列中学习仍然是深度神经网络面临的基本挑战，尤其是在临床领域如颅内脑电图（iEEG）中。本文提出了一种新颖的自注意力机制——多变量并行注意力（MVPA），它能够解耦内容、时间和空间注意力，从而灵活、高效地建模具有不同通道数量和配置的时间序列数据。基于MVPA，我们构建了MVPFormer，一个用于人类电生理学的生成基础模型，能够预测不同受试者的iEEG信号演变。我们还发布了SWEC iEEG数据集，这是迄今为止最大的公开iEEG数据集，包含近10,000小时来自异构临床来源的记录。MVPFormer在多个iEEG任务中表现出专家级的性能，超越了当前最先进的Transformer基线。

## 🔬 方法详解

**问题定义**：本文旨在解决深度神经网络在处理具有异构通道配置的多变量时间序列时的灵活性和可泛化性不足的问题。现有方法往往无法有效适应不同受试者的iEEG信号特征。

**核心思路**：论文提出的MVPA机制通过解耦内容、时间和空间注意力，能够灵活地适应不同的通道配置，从而提高模型的泛化能力和效率。

**技术框架**：MVPFormer的整体架构包括输入层、MVPA模块和输出层。MVPA模块负责处理输入的多变量时间序列数据，提取相关的时间和空间特征。

**关键创新**：MVPA作为一种新的自注意力机制，能够有效解耦不同类型的注意力，显著提高了模型在处理异构时间序列数据时的性能，与现有方法相比具有本质的区别。

**关键设计**：在模型设计中，采用了特定的损失函数以优化预测精度，并在网络结构中引入了多层MVPA模块，以增强模型的表达能力和学习能力。具体的参数设置和网络层数根据实验结果进行了优化。

## 📊 实验亮点

MVPFormer在多个数据集上表现出色，尤其是在癫痫检测任务中，超越了SWEC、MAYO和FNUSA数据集上的现有最先进模型。此外，在四个Brain TreeBank iEEG解码任务中也达到了最先进的性能，验证了MVPA的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括临床电生理学、神经科学研究以及相关的医疗设备开发。通过提供一个开放源代码和开放数据的基础模型，研究者可以在此基础上进行进一步的探索和应用，推动iEEG信号分析的进步。

## 📄 摘要（原文）

> Learning from multi-variate time-series with heterogeneous channel configurations remains a fundamental challenge for deep neural networks, particularly in clinical domains such as intracranial electroencephalography (iEEG), where channel setups vary widely across subjects. In this work, we introduce multi-variate parallel attention (MVPA), a novel self-attention mechanism that disentangles content, temporal, and spatial attention, enabling flexible, generalizable, and efficient modeling of time-series data with varying channel counts and configurations. We use MVPA to build MVPFormer, a generative foundation model for human electrophysiology, trained to predict the evolution of iEEG signals across diverse subjects. To support this and future efforts by the community, we release the SWEC iEEG dataset, the largest publicly available iEEG dataset to date, comprising nearly 10,000 hours of recordings from heterogeneous clinical sources. MVPFormer leverages MVPA to achieve strong generalization across subjects, demonstrating expert-level performance in several iEEG tasks. MVPFormer surpasses state-of-the-art Transformer baselines in seizure detection across the SWEC, the MAYO, and the FNUSA datasets, while also achieving state-of-the-art performance on four Brain TreeBank iEEG decoding tasks. We further validate MVPA on standard time-series forecasting and classification tasks, where it matches or exceeds the performance of existing attention-based models. Together, our contributions establish MVPA as a general-purpose attention mechanism for heterogeneous time-series and MVPFormer as the first open-source, open-weights, and open-data iEEG foundation model with SOTA clinical performance. The code is available at https://github.com/IBM/multi-variate-parallel-transformer. The SWEC iEEG dataset is available at https://huggingface.co/datasets/NeuroTec/SWEC_iEEG_Dataset.

