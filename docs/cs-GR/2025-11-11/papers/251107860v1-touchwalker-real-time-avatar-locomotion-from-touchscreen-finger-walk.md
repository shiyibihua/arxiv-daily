---
layout: default
title: TouchWalker: Real-Time Avatar Locomotion from Touchscreen Finger Walking
---

# TouchWalker: Real-Time Avatar Locomotion from Touchscreen Finger Walking

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.07860" target="_blank" class="toolbar-btn">arXiv: 2511.07860v1</a>
    <a href="https://arxiv.org/pdf/2511.07860.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.07860v1" 
            onclick="toggleFavorite(this, '2511.07860v1', 'TouchWalker: Real-Time Avatar Locomotion from Touchscreen Finger Walking')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Geuntae Park, Jiwon Yi, Taehyun Rhee, Kwanguk Kim, Yoonsang Lee

**分类**: cs.HC, cs.GR

**发布日期**: 2025-11-11

**备注**: Accepted to ISMAR 2025

---

## 💡 一句话要点

**TouchWalker：提出一种基于触摸屏手指行走的实时全身Avatar运动控制系统**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `Avatar控制` `运动生成` `触摸屏交互` `深度学习` `MoE-GRU` `实时系统`

## 📋 核心要点

1. 现有Avatar控制方法依赖预定义动作或复杂手势，缺乏连续性和实时性，难以实现自然流畅的全身运动控制。
2. TouchWalker利用神经运动生成器MotionNet，从稀疏双指输入逐帧合成全身运动，实现连续、上下文感知的Avatar控制。
3. 用户研究表明，TouchWalker在具身感、乐趣和沉浸感方面优于虚拟摇杆基线，提升了用户体验。

## 📝 摘要（中文）

本文提出TouchWalker，一个利用触摸屏手指行走手势实时控制全身Avatar运动的系统。该系统包含两个主要组成部分：TouchWalker-MotionNet，一个神经运动生成器，它基于时间上稀疏的双指输入，逐帧合成全身Avatar运动；以及TouchWalker-UI，一个紧凑的触摸界面，它将用户的触摸输入解释为Avatar相对的脚部位置。与依赖符号手势触发或预定义运动序列的现有系统不同，TouchWalker利用其神经组件逐帧生成连续的、上下文感知的全身运动——包括跑步等空中阶段，即使在空中步进期间没有输入也能实现——从而实现更具表现力和即时性的交互。为了确保手指接触和Avatar运动之间的精确对齐，它采用了一种具有专用足部对齐损失的MoE-GRU架构。我们在用户研究中评估了TouchWalker，并将其与具有预定义运动的虚拟摇杆基线在不同的运动任务中进行了比较。结果表明，TouchWalker提高了用户的具身感、乐趣和沉浸感。

## 🔬 方法详解

**问题定义**：现有Avatar运动控制方法，如虚拟摇杆或基于手势的控制，通常依赖于预定义的动作序列或离散的手势触发。这些方法缺乏连续性和实时性，难以生成自然流畅的全身运动，尤其是在空中阶段，例如跑步时的跳跃。此外，用户难以直观地控制Avatar的脚部位置，导致控制精度和沉浸感不足。

**核心思路**：TouchWalker的核心思路是利用深度学习模型，从触摸屏上的双指行走手势直接生成连续的全身Avatar运动。通过学习手指运动与Avatar运动之间的映射关系，系统能够根据用户的触摸输入实时合成自然的运动，包括空中阶段。这种方法避免了预定义动作的限制，实现了更具表现力和灵活性的控制。

**技术框架**：TouchWalker系统包含两个主要模块：TouchWalker-MotionNet和TouchWalker-UI。TouchWalker-UI负责将用户的触摸输入转换为Avatar相对的脚部位置。TouchWalker-MotionNet是一个神经运动生成器，它接收来自TouchWalker-UI的脚部位置信息，并逐帧生成全身Avatar运动。MotionNet采用MoE-GRU架构，能够处理时间序列数据，并生成连续的运动。

**关键创新**：TouchWalker的关键创新在于其神经运动生成器MotionNet能够从稀疏的触摸输入生成连续的全身运动，包括空中阶段。与传统的基于规则或预定义动作的方法不同，MotionNet能够学习复杂的运动模式，并根据用户的输入实时生成自然的运动。此外，系统还引入了足部对齐损失，以确保手指接触和Avatar运动之间的精确对齐。

**关键设计**：MotionNet采用MoE-GRU架构，其中MoE（Mixture of Experts）用于处理不同的运动模式，GRU（Gated Recurrent Unit）用于处理时间序列数据。足部对齐损失用于约束生成的运动，使其与用户的触摸输入保持一致。具体来说，损失函数惩罚了Avatar脚部位置与用户手指位置之间的差异。此外，系统还采用了数据增强技术，以提高模型的泛化能力。

## 📊 实验亮点

用户研究表明，TouchWalker在具身感、乐趣和沉浸感方面显著优于虚拟摇杆基线。具体来说，用户在使用TouchWalker时，对Avatar的控制感更强，感觉更像是自己在虚拟世界中行走。此外，用户也更喜欢使用TouchWalker进行运动控制，认为它更有趣、更自然。

## 🎯 应用场景

TouchWalker可应用于虚拟现实、游戏、远程协作等领域，为用户提供更自然、沉浸式的Avatar控制体验。例如，在VR游戏中，用户可以通过手指行走控制Avatar的移动，从而获得更强的具身感。在远程协作中，用户可以通过Avatar进行更生动的交流和互动。该技术还可用于康复训练，帮助患者恢复运动能力。

## 📄 摘要（原文）

> We present TouchWalker, a real-time system for controlling full-body avatar locomotion using finger-walking gestures on a touchscreen. The system comprises two main components: TouchWalker-MotionNet, a neural motion generator that synthesizes full-body avatar motion on a per-frame basis from temporally sparse two-finger input, and TouchWalker-UI, a compact touch interface that interprets user touch input to avatar-relative foot positions. Unlike prior systems that rely on symbolic gesture triggers or predefined motion sequences, TouchWalker uses its neural component to generate continuous, context-aware full-body motion on a per-frame basis-including airborne phases such as running, even without input during mid-air steps-enabling more expressive and immediate interaction. To ensure accurate alignment between finger contacts and avatar motion, it employs a MoE-GRU architecture with a dedicated foot-alignment loss. We evaluate TouchWalker in a user study comparing it to a virtual joystick baseline with predefined motion across diverse locomotion tasks. Results show that TouchWalker improves users' sense of embodiment, enjoyment, and immersion.

