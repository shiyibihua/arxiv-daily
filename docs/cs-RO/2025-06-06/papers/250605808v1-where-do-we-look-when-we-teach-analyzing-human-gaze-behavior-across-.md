---
layout: default
title: Where Do We Look When We Teach? Analyzing Human Gaze Behavior Across Demonstration Devices in Robot Imitation Learning
---

# Where Do We Look When We Teach? Analyzing Human Gaze Behavior Across Demonstration Devices in Robot Imitation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05808" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05808v1</a>
  <a href="https://arxiv.org/pdf/2506.05808.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05808v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05808v1', 'Where Do We Look When We Teach? Analyzing Human Gaze Behavior Across Demonstration Devices in Robot Imitation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yutaro Ishida, Takamitsu Matsubara, Takayuki Kanai, Kazuhiro Shintani, Hiroshi Bito

**分类**: cs.RO

**发布日期**: 2025-06-06

---

## 💡 一句话要点

**提出实验框架分析教学中人类注视行为以提升模仿学习效果**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `模仿学习` `人类注视行为` `机器人学习` `示范设备` `任务成功率` `数据收集` `认知技能`

## 📋 核心要点

1. 现有的模仿学习方法依赖大量示范数据，导致成本高且效率低下。
2. 本文提出一个实验框架，系统分析不同示范设备下的示范者注视行为，以提取任务相关线索。
3. 实验结果显示，使用自然行为捕捉设备的数据显著提高了任务成功率，提升幅度达到50%。

## 📝 摘要（中文）

模仿学习在获取可泛化策略时通常需要大量示范数据，成本高昂。为解决这一挑战，本文提出通过分析人类示范者的注视行为来提取任务相关线索。研究表明，模拟机器人体现或视觉条件的设备会削弱示范者提取任务线索的能力，且这种削弱程度与模拟的程度有关。此外，使用捕捉自然人类行为的设备收集的注视数据，能将策略的任务成功率从18.8%提升至68.8%。

## 🔬 方法详解

**问题定义**：本文旨在解决模仿学习中示范数据收集的高成本问题，现有方法在提取任务相关线索时面临设备影响注视行为的挑战。

**核心思路**：通过设计实验框架，系统分析不同示范设备对示范者注视行为的影响，从而优化数据收集过程。

**技术框架**：研究包括多个阶段：首先，选择不同的示范设备；其次，记录示范者的注视行为；最后，分析注视数据与任务成功率之间的关系。

**关键创新**：本研究的创新在于系统性地探讨了设备模拟对人类注视行为的影响，揭示了设备设计与学习效果之间的关联。

**关键设计**：实验中采用了多种设备，设置了不同的视觉条件，并使用统计分析方法评估注视行为与任务成功率的关系。具体的参数设置和损失函数设计未在摘要中详细说明，需参考完整论文。

## 📊 实验亮点

实验结果显示，使用自然行为捕捉设备收集的注视数据，任务成功率从18.8%显著提升至68.8%，表明设备设计对模仿学习的影响显著。

## 🎯 应用场景

该研究的潜在应用领域包括机器人学习、教育技术和人机交互等。通过优化示范数据的收集方式，可以在多种场景中提升机器学习的效率和效果，推动智能系统的实际应用。

## 📄 摘要（原文）

> Imitation learning for acquiring generalizable policies often requires a large volume of demonstration data, making the process significantly costly. One promising strategy to address this challenge is to leverage the cognitive and decision-making skills of human demonstrators with strong generalization capability, particularly by extracting task-relevant cues from their gaze behavior. However, imitation learning typically involves humans collecting data using demonstration devices that emulate a robot's embodiment and visual condition. This raises the question of how such devices influence gaze behavior. We propose an experimental framework that systematically analyzes demonstrators' gaze behavior across a spectrum of demonstration devices. Our experimental results indicate that devices emulating (1) a robot's embodiment or (2) visual condition impair demonstrators' capability to extract task-relevant cues via gaze behavior, with the extent of impairment depending on the degree of emulation. Additionally, gaze data collected using devices that capture natural human behavior improves the policy's task success rate from 18.8% to 68.8% under environmental shifts.

