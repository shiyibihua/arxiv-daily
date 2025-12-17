---
layout: default
title: A Threshold-Triggered Deep Q-Network-Based Framework for Self-Healing in Autonomic Software-Defined IIoT-Edge Networks
---

# A Threshold-Triggered Deep Q-Network-Based Framework for Self-Healing in Autonomic Software-Defined IIoT-Edge Networks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14297" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14297v1</a>
  <a href="https://arxiv.org/pdf/2512.14297.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14297v1" onclick="toggleFavorite(this, '2512.14297v1', 'A Threshold-Triggered Deep Q-Network-Based Framework for Self-Healing in Autonomic Software-Defined IIoT-Edge Networks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Agrippina Mwangi, León Navarro-Hilfiker, Lukasz Brewka, Mikkel Gryning, Elena Fumagalli, Madeleine Gibescu

**分类**: cs.NI, cs.AI, cs.ET, cs.PF, hep-ex

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于阈值触发深度Q网络的自愈框架，用于软件定义IIoT边缘网络**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `软件定义网络` `工业物联网` `自愈网络` `Q学习` `网络优化` `阈值触发` `边缘计算`

## 📋 核心要点

1. 工业网络易受流量突发和硬件波动影响，导致服务降级，现有方法难以实时应对。
2. 提出一种基于阈值触发的DQN自愈代理，通过实时调整路由和资源分配来缓解网络中断。
3. 实验表明，该代理在中断恢复性能上优于现有方法，并能主动维持交换机热稳定性。

## 📝 摘要（中文）

本研究提出了一种基于阈值触发的深度Q网络（DQN）自愈代理，用于自主检测、分析和缓解软件定义工业网络中的中断，并实时调整路由行为和资源分配。这些中断通常由良性流量突发和交换机热波动等随机事件引起，违反了IEC 61850派生的服务质量要求和用户定义的服务级别协议。该代理在一个基于云的概念验证测试平台上部署的三集群交换机网络中进行了训练、验证和测试。仿真结果表明，与基线最短路径和负载均衡路由方法相比，该代理将中断恢复性能提高了53.84%，并且在超脊叶数据平面架构中，优于最先进的方法，包括自适应网络模糊推理系统（13.1%）和基于深度Q网络和流量预测的路由优化方法（21.5%）。此外，该代理通过在需要时主动启动外部机架冷却来维持交换机的热稳定性。这些发现突出了深度强化学习在构建部署于任务关键型、时间敏感型应用场景中的软件定义工业网络中的弹性潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决软件定义工业网络中，由于随机扰动（如流量突发和交换机热波动）导致的服务中断问题。现有方法，如静态路由和简单的负载均衡，无法有效应对这些动态变化，导致服务质量下降，甚至影响关键控制信号的传输。现有方法的痛点在于缺乏自适应性和实时性，难以在中断发生时快速做出响应和调整。

**核心思路**：论文的核心思路是利用深度强化学习（DRL）训练一个智能代理，使其能够自主地学习网络行为，并在检测到异常时，通过调整路由和资源分配来缓解中断。通过设定阈值触发机制，代理能够及时响应网络状态的变化，从而实现自愈。这种方法的核心在于利用DRL的自学习能力，使网络能够适应不断变化的环境。

**技术框架**：该框架包含以下主要模块：1) **网络状态监控**：实时监测网络流量、交换机温度等关键指标。2) **阈值触发器**：当网络状态超过预设阈值时，触发DQN代理。3) **DQN代理**：基于当前网络状态，选择合适的动作（如调整路由、分配资源）。4) **动作执行器**：执行DQN代理选择的动作。5) **奖励函数**：根据动作执行后的网络性能（如延迟、丢包率）给予代理奖励或惩罚，用于训练DQN。整个流程形成一个闭环控制系统，不断优化网络性能。

**关键创新**：该论文的关键创新在于将阈值触发机制与DQN相结合。传统的DQN方法通常需要大量的探索和学习时间，而阈值触发机制可以减少不必要的探索，提高学习效率和响应速度。此外，该方法能够同时考虑路由优化和资源分配，从而更全面地提升网络性能。与现有方法相比，该方法能够更快速、更有效地应对网络中断。

**关键设计**：DQN代理的网络结构采用多层感知机（MLP），输入是网络状态（如链路利用率、交换机温度），输出是可采取的动作（如调整路由权重、分配带宽）。奖励函数的设计综合考虑了延迟、丢包率和交换机温度等因素，旨在实现低延迟、高可靠性和热稳定的网络运行。阈值的设定需要根据实际网络环境进行调整，以平衡响应速度和误触发率。

## 📊 实验亮点

仿真结果表明，所提出的自愈代理在中断恢复性能方面优于基线最短路径和负载均衡路由方法53.84%。与最先进的自适应网络模糊推理系统（ANFIS）相比，性能提升了13.1%，与基于深度Q网络和流量预测的路由优化方法相比，性能提升了21.5%。此外，该代理还能够主动维持交换机热稳定性，进一步验证了其在实际应用中的有效性。

## 🎯 应用场景

该研究成果可应用于各种软件定义的工业网络，例如智能工厂、智能电网和智能交通系统。通过实现网络的自愈能力，可以提高系统的可靠性和可用性，减少人工干预，降低运营成本。尤其是在任务关键型和时间敏感型应用场景中，该方法能够有效保障服务的连续性和稳定性，具有重要的实际应用价值和广阔的应用前景。

## 📄 摘要（原文）

> Stochastic disruptions such as flash events arising from benign traffic bursts and switch thermal fluctuations are major contributors to intermittent service degradation in software-defined industrial networks. These events violate IEC~61850-derived quality-of-service requirements and user-defined service-level agreements, hindering the reliable and timely delivery of control, monitoring, and best-effort traffic in IEC~61400-25-compliant wind power plants. Failure to maintain these requirements often results in delayed or lost control signals, reduced operational efficiency, and increased risk of wind turbine generator downtime.
>   To address these challenges, this study proposes a threshold-triggered Deep Q-Network self-healing agent that autonomically detects, analyzes, and mitigates network disruptions while adapting routing behavior and resource allocation in real time. The proposed agent was trained, validated, and tested on an emulated tri-clustered switch network deployed in a cloud-based proof-of-concept testbed.
>   Simulation results show that the proposed agent improves disruption recovery performance by 53.84% compared to a baseline shortest-path and load-balanced routing approach and outperforms state-of-the-art methods, including the Adaptive Network-based Fuzzy Inference System by 13.1% and the Deep Q-Network and traffic prediction-based routing optimization method by 21.5%, in a super-spine leaf data-plane architecture.
>   Additionally, the agent maintains switch thermal stability by proactively initiating external rack cooling when required. These findings highlight the potential of deep reinforcement learning in building resilience in software-defined industrial networks deployed in mission-critical, time-sensitive application scenarios.

