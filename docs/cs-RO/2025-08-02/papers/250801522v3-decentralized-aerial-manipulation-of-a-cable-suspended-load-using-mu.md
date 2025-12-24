---
layout: default
title: Decentralized Aerial Manipulation of a Cable-Suspended Load using Multi-Agent Reinforcement Learning
---

# Decentralized Aerial Manipulation of a Cable-Suspended Load using Multi-Agent Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01522" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01522v3</a>
  <a href="https://arxiv.org/pdf/2508.01522.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01522v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01522v3', 'Decentralized Aerial Manipulation of a Cable-Suspended Load using Multi-Agent Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jack Zeng, Andreu Matoses Gimenez, Eugene Vinitsky, Javier Alonso-Mora, Sihao Sun

**分类**: cs.RO, cs.AI, cs.MA

**发布日期**: 2025-08-02 (更新: 2025-11-05)

**期刊**: Proceedings of the 9th Conference on Robot Learning, PMLR 305:3850-3868, 2025

---

## 💡 一句话要点

**提出去中心化方法以实现多无人机对吊载的6自由度操控**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多智能体强化学习` `去中心化控制` `微型无人机` `吊载操控` `仿真到现实转移` `动态环境` `协作能力`

## 📋 核心要点

1. 现有的集中式控制方法在多无人机协作操控中面临通信需求高和计算成本大的挑战。
2. 本文提出的去中心化MARL方法允许无人机通过载荷姿态观察进行隐式通信，提升了系统的可扩展性和灵活性。
3. 实验结果表明，该方法在负载模型不确定性下的全姿态控制性能与集中式方法相当，并展示了对单个无人机失效的鲁棒性。

## 📝 摘要（中文）

本文提出了一种首个去中心化的方法，利用多智能体强化学习（MARL）实现微型无人机（MAVs）对吊载的6自由度操控。与现有的集中式控制器不同，该方法不需要全局状态、无人机间的通信或邻近无人机的信息。相反，智能体仅通过载荷姿态观察进行隐式通信，从而实现高可扩展性和灵活性，并显著降低推理时的计算成本，支持政策的机载部署。此外，本文设计了一种新的动作空间，采用线性加速度和机体速率的组合，结合稳健的低级控制器，确保在动态三维运动中尽管存在由于缆绳张力引起的显著不确定性，仍能可靠地实现仿真到现实的转移。通过多项真实世界实验验证了该方法的有效性，结果显示其设定点跟踪性能与最先进的集中式方法相当。

## 🔬 方法详解

**问题定义**：本文旨在解决多无人机对吊载进行6自由度操控时，现有集中式控制方法在通信和计算成本上的不足。现有方法需要全局状态和无人机间的实时通信，限制了系统的可扩展性。

**核心思路**：论文提出了一种去中心化的多智能体强化学习方法，允许无人机通过载荷姿态观察进行隐式通信，从而消除对全局状态和邻近无人机信息的依赖。这种设计提高了系统的灵活性和可扩展性。

**技术框架**：整体框架包括多个MAVs，每个MAV通过MARL训练外部控制策略。系统分为高层策略和低层控制器，前者负责决策，后者确保动作的执行。

**关键创新**：最重要的创新在于去中心化的控制策略设计，使得每个无人机能够独立操作而无需全局信息。这与传统集中式方法的本质区别在于，后者依赖于全局状态和实时通信。

**关键设计**：本文设计了新的动作空间，采用线性加速度和机体速率的组合，结合稳健的低级控制器，以应对动态环境中的不确定性。此外，损失函数和训练策略也经过精心设计，以确保在仿真到现实的转移中保持高效性和可靠性。

## 📊 实验亮点

实验结果显示，所提方法在负载模型不确定性下的设定点跟踪性能与最先进的集中式方法相当，且在单个无人机失效情况下仍能保持良好的协作能力。这表明该方法在实际应用中的鲁棒性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括灾后救援、建筑施工和物流运输等场景，能够有效提升多无人机系统在复杂环境中的协作能力。未来，这种去中心化的控制方法可能会在更广泛的无人机应用中得到推广，推动智能体协作技术的发展。

## 📄 摘要（原文）

> This paper presents the first decentralized method to enable real-world 6-DoF manipulation of a cable-suspended load using a team of Micro-Aerial Vehicles (MAVs). Our method leverages multi-agent reinforcement learning (MARL) to train an outer-loop control policy for each MAV. Unlike state-of-the-art controllers that utilize a centralized scheme, our policy does not require global states, inter-MAV communications, nor neighboring MAV information. Instead, agents communicate implicitly through load pose observations alone, which enables high scalability and flexibility. It also significantly reduces computing costs during inference time, enabling onboard deployment of the policy. In addition, we introduce a new action space design for the MAVs using linear acceleration and body rates. This choice, combined with a robust low-level controller, enables reliable sim-to-real transfer despite significant uncertainties caused by cable tension during dynamic 3D motion. We validate our method in various real-world experiments, including full-pose control under load model uncertainties, showing setpoint tracking performance comparable to the state-of-the-art centralized method. We also demonstrate cooperation amongst agents with heterogeneous control policies, and robustness to the complete in-flight loss of one MAV. Videos of experiments: https://autonomousrobots.nl/paper_websites/aerial-manipulation-marl

