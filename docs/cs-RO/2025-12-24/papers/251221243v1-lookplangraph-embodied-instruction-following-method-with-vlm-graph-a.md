---
layout: default
title: "LookPlanGraph: Embodied Instruction Following Method with VLM Graph Augmentation"
---

# LookPlanGraph: Embodied Instruction Following Method with VLM Graph Augmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21243" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21243v1</a>
  <a href="https://arxiv.org/pdf/2512.21243.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21243v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21243v1', 'LookPlanGraph: Embodied Instruction Following Method with VLM Graph Augmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anatoly O. Onishchenko, Alexey K. Kovalev, Aleksandr I. Panov

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**提出LookPlanGraph，通过VLM图增强实现具身指令跟随任务**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能` `指令跟随` `视觉语言模型` `场景图` `动态环境`

## 📋 核心要点

1. 现有具身指令跟随方法依赖预构建的静态场景图，无法应对任务执行期间环境变化带来的挑战。
2. LookPlanGraph通过VLM持续更新场景图，利用智能体的视觉信息动态调整环境认知，提升任务完成的鲁棒性。
3. 实验表明，LookPlanGraph在模拟和真实环境中均优于静态场景图方法，证明了其有效性和实用性。

## 📝 摘要（中文）

本文提出LookPlanGraph，一种利用视觉语言模型（VLM）增强图结构的具身指令跟随方法。该方法使用包含静态资产和对象先验的场景图。在规划执行期间，LookPlanGraph通过验证现有先验或发现新实体，利用智能体的自我中心相机视图，持续更新图结构。实验结果表明，在VirtualHome和OmniGibson模拟环境中，LookPlanGraph优于基于预定义静态场景图的方法。同时，在真实世界环境中验证了该方法的实际应用性。此外，本文还引入了GraSIF数据集，包含来自SayPlan Office、BEHAVIOR-1K和VirtualHome RobotHow的514个任务，并带有自动化验证框架。

## 🔬 方法详解

**问题定义**：现有基于LLM的具身指令跟随方法依赖预先构建的静态场景图，然而真实环境中物体位置可能发生变化，导致静态场景图与实际环境不符，影响任务完成。现有方法无法有效处理这种环境变化带来的不确定性。

**核心思路**：LookPlanGraph的核心思路是在任务执行过程中，利用视觉语言模型（VLM）持续更新场景图。通过智能体的自我中心视角，VLM可以识别新的物体或验证已知的物体先验，从而动态调整场景图，使其与当前环境保持一致。

**技术框架**：LookPlanGraph的整体框架包含以下几个主要阶段：1) 初始化：使用静态资产和对象先验构建初始场景图。2) 规划：利用LLM基于当前场景图生成任务执行计划。3) 执行：智能体按照计划执行动作。4) 观察与更新：在执行过程中，智能体通过自我中心相机获取视觉信息，利用VLM识别物体并更新场景图。5) 循环：重复执行步骤3和4，直到任务完成。

**关键创新**：LookPlanGraph的关键创新在于动态场景图的构建和更新机制。与静态场景图方法不同，LookPlanGraph能够根据智能体的视觉输入，实时调整场景图，从而更好地适应环境变化。这种动态更新机制使得智能体能够更准确地理解环境，并做出更合理的决策。

**关键设计**：VLM的选择和使用是关键设计之一。论文中使用了特定的VLM模型（具体模型名称未知），并设计了相应的提示工程（prompt engineering）方法，以提高物体识别的准确性和效率。此外，场景图的更新策略也至关重要，需要平衡更新频率和计算成本。具体的参数设置、损失函数和网络结构等技术细节在论文中可能有所描述，但摘要中未明确提及。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21243v1/images/problem.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21243v1/images/overview.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21243v1/images/prompts.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，LookPlanGraph在VirtualHome和OmniGibson模拟环境中均优于基于静态场景图的方法。此外，在真实世界环境中的实验也验证了该方法的实用性。GraSIF数据集的发布为具身指令跟随领域提供了新的benchmark，并带有自动化验证框架，方便研究者进行算法评估。

## 🎯 应用场景

LookPlanGraph可应用于各种需要智能体与动态环境交互的场景，例如家庭服务机器人、仓库拣选机器人、自动驾驶等。该方法能够提高机器人在复杂、变化环境中的适应性和鲁棒性，使其能够更好地完成各种任务。未来，该方法有望推动具身智能的进一步发展。

## 📄 摘要（原文）

> Methods that use Large Language Models (LLM) as planners for embodied instruction following tasks have become widespread. To successfully complete tasks, the LLM must be grounded in the environment in which the robot operates. One solution is to use a scene graph that contains all the necessary information. Modern methods rely on prebuilt scene graphs and assume that all task-relevant information is available at the start of planning. However, these approaches do not account for changes in the environment that may occur between the graph construction and the task execution. We propose LookPlanGraph - a method that leverages a scene graph composed of static assets and object priors. During plan execution, LookPlanGraph continuously updates the graph with relevant objects, either by verifying existing priors or discovering new entities. This is achieved by processing the agents egocentric camera view using a Vision Language Model. We conducted experiments with changed object positions VirtualHome and OmniGibson simulated environments, demonstrating that LookPlanGraph outperforms methods based on predefined static scene graphs. To demonstrate the practical applicability of our approach, we also conducted experiments in a real-world setting. Additionally, we introduce the GraSIF (Graph Scenes for Instruction Following) dataset with automated validation framework, comprising 514 tasks drawn from SayPlan Office, BEHAVIOR-1K, and VirtualHome RobotHow. Project page available at https://lookplangraph.github.io .

