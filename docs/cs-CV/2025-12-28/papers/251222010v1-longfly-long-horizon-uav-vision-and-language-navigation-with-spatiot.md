---
layout: default
title: "LongFly: Long-Horizon UAV Vision-and-Language Navigation with Spatiotemporal Context Integration"
---

# LongFly: Long-Horizon UAV Vision-and-Language Navigation with Spatiotemporal Context Integration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.22010" class="toolbar-btn" target="_blank">📄 arXiv: 2512.22010v1</a>
  <a href="https://arxiv.org/pdf/2512.22010.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.22010v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.22010v1', 'LongFly: Long-Horizon UAV Vision-and-Language Navigation with Spatiotemporal Context Integration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wen Jiang, Li Wang, Kangyao Huang, Wei Fan, Jinyuan Liu, Shaoyu Liu, Hongwei Duan, Bin Xu, Xiangyang Ji

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-26

---

## 💡 一句话要点

**LongFly：针对长程无人机视觉-语言导航，提出时空上下文融合框架**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无人机导航` `视觉-语言导航` `时空上下文建模` `历史信息融合` `多模态融合`

## 📋 核心要点

1. 现有无人机视觉-语言导航方法难以有效建模长程时空上下文，导致语义对齐不准确和路径规划不稳定。
2. LongFly通过历史感知时空建模策略，将历史数据转换为结构化、紧凑和富有表现力的表示，从而提升导航性能。
3. 实验结果表明，LongFly在成功率和成功率加权路径长度方面均优于现有方法，并在不同环境中表现出一致性。

## 📝 摘要（中文）

本文提出LongFly，一个用于长程无人机视觉-语言导航的时空上下文建模框架。针对灾后搜救等场景中无人机导航面临的信息密度高、视角变化快和动态结构等挑战，现有方法难以有效建模长程时空上下文，导致语义对齐不准确和路径规划不稳定。LongFly提出了一种历史感知时空建模策略，将碎片化和冗余的历史数据转换为结构化、紧凑和富有表现力的表示。首先，提出了基于槽位的历史图像压缩模块，动态地将多视角历史观测提炼成固定长度的上下文表示。然后，引入时空轨迹编码模块，以捕获无人机轨迹的时间动态和空间结构。最后，为了将现有的时空上下文与当前的观测相结合，设计了提示引导的多模态融合模块，以支持基于时间的推理和鲁棒的航点预测。实验结果表明，LongFly在成功率方面比最先进的无人机VLN基线高出7.89%，在成功率加权路径长度方面高出6.33%，在已见和未见环境中均表现出一致的性能。

## 🔬 方法详解

**问题定义**：无人机在复杂环境下的长程视觉-语言导航任务，尤其是在灾后搜救等场景中，面临信息密度高、视角变化快、动态结构等挑战。现有方法难以有效建模长程时空上下文，导致语义对齐不准确，路径规划不稳定，最终影响导航的成功率和效率。现有方法通常无法有效地利用历史观测信息，或者无法将历史信息与当前观测进行有效融合。

**核心思路**：LongFly的核心思路是构建一个能够有效建模长程时空上下文的框架。通过将碎片化和冗余的历史数据转换为结构化、紧凑和富有表现力的表示，从而提升导航性能。该框架通过历史图像压缩、时空轨迹编码和多模态融合等模块，实现对历史信息的有效提取、编码和利用。

**技术框架**：LongFly框架主要包含三个模块：1) 基于槽位的历史图像压缩模块：动态地将多视角历史观测提炼成固定长度的上下文表示。2) 时空轨迹编码模块：捕获无人机轨迹的时间动态和空间结构。3) 提示引导的多模态融合模块：将现有的时空上下文与当前的观测相结合，支持基于时间的推理和鲁棒的航点预测。

**关键创新**：LongFly的关键创新在于其历史感知时空建模策略。该策略能够有效地将碎片化和冗余的历史数据转换为结构化、紧凑和富有表现力的表示。此外，提示引导的多模态融合模块能够有效地将历史信息与当前观测进行融合，从而提升导航性能。与现有方法相比，LongFly能够更好地利用历史信息，并实现更准确的语义对齐和更稳定的路径规划。

**关键设计**：基于槽位的历史图像压缩模块采用动态注意力机制，选择性地提取历史图像中的关键信息。时空轨迹编码模块使用Transformer网络，捕获轨迹的时间依赖关系和空间结构。提示引导的多模态融合模块使用Prompt Learning，引导模型关注与导航指令相关的关键信息。损失函数包括导航损失和辅助损失，用于优化模型的导航性能和上下文建模能力。具体参数设置未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22010v1/picture/motivation12-22.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22010v1/picture/overview9.17.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22010v1/picture/shic.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

LongFly在无人机视觉-语言导航任务中取得了显著的性能提升。实验结果表明，LongFly在成功率方面比最先进的无人机VLN基线高出7.89%，在成功率加权路径长度方面高出6.33%，并且在已见和未见环境中均表现出一致的性能。这些结果表明，LongFly能够有效地建模长程时空上下文，并提升无人机的导航能力。

## 🎯 应用场景

LongFly在灾后搜救、环境监测、智能巡检等领域具有广泛的应用前景。该方法可以帮助无人机在复杂环境中实现自主导航，提高任务效率和安全性。未来，LongFly可以进一步扩展到其他机器人平台，例如地面机器人和水下机器人，从而实现更广泛的应用。

## 📄 摘要（原文）

> Unmanned aerial vehicles (UAVs) are crucial tools for post-disaster search and rescue, facing challenges such as high information density, rapid changes in viewpoint, and dynamic structures, especially in long-horizon navigation. However, current UAV vision-and-language navigation(VLN) methods struggle to model long-horizon spatiotemporal context in complex environments, resulting in inaccurate semantic alignment and unstable path planning. To this end, we propose LongFly, a spatiotemporal context modeling framework for long-horizon UAV VLN. LongFly proposes a history-aware spatiotemporal modeling strategy that transforms fragmented and redundant historical data into structured, compact, and expressive representations. First, we propose the slot-based historical image compression module, which dynamically distills multi-view historical observations into fixed-length contextual representations. Then, the spatiotemporal trajectory encoding module is introduced to capture the temporal dynamics and spatial structure of UAV trajectories. Finally, to integrate existing spatiotemporal context with current observations, we design the prompt-guided multimodal integration module to support time-based reasoning and robust waypoint prediction. Experimental results demonstrate that LongFly outperforms state-of-the-art UAV VLN baselines by 7.89\% in success rate and 6.33\% in success weighted by path length, consistently across both seen and unseen environments.

