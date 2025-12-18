---
layout: default
title: A Game-Theoretic Predictive Control Framework with Statistical Collision Avoidance Constraints for Autonomous Vehicle Overtaking
---

# A Game-Theoretic Predictive Control Framework with Statistical Collision Avoidance Constraints for Autonomous Vehicle Overtaking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13545" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13545v1</a>
  <a href="https://arxiv.org/pdf/2509.13545.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13545v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13545v1', 'A Game-Theoretic Predictive Control Framework with Statistical Collision Avoidance Constraints for Autonomous Vehicle Overtaking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sheng Yu, Boli Chen, Imad M. Jaimoukha, Simos A. Evangelou

**分类**: eess.SY

**发布日期**: 2025-09-16

---

## 💡 一句话要点

**提出基于博弈论预测控制的自主超车框架，解决混合交通中统计碰撞避免问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `自主超车` `博弈论` `预测控制` `随机模型预测控制` `人机交互` `混合交通` `碰撞避免`

## 📋 核心要点

1. 现有自主超车方法难以应对混合交通中人工驾驶车辆的交互行为和不确定性。
2. GT-PRO策略通过博弈论预测控制，解耦纵向和横向动力学，并利用真实数据进行人类行为预测。
3. 仿真结果表明，GT-PRO在安全、效率和舒适性方面优于现有方法，并具备实时性。

## 📝 摘要（中文）

本文提出了一种用于混合交通环境中互联自动驾驶车辆(CAV)自主超车的控制框架，其中被超车辆为非互联但具有交互行为的人工驾驶车辆。该方法被称为博弈论预测超车(GT-PRO)策略，成功地解耦了CAV的纵向和横向车辆动力学，并通过创新的基于模型预测控制(MPC)的纵向和横向控制器全面协调这些解耦的动力学。为了解决人工驾驶被超车辆的实时交互行为，横向控制器求解一个基于动态Stackelberg博弈的双层优化问题，以直接控制CAV的横向运动并预测被超车辆的纵向响应，随后这些响应被共享给控制CAV纵向运动的随机MPC。该策略利用了一个全面的真实世界数据集，该数据集捕捉了人类驾驶员在被超车时的反应，以根据最常见的人类反应调整博弈论横向控制器，并对人类不确定性进行统计表征，从而为随机纵向控制器实施碰撞避免概率约束。被超车辆的礼貌和激进人类响应案例研究的仿真结果表明，与文献中现有的自主超车方法相比，所提出的GT-PRO可以为这种范围的人类驾驶员响应实现更安全、更高效和更舒适的自主超车。此外，结果表明GT-PRO方法能够实时实现。

## 🔬 方法详解

**问题定义**：论文旨在解决混合交通环境中，自主车辆安全高效地超车人工驾驶车辆的问题。现有方法通常难以准确预测人工驾驶车辆的行为，导致超车过程存在安全隐患，效率低下，舒适性差。特别是人工驾驶车辆的交互行为和不确定性给自主超车带来了挑战。

**核心思路**：论文的核心思路是将自主超车问题建模为一个动态Stackelberg博弈，其中自主车辆作为领导者，人工驾驶车辆作为跟随者。自主车辆通过预测人工驾驶车辆的响应来优化自身的超车策略。同时，利用真实世界数据集对人工驾驶车辆的行为进行建模，并采用随机模型预测控制来处理人工驾驶车辆的不确定性。

**技术框架**：GT-PRO框架包含以下主要模块：1) 横向控制器：基于动态Stackelberg博弈，预测人工驾驶车辆的纵向响应，并控制自主车辆的横向运动。2) 纵向控制器：基于随机模型预测控制，考虑人工驾驶车辆的不确定性，控制自主车辆的纵向运动。3) 数据驱动的人类行为建模：利用真实世界数据集，对人工驾驶车辆的行为进行建模，并用于横向控制器的博弈论优化和纵向控制器的概率约束设计。

**关键创新**：论文的关键创新在于：1) 将自主超车问题建模为动态Stackelberg博弈，能够有效地预测人工驾驶车辆的响应。2) 利用真实世界数据集对人工驾驶车辆的行为进行建模，提高了预测的准确性。3) 采用随机模型预测控制来处理人工驾驶车辆的不确定性，保证了超车过程的安全性。

**关键设计**：横向控制器采用双层优化结构，上层优化自主车辆的横向运动，下层预测人工驾驶车辆的纵向响应。纵向控制器采用概率约束，保证碰撞概率低于预设阈值。人类行为模型基于真实世界数据集进行训练，并用于调整博弈论横向控制器的参数。

## 📊 实验亮点

仿真结果表明，与现有方法相比，GT-PRO在安全、效率和舒适性方面均有显著提升。在礼貌和激进的人工驾驶车辆响应案例中，GT-PRO均能实现安全超车，且超车时间更短，横向加速度更小。具体而言，GT-PRO能够有效降低碰撞风险，并提高超车过程的平稳性，从而提升乘客的舒适度。

## 🎯 应用场景

该研究成果可应用于各种自动驾驶场景，尤其是在混合交通环境中，例如高速公路、城市道路等。通过提高自主超车的安全性、效率和舒适性，可以提升自动驾驶车辆的整体性能和用户体验，并加速自动驾驶技术的商业化落地。此外，该方法也可以推广到其他需要考虑人类交互行为的自主决策问题中。

## 📄 摘要（原文）

> This work develops a control framework for the autonomous overtaking of connected and automated vehicles (CAVs) in a mixed traffic environment, where the overtaken vehicle is an unconnected but interactive human-driven vehicle. The proposed method, termed the Game-Theoretic, PRedictive Overtaking (GT-PRO) strategy, successfully decouples the longitudinal and lateral vehicle dynamics of the CAV and comprehensively coordinates these decoupled dynamics via innovative longitudinal and lateral model predictive (MPC) based controllers, respectively. To address the real-time interactive behavior of the human-driven overtaken vehicle, a dynamic Stackelberg game-based bilevel optimization is solved by the lateral controller to directly control the CAV lateral motion and predict the overtaken vehicle longitudinal responses that are subsequently shared with a stochastic MPC that governs the CAV longitudinal motion. The proposed strategy exploits a comprehensive real-world dataset, which captures human driver responses when being overtaken, to tune the game-theoretic lateral controller according to the most common human responses, and to statistically characterize human uncertainties and hence implement a collision avoidance chance constraint for the stochastic longitudinal controller. The simulation results for both polite and aggressive human response case studies of the overtaken vehicle demonstrate that the proposed GT-PRO can achieve for this range of human driver responsiveness, safer, more efficient, and more comfortable autonomous overtaking, as compared to existing autonomous overtaking approaches in the literature. Furthermore, the results suggest that the GT-PRO method is capable of real-time implementation.

