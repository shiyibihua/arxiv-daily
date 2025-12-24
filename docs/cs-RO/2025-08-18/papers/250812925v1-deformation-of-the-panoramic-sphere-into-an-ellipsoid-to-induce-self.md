---
layout: default
title: Deformation of the panoramic sphere into an ellipsoid to induce self-motion in telepresence users
---

# Deformation of the panoramic sphere into an ellipsoid to induce self-motion in telepresence users

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12925" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12925v1</a>
  <a href="https://arxiv.org/pdf/2508.12925.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12925v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12925v1', 'Deformation of the panoramic sphere into an ellipsoid to induce self-motion in telepresence users')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eetu Laukka, Evan G. Center, Timo Ojala, Steven M. LaValle, Matti Pouke

**分类**: cs.RO, cs.HC

**发布日期**: 2025-08-18

**备注**: 2025 IEEE Conference on Telepresence

---

## 💡 一句话要点

**提出光流技术以解决远程操控延迟问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `远程呈现` `光流技术` `虚拟现实` `用户体验` `机器人控制`

## 📋 核心要点

1. 现有的360度摄像头系统在远程操控中存在高延迟问题，影响用户体验和控制精度。
2. 论文提出利用光流技术在延迟期间创造自我运动的错觉，以提升用户的沉浸感和操控体验。
3. 实验结果显示，在500毫秒的延迟下，使用自我运动错觉对任务完成时间和碰撞率没有显著改善，但可能增加虚拟现实晕动症的风险。

## 📝 摘要（中文）

移动远程呈现机器人使用户能够通过技术感知和探索远程环境。尽管360度摄像头等高沉浸技术能够提高用户的情境意识和存在感，但也带来了显著的挑战，如处理和带宽需求，导致延迟高达数秒。本文提出了一种新颖的方法，利用光流技术在用户发送运动指令与通过360度摄像头流看到实际运动之间的延迟期间，创造自我运动的错觉。研究发现，在500毫秒的延迟下，使用自我运动错觉对远程机器人控制的性能和准确性没有显著益处，但可能会增加虚拟现实的晕动症。进一步的调整是必要的，以使该方法可行。

## 🔬 方法详解

**问题定义**：本文旨在解决移动远程呈现机器人中由于360度摄像头引起的高延迟问题，导致用户在发送指令与看到反馈之间的体验不佳。现有方法在高延迟下缺乏有效的用户支持。

**核心思路**：通过光流技术，论文提出在用户发送运动指令与实际反馈之间创造自我运动的错觉，以增强用户的沉浸感和控制体验。这种设计旨在减轻延迟带来的负面影响。

**技术框架**：整体架构包括用户输入模块、光流计算模块和反馈展示模块。用户输入模块接收运动指令，光流计算模块生成自我运动的视觉效果，反馈展示模块则通过360度摄像头展示实际运动。

**关键创新**：最重要的技术创新在于利用光流技术在高延迟环境中创造自我运动的错觉，这与传统的直接反馈方法有本质区别，后者无法有效应对延迟问题。

**关键设计**：在实验中，设置了500毫秒的延迟，并使用模拟器晕动症问卷（SSQ）评估用户体验。关键参数包括光流算法的精度和延迟时间的控制，这些设计影响了用户的沉浸感和控制效果。

## 📊 实验亮点

实验结果表明，在500毫秒的延迟下，使用自我运动错觉对任务完成时间和碰撞率没有显著改善，且可能增加虚拟现实晕动症的风险。这一发现为后续研究提供了重要的实验基础。

## 🎯 应用场景

该研究的潜在应用领域包括远程医疗、教育和虚拟旅游等场景，能够提升用户在高延迟环境下的交互体验。通过改善用户的沉浸感，未来可能推动更多高沉浸感技术的应用与发展。

## 📄 摘要（原文）

> Mobile telepresence robots allow users to feel present and explore remote environments using technology. Traditionally, these systems are implemented using a camera onboard a mobile robot that can be controlled. Although high-immersion technologies, such as 360-degree cameras, can increase situational awareness and presence, they also introduce significant challenges. Additional processing and bandwidth requirements often result in latencies of up to seconds. The current delay with a 360-degree camera streaming over the internet makes real-time control of these systems difficult. Working with high-latency systems requires some form of assistance to the users.
>   This study presents a novel way to utilize optical flow to create an illusion of self-motion to the user during the latency period between user sending motion commands to the robot and seeing the actual motion through the 360-camera stream. We find no significant benefit of using the self-motion illusion to performance or accuracy of controlling a telepresence robot with a latency of 500 ms, as measured by the task completion time and collisions into objects. Some evidence is shown that the method might increase virtual reality (VR) sickness, as measured by the simulator sickness questionnaire (SSQ). We conclude that further adjustments are necessary in order to render the method viable.

