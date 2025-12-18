---
layout: default
title: Safe Robust Predictive Control-based Motion Planning of Automated Surface Vessels in Inland Waterways
---

# Safe Robust Predictive Control-based Motion Planning of Automated Surface Vessels in Inland Waterways

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06687" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06687v1</a>
  <a href="https://arxiv.org/pdf/2509.06687.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06687v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06687v1', 'Safe Robust Predictive Control-based Motion Planning of Automated Surface Vessels in Inland Waterways')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sajad Ahmadi, Hossein Nejatbakhsh Esfahani, Javad Mohammadpour Velni

**分类**: cs.RO, eess.SY

**发布日期**: 2025-09-08

---

## 💡 一句话要点

**提出基于安全鲁棒预测控制的水面无人艇内河航行运动规划方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `水面无人艇` `鲁棒模型预测控制` `控制屏障函数` `运动规划` `自主导航`

## 📋 核心要点

1. 内河航运面临狭窄航道、高交通密度和水动力扰动等挑战，现有自主航行方法缺乏足够的鲁棒性和精确性。
2. 论文核心在于结合鲁棒模型预测控制（RMPC）和控制屏障函数（CBF），将航道边界和障碍物作为安全约束。
3. 仿真结果验证了该方法在复杂水道上的有效性，表明其在安全性和适应性方面优于现有技术。

## 📝 摘要（中文）

本文提出了一种用于自动化水面无人艇（ASV）的运动规划新方法，该方法结合了鲁棒模型预测控制（RMPC）和控制屏障函数（CBF）。通过将航道边界和障碍物作为安全约束纳入控制设计框架，该方法确保了在复杂水道上的避碰和鲁棒导航。仿真结果表明，该方法在实际条件下能够安全地引导ASV，与现有技术相比，提高了安全性和适应性。

## 🔬 方法详解

**问题定义**：论文旨在解决自动化水面无人艇（ASV）在内河航道中安全、鲁棒的运动规划问题。现有方法在狭窄航道、高交通密度和水动力扰动等复杂环境下，难以保证ASV的航行安全和精确性，容易发生碰撞或偏离航线。

**核心思路**：论文的核心思路是将鲁棒模型预测控制（RMPC）与控制屏障函数（CBF）相结合。RMPC用于优化ASV的运动轨迹，CBF则用于确保ASV满足安全约束，如避碰和保持在航道内。通过将安全约束显式地纳入控制设计框架，可以提高ASV在不确定环境下的鲁棒性和安全性。

**技术框架**：该方法的技术框架主要包括以下几个模块：1) ASV的动力学模型；2) RMPC控制器设计，用于生成最优控制输入；3) CBF设计，用于定义安全区域和约束；4) 优化问题求解器，用于求解RMPC问题并满足CBF约束。整体流程是，首先根据环境信息和目标点，RMPC控制器生成初步的控制输入，然后CBF模块检查该控制输入是否满足安全约束，如果不满足，则对控制输入进行调整，直到满足安全约束为止。

**关键创新**：该方法最重要的技术创新点在于将RMPC和CBF有效地结合起来，从而在保证ASV运动性能的同时，确保其航行安全。与传统的RMPC方法相比，该方法能够更有效地处理安全约束，避免碰撞。与单独使用CBF的方法相比，该方法能够更好地优化ASV的运动轨迹，提高航行效率。

**关键设计**：CBF的设计是关键。论文需要定义合适的安全区域，并设计相应的CBF函数，以确保ASV始终保持在安全区域内。RMPC控制器的参数设置也至关重要，需要根据ASV的动力学特性和环境条件进行调整，以获得最佳的控制性能。此外，优化问题求解器的选择也会影响计算效率和控制效果。

## 📊 实验亮点

仿真结果表明，该方法能够有效地引导ASV在复杂的内河航道中安全航行，避免碰撞，并保持在航道内。与现有方法相比，该方法在安全性和适应性方面均有显著提升。具体的性能数据（如避碰成功率、航行时间等）未在摘要中明确给出，但强调了其优于现有技术的表现。

## 🎯 应用场景

该研究成果可应用于内河水域的自动化航运、港口物流、水上巡逻和环境监测等领域。通过提高水面无人艇的自主导航能力和安全性，可以降低运营成本，提高运输效率，并减少人为事故的发生。未来，该技术有望推广到更广泛的水域，促进智能航运的发展。

## 📄 摘要（原文）

> Deploying self-navigating surface vessels in inland waterways offers a sustainable alternative to reduce road traffic congestion and emissions. However, navigating confined waterways presents unique challenges, including narrow channels, higher traffic density, and hydrodynamic disturbances. Existing methods for autonomous vessel navigation often lack the robustness or precision required for such environments. This paper presents a new motion planning approach for Automated Surface Vessels (ASVs) using Robust Model Predictive Control (RMPC) combined with Control Barrier Functions (CBFs). By incorporating channel borders and obstacles as safety constraints within the control design framework, the proposed method ensures both collision avoidance and robust navigation on complex waterways. Simulation results demonstrate the efficacy of the proposed method in safely guiding ASVs under realistic conditions, highlighting its improved safety and adaptability compared to the state-of-the-art.

