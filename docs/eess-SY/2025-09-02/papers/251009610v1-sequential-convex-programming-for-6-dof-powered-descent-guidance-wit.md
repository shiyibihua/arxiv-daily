---
layout: default
title: Sequential Convex Programming for 6-DoF Powered Descent Guidance with Continuous-Time Compound State-Triggered Constraints
---

# Sequential Convex Programming for 6-DoF Powered Descent Guidance with Continuous-Time Compound State-Triggered Constraints

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.09610" class="toolbar-btn" target="_blank">📄 arXiv: 2510.09610v1</a>
  <a href="https://arxiv.org/pdf/2510.09610.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09610v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.09610v1', 'Sequential Convex Programming for 6-DoF Powered Descent Guidance with Continuous-Time Compound State-Triggered Constraints')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Samet Uzun, Behcet Acikmese, John M. Carson

**分类**: eess.SY

**发布日期**: 2025-09-02

**🔗 代码/项目**: [GITHUB](https://github.com/UW-ACL/CT-cSTC)

---

## 💡 一句话要点

**提出一种基于序列凸规划的6自由度动力下降制导方法，保证连续时间复合状态触发约束**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `序列凸规划` `动力下降制导` `连续时间约束` `复合状态触发约束` `轨迹优化`

## 📋 核心要点

1. 动力下降制导（PDG）问题中，现有方法难以保证连续时间复合状态触发约束的满足，尤其是在复杂逻辑规范下。
2. 该论文提出结合D-GMSR和CT-SCvx的SCP框架，将离散时间逻辑规范转化为平滑函数，并利用连续时间凸化方法求解。
3. 数值模拟验证了该框架的有效性，表明该方法能够在保证理论保证的前提下，高效解决PDG问题。

## 📝 摘要（中文）

本文提出了一种序列凸规划（SCP）框架，用于确保动力下降制导（PDG）问题中连续时间复合状态触发约束（一种逻辑规范子集）的满足。该框架结合了广义均值平滑鲁棒性度量（D-GMSR）——一种为通过平滑函数表达离散时间时序和逻辑规范而量身定制的参数化技术，以及连续时间逐次凸化（CT-SCvx）方法——一种用于约束轨迹优化的实时解决方案，保证连续时间约束满足和收敛。D-GMSR参数化的时序和逻辑规范的平滑性使得能够使用鲁棒且高效的SCP算法解决由此产生的优化问题，同时保留理论保证。除了平滑性之外，参数化的规范是可靠且完备的，这意味着规范成立当且仅当参数化函数定义的约束得到满足。然后，应用CT-SCvx框架来解决参数化问题，包括：（1）用于连续时间路径约束满足的重构，（2）时间膨胀以将自由最终时间PDG问题转换为固定最终时间问题，（3）用于精确离散化的多重打靶法，（4）用于惩罚非凸约束的精确惩罚函数，以及（5）prox-linear方法——一种保证收敛的SCP算法，以解决由此产生的有限维非凸PDG问题。通过数值模拟证明了该框架的有效性。该实现可在https://github.com/UW-ACL/CT-cSTC获得。

## 🔬 方法详解

**问题定义**：论文旨在解决动力下降制导（PDG）问题中，如何保证连续时间复合状态触发约束（compound state-triggered constraints）的满足。现有的方法在处理复杂的逻辑规范时，难以保证约束的连续时间满足，并且计算效率较低。尤其是在自由最终时间（free-final-time）的PDG问题中，约束的处理更加复杂。

**核心思路**：论文的核心思路是将离散时间的时序和逻辑规范，通过广义均值平滑鲁棒性度量（D-GMSR）进行参数化，转化为平滑函数。然后，利用连续时间逐次凸化（CT-SCvx）方法，将非凸的PDG问题转化为一系列凸优化问题进行求解。通过这种方式，既保证了约束的连续时间满足，又提高了计算效率。

**技术框架**：整体框架包括以下几个主要模块：
1. **D-GMSR参数化**：将离散时间逻辑规范转化为平滑函数。
2. **CT-SCvx凸化**：利用连续时间逐次凸化方法，将非凸问题转化为凸优化问题。
3. **时间膨胀**：将自由最终时间问题转化为固定最终时间问题。
4. **多重打靶法**：用于精确离散化。
5. **精确惩罚函数**：用于惩罚非凸约束。
6. **Prox-linear方法**：使用保证收敛的SCP算法求解最终的优化问题。

**关键创新**：最重要的技术创新点在于将D-GMSR和CT-SCvx相结合，实现了连续时间复合状态触发约束的满足。D-GMSR的平滑性保证了可以使用高效的SCP算法进行求解，而CT-SCvx保证了约束的连续时间满足。与现有方法相比，该方法能够在保证理论保证的前提下，更有效地解决PDG问题。

**关键设计**：关键设计包括：
1. **D-GMSR的参数化方式**：选择合适的均值函数和鲁棒性参数，以保证参数化后的函数既平滑又能够准确地表达原始的逻辑规范。
2. **CT-SCvx的凸化策略**：选择合适的凸化方法，以保证凸优化问题的求解效率和精度。
3. **时间膨胀的比例**：选择合适的时间膨胀比例，以保证转化后的固定最终时间问题与原始的自由最终时间问题等价。
4. **精确惩罚函数的权重**：选择合适的权重，以保证非凸约束的满足。

## 📊 实验亮点

论文通过数值模拟验证了所提出框架的有效性。实验结果表明，该方法能够在满足连续时间复合状态触发约束的前提下，有效地解决动力下降制导问题。具体的性能数据和对比基线在论文中进行了详细的展示，证明了该方法在保证约束满足和计算效率方面的优势。

## 🎯 应用场景

该研究成果可应用于航天器的精确着陆、无人机的自主导航、以及机器人的运动规划等领域。通过保证连续时间复合状态触发约束的满足，可以提高系统的安全性和可靠性，例如在着陆过程中避开危险区域，或者在导航过程中遵守交通规则。该方法具有重要的实际应用价值和未来发展潜力。

## 📄 摘要（原文）

> This paper presents a sequential convex programming (SCP) framework for ensuring the continuous-time satisfaction of compound state-triggered constraints, a subset of logical specifications, in the powered descent guidance (PDG) problem. The proposed framework combines the generalized mean-based smooth robustness measure (D-GMSR), a parameterization technique tailored for expressing discrete-time temporal and logical specifications through smooth functions, with the continuous-time successive convexification (CT-SCvx) method, a real-time solution for constrained trajectory optimization that guarantees continuous-time constraint satisfaction and convergence. The smoothness of the temporal and logical specifications parameterized via D-GMSR enables solving the resulting optimization problem with robust and efficient SCP algorithms while preserving theoretical guarantees. In addition to their smoothness, the parameterized specifications are sound and complete, meaning the specification holds if and only if the constraint defined by the parameterized function is satisfied. The CT-SCvx framework is then applied to solve the parameterized problem, incorporating: (1) reformulation for continuous-time path constraint satisfaction, (2) time-dilation to transform the free-final-time PDG problem into a fixed-final-time problem, (3) multiple shooting for exact discretization, (4) exact penalty functions for penalizing nonconvex constraints, and (5) the prox-linear method, a convergence-guaranteed SCP algorithm, to solve the resulting finite-dimensional nonconvex PDG problem. The effectiveness of the framework is demonstrated through a numerical simulation. The implementation is available at https://github.com/UW-ACL/CT-cSTC

