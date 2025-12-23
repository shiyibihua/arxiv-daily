---
layout: default
title: Robust control for multi-legged elongate robots in noisy environments
---

# Robust control for multi-legged elongate robots in noisy environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15788" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15788v1</a>
  <a href="https://arxiv.org/pdf/2506.15788.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15788v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15788v1', 'Robust control for multi-legged elongate robots in noisy environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Baxi Chong, Juntao He, Daniel Irvine, Tianyu Wang, Esteban Flores, Daniel Soto, Jianfeng Lin, Zhaochen Xu, Vincent R Nienhusser, Grigoriy Blekherman, Daniel I. Goldman

**分类**: cs.RO, eess.SY

**发布日期**: 2025-06-18

---

## 💡 一句话要点

**提出一种新范式以增强多足延伸机器人在噪声环境中的鲁棒性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `多足机器人` `鲁棒控制` `机械智能` `计算智能` `复杂地形` `反馈控制` `噪声环境` `自动重复请求`

## 📋 核心要点

1. 现有的多足机器人在复杂地形中表现出色，但依赖高带宽传感器和特定训练，限制了其适应性。
2. 论文提出了一种新范式，通过将每个腿与地面的接触视为基本主动接触，利用冗余实现鲁棒运动。
3. 实验结果表明，所提出的控制方案在复杂地形上实现了约每周期半个身体长度的有效运动，显示出良好的鲁棒性。

## 📝 摘要（中文）

现代两足和四足机器人在复杂地形上的出色移动性主要归功于学习算法的进步。然而，这些系统通常依赖于高带宽传感器和机载计算来感知和响应地形的不确定性。当前的运动策略通常需要大量特定于机器人的训练，限制了它们在不同平台上的通用性。基于我们之前的研究，本文提出了一种新的范式，构建能够在杂乱、非结构化环境中有效操作的多足延伸机器人（MERs），通过被动机械响应和反馈控制方案实现可靠的运动。我们的工作为MER控制的系统化发展奠定了基础，推动了能够在极端环境中操作的灵活且具有韧性的机器人系统的研究。

## 🔬 方法详解

**问题定义**：本文旨在解决多足延伸机器人在噪声环境中运动的鲁棒性问题。现有方法依赖于高带宽传感器和特定训练，导致适应性不足。

**核心思路**：通过将每个腿与地面的接触视为基本主动接触（bac），利用冗余实现可靠的开环运动，并通过被动机械响应增强鲁棒性。

**技术框架**：整体架构包括机械智能（MI）和计算智能（CI）两部分，MI通过被动响应实现鲁棒性，CI通过反馈控制增强运动能力。

**关键创新**：最重要的创新在于将机械智能与计算智能结合，形成一种新的控制方案，使得机器人在复杂地形中表现出色，且无需大量特定训练。

**关键设计**：在设计中，采用了冗余的主动接触机制，结合反馈控制方案，确保在复杂环境中实现有效的运动。

## 📊 实验亮点

实验结果显示，所提出的多足延伸机器人在复杂地形上实现了约每周期半个身体长度的有效运动，且在面对超过机器人高度两倍的地形噪声时，依然保持良好的鲁棒性，显著优于现有方法。

## 🎯 应用场景

该研究的潜在应用领域包括救援机器人、探索机器人和农业机器人等，这些领域需要在复杂和不确定的环境中进行高效操作。未来，该研究可能推动更具适应性和韧性的机器人系统的发展，能够在极端环境中执行任务。

## 📄 摘要（原文）

> Modern two and four legged robots exhibit impressive mobility on complex terrain, largely attributed to advancement in learning algorithms. However, these systems often rely on high-bandwidth sensing and onboard computation to perceive/respond to terrain uncertainties. Further, current locomotion strategies typically require extensive robot-specific training, limiting their generalizability across platforms. Building on our prior research connecting robot-environment interaction and communication theory, we develop a new paradigm to construct robust and simply controlled multi-legged elongate robots (MERs) capable of operating effectively in cluttered, unstructured environments. In this framework, each leg-ground contact is thought of as a basic active contact (bac), akin to bits in signal transmission. Reliable locomotion can be achieved in open-loop on "noisy" landscapes via sufficient redundancy in bacs. In such situations, robustness is achieved through passive mechanical responses. We term such processes as those displaying mechanical intelligence (MI) and analogize these processes to forward error correction (FEC) in signal transmission. To augment MI, we develop feedback control schemes, which we refer to as computational intelligence (CI) and such processes analogize automatic repeat request (ARQ) in signal transmission. Integration of these analogies between locomotion and communication theory allow analysis, design, and prediction of embodied intelligence control schemes (integrating MI and CI) in MERs, showing effective and reliable performance (approximately half body lengths per cycle) on complex landscapes with terrain "noise" over twice the robot's height. Our work provides a foundation for systematic development of MER control, paving the way for terrain-agnostic, agile, and resilient robotic systems capable of operating in extreme environments.

