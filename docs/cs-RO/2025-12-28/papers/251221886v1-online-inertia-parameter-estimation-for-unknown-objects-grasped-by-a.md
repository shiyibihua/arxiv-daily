---
layout: default
title: Online Inertia Parameter Estimation for Unknown Objects Grasped by a Manipulator Towards Space Applications
---

# Online Inertia Parameter Estimation for Unknown Objects Grasped by a Manipulator Towards Space Applications

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21886" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21886v1</a>
  <a href="https://arxiv.org/pdf/2512.21886.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21886v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21886v1', 'Online Inertia Parameter Estimation for Unknown Objects Grasped by a Manipulator Towards Space Applications')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Akiyoshi Uchida, Antonine Richard, Kentaro Uno, Miguel Olivares-Mendez, Kazuya Yoshida

**分类**: cs.RO

**发布日期**: 2025-12-26

**备注**: Author's version of a manuscript accepted at the International Conference on Space Robotics 2025 (iSpaRo 2025). (c) IEEE

---

## 💡 一句话要点

**针对空间机器人，提出基于动量守恒的在线惯性参数估计方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `空间机器人` `惯性参数估计` `在线辨识` `动量守恒` `浮动基座`

## 📋 核心要点

1. 空间机器人操作中，精确掌握抓取物体的惯性参数至关重要，但现有方法难以直接应用于浮动基座机器人。
2. 本研究扩展了现有在线辨识方法，引入动量守恒定律，使其适用于浮动基座机器人，从而实现对未知物体的惯性参数估计。
3. 通过数值仿真验证了该方法的有效性，结果表明该方法能够准确辨识物体惯性参数，适用于空间任务。

## 📝 摘要（中文）

本文研究了在机械臂抓取未知物体时，对其惯性参数进行估计的问题，这对于动力学感知的操作至关重要，尤其是在具有自由漂浮基座的空间机器人中。我们应用并扩展了一种现有的在线辨识方法，通过结合动量守恒定律，使其能够应用于浮动基座机器人。通过数值仿真验证了所提出的方法，并将估计的参数与真实值进行了比较。结果表明，该方法在各种场景中都能实现准确的辨识，突出了其在在轨服务和其他空间任务中的适用性。

## 🔬 方法详解

**问题定义**：论文旨在解决浮动基座空间机器人抓取未知物体时，如何在线估计该物体惯性参数的问题。现有方法通常假设基座固定，无法直接应用于浮动基座机器人，导致动力学建模不准确，影响操作性能。

**核心思路**：核心思路是将动量守恒定律融入到在线惯性参数辨识过程中。由于浮动基座机器人系统在不受外力矩作用时，其总动量守恒，因此可以利用这一约束来提高惯性参数估计的准确性和鲁棒性。

**技术框架**：该方法基于现有的在线辨识方法，主要包含以下几个阶段：1) 机器人运动控制，产生合适的轨迹；2) 传感器数据采集，包括关节角度、角速度等；3) 动量计算，利用机器人和物体的运动状态计算系统总动量；4) 惯性参数估计，利用最小二乘法等优化算法，结合动量守恒约束，在线估计物体惯性参数。

**关键创新**：关键创新在于将动量守恒定律显式地引入到在线辨识过程中。传统方法忽略了这一物理约束，导致在浮动基座机器人上的估计精度下降。通过引入动量守恒，可以有效提高估计的准确性和鲁棒性。

**关键设计**：具体实现上，需要精确计算机器人和物体的动量，并将其作为约束条件加入到优化问题中。优化的目标函数通常是最小化测量值与模型预测值之间的误差。此外，还需要选择合适的激励轨迹，以保证参数的可辨识性。动量守恒的引入，体现在优化问题的约束条件中，例如，总动量在一段时间内保持不变。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21886v1/fig/intro/concept_not_credit_2.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21886v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21886v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过数值仿真验证了所提出方法的有效性。仿真结果表明，该方法能够准确估计未知物体的惯性参数，并且在存在噪声的情况下依然具有较好的鲁棒性。通过对比引入动量守恒约束前后的估计结果，验证了该约束对提高估计精度的作用。

## 🎯 应用场景

该研究成果可应用于在轨服务、空间碎片清理、行星探测等多种空间任务。准确的惯性参数估计能够提高机器人操作的精度和效率，降低任务风险。例如，在轨服务机器人需要抓取和操作各种卫星部件，准确的惯性参数估计是实现精确操作的前提。未来，该方法有望推广到其他类型的浮动基座机器人，例如水下机器人。

## 📄 摘要（原文）

> Knowing the inertia parameters of a grasped object is crucial for dynamics-aware manipulation, especially in space robotics with free-floating bases. This work addresses the problem of estimating the inertia parameters of an unknown target object during manipulation. We apply and extend an existing online identification method by incorporating momentum conservation, enabling its use for the floating-base robots. The proposed method is validated through numerical simulations, and the estimated parameters are compared with ground-truth values. Results demonstrate accurate identification in the scenarios, highlighting the method's applicability to on-orbit servicing and other space missions.

