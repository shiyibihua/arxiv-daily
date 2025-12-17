---
layout: default
title: TOPP-DWR: Time-Optimal Path Parameterization of Differential-Driven Wheeled Robots Considering Piecewise-Constant Angular Velocity Constraints
---

# TOPP-DWR: Time-Optimal Path Parameterization of Differential-Driven Wheeled Robots Considering Piecewise-Constant Angular Velocity Constraints

**arXiv**: [2511.12910v1](https://arxiv.org/abs/2511.12910) | [PDF](https://arxiv.org/pdf/2511.12910.pdf)

**作者**: Yong Li, Yujun Huang, Yi Chen, Hui Cheng

**分类**: cs.RO

**发布日期**: 2025-11-17

**期刊**: 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2025)

---

## 💡 一句话要点

**提出TOPP-DWR算法，解决差速轮式机器人时间最优路径规划中角速度约束问题**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `时间最优路径规划` `差速轮式机器人` `角速度约束` `二阶锥规划` `自主导航`

## 📋 核心要点

1. 现有移动机器人时间最优路径规划（TOPP）通常忽略角速度和关节速度约束，导致实际控制性能下降。
2. TOPP-DWR算法将分段常数角速度、关节速度、线速度和线加速度约束统一表示为线速度约束，并转化为SOCP问题。
3. 实验结果表明，TOPP-DWR算法在满足所有约束的条件下实现了时间最优路径规划，并在实际导航中验证了可行性。

## 📝 摘要（中文）

本文提出了一种针对差速轮式机器人（DWR）的时间最优路径参数化（TOPP）算法，名为TOPP-DWR。该算法旨在解决现有TOPP方法忽略角速度和关节速度约束的问题，这些约束的忽略会导致实际应用中控制性能下降。首先，采用非均匀B样条表示任务空间中的初始轨迹。其次，将分段常数的角速度、关节速度、线速度和线加速度约束纳入TOPP问题。在构建优化问题时，上述约束被统一表示为线速度约束。为了提高数值计算效率，引入松弛变量将问题转化为二阶锥规划（SOCP）。通过对比实验验证了该方法的优越性。定量性能指标表明，TOPP-DWR在满足所有约束的同时实现了TOPP。最后，通过现场自主导航实验验证了TOPP-DWR在实际应用中的可行性。

## 🔬 方法详解

**问题定义**：论文旨在解决差速轮式机器人在时间最优路径规划（TOPP）中，现有方法忽略角速度和关节速度约束，导致实际控制性能下降的问题。这些约束在实际机器人运动中至关重要，忽略它们会导致规划的轨迹无法被机器人精确执行，从而影响导航和控制的精度。

**核心思路**：论文的核心思路是将角速度、关节速度、线速度和线加速度等多种约束统一表示为线速度约束，从而简化优化问题的形式。此外，为了提高计算效率，引入松弛变量，将优化问题转化为二阶锥规划（SOCP）问题，SOCP问题具有高效的求解器，能够快速得到最优解。

**技术框架**：TOPP-DWR算法的整体流程如下：1) 使用非均匀B样条曲线表示初始轨迹；2) 将角速度、关节速度、线速度和线加速度约束转化为线速度约束；3) 引入松弛变量，将优化问题转化为SOCP问题；4) 使用SOCP求解器求解最优时间参数；5) 根据最优时间参数生成最终轨迹。

**关键创新**：该论文的关键创新在于将多种类型的约束（包括角速度、关节速度等）统一表示为线速度约束，并将其纳入TOPP问题中。这种统一表示方法简化了优化问题的形式，使得可以使用标准的SOCP求解器进行求解。此外，引入松弛变量进一步提高了计算效率。

**关键设计**：论文中一个关键的设计是将分段常数的角速度约束纳入考虑。这意味着在每个时间段内，角速度被限制在一个常数值范围内。这种分段常数约束更符合实际机器人运动的特点，也更容易在优化问题中进行处理。此外，选择非均匀B样条曲线作为初始轨迹的表示方法，因为它具有良好的局部可控性和平滑性。

## 📊 实验亮点

实验结果表明，TOPP-DWR算法能够在满足所有约束条件（包括角速度、关节速度、线速度和线加速度约束）的情况下，实现时间最优的路径参数化。与忽略角速度约束的传统TOPP方法相比，TOPP-DWR算法能够生成更平滑、更可执行的轨迹，从而提高机器人的控制性能。现场自主导航实验验证了TOPP-DWR算法在实际应用中的可行性。

## 🎯 应用场景

TOPP-DWR算法可广泛应用于各种差速轮式机器人的自主导航、路径规划和运动控制等领域。例如，在仓储物流机器人、服务机器人、农业机器人等场景中，该算法可以生成满足各种约束条件的时间最优轨迹，提高机器人的运动效率和控制精度。此外，该算法还可以扩展到其他类型的移动机器人，具有广泛的应用前景。

## 📄 摘要（原文）

> Differential-driven wheeled robots (DWR) represent the quintessential type of mobile robots and find extensive appli- cations across the robotic field. Most high-performance control approaches for DWR explicitly utilize the linear and angular velocities of the trajectory as control references. However, existing research on time-optimal path parameterization (TOPP) for mobile robots usually neglects the angular velocity and joint vel- ocity constraints, which can result in degraded control perfor- mance in practical applications. In this article, a systematic and practical TOPP algorithm named TOPP-DWR is proposed for DWR and other mobile robots. First, the non-uniform B-spline is adopted to represent the initial trajectory in the task space. Second, the piecewise-constant angular velocity, as well as joint velocity, linear velocity, and linear acceleration constraints, are incorporated into the TOPP problem. During the construction of the optimization problem, the aforementioned constraints are uniformly represented as linear velocity constraints. To boost the numerical computational efficiency, we introduce a slack variable to reformulate the problem into second-order-cone programming (SOCP). Subsequently, comparative experiments are conducted to validate the superiority of the proposed method. Quantitative performance indexes show that TOPP-DWR achieves TOPP while adhering to all constraints. Finally, field autonomous navigation experiments are carried out to validate the practicability of TOPP-DWR in real-world applications.

