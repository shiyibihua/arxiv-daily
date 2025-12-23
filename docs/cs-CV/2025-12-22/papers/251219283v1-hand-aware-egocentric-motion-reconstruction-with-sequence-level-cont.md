---
layout: default
title: Hand-Aware Egocentric Motion Reconstruction with Sequence-Level Context
---

# Hand-Aware Egocentric Motion Reconstruction with Sequence-Level Context

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19283" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19283v1</a>
  <a href="https://arxiv.org/pdf/2512.19283.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19283v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19283v1', 'Hand-Aware Egocentric Motion Reconstruction with Sequence-Level Context')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kyungwon Cho, Hanbyul Joo

**分类**: cs.CV

**发布日期**: 2025-12-22

**备注**: Project Page: https://kyungwoncho.github.io/HaMoS/

---

## 💡 一句话要点

**提出HaMoS：一种手部感知的序列级自中心运动重建扩散框架**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `自中心视觉` `运动重建` `手部感知` `序列建模` `扩散模型`

## 📋 核心要点

1. 现有自中心运动重建方法依赖头部轨迹或假设连续手部跟踪，在实际应用中存在模糊性和不现实性。
2. HaMoS框架利用头部轨迹和间歇性可见的手部线索，结合序列级上下文信息，实现更准确的运动重建。
3. 通过新颖的数据增强方法和局部注意力机制，HaMoS在公共基准上取得了state-of-the-art的准确性和时间平滑性。

## 📝 摘要（中文）

自中心视觉系统日益普及，为人机交互创造了新机遇。一个核心挑战是从第一人称视频中估计穿戴者的全身运动，这对于理解人类行为至关重要。然而，这项任务很困难，因为大部分身体部位在自中心视角下是不可见的。先前的方法主要依赖于头部轨迹，导致模糊性，或者假设连续跟踪手部，这对于轻量级自中心设备是不现实的。本文提出了HaMoS，这是第一个手部感知的序列级扩散框架，它直接以头部轨迹和因视场限制和遮挡而间歇性可见的手部线索为条件，就像在真实的自中心设备中一样。为了克服缺乏将多样相机视角与人体运动配对的数据集的问题，我们引入了一种新的增强方法，该方法模拟了这种真实世界的条件。我们还证明了诸如体型和视场之类的序列级上下文对于准确的运动重建至关重要，因此采用局部注意力来有效地推断长序列。在公共基准上的实验表明，我们的方法实现了最先进的准确性和时间平滑性，展示了朝着可靠的野外自中心3D运动理解迈出的实际一步。

## 🔬 方法详解

**问题定义**：论文旨在解决从自中心视角视频中准确重建人体全身运动的问题。现有方法要么依赖不准确的头部轨迹，要么假设不现实的连续手部跟踪，无法很好地处理真实场景中手部遮挡和视场限制等问题。

**核心思路**：论文的核心思路是利用间歇性可见的手部信息作为补充，结合头部轨迹，并引入序列级上下文信息（如体型和视场），来更准确地推断全身运动。通过扩散模型，将这些信息融合在一起，实现鲁棒的运动重建。

**技术框架**：HaMoS框架主要包含以下几个模块：1) 特征提取模块，用于提取头部轨迹和手部关键点的特征；2) 序列建模模块，利用局部注意力机制对序列级上下文进行建模；3) 扩散模型，将提取的特征和上下文信息作为条件，生成人体运动序列。框架采用了一种新颖的数据增强方法，模拟真实场景中的手部遮挡和视场限制。

**关键创新**：论文的关键创新在于：1) 提出了手部感知的自中心运动重建方法，充分利用了间歇性可见的手部信息；2) 引入了序列级上下文信息，提高了运动重建的准确性；3) 设计了一种新的数据增强方法，模拟真实场景中的手部遮挡和视场限制。

**关键设计**：论文的关键设计包括：1) 局部注意力机制，用于高效地建模长序列上下文；2) 扩散模型，用于生成高质量的运动序列；3) 数据增强策略，通过随机遮挡手部和改变视场来模拟真实场景。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19283v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19283v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19283v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

HaMoS在公共基准测试中取得了state-of-the-art的性能，显著提高了自中心运动重建的准确性和时间平滑性。实验结果表明，该方法能够有效地处理手部遮挡和视场限制等问题，在真实场景中具有良好的鲁棒性。具体性能数据和对比基线信息未在摘要中详细给出，需查阅论文全文。

## 🎯 应用场景

该研究成果可应用于人机交互、虚拟现实、增强现实等领域。通过准确重建用户在自中心视角下的全身运动，可以实现更自然、更沉浸式的交互体验。例如，在VR游戏中，可以根据用户的真实运动来控制虚拟角色的行为。此外，该技术还可以用于运动分析、健康监测等领域。

## 📄 摘要（原文）

> Egocentric vision systems are becoming widely available, creating new opportunities for human-computer interaction. A core challenge is estimating the wearer's full-body motion from first-person videos, which is crucial for understanding human behavior. However, this task is difficult since most body parts are invisible from the egocentric view. Prior approaches mainly rely on head trajectories, leading to ambiguity, or assume continuously tracked hands, which is unrealistic for lightweight egocentric devices. In this work, we present HaMoS, the first hand-aware, sequence-level diffusion framework that directly conditions on both head trajectory and intermittently visible hand cues caused by field-of-view limitations and occlusions, as in real-world egocentric devices. To overcome the lack of datasets pairing diverse camera views with human motion, we introduce a novel augmentation method that models such real-world conditions. We also demonstrate that sequence-level contexts such as body shape and field-of-view are crucial for accurate motion reconstruction, and thus employ local attention to infer long sequences efficiently. Experiments on public benchmarks show that our method achieves state-of-the-art accuracy and temporal smoothness, demonstrating a practical step toward reliable in-the-wild egocentric 3D motion understanding.

