---
layout: default
title: Integration of Robot and Scene Kinematics for Sequential Mobile Manipulation Planning
---

# Integration of Robot and Scene Kinematics for Sequential Mobile Manipulation Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18627" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18627v1</a>
  <a href="https://arxiv.org/pdf/2508.18627.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18627v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18627v1', 'Integration of Robot and Scene Kinematics for Sequential Mobile Manipulation Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyuan Jiao, Yida Niu, Zeyu Zhang, Yangyang Wu, Yao Su, Yixin Zhu, Hangxin Liu, Song-Chun Zhu

**分类**: cs.RO

**发布日期**: 2025-08-26

**备注**: 20 pages, 13 figures; accepted by Transactions on Robotics

---

## 💡 一句话要点

**提出顺序移动操控规划框架以解决长时间多步操控问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `移动操控` `运动学模型` `增强配置空间` `任务规划` `运动规划` `机器人系统` `复杂操控` `长时间任务`

## 📋 核心要点

1. 现有的移动操控方法在处理长时间多步任务时，往往无法有效协调机器人与环境的交互，导致成功率低。
2. 论文提出的顺序移动操控规划框架通过构建增强配置空间，将环境运动学与机器人运动学整合，优化了任务规划和运动规划的过程。
3. 实验结果显示，使用增强配置空间进行规划的成功率比传统基线方法提高了84.6%，并在真实场景中验证了其有效性。

## 📝 摘要（中文）

我们提出了一种顺序移动操控规划（SMMP）框架，能够解决长时间多步的移动操控任务，尤其是在与关节物体交互时。通过将环境结构抽象为运动学模型，并与机器人的运动学相结合，我们构建了一个增强配置空间（A-Space），统一了导航和操控的任务约束，同时考虑了机器人底座、手臂和被操控物体的关节可达性。该框架在三层次结构中高效规划：任务规划器生成符号动作序列以建模A-Space的演变，基于优化的运动规划器在A-Space内计算连续轨迹以实现机器人和场景元素的期望配置，最后的计划细化阶段选择确保长时间可行性的动作目标。我们的仿真研究表明，A-Space的规划成功率比基线方法提高了84.6%。在真实机器人系统上的验证展示了流畅的移动操控，涉及七种刚性和关节物体，在17种不同的上下文中，且长时间任务可达14个顺序步骤。我们的结果强调了将场景运动学建模为规划实体的重要性，而非编码特定任务的约束，提供了一种可扩展和通用的复杂机器人操控方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决长时间多步移动操控任务中的规划效率和成功率问题。现有方法在处理复杂环境和关节物体时，往往无法有效协调机器人与环境的交互，导致任务成功率低下。

**核心思路**：论文的核心思路是通过将环境结构抽象为运动学模型，并与机器人的运动学相结合，构建一个增强配置空间（A-Space），以统一导航和操控的任务约束，从而提高规划的效率和成功率。

**技术框架**：整体架构分为三个主要模块：任务规划器生成符号动作序列以建模A-Space的演变；优化基础的运动规划器在A-Space内计算连续轨迹；计划细化阶段选择确保长时间可行性的动作目标。

**关键创新**：最重要的技术创新点在于将场景运动学建模为规划实体，而非简单编码特定任务的约束。这种方法使得规划过程更加灵活和可扩展，能够适应复杂的操控任务。

**关键设计**：在设计中，关键参数包括A-Space的构建方式、任务规划器和运动规划器的优化算法，以及确保长时间可行性的动作目标选择策略等。

## 📊 实验亮点

实验结果表明，使用增强配置空间进行规划的成功率比基线方法提高了84.6%。在真实机器人系统中，验证了其在处理七种刚性和关节物体的流畅移动操控能力，且能够完成长达14个步骤的复杂任务。

## 🎯 应用场景

该研究的潜在应用场景包括服务机器人、工业自动化和智能家居等领域，能够有效提升机器人在复杂环境中的操控能力。未来，该框架有望推广到更多类型的机器人任务中，增强其适应性和智能化水平。

## 📄 摘要（原文）

> We present a Sequential Mobile Manipulation Planning (SMMP) framework that can solve long-horizon multi-step mobile manipulation tasks with coordinated whole-body motion, even when interacting with articulated objects. By abstracting environmental structures as kinematic models and integrating them with the robot's kinematics, we construct an Augmented Configuration Apace (A-Space) that unifies the previously separate task constraints for navigation and manipulation, while accounting for the joint reachability of the robot base, arm, and manipulated objects. This integration facilitates efficient planning within a tri-level framework: a task planner generates symbolic action sequences to model the evolution of A-Space, an optimization-based motion planner computes continuous trajectories within A-Space to achieve desired configurations for both the robot and scene elements, and an intermediate plan refinement stage selects action goals that ensure long-horizon feasibility. Our simulation studies first confirm that planning in A-Space achieves an 84.6\% higher task success rate compared to baseline methods. Validation on real robotic systems demonstrates fluid mobile manipulation involving (i) seven types of rigid and articulated objects across 17 distinct contexts, and (ii) long-horizon tasks of up to 14 sequential steps. Our results highlight the significance of modeling scene kinematics into planning entities, rather than encoding task-specific constraints, offering a scalable and generalizable approach to complex robotic manipulation.

