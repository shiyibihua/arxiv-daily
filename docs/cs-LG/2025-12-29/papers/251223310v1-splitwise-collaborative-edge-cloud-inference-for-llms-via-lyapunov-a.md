---
layout: default
title: "Splitwise: Collaborative Edge-Cloud Inference for LLMs via Lyapunov-Assisted DRL"
---

# Splitwise: Collaborative Edge-Cloud Inference for LLMs via Lyapunov-Assisted DRL

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23310" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23310v1</a>
  <a href="https://arxiv.org/pdf/2512.23310.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23310v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23310v1', 'Splitwise: Collaborative Edge-Cloud Inference for LLMs via Lyapunov-Assisted DRL')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abolfazl Younesi, Abbas Shabrang Maryan, Elyas Oustad, Zahra Najafabadi Samani, Mohsen Ansari, Thomas Fahringer

**分类**: cs.LG, cs.AI, cs.DC, cs.ET, cs.NI

**发布日期**: 2025-12-29

**备注**: 11 pages, 9 figures. Accepted by ACM for presentation at UCC '25 (18th International Conference on Utility and Cloud Computing), December 1-4, 2025, France. Proceedings publication pending

**DOI**: [10.1145/3773274.3774267](https://doi.org/10.1145/3773274.3774267)

---

## 💡 一句话要点

**Splitwise：基于Lyapunov优化的DRL实现LLM在边缘-云协同推理的自适应切分。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `边缘计算` `大语言模型` `深度强化学习` `模型切分` `Lyapunov优化`

## 📋 核心要点

1. 现有边缘-云 LLM 推理方案难以在延迟、能耗和精度之间取得良好平衡，且无法适应动态网络环境。
2. Splitwise 提出一种基于 Lyapunov 优化的分层 DRL 框架，实现 LLM 在边缘和云之间的细粒度自适应切分。
3. 实验表明，Splitwise 显著降低了端到端延迟和能耗，同时保持了精度和鲁棒性，优于现有方案。

## 📝 摘要（中文）

由于边缘设备内存和算力资源有限，在大语言模型（LLM）上部署具有挑战性。仅在云端推理虽然减轻了设备负担，但引入了高延迟和高成本。静态的边缘-云划分方案仅优化单一指标，难以应对带宽波动。我们提出了Splitwise，一种新颖的基于Lyapunov优化的深度强化学习（DRL）框架，用于LLM在边缘和云环境之间进行细粒度的自适应划分。Splitwise将Transformer层分解为注意力头和前馈子块，比逐层划分方案暴露了更多的划分选择。一个由Lyapunov优化指导的分层DRL策略，在随机工作负载和可变网络带宽下，联合最小化延迟、能耗和精度下降，同时保证队列稳定性。Splitwise还通过具有指数退避恢复的划分检查点来保证通信失败时的鲁棒性。在Jetson Orin NX、Galaxy S23和Raspberry Pi 5上使用GPT-2 (1.5B)、LLaMA-7B和LLaMA-13B进行的实验表明，与现有的划分器相比，Splitwise将端到端延迟降低了1.4x-2.8x，并将能耗降低了高达41%。相对于仅在云端执行，它将第95百分位的延迟降低了53-61%，同时保持了精度和适度的内存需求。

## 🔬 方法详解

**问题定义**：论文旨在解决在边缘设备上部署大型语言模型（LLM）时，由于资源限制和网络波动导致的推理延迟高、能耗大以及精度下降的问题。现有的静态边缘-云划分方法无法很好地适应动态变化的网络环境，并且通常只优化单一指标，难以实现多目标优化。

**核心思路**：论文的核心思路是利用深度强化学习（DRL）来学习一个自适应的LLM划分策略，该策略能够根据当前的网络状态、设备资源和任务需求，动态地将LLM的不同部分分配到边缘设备和云端进行推理。通过Lyapunov优化来保证系统的稳定性，并使用细粒度的划分方式来增加划分的灵活性。

**技术框架**：Splitwise 的整体框架包含以下几个主要模块：1) LLM 分解模块：将 Transformer 层分解为更小的单元（注意力头和前馈子块），从而提供更细粒度的划分选择。2) 状态观测模块：收集边缘设备和云端的资源信息、网络带宽以及任务队列长度等状态信息。3) DRL 策略学习模块：使用分层 DRL 策略，结合 Lyapunov 优化，学习最优的划分策略。4) 推理执行模块：根据 DRL 策略将 LLM 的不同部分分配到边缘设备和云端进行推理，并进行结果整合。5) 故障恢复模块：在通信失败时，通过划分检查点和指数退避恢复机制保证系统的鲁棒性。

**关键创新**：论文的关键创新在于：1) 提出了细粒度的 LLM 划分方法，将 Transformer 层分解为更小的单元，增加了划分的灵活性。2) 结合 Lyapunov 优化和 DRL，实现多目标优化，同时保证系统的稳定性。3) 提出了分层 DRL 策略，降低了学习的复杂性。4) 实现了通信失败时的鲁棒性保证。

**关键设计**：论文的关键设计包括：1) Lyapunov 函数的设计，用于保证任务队列的稳定性。2) DRL 策略网络的结构，包括状态表示、动作空间和奖励函数的设计。3) 划分检查点和指数退避恢复机制的具体实现。4) 针对不同 LLM 和边缘设备的参数调优。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23310v1/source/Figures/OperationalCostAnalysis.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23310v1/source/Figures/MemoryRequirements.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23310v1/source/Figures/PerformanceScalingSpeedupvscloudonly.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Splitwise 在 GPT-2 (1.5B)、LLaMA-7B 和 LLaMA-13B 模型上，相比现有划分器，端到端延迟降低了 1.4x-2.8x，能耗降低了高达 41%。相对于仅在云端执行，第 95 百分位的延迟降低了 53-61%，同时保持了精度和适度的内存需求。这些结果验证了 Splitwise 在边缘-云协同推理中的有效性。

## 🎯 应用场景

Splitwise 的应用场景广泛，包括智能家居、自动驾驶、工业物联网等需要在边缘设备上进行低延迟、高能效 LLM 推理的领域。该研究成果有助于推动 LLM 在资源受限环境中的部署，并为未来的边缘智能应用提供技术支撑。

## 📄 摘要（原文）

> Deploying large language models (LLMs) on edge devices is challenging due to their limited memory and power resources. Cloud-only inference reduces device burden but introduces high latency and cost. Static edge-cloud partitions optimize a single metric and struggle when bandwidth fluctuates. We propose Splitwise, a novel Lyapunov-assisted deep reinforcement learning (DRL) framework for fine-grained, adaptive partitioning of LLMs across edge and cloud environments. Splitwise decomposes transformer layers into attention heads and feed-forward sub-blocks, exposing more partition choices than layer-wise schemes. A hierarchical DRL policy, guided by Lyapunov optimization, jointly minimizes latency, energy consumption, and accuracy degradation while guaranteeing queue stability under stochastic workloads and variable network bandwidth. Splitwise also guarantees robustness via partition checkpoints with exponential backoff recovery in case of communication failures. Experiments on Jetson Orin NX, Galaxy S23, and Raspberry Pi 5 with GPT-2 (1.5B), LLaMA-7B, and LLaMA-13B show that Splitwise reduces end-to-end latency by 1.4x-2.8x and cuts energy consumption by up to 41% compared with existing partitioners. It lowers the 95th-percentile latency by 53-61% relative to cloud-only execution, while maintaining accuracy and modest memory requirements.

