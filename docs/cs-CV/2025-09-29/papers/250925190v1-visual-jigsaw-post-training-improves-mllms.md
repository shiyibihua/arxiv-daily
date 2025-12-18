---
layout: default
title: Visual Jigsaw Post-Training Improves MLLMs
---

# Visual Jigsaw Post-Training Improves MLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25190" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25190v1</a>
  <a href="https://arxiv.org/pdf/2509.25190.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25190v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25190v1', 'Visual Jigsaw Post-Training Improves MLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Penghao Wu, Yushan Zhang, Haiwen Diao, Bo Li, Lewei Lu, Ziwei Liu

**分类**: cs.CV

**发布日期**: 2025-09-29

**🔗 代码/项目**: [PROJECT_PAGE](https://penghao-wu.github.io/visual_jigsaw/)

---

## 💡 一句话要点

**Visual Jigsaw：通过视觉拼图后训练提升多模态大语言模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `视觉理解` `自监督学习` `后训练` `视觉拼图` `强化学习` `视觉模态` `排序任务`

## 📋 核心要点

1. 现有MLLM后训练方法侧重于文本，忽略了视觉理解的提升，视觉信息仅作为文本推理的辅助。
2. Visual Jigsaw通过自监督的视觉拼图任务，让模型学习重建打乱的视觉信息，从而提升视觉理解能力。
3. 实验证明，Visual Jigsaw在图像、视频和3D数据上均能有效提升MLLM的细粒度感知、时间推理和空间理解能力。

## 📝 摘要（中文）

基于强化学习的后训练已成为增强多模态大语言模型（MLLM）对齐和推理能力的有效范例。虽然以视觉为中心的后训练对于增强 MLLM 对视觉信号的内在理解至关重要，但当前的后训练范例主要以文本为中心，其中密集的视觉输入仅用于提取稀疏的线索以进行基于文本的推理。虽然存在一些朝这个方向发展的方法，但它们通常仍然依赖文本作为中间媒介或引入额外的视觉生成设计。在这项工作中，我们引入了 Visual Jigsaw，这是一个通用的自监督后训练框架，旨在加强 MLLM 中的视觉理解。Visual Jigsaw 被构建为一个通用的排序任务：视觉输入被分割、打乱，模型必须通过生成自然语言中的正确排列来重建视觉信息。这自然地与来自可验证奖励的强化学习（RLVR）对齐，不需要额外的视觉生成组件，并自动导出其监督信号，无需任何注释。我们在三种视觉模态（包括图像、视频和 3D 数据）上实例化 Visual Jigsaw。广泛的实验表明，在细粒度感知、时间推理和 3D 空间理解方面都有显著改进。我们的发现突出了以视觉为中心的自监督任务在后训练 MLLM 中的潜力，并旨在激发对以视觉为中心的前置任务设计的进一步研究。

## 🔬 方法详解

**问题定义**：现有MLLM的后训练方法主要集中在文本模态，视觉信息通常被用作文本推理的辅助。这导致模型在视觉理解方面存在不足，尤其是在细粒度感知、时间推理和3D空间理解等任务上。现有方法要么依赖文本作为中间媒介，要么引入额外的视觉生成模块，增加了复杂性。

**核心思路**：Visual Jigsaw的核心思路是通过一个自监督的视觉拼图任务来提升MLLM的视觉理解能力。具体来说，将视觉输入分割成多个部分并打乱顺序，然后要求模型预测正确的排列顺序。这种方式迫使模型学习理解视觉信息之间的关系，从而提升其视觉理解能力。

**技术框架**：Visual Jigsaw的整体框架包括以下步骤：1) 视觉输入分割：将图像、视频或3D数据分割成多个patch。2) 顺序打乱：随机打乱这些patch的顺序。3) 模型预测：MLLM接收打乱顺序的patch，并预测正确的排列顺序，以自然语言形式输出。4) 奖励计算：根据预测的排列顺序与真实顺序的匹配程度计算奖励，使用强化学习进行训练。

**关键创新**：Visual Jigsaw的关键创新在于其自监督的视觉拼图任务设计。与现有方法相比，它不需要额外的文本标注或视觉生成模块，而是通过一个简单的排序任务来提升视觉理解能力。此外，该方法可以很容易地应用于不同的视觉模态，包括图像、视频和3D数据。

**关键设计**：Visual Jigsaw的关键设计包括：1) Patch分割策略：根据不同的视觉模态选择合适的分割策略。2) 排列顺序预测：使用自然语言生成模型预测patch的排列顺序。3) 奖励函数：使用BLEU score等指标来衡量预测的排列顺序与真实顺序的匹配程度。4) 强化学习算法：使用PPO等算法来训练模型。

## 📊 实验亮点

实验结果表明，Visual Jigsaw 在图像、视频和 3D 数据上均能有效提升 MLLM 的性能。例如，在细粒度图像分类任务中，Visual Jigsaw 能够显著提高模型的准确率。在视频时间推理任务中，模型能够更准确地预测事件的发生顺序。在 3D 空间理解任务中，模型能够更好地理解物体的空间关系。

## 🎯 应用场景

Visual Jigsaw 有潜力应用于各种需要细粒度视觉理解的多模态任务，例如视频内容分析、医学影像诊断、自动驾驶和机器人导航。通过提升 MLLM 的视觉理解能力，可以提高这些应用场景的性能和可靠性，并为未来的多模态人工智能研究提供新的方向。

## 📄 摘要（原文）

> Reinforcement learning based post-training has recently emerged as a powerful paradigm for enhancing the alignment and reasoning capabilities of multimodal large language models (MLLMs). While vision-centric post-training is crucial for enhancing MLLMs' intrinsic understanding of visual signals, current post-training paradigms are predominantly text-centric, where dense visual inputs are only leveraged to extract sparse cues for text-based reasoning. There exist a few approaches in this direction, however, they often still rely on text as an intermediate mediator or introduce additional visual generative designs. In this work, we introduce Visual Jigsaw, a generic self-supervised post-training framework designed to strengthen visual understanding in MLLMs. Visual Jigsaw is formulated as a general ordering task: visual inputs are partitioned, shuffled, and the model must reconstruct the visual information by producing the correct permutation in natural language. This naturally aligns with reinforcement learning from verifiable rewards (RLVR), requires no additional visual generative components, and derives its supervisory signal automatically without any annotations. We instantiate Visual Jigsaw across three visual modalities, including images, videos, and 3D data. Extensive experiments demonstrate substantial improvements in fine-grained perception, temporal reasoning, and 3D spatial understanding. Our findings highlight the potential of self-supervised vision-centric tasks in post-training MLLMs and aim to inspire further research on vision-centric pretext designs. Project Page: https://penghao-wu.github.io/visual_jigsaw/

