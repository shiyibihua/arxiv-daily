---
layout: default
title: SPIDER: Scalable Physics-Informed Dexterous Retargeting
---

# SPIDER: Scalable Physics-Informed Dexterous Retargeting

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.09484" target="_blank" class="toolbar-btn">arXiv: 2511.09484v1</a>
    <a href="https://arxiv.org/pdf/2511.09484.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.09484v1" 
            onclick="toggleFavorite(this, '2511.09484v1', 'SPIDER: Scalable Physics-Informed Dexterous Retargeting')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Chaoyi Pan, Changhao Wang, Haozhi Qi, Zixi Liu, Homanga Bharadhwaj, Akash Sharma, Tingfan Wu, Guanya Shi, Jitendra Malik, Francois Hogan

**分类**: cs.RO, cs.CV

**发布日期**: 2025-11-12

**备注**: Project website: https://jc-bao.github.io/spider-project/

---

## 💡 一句话要点

**SPIDER：可扩展的基于物理信息的灵巧重定向框架，用于生成机器人控制策略。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人控制` `灵巧操作` `运动重定向` `物理引擎` `强化学习` `数据增强` `人形机器人`

## 📋 核心要点

1. 现有机器人灵巧操作策略学习面临数据稀缺问题，直接在机器人上收集数据成本高昂。
2. SPIDER利用人类运动数据提供全局任务结构，结合物理引擎采样和虚拟接触引导，生成动态可行的机器人轨迹。
3. 实验表明，SPIDER在多种机器人和数据集上表现出色，成功率提升显著，且效率远高于强化学习方法。

## 📝 摘要（中文）

针对人形机器人和灵巧手控制策略学习需要大规模演示数据的问题，提出了一种可扩展的基于物理信息的灵巧重定向框架（SPIDER）。该框架旨在将仅包含运动学信息的人类演示数据转换为动态可行的机器人轨迹，从而解决机器人数据稀缺问题。SPIDER的核心思想是利用人类演示数据提供全局任务结构和目标，并通过大规模的基于物理的采样和课程学习式的虚拟接触引导来优化轨迹，确保动力学可行性和正确的接触序列。SPIDER在9种人形/灵巧手机器人和6个数据集上进行了验证，相比标准采样方法，成功率提高了18%，并且比强化学习基线快10倍，能够生成包含240万帧的动态可行机器人数据集，用于策略学习。SPIDER作为一种通用的基于物理的重定向方法，可以处理各种质量的数据，并生成多样且高质量的数据，从而实现使用强化学习等方法进行高效的策略学习。

## 🔬 方法详解

**问题定义**：论文旨在解决人形机器人和灵巧手控制策略学习中，由于机器人数据收集成本高昂导致的数据稀缺问题。现有方法难以直接将人类运动数据应用于机器人控制，因为人类运动数据通常只包含运动学信息，缺乏动力学信息（如力和力矩），并且存在机器人和人类的形态差异（embodiment gap）。

**核心思路**：论文的核心思路是将人类演示数据视为全局任务结构的指导，利用物理引擎进行大规模采样，并通过课程学习式的虚拟接触引导来优化轨迹。这样既能利用人类数据的全局信息，又能保证生成的机器人轨迹在动力学上是可行的。

**技术框架**：SPIDER框架包含以下几个主要阶段：1) 从人类演示数据中提取全局任务目标。2) 使用物理引擎对机器人的运动轨迹进行采样。3) 利用课程学习式的虚拟接触引导，逐步优化采样得到的轨迹，使其满足动力学约束，并保证正确的接触序列。4) 生成大规模的动态可行机器人数据集，用于后续的策略学习。

**关键创新**：SPIDER的关键创新在于将人类运动数据作为全局指导，结合物理引擎采样和课程学习式的虚拟接触引导。这种方法能够有效地将人类运动数据迁移到机器人上，并生成动态可行的机器人轨迹。与现有方法相比，SPIDER不需要大量的机器人数据，并且能够生成高质量的训练数据。

**关键设计**：SPIDER使用课程学习的方式来引导虚拟接触。具体来说，首先引导机器人与环境进行粗略的接触，然后逐步提高接触的精度和复杂性。这种课程学习的方式能够有效地避免陷入局部最优解，并提高轨迹优化的效率。此外，SPIDER还使用了多种损失函数来约束机器人的运动轨迹，例如动力学约束、接触约束等。

## 📊 实验亮点

SPIDER在9种人形/灵巧手机器人和6个数据集上进行了验证，实验结果表明，相比标准采样方法，SPIDER的成功率提高了18%，并且比强化学习基线快10倍。SPIDER能够生成包含240万帧的动态可行机器人数据集，为后续的策略学习提供了有力支持。

## 🎯 应用场景

SPIDER框架可广泛应用于机器人灵巧操作、人机协作等领域。通过利用现成的人类运动数据，可以快速生成大量高质量的机器人训练数据，从而加速机器人控制策略的学习和部署。该方法还可用于虚拟现实、游戏等领域，生成更加逼真的机器人动画。

## 📄 摘要（原文）

> Learning dexterous and agile policy for humanoid and dexterous hand control requires large-scale demonstrations, but collecting robot-specific data is prohibitively expensive. In contrast, abundant human motion data is readily available from motion capture, videos, and virtual reality, which could help address the data scarcity problem. However, due to the embodiment gap and missing dynamic information like force and torque, these demonstrations cannot be directly executed on robots. To bridge this gap, we propose Scalable Physics-Informed DExterous Retargeting (SPIDER), a physics-based retargeting framework to transform and augment kinematic-only human demonstrations to dynamically feasible robot trajectories at scale. Our key insight is that human demonstrations should provide global task structure and objective, while large-scale physics-based sampling with curriculum-style virtual contact guidance should refine trajectories to ensure dynamical feasibility and correct contact sequences. SPIDER scales across diverse 9 humanoid/dexterous hand embodiments and 6 datasets, improving success rates by 18% compared to standard sampling, while being 10X faster than reinforcement learning (RL) baselines, and enabling the generation of a 2.4M frames dynamic-feasible robot dataset for policy learning. As a universal physics-based retargeting method, SPIDER can work with diverse quality data and generate diverse and high-quality data to enable efficient policy learning with methods like RL.

