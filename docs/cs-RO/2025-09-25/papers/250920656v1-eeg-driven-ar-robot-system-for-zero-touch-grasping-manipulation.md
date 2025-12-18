---
layout: default
title: EEG-Driven AR-Robot System for Zero-Touch Grasping Manipulation
---

# EEG-Driven AR-Robot System for Zero-Touch Grasping Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20656" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20656v1</a>
  <a href="https://arxiv.org/pdf/2509.20656.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20656v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20656v1', 'EEG-Driven AR-Robot System for Zero-Touch Grasping Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junzhe Wang, Jiarui Xie, Pengfei Hao, Zheng Li, Yi Cai

**分类**: cs.RO

**发布日期**: 2025-09-25

**备注**: 8 pages, 14 figures, submitted to ICRA 2026

---

## 💡 一句话要点

**提出基于脑电的AR-机器人系统，实现零接触抓取操作，提升运动障碍人士人机交互能力。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `脑机接口` `增强现实` `机器人控制` `运动想象` `辅助机器人` `人机交互` `零接触操作`

## 📋 核心要点

1. 现有脑机接口-机器人系统面临脑电信号噪声大、目标选择不灵活以及缺乏闭环验证等问题，限制了其在辅助场景中的实际应用。
2. 本文提出一种闭环BCI-AR-Robot系统，利用运动想象脑电信号解码、增强现实神经反馈和机器人抓取，实现零接触操作。
3. 实验结果表明，该系统在运动想象训练准确率、信息传输速率和闭环抓取成功率方面均表现出色，验证了AR反馈对脑电控制的稳定作用。

## 📝 摘要（中文）

本文提出了一种闭环脑机接口（BCI）-增强现实（AR）-机器人系统，用于零接触操作。该系统集成了基于运动想象（MI）的脑电信号解码、AR神经反馈和机器人抓取。使用14通道脑电头盔进行个性化的MI校准，基于智能手机的AR界面支持多目标导航，并提供方向一致的反馈以增强稳定性。机器人手臂结合决策输出和基于视觉的姿态估计，实现自主抓取。实验验证了该框架的有效性：MI训练达到93.1%的准确率，平均信息传输速率（ITR）为14.8 bit/min；AR神经反馈显著提高了持续控制能力（SCI = 0.210），并实现了最高的ITR（21.3 bit/min），优于静态、伪反馈和无AR基线；闭环抓取成功率达到97.2%，具有良好的效率和用户控制感。结果表明，AR反馈显著稳定了基于脑电的控制，所提出的框架实现了鲁棒的零接触抓取，推动了辅助机器人应用和未来人机交互模式的发展。

## 🔬 方法详解

**问题定义**：论文旨在解决运动障碍人士在人机交互中面临的挑战，即如何利用脑机接口技术实现对机器人的精确控制，从而完成诸如抓取等操作。现有方法的痛点在于脑电信号的噪声干扰、目标选择的局限性以及缺乏有效的反馈机制，导致控制不稳定且效率低下。

**核心思路**：论文的核心思路是结合增强现实（AR）技术，为用户提供实时的视觉反馈，从而增强脑机接口控制的稳定性和准确性。通过AR界面，用户可以更直观地了解机器人的状态和目标位置，从而更好地调整运动想象，提高控制效果。同时，结合视觉伺服技术，使机器人能够自主完成抓取动作。

**技术框架**：该系统主要包含三个模块：1) 基于运动想象（MI）的脑电信号解码模块，用于识别用户的控制意图；2) 基于智能手机的AR神经反馈模块，为用户提供实时的视觉反馈，增强控制稳定性；3) 机器人抓取模块，结合决策输出和基于视觉的姿态估计，实现自主抓取。整个系统构成一个闭环控制系统，用户通过脑电信号控制机器人，机器人执行动作后，通过AR界面将结果反馈给用户，用户根据反馈调整控制策略。

**关键创新**：该论文的关键创新在于将增强现实技术引入到脑机接口-机器人控制系统中，利用AR界面为用户提供实时的、方向一致的视觉反馈，显著提高了脑电控制的稳定性和信息传输速率。此外，系统还实现了基于视觉的自主抓取，减少了人工干预，提高了操作效率。

**关键设计**：在脑电信号解码方面，采用了14通道脑电头盔进行数据采集，并针对每个用户进行个性化的MI校准。在AR神经反馈方面，设计了方向一致的视觉提示，引导用户进行运动想象。在机器人抓取方面，结合了决策输出和视觉伺服技术，实现了自主抓取。具体参数设置和网络结构等细节未在摘要中详细描述，属于未知信息。

## 📊 实验亮点

实验结果表明，该系统在多个方面取得了显著的性能提升。运动想象训练的准确率达到93.1%，平均信息传输速率（ITR）为14.8 bit/min。AR神经反馈显著提高了持续控制能力（SCI = 0.210），并实现了最高的ITR（21.3 bit/min），优于静态、伪反馈和无AR基线。闭环抓取成功率达到97.2%，表明该系统具有良好的鲁棒性和实用性。

## 🎯 应用场景

该研究成果可应用于辅助机器人领域，帮助运动障碍人士完成日常生活中的各种任务，例如取物、进食等。此外，该技术还可应用于远程操作、危险环境作业等领域，提高操作的安全性和效率。未来，随着脑机接口技术的不断发展，该系统有望成为一种重要的辅助工具，改善人们的生活质量。

## 📄 摘要（原文）

> Reliable brain-computer interface (BCI) control of robots provides an intuitive and accessible means of human-robot interaction, particularly valuable for individuals with motor impairments. However, existing BCI-Robot systems face major limitations: electroencephalography (EEG) signals are noisy and unstable, target selection is often predefined and inflexible, and most studies remain restricted to simulation without closed-loop validation. These issues hinder real-world deployment in assistive scenarios. To address them, we propose a closed-loop BCI-AR-Robot system that integrates motor imagery (MI)-based EEG decoding, augmented reality (AR) neurofeedback, and robotic grasping for zero-touch operation. A 14-channel EEG headset enabled individualized MI calibration, a smartphone-based AR interface supported multi-target navigation with direction-congruent feedback to enhance stability, and the robotic arm combined decision outputs with vision-based pose estimation for autonomous grasping. Experiments are conducted to validate the framework: MI training achieved 93.1 percent accuracy with an average information transfer rate (ITR) of 14.8 bit/min; AR neurofeedback significantly improved sustained control (SCI = 0.210) and achieved the highest ITR (21.3 bit/min) compared with static, sham, and no-AR baselines; and closed-loop grasping achieved a 97.2 percent success rate with good efficiency and strong user-reported control. These results show that AR feedback substantially stabilizes EEG-based control and that the proposed framework enables robust zero-touch grasping, advancing assistive robotic applications and future modes of human-robot interaction.

