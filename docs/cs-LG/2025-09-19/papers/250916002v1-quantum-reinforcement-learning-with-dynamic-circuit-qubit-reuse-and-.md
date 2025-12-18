---
layout: default
title: Quantum Reinforcement Learning with Dynamic-Circuit Qubit Reuse and Grover-Based Trajectory Optimization
---

# Quantum Reinforcement Learning with Dynamic-Circuit Qubit Reuse and Grover-Based Trajectory Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16002" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16002v1</a>
  <a href="https://arxiv.org/pdf/2509.16002.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16002v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16002v1', 'Quantum Reinforcement Learning with Dynamic-Circuit Qubit Reuse and Grover-Based Trajectory Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Thet Htar Su, Shaswot Shresthamali, Masaaki Kondo

**分类**: quant-ph, cs.LG

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**提出基于动态量子电路和Grover算法的量子强化学习框架，提升可扩展性。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `量子强化学习` `动态量子电路` `量子比特重用` `Grover算法` `量子马尔可夫决策过程`

## 📋 核心要点

1. 传统强化学习在处理大规模状态空间时面临维度灾难，量子强化学习旨在利用量子计算的优势解决此问题。
2. 该论文提出一种完全量子化的强化学习框架，利用量子叠加并行探索策略，并采用动态量子电路减少量子比特需求。
3. 实验结果表明，该框架在降低量子比特需求的同时保持了轨迹保真度，并在真实量子硬件上验证了其可行性。

## 📝 摘要（中文）

本文提出了一个完整的量子强化学习框架，该框架集成了量子马尔可夫决策过程、基于动态电路的量子比特重用以及用于轨迹优化的Grover算法。该框架将状态、动作、奖励和转移完全编码在量子域中，通过叠加实现状态-动作序列的并行探索，并消除了经典子程序。动态电路操作（包括中间电路测量和重置）允许在多次智能体-环境交互中重复使用相同的物理量子比特，从而将量子比特需求从7*T减少到7（对于T个时间步），同时保持逻辑连续性。量子算术计算轨迹回报，并应用Grover搜索来叠加这些评估的轨迹，以放大测量具有最高回报的轨迹的概率，从而加速识别最优策略。仿真表明，基于动态电路的实现保持了轨迹保真度，同时相对于静态设计减少了66%的量子比特使用量。在IBM Heron类量子硬件上的实验部署证实，该框架在当前量子处理器的约束范围内运行，并验证了在噪声中等规模量子条件下完全量子多步强化学习的可行性。该框架提高了量子强化学习在大型顺序决策任务中的可扩展性和实际应用。

## 🔬 方法详解

**问题定义**：传统量子强化学习方法在处理多步决策问题时，需要大量的量子比特资源，限制了其在实际量子硬件上的应用。此外，许多方法依赖于经典子程序，无法充分发挥量子计算的优势。本文旨在解决量子强化学习中的量子比特资源瓶颈问题，并构建一个完全量子化的强化学习框架。

**核心思路**：本文的核心思路是利用动态量子电路技术，通过量子比特的重用，显著减少量子比特的需求量。同时，采用Grover搜索算法加速最优策略的搜索过程，并构建完全量子化的强化学习流程，避免经典计算的参与，充分利用量子计算的并行性。

**技术框架**：该框架包含以下几个主要模块：1) 量子马尔可夫决策过程（QMDP）的构建，将状态、动作、奖励和转移概率编码为量子态。2) 基于动态量子电路的量子比特重用机制，通过中间测量和重置操作，在不同的时间步重复使用相同的物理量子比特。3) 量子算术单元，用于计算轨迹的回报值。4) Grover搜索算法，用于在叠加的轨迹中搜索具有最高回报的轨迹，从而找到最优策略。

**关键创新**：该论文的关键创新在于动态量子电路的量子比特重用机制。传统的量子算法通常需要为每个时间步分配独立的量子比特，导致量子比特需求随时间步线性增长。而本文提出的方法通过动态电路操作，在不同的时间步重复使用相同的量子比特，从而将量子比特需求降低到常数级别。此外，完全量子化的框架避免了经典子程序的参与，能够更好地利用量子计算的优势。

**关键设计**：动态量子电路的设计是关键。通过在量子电路中插入中间测量和重置操作，可以在不同的时间步重复使用相同的量子比特。Grover搜索算法的迭代次数需要根据问题的规模进行调整，以保证搜索的效率和精度。此外，量子算术单元的设计也需要考虑量子比特的限制和噪声的影响。

## 📊 实验亮点

实验结果表明，基于动态电路的实现相对于静态设计，量子比特使用量减少了66%。在IBM Heron类量子硬件上的实验验证了该框架的可行性，并表明该框架能够在当前量子处理器的约束范围内运行。这些结果验证了完全量子多步强化学习在噪声中等规模量子条件下的可行性。

## 🎯 应用场景

该研究成果可应用于资源受限环境下的复杂决策问题，例如机器人路径规划、金融交易策略优化、以及药物发现等领域。通过降低量子比特需求，该框架有望在近期的量子计算机上实现，加速量子强化学习的实际应用进程，并推动人工智能领域的发展。

## 📄 摘要（原文）

> A fully quantum reinforcement learning framework is developed that integrates a quantum Markov decision process, dynamic circuit-based qubit reuse, and Grover's algorithm for trajectory optimization. The framework encodes states, actions, rewards, and transitions entirely within the quantum domain, enabling parallel exploration of state-action sequences through superposition and eliminating classical subroutines. Dynamic circuit operations, including mid-circuit measurement and reset, allow reuse of the same physical qubits across multiple agent-environment interactions, reducing qubit requirements from 7*T to 7 for T time steps while preserving logical continuity. Quantum arithmetic computes trajectory returns, and Grover's search is applied to the superposition of these evaluated trajectories to amplify the probability of measuring those with the highest return, thereby accelerating the identification of the optimal policy. Simulations demonstrate that the dynamic-circuit-based implementation preserves trajectory fidelity while reducing qubit usage by 66 percent relative to the static design. Experimental deployment on IBM Heron-class quantum hardware confirms that the framework operates within the constraints of current quantum processors and validates the feasibility of fully quantum multi-step reinforcement learning under noisy intermediate-scale quantum conditions. This framework advances the scalability and practical application of quantum reinforcement learning for large-scale sequential decision-making tasks.

