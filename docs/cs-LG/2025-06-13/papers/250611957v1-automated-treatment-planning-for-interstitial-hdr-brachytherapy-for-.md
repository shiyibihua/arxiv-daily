---
layout: default
title: Automated Treatment Planning for Interstitial HDR Brachytherapy for Locally Advanced Cervical Cancer using Deep Reinforcement Learning
---

# Automated Treatment Planning for Interstitial HDR Brachytherapy for Locally Advanced Cervical Cancer using Deep Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11957" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11957v1</a>
  <a href="https://arxiv.org/pdf/2506.11957.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11957v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11957v1', 'Automated Treatment Planning for Interstitial HDR Brachytherapy for Locally Advanced Cervical Cancer using Deep Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammadamin Moradi, Runyu Jiang, Yingzi Liu, Malvern Madondo, Tianming Wu, James J. Sohn, Xiaofeng Yang, Yasmin Hasan, Zhen Tian

**分类**: physics.med-ph, cs.LG

**发布日期**: 2025-06-13

**备注**: 12 pages, 2 figures, 3 tables

---

## 💡 一句话要点

**提出基于深度强化学习的自动化HDR近距离放疗计划框架以解决宫颈癌治疗问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `HDR近距离放疗` `自动化治疗计划` `宫颈癌` `剂量优化` `临床应用` `放疗技术`

## 📋 核心要点

1. 现有HDR近距离放疗计划高度依赖手动经验，导致一致性和效率不足。
2. 本研究提出了一个基于深度强化学习的自动化HDR近距离放疗计划框架，能够自动选择治疗计划参数。
3. 实验结果显示，该方法在未见测试患者中平均得分为93.89%，超过临床计划的91.86%，且保持靶区覆盖完整。

## 📝 摘要（中文）

高剂量率（HDR）近距离放疗在局部晚期宫颈癌的治疗中发挥着关键作用，但仍然高度依赖手动治疗计划的专业知识。本研究的目标是开发一个完全自动化的HDR近距离放疗计划框架，集成强化学习（RL）和基于剂量的优化，以生成临床可接受的治疗计划，提高一致性和效率。我们提出了一个分层的两阶段自动规划框架。在第一阶段，基于深度Q网络（DQN）的RL代理迭代选择治疗计划参数（TPPs），控制靶区覆盖与危及器官（OAR）保护之间的权衡。第二阶段，定制的Adam优化器计算所选TPPs的相应停留时间分布。该框架在复杂应用几何的患者群体中进行了评估，成功学习了临床相关的TPP调整。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有HDR近距离放疗计划依赖手动经验的问题，导致治疗计划的一致性和效率不足。

**核心思路**：通过引入深度强化学习，自动选择治疗计划参数（TPPs），以优化靶区覆盖与危及器官保护之间的权衡，从而实现自动化治疗计划生成。

**技术框架**：整体框架分为两个阶段：第一阶段使用DQN代理迭代选择TPPs，第二阶段使用定制的Adam优化器计算停留时间分布。

**关键创新**：该框架通过结合强化学习与剂量优化，成功实现了治疗计划的自动化，显著提高了计划的一致性和效率。

**关键设计**：代理的状态表示包括剂量-体积直方图（DVH）指标和当前TPP值，奖励函数则结合了临床剂量目标和安全约束，确保了临床可接受性。优化器使用临床信息驱动的损失函数进行停留时间分布计算。

## 📊 实验亮点

实验结果表明，基于RL的自动化规划方法在未见测试患者中的平均得分为93.89%，显著高于传统临床计划的91.86%。此外，该方法在大多数情况下保持了靶区的完整覆盖，并减少了CTV热点，显示出其临床应用的潜力。

## 🎯 应用场景

该研究的自动化HDR近距离放疗计划框架具有广泛的应用潜力，能够在临床实践中提高治疗计划的效率和一致性，减轻放疗专家的工作负担，提升患者的治疗效果。未来，该方法可能扩展到其他类型的放疗或肿瘤治疗中，推动个性化医疗的发展。

## 📄 摘要（原文）

> High-dose-rate (HDR) brachytherapy plays a critical role in the treatment of locally advanced cervical cancer but remains highly dependent on manual treatment planning expertise. The objective of this study is to develop a fully automated HDR brachytherapy planning framework that integrates reinforcement learning (RL) and dose-based optimization to generate clinically acceptable treatment plans with improved consistency and efficiency. We propose a hierarchical two-stage autoplanning framework. In the first stage, a deep Q-network (DQN)-based RL agent iteratively selects treatment planning parameters (TPPs), which control the trade-offs between target coverage and organ-at-risk (OAR) sparing. The agent's state representation includes both dose-volume histogram (DVH) metrics and current TPP values, while its reward function incorporates clinical dose objectives and safety constraints, including D90, V150, V200 for targets, and D2cc for all relevant OARs (bladder, rectum, sigmoid, small bowel, and large bowel). In the second stage, a customized Adam-based optimizer computes the corresponding dwell time distribution for the selected TPPs using a clinically informed loss function. The framework was evaluated on a cohort of patients with complex applicator geometries. The proposed framework successfully learned clinically meaningful TPP adjustments across diverse patient anatomies. For the unseen test patients, the RL-based automated planning method achieved an average score of 93.89%, outperforming the clinical plans which averaged 91.86%. These findings are notable given that score improvements were achieved while maintaining full target coverage and reducing CTV hot spots in most cases.

