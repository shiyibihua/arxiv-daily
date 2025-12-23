---
layout: default
title: Curriculum Reinforcement Learning from Easy to Hard Tasks Improves LLM Reasoning
---

# Curriculum Reinforcement Learning from Easy to Hard Tasks Improves LLM Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06632" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06632v2</a>
  <a href="https://arxiv.org/pdf/2506.06632.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06632v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06632v2', 'Curriculum Reinforcement Learning from Easy to Hard Tasks Improves LLM Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shubham Parashar, Shurui Gui, Xiner Li, Hongyi Ling, Sushil Vemuri, Blake Olson, Eric Li, Yu Zhang, James Caverlee, Dileep Kalathil, Shuiwang Ji

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-07 (更新: 2025-11-02)

**🔗 代码/项目**: [GITHUB](https://github.com/divelab/E2H-Reasoning)

---

## 💡 一句话要点

**提出E2H Reasoner以提升大语言模型的推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `推理能力` `课程学习` `大语言模型` `任务调度` `模型训练` `样本复杂度` `E2H Reasoner`

## 📋 核心要点

1. 现有的强化学习方法在处理本质上困难的推理任务时效果不佳，容易导致模型过拟合。
2. 本研究提出E2H Reasoner，通过从简单到困难的任务调度，帮助大语言模型逐步建立推理能力。
3. 实验结果表明，E2H Reasoner显著提升了小型语言模型的推理能力，相较于传统RL方法效果更佳。

## 📝 摘要（中文）

本研究旨在通过强化学习（RL）提升语言模型的推理能力。尽管现有的RL后训练模型如DeepSeek-R1在数学和编码任务上展现了推理能力，但单靠RL在本质上困难的任务上提升推理效果的研究较少。我们借鉴了课程学习的理念，提出了从简单到困难（E2H）的任务调度方法，使大语言模型能够逐步建立推理技能。通过实验证明，E2H Reasoner显著提升了小型语言模型（1.5B到3B）的推理能力，尤其是在仅使用传统RL训练时表现不佳的情况下。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有强化学习方法在推理任务中效果不佳的问题，尤其是在面对复杂任务时，模型容易过拟合，导致推理能力不足。

**核心思路**：我们提出E2H Reasoner，通过课程学习的理念，从简单任务逐步过渡到困难任务，使模型能够逐步掌握推理技能。这种逐步学习的方式有助于模型在复杂任务上更好地进行推理。

**技术框架**：E2H Reasoner的整体架构包括任务调度模块和强化学习模块。任务调度模块负责根据模型的学习进度调整任务难度，而强化学习模块则用于优化模型的推理策略。

**关键创新**：本研究的主要创新在于提出了E2H的任务调度策略，强调了在学习过程中逐步增加任务难度的重要性。这与传统的直接学习方法形成了鲜明对比，后者往往忽视了任务难度的渐进性。

**关键设计**：在设计中，我们设置了适当的任务难度衰减策略，以防止模型过拟合。此外，我们还在理论上建立了E2H Reasoner的收敛性保证，并推导了有限样本复杂度界限，确保在适当的任务分解和条件下，课程学习阶段所需的样本总数少于直接学习。

## 📊 实验亮点

实验结果显示，E2H Reasoner在多个领域的推理能力上显著优于传统的强化学习方法。具体而言，小型语言模型在推理任务中的表现提升幅度达到了XX%，有效解决了在仅使用传统RL训练时的性能瓶颈。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动化推理系统和智能助手等。通过提升大语言模型的推理能力，E2H Reasoner可以在复杂问题求解、编程辅助和智能问答等场景中发挥重要作用，未来可能对人机交互和智能决策产生深远影响。

## 📄 摘要（原文）

> We aim to improve the reasoning capabilities of language models via reinforcement learning (RL). Recent RL post-trained models like DeepSeek-R1 have demonstrated reasoning abilities on mathematical and coding tasks. However, prior studies suggest that using RL alone to improve reasoning on inherently difficult tasks is less effective. Here, we draw inspiration from curriculum learning and propose to schedule tasks from easy to hard (E2H), allowing LLMs to build reasoning skills gradually. Our method is termed E2H Reasoner. Empirically, we observe that, although easy tasks are important initially, fading them out through appropriate scheduling is essential in preventing overfitting. Theoretically, we establish convergence guarantees for E2H Reasoner within an approximate policy iteration framework. We derive finite-sample complexity bounds and show that when tasks are appropriately decomposed and conditioned, learning through curriculum stages requires fewer total samples than direct learning. Experiments across multiple domains show that E2H Reasoner significantly improves the reasoning ability of small LLMs (1.5B to 3B), which otherwise struggle when trained with vanilla RL alone, highlighting the effectiveness of our method. Our code can be found on https://github.com/divelab/E2H-Reasoning.

