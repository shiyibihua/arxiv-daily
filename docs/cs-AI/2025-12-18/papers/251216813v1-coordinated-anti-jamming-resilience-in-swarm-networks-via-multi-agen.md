---
layout: default
title: Coordinated Anti-Jamming Resilience in Swarm Networks via Multi-Agent Reinforcement Learning
---

# Coordinated Anti-Jamming Resilience in Swarm Networks via Multi-Agent Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16813" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16813v1</a>
  <a href="https://arxiv.org/pdf/2512.16813.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16813v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16813v1', 'Coordinated Anti-Jamming Resilience in Swarm Networks via Multi-Agent Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bahman Abolhassani, Tugba Erpek, Kemal Davaslioglu, Yalin E. Sagduyu, Sastry Kompella

**分类**: cs.NI, cs.AI, cs.DC, cs.LG, eess.SP

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出基于QMIX的多智能体强化学习方法，提升集群网络在反应式干扰下的通信韧性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多智能体强化学习` `集群网络` `反应式干扰` `QMIX算法` `通信安全`

## 📋 核心要点

1. 反应式干扰严重威胁机器人集群网络，传统固定策略难以有效应对自适应干扰。
2. 提出基于QMIX的多智能体强化学习框架，协调信道和功率选择，提升通信韧性。
3. 实验表明，QMIX能快速收敛到协作策略，显著提高吞吐量并降低干扰发生率。

## 📝 摘要（中文）

本文提出了一种基于QMIX算法的多智能体强化学习(MARL)框架，旨在提高集群通信在反应式干扰下的韧性。反应式干扰机会选择性地干扰智能体间的通信，从而破坏集群的完整性和任务成功率，对机器人集群网络构成严重的安全威胁。传统的对策，如固定功率控制或静态信道跳频，对这种自适应的攻击者基本无效。本文考虑了一个多发射机-接收机对共享信道的网络，同时一个具有马尔可夫阈值动态的反应式干扰机感知总功率并做出相应反应。每个智能体联合选择发射频率（信道）和功率，QMIX学习一个集中式但可分解的动作价值函数，从而实现协调但分散的执行。在无信道复用设置中，我们将QMIX与genie-aided最优策略进行基准测试，在启用信道复用的更一般的衰落环境中，将其与局部上限置信区间(UCB)和无状态反应策略进行基准测试。仿真结果表明，QMIX迅速收敛到接近genie-aided界限的协作策略，同时比基线实现更高的吞吐量和更低的干扰发生率，从而证明了MARL在竞争环境中保护自主集群的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人集群网络在反应式干扰下的通信安全问题。现有的固定功率控制或静态信道跳频等方法无法有效应对自适应的反应式干扰，导致集群通信中断，任务失败。

**核心思路**：论文的核心思路是利用多智能体强化学习（MARL）来训练集群中的每个智能体，使其能够根据环境（包括其他智能体的行为和干扰机的行为）自适应地选择合适的信道和功率，从而最大化集群的整体通信性能。通过学习协作策略，智能体可以共同避免干扰，提高通信的可靠性和效率。

**技术框架**：该框架包含多个发射机-接收机对，它们共享信道进行通信。一个反应式干扰机监听信道上的总功率，并根据马尔可夫阈值动态决定是否进行干扰。每个智能体（发射机）通过MARL算法学习选择合适的信道和功率。QMIX算法被用于学习一个集中式但可分解的动作价值函数，该函数允许智能体在分散的环境中执行协调的动作。

**关键创新**：该论文的关键创新在于使用QMIX算法来解决集群网络中的抗干扰问题。QMIX能够学习一个集中式的价值函数，同时允许智能体分散地执行动作，这使得智能体能够在复杂的环境中进行有效的协作。此外，该论文还考虑了反应式干扰机的自适应行为，并设计了相应的奖励函数来鼓励智能体学习避免干扰的策略。

**关键设计**：QMIX算法中的关键设计包括：1）状态表示：每个智能体观察到的状态包括信道状态、其他智能体的行为以及干扰机的行为。2）动作空间：每个智能体的动作空间包括选择信道和功率级别。3）奖励函数：奖励函数的设计旨在鼓励智能体最大化吞吐量，同时避免干扰。4）网络结构：QMIX使用一个混合网络来将每个智能体的Q值组合成一个联合Q值，该联合Q值用于指导智能体的学习。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16813v1/topology.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16813v1/based10.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16813v1/based8.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，QMIX算法在无信道复用场景下，性能接近genie-aided最优策略。在更一般的信道复用场景下，QMIX算法相比于局部UCB和无状态反应策略，实现了更高的吞吐量和更低的干扰发生率，验证了MARL在保护自主集群通信方面的有效性。

## 🎯 应用场景

该研究成果可应用于各种需要高可靠性通信的集群机器人系统，例如：无人机集群搜索救援、自主水下航行器集群环境监测、以及工业机器人集群协同作业等。通过提高集群通信的抗干扰能力，可以确保任务的顺利完成，并降低因通信中断带来的风险。

## 📄 摘要（原文）

> Reactive jammers pose a severe security threat to robotic-swarm networks by selectively disrupting inter-agent communications and undermining formation integrity and mission success. Conventional countermeasures such as fixed power control or static channel hopping are largely ineffective against such adaptive adversaries. This paper presents a multi-agent reinforcement learning (MARL) framework based on the QMIX algorithm to improve the resilience of swarm communications under reactive jamming. We consider a network of multiple transmitter-receiver pairs sharing channels while a reactive jammer with Markovian threshold dynamics senses aggregate power and reacts accordingly. Each agent jointly selects transmit frequency (channel) and power, and QMIX learns a centralized but factorizable action-value function that enables coordinated yet decentralized execution. We benchmark QMIX against a genie-aided optimal policy in a no-channel-reuse setting, and against local Upper Confidence Bound (UCB) and a stateless reactive policy in a more general fading regime with channel reuse enabled. Simulation results show that QMIX rapidly converges to cooperative policies that nearly match the genie-aided bound, while achieving higher throughput and lower jamming incidence than the baselines, thereby demonstrating MARL's effectiveness for securing autonomous swarms in contested environments.

