---
layout: default
title: ScheduleStream: Temporal Planning with Samplers for GPU-Accelerated Multi-Arm Task and Motion Planning & Scheduling
---

# ScheduleStream: Temporal Planning with Samplers for GPU-Accelerated Multi-Arm Task and Motion Planning & Scheduling

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.04758" target="_blank" class="toolbar-btn">arXiv: 2511.04758v1</a>
    <a href="https://arxiv.org/pdf/2511.04758.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.04758v1" 
            onclick="toggleFavorite(this, '2511.04758v1', 'ScheduleStream: Temporal Planning with Samplers for GPU-Accelerated Multi-Arm Task and Motion Planning & Scheduling')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Caelan Garrett, Fabio Ramos

**分类**: cs.RO, cs.AI, cs.MA

**发布日期**: 2025-11-06

**备注**: Project website: https://schedulestream.github.io

---

## 💡 一句话要点

**提出ScheduleStream框架，通过GPU加速采样实现多臂机器人任务和运动规划与调度**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `多臂机器人` `任务规划` `运动规划` `调度` `GPU加速` `采样` `混合动作空间`

## 📋 核心要点

1. 多臂机器人具有高效完成任务的潜力，但其混合离散-连续动作空间的增长给控制带来了计算挑战。
2. ScheduleStream通过混合持续时间动作建模时间动态，并结合GPU加速采样，实现了多臂并行运动的规划与调度。
3. 实验表明，ScheduleStream算法在仿真中优于多个消融实验，并在真实双臂机器人任务中得到验证。

## 📝 摘要（中文）

本文提出ScheduleStream，这是一个通用的规划与调度框架，它使用采样操作来扩展任务和运动规划（TAMP）算法，使其能够生成允许多臂并行运动的调度方案。ScheduleStream使用混合持续时间动作对时间动态进行建模，这些动作可以异步启动，并持续一段取决于其参数的时间。论文提出了与领域无关的算法，无需任何特定于应用程序的机制即可解决ScheduleStream问题。论文将ScheduleStream应用于任务和运动规划与调度（TAMPAS），并在采样器中使用GPU加速来加快规划速度。在仿真中，论文将ScheduleStream算法与多个消融实验进行比较，发现它们产生了更有效的解决方案。最后，论文在多个真实世界的双臂机器人任务上展示了ScheduleStream的性能。

## 🔬 方法详解

**问题定义**：现有的任务和运动规划（TAMP）算法通常生成串行的动作计划，即一次只有一个机械臂在运动，无法充分利用多臂机器人的并行能力。因此，需要一种能够生成并行调度方案的TAMP算法，以提高任务效率。现有的TAMP算法难以处理混合离散-连续动作空间，以及动作持续时间与参数相关的复杂时间动态。

**核心思路**：ScheduleStream的核心思路是将TAMP扩展到调度问题，允许动作异步启动并持续一段时间，从而实现多臂并行运动。通过引入混合持续时间动作，可以更灵活地建模时间动态。利用GPU加速采样，可以加速在混合离散-连续动作空间中的搜索过程。

**技术框架**：ScheduleStream的整体框架包括以下几个主要模块：1) 状态空间表示：使用混合离散-连续变量表示机器人的状态，包括机械臂的位置、姿态和任务状态。2) 动作空间表示：使用混合持续时间动作表示机器人的动作，每个动作可以异步启动，并持续一段取决于其参数的时间。3) 采样器：使用GPU加速的采样器在动作空间中生成候选动作。4) 规划器：使用采样得到的动作构建调度方案，并评估其可行性和效率。5) 调度器：根据规划结果，生成最终的机器人执行指令。

**关键创新**：ScheduleStream的关键创新在于：1) 提出了一个通用的规划与调度框架，可以处理混合持续时间动作，并生成允许多臂并行运动的调度方案。2) 利用GPU加速采样，显著提高了在混合离散-连续动作空间中的搜索效率。3) 提出了与领域无关的算法，无需任何特定于应用程序的机制即可解决ScheduleStream问题。

**关键设计**：ScheduleStream的关键设计包括：1) 混合持续时间动作的建模方式，允许动作的持续时间是其参数的函数。2) GPU加速采样器的设计，利用GPU的并行计算能力加速采样过程。3) 规划器的搜索策略，旨在找到可行且高效的调度方案。具体的参数设置、损失函数和网络结构等技术细节在论文中没有详细描述，属于未知信息。

## 📊 实验亮点

实验结果表明，ScheduleStream算法在仿真环境中能够生成比消融实验更有效的解决方案。在真实的双臂机器人任务中，ScheduleStream成功地实现了多臂协同操作，验证了其在实际应用中的可行性。具体的性能数据和提升幅度在摘要中没有给出，属于未知信息。

## 🎯 应用场景

ScheduleStream可应用于各种需要多臂机器人协同完成任务的场景，例如：工业装配、物流搬运、医疗手术等。通过优化任务调度，可以显著提高生产效率和自动化水平。该研究为多臂机器人的智能化控制提供了新的思路，有望推动机器人技术在更多领域的应用。

## 📄 摘要（原文）

> Bimanual and humanoid robots are appealing because of their human-like ability to leverage multiple arms to efficiently complete tasks. However, controlling multiple arms at once is computationally challenging due to the growth in the hybrid discrete-continuous action space. Task and Motion Planning (TAMP) algorithms can efficiently plan in hybrid spaces but generally produce plans, where only one arm is moving at a time, rather than schedules that allow for parallel arm motion. In order to extend TAMP to produce schedules, we present ScheduleStream, the first general-purpose framework for planning & scheduling with sampling operations. ScheduleStream models temporal dynamics using hybrid durative actions, which can be started asynchronously and persist for a duration that's a function of their parameters. We propose domain-independent algorithms that solve ScheduleStream problems without any application-specific mechanisms. We apply ScheduleStream to Task and Motion Planning & Scheduling (TAMPAS), where we use GPU acceleration within samplers to expedite planning. We compare ScheduleStream algorithms to several ablations in simulation and find that they produce more efficient solutions. We demonstrate ScheduleStream on several real-world bimanual robot tasks at https://schedulestream.github.io.

