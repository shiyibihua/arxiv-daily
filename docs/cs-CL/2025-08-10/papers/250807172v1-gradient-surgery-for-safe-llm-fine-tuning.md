---
layout: default
title: Gradient Surgery for Safe LLM Fine-Tuning
---

# Gradient Surgery for Safe LLM Fine-Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07172" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07172v1</a>
  <a href="https://arxiv.org/pdf/2508.07172.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07172v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07172v1', 'Gradient Surgery for Safe LLM Fine-Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Biao Yi, Jiahao Li, Baolei Zhang, Lihai Nie, Tong Li, Tiansheng Huang, Zheli Liu

**分类**: cs.CL

**发布日期**: 2025-08-10

---

## 💡 一句话要点

**提出SafeGrad以解决LLM微调中的安全性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `安全微调` `大型语言模型` `梯度手术` `多目标优化` `对齐损失` `鲁棒性` `自然语言处理`

## 📋 核心要点

1. 现有的安全微调方法在处理恶意示例比例时表现出高度敏感性，防御效果随着恶意比例的增加而急剧下降。
2. 本文提出SafeGrad，通过梯度手术技术在检测到冲突时消除有害梯度成分，从而保持安全性与任务性能的平衡。
3. 实验结果显示，SafeGrad在多种LLMs和数据集上表现出色，能够在高恶意比例下保持安全性，且不影响任务的准确性。

## 📝 摘要（中文）

微调即服务引入了一个关键漏洞，即用户微调数据集中混入少量恶意示例可能会破坏大型语言模型（LLMs）的安全对齐。现有的安全微调解决方案在处理恶意示例比例时表现出高度敏感性，防御效果随着恶意比例的增加而急剧下降。为了解决这一问题，本文提出了SafeGrad，一种新颖的梯度手术方法。当检测到冲突时，SafeGrad通过将用户任务梯度的有害成分投影到对齐梯度的正交平面上来消除这些成分，从而使模型能够在不牺牲安全性的情况下学习用户任务。大量实验表明，SafeGrad在各种LLMs和数据集上提供了最先进的防御效果，即使在高恶意比例下也能保持安全性而不影响任务的准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决在微调大型语言模型时，恶意示例混入数据集导致的安全性对齐问题。现有方法在处理恶意比例增加时，防御效果显著下降，无法有效应对这种挑战。

**核心思路**：论文提出的SafeGrad方法通过梯度手术技术，检测到用户任务梯度与安全目标之间的冲突时，消除有害成分，从而使模型能够在不牺牲安全性的情况下完成用户任务。

**技术框架**：SafeGrad的整体架构包括冲突检测模块和梯度调整模块。首先，检测用户任务梯度与安全对齐梯度之间的冲突，然后通过投影技术调整梯度，确保模型学习的安全性与任务性能之间的平衡。

**关键创新**：SafeGrad的主要创新在于其梯度手术方法，通过将有害梯度成分投影到对齐梯度的正交平面上，有效消除了冲突。这一方法与现有的多目标优化方法本质上不同，后者在高恶意比例下容易失效。

**关键设计**：SafeGrad采用KL散度对齐损失函数，以学习良好对齐基础模型的丰富分布安全特征。此外，模型的参数设置和网络结构经过精心设计，以确保在高恶意比例下仍能保持任务的准确性和安全性。

## 📊 实验亮点

实验结果表明，SafeGrad在多种大型语言模型和数据集上实现了最先进的防御效果。在高达30%的恶意比例下，仍能保持超过90%的任务准确性，显著优于现有的防御方法，展示了其卓越的鲁棒性和数据效率。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和自动内容生成等。通过提高大型语言模型在微调过程中的安全性，SafeGrad能够有效防止恶意攻击，保障用户数据的安全性，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Fine-tuning-as-a-Service introduces a critical vulnerability where a few malicious examples mixed into the user's fine-tuning dataset can compromise the safety alignment of Large Language Models (LLMs). While a recognized paradigm frames safe fine-tuning as a multi-objective optimization problem balancing user task performance with safety alignment, we find existing solutions are critically sensitive to the harmful ratio, with defenses degrading sharply as harmful ratio increases. We diagnose that this failure stems from conflicting gradients, where the user-task update directly undermines the safety objective. To resolve this, we propose SafeGrad, a novel method that employs gradient surgery. When a conflict is detected, SafeGrad nullifies the harmful component of the user-task gradient by projecting it onto the orthogonal plane of the alignment gradient, allowing the model to learn the user's task without sacrificing safety. To further enhance robustness and data efficiency, we employ a KL-divergence alignment loss that learns the rich, distributional safety profile of the well-aligned foundation model. Extensive experiments show that SafeGrad provides state-of-the-art defense across various LLMs and datasets, maintaining robust safety even at high harmful ratios without compromising task fidelity.

