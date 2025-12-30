---
layout: default
title: "FRoD: Full-Rank Efficient Fine-Tuning with Rotational Degrees for Fast Convergence"
---

# FRoD: Full-Rank Efficient Fine-Tuning with Rotational Degrees for Fast Convergence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23485" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23485v1</a>
  <a href="https://arxiv.org/pdf/2512.23485.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23485v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23485v1', 'FRoD: Full-Rank Efficient Fine-Tuning with Rotational Degrees for Fast Convergence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guoan Wan, Tianyu Chen, Fangzheng Feng, Haoyi Zhou, Runhua Xu

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-29

**备注**: The 40th Annual AAAI Conference on Artificial Intelligence

---

## 💡 一句话要点

**FRoD：利用旋转自由度实现全秩高效微调，加速模型收敛**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `参数高效微调` `全秩微调` `旋转自由度` `分层联合分解` `深度学习` `模型优化`

## 📋 核心要点

1. 现有PEFT方法受限于低秩约束，难以在效率和表达能力之间取得平衡，导致收敛速度慢，适应能力不足。
2. FRoD通过分层联合分解和旋转自由度，提取全局共享基，并注入稀疏可学习扰动，实现灵活的全秩更新。
3. 实验表明，FRoD在20个基准测试中，仅使用1.72%的可训练参数，即可达到与全模型微调相当的精度。

## 📝 摘要（中文）

参数高效微调（PEFT）方法已成为将大型基础模型适配到下游任务的实用解决方案，它通过仅更新一小部分参数来降低计算和内存成本。其中，LoRA等方法旨在平衡效率和表达能力，但由于其固有的低秩约束，常常面临收敛速度慢和适应能力有限的问题。这种权衡阻碍了PEFT方法捕捉多样化任务所需的复杂模式。为了解决这些挑战，我们提出了一种新的微调方法FRoD，它结合了分层联合分解和旋转自由度。通过提取跨层的全局共享基，并将稀疏的可学习扰动注入到缩放因子中，以实现灵活的全秩更新，FRoD增强了表达能力和效率，从而实现更快、更稳健的收敛。在涵盖视觉、推理和语言理解的20个基准测试中，FRoD在相同的训练预算下，仅使用1.72%的可训练参数，即可达到与全模型微调相当的精度。

## 🔬 方法详解

**问题定义**：现有参数高效微调方法（PEFT），如LoRA，虽然减少了计算和存储开销，但由于其低秩特性，限制了模型的表达能力，导致收敛速度慢，无法充分适应下游任务的复杂模式。因此，如何在保证效率的同时，提升PEFT方法的表达能力和收敛速度，是一个亟待解决的问题。

**核心思路**：FRoD的核心思路是打破低秩约束，实现高效的全秩微调。它通过提取跨层的全局共享基，并在此基础上引入稀疏的可学习扰动，从而在参数量较少的情况下，实现对模型参数的灵活调整。这种方法既保证了微调的效率，又提升了模型的表达能力。

**技术框架**：FRoD的技术框架主要包含两个关键步骤：1) 分层联合分解：对模型参数进行分解，提取跨层的全局共享基。这一步旨在减少参数冗余，提高微调效率。2) 旋转自由度注入：在全局共享基的基础上，引入稀疏的可学习扰动，并将其注入到缩放因子中。这些扰动通过旋转操作，实现对模型参数的灵活调整，从而提升模型的表达能力。

**关键创新**：FRoD最重要的技术创新在于其结合了分层联合分解和旋转自由度，实现了高效的全秩微调。与传统的低秩微调方法相比，FRoD能够更好地捕捉下游任务的复杂模式，从而提升模型的性能。此外，FRoD通过稀疏扰动的方式，进一步降低了参数量，提高了微调效率。

**关键设计**：FRoD的关键设计包括：1) 全局共享基的提取方法：具体采用何种分解方式提取全局共享基，例如奇异值分解（SVD）或其他矩阵分解方法。2) 稀疏扰动的注入方式：如何选择合适的稀疏模式，以及如何将扰动注入到缩放因子中。3) 旋转操作的具体实现：如何设计旋转矩阵，以实现对模型参数的灵活调整。论文中可能还涉及损失函数的设计，以引导模型学习到更有效的参数。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23485v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23485v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23485v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

FRoD在20个涵盖视觉、推理和语言理解的基准测试中表现出色。在相同的训练预算下，FRoD仅使用1.72%的可训练参数，即可达到与全模型微调相当的精度。这表明FRoD在保证效率的同时，显著提升了模型的性能。该结果突显了FRoD在参数高效微调方面的优势。

## 🎯 应用场景

FRoD具有广泛的应用前景，可用于各种大型预训练模型的微调，例如在自然语言处理、计算机视觉和语音识别等领域。它可以帮助企业和研究机构更高效地将大型模型应用于各种下游任务，降低计算成本和开发周期，加速人工智能技术的落地。此外，FRoD还可以促进模型的可持续发展，减少能源消耗。

## 📄 摘要（原文）

> Parameter-efficient fine-tuning (PEFT) methods have emerged as a practical solution for adapting large foundation models to downstream tasks, reducing computational and memory costs by updating only a small subset of parameters. Among them, approaches like LoRA aim to strike a balance between efficiency and expressiveness, but often suffer from slow convergence and limited adaptation capacity due to their inherent low-rank constraints. This trade-off hampers the ability of PEFT methods to capture complex patterns needed for diverse tasks. To address these challenges, we propose FRoD, a novel fine-tuning method that combines hierarchical joint decomposition with rotational degrees of freedom. By extracting a globally shared basis across layers and injecting sparse, learnable perturbations into scaling factors for flexible full-rank updates, FRoD enhances expressiveness and efficiency, leading to faster and more robust convergence. On 20 benchmarks spanning vision, reasoning, and language understanding, FRoD matches full model fine-tuning in accuracy, while using only 1.72% of trainable parameters under identical training budgets.

