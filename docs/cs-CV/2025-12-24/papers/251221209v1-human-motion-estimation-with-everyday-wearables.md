---
layout: default
title: Human Motion Estimation with Everyday Wearables
---

# Human Motion Estimation with Everyday Wearables

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21209" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21209v1</a>
  <a href="https://arxiv.org/pdf/2512.21209.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21209v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21209v1', 'Human Motion Estimation with Everyday Wearables')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siqi Zhu, Yixuan Li, Junfu Li, Qi Wu, Zan Wang, Haozhe Ma, Wei Liang

**分类**: cs.CV

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**EveryWear：利用日常可穿戴设备进行轻量级、免标定的全身人体运动估计**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人体运动估计` `可穿戴设备` `多模态融合` `师生学习` `免标定` `真实世界数据` `Ego-Elec数据集`

## 📋 核心要点

1. 现有基于可穿戴设备的人体运动估计方法存在穿戴不便、硬件昂贵和校准繁琐等问题，限制了其在日常生活中的应用。
2. EveryWear利用智能手机、智能手表、耳机和智能眼镜等日常可穿戴设备，结合视觉和惯性信号，实现轻量级、免标定的全身人体运动估计。
3. 通过在真实世界数据集Ego-Elec上训练，并采用多模态师生框架，该方法有效消除了sim-to-real差距，并在实验中优于基线模型。

## 📝 摘要（中文）

本文提出EveryWear，一种轻量级且实用的全身人体运动捕捉方法，完全基于日常可穿戴设备：智能手机、智能手表、耳机和智能眼镜，眼镜配备一个前置摄像头和两个下视摄像头，无需使用前进行显式校准。为了促进该方向的稳健研究和基准测试，我们引入了Ego-Elec，一个9小时的真实世界数据集，涵盖17个不同的室内和室外环境中的56项日常活动，并由运动捕捉（MoCap）提供ground-truth 3D标注。我们的方法采用多模态师生框架，将来自以自我为中心的摄像头的视觉线索与来自消费设备的惯性信号相结合。通过直接在真实世界数据上进行训练，我们的模型有效地消除了限制先前工作的sim-to-real差距。实验表明，我们的方法优于基线模型，验证了其在实际全身运动估计中的有效性。

## 🔬 方法详解

**问题定义**：现有基于可穿戴设备的人体运动估计方法依赖于特定的、昂贵的硬件，并且需要繁琐的校准过程，这使得它们难以在日常生活中普及。因此，需要一种轻量级、低成本、易于使用的解决方案，能够利用常见的可穿戴设备进行准确的人体运动估计。

**核心思路**：论文的核心思路是利用日常生活中常见的可穿戴设备（智能手机、智能手表、耳机、智能眼镜）作为传感器，通过融合来自不同模态（视觉和惯性）的数据，实现全身人体运动的估计。这种方法避免了对专用硬件的依赖，降低了成本，并提高了易用性。

**技术框架**：EveryWear采用多模态师生框架。首先，利用配备摄像头的智能眼镜捕捉第一人称视角的视觉信息，同时利用智能手机、智能手表和耳机等设备的惯性传感器获取运动数据。然后，将这些多模态数据输入到模型中进行训练。该模型采用师生学习框架，其中教师模型可能是一个更复杂的模型，用于生成伪标签，而学生模型则是一个更轻量级的模型，用于实际的运动估计。

**关键创新**：该方法最重要的创新点在于其完全依赖于日常可穿戴设备，无需任何额外的专用硬件或复杂的校准过程。此外，通过直接在真实世界数据集上进行训练，有效地解决了sim-to-real的迁移问题，提高了模型的泛化能力。

**关键设计**：Ego-Elec数据集的构建是关键设计之一，它提供了丰富的真实世界数据，涵盖了各种日常活动和环境。多模态融合策略也是关键，如何有效地将视觉和惯性数据结合起来，以获得更准确的运动估计结果，是需要仔细设计的。损失函数的设计也至关重要，需要能够有效地指导模型学习人体运动的规律。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21209v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21209v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21209v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

EveryWear在Ego-Elec数据集上进行了评估，实验结果表明，该方法在全身人体运动估计方面优于基线模型。通过直接在真实世界数据上进行训练，该方法有效地消除了sim-to-real差距，提高了模型的泛化能力。具体性能数据和与基线模型的对比结果在论文中有详细展示。

## 🎯 应用场景

该研究成果可广泛应用于XR交互、虚拟现实、游戏、运动分析、健康监测等领域。例如，在VR/AR游戏中，用户可以通过日常可穿戴设备实现全身动作捕捉，从而获得更沉浸式的体验。在运动分析中，可以利用该技术对运动员的动作进行精确分析，提高训练效果。在健康监测中，可以实时监测用户的运动状态，提供个性化的健康建议。

## 📄 摘要（原文）

> While on-body device-based human motion estimation is crucial for applications such as XR interaction, existing methods often suffer from poor wearability, expensive hardware, and cumbersome calibration, which hinder their adoption in daily life. To address these challenges, we present EveryWear, a lightweight and practical human motion capture approach based entirely on everyday wearables: a smartphone, smartwatch, earbuds, and smart glasses equipped with one forward-facing and two downward-facing cameras, requiring no explicit calibration before use. We introduce Ego-Elec, a 9-hour real-world dataset covering 56 daily activities across 17 diverse indoor and outdoor environments, with ground-truth 3D annotations provided by the motion capture (MoCap), to facilitate robust research and benchmarking in this direction. Our approach employs a multimodal teacher-student framework that integrates visual cues from egocentric cameras with inertial signals from consumer devices. By training directly on real-world data rather than synthetic data, our model effectively eliminates the sim-to-real gap that constrains prior work. Experiments demonstrate that our method outperforms baseline models, validating its effectiveness for practical full-body motion estimation.

