---
layout: default
title: Resource-Aware Neural Network Pruning Using Graph-based Reinforcement Learning
---

# Resource-Aware Neural Network Pruning Using Graph-based Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10526" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10526v1</a>
  <a href="https://arxiv.org/pdf/2509.10526.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10526v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10526v1', 'Resource-Aware Neural Network Pruning Using Graph-based Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dieter Balemans, Thomas Huybrechts, Jan Steckel, Siegfried Mercelis

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-04

---

## 💡 一句话要点

**提出基于图强化学习的资源感知型神经网络剪枝方法，提升剪枝效率。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `神经网络剪枝` `图神经网络` `强化学习` `AutoML` `模型压缩`

## 📋 核心要点

1. 现有剪枝方法依赖手工启发式和局部优化，导致性能次优和效率低下。
2. 提出基于图的强化学习剪枝框架，利用图注意力网络编码网络拓扑结构，学习最优通道重要性。
3. 实验表明，该方法在 CIFAR 和 ImageNet 等数据集上优于传统剪枝技术，达到SOTA。

## 📝 摘要（中文）

本文提出了一种新颖的神经网络剪枝方法，该方法将基于图的观察空间集成到 AutoML 框架中，以解决现有方法的局限性。传统的剪枝方法通常依赖于手工设计的启发式方法和局部优化视角，这可能导致次优的性能和低效的剪枝策略。我们的框架通过引入目标神经网络的图表示来转换剪枝过程，该图表示捕获层和通道之间的完整拓扑关系，用网络结构的全局视图取代了有限的逐层观察空间。核心创新包括一个图注意力网络 (GAT) 编码器，它处理网络的图表示并生成丰富的嵌入。此外，对于动作空间，我们从连续的剪枝率过渡到细粒度的二元动作空间，这使智能体能够直接从数据中学习最佳通道重要性标准，从而摆脱了预定义的评分函数。这些贡献在约束马尔可夫决策过程 (CMDP) 框架中建模，允许智能体在满足资源约束（如目标压缩率）的同时做出明智的剪枝决策。为此，我们设计了一个自我竞争奖励系统，鼓励智能体在满足定义的约束的同时超越其先前的最佳性能。我们通过在包括 CIFAR-10、CIFAR-100 和 ImageNet 在内的基准数据集上进行的大量实验证明了我们方法的有效性。实验表明，我们的方法始终优于传统的剪枝技术，显示出最先进的结果，同时学习特定于任务的剪枝策略，这些策略可以识别功能上冗余的连接，而不仅仅是简单的权重幅度考虑。

## 🔬 方法详解

**问题定义**：现有的神经网络剪枝方法通常依赖于手工设计的启发式规则和局部优化策略，缺乏对网络全局结构的感知，导致剪枝效果不佳，难以达到最优的压缩率和性能平衡。此外，预定义的评分函数无法充分利用数据信息，难以识别真正冗余的连接。

**核心思路**：本文的核心思路是将神经网络的剪枝过程建模为一个强化学习问题，并引入图结构来表示网络的拓扑关系。通过图注意力网络（GAT）学习网络中每个连接的重要性，并使用强化学习智能体根据资源约束（如压缩率）做出剪枝决策。这种方法能够全局地优化剪枝策略，并从数据中学习任务相关的剪枝模式。

**技术框架**：该框架基于约束马尔可夫决策过程（CMDP），主要包含以下几个模块：1) 图表示模块：将神经网络表示为一个图，节点代表层或通道，边代表连接关系。2) 图注意力网络（GAT）编码器：处理图表示，为每个节点生成嵌入向量，捕捉节点的重要性信息。3) 强化学习智能体：根据GAT的输出，做出二元剪枝决策（保留或剪除通道）。4) 奖励函数：设计一个自我竞争奖励系统，鼓励智能体在满足资源约束的同时，超越其先前的最佳性能。

**关键创新**：该方法最重要的创新点在于：1) 使用图结构表示神经网络，能够捕捉全局拓扑关系。2) 使用图注意力网络学习连接的重要性，避免了手工设计启发式规则。3) 将剪枝过程建模为约束马尔可夫决策过程，能够显式地考虑资源约束。4) 采用细粒度的二元动作空间，允许智能体直接学习通道重要性。

**关键设计**：GAT编码器使用多头注意力机制，学习节点之间的关系。奖励函数包含两部分：性能奖励和约束惩罚。性能奖励鼓励智能体提高剪枝后网络的性能，约束惩罚则惩罚违反资源约束的行为。智能体使用PPO算法进行训练。

## 📊 实验亮点

在 CIFAR-10、CIFAR-100 和 ImageNet 等基准数据集上的实验表明，该方法优于传统的剪枝技术，取得了最先进的结果。具体而言，该方法能够在保持甚至提高模型精度的同时，显著降低模型的参数量和计算量，证明了其在资源受限环境下的有效性。

## 🎯 应用场景

该研究成果可应用于各种需要模型压缩和加速的场景，例如移动设备上的图像识别、自动驾驶系统中的目标检测、以及资源受限的边缘计算环境。通过自动学习任务相关的剪枝策略，可以显著降低模型大小和计算复杂度，提高部署效率和用户体验。

## 📄 摘要（原文）

> This paper presents a novel approach to neural network pruning by integrating a graph-based observation space into an AutoML framework to address the limitations of existing methods. Traditional pruning approaches often depend on hand-crafted heuristics and local optimization perspectives, which can lead to suboptimal performance and inefficient pruning strategies. Our framework transforms the pruning process by introducing a graph representation of the target neural network that captures complete topological relationships between layers and channels, replacing the limited layer-wise observation space with a global view of network structure. The core innovations include a Graph Attention Network (GAT) encoder that processes the network's graph representation and generates a rich embedding. Additionally, for the action space we transition from continuous pruning ratios to fine-grained binary action spaces which enables the agent to learn optimal channel importance criteria directly from data, moving away from predefined scoring functions. These contributions are modelled within a Constrained Markov Decision Process (CMDP) framework, allowing the agent to make informed pruning decisions while adhering to resource constraints such as target compression rates. For this, we design a self-competition reward system that encourages the agent to outperform its previous best performance while satisfying the defined constraints. We demonstrate the effectiveness of our approach through extensive experiments on benchmark datasets including CIFAR-10, CIFAR-100, and ImageNet. The experiments show that our method consistently outperforms traditional pruning techniques, showing state-of-the-art results while learning task-specific pruning strategies that identify functionally redundant connections beyond simple weight magnitude considerations.

