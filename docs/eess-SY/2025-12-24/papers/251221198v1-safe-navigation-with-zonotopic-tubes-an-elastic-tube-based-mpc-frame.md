---
layout: default
title: "Safe Navigation with Zonotopic Tubes: An Elastic Tube-based MPC Framework"
---

# Safe Navigation with Zonotopic Tubes: An Elastic Tube-based MPC Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21198" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21198v1</a>
  <a href="https://arxiv.org/pdf/2512.21198.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21198v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21198v1', 'Safe Navigation with Zonotopic Tubes: An Elastic Tube-based MPC Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Niyousha Ghiasi, Bahare Kiumarsi, Hamidreza Modares

**分类**: eess.SY

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**提出基于Zonotope Tube的弹性Tube-based MPC框架，用于未知线性系统的安全导航。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模型预测控制` `MPC` `Zonotope Tube` `鲁棒控制` `自适应控制` `安全导航` `线性系统` `不确定系统`

## 📋 核心要点

1. 现有弹性Tube-based MPC方法通常假设已知精确的系统模型和扰动边界，这在实际应用中难以满足。
2. 该论文提出一种迭代细化Zonotope扰动集的方法，融合先验知识和在线数据，以提高MPC的性能和可行性。
3. 通过自适应协同设计Tube和反馈增益，实现了λ-收缩Zonotope Tube，保证了鲁棒性和稳定性，仿真验证了其有效性。

## 📝 摘要（中文）

本文提出了一种基于弹性Tube的MPC框架，用于处理受扰动的未知离散时间线性系统。与现有方法不同，该方法不假设系统模型或扰动边界的完美知识。相反，初始化一个保守的Zonotope扰动集，并通过数据和先验知识迭代细化：利用数据识别系统动力学的矩阵Zonotope模型集，并利用先验物理知识排除与已知约束不一致的模型和扰动。该过程产生受约束的矩阵Zonotope，代表扰动实现和动力学，从而将离线信息与有限的在线数据进行融合，提高MPC的可行性和性能。该设计利用闭环系统特性来学习和细化控制增益，以保持较小的Tube尺寸。通过在误差动态中分离开环模型失配和闭环效应，该方法避免了对状态和输入操作区域大小的依赖，从而降低了保守性。Tube和辅助反馈的自适应协同设计确保了λ-收缩Zonotope Tube，保证了鲁棒正不变性，提高了可行性裕度，并增强了抗扰动能力。建立了递归可行性条件，并为误差Tube引入了多面体Lyapunov候选函数，证明了在自适应Tube增益更新下闭环误差动态的指数稳定性。仿真结果表明，仅使用少量在线数据即可提高鲁棒性，扩大可行性区域，并实现安全的闭环性能。

## 🔬 方法详解

**问题定义**：该论文旨在解决在系统模型和扰动边界未知的情况下，如何实现线性系统的安全导航问题。现有弹性Tube-based MPC方法通常假设系统模型和扰动边界已知，这在实际应用中往往难以满足，导致控制性能下降甚至失效。

**核心思路**：论文的核心思路是利用Zonotope来保守地估计系统的不确定性，并通过在线数据和先验知识迭代地细化Zonotope的边界，从而提高模型精度和控制性能。同时，通过自适应地调整Tube的大小和反馈增益，保证系统的鲁棒性和稳定性。

**技术框架**：该方法主要包含以下几个阶段：1) 初始化一个保守的Zonotope扰动集；2) 利用在线数据识别系统动力学的矩阵Zonotope模型集；3) 利用先验知识排除与已知约束不一致的模型和扰动；4) 自适应地调整Tube的大小和反馈增益，保证λ-收缩性；5) 利用多面体Lyapunov函数证明闭环系统的稳定性。

**关键创新**：该方法最重要的创新点在于能够将离线信息与有限的在线数据进行融合，从而在系统模型和扰动边界未知的情况下，实现安全导航。此外，通过自适应地调整Tube的大小和反馈增益，可以有效地降低保守性，提高控制性能。

**关键设计**：关键设计包括：1) 使用矩阵Zonotope来表示系统动力学的不确定性；2) 设计自适应的Tube和反馈增益更新策略，保证λ-收缩性；3) 使用多面体Lyapunov函数来证明闭环系统的稳定性；4) 迭代细化Zonotope扰动集，融合先验知识和在线数据。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21198v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21198v1/RbXL.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21198v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

仿真结果表明，该方法仅使用少量在线数据即可提高鲁棒性，扩大可行性区域，并实现安全的闭环性能。与传统方法相比，该方法能够更好地处理系统模型和扰动边界未知的情况，具有更强的适应性和鲁棒性。具体性能提升数据未知。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、飞行器控制等领域，尤其适用于环境不确定、模型难以精确获取的场景。通过融合先验知识和在线数据，该方法能够提高系统的鲁棒性和安全性，具有重要的实际应用价值和广阔的应用前景。

## 📄 摘要（原文）

> This paper presents an elastic tube-based model predictive control (MPC) framework for unknown discrete-time linear systems subject to disturbances. Unlike most existing elastic tube-based MPC methods, we do not assume perfect knowledge of the system model or disturbance realizations bounds. Instead, a conservative zonotopic disturbance set is initialized and iteratively refined using data and prior knowledge: data are used to identify matrix zonotope model sets for the system dynamics, while prior physical knowledge is employed to discard models and disturbances inconsistent with known constraints. This process yields constrained matrix zonotopes representing disturbance realizations and dynamics that enable a principled fusion of offline information with limited online data, improving MPC feasibility and performance. The proposed design leverages closed-loop system characterization to learn and refine control gains that maintain a small tube size. By separating open-loop model mismatch from closed-loop effects in the error dynamics, the method avoids dependence on the size of the state and input operating regions, thereby reducing conservatism. An adaptive co-design of the tube and ancillary feedback ensures $λ$-contractive zonotopic tubes, guaranteeing robust positive invariance, improved feasibility margins, and enhanced disturbance tolerance. We establish recursive feasibility conditions and introduce a polyhedral Lyapunov candidate for the error tube, proving exponential stability of the closed-loop error dynamics under the adaptive tube-gain updates. Simulations demonstrate improved robustness, enlarged feasibility regions, and safe closed-loop performance using only a small amount of online data.

