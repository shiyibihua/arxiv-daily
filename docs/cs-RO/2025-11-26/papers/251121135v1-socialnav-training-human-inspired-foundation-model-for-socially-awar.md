---
layout: default
title: SocialNav: Training Human-Inspired Foundation Model for Socially-Aware Embodied Navigation
---

# SocialNav: Training Human-Inspired Foundation Model for Socially-Aware Embodied Navigation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.21135" target="_blank" class="toolbar-btn">arXiv: 2511.21135v1</a>
    <a href="https://arxiv.org/pdf/2511.21135.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.21135v1" 
            onclick="toggleFavorite(this, '2511.21135v1', 'SocialNav: Training Human-Inspired Foundation Model for Socially-Aware Embodied Navigation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Ziyi Chen, Yingnan Guo, Zedong Chu, Minghua Luo, Yanfen Shen, Mingchao Sun, Junjun Hu, Shichao Xie, Kuan Yang, Pei Shi, Zhining Gu, Lu Liu, Honglin Han, Xiaolong Wu, Mu Xu, Yu Zhang

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-11-26

**🔗 代码/项目**: [PROJECT_PAGE](https://amap-eai.github.io/SocialNav/)

---

## 💡 一句话要点

**提出SocialNav，用于训练类人社交感知具身导航的基础模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `具身导航` `社交感知` `基础模型` `强化学习` `社会规范`

## 📋 核心要点

1. 现有具身导航方法在社交规范遵守方面存在不足，难以生成符合人类习惯的轨迹。
2. SocialNav通过分层架构和多阶段训练，使模型能够理解社会规范并生成符合规范的导航轨迹。
3. 实验表明，SocialNav在导航成功率和社会合规率上均显著优于现有方法，提升分别达到38%和46%。

## 📝 摘要（中文）

本文提出了SocialNav，一个用于社交感知导航的基础模型，它采用分层的“大脑-动作”架构，能够理解高层次的社会规范并生成低层次的、符合社会规范的轨迹。为了实现这种双重能力，构建了SocNav数据集，这是一个包含700万样本的大规模数据集，包括：（1）认知激活数据集，提供社会推理信号，如思维链解释和社会可穿越性预测；（2）专家轨迹金字塔，汇总了来自互联网视频、模拟环境和真实世界机器人的各种导航演示。提出了一个多阶段训练流程，逐步注入和完善导航智能：首先通过模仿学习将通用导航技能和社会规范理解注入模型，然后通过精心设计的社交感知流探索GRPO（SAFE-GRPO）来完善这些技能，这是第一个基于流的具身导航强化学习框架，它明确地奖励符合社会规范的行为。与最先进的方法相比，SocialNav的成功率提高了+38%，社会合规率提高了+46%，表明在导航性能和社会合规性方面都有显著提高。

## 🔬 方法详解

**问题定义**：现有具身导航方法难以在复杂社会环境中进行导航，无法理解和遵守社会规范，导致导航行为不自然甚至违反社会规则。现有方法通常缺乏对社会规范的显式建模和推理能力，难以泛化到不同的社交场景。

**核心思路**：SocialNav的核心思路是构建一个能够理解高层次社会规范并生成低层次、符合社会规范轨迹的基础模型。通过分层架构将社会规范理解和运动控制解耦，并利用大规模数据集进行训练，从而提升模型在社交环境中的导航能力。

**技术框架**：SocialNav采用分层的“大脑-动作”架构。 “大脑”部分负责理解高层次的社会规范，并生成社会推理信号，例如思维链解释和社会可穿越性预测。“动作”部分则根据“大脑”的输出，生成低层次的、符合社会规范的轨迹。整个框架包含SocNav数据集的构建、多阶段训练流程以及SAFE-GRPO强化学习算法。

**关键创新**：SocialNav的关键创新在于：（1）构建了大规模的SocNav数据集，包含认知激活数据和专家轨迹金字塔，为模型训练提供了丰富的数据来源。（2）提出了SAFE-GRPO，一种基于流的强化学习框架，能够显式地奖励符合社会规范的行为，从而提升模型的社会合规性。（3）采用分层架构，将社会规范理解和运动控制解耦，使得模型能够更好地理解和遵守社会规范。

**关键设计**：SocNav数据集包含认知激活数据集和专家轨迹金字塔。认知激活数据集提供社会推理信号，例如思维链解释和社会可穿越性预测。专家轨迹金字塔汇总了来自互联网视频、模拟环境和真实世界机器人的各种导航演示。多阶段训练流程包括模仿学习和强化学习两个阶段。模仿学习阶段用于将通用导航技能和社会规范理解注入模型。强化学习阶段则通过SAFE-GRPO来完善这些技能。SAFE-GRPO是一种基于流的强化学习框架，它明确地奖励符合社会规范的行为。具体损失函数设计未知。

## 📊 实验亮点

SocialNav在实验中取得了显著的成果，与最先进的方法相比，成功率提高了38%，社会合规率提高了46%。这些结果表明，SocialNav在导航性能和社会合规性方面都取得了显著的提升，能够更好地适应复杂的社会环境。

## 🎯 应用场景

SocialNav具有广泛的应用前景，例如服务型机器人、自动驾驶汽车、虚拟现实等。它可以使机器人在复杂的社会环境中更加自然、安全地导航，提升用户体验。例如，服务型机器人可以在商场、医院等场所为人们提供导航服务，自动驾驶汽车可以在城市道路上安全行驶，虚拟现实中的虚拟角色可以更加真实地与用户互动。

## 📄 摘要（原文）

> Embodied navigation that adheres to social norms remains an open research challenge. Our \textbf{SocialNav} is a foundational model for socially-aware navigation with a hierarchical "brain-action" architecture, capable of understanding high-level social norms and generating low-level, socially compliant trajectories. To enable such dual capabilities, we construct the SocNav Dataset, a large-scale collection of 7 million samples, comprising (1) a Cognitive Activation Dataset providing social reasoning signals such as chain-of-thought explanations and social traversability prediction, and (2) an Expert Trajectories Pyramid aggregating diverse navigation demonstrations from internet videos, simulated environments, and real-world robots. A multi-stage training pipeline is proposed to gradually inject and refine navigation intelligence: we first inject general navigation skills and social norms understanding into the model via imitation learning, and then refine such skills through a deliberately designed Socially-Aware Flow Exploration GRPO (SAFE-GRPO), the first flow-based reinforcement learning framework for embodied navigation that explicitly rewards socially compliant behaviors. SocialNav achieves +38% success rate and +46% social compliance rate compared to the state-of-the-art method, demonstrating strong gains in both navigation performance and social compliance. Our project page: https://amap-eai.github.io/SocialNav/

