---
layout: default
title: Control of Microrobots with Reinforcement Learning under On-Device Compute Constraints
---

# Control of Microrobots with Reinforcement Learning under On-Device Compute Constraints

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24740" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24740v1</a>
  <a href="https://arxiv.org/pdf/2512.24740.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24740v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24740v1', 'Control of Microrobots with Reinforcement Learning under On-Device Compute Constraints')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yichen Liu, Kesava Viswanadha, Zhongyu Li, Nelson Lojo, Kristofer S. J. Pister

**分类**: cs.RO, eess.SY

**发布日期**: 2025-12-31

**备注**: 9 pages, 10 figures

---

## 💡 一句话要点

**提出一种边缘计算约束下的强化学习微型机器人控制方法，实现低延迟鲁棒运动。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `微型机器人` `强化学习` `边缘计算` `领域随机化` `整数量化` `片上系统` `低功耗控制`

## 📋 核心要点

1. 微型机器人在复杂地形上的鲁棒运动控制面临计算资源、内存和功耗的严格限制，传统的控制方法难以满足需求。
2. 该论文提出了一种基于边缘机器学习的强化学习控制方法，通过在资源受限的片上系统上部署紧凑型神经网络策略，实现低延迟控制。
3. 通过领域随机化训练和整数量化技术，提升了策略的鲁棒性和推理速度，并在真实大型机器人上验证了领域随机化训练的有效性。

## 📝 摘要（中文）

本文探索了一种用于微型机器人运动的边缘机器学习方法，允许在计算、内存和功率约束下进行片上、低延迟控制。本文研究了亚厘米级四足微型机器人的运动，通过强化学习(RL)训练控制器，并将其部署在超小型片上系统(SoC) SCμM-3C上，该系统采用运行在5 MHz的ARM Cortex-M0微控制器。我们在大规模并行GPU模拟中训练了一个紧凑的FP32多层感知器(MLP)策略，该策略具有两个隐藏层([128, 64])，并通过对模拟参数进行域随机化来增强鲁棒性。然后，我们研究整数(Int8)量化(per-tensor和per-feature)，以便在资源受限的硬件上实现更高的推理更新速率，并通过Cortex-M0上推理的每次更新周期模型，将硬件功率预算与可实现的更新频率联系起来。我们提出了一种资源感知的步态调度观点：给定设备功率预算，我们可以选择以相应的可行更新频率最大化预期RL奖励的步态模式(小跑/中间/疾驰)。最后，我们将MLP策略部署在不平坦地形上的真实大型机器人上，定性地注意到，域随机化训练可以提高分布外稳定性。我们不声称在这项工作中实现真实世界大型机器人的经验零样本迁移。

## 🔬 方法详解

**问题定义**：微型机器人在实际应用中，需要在计算资源极其有限的条件下，实现复杂地形上的稳定运动控制。传统的控制算法往往计算量大，难以在微型机器人的片上系统上实时运行。此外，真实环境与仿真环境存在差异，导致在仿真环境中训练的策略在真实环境中表现不佳。

**核心思路**：该论文的核心思路是利用强化学习训练一个紧凑型神经网络策略，并将其部署在资源受限的片上系统上。通过领域随机化技术，提高策略在不同环境下的泛化能力。同时，采用整数量化技术，降低模型的计算复杂度和内存占用，从而提高推理速度。

**技术框架**：整体框架包括三个主要阶段：1) 在GPU上进行强化学习训练，得到一个FP32精度的MLP策略；2) 对MLP策略进行整数量化，得到Int8精度的模型；3) 将量化后的模型部署到ARM Cortex-M0微控制器上，进行实时控制。此外，论文还提出了资源感知的步态调度方法，根据设备功率预算选择合适的步态模式。

**关键创新**：该论文的关键创新在于将强化学习与边缘计算相结合，提出了一种适用于资源受限微型机器人的控制方法。通过领域随机化和整数量化，提高了策略的鲁棒性和推理速度。此外，资源感知的步态调度方法能够根据设备功率预算动态调整控制策略，从而实现更高效的能量利用。

**关键设计**：MLP策略采用两层隐藏层结构，大小分别为[128, 64]。强化学习算法采用未知（论文未明确指出）。领域随机化通过随机改变仿真环境的参数，如摩擦系数、地形高度等，来提高策略的泛化能力。整数量化采用per-tensor和per-feature两种方式。资源感知的步态调度方法根据不同步态模式的功率消耗和预期奖励，选择最优的步态模式。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24740v1/figures/scum_robot.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24740v1/figures/hardware_config.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24740v1/figures/matlab_model.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该论文在仿真环境中训练了一个紧凑的MLP策略，并通过领域随机化和整数量化技术，成功将其部署在资源受限的ARM Cortex-M0微控制器上。定性实验表明，领域随机化训练可以提高策略在真实大型机器人上的稳定性。虽然论文没有提供具体的性能数据，但其提出的方法为微型机器人的边缘计算控制提供了一种可行的解决方案。

## 🎯 应用场景

该研究成果可应用于微型机器人在复杂环境下的自主导航、搜索救援、医疗诊断等领域。通过在边缘设备上实现低延迟、鲁棒的控制，可以提高微型机器人的自主性和适应性，使其能够在各种实际场景中发挥作用。未来，该技术有望推动微型机器人在工业、医疗、军事等领域的广泛应用。

## 📄 摘要（原文）

> An important function of autonomous microrobots is the ability to perform robust movement over terrain. This paper explores an edge ML approach to microrobot locomotion, allowing for on-device, lower latency control under compute, memory, and power constraints. This paper explores the locomotion of a sub-centimeter quadrupedal microrobot via reinforcement learning (RL) and deploys the resulting controller on an ultra-small system-on-chip (SoC), SC$μ$M-3C, featuring an ARM Cortex-M0 microcontroller running at 5 MHz. We train a compact FP32 multilayer perceptron (MLP) policy with two hidden layers ($[128, 64]$) in a massively parallel GPU simulation and enhance robustness by utilizing domain randomization over simulation parameters. We then study integer (Int8) quantization (per-tensor and per-feature) to allow for higher inference update rates on our resource-limited hardware, and we connect hardware power budgets to achievable update frequency via a cycles-per-update model for inference on our Cortex-M0. We propose a resource-aware gait scheduling viewpoint: given a device power budget, we can select the gait mode (trot/intermediate/gallop) that maximizes expected RL reward at a corresponding feasible update frequency. Finally, we deploy our MLP policy on a real-world large-scale robot on uneven terrain, qualitatively noting that domain-randomized training can improve out-of-distribution stability. We do not claim real-world large-robot empirical zero-shot transfer in this work.

