---
layout: default
title: Continual Self-Supervised Learning with Masked Autoencoders in Remote Sensing
---

# Continual Self-Supervised Learning with Masked Autoencoders in Remote Sensing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21312" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21312v1</a>
  <a href="https://arxiv.org/pdf/2506.21312.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21312v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21312v1', 'Continual Self-Supervised Learning with Masked Autoencoders in Remote Sensing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lars Möllenbrok, Behnood Rasti, Begüm Demir

**分类**: cs.CV

**发布日期**: 2025-06-26

**备注**: Accepted to IEEE Geoscience and Remote Sensing Letters. Our code is available at https://git.tu-berlin.de/rsim/CoSMAE

**DOI**: [10.1109/LGRS.2025.3579585](https://doi.org/10.1109/LGRS.2025.3579585)

---

## 💡 一句话要点

**提出CoSMAE以解决遥感中的持续学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `持续学习` `自监督学习` `遥感` `知识蒸馏` `数据混合` `模型混合` `灾难性遗忘` `深度学习`

## 📋 核心要点

1. 现有的持续学习方法在遥感领域通常依赖大量标记样本，导致成本高且难以实现。
2. 本文提出的CoSMAE方法通过数据混合和模型混合知识蒸馏来解决灾难性遗忘问题。
3. 实验结果显示，CoSMAE在多个基准上相较于现有方法提升了最高4.94%的性能。

## 📝 摘要（中文）

持续学习（CL）方法的发展旨在从不断获取的训练数据中以顺序方式学习新任务，近年来在遥感（RS）领域受到广泛关注。现有的CL方法在学习新任务时，增强了对灾难性遗忘的鲁棒性，但通常需要大量标记训练样本，这在遥感中成本高且不易获得。为此，本文提出了一种新颖的持续自监督学习方法CoSMAE，结合了数据混合和模型混合知识蒸馏两个组件，以更好地在任务间进行泛化并降低灾难性遗忘的风险。实验结果表明，CoSMAE在应用于MAE的CL方法中，性能提升显著，最高可达4.94%。

## 🔬 方法详解

**问题定义**：本文旨在解决遥感领域中持续学习方法对标记样本依赖过重的问题，导致灾难性遗忘的现象。现有方法在学习新任务时，往往无法有效保留旧任务的信息。

**核心思路**：CoSMAE的核心思想是通过数据混合和模型混合知识蒸馏来增强模型的鲁棒性，确保在学习新任务时能够保留旧任务的知识。数据混合通过插值当前任务与过去任务的图像来保持信息，而模型混合则通过插值模型权重来进行知识蒸馏。

**技术框架**：CoSMAE的整体架构包括两个主要模块：数据混合模块和模型混合知识蒸馏模块。数据混合模块负责处理输入数据，确保信息的保留；模型混合模块则通过蒸馏技术整合过去和当前模型的知识。

**关键创新**：CoSMAE的创新之处在于将数据混合与模型混合知识蒸馏相结合，形成了一种新的自监督学习框架。这一设计使得模型在面对新任务时，能够有效减少灾难性遗忘的风险。

**关键设计**：在实现中，CoSMAE采用了特定的损失函数来平衡数据和模型的学习过程，同时在网络结构上进行了优化，以支持混合操作的高效执行。

## 📊 实验亮点

实验结果表明，CoSMAE在多个基准测试中相较于最先进的持续学习方法提升了最高4.94%的性能，展示了其在减少灾难性遗忘和增强模型泛化能力方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括遥感图像分析、环境监测和农业监控等。通过提升模型在新任务学习中的表现，CoSMAE能够帮助研究人员和工程师更高效地利用遥感数据，推动相关领域的技术进步和应用落地。

## 📄 摘要（原文）

> The development of continual learning (CL) methods, which aim to learn new tasks in a sequential manner from the training data acquired continuously, has gained great attention in remote sensing (RS). The existing CL methods in RS, while learning new tasks, enhance robustness towards catastrophic forgetting. This is achieved by using a large number of labeled training samples, which is costly and not always feasible to gather in RS. To address this problem, we propose a novel continual self-supervised learning method in the context of masked autoencoders (denoted as CoSMAE). The proposed CoSMAE consists of two components: i) data mixup; and ii) model mixup knowledge distillation. Data mixup is associated with retaining information on previous data distributions by interpolating images from the current task with those from the previous tasks. Model mixup knowledge distillation is associated with distilling knowledge from past models and the current model simultaneously by interpolating their model weights to form a teacher for the knowledge distillation. The two components complement each other to regularize the MAE at the data and model levels to facilitate better generalization across tasks and reduce the risk of catastrophic forgetting. Experimental results show that CoSMAE achieves significant improvements of up to 4.94% over state-of-the-art CL methods applied to MAE. Our code is publicly available at: https://git.tu-berlin.de/rsim/CoSMAE.

