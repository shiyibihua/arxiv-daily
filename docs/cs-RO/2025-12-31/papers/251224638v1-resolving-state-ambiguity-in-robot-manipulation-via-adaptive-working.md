---
layout: default
title: Resolving State Ambiguity in Robot Manipulation via Adaptive Working Memory Recoding
---

# Resolving State Ambiguity in Robot Manipulation via Adaptive Working Memory Recoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24638" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24638v1</a>
  <a href="https://arxiv.org/pdf/2512.24638.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24638v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24638v1', 'Resolving State Ambiguity in Robot Manipulation via Adaptive Working Memory Recoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qingda Hu, Ziheng Qiu, Zijun Xu, Kaizhao Zhang, Xizhou Bu, Zuolei Sun, Bo Zhang, Jieru Zhao, Zhongxue Gan, Wenchao Ding

**分类**: cs.RO

**发布日期**: 2025-12-31

**🔗 代码/项目**: [PROJECT_PAGE](https://tinda24.github.io/pam/)

---

## 💡 一句话要点

**提出基于自适应工作记忆的策略PAM，解决机器人操作中的状态歧义问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人操作` `状态歧义` `自适应工作记忆` `长时依赖` `视觉运动策略`

## 📋 核心要点

1. 机器人操作中状态歧义普遍存在，相同观测可能对应多个行为轨迹，需要有效利用历史信息。
2. PAM通过自适应工作记忆，分层提取特征，并使用上下文路由压缩历史信息，解决长时依赖问题。
3. 实验证明PAM能有效处理多种状态歧义场景，在长历史窗口下保持稳定训练和较高推理速度。

## 📝 摘要（中文）

本文提出了一种名为PAM的视觉运动策略，它配备了自适应工作记忆，旨在解决机器人操作中常见的状态歧义问题。相同的观测可能对应多个有效的行为轨迹，因此策略需要从历史信息中正确提取信息以识别当前任务阶段。PAM通过分层帧特征提取器为运动原语和时间消歧生成不同的表示，并采用带有范围特定查询的上下文路由来生成跨多个历史长度的紧凑上下文特征。引入重构历史信息的辅助目标，确保上下文路由作为有效的瓶颈。实验表明，PAM能够同时处理多种状态歧义场景，在约10秒的历史窗口下，仍能保持稳定的训练和20Hz以上的推理速度。

## 🔬 方法详解

**问题定义**：机器人操作中，由于传感器噪声、部分观测等原因，常常出现状态歧义，即相同的观测可能对应多个不同的行为轨迹。现有的方法要么依赖于手工设计的状态表示，要么简单地扩展历史窗口，前者泛化性差，后者计算成本高且容易过拟合。

**核心思路**：受到人类推理和工作记忆重编码的启发，论文提出使用自适应工作记忆来解决状态歧义问题。核心思想是学习一种能够动态选择和压缩历史信息的策略，从而在保证推理速度的同时，有效地利用长时依赖关系。

**技术框架**：PAM包含以下几个主要模块：1) 分层帧特征提取器：提取运动原语和时间消歧两种不同的特征表示。2) 上下文路由：使用范围特定的查询来生成跨多个历史长度的紧凑上下文特征。3) 策略网络：基于上下文特征输出动作。4) 辅助重构目标：用于训练上下文路由，使其能够有效地压缩历史信息。整体流程是，首先通过分层帧特征提取器提取每一帧的特征，然后通过上下文路由将历史帧的特征压缩成上下文特征，最后策略网络基于上下文特征输出动作。

**关键创新**：PAM的关键创新在于自适应工作记忆的设计，它能够动态地选择和压缩历史信息，从而在保证推理速度的同时，有效地利用长时依赖关系。与现有方法相比，PAM不需要手工设计状态表示，也不需要简单地扩展历史窗口，因此具有更好的泛化性和计算效率。

**关键设计**：1) 分层帧特征提取器：使用两个独立的卷积神经网络分别提取运动原语和时间消歧特征。2) 上下文路由：使用多个范围特定的查询，每个查询负责提取特定时间范围内的信息。3) 辅助重构目标：使用一个解码器来重构历史帧的特征，并使用重构误差作为损失函数来训练上下文路由。4) 训练方式：采用两阶段训练方式，首先训练分层帧特征提取器和上下文路由，然后固定这些模块，训练策略网络。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24638v1/figures/coarse.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24638v1/figures/pipeline.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24638v1/figures/exp.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，PAM在多个状态歧义场景中表现出色，能够同时处理多种类型的歧义。在具有约10秒历史窗口的情况下，PAM仍然能够保持稳定的训练，并实现20Hz以上的推理速度。相较于基线方法，PAM在多个任务上取得了显著的性能提升。

## 🎯 应用场景

该研究成果可应用于各种需要处理状态歧义的机器人操作任务，例如装配、抓取、导航等。通过利用长时依赖关系，机器人可以更好地理解任务目标，并做出更合理的决策。此外，该方法还可以推广到其他需要处理序列数据的领域，例如自然语言处理、语音识别等。

## 📄 摘要（原文）

> State ambiguity is common in robotic manipulation. Identical observations may correspond to multiple valid behavior trajectories. The visuomotor policy must correctly extract the appropriate types and levels of information from the history to identify the current task phase. However, naively extending the history window is computationally expensive and may cause severe overfitting. Inspired by the continuous nature of human reasoning and the recoding of working memory, we introduce PAM, a novel visuomotor Policy equipped with Adaptive working Memory. With minimal additional training cost in a two-stage manner, PAM supports a 300-frame history window while maintaining high inference speed. Specifically, a hierarchical frame feature extractor yields two distinct representations for motion primitives and temporal disambiguation. For compact representation, a context router with range-specific queries is employed to produce compact context features across multiple history lengths. And an auxiliary objective of reconstructing historical information is introduced to ensure that the context router acts as an effective bottleneck. We meticulously design 7 tasks and verify that PAM can handle multiple scenarios of state ambiguity simultaneously. With a history window of approximately 10 seconds, PAM still supports stable training and maintains inference speeds above 20Hz. Project website: https://tinda24.github.io/pam/

