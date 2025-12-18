---
layout: default
title: Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception
---

# Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15333" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15333v1</a>
  <a href="https://arxiv.org/pdf/2509.15333.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15333v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15333v1', 'Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yulin Wang, Yang Yue, Yang Yue, Huanqian Wang, Haojun Jiang, Yizeng Han, Zanlin Ni, Yifan Pu, Minglei Shi, Rui Lu, Qisen Yang, Andrew Zhao, Zhuofan Xia, Shiji Song, Gao Huang

**分类**: cs.CV, cs.AI, cs.LG, eess.IV

**发布日期**: 2025-09-18

**🔗 代码/项目**: [GITHUB](https://github.com/LeapLabTHU/AdaptiveNN)

---

## 💡 一句话要点

**提出AdaptiveNN，通过模仿人类自适应视觉实现高效灵活的机器视觉感知**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自适应视觉` `强化学习` `序列决策` `视觉感知` `高效计算`

## 📋 核心要点

1. 现有机器视觉模型被动处理整个场景，导致资源消耗巨大，难以适应复杂环境和实际应用。
2. AdaptiveNN模仿人类视觉的自适应机制，通过序列注视和增量信息融合，实现高效的视觉感知。
3. 实验表明，AdaptiveNN在多个任务上实现了显著的推理成本降低，并展现出与人类相似的感知行为。

## 📝 摘要（中文）

人类视觉具有高度的适应性，通过顺序地注视任务相关的区域来高效地采样复杂环境。相比之下，目前流行的机器视觉模型被动地一次性处理整个场景，导致过度的资源需求，并随着时空输入分辨率和模型大小而扩展，从而产生阻碍未来发展和实际应用的关键限制。本文介绍AdaptiveNN，一个旨在推动从“被动”到“主动、自适应”视觉模型范式转变的通用框架。AdaptiveNN将视觉感知构建为一个由粗到精的顺序决策过程，逐步识别和关注与任务相关的区域，增量地组合跨注视的信息，并在信息充足时主动结束观察。我们建立了一个将表征学习与自奖励强化学习相结合的理论，从而能够对不可微的AdaptiveNN进行端到端训练，而无需对注视位置进行额外的监督。我们在涵盖9个任务的17个基准上评估了AdaptiveNN，包括大规模视觉识别、细粒度判别、视觉搜索、处理来自真实驾驶和医疗场景的图像、语言驱动的具身AI，以及与人类的并排比较。AdaptiveNN在不牺牲准确性的前提下，实现了高达28倍的推理成本降低，灵活地适应不同的任务需求和资源预算而无需重新训练，并通过其注视模式提供了增强的可解释性，展示了通往高效、灵活和可解释的计算机视觉的有希望的途径。此外，AdaptiveNN在许多情况下表现出与人类非常相似的感知行为，揭示了其作为研究视觉认知的宝贵工具的潜力。

## 🔬 方法详解

**问题定义**：现有机器视觉模型通常采用被动式处理方式，即一次性处理整个图像或视频帧，导致计算资源消耗巨大，尤其是在处理高分辨率或长时间序列数据时。这种被动式处理方式忽略了人类视觉系统选择性关注重要区域的能力，限制了模型在资源受限环境下的应用，并且缺乏可解释性。

**核心思路**：AdaptiveNN的核心思路是模仿人类视觉系统的自适应注视机制，将视觉感知过程建模为一个序列决策过程。模型通过逐步识别和关注与任务相关的区域，并增量地融合来自不同注视点的信息，从而实现高效的视觉感知。这种自适应的方式允许模型在信息充足时主动停止观察，进一步降低计算成本。

**技术框架**：AdaptiveNN的整体框架包含以下几个主要模块：1) **注视点预测器**：负责预测下一个需要关注的区域。2) **视觉编码器**：提取当前注视区域的视觉特征。3) **信息融合模块**：将来自不同注视点的视觉特征进行融合，形成对整个场景的综合理解。4) **决策模块**：根据融合后的信息，做出最终的预测或决策。整个过程通过强化学习进行端到端训练，无需额外的注视点标注。

**关键创新**：AdaptiveNN最重要的创新点在于其将视觉感知建模为一个自适应的序列决策过程，并采用强化学习进行训练。与传统的被动式视觉模型相比，AdaptiveNN能够根据任务需求和场景内容动态地调整其关注区域，从而实现更高的效率和灵活性。此外，AdaptiveNN的注视模式也提供了更强的可解释性。

**关键设计**：AdaptiveNN的关键设计包括：1) 使用深度强化学习（例如，Actor-Critic算法）训练注视点预测器，奖励函数的设计鼓励模型关注信息量大的区域，并尽早做出准确的预测。2) 采用循环神经网络（RNN）或Transformer等序列模型作为信息融合模块，以有效地整合来自不同注视点的信息。3) 设计合适的探索策略，鼓励模型探索不同的注视模式，避免陷入局部最优。

## 📊 实验亮点

AdaptiveNN在17个基准测试中表现出色，涵盖大规模视觉识别、细粒度判别、视觉搜索等任务。在不牺牲准确性的前提下，AdaptiveNN实现了高达28倍的推理成本降低。此外，AdaptiveNN在真实驾驶和医疗场景中也表现出良好的适应性。与人类的并排比较表明，AdaptiveNN在许多情况下表现出与人类非常相似的感知行为。

## 🎯 应用场景

AdaptiveNN具有广泛的应用前景，包括自动驾驶、医疗影像分析、机器人导航、视频监控等领域。其高效的计算特性使其能够在资源受限的设备上运行，例如移动设备和嵌入式系统。此外，AdaptiveNN的可解释性使其能够帮助人们更好地理解模型的决策过程，从而提高模型的可靠性和可信度。未来，AdaptiveNN有望成为一种通用的视觉感知框架，推动计算机视觉技术的发展。

## 📄 摘要（原文）

> Human vision is highly adaptive, efficiently sampling intricate environments by sequentially fixating on task-relevant regions. In contrast, prevailing machine vision models passively process entire scenes at once, resulting in excessive resource demands scaling with spatial-temporal input resolution and model size, yielding critical limitations impeding both future advancements and real-world application. Here we introduce AdaptiveNN, a general framework aiming to drive a paradigm shift from 'passive' to 'active, adaptive' vision models. AdaptiveNN formulates visual perception as a coarse-to-fine sequential decision-making process, progressively identifying and attending to regions pertinent to the task, incrementally combining information across fixations, and actively concluding observation when sufficient. We establish a theory integrating representation learning with self-rewarding reinforcement learning, enabling end-to-end training of the non-differentiable AdaptiveNN without additional supervision on fixation locations. We assess AdaptiveNN on 17 benchmarks spanning 9 tasks, including large-scale visual recognition, fine-grained discrimination, visual search, processing images from real driving and medical scenarios, language-driven embodied AI, and side-by-side comparisons with humans. AdaptiveNN achieves up to 28x inference cost reduction without sacrificing accuracy, flexibly adapts to varying task demands and resource budgets without retraining, and provides enhanced interpretability via its fixation patterns, demonstrating a promising avenue toward efficient, flexible, and interpretable computer vision. Furthermore, AdaptiveNN exhibits closely human-like perceptual behaviors in many cases, revealing its potential as a valuable tool for investigating visual cognition. Code is available at https://github.com/LeapLabTHU/AdaptiveNN.

