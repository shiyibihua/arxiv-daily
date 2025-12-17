---
layout: default
title: Expanding the Workspace of Electromagnetic Navigation Systems Using Dynamic Feedback for Single- and Multi-agent Control
---

# Expanding the Workspace of Electromagnetic Navigation Systems Using Dynamic Feedback for Single- and Multi-agent Control

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.18486" target="_blank" class="toolbar-btn">arXiv: 2511.18486v1</a>
    <a href="https://arxiv.org/pdf/2511.18486.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18486v1" 
            onclick="toggleFavorite(this, '2511.18486v1', 'Expanding the Workspace of Electromagnetic Navigation Systems Using Dynamic Feedback for Single- and Multi-agent Control')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Jasan Zughaibi, Denis von Arx, Maurus Derungs, Florian Heemeyer, Luca A. Antonelli, Quentin Boehler, Michael Muehlebach, Bradley J. Nelson

**分类**: cs.RO, eess.SY

**发布日期**: 2025-11-23

---

## 💡 一句话要点

**利用动态反馈扩展电磁导航系统工作空间，实现单/多智能体控制**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `电磁导航系统` `磁操纵` `动态反馈控制` `多智能体控制` `工作空间扩展`

## 📋 核心要点

1. 电磁导航系统(eMNS)在外科手术中应用受限，主要挑战在于功率和热限制导致有效工作空间狭小。
2. 论文提出系统级控制设计，通过运动目标优化、能量最优电流分配、动态反馈等方法，显著降低所需电流。
3. 实验结果表明，该方法能以更低电流稳定3D倒立摆，并扩展到多智能体控制，在临床eMNS上验证了工作空间扩展。

## 📝 摘要（中文）

电磁导航系统(eMNS)在磁引导外科手术中具有广泛应用。然而，磁操纵手术工具的一个挑战是eMNS的有效工作空间通常受到功率和热限制的严重约束。本文表明，通过降低实现期望运动所需的电流，系统级控制设计可以显著扩展该工作空间。我们确定了五个关键的系统方法来实现这一扩展：(i)以运动为中心的扭矩/力目标，(ii)能量最优电流分配，(iii)实时姿态估计，(iv)动态反馈，以及(v)高带宽eMNS组件。通过用以运动为中心的扭矩/力方法取代以场为中心的场对齐策略，我们使用显著更低的电流（0.1-0.2 A vs. 8-14 A）在八线圈OctoMag eMNS上稳定了一个3D倒立摆。通过利用磁场非线性和线圈冗余进行独立驱动，我们将该方法推广到多智能体控制，在共享工作空间内同时稳定两个倒立摆。结构化分析比较了两种范例的电磁工作空间，并检查了将运动目标映射到线圈电流的电流分配策略。对临床导向的Navion eMNS的跨平台评估进一步证明了显著的工作空间扩展，在距离线圈高达50厘米的距离上保持稳定的平衡。结果表明，反馈是可扩展、高效且与临床相关的磁操纵的实用途径。

## 🔬 方法详解

**问题定义**：电磁导航系统(eMNS)在磁操纵手术工具时，由于功率和热限制，其有效工作空间受到严重约束。现有的场对齐策略需要较高的电流，导致能量效率低，限制了eMNS的应用范围。

**核心思路**：论文的核心思路是通过系统级的控制设计，优化电流分配，降低实现期望运动所需的电流。这包括采用以运动为中心的扭矩/力目标，能量最优电流分配，实时姿态估计，动态反馈以及使用高带宽eMNS组件。

**技术框架**：整体框架包括以下几个关键模块：1) 运动目标设定：根据期望的运动轨迹或姿态，设定扭矩/力目标。2) 电流分配：使用能量最优的电流分配策略，将扭矩/力目标映射到各个线圈的电流。3) 姿态估计：通过传感器或视觉系统实时估计被操纵物体的姿态。4) 动态反馈：利用姿态估计结果，通过反馈控制调整电流分配，实现稳定控制。5) 电磁系统：使用高带宽的电磁系统，以实现快速响应和精确控制。

**关键创新**：最重要的创新在于将传统的以场为中心的场对齐策略，转变为以运动为中心的扭矩/力方法。这种方法能够更有效地利用电磁场的非线性特性和线圈冗余，从而降低所需的电流，扩展工作空间。此外，多智能体控制的实现，展示了该方法在复杂场景下的应用潜力。

**关键设计**：在电流分配方面，论文采用了能量最优的策略，即最小化线圈电流的平方和，以降低功率损耗。在动态反馈方面，使用了PID控制器或更高级的控制算法，根据姿态误差调整电流分配。对于多智能体控制，利用磁场非线性和线圈冗余，设计了解耦控制策略，实现对每个智能体的独立控制。

## 📊 实验亮点

实验结果表明，通过采用以运动为中心的扭矩/力方法，所需的电流从8-14A降低到0.1-0.2A，显著降低了功率消耗。在临床导向的Navion eMNS上，实现了在距离线圈高达50厘米的距离上保持稳定的平衡，验证了工作空间的显著扩展。同时，成功实现了两个倒立摆的同步稳定控制，展示了多智能体控制的能力。

## 🎯 应用场景

该研究成果可应用于微创手术、药物递送、细胞操纵等领域。通过扩展电磁导航系统的工作空间，可以实现更精确、更灵活的磁操纵，提高手术的成功率和安全性。未来，该技术有望应用于远程手术、康复机器人等领域，具有广阔的应用前景。

## 📄 摘要（原文）

> Electromagnetic navigation systems (eMNS) enable a number of magnetically guided surgical procedures. A challenge in magnetically manipulating surgical tools is that the effective workspace of an eMNS is often severely constrained by power and thermal limits. We show that system-level control design significantly expands this workspace by reducing the currents needed to achieve a desired motion. We identified five key system approaches that enable this expansion: (i) motion-centric torque/force objectives, (ii) energy-optimal current allocation, (iii) real-time pose estimation, (iv) dynamic feedback, and (v) high-bandwidth eMNS components. As a result, we stabilize a 3D inverted pendulum on an eight-coil OctoMag eMNS with significantly lower currents (0.1-0.2 A vs. 8-14 A), by replacing a field-centric field-alignment strategy with a motion-centric torque/force-based approach. We generalize to multi-agent control by simultaneously stabilizing two inverted pendulums within a shared workspace, exploiting magnetic-field nonlinearity and coil redundancy for independent actuation. A structured analysis compares the electromagnetic workspaces of both paradigms and examines current-allocation strategies that map motion objectives to coil currents. Cross-platform evaluation of the clinically oriented Navion eMNS further demonstrates substantial workspace expansion by maintaining stable balancing at distances up to 50 cm from the coils. The results demonstrate that feedback is a practical path to scalable, efficient, and clinically relevant magnetic manipulation.

