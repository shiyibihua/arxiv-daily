---
layout: default
title: Improving Pre-Trained Vision-Language-Action Policies with Model-Based Search
---

# Improving Pre-Trained Vision-Language-Action Policies with Model-Based Search

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12211" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12211v2</a>
  <a href="https://arxiv.org/pdf/2508.12211.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12211v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12211v2', 'Improving Pre-Trained Vision-Language-Action Policies with Model-Based Search')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cyrus Neary, Omar G. Younis, Artur Kuramshin, Ozgur Aslan, Glen Berseth

**分类**: cs.RO, cs.AI

**发布日期**: 2025-08-17 (更新: 2025-11-12)

---

## 💡 一句话要点

**提出VLAPS框架以提升预训练视觉-语言-动作策略的性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `模型搜索` `蒙特卡洛树搜索` `机器人策略` `任务执行` `强化学习` `语言条件任务`

## 📋 核心要点

1. 现有的预训练视觉-语言-动作模型在分布外场景中表现不佳，容易导致不安全的失败。
2. 本文提出的VLAPS框架通过将基于模型的搜索嵌入到VLA策略的推理中，提升了机器人任务的执行性能。
3. 实验结果显示，VLAPS在语言指定任务上成功率提高了67个百分点，显著优于传统的VLA基线。

## 📝 摘要（中文）

预训练的视觉-语言-动作（VLA）模型为通用机器人策略提供了良好的基础，但在零-shot部署于分布外场景时，往往会产生脆弱的行为或不安全的失败。本文提出了视觉-语言-动作规划与搜索（VLAPS）框架及相关算法，将基于模型的搜索嵌入到预训练VLA策略的推理过程中，以提高其在机器人任务上的表现。具体而言，我们的方法通过使用目标环境的模型，利用VLA策略定义的动作先验，偏向修改后的蒙特卡洛树搜索（MCTS）算法。通过在基于模型的搜索中使用VLA派生的抽象和先验，VLAPS有效探索语言条件的机器人任务，这些任务的搜索空间在没有信息的情况下是不可处理的。与直接遵循VLA策略的动作预测相比，VLAPS整合了基于模型的搜索与VLA策略的推理过程，产生了更高效的行为。实验结果表明，VLAPS在语言指定任务上显著优于仅使用VLA的基线，成功率提高了多达67个百分点。

## 🔬 方法详解

**问题定义**：本文旨在解决预训练视觉-语言-动作（VLA）模型在分布外场景中表现脆弱的问题，现有方法在面对复杂的语言条件任务时，往往无法有效探索搜索空间，导致性能下降。

**核心思路**：VLAPS框架的核心思路是将基于模型的搜索与VLA策略的推理过程相结合，通过利用VLA策略提供的动作先验，优化搜索过程，从而提高任务执行的成功率。

**技术框架**：VLAPS的整体架构包括三个主要模块：首先，使用VLA模型生成动作先验；其次，基于目标环境的模型进行蒙特卡洛树搜索（MCTS）；最后，将搜索结果整合到VLA策略的推理中，形成最终的动作决策。

**关键创新**：VLAPS的主要创新在于将基于模型的搜索与VLA策略的推理过程有效结合，利用VLA派生的先验信息来引导搜索，从而在复杂任务中实现更高效的探索。

**关键设计**：在实现过程中，VLAPS对MCTS算法进行了修改，以便更好地利用VLA策略的动作先验，同时在参数设置上进行了优化，以确保搜索过程的高效性和准确性。

## 📊 实验亮点

实验结果表明，VLAPS在语言指定任务上显著优于仅使用VLA的基线，成功率提高了67个百分点，展示了其在复杂任务中的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动化制造、服务机器人等。通过提升机器人在复杂语言条件下的任务执行能力，VLAPS能够在实际应用中显著提高机器人系统的安全性和可靠性，推动智能机器人技术的进一步发展。

## 📄 摘要（原文）

> Pre-trained vision-language-action (VLA) models offer a promising foundation for generalist robot policies, but often produce brittle behaviors or unsafe failures when deployed zero-shot in out-of-distribution scenarios. We present Vision-Language-Action Planning & Search (VLAPS) -- a novel framework and accompanying algorithms that embed model-based search into the inference procedure of pre-trained VLA policies to improve their performance on robotic tasks. Specifically, our method biases a modified Monte Carlo Tree Search (MCTS) algorithm -- run using a model of the target environment -- using action priors defined by the VLA policy. By using VLA-derived abstractions and priors in model-based search, VLAPS efficiently explores language-conditioned robotics tasks whose search spaces would otherwise be intractably large. Conversely, by integrating model-based search with the VLA policy's inference procedure, VLAPS yields behaviors that are more performant than those obtained by directly following the VLA policy's action predictions. VLAPS offers a principled framework to: i) control test-time compute in VLA models, ii) leverage a priori knowledge of the robotic environment, and iii) integrate established planning and reinforcement learning techniques into the VLA inference process. Across all experiments, VLAPS significantly outperforms VLA-only baselines on language-specified tasks that would otherwise be intractable for uninformed search algorithms, increasing success rates by as much as 67 percentage points.

