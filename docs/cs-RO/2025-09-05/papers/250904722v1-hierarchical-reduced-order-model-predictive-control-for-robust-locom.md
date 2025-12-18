---
layout: default
title: Hierarchical Reduced-Order Model Predictive Control for Robust Locomotion on Humanoid Robots
---

# Hierarchical Reduced-Order Model Predictive Control for Robust Locomotion on Humanoid Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04722" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04722v1</a>
  <a href="https://arxiv.org/pdf/2509.04722.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04722v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04722v1', 'Hierarchical Reduced-Order Model Predictive Control for Robust Locomotion on Humanoid Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Adrian B. Ghansah, Sergio A. Esteban, Aaron D. Ames

**分类**: cs.RO

**发布日期**: 2025-09-05

**备注**: 8 pages, 6 figures, accepted to IEEE-RAS International Conference on Humanoid Robots 2025

---

## 💡 一句话要点

**提出基于分层降阶模型预测控制的人形机器人鲁棒步态方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `人形机器人` `鲁棒步态` `模型预测控制` `分层控制` `降阶模型`

## 📋 核心要点

1. 现有方法难以在复杂环境中保证人形机器人的鲁棒行走，尤其是在扰动和地形变化下。
2. 该方法采用分层控制架构，利用降阶模型进行高效的步态规划，并融合手臂和躯干动力学以增强稳定性。
3. 实验表明，该方法在多种地形下实现了鲁棒行走，自适应步进时序显著提升了抗扰动能力。

## 📝 摘要（中文）

为了使人形机器人在真实环境中实现鲁棒的运动，本文提出了一种计算高效的分层控制框架，该框架基于降阶模型，能够实现通用的步态规划，并结合手臂和躯干动力学以更好地稳定行走。在高层，我们使用ALIP模型的步间动力学，通过非线性MPC同时优化步周期、步长和踝关节扭矩。ALIP轨迹被用作线性MPC框架的参考，该框架扩展了标准的SRB-MPC，还包括简化的手臂和躯干动力学。我们通过在Unitree G1人形机器人上的仿真和硬件实验验证了该方法的性能。在该框架中，高层步态规划器以40 Hz运行，中层MPC使用板载mini-PC以500 Hz运行。自适应步进时序将推力恢复成功率提高了36%，并且上半身控制改善了偏航扰动抑制。我们还展示了在各种室内和室外地形（包括草地、石板路和不平坦的体操垫）上的鲁棒运动。

## 🔬 方法详解

**问题定义**：人形机器人在复杂真实环境中行走时，需要具备鲁棒性，能够应对各种扰动和地形变化。现有的控制方法通常计算复杂度高，难以实时运行，或者对模型简化过度，导致抗扰动能力不足。

**核心思路**：本文的核心思路是采用分层控制架构，将复杂的全身运动控制问题分解为多个层次，每个层次使用不同的降阶模型和控制策略。高层进行步态规划，中层进行全身运动控制，从而在保证计算效率的同时，提高鲁棒性。

**技术框架**：该框架包含两个主要层次：高层步态规划和中层全身运动控制。高层使用ALIP（Angular Momentum Inverted Pendulum）模型，通过非线性MPC优化步周期、步长和踝关节扭矩，生成参考步态轨迹。中层使用扩展的SRB-MPC（Simplified Robot Body Model Predictive Control），除了标准的SRB模型外，还包括简化的手臂和躯干动力学，以提高稳定性。中层MPC跟踪高层生成的参考轨迹，并进行实时的运动控制。

**关键创新**：该方法的关键创新在于：1) 采用分层控制架构，有效降低了计算复杂度；2) 在中层MPC中融合了手臂和躯干动力学，提高了抗扰动能力；3) 使用自适应步进时序，进一步增强了鲁棒性。

**关键设计**：高层非线性MPC的目标函数包括步周期、步长和踝关节扭矩的优化项，以及约束条件，如步长范围、踝关节扭矩限制等。中层SRB-MPC的目标函数包括跟踪高层参考轨迹的误差项，以及控制力矩的惩罚项。自适应步进时序根据机器人的状态动态调整步周期，以提高抗扰动能力。

## 📊 实验亮点

实验结果表明，该方法在Unitree G1人形机器人上实现了鲁棒行走。自适应步进时序将推力恢复成功率提高了36%，表明其显著增强了抗扰动能力。此外，上半身控制改善了偏航扰动抑制，证明了融合手臂和躯干动力学的有效性。该方法还在草地、石板路和不平坦的体操垫等多种地形上实现了稳定行走。

## 🎯 应用场景

该研究成果可应用于人形机器人在复杂环境中的自主导航、搜索救援、工业巡检等领域。通过提高人形机器人的鲁棒性和适应性，使其能够在各种地形和扰动下稳定行走，从而扩展其应用范围和实用性。未来，该方法可以进一步扩展到更复杂的任务，如人机协作、物体操作等。

## 📄 摘要（原文）

> As humanoid robots enter real-world environments, ensuring robust locomotion across diverse environments is crucial. This paper presents a computationally efficient hierarchical control framework for humanoid robot locomotion based on reduced-order models -- enabling versatile step planning and incorporating arm and torso dynamics to better stabilize the walking. At the high level, we use the step-to-step dynamics of the ALIP model to simultaneously optimize over step periods, step lengths, and ankle torques via nonlinear MPC. The ALIP trajectories are used as references to a linear MPC framework that extends the standard SRB-MPC to also include simplified arm and torso dynamics. We validate the performance of our approach through simulation and hardware experiments on the Unitree G1 humanoid robot. In the proposed framework the high-level step planner runs at 40 Hz and the mid-level MPC at 500 Hz using the onboard mini-PC. Adaptive step timing increased the push recovery success rate by 36%, and the upper body control improved the yaw disturbance rejection. We also demonstrate robust locomotion across diverse indoor and outdoor terrains, including grass, stone pavement, and uneven gym mats.

