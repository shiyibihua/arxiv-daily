---
layout: default
title: Learning Generalizable Hand-Object Tracking from Synthetic Demonstrations
---

# Learning Generalizable Hand-Object Tracking from Synthetic Demonstrations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19583" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19583v1</a>
  <a href="https://arxiv.org/pdf/2512.19583.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19583v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19583v1', 'Learning Generalizable Hand-Object Tracking from Synthetic Demonstrations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yinhuai Wang, Runyi Yu, Hok Wai Tsui, Xiaoyi Lin, Hui Zhang, Qihan Zhao, Ke Fan, Miao Li, Jie Song, Jingbo Wang, Qifeng Chen, Ping Tan

**分类**: cs.RO, cs.GR

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**提出HOP+HOT框架，仅用合成数据学习通用手-物跟踪控制器**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `灵巧手操作` `手-物跟踪` `合成数据` `强化学习` `模仿学习` `机器人控制` `泛化能力`

## 📋 核心要点

1. 现有灵巧操作方法依赖大量真实数据，成本高昂且难以扩展到新场景。
2. 论文提出HOP+HOT框架，利用HOP生成多样化合成数据，HOT学习通用跟踪控制器，实现从合成到真实的迁移。
3. 实验表明，该方法能使灵巧手跟踪复杂序列，包括物体重排列和掌内重定向，显著提升泛化能力。

## 📝 摘要（中文）

本文提出了一个系统，用于仅从合成数据中学习可泛化的手-物跟踪控制器，无需任何人工演示。该方法主要有两个贡献：(1) HOP（Hand-Object Planner），可以合成多样化的手-物轨迹；(2) HOT（Hand-Object Tracker），通过强化学习和交互模仿学习弥合了从合成到物理的迁移，从而提供了一个以目标手-物状态为条件的通用控制器。该方法可以扩展到不同的物体形状和手部形态。通过广泛的评估，我们表明该方法能够使灵巧的手跟踪具有挑战性的、长期的序列，包括物体重新排列和灵巧的掌内重定向。这些结果代表了迈向可扩展的操纵基础控制器的重要一步，该控制器可以完全从合成数据中学习，打破了长期以来限制灵巧操纵进展的数据瓶颈。

## 🔬 方法详解

**问题定义**：现有灵巧手操作方法严重依赖于大量真实世界的数据，这使得训练过程成本高昂且难以扩展到新的物体形状、手部形态和任务场景。数据收集的瓶颈限制了灵巧操作领域的发展。因此，如何仅使用合成数据训练出具有良好泛化能力的灵巧手-物跟踪控制器是一个关键问题。

**核心思路**：论文的核心思路是利用合成数据生成多样化的手-物交互轨迹，并训练一个能够从合成数据泛化到真实世界的跟踪控制器。通过结合手-物规划器（HOP）和手-物跟踪器（HOT），该方法旨在弥合合成数据和真实数据之间的差距，从而实现仅使用合成数据训练出鲁棒的灵巧手操作控制器。

**技术框架**：该方法包含两个主要模块：HOP（Hand-Object Planner）和 HOT（Hand-Object Tracker）。HOP负责生成多样化的手-物交互轨迹，作为HOT的训练数据。HOT则利用这些合成数据，通过强化学习和交互模仿学习训练一个通用的手-物跟踪控制器。该控制器以目标手-物状态为条件，能够根据目标状态调整手的运动，从而实现对物体的跟踪和操作。整体流程是从HOP生成合成数据，然后利用这些数据训练HOT，最后将训练好的HOT部署到真实机器人上。

**关键创新**：该方法最重要的创新在于提出了一种完全基于合成数据学习通用手-物跟踪控制器的框架。与以往依赖大量真实数据的方法不同，该方法通过HOP生成多样化的合成数据，并利用HOT学习从合成到真实的迁移，从而打破了数据瓶颈。此外，结合强化学习和交互模仿学习，使得HOT能够学习到更加鲁棒和泛化的控制策略。

**关键设计**：HOP的设计关键在于生成多样化的手-物交互轨迹，这需要考虑不同的物体形状、手部形态和任务目标。HOT的设计关键在于如何弥合合成数据和真实数据之间的差距，这需要仔细设计强化学习的奖励函数和交互模仿学习的目标函数。具体的网络结构和参数设置在论文中应该有详细描述，但摘要中未提及。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19583v1/img/teaser.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19583v1/img/overview.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19583v1/img/hop.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该论文通过实验验证了所提出方法的有效性，展示了灵巧手在复杂场景下的跟踪能力，包括物体重新排列和掌内重定向等。虽然摘要中没有给出具体的性能数据和对比基线，但强调了该方法在泛化能力方面的显著提升，表明其在解决灵巧操作问题上具有重要潜力。

## 🎯 应用场景

该研究成果可广泛应用于机器人自动化领域，例如工业生产中的物体抓取和装配、家庭服务机器人中的物品整理和清洁、以及医疗机器人中的手术辅助等。通过降低对真实数据的依赖，该方法有望加速灵巧操作机器人的研发和部署，提高机器人的智能化水平和服务能力。

## 📄 摘要（原文）

> We present a system for learning generalizable hand-object tracking controllers purely from synthetic data, without requiring any human demonstrations. Our approach makes two key contributions: (1) HOP, a Hand-Object Planner, which can synthesize diverse hand-object trajectories; and (2) HOT, a Hand-Object Tracker that bridges synthetic-to-physical transfer through reinforcement learning and interaction imitation learning, delivering a generalizable controller conditioned on target hand-object states. Our method extends to diverse object shapes and hand morphologies. Through extensive evaluations, we show that our approach enables dexterous hands to track challenging, long-horizon sequences including object re-arrangement and agile in-hand reorientation. These results represent a significant step toward scalable foundation controllers for manipulation that can learn entirely from synthetic data, breaking the data bottleneck that has long constrained progress in dexterous manipulation.

