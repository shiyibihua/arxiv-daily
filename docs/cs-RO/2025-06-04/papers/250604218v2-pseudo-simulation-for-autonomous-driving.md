---
layout: default
title: Pseudo-Simulation for Autonomous Driving
---

# Pseudo-Simulation for Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04218" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04218v2</a>
  <a href="https://arxiv.org/pdf/2506.04218.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04218v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04218v2', 'Pseudo-Simulation for Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wei Cao, Marcel Hallgarten, Tianyu Li, Daniel Dauner, Xunjiang Gu, Caojun Wang, Yakov Miron, Marco Aiello, Hongyang Li, Igor Gilitschenski, Boris Ivanovic, Marco Pavone, Andreas Geiger, Kashyap Chitta

**分类**: cs.RO, cs.AI, cs.CV, cs.LG

**发布日期**: 2025-06-04 (更新: 2025-08-27)

**备注**: CoRL 2025

**🔗 代码/项目**: [GITHUB](https://github.com/autonomousvision/navsim)

---

## 💡 一句话要点

**提出伪仿真以解决自动驾驶评估中的局限性**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `自动驾驶` `伪仿真` `评估方法` `3D高斯点云` `合成观测` `错误恢复` `因果混淆` `开放式评估`

## 📋 核心要点

1. 现有的自动驾驶评估方法在安全性和可重复性方面存在显著挑战，尤其是在真实世界环境中。
2. 本文提出的伪仿真方法通过在真实数据集上生成合成观测，增强了评估的准确性和有效性。
3. 实验结果表明，伪仿真与闭环仿真的相关性更高，提供了更可靠的评估基准。

## 📝 摘要（中文）

现有的自动驾驶车辆（AV）评估范式面临重大局限。现实世界评估因安全问题和缺乏可重复性而困难，而闭环仿真则可能面临现实性不足或计算成本高的问题。开放式评估虽然高效且数据驱动，但依赖的指标通常忽视了累积误差。本文提出伪仿真，这是一种新颖的范式，旨在解决这些局限。伪仿真基于真实数据集，类似于开放式评估，但通过3D高斯点云生成的合成观测进行增强。我们的关键思想是通过生成在位置、朝向和速度上变化的多样化观测，来近似AV可能遇到的潜在未来状态。我们的方法通过一种新颖的基于接近度的加权方案，赋予最符合AV可能行为的合成观测更高的重要性。这使得在不需要顺序交互仿真的情况下，能够评估错误恢复和因果混淆的缓解。我们证明伪仿真与闭环仿真的相关性更高（$R^2=0.8$），优于现有最佳开放式方法（$R^2=0.7$）。

## 🔬 方法详解

**问题定义**：现有的自动驾驶评估方法在真实世界中面临安全性和可重复性的问题，而闭环仿真则可能缺乏现实性或计算成本过高。开放式评估虽然高效，但通常忽视累积误差。

**核心思路**：本文提出的伪仿真方法通过在真实数据集上生成合成观测，来近似自动驾驶车辆可能遇到的未来状态，从而提高评估的准确性。

**技术框架**：伪仿真方法的整体架构包括数据集的真实观测和合成观测的生成，利用3D高斯点云技术生成多样化的合成观测，并通过基于接近度的加权方案来增强评估的有效性。

**关键创新**：伪仿真的关键创新在于结合真实数据和合成观测，通过动态生成多样化的未来状态来提高评估的准确性，与现有方法相比，能够更好地捕捉潜在的行为模式。

**关键设计**：在伪仿真中，合成观测的生成依赖于3D高斯点云技术，重要性加权则基于AV的行为预测，确保最符合实际情况的观测被赋予更高的权重。具体的参数设置和损失函数设计在论文中有详细描述。

## 📊 实验亮点

实验结果显示，伪仿真与闭环仿真的相关性达到$R^2=0.8$，显著优于现有最佳开放式方法的$R^2=0.7$。此外，研究团队还建立了一个公共基准平台，供社区使用伪仿真进行新方法的评估和比较。

## 🎯 应用场景

该研究的伪仿真方法具有广泛的应用潜力，特别是在自动驾驶车辆的开发和测试中。通过提供更准确的评估手段，能够帮助研究人员和工程师更有效地优化自动驾驶系统，提高其安全性和可靠性。未来，该方法还可能扩展到其他领域的仿真评估中，推动相关技术的发展。

## 📄 摘要（原文）

> Existing evaluation paradigms for Autonomous Vehicles (AVs) face critical limitations. Real-world evaluation is often challenging due to safety concerns and a lack of reproducibility, whereas closed-loop simulation can face insufficient realism or high computational costs. Open-loop evaluation, while being efficient and data-driven, relies on metrics that generally overlook compounding errors. In this paper, we propose pseudo-simulation, a novel paradigm that addresses these limitations. Pseudo-simulation operates on real datasets, similar to open-loop evaluation, but augments them with synthetic observations generated prior to evaluation using 3D Gaussian Splatting. Our key idea is to approximate potential future states the AV might encounter by generating a diverse set of observations that vary in position, heading, and speed. Our method then assigns a higher importance to synthetic observations that best match the AV's likely behavior using a novel proximity-based weighting scheme. This enables evaluating error recovery and the mitigation of causal confusion, as in closed-loop benchmarks, without requiring sequential interactive simulation. We show that pseudo-simulation is better correlated with closed-loop simulations ($R^2=0.8$) than the best existing open-loop approach ($R^2=0.7$). We also establish a public leaderboard for the community to benchmark new methodologies with pseudo-simulation. Our code is available at https://github.com/autonomousvision/navsim.

