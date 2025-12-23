---
layout: default
title: Bootstrapping World Models from Dynamics Models in Multimodal Foundation Models
---

# Bootstrapping World Models from Dynamics Models in Multimodal Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06006" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06006v1</a>
  <a href="https://arxiv.org/pdf/2506.06006.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06006v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06006v1', 'Bootstrapping World Models from Dynamics Models in Multimodal Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifu Qiu, Yftah Ziser, Anna Korhonen, Shay B. Cohen, Edoardo M. Ponti

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-06-06

---

## 💡 一句话要点

**提出通过动态模型引导世界模型以解决多模态基础模型的局限性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态基础模型` `动态模型` `世界模型` `弱监督学习` `图像编辑` `推理验证` `计算机视觉`

## 📋 核心要点

1. 现有的开源基础模型在构建现实世界模型和动态模型方面存在显著挑战，尤其是在通过语言表达动作时。
2. 论文提出通过动态模型引导世界模型的两种策略，分别是弱监督学习和推理时验证，以提升模型的性能。
3. 实验结果表明，所提出的模型在Aurora-Bench的图像编辑任务中表现优于现有模型，提升幅度达到15%。

## 📝 摘要（中文）

本研究探讨了视觉与语言基础模型在构建现实世界模型和动态模型方面的能力，发现通过监督微调动态模型比获取世界模型更为简单。研究提出了两种策略来利用动态模型引导世界模型：1) 从合成数据中进行弱监督学习，2) 推理时验证。通过这两种策略，动态模型能够为未标记的视频帧对注释动作，并为世界模型的多个样本分配奖励，从而在推理时有效指导搜索。实验结果显示，所提出的模型在Aurora-Bench的以动作为中心的图像编辑任务中表现优异，超越了现有的图像编辑模型，尤其在真实世界子集上提升了15%。

## 🔬 方法详解

**问题定义**：本研究旨在解决视觉与语言基础模型在构建现实世界模型和动态模型时的不足，尤其是在通过语言表达动作的场景中，现有方法的效果不理想。

**核心思路**：论文的核心思路是利用动态模型来引导世界模型的构建，通过两种策略来增强模型的学习能力和推理效果。这样的设计旨在克服现有模型在数据标注和推理效率上的局限性。

**技术框架**：整体架构包括两个主要模块：动态模型和世界模型。动态模型通过弱监督学习从合成数据中生成标注，并在推理时为世界模型提供奖励信号，以优化其输出。

**关键创新**：最重要的技术创新在于提出了通过动态模型进行世界模型引导的两种策略，尤其是引入了基于重要性加权的图像标记机制，这在现有文献中尚属首次。

**关键设计**：在动态模型的训练中，采用了新的目标函数，使得观察对中的图像标记根据其重要性进行加权。此外，推理时的奖励分配机制也经过优化，以提高搜索效率和结果质量。

## 📊 实验亮点

实验结果显示，所提出的模型在Aurora-Bench的以动作为中心的图像编辑任务中，性能与最先进的图像编辑模型相当，并在真实世界子集上提升了15%。此外，模型在所有子集上的平均人类评估表现最佳，显示出其优越性。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、机器人控制和人机交互等。通过提升多模态基础模型的性能，能够在图像编辑、视频理解和自动化决策等实际场景中发挥重要作用，未来可能推动相关技术的广泛应用和发展。

## 📄 摘要（原文）

> To what extent do vision-and-language foundation models possess a realistic world model (observation $\times$ action $\rightarrow$ observation) and a dynamics model (observation $\times$ observation $\rightarrow$ action), when actions are expressed through language? While open-source foundation models struggle with both, we find that fine-tuning them to acquire a dynamics model through supervision is significantly easier than acquiring a world model. In turn, dynamics models can be used to bootstrap world models through two main strategies: 1) weakly supervised learning from synthetic data and 2) inference time verification. Firstly, the dynamics model can annotate actions for unlabelled pairs of video frame observations to expand the training data. We further propose a new objective, where image tokens in observation pairs are weighted by their importance, as predicted by a recognition model. Secondly, the dynamics models can assign rewards to multiple samples of the world model to score them, effectively guiding search at inference time. We evaluate the world models resulting from both strategies through the task of action-centric image editing on Aurora-Bench. Our best model achieves a performance competitive with state-of-the-art image editing models, improving on them by a margin of $15\%$ on real-world subsets according to GPT4o-as-judge, and achieving the best average human evaluation across all subsets of Aurora-Bench.

