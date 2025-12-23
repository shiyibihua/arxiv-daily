---
layout: default
title: Scaffolding Dexterous Manipulation with Vision-Language Models
---

# Scaffolding Dexterous Manipulation with Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19212" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19212v2</a>
  <a href="https://arxiv.org/pdf/2506.19212.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19212v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19212v2', 'Scaffolding Dexterous Manipulation with Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vincent de Bakker, Joey Hejna, Tyler Ga Wei Lum, Onur Celik, Aleksandar Taranovic, Denis Blessing, Gerhard Neumann, Jeannette Bohg, Dorsa Sadigh

**分类**: cs.RO

**发布日期**: 2025-06-24 (更新: 2025-11-16)

---

## 💡 一句话要点

**提出视觉语言模型辅助灵巧操控以解决训练难题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `灵巧操控` `视觉语言模型` `强化学习` `机器人手` `任务指导`

## 📋 核心要点

1. 现有灵巧操控方法面临演示收集困难和高维控制挑战，限制了训练效果。
2. 本文提出利用视觉语言模型自动识别关键点并合成3D轨迹，简化了任务指导过程。
3. 实验结果表明，该方法在多种模拟任务中学习到的操控策略具有良好的鲁棒性，并成功转移到真实环境。

## 📝 摘要（中文）

灵巧机器人手在执行复杂操作任务中至关重要，但由于演示收集和高维控制的挑战，训练仍然困难。尽管强化学习（RL）可以通过模拟生成经验来缓解数据瓶颈，但通常依赖于精心设计的任务特定奖励函数，限制了可扩展性和泛化能力。本文提出了一种新方法，利用现代视觉语言模型（VLM）编码的常识空间和语义知识，结合任务描述和视觉场景，识别任务相关的关键点，并合成手部和物体运动的3D轨迹。通过在模拟中训练低级残差RL策略以高保真度跟踪这些粗略轨迹，实验表明该方法能够学习到稳健的灵巧操控策略，并且能够在没有人类演示或手工奖励的情况下转移到真实机器人手上。

## 🔬 方法详解

**问题定义**：本文旨在解决灵巧机器人手的训练难题，现有方法依赖于精心设计的任务特定奖励函数，导致可扩展性和泛化能力不足。

**核心思路**：通过利用现代视觉语言模型（VLM）编码的空间和语义知识，结合任务描述和视觉场景，自动识别关键点并合成3D轨迹，从而指导强化学习策略的训练。

**技术框架**：整体方法包括两个主要阶段：首先，使用VLM识别任务相关的关键点；其次，合成手部和物体运动的3D轨迹，并在模拟中训练低级残差RL策略以跟踪这些轨迹。

**关键创新**：该方法的创新在于将视觉语言模型与强化学习相结合，利用VLM的常识知识替代传统的参考轨迹，显著简化了任务指导过程。

**关键设计**：在设计中，使用了标准的VLM进行关键点识别，轨迹合成采用了基于任务描述的生成策略，RL策略则通过低级残差学习进行优化，确保高保真度的轨迹跟踪。

## 📊 实验亮点

实验结果显示，该方法在多种模拟任务中成功学习到稳健的灵巧操控策略，相较于传统方法，性能提升显著，能够在没有人类演示或手工奖励的情况下，直接转移到真实机器人手上，展示了良好的适应性和鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、工业自动化和人机协作等场景。通过提高灵巧机器人手的操作能力，能够在复杂环境中执行多种任务，提升自动化水平，降低人力成本，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Dexterous robotic hands are essential for performing complex manipulation tasks, yet remain difficult to train due to the challenges of demonstration collection and high-dimensional control. While reinforcement learning (RL) can alleviate the data bottleneck by generating experience in simulation, it typically relies on carefully designed, task-specific reward functions, which hinder scalability and generalization. Thus, contemporary works in dexterous manipulation have often bootstrapped from reference trajectories. These trajectories specify target hand poses that guide the exploration of RL policies and object poses that enable dense, task-agnostic rewards. However, sourcing suitable trajectories - particularly for dexterous hands - remains a significant challenge. Yet, the precise details in explicit reference trajectories are often unnecessary, as RL ultimately refines the motion. Our key insight is that modern vision-language models (VLMs) already encode the commonsense spatial and semantic knowledge needed to specify tasks and guide exploration effectively. Given a task description (e.g., "open the cabinet") and a visual scene, our method uses an off-the-shelf VLM to first identify task-relevant keypoints (e.g., handles, buttons) and then synthesize 3D trajectories for hand motion and object motion. Subsequently, we train a low-level residual RL policy in simulation to track these coarse trajectories or "scaffolds" with high fidelity. Across a number of simulated tasks involving articulated objects and semantic understanding, we demonstrate that our method is able to learn robust dexterous manipulation policies. Moreover, we showcase that our method transfers to real-world robotic hands without any human demonstrations or handcrafted rewards.

