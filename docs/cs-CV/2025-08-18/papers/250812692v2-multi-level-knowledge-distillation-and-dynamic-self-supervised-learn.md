---
layout: default
title: Multi-Level Knowledge Distillation and Dynamic Self-Supervised Learning for Continual Learning
---

# Multi-Level Knowledge Distillation and Dynamic Self-Supervised Learning for Continual Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12692" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12692v2</a>
  <a href="https://arxiv.org/pdf/2508.12692.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12692v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12692v2', 'Multi-Level Knowledge Distillation and Dynamic Self-Supervised Learning for Continual Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Taeheon Kim, San Kim, Minhyuk Seo, Dongjae Jeon, Wonje Jeung, Jonghyun Choi

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-08-18 (更新: 2025-08-22)

---

## 💡 一句话要点

**提出多层次知识蒸馏与动态自监督学习以解决持续学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `类增量学习` `知识蒸馏` `自监督学习` `动态加权` `未标记数据利用` `模型稳定性` `持续学习`

## 📋 核心要点

1. 现有的类增量学习方法通常假设每个任务包含未见过的类，缺乏对重复类引入的有效处理。
2. 论文提出的多层次知识蒸馏（MLKD）和动态自监督损失（SSL）方法，旨在高效利用外部未标记数据，提升模型的学习能力。
3. 实验结果显示，所提方法在CIR设置下显著提升了性能，在CVPR CLVISION挑战赛中获得第二名。

## 📝 摘要（中文）

本文研究了类增量学习中的重复类引入问题，提出了多层次知识蒸馏（MLKD）和动态自监督损失（SSL）两种新方法，以有效利用外部未标记数据，确保模型在类增量学习中的稳定性与灵活性。MLKD从多个先前模型中提取知识，涵盖特征和输出，增强模型对历史知识的保持能力；而动态SSL则加速新类的学习，同时通过动态加权保持对主要任务的关注。实验结果表明，所提方法在CVPR第五届CLVISION挑战赛中获得第二名，显著提升了CIR设置下的性能。

## 🔬 方法详解

**问题定义**：本文解决类增量学习中的重复类引入问题，现有方法在处理此类场景时表现不佳，导致模型无法有效保持历史知识。

**核心思路**：提出多层次知识蒸馏（MLKD）从多个先前模型中提取知识，并结合动态自监督损失（SSL）利用未标记数据，确保模型在学习新类时仍能保持对旧类的记忆。

**技术框架**：整体架构包括两个主要模块：MLKD模块用于知识提取，SSL模块用于未标记数据的自监督学习。通过动态加权机制，确保训练过程中的重点始终放在当前主要任务上。

**关键创新**：MLKD的创新在于从多个视角（特征与输出）提取知识，增强模型的知识保持能力；动态SSL则通过动态调整损失权重，优化新类学习过程。

**关键设计**：在MLKD中，设计了多层次的知识蒸馏策略，确保不同层次的知识被有效利用；在动态SSL中，采用动态加权策略，确保模型在学习新类时不遗忘旧类。具体的损失函数和网络结构设计细节在论文中有详细描述。

## 📊 实验亮点

在CVPR第五届CLVISION挑战赛中，所提方法获得第二名，显著提升了类增量学习的性能。实验结果表明，使用MLKD和动态SSL后，模型在CIR设置下的准确率提升了XX%，相较于基线方法表现出明显的优势。

## 🎯 应用场景

该研究的潜在应用领域包括机器人视觉、自动驾驶、智能监控等需要持续学习的场景。通过有效处理重复类引入问题，模型能够在动态环境中不断适应新任务，提升智能系统的灵活性和稳定性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Class-incremental with repetition (CIR), where previously trained classes repeatedly introduced in future tasks, is a more realistic scenario than the traditional class incremental setup, which assumes that each task contains unseen classes. CIR assumes that we can easily access abundant unlabeled data from external sources, such as the Internet. Therefore, we propose two components that efficiently use the unlabeled data to ensure the high stability and the plasticity of models trained in CIR setup. First, we introduce multi-level knowledge distillation (MLKD) that distills knowledge from multiple previous models across multiple perspectives, including features and logits, so the model can maintain much various previous knowledge. Moreover, we implement dynamic self-supervised loss (SSL) to utilize the unlabeled data that accelerates the learning of new classes, while dynamic weighting of SSL keeps the focus of training to the primary task. Both of our proposed components significantly improve the performance in CIR setup, achieving 2nd place in the CVPR 5th CLVISION Challenge.

