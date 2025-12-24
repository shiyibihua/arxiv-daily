---
layout: default
title: Decentralized Rank Scheduling for Energy-Constrained Multi-Task Federated Fine-Tuning in Edge-Assisted IoV Networks
---

# Decentralized Rank Scheduling for Energy-Constrained Multi-Task Federated Fine-Tuning in Edge-Assisted IoV Networks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09532" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09532v1</a>
  <a href="https://arxiv.org/pdf/2508.09532.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09532v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09532v1', 'Decentralized Rank Scheduling for Energy-Constrained Multi-Task Federated Fine-Tuning in Edge-Assisted IoV Networks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bokeng Zheng, Jianqiang Zhong, Jiayi Liu, Xiaoxi Zhang

**分类**: cs.LG, cs.AI, cs.NI

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出去中心化排名调度解决边缘IoV网络中的多任务联邦微调问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `联邦学习` `车联网` `多任务学习` `低秩适应` `能量感知` `去中心化` `动态环境` `智能交通`

## 📋 核心要点

1. 现有的联邦学习方法在动态和资源受限的车联网环境中面临挑战，尤其是在客户端移动性和连接不稳定的情况下。
2. 本文提出了一种分层的联邦微调框架，结合低秩适应技术，设计了一种去中心化的能量感知排名适应机制，以应对多任务学习的需求。
3. 实验结果表明，所提方法在准确性和效率上优于所有基线，延迟减少超过24%，平均准确性提高超过2.5%。

## 📝 摘要（中文）

联邦微调已成为在边缘环境中适应基础模型（FMs）到多样化下游任务的有前景的方法。在车联网（IoV）系统中，由于客户端的移动性、异构资源和间歇性连接，使得高效低延迟的多任务适应尤为具有挑战性。本文提出了一种分层的联邦微调框架，协调路边单元（RSUs）和车辆，以支持动态IoV场景下的资源感知和抗移动性学习。通过低秩适应（LoRA），我们引入了一种去中心化的、能量感知的排名适应机制，并将其形式化为受限的多臂赌博机问题。开发了一种新颖的UCB-DUAL算法，以在每个任务的能量预算下实现自适应探索，达到可证明的次线性遗憾。通过构建基于真实轨迹的大规模IoV模拟器，评估了我们的方法，实验结果显示该方法在所有基线中实现了最佳的准确性与效率平衡，延迟减少超过24%，平均准确性提高超过2.5%。

## 🔬 方法详解

**问题定义**：本文旨在解决在车联网（IoV）环境中进行多任务联邦微调时面临的资源限制和客户端移动性问题。现有方法往往无法有效应对动态变化的网络条件和异构资源的挑战。

**核心思路**：提出了一种分层的联邦微调框架，结合低秩适应（LoRA）技术，通过去中心化的排名适应机制，优化能量使用并提高学习的鲁棒性。

**技术框架**：整体架构包括路边单元（RSUs）和车辆的协调机制，采用多臂赌博机模型来动态调整任务的能量分配，确保在不同任务间的资源合理分配。

**关键创新**：引入了UCB-DUAL算法，支持在每个任务的能量预算下进行自适应探索，显著降低了学习过程中的延迟和能量消耗。与传统方法相比，具有更好的适应性和效率。

**关键设计**：在算法设计中，设置了每个任务的能量预算，并通过优化损失函数和网络结构，确保在动态环境中保持高效的学习性能。

## 📊 实验亮点

实验结果显示，所提方法在所有对比基线中表现最佳，延迟减少超过24%，平均准确性提高超过2.5%。这些结果表明，去中心化的能量感知排名适应机制在动态IoV环境中具有显著的优势，能够有效提升多任务联邦微调的性能。

## 🎯 应用场景

该研究的潜在应用领域包括智能交通系统、自动驾驶汽车和车联网服务等。通过提高多任务学习的效率和准确性，可以显著提升车辆间的协作和信息共享能力，推动智能交通的发展。未来，该方法有望在更广泛的边缘计算场景中得到应用，促进智能设备的智能化和自主决策能力。

## 📄 摘要（原文）

> Federated fine-tuning has emerged as a promising approach for adapting foundation models (FMs) to diverse downstream tasks in edge environments. In Internet of Vehicles (IoV) systems, enabling efficient and low-latency multi-task adaptation is particularly challenging due to client mobility, heterogeneous resources, and intermittent connectivity. This paper proposes a hierarchical federated fine-tuning framework that coordinates roadside units (RSUs) and vehicles to support resource-aware and mobility-resilient learning across dynamic IoV scenarios. Leveraging Low-Rank Adaptation (LoRA), we introduce a decentralized, energy-aware rank adaptation mechanism formulated as a constrained multi-armed bandit problem. A novel UCB-DUAL algorithm is developed to enable adaptive exploration under per-task energy budgets, achieving provable sublinear regret. To evaluate our method, we construct a large-scale IoV simulator based on real-world trajectories, capturing dynamic participation, RSU handoffs, and communication variability. Extensive experiments show that our approach achieves the best accuracy-efficiency trade-off among all baselines, reducing latency by over 24\% and improving average accuracy by more than 2.5\%.

