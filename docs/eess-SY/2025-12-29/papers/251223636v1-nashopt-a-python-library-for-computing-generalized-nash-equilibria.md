---
layout: default
title: NashOpt - A Python Library for Computing Generalized Nash Equilibria
---

# NashOpt - A Python Library for Computing Generalized Nash Equilibria

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23636" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23636v1</a>
  <a href="https://arxiv.org/pdf/2512.23636.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23636v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23636v1', 'NashOpt - A Python Library for Computing Generalized Nash Equilibria')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alberto Bemporad

**分类**: eess.SY, cs.GT

**发布日期**: 2025-12-29

**备注**: 23 pages, 6 figures

**🔗 代码/项目**: [GITHUB](https://github.com/bemporad/nashopt)

---

## 💡 一句话要点

**NashOpt：用于计算广义纳什均衡的Python库**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `广义纳什均衡` `非合作博弈` `KKT条件` `JAX自动微分` `混合整数线性规划` `多智能体系统` `博弈论控制`

## 📋 核心要点

1. 现有方法在求解具有共享约束的非合作博弈中的广义纳什均衡（GNEs）时，效率和通用性存在挑战。
2. NashOpt库通过利用联合KKT条件，并结合JAX自动微分和混合整数线性规划，提供了一种高效且通用的GNE求解方案。
3. 通过线性二次调节和模型预测控制等实例验证了NashOpt在非合作博弈论控制问题中的有效性。

## 📝 摘要（中文）

NashOpt是一个开源Python库，用于计算和设计具有共享约束和实值决策变量的非合作博弈中的广义纳什均衡（GNEs）。该库利用所有参与者的联合Karush-Kuhn-Tucker（KKT）条件来处理一般的非线性GNEs和线性二次博弈，包括它们的变分版本。非线性博弈通过非线性最小二乘公式求解，依赖于JAX进行自动微分。线性二次GNEs被重新表述为混合整数线性规划，从而能够高效地计算多个均衡。该框架还支持逆博弈和Stackelberg博弈设计问题。NashOpt的功能通过几个例子得到证明，包括线性二次调节和模型预测控制的非合作博弈论控制问题。该库可在https://github.com/bemporad/nashopt 获取。

## 🔬 方法详解

**问题定义**：该论文旨在解决非合作博弈中广义纳什均衡（GNEs）的计算问题，特别是当博弈具有共享约束和实值决策变量时。现有方法在处理非线性博弈和寻找多个均衡方面存在效率瓶颈，并且缺乏对逆博弈和Stackelberg博弈设计的支持。

**核心思路**：NashOpt的核心思路是利用所有参与者的联合Karush-Kuhn-Tucker（KKT）条件来统一处理GNEs。对于非线性博弈，采用非线性最小二乘公式，并借助JAX进行自动微分以高效计算梯度。对于线性二次博弈，则将其转化为混合整数线性规划（MILP）问题，从而能够有效地找到多个均衡。

**技术框架**：NashOpt库的整体框架包括以下几个主要模块：1) 博弈定义模块：用于定义参与者、决策变量、目标函数和约束条件；2) KKT条件构建模块：基于博弈定义，构建所有参与者的联合KKT条件；3) 求解器模块：针对非线性博弈，采用基于JAX的非线性最小二乘求解器；针对线性二次博弈，采用MILP求解器；4) 结果分析模块：用于分析求解得到的GNE，并支持逆博弈和Stackelberg博弈设计。

**关键创新**：NashOpt的关键创新在于其统一的框架，能够同时处理非线性GNEs和线性二次GNEs。通过将线性二次GNEs转化为MILP问题，实现了多个均衡的高效计算。此外，该库还支持逆博弈和Stackelberg博弈设计，扩展了GNE的应用范围。

**关键设计**：对于非线性博弈，NashOpt依赖JAX进行自动微分，无需手动推导梯度，简化了开发流程。对于线性二次博弈，MILP的构建需要仔细选择决策变量和约束条件，以保证求解效率。逆博弈和Stackelberg博弈设计则需要根据具体问题，设计合适的目标函数和约束条件。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23636v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23636v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23636v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过多个示例展示了NashOpt的有效性，包括线性二次调节和模型预测控制的非合作博弈论控制问题。实验结果表明，NashOpt能够高效地计算GNE，并且能够处理具有复杂约束的博弈。此外，该库还展示了在逆博弈和Stackelberg博弈设计方面的应用。

## 🎯 应用场景

NashOpt可应用于多个领域，包括但不限于：多智能体系统控制、资源分配、交通网络优化、电力市场建模、以及博弈论在经济学和工程学中的其他应用。该库能够帮助研究人员和工程师设计和分析复杂的非合作博弈，并找到有效的均衡策略，从而优化系统性能。

## 📄 摘要（原文）

> NashOpt is an open-source Python library for computing and designing generalized Nash equilibria (GNEs) in noncooperative games with shared constraints and real-valued decision variables. The library exploits the joint Karush-Kuhn-Tucker (KKT) conditions of all players to handle both general nonlinear GNEs and linear-quadratic games, including their variational versions. Nonlinear games are solved via nonlinear least-squares formulations, relying on JAX for automatic differentiation. Linear-quadratic GNEs are reformulated as mixed-integer linear programs, enabling efficient computation of multiple equilibria. The framework also supports inverse-game and Stackelberg game-design problems. The capabilities of NashOpt are demonstrated through several examples, including noncooperative game-theoretic control problems of linear quadratic regulation and model predictive control. The library is available at https://github.com/bemporad/nashopt

