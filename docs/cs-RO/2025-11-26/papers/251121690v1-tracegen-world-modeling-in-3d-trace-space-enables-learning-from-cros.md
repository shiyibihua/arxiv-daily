---
layout: default
title: TraceGen: World Modeling in 3D Trace Space Enables Learning from Cross-Embodiment Videos
---

# TraceGen: World Modeling in 3D Trace Space Enables Learning from Cross-Embodiment Videos

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.21690" target="_blank" class="toolbar-btn">arXiv: 2511.21690v1</a>
    <a href="https://arxiv.org/pdf/2511.21690.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.21690v1" 
            onclick="toggleFavorite(this, '2511.21690v1', 'TraceGen: World Modeling in 3D Trace Space Enables Learning from Cross-Embodiment Videos')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Seungjae Lee, Yoonkyo Jung, Inkook Chun, Yao-Chih Lee, Zikui Cai, Hongjia Huang, Aayush Talreja, Tan Dat Dao, Yongyuan Liang, Jia-Bin Huang, Furong Huang

**分类**: cs.RO, cs.CV, cs.LG

**发布日期**: 2025-11-26

---

## 💡 一句话要点

**TraceGen：通过3D轨迹空间的世界建模实现跨具身视频学习**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `机器人学习` `跨具身学习` `世界模型` `轨迹预测` `迁移学习`

## 📋 核心要点

1. 现有方法难以利用来自不同具身（人类、其他机器人）的视频进行机器人学习，因为具身、相机和环境的差异阻碍了直接使用。
2. TraceGen通过引入3D轨迹空间作为统一表示，将异构视频转换为一致的轨迹，从而抽象掉外观差异，保留几何结构。
3. 实验表明，TraceGen仅需少量目标机器人视频即可实现高效迁移学习，并在真实机器人任务中取得显著成功，推理速度远超现有方法。

## 📝 摘要（中文）

本文提出了一种新的方法TraceGen，通过统一的符号表示——场景级轨迹的紧凑3D“轨迹空间”，实现从跨具身、跨环境和跨任务视频中学习新的机器人任务。TraceGen是一个世界模型，它在轨迹空间而非像素空间中预测未来运动，抽象掉外观，同时保留操作所需的几何结构。为了大规模训练TraceGen，开发了TraceForge数据管道，将异构的人类和机器人视频转换为一致的3D轨迹，生成包含12.3万个视频和180万个观察-轨迹-语言三元组的语料库。预训练的TraceGen产生了一个可迁移的3D运动先验，能够高效适应：仅用五个目标机器人视频，TraceGen在四个任务中达到80%的成功率，同时提供比最先进的基于视频的世界模型快50-600倍的推理速度。在更具挑战性的情况下，仅有五个在手持电话上捕获的未校准的人类演示视频可用时，它仍然可以在真实机器人上达到67.5%的成功率，突显了TraceGen在不依赖对象检测器或繁重的像素空间生成的情况下跨具身适应的能力。

## 🔬 方法详解

**问题定义**：现有机器人学习方法难以直接利用大量存在的跨具身（例如，人类和不同机器人）视频数据。这是因为不同具身、相机视角以及环境的差异导致了数据分布的巨大差异，使得直接的像素空间学习变得困难。现有方法通常依赖于大量的目标机器人数据或复杂的像素级生成模型，计算成本高昂且泛化能力有限。

**核心思路**：TraceGen的核心思路是将视频数据投影到一个统一的3D轨迹空间中，从而抽象掉外观信息，保留关键的几何结构。通过在这个轨迹空间中进行运动预测，模型可以学习到与具身无关的运动先验知识，从而实现跨具身的迁移学习。这种方法避免了直接在像素空间进行学习，降低了计算复杂度，并提高了泛化能力。

**技术框架**：TraceGen的整体框架包括两个主要部分：TraceForge数据管道和TraceGen世界模型。TraceForge负责将异构的视频数据转换为3D轨迹，生成大规模的训练数据集。TraceGen则是一个基于Transformer的序列预测模型，它以轨迹序列作为输入，预测未来的轨迹。整个流程包括数据收集、轨迹提取、模型训练和运动规划等步骤。

**关键创新**：TraceGen的关键创新在于提出了3D轨迹空间作为统一的表示形式，以及TraceForge数据管道用于生成大规模的跨具身训练数据。与现有方法相比，TraceGen不需要依赖于对象检测器或复杂的像素空间生成模型，而是直接在轨迹空间中进行学习，从而降低了计算成本，提高了泛化能力。

**关键设计**：TraceGen使用Transformer架构进行轨迹预测，损失函数包括轨迹预测损失和语言描述损失。TraceForge数据管道利用SfM（Structure from Motion）技术从视频中重建3D场景，并提取轨迹。为了处理不同视频的尺度和视角差异，TraceForge还采用了数据增强技术，例如随机缩放和旋转。

## 📊 实验亮点

实验结果表明，TraceGen在四个机器人任务中仅使用五个目标机器人视频即可达到80%的成功率，并且推理速度比最先进的基于视频的世界模型快50-600倍。在更具挑战性的情况下，仅使用五个未校准的人类演示视频，TraceGen仍然可以在真实机器人上达到67.5%的成功率，证明了其强大的跨具身迁移能力。

## 🎯 应用场景

TraceGen具有广泛的应用前景，例如可以用于机器人模仿学习、人机协作、自动驾驶等领域。通过利用大量的跨具身视频数据，TraceGen可以帮助机器人快速学习新的技能，并适应不同的环境。此外，TraceGen还可以用于生成逼真的机器人动画，以及进行虚拟现实和增强现实应用。

## 📄 摘要（原文）

> Learning new robot tasks on new platforms and in new scenes from only a handful of demonstrations remains challenging. While videos of other embodiments - humans and different robots - are abundant, differences in embodiment, camera, and environment hinder their direct use. We address the small-data problem by introducing a unifying, symbolic representation - a compact 3D "trace-space" of scene-level trajectories - that enables learning from cross-embodiment, cross-environment, and cross-task videos. We present TraceGen, a world model that predicts future motion in trace-space rather than pixel space, abstracting away appearance while retaining the geometric structure needed for manipulation. To train TraceGen at scale, we develop TraceForge, a data pipeline that transforms heterogeneous human and robot videos into consistent 3D traces, yielding a corpus of 123K videos and 1.8M observation-trace-language triplets. Pretraining on this corpus produces a transferable 3D motion prior that adapts efficiently: with just five target robot videos, TraceGen attains 80% success across four tasks while offering 50-600x faster inference than state-of-the-art video-based world models. In the more challenging case where only five uncalibrated human demonstration videos captured on a handheld phone are available, it still reaches 67.5% success on a real robot, highlighting TraceGen's ability to adapt across embodiments without relying on object detectors or heavy pixel-space generation.

