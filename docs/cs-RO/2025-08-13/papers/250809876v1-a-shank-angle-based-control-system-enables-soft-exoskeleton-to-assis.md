---
layout: default
title: A Shank Angle-Based Control System Enables Soft Exoskeleton to Assist Human Non-Steady Locomotion
---

# A Shank Angle-Based Control System Enables Soft Exoskeleton to Assist Human Non-Steady Locomotion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09876" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09876v1</a>
  <a href="https://arxiv.org/pdf/2508.09876.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09876v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09876v1', 'A Shank Angle-Based Control System Enables Soft Exoskeleton to Assist Human Non-Steady Locomotion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaowei Tan, Weizhong Jiang, Bi Zhang, Wanxin Chen, Yiwen Zhao, Ning Li, Lianqing Liu, Xingang Zhao

**分类**: cs.RO, eess.SY

**发布日期**: 2025-08-13

**备注**: 49 pages, 20 figures, 4 tables

---

## 💡 一句话要点

**提出基于小腿角度的控制系统以解决非稳态运动辅助问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `外骨骼` `非稳态运动` `控制系统` `生物力学` `实时协调` `辅助技术` `运动康复`

## 📋 核心要点

1. 现有外骨骼技术在非稳态运动中的应用研究不足，尤其是在步态周期内的非线性相位进展方面。
2. 本研究提出了一种基于小腿角度的控制系统，能够实时协调人类步态并动态调整辅助配置，以适应不同的运动任务。
3. 通过多项实验验证了控制系统的有效性，显示出其在应对步态扰动时的鲁棒性和对用户生理反应的积极影响。

## 📝 摘要（中文）

外骨骼已被证明能有效辅助人类在稳态运动中的表现。然而，其在非稳态运动中的效果尚未得到充分探索，尤其是在多样化活动中。本研究提出了一种基于小腿角度的控制系统，使外骨骼能够实时协调人类步态，即使在相位扰动下，也能动态调整辅助配置以匹配生物脚踝的力矩模式。该控制系统包括在线生成辅助配置的方法和基于模型的前馈控制方法。通过仅利用IMU测量，模型参数在每一步中在线更新，以适应个体间和个体内的生物力学变异。实验结果验证了各个方法的有效性，展示了控制系统在各种活动中的鲁棒性，并揭示了人类用户对外骨骼机械辅助的积极生物力学和生理反应。

## 🔬 方法详解

**问题定义**：本研究旨在解决外骨骼在非稳态运动中无法有效辅助的问题。现有方法在应对步态周期内的相位扰动时缺乏灵活性和实时性。

**核心思路**：提出了一种基于小腿角度的控制系统，通过实时生成辅助配置和模型驱动的前馈控制，确保外骨骼与人类步态的协调性。

**技术框架**：该系统包括两个主要模块：一是在线生成辅助配置的方法，二是基于人类-外骨骼运动学和刚度模型的前馈控制。辅助配置采用双高斯模型，独立变量为小腿角度。

**关键创新**：本研究的创新点在于利用IMU测量在线更新模型参数，适应个体间和个体内的生物力学变异，显著减少对历史控制数据的依赖。

**关键设计**：模型参数通过每一步的IMU数据更新，辅助配置采用双高斯模型，前馈控制部分结合了运动学和刚度模型，确保了对非稳态运动的有效适应。

## 📊 实验亮点

实验结果表明，控制系统在面对步态扰动时表现出良好的鲁棒性，能够有效适应多种运动任务。参与者在使用外骨骼时，生物力学和生理反应均显示出积极的改善，验证了系统的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括康复医学、老年人辅助设备以及运动训练等。通过提升外骨骼在非稳态运动中的辅助能力，能够帮助更多人群改善运动能力和生活质量，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> Exoskeletons have been shown to effectively assist humans during steady locomotion. However, their effects on non-steady locomotion, characterized by nonlinear phase progression within a gait cycle, remain insufficiently explored, particularly across diverse activities. This work presents a shank angle-based control system that enables the exoskeleton to maintain real-time coordination with human gait, even under phase perturbations, while dynamically shaping assistance profiles to match the biological ankle moment patterns across walking, running, stair negotiation tasks. The control system consists of an assistance profile online generation method and a model-based feedforward control method. The assistance profile is formulated as a dual-Gaussian model with the shank angle as the independent variable. Leveraging only IMU measurements, the model parameters are updated online each stride to adapt to inter- and intra-individual biomechanical variability. The profile tracking control employs a human-exoskeleton kinematics and stiffness model as a feedforward component, reducing reliance on historical control data due to the lack of clear and consistent periodicity in non-steady locomotion. Three experiments were conducted using a lightweight soft exoskeleton with multiple subjects. The results validated the effectiveness of each individual method, demonstrated the robustness of the control system against gait perturbations across various activities, and revealed positive biomechanical and physiological responses of human users to the exoskeleton's mechanical assistance.

