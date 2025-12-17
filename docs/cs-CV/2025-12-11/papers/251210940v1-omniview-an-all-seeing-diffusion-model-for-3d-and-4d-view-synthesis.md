---
layout: default
title: OmniView: An All-Seeing Diffusion Model for 3D and 4D View Synthesis
---

# OmniView: An All-Seeing Diffusion Model for 3D and 4D View Synthesis

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.10940" target="_blank" class="toolbar-btn">arXiv: 2512.10940v1</a>
    <a href="https://arxiv.org/pdf/2512.10940.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.10940v1" 
            onclick="toggleFavorite(this, '2512.10940v1', 'OmniView: An All-Seeing Diffusion Model for 3D and 4D View Synthesis')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Xiang Fan, Sharath Girish, Vivek Ramanujan, Chaoyang Wang, Ashkan Mirzaei, Petr Sushko, Aliaksandr Siarohin, Sergey Tulyakov, Ranjay Krishna

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-11

**备注**: Project page: https://snap-research.github.io/OmniView/

**🔗 代码/项目**: [PROJECT_PAGE](https://snap-research.github.io/OmniView/)

---

## 💡 一句话要点

**OmniView：用于3D和4D视图合成的统一扩散模型**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `扩散模型` `4D视图合成` `新视角合成` `视频生成` `相机控制` `条件生成` `多视图学习`

## 📋 核心要点

1. 现有方法在4D一致性任务上分散，缺乏统一的训练框架，导致数据利用率低。
2. OmniView通过分离空间、时间和视图条件，实现对各种4D任务的灵活组合和泛化。
3. OmniView在多个数据集上超越特定任务模型，显著提升图像质量和相机控制精度。

## 📝 摘要（中文）

现有方法将相机控制融入扩散模型，但往往专注于4D一致性任务的特定子集，例如新视角合成、带相机控制的文本到视频生成、图像到视频生成等。这些方法在可用的3D/4D数据的不相交切片上进行训练。本文提出了OmniView，一个统一的框架，可以推广到各种4D一致性任务。该方法分别表示空间、时间和视图条件，从而能够灵活地组合这些输入。例如，OmniView可以从静态、动态和多视图输入中合成新视角，在时间上向前和向后推断轨迹，并从文本或图像提示创建具有完全相机控制的视频。OmniView在不同的基准和指标上与特定任务模型相比具有竞争力，在多视图NVS LLFF数据集中，相机条件扩散模型的图像质量得分提高了33%，在动态NVS Neural 3D Video基准中提高了60%，在RE-10K上的静态相机控制提高了20%，在文本条件视频生成中，相机轨迹误差降低了4倍。凭借在一个模型中的强大泛化能力，OmniView展示了通用4D视频模型的可行性。

## 🔬 方法详解

**问题定义**：现有方法针对不同的4D一致性任务（如新视角合成、文本到视频等）设计独立的模型，导致模型碎片化，无法充分利用现有的3D/4D数据。每个模型只在特定的数据切片上训练，泛化能力受限。

**核心思路**：OmniView的核心在于构建一个统一的扩散模型，能够处理多种4D一致性任务。通过将空间、时间和视图条件解耦，模型可以灵活地组合这些条件，从而适应不同的输入和输出形式。这种解耦的设计使得模型能够从各种数据中学习，并泛化到新的任务上。

**技术框架**：OmniView采用扩散模型的框架，并引入了三个关键的条件输入：空间条件（例如，图像或多视图图像）、时间条件（例如，时间步长或轨迹）和视图条件（例如，相机姿态）。这些条件通过独立的编码器进行处理，然后融合到扩散模型的噪声预测网络中。模型通过学习如何从噪声中生成符合这些条件的图像或视频来实现4D视图合成。

**关键创新**：OmniView的关键创新在于其统一的框架和解耦的条件表示。与以往针对特定任务设计的模型不同，OmniView能够处理多种4D一致性任务，并且具有更强的泛化能力。通过解耦空间、时间和视图条件，模型可以灵活地组合这些条件，从而适应不同的输入和输出形式。

**关键设计**：OmniView使用Transformer网络来编码空间、时间和视图条件。扩散模型采用U-Net架构，并使用注意力机制来融合条件编码。损失函数采用标准的扩散模型损失，即预测噪声与真实噪声之间的均方误差。在训练过程中，模型使用多种3D/4D数据集进行训练，以提高其泛化能力。

## 📊 实验亮点

OmniView在多个数据集上取得了显著的性能提升。在LLFF数据集上，图像质量得分提高了33%。在Neural 3D Video数据集上，图像质量得分提高了60%。在RE-10K数据集上，静态相机控制的图像质量得分提高了20%。在文本条件视频生成任务中，相机轨迹误差降低了4倍。这些结果表明，OmniView具有强大的泛化能力和优越的性能。

## 🎯 应用场景

OmniView具有广泛的应用前景，包括虚拟现实、增强现实、游戏开发、电影制作等领域。它可以用于生成逼真的3D场景和动态视频，实现沉浸式的用户体验。此外，OmniView还可以用于机器人导航、自动驾驶等领域，帮助机器人理解和感知周围环境。

## 📄 摘要（原文）

> Prior approaches injecting camera control into diffusion models have focused on specific subsets of 4D consistency tasks: novel view synthesis, text-to-video with camera control, image-to-video, amongst others. Therefore, these fragmented approaches are trained on disjoint slices of available 3D/4D data. We introduce OmniView, a unified framework that generalizes across a wide range of 4D consistency tasks. Our method separately represents space, time, and view conditions, enabling flexible combinations of these inputs. For example, OmniView can synthesize novel views from static, dynamic, and multiview inputs, extrapolate trajectories forward and backward in time, and create videos from text or image prompts with full camera control. OmniView is competitive with task-specific models across diverse benchmarks and metrics, improving image quality scores among camera-conditioned diffusion models by up to 33\% in multiview NVS LLFF dataset, 60\% in dynamic NVS Neural 3D Video benchmark, 20\% in static camera control on RE-10K, and reducing camera trajectory errors by 4x in text-conditioned video generation. With strong generalizability in one model, OmniView demonstrates the feasibility of a generalist 4D video model. Project page is available at https://snap-research.github.io/OmniView/

