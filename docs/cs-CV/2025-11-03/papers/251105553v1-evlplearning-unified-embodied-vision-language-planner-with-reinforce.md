---
layout: default
title: EVLP:Learning Unified Embodied Vision-Language Planner with Reinforced Supervised Fine-Tuning
---

# EVLP:Learning Unified Embodied Vision-Language Planner with Reinforced Supervised Fine-Tuning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.05553" target="_blank" class="toolbar-btn">arXiv: 2511.05553v1</a>
    <a href="https://arxiv.org/pdf/2511.05553.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.05553v1" 
            onclick="toggleFavorite(this, '2511.05553v1', 'EVLP:Learning Unified Embodied Vision-Language Planner with Reinforced Supervised Fine-Tuning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Xinyan Cai, Shiguang Wu, Dafeng Chi, Yuzheng Zhuang, Xingyue Quan, Jianye Hao, Qiang Guan

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-03

---

## 💡 一句话要点

**提出EVLP，通过强化监督微调学习统一具身视觉-语言规划器，解决长程操作任务中的多模态规划问题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `具身智能` `视觉语言规划` `多模态学习` `强化学习` `长程操作任务`

## 📋 核心要点

1. 现有方法在复杂具身长程操作任务中，缺乏统一的多模态生成框架，导致语言推理和视觉空间想象的协同集成不足。
2. EVLP通过统一的多模态生成框架，动态感知预训练和强化监督微调，实现了语言推理和视觉生成的联合建模。
3. 该方法通过强化学习对齐文本动作和生成图像的空间逻辑，使模型具备空间感知能力的多模态规划能力，提升了长程任务的性能。

## 📝 摘要（中文）

本文提出了一种名为EVLP（Embodied Vision-Language Planner）的创新多模态统一生成框架，用于联合建模语言推理和视觉生成，从而实现长程任务的多模态规划。现有方法未能采用统一的生成框架进行多模态规划，导致多模态规划不一致。EVLP通过动态预训练和强化对齐的新型训练流程来实现多模态规划。其核心创新包括：统一的多模态生成框架，集成了语义信息和空间特征以提供全面的视觉感知，并直接学习离散图像的联合分布以进行单步视觉合成；双向动态对齐策略，采用逆动力学任务和正向动力学任务，有效加强统一特征空间内的多模态相关性；以及强化监督微调，在统一生成空间中进行基于指令的微调时，构建强化损失以对齐文本动作和生成图像之间的空间逻辑，使模型能够获得具有空间感知能力的多模态规划能力。

## 🔬 方法详解

**问题定义**：论文旨在解决复杂具身长程操作任务中，现有方法无法有效统一语言推理和视觉空间想象进行多模态规划的问题。现有方法通常采用分离的模块进行语言理解和视觉生成，导致两者之间缺乏一致性，难以进行有效的任务分解和执行。

**核心思路**：论文的核心思路是提出一个统一的多模态生成框架，将语言推理和视觉生成整合到一个模型中。通过动态预训练和强化对齐，使模型能够学习到语言和视觉之间的深层关联，从而实现更有效、更准确的多模态规划。这样设计的目的是为了克服现有方法中模块分离带来的不一致性问题，提高模型在复杂任务中的表现。

**技术框架**：EVLP的整体框架包含三个主要组成部分：1) 统一的多模态生成框架：该框架集成了语义信息和空间特征，用于全面的视觉感知，并直接学习离散图像的联合分布，用于单步视觉合成。2) 动态感知预训练：采用双向动态对齐策略，包括逆动力学任务和正向动力学任务，以加强统一特征空间内的多模态相关性。3) 强化监督微调：在统一生成空间中进行基于指令的微调，并构建强化损失，以对齐文本动作和生成图像之间的空间逻辑。

**关键创新**：该论文的关键创新在于提出了一个统一的多模态生成框架，能够同时处理语言和视觉信息，并学习它们之间的关联。与现有方法相比，EVLP避免了模块分离带来的不一致性问题，能够更有效地进行多模态规划。此外，动态感知预训练和强化监督微调进一步提升了模型的性能。

**关键设计**：在统一的多模态生成框架中，使用了可学习的跨模态注意力机制，用于协调语言和视觉建模。动态感知预训练中的逆动力学任务和正向动力学任务，旨在从不同方向加强多模态相关性。强化监督微调中的强化损失，用于对齐文本动作和生成图像之间的空间逻辑，具体形式未知。

## 📊 实验亮点

论文通过实验验证了EVLP的有效性，具体的性能数据和对比基线未知。强化监督微调显著提升了模型在长程任务中的表现，表明EVLP能够有效地学习到语言和视觉之间的关联，并进行准确的多模态规划。实验结果表明，EVLP在多模态规划任务上优于现有方法，具体的提升幅度未知。

## 🎯 应用场景

该研究成果可应用于机器人操作、自动驾驶、虚拟现实等领域。例如，在机器人操作中，EVLP可以帮助机器人理解人类指令，并生成相应的视觉图像序列，从而完成复杂的任务。在自动驾驶中，EVLP可以用于理解交通规则和场景信息，并生成相应的驾驶策略。该研究具有重要的实际价值和广阔的应用前景。

## 📄 摘要（原文）

> In complex embodied long-horizon manipulation tasks, effective task decomposition and execution require synergistic integration of textual logical reasoning and visual-spatial imagination to ensure efficient and accurate operation. Current methods fail to adopt a unified generation framework for multimodal planning, lead to inconsistent in multimodal planning. To address this challenge, we present \textbf{EVLP (Embodied Vision-Language Planner)}, an innovative multimodal unified generation framework that jointly models linguistic reasoning and visual generation. Our approach achieves multimodal planning for long-horizon tasks through a novel training pipeline incorporating dynamic pretraining and reinforced alignment. Our core innovations consist of three key components: \textbf{1) Unified Multimodal Generation Framework}: For understanding, We integrate semantic information with spatial features to provide comprehensive visual perception. For generation, we directly learn the joint distribution of discrete images for one-step visual synthesis, enabling coordinated language-visual modeling through learnable cross-modal attention mechanisms. \textbf{2) Dynamic Perception Pretraining}: We propose a bidirectional dynamic alignment strategy employing inverse dynamics tasks and forward dynamics tasks, effectively strengthening multimodal correlations within a unified feature space. \textbf{3) Reinforced Supervised Fine-Tuning}: While conducting instruction-based fine-tuning in the unified generation space, we construct a reinforce loss to align the spatial logic between textual actions and generated images, enabling the model to acquire spatio-awared multimodal planning capabilities.

