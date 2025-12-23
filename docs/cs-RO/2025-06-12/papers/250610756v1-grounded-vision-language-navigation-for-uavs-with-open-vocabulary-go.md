---
layout: default
title: Grounded Vision-Language Navigation for UAVs with Open-Vocabulary Goal Understanding
---

# Grounded Vision-Language Navigation for UAVs with Open-Vocabulary Goal Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10756" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10756v1</a>
  <a href="https://arxiv.org/pdf/2506.10756.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10756v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10756v1', 'Grounded Vision-Language Navigation for UAVs with Open-Vocabulary Goal Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuhang Zhang, Haosheng Yu, Jiaping Xiao, Mir Feroskhan

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**提出VLFly框架以解决无人机的语言引导导航问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉与语言导航` `无人机` `开放词汇理解` `连续动作空间` `多模态融合`

## 📋 核心要点

1. 现有视觉与语言导航方法在处理分布外环境时泛化能力不足，且依赖固定的离散动作空间，限制了其应用。
2. 本文提出的VLFly框架通过集成指令编码、目标检索和航点规划模块，实现了无人机的语言引导飞行。
3. VLFly在多种仿真环境中表现优异，且在真实室内外环境中展示了强大的开放词汇目标理解和泛化导航能力。

## 📝 摘要（中文）

视觉与语言导航（VLN）是自主机器人领域的一个长期挑战，旨在使代理能够在复杂环境中遵循人类指令进行导航。该领域面临两个主要瓶颈：对分布外环境的泛化能力不足以及对固定离散动作空间的依赖。为了解决这些问题，本文提出了Vision-Language Fly（VLFly）框架，专为无人机设计，能够执行语言引导的飞行。VLFly通过机载单目相机捕获的自我中心观察，输出连续的速度指令，无需定位或主动测距传感器。该框架集成了三个模块：基于大型语言模型的指令编码器、由视觉-语言模型驱动的目标检索器，以及生成可执行轨迹的航点规划器。VLFly在多样化的仿真环境中进行评估，无需额外微调，且始终优于所有基线方法。

## 🔬 方法详解

**问题定义**：本文旨在解决无人机在复杂环境中进行语言引导导航的挑战，现有方法在泛化能力和动作空间上存在明显不足。

**核心思路**：VLFly框架通过不依赖定位或主动测距传感器，利用机载单目相机的自我中心观察，输出连续的速度指令，从而实现灵活的导航。

**技术框架**：VLFly整体架构包括三个主要模块：指令编码器、目标检索器和航点规划器。指令编码器将高层语言转化为结构化提示，目标检索器通过视觉-语言相似性匹配提示与目标图像，航点规划器生成可执行的飞行轨迹。

**关键创新**：VLFly的主要创新在于其开放词汇目标理解能力，能够处理抽象语言输入并在多样化环境中实现有效导航，这与传统方法的固定动作空间设计形成鲜明对比。

**关键设计**：VLFly采用大型语言模型进行指令编码，视觉-语言模型进行目标匹配，航点规划器则基于实时反馈生成轨迹，确保无人机能够在动态环境中灵活应对。

## 📊 实验亮点

VLFly在多样化的仿真环境中表现出色，始终优于所有基线方法，且在真实环境中的实验结果显示其在开放词汇目标理解和导航能力上具有显著提升，具体性能数据未详述。

## 🎯 应用场景

该研究的潜在应用领域包括无人机在搜索与救援、环境监测、物流配送等场景中的自主导航。VLFly框架的开放词汇理解能力使其在处理复杂指令时具有更高的灵活性和适应性，未来可能推动无人机技术在更广泛领域的应用。

## 📄 摘要（原文）

> Vision-and-language navigation (VLN) is a long-standing challenge in autonomous robotics, aiming to empower agents with the ability to follow human instructions while navigating complex environments. Two key bottlenecks remain in this field: generalization to out-of-distribution environments and reliance on fixed discrete action spaces. To address these challenges, we propose Vision-Language Fly (VLFly), a framework tailored for Unmanned Aerial Vehicles (UAVs) to execute language-guided flight. Without the requirement for localization or active ranging sensors, VLFly outputs continuous velocity commands purely from egocentric observations captured by an onboard monocular camera. The VLFly integrates three modules: an instruction encoder based on a large language model (LLM) that reformulates high-level language into structured prompts, a goal retriever powered by a vision-language model (VLM) that matches these prompts to goal images via vision-language similarity, and a waypoint planner that generates executable trajectories for real-time UAV control. VLFly is evaluated across diverse simulation environments without additional fine-tuning and consistently outperforms all baselines. Moreover, real-world VLN tasks in indoor and outdoor environments under direct and indirect instructions demonstrate that VLFly achieves robust open-vocabulary goal understanding and generalized navigation capabilities, even in the presence of abstract language input.

