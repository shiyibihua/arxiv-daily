---
layout: default
title: A Force Feedback Exoskeleton for Teleoperation Using Magnetorheological Clutches
---

# A Force Feedback Exoskeleton for Teleoperation Using Magnetorheological Clutches

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15124" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15124v1</a>
  <a href="https://arxiv.org/pdf/2506.15124.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15124v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15124v1', 'A Force Feedback Exoskeleton for Teleoperation Using Magnetorheological Clutches')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhongyuan Kong, Lei Li, Erwin Ang Tien Yew, Zirui Chen, Wenbo Li, Shiwu Zhang, Jian Yang, Shuaishuai Sun

**分类**: eess.SY

**发布日期**: 2025-06-18

---

## 💡 一句话要点

**提出基于磁流变离合器的半主动力反馈外骨骼以提升遥操作精度**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `外骨骼` `遥操作` `磁流变离合器` `力反馈` `深空探测` `机器人技术` `虚拟现实`

## 📋 核心要点

1. 现有的外骨骼遥操作系统多依赖于电机驱动，导致系统复杂且能耗高，且存在安全隐患。
2. 本文提出了一种基于磁流变离合器的半主动力反馈策略，通过动态磁场控制实现关节刚度和阻尼的精确调节。
3. 实验结果表明，该系统在力反馈方面表现出色，扭矩质量比达到93.6 Nm/kg，相较于以往设计提升约246%。

## 📝 摘要（中文）

本文提出了一种基于磁流变（MR）离合器的上肢外骨骼遥操作系统，旨在提高月球采样任务中的操作精度和沉浸体验。传统的外骨骼遥操作系统通常采用主动力反馈解决方案，如伺服电机，这些方案通常面临系统复杂性高和能耗增加的问题。此外，利用电机和齿轮减速器的力反馈设备通常会妨碍反驱动性，并对操作员构成安全风险。为了解决这些局限性，本文提出了一种基于MR离合器的半主动力反馈策略。动态磁场控制使关节刚度和阻尼的精确调整成为可能，从而提供平滑且高分辨率的力反馈。实验结果验证了该系统提供高保真力反馈的能力，展现了其在深空遥操作中的应用潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决传统外骨骼遥操作系统在复杂性、能耗和安全性方面的不足，尤其是主动力反馈方案带来的挑战。

**核心思路**：提出一种基于磁流变离合器的半主动力反馈策略，通过动态调整磁场来控制关节的刚度和阻尼，从而实现高精度的力反馈。

**技术框架**：系统主要包括磁流变离合器、控制模块和反馈机制。控制模块负责动态调节磁场，以实现对关节力反馈的实时控制。

**关键创新**：最重要的创新在于采用磁流变离合器替代传统电机驱动，显著提高了扭矩质量比和系统的反驱动性，降低了能耗和安全风险。

**关键设计**：设计中优化了磁流变离合器的参数设置，确保其在不同工作状态下都能提供稳定的力反馈，具体包括扭矩质量比93.6 Nm/kg和扭矩体积比4.05 x 10^5 Nm/m^3等关键指标。

## 📊 实验亮点

实验结果显示，所设计的MR离合器在关键性能指标上表现优异，扭矩质量比达到93.6 Nm/kg，相较于以往设计提升约246%。该系统能够提供高保真的力反馈，验证了其在深空遥操作中的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括深空探测、机器人手术和虚拟现实等场景，能够为遥操作任务提供更高的安全性和操作精度，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> This paper proposes an upper-limb exoskeleton teleoperation system based on magnetorheological (MR) clutches, aiming to improve operational accuracy and enhance the immersive experience during lunar sampling tasks. Conventional exoskeleton teleoperation systems commonly employ active force feedback solutions, such as servo motors, which typically suffer from high system complexity and increased energy consumption. Furthermore, force feedback devices utilizing motors and gear reducers generally compromise backdrivability and pose safety risks to operators due to active force output. To address these limitations, we propose a semi-active force feedback strategy based on MR clutches. Dynamic magnetic field control enables precise adjustment of joint stiffness and damping, thereby providing smooth and high-resolution force feedback. The designed MR clutch exhibits outstanding performance across key metrics, achieving a torque-to-mass ratio (TMR) of 93.6 Nm/kg, a torque-to-volume ratio (TVR) of 4.05 x 10^5 Nm/m^3, and a torque-to-power ratio (TPR) of 4.15 Nm/W. Notably, the TMR represents an improvement of approximately 246% over a representative design in prior work. Experimental results validate the system's capability to deliver high-fidelity force feedback. Overall, the proposed system presents a promising solution for deep-space teleoperation with strong potential for real-world deployment in future missions.

