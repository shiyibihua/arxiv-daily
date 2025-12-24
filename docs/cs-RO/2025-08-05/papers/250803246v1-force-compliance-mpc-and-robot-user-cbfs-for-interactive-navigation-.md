---
layout: default
title: Force-Compliance MPC and Robot-User CBFs for Interactive Navigation and User-Robot Safety in Hexapod Guide Robots
---

# Force-Compliance MPC and Robot-User CBFs for Interactive Navigation and User-Robot Safety in Hexapod Guide Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03246" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03246v1</a>
  <a href="https://arxiv.org/pdf/2508.03246.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03246v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03246v1', 'Force-Compliance MPC and Robot-User CBFs for Interactive Navigation and User-Robot Safety in Hexapod Guide Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zehua Fan, Feng Gao, Zhijun Chen, Yunpeng Yin, Limin Yang, Qingxing Xi, En Yang, Xuefeng Luo

**分类**: cs.RO

**发布日期**: 2025-08-05

---

## 💡 一句话要点

**提出力合规模型预测控制以解决盲人导航安全问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `力合规控制` `模型预测控制` `机器人安全` `视障导航` `动态障碍物` `人机交互` `卡尔曼滤波` `DBSCAN聚类`

## 📋 核心要点

1. 现有方法在复杂环境中缺乏有效的实时交互和安全保障，难以满足视障人士的导航需求。
2. 本文提出的FC-MPC通过动态模型和递归最小二乘法估计用户施加的力，实现双向交互，CBFs则确保安全性。
3. 实验结果显示，该系统在复杂环境中能够实时适应用户指令，确保用户和机器人安全，提升了导航的有效性。

## 📝 摘要（中文）

在复杂环境中引导视障人士需要实时双向交互和安全保障。本文提出了一种力合规模型预测控制（FC-MPC）和机器人-用户控制障碍函数（CBFs），用于六足引导机器人中的力合规导航和障碍物规避。FC-MPC通过估计用户施加的力和力矩，调整机器人的运动，而CBFs则确保用户和机器人的安全，处理静态和动态障碍物，并通过加权松弛变量克服复杂动态环境中的可行性问题。实验结果表明，该系统能够在复杂环境中适应用户的力命令，同时保证用户和机器人的安全。

## 🔬 方法详解

**问题定义**：本文旨在解决在复杂环境中引导视障人士时，现有方法缺乏实时交互和安全保障的问题。现有技术在处理动态障碍物时存在可行性不足的挑战。

**核心思路**：论文提出的FC-MPC通过估计用户施加的力和力矩，实时调整机器人运动，以实现双向交互。同时，CBFs用于处理障碍物，确保用户和机器人的安全。

**技术框架**：整体架构包括力合规模型预测控制模块、机器人-用户控制障碍函数模块和障碍物聚类模块。FC-MPC模块负责动态调整机器人运动，CBFs模块确保安全，障碍物聚类模块则通过DBSCAN方法优化计算复杂度。

**关键创新**：最重要的技术创新在于结合了力合规控制和控制障碍函数，能够在复杂动态环境中有效处理用户交互和安全问题，显著提高了导航的安全性和灵活性。

**关键设计**：在障碍物建模中使用最小包围椭圆（MBEs），并通过卡尔曼滤波预测其轨迹。采用加权松弛变量来解决复杂环境中的可行性问题，同时通过八向连接的DBSCAN方法将计算复杂度从O(n²)降低至O(n)。

## 📊 实验亮点

实验结果表明，系统在复杂环境中能够实时适应用户施加的力命令，成功处理多种静态和动态障碍物，确保用户和机器人安全。相较于传统方法，系统在导航效率和安全性上均有显著提升，表现出更高的适应性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括视障人士的导航辅助系统、智能机器人导览服务以及其他需要人机交互的复杂环境。其实际价值在于提升了视障人士的出行安全性和自主性，未来可能推动相关技术在公共服务和智能家居等领域的广泛应用。

## 📄 摘要（原文）

> Guiding the visually impaired in complex environments requires real-time two-way interaction and safety assurance. We propose a Force-Compliance Model Predictive Control (FC-MPC) and Robot-User Control Barrier Functions (CBFs) for force-compliant navigation and obstacle avoidance in Hexapod guide robots. FC-MPC enables two-way interaction by estimating user-applied forces and moments using the robot's dynamic model and the recursive least squares (RLS) method, and then adjusting the robot's movements accordingly, while Robot-User CBFs ensure the safety of both the user and the robot by handling static and dynamic obstacles, and employ weighted slack variables to overcome feasibility issues in complex dynamic environments. We also adopt an Eight-Way Connected DBSCAN method for obstacle clustering, reducing computational complexity from O(n2) to approximately O(n), enabling real-time local perception on resource-limited on-board robot computers. Obstacles are modeled using Minimum Bounding Ellipses (MBEs), and their trajectories are predicted through Kalman filtering. Implemented on the HexGuide robot, the system seamlessly integrates force compliance, autonomous navigation, and obstacle avoidance. Experimental results demonstrate the system's ability to adapt to user force commands while guaranteeing user and robot safety simultaneously during navigation in complex environments.

