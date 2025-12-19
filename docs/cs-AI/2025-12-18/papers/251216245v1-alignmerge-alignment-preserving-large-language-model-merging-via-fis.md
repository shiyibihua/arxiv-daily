---
layout: default
title: AlignMerge - Alignment-Preserving Large Language Model Merging via Fisher-Guided Geometric Constraints
---

# AlignMerge - Alignment-Preserving Large Language Model Merging via Fisher-Guided Geometric Constraints

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16245" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16245v1</a>
  <a href="https://arxiv.org/pdf/2512.16245.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16245v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16245v1', 'AlignMerge - Alignment-Preserving Large Language Model Merging via Fisher-Guided Geometric Constraints')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aniruddha Roy, Jyoti Patel, Aman Chadha, Vinija Jain, Amitava Das

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**AlignMerge：通过Fisher引导的几何约束实现对齐保持的大语言模型合并**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型合并` `模型对齐` `Fisher-Rao几何` `几何约束优化` `安全性` `对齐质量指数` `模型融合`

## 📋 核心要点

1. 现有LLM合并方法在保持模型性能的同时，容易破坏模型的对齐性，导致安全性下降。
2. AlignMerge通过在Fisher-Rao几何空间中施加约束，显式地将对齐作为合并过程中的不变性来保持。
3. 实验表明，AlignMerge在多个模型上提高了对齐指标，同时保持或超过了最佳专家的指令遵循和推理能力。

## 📝 摘要（中文）

合并大型语言模型（LLM）是一种实用的方法，可以在不重新训练的情况下组合来自多个微调检查点的能力。然而，标准方案（线性权重平均、任务向量和Fisher加权平均）可能会在保持损失的同时悄然破坏对齐。我们认为合并不是一种数值技巧，而是一种围绕已对齐锚点的几何约束操作：必须引导融合以尊重安全性几何，而不是事后验证。我们引入AlignMerge，这是一个几何感知合并框架，它使对齐成为显式不变性。在指令调整基础周围的局部Fisher图中，我们使用投影算子P_A估计对齐子空间并优化：L_AlignMerge = L_geo + lambda_align * L_align + lambda_bud * L_bud，其中L_geo使合并结果在Fisher-Rao几何中接近其专家，L_align惩罚沿对齐敏感方向的运动，L_bud强制执行软对齐预算。作为对齐函数，我们使用解码不变的对齐质量指数（AQI），这是一个潜在空间标准，用于捕获对齐和未对齐行为在表示空间中分离的清晰程度。在五个模型系列（LLaMA-3 8B、Mistral 7B、Qwen 2、Phi-3.5、Gemma 2）中，将安全锚点与任务专家合并，AlignMerge提高了对齐指标（AQI、毒性、LLM-judge对齐），同时在指令遵循、推理和帮助性方面匹配或超过了最佳专家。与Fisher soups、TIES、SafeMerge和MergeAlign相比，它还表现出更小的对齐子空间漂移和更少的预算违规。这些结果使对齐保持合并成为首要的设计目标，并为未来基础模型的几何感知组合提供了一条途径。

## 🔬 方法详解

**问题定义**：现有的大语言模型合并方法，如线性权重平均、任务向量等，虽然可以保持模型的性能指标，但往往会忽略模型的对齐性，导致合并后的模型在安全性、毒性等方面表现不佳。这些方法没有将对齐作为合并过程中的一个重要约束条件，容易产生意想不到的副作用。

**核心思路**：AlignMerge的核心思路是将模型合并视为一个几何约束优化问题，在Fisher-Rao几何空间中，通过约束合并后的模型使其接近原始模型，并同时保持模型的对齐性。这种方法显式地将对齐作为合并过程中的不变性，从而避免了对齐性的损失。

**技术框架**：AlignMerge框架主要包含以下几个关键部分：1) 在指令调整后的基础模型周围构建局部Fisher图；2) 使用投影算子估计对齐子空间；3) 定义包含几何约束、对齐约束和预算约束的损失函数L_AlignMerge；4) 通过优化L_AlignMerge来实现模型的合并。

**关键创新**：AlignMerge的关键创新在于它将模型合并问题转化为一个几何约束优化问题，并显式地考虑了模型的对齐性。与现有方法相比，AlignMerge不是简单地对模型权重进行平均，而是通过在Fisher-Rao几何空间中施加约束，来保证合并后的模型在保持性能的同时，也能够保持良好的对齐性。

**关键设计**：AlignMerge的关键设计包括：1) 使用Fisher-Rao几何来度量模型之间的距离；2) 使用对齐质量指数（AQI）作为对齐性的度量标准；3) 定义包含几何损失L_geo、对齐损失L_align和预算损失L_bud的损失函数L_AlignMerge；4) 通过调整lambda_align和lambda_bud来平衡对齐性和性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16245v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16245v1/figures/mechanistic.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16245v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

AlignMerge在五个模型系列（LLaMA-3 8B、Mistral 7B、Qwen 2、Phi-3.5、Gemma 2）上进行了评估，结果表明，与Fisher soups、TIES、SafeMerge和MergeAlign等基线方法相比，AlignMerge在提高对齐指标（AQI、毒性、LLM-judge对齐）的同时，能够匹配或超过最佳专家在指令遵循、推理和帮助性方面的性能。此外，AlignMerge还表现出更小的对齐子空间漂移和更少的预算违规。

## 🎯 应用场景

AlignMerge可应用于安全LLM的构建，通过合并不同领域的专家模型，在不牺牲安全性的前提下，提升模型在特定任务上的性能。该方法还可用于构建更可靠、更可控的LLM，降低模型产生有害或不当输出的风险，促进LLM在安全敏感领域的应用。

## 📄 摘要（原文）

> Merging large language models (LLMs) is a practical way to compose capabilities from multiple fine-tuned checkpoints without retraining. Yet standard schemes (linear weight soups, task vectors, and Fisher-weighted averaging) can preserve loss while quietly destroying alignment. We argue that merging is not a numerical trick but a geometry-constrained operation around an already-aligned anchor: fusion must be steered to respect safety geometry, not validated post hoc.
>   We introduce AlignMerge, a geometry-aware merging framework that makes alignment an explicit invariant. In a local Fisher chart around an instruction-tuned base, we estimate an alignment subspace with projector P_A and optimize:
>   L_AlignMerge = L_geo + lambda_align * L_align + lambda_bud * L_bud,
>   where L_geo keeps the merge close to its experts in Fisher-Rao geometry, L_align penalizes motion along alignment-sensitive directions, and L_bud enforces a soft alignment budget. As the alignment functional we use the decoding-invariant Alignment Quality Index (AQI), a latent-space criterion that captures how cleanly aligned and misaligned behaviors separate in representation space.
>   Across five model families (LLaMA-3 8B, Mistral 7B, Qwen 2, Phi-3.5, Gemma 2), merging safety anchors with task experts, AlignMerge improves alignment metrics (AQI, toxicity, LLM-judge alignment) while matching or exceeding the best expert on instruction-following, reasoning, and helpfulness. It also exhibits smaller alignment-subspace drift and fewer budget violations than Fisher soups, TIES, SafeMerge, and MergeAlign. These results make alignment-preserving merging a first-class design goal and suggest a path to geometry-aware composition of future foundation models.

