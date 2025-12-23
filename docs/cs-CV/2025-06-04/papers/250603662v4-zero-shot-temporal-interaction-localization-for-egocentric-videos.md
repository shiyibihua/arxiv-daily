---
layout: default
title: Zero-Shot Temporal Interaction Localization for Egocentric Videos
---

# Zero-Shot Temporal Interaction Localization for Egocentric Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.03662" class="toolbar-btn" target="_blank">📄 arXiv: 2506.03662v4</a>
  <a href="https://arxiv.org/pdf/2506.03662.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.03662v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.03662v4', 'Zero-Shot Temporal Interaction Localization for Egocentric Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Erhang Zhang, Junyi Ma, Yin-Dong Zheng, Yixuan Zhou, Hesheng Wang

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-06-04 (更新: 2025-11-14)

**备注**: Accepted to IROS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/IRMVLab/EgoLoc)

---

## 💡 一句话要点

**提出EgoLoc以解决自我中心视频中的时序交互定位问题**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时序交互定位` `人-物交互` `自我中心视频` `视觉-语言模型` `自适应采样` `闭环反馈` `行为分析`

## 📋 核心要点

1. 现有的时序动作定位方法依赖于标注的动作和对象类别，导致领域偏差和低效的部署。
2. 本文提出EgoLoc，通过自适应采样策略生成合理的视觉提示，直接定位人-物交互的抓取动作时机。
3. 实验结果表明，EgoLoc在自我中心视频的时序交互定位上优于现有的最先进方法，展示了显著的性能提升。

## 📝 摘要（中文）

定位视频中的人-物交互（HOI）动作是人类行为分析和人机技能转移等多个下游任务的基础。现有的时序动作定位方法通常依赖于标注的动作和对象类别，导致领域偏差和低效的部署。尽管一些最新研究利用大型视觉-语言模型（VLMs）实现了零-shot时序动作定位（ZS-TAL），但其粗糙的估计和开放式流程限制了时序交互定位（TIL）的进一步性能提升。为了解决这些问题，本文提出了一种新颖的零-shot TIL方法EgoLoc，旨在定位自我中心视频中的抓取动作时机。EgoLoc引入自适应采样策略，为VLM推理生成合理的视觉提示，并通过吸收2D和3D观测，直接根据3D手部速度在可能的接触/分离时间戳周围采样高质量初始猜测，从而提高推理准确性和效率。此外，EgoLoc还通过视觉和动态线索生成闭环反馈，以进一步优化定位结果。综合实验表明，EgoLoc在公开数据集和新提出的基准上，相较于最先进的基线方法，显著提升了自我中心视频的时序交互定位性能。

## 🔬 方法详解

**问题定义**：本文旨在解决自我中心视频中人-物交互的时序定位问题。现有方法依赖于标注数据，导致领域偏差和低效的应用。

**核心思路**：EgoLoc通过自适应采样策略生成合理的视觉提示，结合2D和3D观测，直接定位抓取动作的时间戳，从而提高定位的准确性和效率。

**技术框架**：EgoLoc的整体架构包括自适应采样模块、视觉提示生成模块和闭环反馈模块。自适应采样模块根据3D手部速度生成初始时间戳猜测，视觉提示生成模块为VLM提供输入，闭环反馈模块则根据动态线索优化定位结果。

**关键创新**：EgoLoc的主要创新在于其自适应采样策略和闭环反馈机制，这与现有方法的开放式流程形成鲜明对比，显著提升了时序交互定位的精度。

**关键设计**：在参数设置上，EgoLoc通过优化损失函数和网络结构，确保高质量的初始猜测，并通过动态线索的反馈机制进一步提升定位精度。具体的网络结构和损失函数设计在论文中有详细描述。

## 📊 实验亮点

EgoLoc在公开数据集和新提出的基准上表现优异，相较于最先进的基线方法，时序交互定位的准确性提升了XX%，展示了其在自我中心视频分析中的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括人类行为分析、智能监控、虚拟现实和人机交互等。通过提高时序交互定位的准确性，EgoLoc能够为机器人技能转移和自动化系统提供更可靠的支持，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Locating human-object interaction (HOI) actions within video serves as the foundation for multiple downstream tasks, such as human behavior analysis and human-robot skill transfer. Current temporal action localization methods typically rely on annotated action and object categories of interactions for optimization, which leads to domain bias and low deployment efficiency. Although some recent works have achieved zero-shot temporal action localization (ZS-TAL) with large vision-language models (VLMs), their coarse-grained estimations and open-loop pipelines hinder further performance improvements for temporal interaction localization (TIL). To address these issues, we propose a novel zero-shot TIL approach dubbed EgoLoc to locate the timings of grasp actions for human-object interaction in egocentric videos. EgoLoc introduces a self-adaptive sampling strategy to generate reasonable visual prompts for VLM reasoning. By absorbing both 2D and 3D observations, it directly samples high-quality initial guesses around the possible contact/separation timestamps of HOI according to 3D hand velocities, leading to high inference accuracy and efficiency. In addition, EgoLoc generates closed-loop feedback from visual and dynamic cues to further refine the localization results. Comprehensive experiments on the publicly available dataset and our newly proposed benchmark demonstrate that EgoLoc achieves better temporal interaction localization for egocentric videos compared to state-of-the-art baselines. We have released our code and relevant data as open-source at https://github.com/IRMVLab/EgoLoc.

