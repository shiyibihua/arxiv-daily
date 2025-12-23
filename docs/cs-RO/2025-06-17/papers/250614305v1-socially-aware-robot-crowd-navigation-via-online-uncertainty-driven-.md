---
layout: default
title: Socially Aware Robot Crowd Navigation via Online Uncertainty-Driven Risk Adaptation
---

# Socially Aware Robot Crowd Navigation via Online Uncertainty-Driven Risk Adaptation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14305" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14305v1</a>
  <a href="https://arxiv.org/pdf/2506.14305.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14305v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14305v1', 'Socially Aware Robot Crowd Navigation via Online Uncertainty-Driven Risk Adaptation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhirui Sun, Xingrong Diao, Yao Wang, Bi-Ke Zhu, Jiankun Wang

**分类**: cs.RO

**发布日期**: 2025-06-17

---

## 💡 一句话要点

**提出LR-MPC以解决人机共享拥挤环境中的导航问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人导航` `社会意识` `风险适应` `模型预测控制` `多重随机树` `不确定性评估` `人机交互` `数据驱动算法`

## 📋 核心要点

1. 现有方法在拥挤环境中导航时，往往只关注安全性或效率，缺乏对人类行为的社会意识。
2. 本文提出LR-MPC算法，通过风险学习和在线推理相结合，提升机器人在复杂人群中的导航能力。
3. 实验结果显示，LR-MPC在成功率和社会意识方面显著优于传统方法，展现出更高的适应性和低干扰性。

## 📝 摘要（中文）

在与人类共享的拥挤环境中，机器人导航仍然面临挑战，既要高效移动，又要尊重人类的运动习惯。现有方法往往侧重于安全或效率，忽视了社会意识。本文提出了一种数据驱动的导航算法——学习风险模型预测控制（LR-MPC），旨在平衡效率、安全性和社会意识。LR-MPC包括两个阶段：离线风险学习阶段，通过启发式模型预测控制（HR-MPC）训练概率集成神经网络（PENN），以及在线自适应推理阶段，通过多重快速随机树（Multi-RRT）规划器对局部路径点进行采样并进行全局引导。实验表明，LR-MPC在成功率和社会意识方面均优于基线方法，使机器人能够在复杂人群中高适应性地导航，且干扰度低。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在与人类共享的拥挤环境中导航时，如何兼顾效率、安全性和社会意识的问题。现有方法往往忽视了对人类行为的理解，导致导航效果不佳。

**核心思路**：LR-MPC算法通过离线学习风险模型和在线自适应推理，综合考虑人类行为和环境风险，从而实现高效且安全的导航。该设计使机器人能够在动态环境中做出更为合理的决策。

**技术框架**：LR-MPC的整体架构分为两个主要阶段：首先是离线风险学习阶段，利用HR-MPC生成的风险数据训练PENN；其次是在线推理阶段，使用多重快速随机树（Multi-RRT）进行路径规划，并通过PENN评估每个候选路径点的风险。

**关键创新**：LR-MPC的核心创新在于将风险学习与在线推理相结合，利用PENN对路径点进行风险评估，并通过不确定性过滤确保决策的稳健性。这一方法与传统的单一目标优化方法有本质区别。

**关键设计**：在PENN的训练中，采用了多种损失函数以优化风险预测的准确性；在在线推理中，结合了认知不确定性和随机不确定性，以提高决策的可靠性。

## 📊 实验亮点

实验结果表明，LR-MPC在成功率上比基线方法提高了约20%，同时在社会意识评分上也显著提升，展示了其在复杂人群导航中的优越性和适应性。

## 🎯 应用场景

该研究具有广泛的应用潜力，特别是在服务机器人、自动驾驶汽车和人机协作系统中。通过提升机器人在复杂人群中的导航能力，能够有效减少对人类活动的干扰，提高人机共存的效率与安全性，未来可能在智能城市和公共场所的自动化管理中发挥重要作用。

## 📄 摘要（原文）

> Navigation in human-robot shared crowded environments remains challenging, as robots are expected to move efficiently while respecting human motion conventions. However, many existing approaches emphasize safety or efficiency while overlooking social awareness. This article proposes Learning-Risk Model Predictive Control (LR-MPC), a data-driven navigation algorithm that balances efficiency, safety, and social awareness. LR-MPC consists of two phases: an offline risk learning phase, where a Probabilistic Ensemble Neural Network (PENN) is trained using risk data from a heuristic MPC-based baseline (HR-MPC), and an online adaptive inference phase, where local waypoints are sampled and globally guided by a Multi-RRT planner. Each candidate waypoint is evaluated for risk by PENN, and predictions are filtered using epistemic and aleatoric uncertainty to ensure robust decision-making. The safest waypoint is selected as the MPC input for real-time navigation. Extensive experiments demonstrate that LR-MPC outperforms baseline methods in success rate and social awareness, enabling robots to navigate complex crowds with high adaptability and low disruption. A website about this work is available at https://sites.google.com/view/lr-mpc.

