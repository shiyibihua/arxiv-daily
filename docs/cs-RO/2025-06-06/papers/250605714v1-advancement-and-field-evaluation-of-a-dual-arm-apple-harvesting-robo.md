---
layout: default
title: Advancement and Field Evaluation of a Dual-arm Apple Harvesting Robot
---

# Advancement and Field Evaluation of a Dual-arm Apple Harvesting Robot

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05714" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05714v1</a>
  <a href="https://arxiv.org/pdf/2506.05714.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05714v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05714v1', 'Advancement and Field Evaluation of a Dual-arm Apple Harvesting Robot')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Keyi Zhu, Kyle Lammers, Kaixiang Zhang, Chaaran Arunachalam, Siddhartha Bhattacharya, Jiajia Li, Renfu Lu, Zhaojian Li

**分类**: cs.RO

**发布日期**: 2025-06-06

---

## 💡 一句话要点

**提出双臂苹果采摘机器人以解决人工采摘效率低下问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `苹果采摘` `双臂机器人` `自动化农业` `真空系统` `机器学习` `传感器反馈` `果园机器人`

## 📋 核心要点

1. 现有苹果采摘方法依赖人工，效率低且存在安全隐患，难以满足现代农业需求。
2. 本文提出的双臂采摘机器人通过集成真空系统和动态吸力分配，提高了苹果采摘的效率和可靠性。
3. 实验结果显示，该系统在不同果园环境中成功率高达0.807，采摘时间较单臂机器人减少28%。

## 📝 摘要（中文）

苹果是全球消费最广泛的水果之一。目前，苹果采摘完全依赖人工，成本高、劳动强度大且对工人存在安全隐患。因此，机器人采摘引起了越来越多的关注。然而，现有系统在复杂果园环境中的性能、有效性和可靠性仍然不足。本文提出了一种双臂采摘机器人，集成了ToF相机、两个4自由度的机械臂、集中真空系统和后处理模块。在采摘过程中，真空系统动态分配吸力到任一机械臂，实现高效的苹果脱离，同时降低能耗和噪音。与之前的设计相比，本文引入了平台运动机制，增强了机器人的灵活性和适应性。通过在系统中集成压力传感器，并引入新颖的双臂协调策略，进一步提高了采摘效率。该系统在美国密歇根州的两个商业果园进行了现场演示，成功率达到0.807和0.797，平均采摘周期为5.97秒。与单臂基线相比，采摘时间减少了28%。

## 🔬 方法详解

**问题定义**：本文旨在解决苹果采摘过程中人工效率低下和安全隐患的问题。现有的采摘机器人在复杂果园环境中的性能和可靠性不足，无法有效替代人工。

**核心思路**：提出一种双臂采摘机器人，通过集成真空系统和动态吸力分配机制，提升苹果的采摘效率和灵活性，适应不同的果园结构。

**技术框架**：系统主要由ToF相机、两个4自由度机械臂、集中真空系统和后处理模块组成。采摘过程中，真空系统根据需要动态调整吸力，确保高效采摘。

**关键创新**：引入了双臂协调策略和压力传感器反馈机制，使机器人能够实时响应采摘失败情况，显著提高了采摘效率。

**关键设计**：系统设计中，机械臂的自由度设置为4，真空系统的吸力动态分配，压力传感器用于监测采摘状态，确保机器人在不同环境下的适应性和稳定性。

## 📊 实验亮点

实验结果表明，双臂采摘机器人在两个不同果园的成功率分别为0.807和0.797，平均采摘周期为5.97秒。与单臂基线相比，采摘时间减少了28%，显示出显著的效率提升。

## 🎯 应用场景

该研究的双臂苹果采摘机器人具有广泛的应用潜力，能够在果园中实现高效、自动化的苹果采摘，降低人工成本，提高采摘效率。随着技术的进一步发展，该系统有望在苹果产业中实现商业化应用，推动农业自动化进程。

## 📄 摘要（原文）

> Apples are among the most widely consumed fruits worldwide. Currently, apple harvesting fully relies on manual labor, which is costly, drudging, and hazardous to workers. Hence, robotic harvesting has attracted increasing attention in recent years. However, existing systems still fall short in terms of performance, effectiveness, and reliability for complex orchard environments. In this work, we present the development and evaluation of a dual-arm harvesting robot. The system integrates a ToF camera, two 4DOF robotic arms, a centralized vacuum system, and a post-harvest handling module. During harvesting, suction force is dynamically assigned to either arm via the vacuum system, enabling efficient apple detachment while reducing power consumption and noise. Compared to our previous design, we incorporated a platform movement mechanism that enables both in-out and up-down adjustments, enhancing the robot's dexterity and adaptability to varying canopy structures. On the algorithmic side, we developed a robust apple localization pipeline that combines a foundation-model-based detector, segmentation, and clustering-based depth estimation, which improves performance in orchards. Additionally, pressure sensors were integrated into the system, and a novel dual-arm coordination strategy was introduced to respond to harvest failures based on sensor feedback, further improving picking efficiency. Field demos were conducted in two commercial orchards in MI, USA, with different canopy structures. The system achieved success rates of 0.807 and 0.797, with an average picking cycle time of 5.97s. The proposed strategy reduced harvest time by 28% compared to a single-arm baseline. The dual-arm harvesting robot enhances the reliability and efficiency of apple picking. With further advancements, the system holds strong potential for autonomous operation and commercialization for the apple industry.

