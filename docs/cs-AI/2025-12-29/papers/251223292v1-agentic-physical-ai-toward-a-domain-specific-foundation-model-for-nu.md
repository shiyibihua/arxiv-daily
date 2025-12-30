---
layout: default
title: Agentic Physical AI toward a Domain-Specific Foundation Model for Nuclear Reactor Control
---

# Agentic Physical AI toward a Domain-Specific Foundation Model for Nuclear Reactor Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23292" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23292v1</a>
  <a href="https://arxiv.org/pdf/2512.23292.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23292v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23292v1', 'Agentic Physical AI toward a Domain-Specific Foundation Model for Nuclear Reactor Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yoonpyo Lee, Kazuma Kobayashi, Sai Puppala, Sajedul Talukder, Seid Koric, Souvik Chakraborty, Syed Bahauddin Alam

**分类**: cs.AI, cs.LG

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**提出Agentic Physical AI，用于核反应堆控制的领域特定基础模型。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `核反应堆控制` `物理AI` `领域特定模型` `强化学习` `语言模型`

## 📋 核心要点

1. 通用AI模型在物理系统控制中面临输入不忠实问题，无法保证动作执行结果的安全性。
2. 提出Agentic Physical AI，利用紧凑语言模型，通过物理验证驱动策略优化，而非感知推理。
3. 实验表明，大规模训练可显著降低方差，稳定执行行为，并实现跨物理和模态的知识迁移。

## 📝 摘要（中文）

当前物理系统AI的主流范式，即扩展通用基础模型以实现通用多模态推理，在控制界面面临根本性障碍。最新基准测试表明，即使是最先进的视觉-语言模型在基本定量物理任务上的准确率也仅为50-53%，表现得像近似猜测者，保留语义合理性但违反物理约束。这种输入不忠实性不是缩放缺陷，而是结构性限制。以感知为中心的架构优化参数空间模仿，而安全关键控制需要对执行动作的结果空间保证。本文提出了一种根本不同的领域特定基础模型路径，引入了作为Agentic Physical AI运行的紧凑语言模型，其中策略优化由基于物理的验证驱动，而不是感知推理。我们在合成反应堆控制场景中训练了一个3.6亿参数的模型，将数据集从10^3扩展到10^5个示例。这引发了通用模型中不存在的急剧相变。小规模系统表现出具有灾难性尾部风险的高方差模仿，而大规模模型经历了超过500倍的方差崩溃，稳定了执行级别的行为。尽管平衡地暴露于四个驱动系列，但该模型自主拒绝了大约70%的训练分布，并将95%的运行时执行集中在单个库策略上。学习到的表示可以在不同的物理和连续输入模态之间转移，而无需架构修改。

## 🔬 方法详解

**问题定义**：现有通用人工智能模型在物理系统控制任务中表现不佳，尤其是在核反应堆控制等安全关键领域。这些模型往往依赖于感知输入进行模仿学习，但忽略了物理约束，导致控制动作不安全或无效。现有方法的痛点在于无法保证控制动作的物理合理性和安全性。

**核心思路**：本文的核心思路是放弃以感知为中心的模仿学习，转而采用基于物理验证的策略优化。通过构建一个Agentic Physical AI，利用紧凑的语言模型作为策略生成器，并使用物理模型对生成的策略进行验证和优化，从而确保控制动作的物理可行性和安全性。

**技术框架**：整体框架包含以下几个主要模块：1) **环境模拟器**：用于生成核反应堆控制的合成数据，包括各种控制场景和物理状态。2) **语言模型**：作为策略生成器，接收环境状态信息，输出控制动作序列。3) **物理验证器**：基于核反应堆的物理模型，对语言模型生成的控制动作进行验证，评估其是否满足物理约束和安全要求。4) **优化器**：根据物理验证器的反馈，调整语言模型的参数，优化控制策略。

**关键创新**：最重要的技术创新点在于将物理验证引入到策略优化循环中。与传统的模仿学习方法不同，本文提出的方法不是直接模仿专家策略，而是通过物理模型对策略进行验证和改进，从而确保控制动作的物理合理性和安全性。这种方法能够有效地解决通用AI模型在物理系统控制中面临的输入不忠实问题。

**关键设计**：关键设计包括：1) 使用3.6亿参数的紧凑语言模型，以降低计算成本和提高训练效率。2) 设计合适的损失函数，鼓励语言模型生成满足物理约束的控制策略。3) 通过大规模合成数据训练，提高模型的泛化能力和鲁棒性。4) 采用数据增强技术，增加训练数据的多样性，提高模型的性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23292v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23292v1/Figure_validation_scaling_bins.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23292v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，通过大规模训练，Agentic Physical AI模型能够实现超过500倍的方差崩溃，显著提高了控制策略的稳定性。模型能够自主拒绝70%的训练分布，并将95%的运行时执行集中在单个库策略上，表明模型学习到了有效的控制策略。此外，学习到的表示可以在不同的物理和连续输入模态之间转移，而无需架构修改，展示了模型的泛化能力。

## 🎯 应用场景

该研究成果可应用于核反应堆控制、智能制造、机器人控制等领域。通过构建领域特定的Agentic Physical AI，可以提高控制系统的安全性、可靠性和效率，降低人工干预的需求，并为实现自主控制提供技术支撑。未来，该方法有望推广到其他复杂物理系统的控制任务中。

## 📄 摘要（原文）

> The prevailing paradigm in AI for physical systems, scaling general-purpose foundation models toward universal multimodal reasoning, confronts a fundamental barrier at the control interface. Recent benchmarks show that even frontier vision-language models achieve only 50-53% accuracy on basic quantitative physics tasks, behaving as approximate guessers that preserve semantic plausibility while violating physical constraints. This input unfaithfulness is not a scaling deficiency but a structural limitation. Perception-centric architectures optimize parameter-space imitation, whereas safety-critical control demands outcome-space guarantees over executed actions. Here, we present a fundamentally different pathway toward domain-specific foundation models by introducing compact language models operating as Agentic Physical AI, in which policy optimization is driven by physics-based validation rather than perceptual inference. We train a 360-million-parameter model on synthetic reactor control scenarios, scaling the dataset from 10^3 to 10^5 examples. This induces a sharp phase transition absent in general-purpose models. Small-scale systems exhibit high-variance imitation with catastrophic tail risk, while large-scale models undergo variance collapse exceeding 500x reduction, stabilizing execution-level behavior. Despite balanced exposure to four actuation families, the model autonomously rejects approximately 70% of the training distribution and concentrates 95% of runtime execution on a single-bank strategy. Learned representations transfer across distinct physics and continuous input modalities without architectural modification.

