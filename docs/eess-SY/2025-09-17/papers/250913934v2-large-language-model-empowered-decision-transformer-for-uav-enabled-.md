---
layout: default
title: Large Language Model-Empowered Decision Transformer for UAV-Enabled Data Collection
---

# Large Language Model-Empowered Decision Transformer for UAV-Enabled Data Collection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13934" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13934v2</a>
  <a href="https://arxiv.org/pdf/2509.13934.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13934v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13934v2', 'Large Language Model-Empowered Decision Transformer for UAV-Enabled Data Collection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhixion Chen, Jiangzhou Wang, Hyundong Shin, Arumugam Nallanathan

**分类**: eess.SY, cs.LG

**发布日期**: 2025-09-17 (更新: 2025-09-19)

**备注**: 14pages, 8 figures

---

## 💡 一句话要点

**提出LLM-CRDT框架，解决无人机数据收集中的能效优化问题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无人机` `数据收集` `轨迹规划` `强化学习` `决策Transformer` `大型语言模型` `能源效率` `物联网`

## 📋 核心要点

1. 无人机数据收集面临续航和通信范围限制，传统强化学习方法交互成本高，离线强化学习依赖高质量数据。
2. 提出LLM-CRDT框架，利用预训练LLM增强决策Transformer，并引入评论家网络进行正则化，提升策略学习效果。
3. 实验结果表明，LLM-CRDT在能源效率方面优于现有在线和离线强化学习方法，最高提升达36.7%。

## 📝 摘要（中文）

本文研究了利用无人机（UAV）从空间分布的设备进行可靠且节能的数据收集问题，旨在支持各种物联网（IoT）应用。针对无人机续航和通信范围的限制，需要智能轨迹规划。虽然强化学习（RL）已被广泛用于无人机轨迹优化，但其交互性导致现实环境中的高成本和风险。离线RL缓解了这些问题，但仍易受不稳定训练的影响，并且严重依赖专家质量的数据集。为了解决这些挑战，本文构建了一个联合无人机轨迹规划和资源分配问题，以最大化数据收集的能源效率。资源分配子问题首先被转换为等效的线性规划公式，并在多项式时间内得到最优解。然后，本文提出了一种大型语言模型（LLM）赋能的评论家正则化决策Transformer（DT）框架，称为LLM-CRDT，以学习有效的无人机控制策略。在LLM-CRDT中，本文结合了评论家网络来正则化DT模型训练，从而将DT的序列建模能力与基于评论家的价值指导相结合，从而能够从次优数据集中学习有效的策略。此外，为了缓解Transformer模型的数据饥渴问题，本文采用预训练的LLM作为DT模型的Transformer骨干，并采用参数高效的微调策略，即LoRA，从而能够以小规模数据集和低计算开销快速适应无人机控制任务。大量的仿真结果表明，LLM-CRDT优于基准在线和离线RL方法，与当前最先进的DT方法相比，能源效率提高了36.7%。

## 🔬 方法详解

**问题定义**：本文旨在解决无人机在物联网数据收集中，如何进行高效的轨迹规划和资源分配，以最大化能量效率的问题。现有方法，如在线强化学习，需要大量的环境交互，成本高昂且风险大。离线强化学习虽然避免了在线交互，但训练不稳定，且依赖于高质量的专家数据集，难以适应实际应用场景。

**核心思路**：本文的核心思路是利用大型语言模型（LLM）的强大表征能力，结合决策Transformer（DT）的序列建模优势，并引入评论家网络进行正则化，从而在次优数据集上学习到有效的无人机控制策略。通过预训练LLM和参数高效微调，降低了对大规模数据集的依赖，提高了模型的泛化能力和训练效率。

**技术框架**：LLM-CRDT框架包含以下几个主要模块：1) 资源分配优化模块：将资源分配问题转化为线性规划问题，利用优化算法求解。2) 基于预训练LLM的决策Transformer：使用预训练的LLM作为Transformer的骨干网络，利用其强大的语言理解和生成能力，学习无人机控制策略。3) 评论家网络：评估当前策略的价值，并利用评估结果正则化DT模型的训练，提高策略的稳定性和性能。4) 参数高效微调（LoRA）：仅微调少量参数，降低计算开销，加速模型收敛。

**关键创新**：本文最重要的技术创新点在于将大型语言模型（LLM）引入到无人机轨迹规划的决策Transformer框架中，并结合评论家网络进行正则化。这使得模型能够从次优数据集中学习到有效的策略，同时降低了对大规模数据集的依赖。此外，采用参数高效微调策略，进一步降低了计算开销，提高了模型的训练效率。

**关键设计**：在LLM-CRDT中，预训练LLM作为Transformer的骨干网络，负责提取状态和动作序列的特征。评论家网络采用深度神经网络结构，输入状态和动作，输出价值评估。损失函数包括策略损失和评论家损失，策略损失用于优化DT模型的策略，评论家损失用于训练评论家网络。LoRA通过引入低秩矩阵来微调LLM的参数，仅需更新少量参数即可实现模型的快速适应。

## 📊 实验亮点

实验结果表明，LLM-CRDT在无人机数据收集任务中表现出色，与当前最先进的DT方法相比，能源效率提高了36.7%。此外，LLM-CRDT还优于基准在线和离线强化学习方法，证明了其在次优数据集上学习有效策略的能力。参数高效微调策略LoRA的使用，显著降低了计算开销，使得模型能够快速适应新的任务。

## 🎯 应用场景

该研究成果可应用于各种需要无人机进行数据收集的场景，例如：环境监测、农业巡检、灾害救援、智慧城市等。通过优化无人机的轨迹规划和资源分配，可以显著提高数据收集的效率和能量利用率，降低运营成本，并为物联网应用提供更可靠的数据支持。未来，该方法有望扩展到多无人机协同数据收集等更复杂的场景。

## 📄 摘要（原文）

> The deployment of unmanned aerial vehicles (UAVs) for reliable and energy-efficient data collection from spatially distributed devices holds great promise in supporting diverse Internet of Things (IoT) applications. Nevertheless, the limited endurance and communication range of UAVs necessitate intelligent trajectory planning. While reinforcement learning (RL) has been extensively explored for UAV trajectory optimization, its interactive nature entails high costs and risks in real-world environments. Offline RL mitigates these issues but remains susceptible to unstable training and heavily rely on expert-quality datasets. To address these challenges, we formulate a joint UAV trajectory planning and resource allocation problem to maximize energy efficiency of data collection. The resource allocation subproblem is first transformed into an equivalent linear programming formulation and solved optimally with polynomial-time complexity. Then, we propose a large language model (LLM)-empowered critic-regularized decision transformer (DT) framework, termed LLM-CRDT, to learn effective UAV control policies. In LLM-CRDT, we incorporate critic networks to regularize the DT model training, thereby integrating the sequence modeling capabilities of DT with critic-based value guidance to enable learning effective policies from suboptimal datasets. Furthermore, to mitigate the data-hungry nature of transformer models, we employ a pre-trained LLM as the transformer backbone of the DT model and adopt a parameter-efficient fine-tuning strategy, i.e., LoRA, enabling rapid adaptation to UAV control tasks with small-scale dataset and low computational overhead. Extensive simulations demonstrate that LLM-CRDT outperforms benchmark online and offline RL methods, achieving up to 36.7\% higher energy efficiency than the current state-of-the-art DT approaches.

