---
layout: default
title: "Antagonistic Bowden-Cable Actuation of a Lightweight Robotic Hand: Toward Dexterous Manipulation for Payload Constrained Humanoids"
---

# Antagonistic Bowden-Cable Actuation of a Lightweight Robotic Hand: Toward Dexterous Manipulation for Payload Constrained Humanoids

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24657" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24657v1</a>
  <a href="https://arxiv.org/pdf/2512.24657.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24657v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24657v1', 'Antagonistic Bowden-Cable Actuation of a Lightweight Robotic Hand: Toward Dexterous Manipulation for Payload Constrained Humanoids')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sungjae Min, Hyungjoo Kim, David Hyunchul Shim

**分类**: cs.RO

**发布日期**: 2025-12-31

**备注**: Preprint

---

## 💡 一句话要点

**提出一种基于拮抗式Bowden线缆驱动的轻量化机械手，用于有效载荷受限的人形机器人灵巧操作。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机械手` `Bowden线缆驱动` `拮抗式驱动` `轻量化设计` `人形机器人` `灵巧操作` `滚动接触关节`

## 📋 核心要点

1. 人形机器人需要具备高抓握力、快速驱动、多自由度和轻量化结构的灵巧手，但这些需求相互冲突，难以同时满足。
2. 该论文提出一种基于Bowden线缆驱动的轻量化机械手，通过滚动接触关节优化和拮抗式线缆驱动，实现单电机控制和低线缆长度偏差。
3. 实验结果表明，该机械手远端质量仅为236g，能产生超过18N的指尖力，并能举起超过自身质量一百倍的有效载荷，验证了其鲁棒性。

## 📝 摘要（中文）

本文提出了一种轻量级拟人机械手，该机械手由Bowden线缆驱动，独特地结合了滚动接触关节优化和拮抗式线缆驱动，实现了每个关节单电机控制，且线缆长度偏差可忽略不计。通过将执行器模块重新定位到躯干，该设计在保持拟人尺度和灵巧性的同时，显著降低了远端质量。此外，这种拮抗式线缆驱动消除了电机之间的同步需求。使用所提出的方法，远端质量为236克的机械手（不包括远程执行器和Bowden护套）展示了灵巧任务的可靠执行，超过18N的指尖力，并能举起超过自身质量一百倍的有效载荷。此外，通过Cutkosky分类抓取和在扰动执行器-手部变换下的轨迹一致性验证了鲁棒性。

## 🔬 方法详解

**问题定义**：人形机器人需要灵巧的手部，但现有方法难以同时满足高抓握力、快速驱动、多自由度、轻量化和拟人尺寸等相互冲突的需求。传统的解决方案通常需要更重的执行器和更笨重的传动系统，从而显著限制了机器人手臂的有效载荷能力。

**核心思路**：该论文的核心思路是将执行器模块远程放置到躯干，通过Bowden线缆驱动机械手，从而显著降低手部的远端质量。同时，采用拮抗式线缆驱动，每个关节仅需一个电机，无需电机间的同步，简化了控制系统。

**技术框架**：该机械手的整体架构包括：1) 远程执行器模块（位于躯干）；2) Bowden线缆传动系统；3) 具有滚动接触关节的轻量化机械手。通过拮抗式线缆驱动，每个关节由一对线缆控制，实现正反两个方向的运动。

**关键创新**：该论文的关键创新在于：1) 结合了滚动接触关节优化和拮抗式线缆驱动，实现了单电机-单关节控制，并最大程度地减少了线缆长度偏差；2) 通过远程执行器布局，显著降低了手部的远端质量，提高了有效载荷能力；3) 采用拮抗式线缆驱动，消除了电机同步的需求，简化了控制。

**关键设计**：在机械手设计中，优化了滚动接触关节的几何形状，以减少线缆长度偏差。拮抗式线缆驱动采用预张力，以确保线缆始终处于张紧状态，从而提高控制精度和响应速度。线缆的选择需要考虑强度、柔韧性和摩擦系数等因素。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24657v1/Image/PCDRH2_33Captioned3.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24657v1/Image/Fig_0_HumanHandDOF.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24657v1/Image/Fig_0_RobotHandDOF.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该机械手远端质量仅为236g（不含远程执行器和线缆护套），能够产生超过18N的指尖力，并成功举起超过自身质量一百倍的有效载荷。通过Cutkosky分类抓取实验和在扰动下的轨迹一致性验证，证明了该机械手具有良好的鲁棒性和适应性。这些实验结果表明，该设计在轻量化和灵巧操作方面取得了显著的进展。

## 🎯 应用场景

该研究成果可应用于有效载荷受限的人形机器人，使其能够执行更复杂的灵巧操作任务，例如在狭小空间内的装配、医疗手术辅助、以及危险环境下的物品操作。轻量化设计也有助于提高机器人的安全性，降低与人交互时的风险。未来，该技术有望扩展到外骨骼和假肢等领域。

## 📄 摘要（原文）

> Humanoid robots toward human-level dexterity require robotic hands capable of simultaneously providing high grasping force, rapid actuation speeds, multiple degrees of freedom, and lightweight structures within human-like size constraints. Meeting these conflicting requirements remains challenging, as satisfying this combination typically necessitates heavier actuators and bulkier transmission systems, significantly restricting the payload capacity of robot arms. In this letter, we present a lightweight anthropomorphic hand actuated by Bowden cables, which uniquely combines rolling-contact joint optimization with antagonistic cable actuation, enabling single-motor-per-joint control with negligible cable-length deviation. By relocating the actuator module to the torso, the design substantially reduces distal mass while maintaining anthropomorphic scale and dexterity. Additionally, this antagonistic cable actuation eliminates the need for synchronization between motors. Using the proposed methods, the hand assembly with a distal mass of 236g (excluding remote actuators and Bowden sheaths) demonstrated reliable execution of dexterous tasks, exceeding 18N fingertip force and lifting payloads over one hundred times its own mass. Furthermore, robustness was validated through Cutkosky taxonomy grasps and trajectory consistency under perturbed actuator-hand transformations.

