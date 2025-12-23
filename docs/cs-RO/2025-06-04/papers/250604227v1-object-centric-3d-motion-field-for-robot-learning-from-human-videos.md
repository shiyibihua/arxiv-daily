---
layout: default
title: Object-centric 3D Motion Field for Robot Learning from Human Videos
---

# Object-centric 3D Motion Field for Robot Learning from Human Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04227" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04227v1</a>
  <a href="https://arxiv.org/pdf/2506.04227.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04227v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04227v1', 'Object-centric 3D Motion Field for Robot Learning from Human Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhao-Heng Yin, Sherry Yang, Pieter Abbeel

**分类**: cs.RO, cs.AI, cs.CV, cs.LG, eess.SY

**发布日期**: 2025-06-04

**备注**: Project: https://zhaohengyin.github.io/3DMF

---

## 💡 一句话要点

**提出对象中心的3D运动场以解决机器人从人类视频学习的挑战**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `机器人学习` `3D运动场` `视频理解` `动作表示` `去噪估计` `策略泛化` `跨体现转移`

## 📋 核心要点

1. 现有方法在从视频中提取动作知识时面临建模复杂性和信息丢失等挑战。
2. 本文提出使用对象中心的3D运动场来表示动作，并设计了去噪估计器和密集预测架构。
3. 实验结果显示，方法在3D运动估计误差上降低超过50%，成功率达到55%，显著优于现有方法。

## 📝 摘要（中文）

从人类视频中学习机器人控制策略是一种有前景的机器人学习扩展方向。然而，如何从视频中提取动作知识以进行策略学习仍然是一个关键挑战。现有的动作表示方法如视频帧、像素流和点云流存在建模复杂性或信息丢失等固有局限性。本文提出使用对象中心的3D运动场来表示动作，并展示了一种新颖的框架来从视频中提取这种表示以实现零-shot控制。我们引入了两个新颖的组件：一是训练一个“去噪”3D运动场估计器的训练管道，以稳健地从人类视频中提取细致的对象3D运动；二是一个密集的对象中心3D运动场预测架构，促进跨体现转移和策略对背景的泛化。实验表明，我们的方法在真实世界设置中将3D运动估计误差降低了50%以上，成功率达到55%，而先前方法的成功率低于10%。

## 🔬 方法详解

**问题定义**：本文旨在解决从人类视频中提取有效动作表示以进行机器人控制策略学习的问题。现有方法如视频帧和点云流存在建模复杂性和信息丢失的痛点。

**核心思路**：我们提出使用对象中心的3D运动场作为动作表示，通过去噪估计器提取细致的对象运动，增强策略学习的有效性。

**技术框架**：整体架构包括两个主要模块：一是“去噪”3D运动场估计器，二是密集的对象中心3D运动场预测架构，二者协同工作以实现高效的动作表示提取。

**关键创新**：最重要的创新在于引入了去噪估计器和密集预测架构，前者提高了运动提取的鲁棒性，后者促进了跨体现转移和策略泛化。

**关键设计**：在去噪估计器中，采用了特定的损失函数以优化运动场的精度；密集预测架构则通过多层网络结构实现对复杂背景的适应性。实验中还对参数进行了细致调优，以确保最佳性能。

## 📊 实验亮点

实验结果显示，提出的方法在3D运动估计误差上降低超过50%，成功率达到55%，而先前方法的成功率仅为10%以下。这表明该方法在复杂任务中的有效性和优越性，尤其是在细粒度操作技能的学习上。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、自动化制造和人机交互等。通过从人类视频中学习，机器人能够更灵活地适应复杂环境，提升其自主操作能力，未来可能在家庭服务、医疗辅助等领域发挥重要作用。

## 📄 摘要（原文）

> Learning robot control policies from human videos is a promising direction for scaling up robot learning. However, how to extract action knowledge (or action representations) from videos for policy learning remains a key challenge. Existing action representations such as video frames, pixelflow, and pointcloud flow have inherent limitations such as modeling complexity or loss of information. In this paper, we propose to use object-centric 3D motion field to represent actions for robot learning from human videos, and present a novel framework for extracting this representation from videos for zero-shot control. We introduce two novel components in its implementation. First, a novel training pipeline for training a ''denoising'' 3D motion field estimator to extract fine object 3D motions from human videos with noisy depth robustly. Second, a dense object-centric 3D motion field prediction architecture that favors both cross-embodiment transfer and policy generalization to background. We evaluate the system in real world setups. Experiments show that our method reduces 3D motion estimation error by over 50% compared to the latest method, achieve 55% average success rate in diverse tasks where prior approaches fail~($\lesssim 10$\%), and can even acquire fine-grained manipulation skills like insertion.

