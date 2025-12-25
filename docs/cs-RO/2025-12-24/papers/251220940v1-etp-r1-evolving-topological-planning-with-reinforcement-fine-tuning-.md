---
layout: default
title: "ETP-R1: Evolving Topological Planning with Reinforcement Fine-tuning for Vision-Language Navigation in Continuous Environments"
---

# ETP-R1: Evolving Topological Planning with Reinforcement Fine-tuning for Vision-Language Navigation in Continuous Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20940" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20940v1</a>
  <a href="https://arxiv.org/pdf/2512.20940.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20940v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20940v1', 'ETP-R1: Evolving Topological Planning with Reinforcement Fine-tuning for Vision-Language Navigation in Continuous Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuhao Ye, Sitong Mao, Yuxiang Cui, Xuan Yu, Shichao Zhai, Wen Chen, Shunbo Zhou, Rong Xiong, Yue Wang

**分类**: cs.RO

**发布日期**: 2025-12-24

**备注**: 8 pages, 6 figures

**🔗 代码/项目**: [GITHUB](https://github.com/Cepillar/ETP-R1)

---

## 💡 一句话要点

**ETP-R1：通过强化微调演化拓扑规划，解决连续环境下的视觉-语言导航问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言导航` `连续环境` `拓扑规划` `强化学习` `预训练` `大型语言模型` `机器人导航`

## 📋 核心要点

1. 现有基于图的VLN-CE方法在利用大规模数据和先进训练范式方面落后于基于LVLM的方法。
2. ETP-R1通过构建大规模预训练数据集和引入强化微调，提升了基于图的VLN-CE模型的性能。
3. 实验结果表明，ETP-R1在R2R-CE和RxR-CE基准测试中取得了新的state-of-the-art性能。

## 📝 摘要（中文）

本文提出ETP-R1框架，旨在弥合基于图的视觉-语言导航在连续环境（VLN-CE）中的方法与基于大型视觉-语言模型（LVLMs）的方法之间的差距。ETP-R1将数据规模化和强化微调（RFT）应用于基于图的VLN-CE模型。首先，利用Gemini API构建高质量、大规模的预训练数据集，该数据集包含多样化的、低幻觉的拓扑轨迹指令，为基于图的策略提供了丰富的监督，以将语言映射到拓扑路径。通过统一来自R2R和RxR任务的数据进行联合预训练，进一步加强了这一基础。在此基础上，引入了一个三阶段的训练范式，最终将闭环、在线RFT首次应用于基于图的VLN-CE模型，并由Group Relative Policy Optimization (GRPO)算法提供支持。大量实验表明，该方法非常有效，在R2R-CE和RxR-CE基准测试中都建立了新的最先进的性能。

## 🔬 方法详解

**问题定义**：视觉-语言导航在连续环境（VLN-CE）中，智能体需要根据自然语言指令在连续环境中导航到目标位置。现有基于图的方法虽然通过将环境抽象为拓扑地图并简化动作空间（仅需选择航点）提高了效率，但在利用大规模数据和先进训练范式方面不如基于大型视觉-语言模型（LVLMs）的方法。因此，如何提升基于图的方法的性能，使其能够充分利用大规模数据和先进训练范式，是本文要解决的问题。

**核心思路**：本文的核心思路是将数据规模化和强化微调（RFT）应用于基于图的VLN-CE模型。通过构建大规模、高质量的预训练数据集，为模型提供丰富的监督信息，使其能够更好地将语言指令映射到拓扑路径。然后，通过强化微调进一步优化模型的策略，使其能够在真实环境中更好地导航。

**技术框架**：ETP-R1框架包含三个主要阶段：1) **数据构建阶段**：利用Gemini API生成大规模、高质量的预训练数据集，包含多样化的、低幻觉的拓扑轨迹指令。2) **预训练阶段**：使用R2R和RxR任务的数据进行联合预训练，提升模型的泛化能力。3) **强化微调阶段**：使用Group Relative Policy Optimization (GRPO)算法进行闭环、在线强化微调，进一步优化模型的策略。

**关键创新**：本文的关键创新在于首次将闭环、在线强化微调应用于基于图的VLN-CE模型。此外，利用Gemini API构建大规模、高质量的预训练数据集也是一个重要的创新点，它为模型提供了丰富的监督信息，使其能够更好地学习语言指令和环境之间的关系。

**关键设计**：在数据构建阶段，使用Gemini API生成多样化的、低幻觉的拓扑轨迹指令。在预训练阶段，使用交叉熵损失函数来训练模型，使其能够更好地预测正确的拓扑路径。在强化微调阶段，使用Group Relative Policy Optimization (GRPO)算法来优化模型的策略，GRPO算法通过比较不同智能体的策略来减少方差，提高训练的稳定性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20940v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20940v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20940v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

ETP-R1在R2R-CE和RxR-CE基准测试中都取得了新的state-of-the-art性能。具体来说，在R2R-CE基准测试中，ETP-R1在所有主要指标上都优于现有方法。在RxR-CE基准测试中，ETP-R1也取得了显著的性能提升，表明该方法具有很强的泛化能力。

## 🎯 应用场景

该研究成果可应用于机器人导航、虚拟现实、智能家居等领域。例如，可以利用该技术开发能够根据用户语音指令在复杂环境中自主导航的机器人，或者构建更加智能化的虚拟现实环境，使用户可以通过自然语言与虚拟环境进行交互。此外，该技术还可以应用于智能家居领域，实现更加便捷的语音控制和自动化服务。

## 📄 摘要（原文）

> Vision-Language Navigation in Continuous Environments (VLN-CE) requires an embodied agent to navigate towards target in continuous environments, following natural language instructions. While current graph-based methods offer an efficient, structured approach by abstracting the environment into a topological map and simplifying the action space to waypoint selection, they lag behind methods based on Large Vision-Language Models (LVLMs) in leveraging large-scale data and advanced training paradigms. In this paper, we try to bridge this gap by introducing ETP-R1, a framework that applies the paradigm of scaling up data and Reinforcement Fine-Tuning (RFT) to a graph-based VLN-CE model. To build a strong foundation, we first construct a high-quality, large-scale pretraining dataset using the Gemini API. This dataset consists of diverse, low-hallucination instructions for topological trajectories, providing rich supervision for our graph-based policy to map language to topological paths. This foundation is further strengthened by unifying data from both R2R and RxR tasks for joint pretraining. Building on this, we introduce a three-stage training paradigm, which culminates in the first application of closed-loop, online RFT to a graph-based VLN-CE model, powered by the Group Relative Policy Optimization (GRPO) algorithm. Extensive experiments demonstrate that our approach is highly effective, establishing new state-of-the-art performance across all major metrics on both the R2R-CE and RxR-CE benchmarks. Our code is available at https://github.com/Cepillar/ETP-R1.

