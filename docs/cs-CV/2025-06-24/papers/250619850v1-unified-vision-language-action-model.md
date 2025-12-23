---
layout: default
title: Unified Vision-Language-Action Model
---

# Unified Vision-Language-Action Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19850" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19850v1</a>
  <a href="https://arxiv.org/pdf/2506.19850.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19850v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19850v1', 'Unified Vision-Language-Action Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuqi Wang, Xinghang Li, Wenxuan Wang, Junbo Zhang, Yingyan Li, Yuntao Chen, Xinlong Wang, Zhaoxiang Zhang

**分类**: cs.CV, cs.RO

**发布日期**: 2025-06-24

**备注**: technical report

---

## 💡 一句话要点

**提出UniVLA模型以解决视觉-语言-动作理解问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `多模态学习` `自回归建模` `因果动态` `机器人操作` `长时间任务` `视频理解` `策略学习`

## 📋 核心要点

1. 现有的视觉-语言-动作模型在生成动作信号时，往往忽视了视觉数据中的时序和因果关系，导致性能不足。
2. 本文提出的UniVLA模型通过自回归建模视觉、语言和动作信号，能够有效捕捉多模态信息，特别适合大规模视频数据的学习。
3. UniVLA在多个仿真基准上取得了新的最先进结果，例如在LIBERO基准上达到95.5%的平均成功率，显著优于之前的85.5%。

## 📝 摘要（中文）

视觉-语言-动作模型（VLA）因其在机器人操作中的潜力而受到广泛关注。然而，现有方法主要依赖视觉-语言模型（VLM）的通用理解能力生成动作信号，常常忽视视觉观察中蕴含的丰富时序和因果结构。本文提出了UniVLA，一个统一的多模态VLA模型，能够自回归地将视觉、语言和动作信号建模为离散的标记序列。这种表述方式使得从大规模视频数据中学习灵活的多模态任务成为可能。通过在后期训练中引入世界建模，UniVLA捕捉视频中的因果动态，从而有效地转移到下游策略学习，尤其适用于长时间任务。我们的研究在多个广泛使用的仿真基准上设定了新的最先进结果，显著超越了之前的方法。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉-语言-动作模型在生成动作信号时对时序和因果结构的忽视，导致的性能不足问题。

**核心思路**：UniVLA模型通过自回归方式将视觉、语言和动作信号建模为离散的标记序列，能够更好地捕捉多模态信息和因果关系，提升任务学习的灵活性和有效性。

**技术框架**：UniVLA的整体架构包括三个主要模块：视觉编码器、语言编码器和动作生成器。视觉编码器负责提取视频中的视觉特征，语言编码器处理文本信息，动作生成器则根据前两者生成相应的动作信号。

**关键创新**：UniVLA的主要创新在于其自回归建模方式和后期训练中的世界建模，能够有效捕捉视频中的因果动态，显著提升了模型在长时间任务中的表现。

**关键设计**：模型采用了多层Transformer结构，损失函数设计为结合了预测准确性和因果一致性的复合损失，以确保生成的动作信号与视觉和语言信息的一致性。

## 📊 实验亮点

UniVLA在多个仿真基准上设定了新的最先进结果，例如在LIBERO基准上实现了95.5%的平均成功率，显著超越了pi0-FAST的85.5%。此外，模型在实际应用场景如ALOHA操作和自动驾驶中也展现了良好的适应性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、自动驾驶和人机交互等。UniVLA模型能够在复杂的动态环境中理解和执行任务，具有广泛的实际价值和未来影响，尤其是在需要长时间规划和决策的场景中。

## 📄 摘要（原文）

> Vision-language-action models (VLAs) have garnered significant attention for their potential in advancing robotic manipulation. However, previous approaches predominantly rely on the general comprehension capabilities of vision-language models (VLMs) to generate action signals, often overlooking the rich temporal and causal structure embedded in visual observations. In this paper, we present UniVLA, a unified and native multimodal VLA model that autoregressively models vision, language, and action signals as discrete token sequences. This formulation enables flexible multimodal tasks learning, particularly from large-scale video data. By incorporating world modeling during post-training, UniVLA captures causal dynamics from videos, facilitating effective transfer to downstream policy learning--especially for long-horizon tasks. Our approach sets new state-of-the-art results across several widely used simulation benchmarks, including CALVIN, LIBERO, and Simplenv-Bridge, significantly surpassing previous methods. For example, UniVLA achieves 95.5% average success rate on LIBERO benchmark, surpassing pi0-FAST's 85.5%. We further demonstrate its broad applicability on real-world ALOHA manipulation and autonomous driving.

