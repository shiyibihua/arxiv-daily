---
layout: default
title: Emergent time-keeping mechanisms in a deep reinforcement learning agent performing an interval timing task
---

# Emergent time-keeping mechanisms in a deep reinforcement learning agent performing an interval timing task

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15784" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15784v2</a>
  <a href="https://arxiv.org/pdf/2508.15784.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15784v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15784v2', 'Emergent time-keeping mechanisms in a deep reinforcement learning agent performing an interval timing task')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Amrapali Pednekar, Alvaro Garrido, Pieter Simoens, Yara Khaluf

**分类**: q-bio.NC, cs.LG

**发布日期**: 2025-08-06 (更新: 2025-08-26)

**备注**: Accepted at 2025 Artificial Life Conference

---

## 💡 一句话要点

**提出深度强化学习代理的时间保持机制以解决时间处理问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `时间处理` `生物系统` `神经激活` `间隔计时` `振荡神经元` `生物学模型`

## 📋 核心要点

1. 现有的时间处理机制缺乏统一的理解，尤其是在生物系统与深度神经网络之间的比较上存在挑战。
2. 本研究提出通过深度强化学习代理进行间隔计时任务，探索其内部振荡神经激活与生物系统的相似性。
3. 实验结果表明，代理在不同视频序列上保持了良好的任务表现，显示出其时间保持机制的内化能力。

## 📝 摘要（中文）

本研究通过深度强化学习代理在间隔计时任务中的表现，探讨了时间处理的机制。代理成功训练完成持续时间生产任务，分析其内部状态显示出生物系统中普遍存在的振荡神经激活模式。代理的行为主要受高幅度和频率的振荡神经元影响，这与生物学中的纹状体节拍频率模型相似。代理在不同视频序列上保持了其振荡表示和任务表现，表明其时间保持机制的内化，且对环境的依赖性较小。研究旨在利用深度神经网络理解生物系统，特别是时间处理方面的机制。

## 🔬 方法详解

**问题定义**：本研究旨在解决深度强化学习代理在时间处理任务中的表现机制，现有方法未能充分揭示其内部时间保持机制的生物学对应关系。

**核心思路**：通过训练深度强化学习代理执行持续时间生产任务，分析其内部状态和神经激活模式，以探索其时间处理的生物学机制。

**技术框架**：整体架构包括代理的训练阶段、内部状态分析阶段和行为表现评估阶段。代理在观看视频序列时标记目标间隔，分析其神经元的振荡活动。

**关键创新**：本研究的创新点在于揭示了深度强化学习代理的时间保持机制与生物学模型（如纹状体节拍频率模型）的相似性，提供了新的理解框架。

**关键设计**：代理的训练过程中，采用了特定的损失函数以优化其时间标记能力，并关注高幅度和频率的振荡神经元，确保其在不同环境下的表现一致性。

## 📊 实验亮点

实验结果显示，代理在不同视频序列上均能保持良好的任务表现，振荡神经元的激活模式与目标间隔高度相关，表明其时间保持机制的内化能力。代理在任务执行中的环境依赖性显著降低，展示了其在时间处理方面的稳定性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、智能监控系统和生物节律研究等。通过理解深度学习模型的时间处理机制，可以为生物系统的模拟和优化提供新的思路，推动相关领域的技术进步。

## 📄 摘要（原文）

> Drawing parallels between Deep Artificial Neural Networks (DNNs) and biological systems can aid in understanding complex biological mechanisms that are difficult to disentangle. Temporal processing, an extensively researched topic, is one such example that lacks a coherent understanding of its underlying mechanisms. In this study, we investigate temporal processing in a Deep Reinforcement Learning (DRL) agent performing an interval timing task and explore potential biological counterparts to its emergent behavior. The agent was successfully trained to perform a duration production task, which involved marking successive occurrences of a target interval while viewing a video sequence. Analysis of the agent's internal states revealed oscillatory neural activations, a ubiquitous pattern in biological systems. Interestingly, the agent's actions were predominantly influenced by neurons exhibiting these oscillations with high amplitudes and frequencies corresponding to the target interval. Parallels are drawn between the agent's time-keeping strategy and the Striatal Beat Frequency (SBF) model, a biologically plausible model of interval timing. Furthermore, the agent maintained its oscillatory representations and task performance when tested on different video sequences (including a blank video). Thus, once learned, the agent internalized its time-keeping mechanism and showed minimal reliance on its environment to perform the timing task. A hypothesis about the resemblance between this emergent behavior and certain aspects of the evolution of biological processes like circadian rhythms, has been discussed. This study aims to contribute to recent research efforts of utilizing DNNs to understand biological systems, with a particular emphasis on temporal processing.

