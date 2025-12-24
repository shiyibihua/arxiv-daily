---
layout: default
title: Whole-Body Coordination for Dynamic Object Grasping with Legged Manipulators
---

# Whole-Body Coordination for Dynamic Object Grasping with Legged Manipulators

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08328" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08328v1</a>
  <a href="https://arxiv.org/pdf/2508.08328.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08328v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08328v1', 'Whole-Body Coordination for Dynamic Object Grasping with Legged Manipulators')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qiwei Liang, Boyang Cai, Rongyi He, Hui Li, Tao Teng, Haihan Duan, Changxin Huang, Runhao Zeng

**分类**: cs.RO

**发布日期**: 2025-08-10

---

## 💡 一句话要点

**提出DQ-Net以解决动态物体抓取问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `动态抓取` `四足机器人` `教师-学生框架` `基准评估` `运动规划`

## 📋 核心要点

1. 现有研究主要集中于静态物体抓取，忽视了动态目标的挑战，限制了在动态场景中的应用。
2. 提出DQ-Bench基准和DQ-Net框架，通过教师网络和学生网络的协同工作，推断抓取配置。
3. 实验结果表明，DQ-Net在动态物体抓取任务中表现出色，成功率和响应速度显著提高。

## 📝 摘要（中文）

四足机器人配备操控器在动态环境中具备强大的移动性和适应性，但现有研究主要集中于静态物体抓取，忽视了动态目标带来的挑战。为此，本文提出了DQ-Bench，一个系统评估动态抓取的新基准，涵盖不同物体运动、速度、高度、类型和地形复杂性。基于此基准，提出了DQ-Net，一个紧凑的教师-学生框架，旨在从有限的感知线索中推断抓取配置。通过大量实验，DQ-Net在多个任务设置中实现了动态物体抓取的鲁棒性，显著超越了基线方法。

## 🔬 方法详解

**问题定义**：本文旨在解决四足机器人在动态环境中抓取动态物体的挑战。现有方法多集中于静态物体抓取，缺乏对动态目标的有效处理，限制了其在实际应用中的适用性。

**核心思路**：论文提出DQ-Bench基准和DQ-Net框架，利用教师网络提供的特权信息来全面建模目标的几何特性和动态运动特征，同时设计轻量级的学生网络以实现闭环动作输出。

**技术框架**：DQ-Net由教师网络和学生网络组成。教师网络使用特权信息进行训练，整合抓取融合模块以提供运动规划的指导；学生网络则依赖目标掩码、深度图和自我感知状态进行双视角时间建模。

**关键创新**：DQ-Bench作为新基准系统地评估动态抓取，DQ-Net通过教师-学生框架有效推断抓取配置，显著提升了动态物体抓取的成功率和响应速度。

**关键设计**：教师网络整合了静态几何属性和动态运动特征，学生网络则设计为轻量级，能够在不依赖特权数据的情况下进行有效的抓取决策。

## 📊 实验亮点

在DQ-Bench基准上进行的广泛实验表明，DQ-Net在动态物体抓取任务中显著优于基线方法，成功率和响应速度均有显著提升，具体性能数据未提供，但提升幅度明显。

## 🎯 应用场景

该研究的潜在应用领域包括物流分拣、人与机器人协作等动态场景。通过提升四足机器人在动态环境中的抓取能力，能够更好地满足实际应用需求，推动智能机器人在复杂环境中的广泛应用。

## 📄 摘要（原文）

> Quadrupedal robots with manipulators offer strong mobility and adaptability for grasping in unstructured, dynamic environments through coordinated whole-body control. However, existing research has predominantly focused on static-object grasping, neglecting the challenges posed by dynamic targets and thus limiting applicability in dynamic scenarios such as logistics sorting and human-robot collaboration. To address this, we introduce DQ-Bench, a new benchmark that systematically evaluates dynamic grasping across varying object motions, velocities, heights, object types, and terrain complexities, along with comprehensive evaluation metrics. Building upon this benchmark, we propose DQ-Net, a compact teacher-student framework designed to infer grasp configurations from limited perceptual cues. During training, the teacher network leverages privileged information to holistically model both the static geometric properties and dynamic motion characteristics of the target, and integrates a grasp fusion module to deliver robust guidance for motion planning. Concurrently, we design a lightweight student network that performs dual-viewpoint temporal modeling using only the target mask, depth map, and proprioceptive state, enabling closed-loop action outputs without reliance on privileged data. Extensive experiments on DQ-Bench demonstrate that DQ-Net achieves robust dynamic objects grasping across multiple task settings, substantially outperforming baseline methods in both success rate and responsiveness.

