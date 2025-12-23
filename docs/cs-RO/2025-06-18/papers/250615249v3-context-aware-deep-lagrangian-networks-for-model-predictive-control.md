---
layout: default
title: Context-Aware Deep Lagrangian Networks for Model Predictive Control
---

# Context-Aware Deep Lagrangian Networks for Model Predictive Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15249" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15249v3</a>
  <a href="https://arxiv.org/pdf/2506.15249.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15249v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15249v3', 'Context-Aware Deep Lagrangian Networks for Model Predictive Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lucas Schulze, Jan Peters, Oleg Arenz

**分类**: cs.RO, cs.LG

**发布日期**: 2025-06-18 (更新: 2025-07-27)

**备注**: Accepted to the 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2025)

---

## 💡 一句话要点

**提出上下文感知深度拉格朗日网络以解决复杂环境中的控制问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `深度拉格朗日网络` `上下文感知` `模型预测控制` `在线系统识别` `机器人控制` `物理一致性` `轨迹跟踪`

## 📋 核心要点

1. 在复杂环境中，现有的控制方法难以处理大量潜在交互对象及其不确定的物理属性。
2. 本文提出了一种上下文感知的深度拉格朗日网络，结合递归网络进行在线系统识别，并与模型预测控制相结合。
3. 实验结果显示，所提方法在7自由度机器人手臂的轨迹跟踪中，末端执行器跟踪误差降低了39%。

## 📝 摘要（中文）

基于物理一致性动态模型（如深度拉格朗日网络）的机器人控制可以提高行为的可泛化性和可解释性。然而，在复杂环境中，潜在交互对象数量庞大且物理属性常常不确定，单一全局模型难以适用。因此，本文提出了一种上下文感知模型的在线系统识别方法，旨在捕捉当前环境的相关特征。我们将上下文感知的深度拉格朗日网络与递归网络结合，并与模型预测控制（MPC）集成，实现自适应的物理一致性控制。实验结果表明，该方法在7自由度机器人手臂的轨迹跟踪中，末端执行器跟踪误差降低了39%，相比之下，基于扩展卡尔曼滤波器的基线方法仅改善了21%。

## 🔬 方法详解

**问题定义**：本文旨在解决在复杂环境中，机器人控制面临的多对象交互及物理属性不确定性的问题。现有方法通常依赖单一全局模型，难以适应动态变化的环境。

**核心思路**：论文提出了一种上下文感知的深度拉格朗日网络（DeLaN），通过在线系统识别来捕捉当前环境的相关特征，并与模型预测控制（MPC）结合，实现自适应控制。

**技术框架**：整体架构包括上下文感知的深度拉格朗日网络、递归网络用于在线系统识别，以及模型预测控制模块。该框架能够动态调整控制策略以适应环境变化。

**关键创新**：最重要的创新在于将深度拉格朗日网络扩展为上下文感知模型，并结合递归网络进行实时系统识别，这使得控制策略能够在不同环境上下文中保持物理一致性。

**关键设计**：在模型设计中，采用了残差动态模型以利用已知的机器人名义模型，并在损失函数中引入物理一致性约束，以确保在不同上下文中模型的可用性和准确性。

## 📊 实验亮点

实验结果表明，所提出的方法在7自由度机器人手臂的轨迹跟踪任务中，末端执行器的跟踪误差降低了39%。相比之下，基于扩展卡尔曼滤波器的基线方法仅实现了21%的改善，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、自动驾驶、智能制造等，能够在动态和复杂环境中实现更高效的控制策略。通过提高控制的可适应性和物理一致性，未来可能推动机器人技术在更广泛场景中的应用，提升其智能化水平。

## 📄 摘要（原文）

> Controlling a robot based on physics-consistent dynamic models, such as Deep Lagrangian Networks (DeLaN), can improve the generalizability and interpretability of the resulting behavior. However, in complex environments, the number of objects to potentially interact with is vast, and their physical properties are often uncertain. This complexity makes it infeasible to employ a single global model. Therefore, we need to resort to online system identification of context-aware models that capture only the currently relevant aspects of the environment. While physical principles such as the conservation of energy may not hold across varying contexts, ensuring physical plausibility for any individual context-aware model can still be highly desirable, particularly when using it for receding horizon control methods such as model predictive control (MPC). Hence, in this work, we extend DeLaN to make it context-aware, combine it with a recurrent network for online system identification, and integrate it with an MPC for adaptive, physics-consistent control. We also combine DeLaN with a residual dynamics model to leverage the fact that a nominal model of the robot is typically available. We evaluate our method on a 7-DOF robot arm for trajectory tracking under varying loads. Our method reduces the end-effector tracking error by 39%, compared to a 21% improvement achieved by a baseline that uses an extended Kalman filter.

