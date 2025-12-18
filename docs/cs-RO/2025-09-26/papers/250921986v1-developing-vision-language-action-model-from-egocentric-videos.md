---
layout: default
title: Developing Vision-Language-Action Model from Egocentric Videos
---

# Developing Vision-Language-Action Model from Egocentric Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21986" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21986v1</a>
  <a href="https://arxiv.org/pdf/2509.21986.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21986v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21986v1', 'Developing Vision-Language-Action Model from Egocentric Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tomoya Yoshida, Shuhei Kurita, Taichi Nishimura, Shinsuke Mori

**分类**: cs.RO, cs.AI

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出基于第一视角视频的视觉-语言-动作模型训练方法，无需人工标注。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `第一视角视频` `机器人操作` `预训练` `物体操纵`

## 📋 核心要点

1. 现有VLA模型训练依赖昂贵的手动遥操作或需要详细的手部姿态记录等辅助标注，限制了其可扩展性。
2. 利用EgoScaler框架从原始第一视角视频中提取物体操纵轨迹，构建大规模VLA预训练数据集，无需额外标注。
3. 实验表明，使用该数据集预训练的VLA模型在模拟和真实机器人环境中均显著提升了任务成功率。

## 📝 摘要（中文）

本文提出了一种利用第一视角视频开发视觉-语言-动作模型（VLA）的方法，旨在解决VLA训练中对昂贵且专家驱动的手动遥操作的依赖问题。与此不同，第一视角视频提供了一种可扩展的替代方案，能够捕捉人类操纵物体和工具的方式，从而提供丰富的运动线索。该研究利用EgoScaler框架从第一视角视频中提取6DoF物体操纵轨迹，无需辅助记录。通过将EgoScaler应用于四个大规模第一视角视频数据集，并自动优化噪声或不完整的轨迹，构建了一个新的大规模VLA预训练数据集。在模拟和真实机器人环境中使用最先进的$π_0$架构进行的实验表明：（i）与从头开始训练相比，在本文数据集上进行预训练可将任务成功率提高20％以上；（ii）性能与使用真实机器人数据集所获得的性能相当；（iii）将本文数据集与真实机器人数据相结合可进一步提高性能。这些结果表明，第一视角视频是推进VLA研究的一种有前景且可扩展的资源。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉-语言-动作模型（VLA）训练中数据获取成本高昂的问题。现有方法通常依赖于手动遥操作或需要额外的手部姿态标注，这限制了VLA模型的可扩展性和泛化能力。因此，如何仅利用原始的第一视角视频来训练VLA模型是一个重要的挑战。

**核心思路**：论文的核心思路是利用第一视角视频中蕴含的丰富物体操纵信息，通过EgoScaler框架自动提取物体操纵轨迹，从而构建大规模的VLA预训练数据集。这种方法避免了手动标注或额外传感器数据的需求，降低了数据获取成本，并提高了模型的可扩展性。

**技术框架**：整体框架包括以下几个主要步骤：1) 使用EgoScaler从第一视角视频中提取6DoF物体操纵轨迹；2) 对提取的轨迹进行自动优化，去除噪声和补全缺失数据；3) 利用优化后的轨迹构建VLA预训练数据集；4) 使用该数据集预训练VLA模型（本文使用$π_0$架构）；5) 在模拟和真实机器人环境中评估预训练模型的性能。

**关键创新**：论文的关键创新在于提出了一种完全基于原始第一视角视频的VLA模型训练方法，无需任何人工标注或额外传感器数据。EgoScaler框架能够自动提取物体操纵轨迹，并进行轨迹优化，从而构建高质量的预训练数据集。这种方法显著降低了VLA模型训练的数据获取成本，并提高了模型的可扩展性。

**关键设计**：EgoScaler框架的具体实现细节未知，论文重点在于利用该框架生成的数据集进行VLA模型的预训练。预训练采用的$π_0$架构的具体参数设置和损失函数细节未知。轨迹优化算法的具体细节也未知，但其目标是去除噪声和补全缺失数据，以提高轨迹的质量。

## 📊 实验亮点

实验结果表明，使用该论文提出的数据集进行预训练，VLA模型在任务成功率上比从头开始训练提高了20%以上。此外，预训练模型的性能与使用真实机器人数据集训练的模型相当，并且将该数据集与真实机器人数据结合使用可以进一步提高性能。这些结果验证了该方法在VLA模型训练中的有效性。

## 🎯 应用场景

该研究成果可应用于各种机器人操作任务，例如家庭服务机器人、工业机器人等。通过利用大量的公开第一视角视频数据，可以训练出更通用、更鲁棒的VLA模型，从而提高机器人的自主操作能力。此外，该方法还可以扩展到其他类型的机器人任务，例如导航、抓取等。

## 📄 摘要（原文）

> Egocentric videos capture how humans manipulate objects and tools, providing diverse motion cues for learning object manipulation. Unlike the costly, expert-driven manual teleoperation commonly used in training Vision-Language-Action models (VLAs), egocentric videos offer a scalable alternative. However, prior studies that leverage such videos for training robot policies typically rely on auxiliary annotations, such as detailed hand-pose recordings. Consequently, it remains unclear whether VLAs can be trained directly from raw egocentric videos. In this work, we address this challenge by leveraging EgoScaler, a framework that extracts 6DoF object manipulation trajectories from egocentric videos without requiring auxiliary recordings. We apply EgoScaler to four large-scale egocentric video datasets and automatically refine noisy or incomplete trajectories, thereby constructing a new large-scale dataset for VLA pre-training. Our experiments with a state-of-the-art $π_0$ architecture in both simulated and real-robot environments yield three key findings: (i) pre-training on our dataset improves task success rates by over 20\% compared to training from scratch, (ii) the performance is competitive with that achieved using real-robot datasets, and (iii) combining our dataset with real-robot data yields further improvements. These results demonstrate that egocentric videos constitute a promising and scalable resource for advancing VLA research.

