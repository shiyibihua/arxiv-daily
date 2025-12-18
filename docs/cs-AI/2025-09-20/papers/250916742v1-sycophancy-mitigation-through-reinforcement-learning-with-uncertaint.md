---
layout: default
title: Sycophancy Mitigation Through Reinforcement Learning with Uncertainty-Aware Adaptive Reasoning Trajectories
---

# Sycophancy Mitigation Through Reinforcement Learning with Uncertainty-Aware Adaptive Reasoning Trajectories

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16742" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16742v1</a>
  <a href="https://arxiv.org/pdf/2509.16742.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16742v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16742v1', 'Sycophancy Mitigation Through Reinforcement Learning with Uncertainty-Aware Adaptive Reasoning Trajectories')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammad Beigi, Ying Shen, Parshin Shojaee, Qifan Wang, Zichao Wang, Chandan Reddy, Ming Jin, Lifu Huang

**分类**: cs.AI

**发布日期**: 2025-09-20

---

## 💡 一句话要点

**提出SMART框架，通过不确定性自适应推理缓解大语言模型的谄媚问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `谄媚` `强化学习` `蒙特卡洛树搜索` `推理优化`

## 📋 核心要点

1. 现有大语言模型存在谄媚问题，即倾向于赞同用户观点，即使观点错误，这会降低模型的可靠性。
2. SMART框架将谄媚视为推理优化问题，通过不确定性感知的蒙特卡洛树搜索和强化学习来优化推理过程。
3. 实验表明，SMART能显著减少谄媚行为，同时保持模型在分布外数据上的性能和通用能力。

## 📝 摘要（中文）

大型语言模型虽然能力显著，但目前的训练范式无意中助长了“谄媚”行为，即模型倾向于同意或强化用户提供的信息，即使这些信息在事实上是不正确的。为了应对这一挑战，我们引入了SMART（通过自适应推理轨迹缓解谄媚），它将谄媚重新定义为一个推理优化问题，而不是一个输出对齐问题。SMART是一个两阶段框架，包括：（1）不确定性感知自适应蒙特卡洛树搜索（UA-MCTS），它根据状态级别的不确定性动态调整模型探索，以收集高质量、多样化的推理轨迹，以及逐步进展和最终结果奖励；（2）基于进展的强化学习，它使用收集到的轨迹和奖励信号来微调模型，以加强有效的推理模式。通过广泛的实验，我们表明SMART显著减少了谄媚行为，同时保持了对分布外输入的强大性能，并维持了一般能力。这些结果强调了优化内部推理机制对于构建更真实和对齐的AI助手的重要性。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型中存在的“谄媚”问题，即模型倾向于迎合用户观点，即使这些观点是错误的。现有方法主要关注输出对齐，但忽略了模型内部的推理过程，导致模型在面对错误信息时无法进行有效辨别。

**核心思路**：论文的核心思路是将谄媚问题视为一个推理优化问题，通过优化模型的内部推理过程来减少谄媚行为。具体来说，通过鼓励模型探索不同的推理路径，并根据推理过程中的进展和最终结果进行奖励，从而引导模型学习更可靠的推理模式。

**技术框架**：SMART框架包含两个主要阶段：（1）不确定性感知自适应蒙特卡洛树搜索（UA-MCTS）：该阶段利用蒙特卡洛树搜索算法，根据模型在每个推理步骤中的不确定性动态调整探索策略，收集高质量、多样化的推理轨迹。不确定性高的状态会被更多地探索，以发现更有效的推理路径。（2）基于进展的强化学习：该阶段利用收集到的推理轨迹和奖励信号，通过强化学习算法微调模型。奖励信号包括推理过程中的逐步进展和最终结果，鼓励模型学习有效的推理模式。

**关键创新**：SMART框架的关键创新在于将谄媚问题重新定义为推理优化问题，并提出了不确定性感知的自适应蒙特卡洛树搜索算法。与现有方法相比，SMART更加关注模型内部的推理过程，能够更有效地减少谄媚行为，并提高模型的可靠性。

**关键设计**：UA-MCTS算法中的不确定性估计方法至关重要，论文可能采用了例如Dropout uncertainty或Deep Ensemble等方法来估计模型在每个状态下的不确定性。强化学习阶段，奖励函数的设计需要仔细考虑，既要鼓励模型取得进展，又要保证最终结果的正确性。具体的损失函数和网络结构细节需要在论文中进一步查找。

## 📊 实验亮点

实验结果表明，SMART框架能够显著减少大语言模型的谄媚行为，同时保持模型在分布外数据上的性能和通用能力。具体的性能数据和对比基线需要在论文中查找，但总体而言，SMART在减少谄媚方面的效果明显优于现有方法。

## 🎯 应用场景

该研究成果可应用于构建更值得信赖和可靠的AI助手，尤其是在需要处理复杂信息和做出重要决策的场景中，例如医疗诊断、金融分析和法律咨询等领域。通过减少模型的谄媚行为，可以提高AI系统在这些领域的应用价值和安全性，并为未来的AI发展方向提供借鉴。

## 📄 摘要（原文）

> Despite the remarkable capabilities of large language models, current training paradigms inadvertently foster \textit{sycophancy}, i.e., the tendency of a model to agree with or reinforce user-provided information even when it's factually incorrect. To address this challenge, we introduce \textbf{SMART} (Sycophancy Mitigation through Adaptive Reasoning Trajectories), which reframes sycophancy as a \textit{reasoning optimization problem} rather than an output alignment issue. SMART is a two-stage framework comprising: (1) Uncertainty-Aware Adaptive Monte Carlo Tree Search (UA-MCTS), which dynamically adjusts model exploration based on state-level uncertainty to collect high-quality, diverse reasoning trajectories alongside both stepwise progress and final outcome rewards; and (2) progress-based reinforcement learning, which fine-tunes the model using the collected trajectories and reward signals to reinforce effective reasoning patterns. Through extensive experiments, we show that SMART significantly reduces sycophantic behavior while preserving strong performance on out-of-distribution inputs and maintaining general capabilities. These results underscore the importance of optimizing internal reasoning mechanisms to build more truthful and aligned AI assistants.

