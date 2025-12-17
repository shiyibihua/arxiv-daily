---
layout: default
title: Autonomous Reinforcement Learning Robot Control with Intel's Loihi 2 Neuromorphic Hardware
---

# Autonomous Reinforcement Learning Robot Control with Intel's Loihi 2 Neuromorphic Hardware

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.03911" target="_blank" class="toolbar-btn">arXiv: 2512.03911v1</a>
    <a href="https://arxiv.org/pdf/2512.03911.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.03911v1" 
            onclick="toggleFavorite(this, '2512.03911v1', 'Autonomous Reinforcement Learning Robot Control with Intel\'s Loihi 2 Neuromorphic Hardware')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Kenneth Stewart, Roxana Leontie, Samantha Chapin, Joe Hays, Sumit Bam Shrestha, Carl Glen Henshaw

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-12-03

**备注**: Submitted for review at NICE 2026 (Neuro-Inspired Computational Elements) conference

---

## 💡 一句话要点

**提出基于Loihi 2神经形态硬件的自主强化学习机器人控制方案**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `神经形态计算` `强化学习` `机器人控制` `Loihi 2` `Sigma-Delta神经网络`

## 📋 核心要点

1. 现有机器人控制方法在能效和实时性方面存在挑战，尤其是在资源受限的环境中。
2. 论文提出将强化学习训练的ANN转换为SDNN，并在Intel Loihi 2神经形态硬件上部署，以实现低功耗和低延迟的机器人控制。
3. 实验表明，该方法能够在NVIDIA Omniverse Isaac Lab中实现Astrobee机器人的闭环控制，验证了神经形态硬件在机器人控制中的可行性。

## 📝 摘要（中文）

本文提出了一种端到端的流程，用于在神经形态硬件上部署强化学习（RL）训练的人工神经网络（ANN），方法是将它们转换为脉冲Sigma-Delta神经网络（SDNN）。我们证明了完全在仿真中训练的ANN策略可以转换为与Intel的Loihi 2架构兼容的SDNN，从而实现低延迟和高能效的推理。作为一个测试用例，我们使用了一个RL策略来控制Astrobee自由飞行机器人，类似于先前在太空硬件中验证过的控制器。该策略使用修正线性单元（ReLU）进行训练，然后转换为SDNN并部署在Intel的Loihi 2上，并在NVIDIA的Omniverse Isaac Lab仿真环境中进行评估，以实现Astrobee运动的闭环控制。我们比较了GPU和Loihi 2之间的执行性能。结果突出了使用神经形态平台进行机器人控制的可行性，并为未来空间和地面机器人应用中节能、实时的神经形态计算建立了一条途径。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人控制中能效和实时性之间的矛盾，尤其是在空间机器人等资源受限场景下。传统的机器人控制方法，如基于GPU的深度学习，虽然性能强大，但在功耗方面存在劣势，难以满足长时间自主运行的需求。

**核心思路**：论文的核心思路是将强化学习训练得到的ANN策略转换为脉冲神经网络（SNN），特别是Sigma-Delta神经网络（SDNN），并利用Intel Loihi 2神经形态硬件进行部署。SNN具有事件驱动的特性，能够显著降低功耗，而Loihi 2则提供了专门的硬件加速，从而实现低延迟和高能效的机器人控制。

**技术框架**：整体流程包括三个主要阶段：1) 在仿真环境中训练基于ReLU激活函数的ANN策略；2) 将训练好的ANN策略转换为SDNN，使其兼容Loihi 2架构；3) 在NVIDIA Omniverse Isaac Lab仿真环境中，使用Loihi 2控制Astrobee机器人进行闭环控制。该框架实现了从仿真训练到硬件部署的端到端流程。

**关键创新**：论文的关键创新在于将传统的ANN策略成功迁移到神经形态硬件上，并验证了其在机器人控制中的可行性。通过将ANN转换为SDNN，并利用Loihi 2的硬件加速，实现了低功耗和低延迟的机器人控制。此外，该研究还提供了一个完整的流程，为未来在神经形态硬件上部署强化学习策略提供了参考。

**关键设计**：论文中，ANN策略使用ReLU激活函数进行训练，然后通过Sigma-Delta编码转换为SDNN。SDNN的设计需要考虑Loihi 2的硬件特性，例如神经元的连接方式和脉冲发放机制。在仿真环境中，使用NVIDIA Omniverse Isaac Lab进行闭环控制的评估，并与GPU的执行性能进行比较。具体的参数设置和网络结构细节未在摘要中详细说明，需要参考论文全文。

## 📊 实验亮点

论文成功地将强化学习训练的ANN策略部署在Intel Loihi 2神经形态硬件上，并实现了Astrobee机器人的闭环控制。虽然摘要中没有给出具体的性能数据，但强调了Loihi 2在低延迟和高能效方面的优势，并与GPU的执行性能进行了比较，突出了神经形态平台在机器人控制中的潜力。

## 🎯 应用场景

该研究成果可应用于空间机器人、无人机、移动机器人等领域，尤其是在对功耗和实时性要求较高的场景下。例如，在深空探测任务中，机器人需要在资源有限的环境下长时间自主运行，神经形态硬件的低功耗特性将发挥重要作用。此外，该技术还可以应用于智能家居、自动驾驶等领域，实现更加节能和高效的控制系统。

## 📄 摘要（原文）

> We present an end-to-end pipeline for deploying reinforcement learning (RL) trained Artificial Neural Networks (ANNs) on neuromorphic hardware by converting them into spiking Sigma-Delta Neural Networks (SDNNs). We demonstrate that an ANN policy trained entirely in simulation can be transformed into an SDNN compatible with Intel's Loihi 2 architecture, enabling low-latency and energy-efficient inference. As a test case, we use an RL policy for controlling the Astrobee free-flying robot, similar to a previously hardware in space-validated controller. The policy, trained with Rectified Linear Units (ReLUs), is converted to an SDNN and deployed on Intel's Loihi 2, then evaluated in NVIDIA's Omniverse Isaac Lab simulation environment for closed-loop control of Astrobee's motion. We compare execution performance between GPU and Loihi 2. The results highlight the feasibility of using neuromorphic platforms for robotic control and establish a pathway toward energy-efficient, real-time neuromorphic computation in future space and terrestrial robotics applications.

