---
layout: default
title: Multi-Agent Coordination in Autonomous Vehicle Routing: A Simulation-Based Study of Communication, Memory, and Routing Loops
---

# Multi-Agent Coordination in Autonomous Vehicle Routing: A Simulation-Based Study of Communication, Memory, and Routing Loops

**arXiv**: [2511.17656v1](https://arxiv.org/abs/2511.17656) | [PDF](https://arxiv.org/pdf/2511.17656.pdf)

**作者**: KM Khalid Saifullah, Daniel Palmer

**分类**: cs.MA, cs.LG, cs.RO

**发布日期**: 2025-11-20

---

## 💡 一句话要点

**提出对象记忆管理机制以解决自主车辆路由中的循环问题**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `自主车辆` `多智能体系统` `路径规划` `障碍物记忆` `分布式系统` `Dijkstra算法` `性能优化`

## 📋 核心要点

1. 现有的无记忆重路由方法在动态环境中容易导致车辆陷入低效的路径循环，严重影响整体性能。
2. 本文提出对象记忆管理（OMM）机制，使智能体能够共享和保留障碍物信息，从而避免重复的路径计算。
3. 实验结果表明，OMM显著降低了平均旅行时间75.7%和等待时间88%，并减少了每辆车的重计算次数。

## 📝 摘要（中文）

多智能体协调对于下一代自主车辆系统至关重要，但基于通信的简单重路由实现可能导致性能显著下降。本研究探讨了去中心化多智能体导航中的一个基本问题：路由循环，即没有持久障碍记忆的车辆陷入低效路径重算的循环中。通过72种独特配置的系统仿真实验，我们证明了无记忆反应式重路由相比基线条件平均旅行时间增加了682%。为了解决这一问题，我们提出了对象记忆管理（OMM），一种轻量级机制，使智能体能够保留和共享先前遇到的障碍知识。OMM通过维护一个分布式的阻塞节点黑名单来运作，显著减少了平均旅行时间和等待时间。我们的研究为动态环境中稳健的多智能体协调提供了实证依据，结果对机器人、网络路由和分布式人工智能的设计具有重要启示。

## 🔬 方法详解

**问题定义**：本研究旨在解决自主车辆路由中的循环问题，现有的无记忆重路由方法导致车辆在动态环境中频繁陷入低效路径重算的循环中，影响整体效率。

**核心思路**：提出对象记忆管理（OMM）机制，允许智能体保留和共享遇到的障碍物信息，从而在路径重算时避免无效的循环尝试。

**技术框架**：OMM的整体架构包括一个分布式的黑名单系统，智能体在进行Dijkstra算法路径重算时会参考这一黑名单，以避免选择被阻塞的节点。

**关键创新**：OMM的核心创新在于其轻量级的设计，使得智能体能够在不增加过多计算负担的情况下，保持对环境的持久记忆，从而显著提高了多智能体系统的协调能力。

**关键设计**：OMM机制中，智能体维护的黑名单包含被阻塞的节点信息，重计算时仅需1.67次路径计算，而无记忆系统则需9.83次，极大提高了效率。实验中使用的Dijkstra算法为路径计算的基础。

## 📊 实验亮点

实验结果显示，采用OMM机制后，平均旅行时间减少了75.7%，等待时间减少了88%。与无记忆系统相比，OMM显著降低了每辆车的路径重计算次数，从9.83次减少到1.67次，表明其在多智能体协调中的重要性。

## 🎯 应用场景

该研究的成果可广泛应用于自主车辆、机器人导航、网络路由等领域，提升多智能体系统在动态环境中的协调能力。通过有效的障碍物记忆管理，未来的自主系统能够实现更高效的路径规划和资源利用，推动智能交通和智能城市的发展。

## 📄 摘要（原文）

> Multi-agent coordination is critical for next-generation autonomous vehicle (AV) systems, yet naive implementations of communication-based rerouting can lead to catastrophic performance degradation. This study investigates a fundamental problem in decentralized multi-agent navigation: routing loops, where vehicles without persistent obstacle memory become trapped in cycles of inefficient path recalculation. Through systematic simulation experiments involving 72 unique configurations across varying vehicle densities (15, 35, 55 vehicles) and obstacle frequencies (6, 20 obstacles), we demonstrate that memory-less reactive rerouting increases average travel time by up to 682% compared to baseline conditions. To address this, we introduce Object Memory Management (OMM), a lightweight mechanism enabling agents to retain and share knowledge of previously encountered obstacles. OMM operates by maintaining a distributed blacklist of blocked nodes, which each agent consults during Dijkstra-based path recalculation, effectively preventing redundant routing attempts. Our results show that OMM-enabled coordination reduces average travel time by 75.7% and wait time by 88% compared to memory-less systems, while requiring only 1.67 route recalculations per vehicle versus 9.83 in memory-less scenarios. This work provides empirical evidence that persistent, shared memory is not merely beneficial but essential for robust multi-agent coordination in dynamic environments. The findings have implications beyond autonomous vehicles, informing the design of decentralized systems in robotics, network routing, and distributed AI. We provide a comprehensive experimental analysis, including detailed scenario breakdowns, scalability assessments, and visual documentation of the routing loop phenomenon, demonstrating OMM's critical role in preventing detrimental feedback cycles in cooperative multi-agent systems.

