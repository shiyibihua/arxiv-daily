---
layout: default
title: Human Preference-Aligned Concept Customization Benchmark via Decomposed Evaluation
---

# Human Preference-Aligned Concept Customization Benchmark via Decomposed Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03385" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03385v1</a>
  <a href="https://arxiv.org/pdf/2509.03385.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03385v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03385v1', 'Human Preference-Aligned Concept Customization Benchmark via Decomposed Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Reina Ishikawa, Ryo Fujii, Hideo Saito, Ryo Hachiuma

**分类**: cs.CV

**发布日期**: 2025-09-03

**备注**: Accepted to ICCV Workshop 2025

**🔗 代码/项目**: [GITHUB](https://github.com/ReinaIshikawa/D-GPTScore)

---

## 💡 一句话要点

**提出D-GPTScore，通过分解评估解决概念定制评估与人类偏好不一致问题**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `概念定制` `多模态学习` `大型语言模型` `图像评估` `人类偏好对齐`

## 📋 核心要点

1. 现有概念定制评估方法在保真度和概念交互评估上存在不足，与人类直观感受存在偏差。
2. D-GPTScore通过将评估标准分解为更细粒度的方面，并结合MLLM进行评估，实现与人类偏好对齐。
3. CC-AlignBench基准数据集包含单概念和多概念任务，D-GPTScore在该基准上显著优于现有方法。

## 📝 摘要（中文）

概念定制的评估极具挑战性，它需要全面评估生成提示和概念图像的保真度。评估多个概念比评估单个概念更加困难，因为它不仅需要对每个概念进行详细评估，还需要评估概念之间的相互作用。现有指标通常提供过于狭隘或过于泛化的评估，导致与人类偏好不一致。为了解决这个问题，我们提出了一种新的人类对齐评估方法D-GPTScore，该方法将评估标准分解为更精细的方面，并使用多模态大型语言模型（MLLM）进行基于方面的评估。此外，我们发布了人类偏好对齐的概念定制基准CC-AlignBench，该基准数据集包含单概念和多概念任务，能够跨越从个体动作到多人互动的广泛难度范围进行阶段性评估。我们的方法在这个基准上显著优于现有方法，表现出与人类偏好更高的相关性。这项工作为评估概念定制建立了一个新标准，并强调了未来研究的关键挑战。

## 🔬 方法详解

**问题定义**：概念定制旨在根据用户提供的概念图像和文本提示生成图像，其评估的难点在于如何准确衡量生成图像与用户意图的匹配程度，特别是当涉及多个概念时，需要同时评估每个概念的保真度以及它们之间的交互关系。现有评估指标要么过于关注单一维度，要么过于泛化，无法准确反映人类的偏好。

**核心思路**：D-GPTScore的核心思路是将评估过程分解为多个更细粒度的方面，例如概念的保真度、概念间的关系、图像的整体质量等。通过对每个方面进行独立评估，可以更全面地了解生成图像的优缺点，并更好地与人类的偏好对齐。使用MLLM进行评估是因为MLLM具有强大的多模态理解能力，能够同时处理图像和文本信息，从而更准确地评估生成图像的质量。

**技术框架**：D-GPTScore的整体框架包含以下几个主要步骤：1) 将评估任务分解为多个方面；2) 使用MLLM对每个方面进行评估，生成相应的评估分数；3) 将各个方面的评估分数进行加权平均，得到最终的评估结果。权重可以根据不同的任务和数据集进行调整，以更好地反映人类的偏好。

**关键创新**：D-GPTScore的关键创新在于其分解评估的思想和MLLM的应用。通过分解评估，可以更全面地了解生成图像的优缺点，并更好地与人类的偏好对齐。MLLM的应用使得评估过程更加自动化和客观，避免了人工评估的主观性。

**关键设计**：D-GPTScore的关键设计包括：1) 评估方面的选择：根据不同的任务和数据集，选择合适的评估方面；2) MLLM的选择和训练：选择具有强大的多模态理解能力的MLLM，并使用相关数据进行训练，以提高其评估准确性；3) 权重设置：根据不同的评估方面，设置合适的权重，以更好地反映人类的偏好。

## 📊 实验亮点

D-GPTScore在CC-AlignBench基准数据集上取得了显著的性能提升，与现有方法相比，与人类偏好的相关性更高。实验结果表明，D-GPTScore能够更准确地评估概念定制的效果，并为未来的研究提供了新的方向。

## 🎯 应用场景

该研究成果可应用于各种概念定制场景，例如个性化图像生成、虚拟现实内容创作、以及辅助设计等领域。通过更准确地评估生成图像的质量，可以提高用户满意度，并促进相关技术的发展。未来，该方法还可以扩展到其他生成任务的评估中，例如视频生成、3D模型生成等。

## 📄 摘要（原文）

> Evaluating concept customization is challenging, as it requires a comprehensive assessment of fidelity to generative prompts and concept images. Moreover, evaluating multiple concepts is considerably more difficult than evaluating a single concept, as it demands detailed assessment not only for each individual concept but also for the interactions among concepts. While humans can intuitively assess generated images, existing metrics often provide either overly narrow or overly generalized evaluations, resulting in misalignment with human preference. To address this, we propose Decomposed GPT Score (D-GPTScore), a novel human-aligned evaluation method that decomposes evaluation criteria into finer aspects and incorporates aspect-wise assessments using Multimodal Large Language Model (MLLM). Additionally, we release Human Preference-Aligned Concept Customization Benchmark (CC-AlignBench), a benchmark dataset containing both single- and multi-concept tasks, enabling stage-wise evaluation across a wide difficulty range -- from individual actions to multi-person interactions. Our method significantly outperforms existing approaches on this benchmark, exhibiting higher correlation with human preferences. This work establishes a new standard for evaluating concept customization and highlights key challenges for future research. The benchmark and associated materials are available at https://github.com/ReinaIshikawa/D-GPTScore.

