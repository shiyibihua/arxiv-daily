---
layout: default
title: An efficient deep reinforcement learning environment for flexible job-shop scheduling
---

# An efficient deep reinforcement learning environment for flexible job-shop scheduling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07019" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07019v1</a>
  <a href="https://arxiv.org/pdf/2509.07019.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07019v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07019v1', 'An efficient deep reinforcement learning environment for flexible job-shop scheduling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinquan Wu, Xuefeng Yan, Mingqiang Wei, Donghai Guan

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-07

---

## 💡 一句话要点

**针对柔性作业车间调度，提出一种高效的深度强化学习环境。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `柔性作业车间调度` `深度强化学习` `离散事件模拟` `近端策略优化` `调度环境` `状态表示` `奖励函数`

## 📋 核心要点

1. 现有DRL解决FJSP问题的方法侧重于Agent设计，忽略了DRL环境的建模，限制了调度性能。
2. 论文提出一种基于离散事件模拟的简单时间顺序DRL环境，并设计了新颖的状态表示和奖励函数。
3. 实验表明，该环境能有效提升简单调度规则的性能，且DRL模型性能与现有方法相比具有竞争力。

## 📝 摘要（中文）

柔性作业车间调度问题(FJSP)是一个经典的组合优化问题，在现实世界中有着广泛的应用。为了为FJSP生成快速而精确的调度方案，已经开发了各种深度强化学习(DRL)调度方法。然而，这些方法主要集中在DRL调度Agent的设计上，而忽略了DRL环境的建模。本文提出了一种基于离散事件模拟的简单时间顺序DRL环境用于FJSP，并提出了一种基于近端策略优化(PPO)的端到端DRL调度模型。此外，本文基于调度环境中的两个状态变量，提出了一种新颖的FJSP短状态表示，并基于机器的调度区域设计了一种新颖的、易于理解的奖励函数。在公共基准实例上的实验结果表明，在我们的调度环境中，简单优先级调度规则(PDR)的性能得到了提高，并且我们的DRL调度模型与OR-Tools、元启发式算法、DRL和PDR调度方法相比，获得了具有竞争力的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决柔性作业车间调度问题(FJSP)，这是一个经典的组合优化问题。现有的DRL方法主要关注于设计复杂的DRL Agent，而忽略了DRL环境的建模，这限制了调度算法的效率和性能。现有方法在状态表示和奖励函数设计方面存在不足，导致学习效率低下。

**核心思路**：论文的核心思路是构建一个高效的DRL环境，该环境能够简化状态表示，并提供易于理解的奖励信号，从而加速DRL Agent的学习过程。通过精心设计的环境，可以更容易地训练出高性能的调度策略。

**技术框架**：整体框架包括一个基于离散事件模拟的DRL环境和一个基于近端策略优化(PPO)的DRL Agent。环境负责模拟FJSP的调度过程，并向Agent提供状态信息和奖励信号。Agent根据状态信息选择动作，并根据奖励信号更新策略。整个过程是一个端到端的学习过程。

**关键创新**：论文的关键创新在于提出了一个简单的时间顺序DRL环境，并设计了一种新颖的FJSP短状态表示和易于理解的奖励函数。这种环境能够有效地简化调度问题的复杂性，并加速DRL Agent的学习过程。与现有方法相比，该环境更加高效和易于使用。

**关键设计**：状态表示基于调度环境中的两个状态变量，具体细节未知。奖励函数基于机器的调度区域设计，旨在提供更直接和可解释的奖励信号。DRL Agent采用PPO算法进行训练，PPO是一种常用的策略梯度算法，具有较好的稳定性和收敛性。具体的网络结构和参数设置未知。

## 📊 实验亮点

实验结果表明，在提出的调度环境中，简单优先级调度规则(PDR)的性能得到了提高，这验证了环境的有效性。此外，DRL调度模型与OR-Tools、元启发式算法、DRL和PDR调度方法相比，获得了具有竞争力的性能，表明该方法具有实际应用潜力。具体的性能提升幅度未知。

## 🎯 应用场景

该研究成果可应用于智能制造、生产调度、物流管理等领域，能够提高生产效率、降低生产成本、优化资源配置。通过DRL自动学习调度策略，可以减少人工干预，提高调度的灵活性和适应性。未来可进一步扩展到更复杂的调度场景，如考虑设备故障、物料供应等因素。

## 📄 摘要（原文）

> The Flexible Job-shop Scheduling Problem (FJSP) is a classical combinatorial optimization problem that has a wide-range of applications in the real world. In order to generate fast and accurate scheduling solutions for FJSP, various deep reinforcement learning (DRL) scheduling methods have been developed. However, these methods are mainly focused on the design of DRL scheduling Agent, overlooking the modeling of DRL environment. This paper presents a simple chronological DRL environment for FJSP based on discrete event simulation and an end-to-end DRL scheduling model is proposed based on the proximal policy optimization (PPO). Furthermore, a short novel state representation of FJSP is proposed based on two state variables in the scheduling environment and a novel comprehensible reward function is designed based on the scheduling area of machines. Experimental results on public benchmark instances show that the performance of simple priority dispatching rules (PDR) is improved in our scheduling environment and our DRL scheduling model obtains competing performance compared with OR-Tools, meta-heuristic, DRL and PDR scheduling methods.

