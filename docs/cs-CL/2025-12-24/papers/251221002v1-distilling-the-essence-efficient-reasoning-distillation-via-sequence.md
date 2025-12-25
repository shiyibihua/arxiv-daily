---
layout: default
title: "Distilling the Essence: Efficient Reasoning Distillation via Sequence Truncation"
---

# Distilling the Essence: Efficient Reasoning Distillation via Sequence Truncation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21002" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21002v1</a>
  <a href="https://arxiv.org/pdf/2512.21002.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21002v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21002v1', 'Distilling the Essence: Efficient Reasoning Distillation via Sequence Truncation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wei-Rui Chen, Vignesh Kothapalli, Ata Fatahibaarzi, Hejian Sang, Shao Tang, Qingquan Song, Zhipeng Wang, Muhammad Abdul-Mageed

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-24

**🔗 代码/项目**: [GITHUB](https://github.com/weiruichen01/distilling-the-essence)

---

## 💡 一句话要点

**提出基于序列截断的高效推理蒸馏方法，加速LLM知识迁移。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识蒸馏` `大型语言模型` `推理能力` `序列截断` `计算效率`

## 📋 核心要点

1. 现有LLM推理能力蒸馏方法计算成本高昂，尤其是在处理包含长序列的推理数据时。
2. 该论文提出一种基于序列截断的蒸馏方法，通过优先考虑早期推理token来提高效率。
3. 实验表明，仅使用序列前50%的token进行训练，即可保留约94%的性能，同时显著降低计算成本。

## 📝 摘要（中文）

将大型语言模型(LLM)的推理能力提炼到较小的学生模型通常需要在大量的推理数据上进行训练。然而，在包含提示(P)、思维链(CoT)和答案(A)片段的冗长序列上进行蒸馏，使得计算成本非常高昂。本文研究了在不同片段(P, CoT, A)上分配监督信号如何影响学生模型的性能。分析表明，当提示和答案信息包含在CoT中时，仅对CoT token进行选择性知识蒸馏是有效的。基于此，本文建立了一个截断协议，以量化计算量与质量之间的权衡关系，作为序列长度的函数。观察到，仅在每个训练序列的前50%的token上进行训练，平均可以保留数学基准上完整序列性能的约94%，同时将训练时间、内存使用和FLOPs减少约50%。这些发现表明，推理蒸馏受益于优先考虑早期推理token，并提供了一个简单的计算量与质量权衡的手段。代码已在https://github.com/weiruichen01/distilling-the-essence上发布。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLM）推理能力蒸馏方法，在处理包含提示（Prompt）、思维链（Chain-of-Thought, CoT）和答案（Answer）的长序列数据时，计算成本非常高昂。传统的蒸馏方法需要对整个序列进行训练，导致训练时间长、内存占用大、FLOPs高，限制了其在资源受限环境下的应用。

**核心思路**：该论文的核心思路是，通过分析不同序列片段（Prompt、CoT、Answer）对学生模型性能的影响，发现CoT片段包含了Prompt和Answer的信息，因此只需要对CoT片段进行选择性知识蒸馏即可。进一步，通过截断序列，只保留序列的前一部分（例如前50%），来减少计算量，同时尽可能保留推理性能。这种方法基于一个假设，即推理过程的关键信息集中在序列的早期阶段。

**技术框架**：该论文的技术框架主要包含以下几个步骤：1) 分析Prompt、CoT和Answer片段对学生模型性能的影响；2) 建立一个序列截断协议，允许控制截断的比例；3) 在截断后的序列上进行知识蒸馏，训练学生模型；4) 评估学生模型在数学推理基准上的性能，并分析计算量与性能之间的权衡关系。

**关键创新**：该论文最重要的技术创新点在于，提出了基于序列截断的高效推理蒸馏方法。与传统的蒸馏方法不同，该方法不需要对整个序列进行训练，而是通过选择性地保留序列的早期部分，来减少计算量，同时尽可能保留推理性能。这种方法提供了一种简单而有效的计算量与质量权衡的手段。

**关键设计**：论文的关键设计包括：1) 截断比例的选择：通过实验分析不同截断比例对性能的影响，找到一个合适的截断比例，例如50%；2) 损失函数的设计：使用标准的知识蒸馏损失函数，例如KL散度损失，来衡量学生模型和教师模型之间的输出差异；3) 训练策略：使用标准的训练策略，例如Adam优化器，并设置合适的学习率和batch size。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21002v1/images/combined_section_inclusion_masking.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21002v1/images/one_training_ex_wide.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21002v1/images/combined_LSP.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，仅使用训练序列的前50%的token进行训练，平均可以保留数学基准上完整序列性能的约94%，同时将训练时间、内存使用和FLOPs减少约50%。这表明该方法在显著降低计算成本的同时，能够保持较高的推理性能。

## 🎯 应用场景

该研究成果可应用于各种需要将大型语言模型的推理能力迁移到小型模型的场景，例如移动设备、嵌入式系统等资源受限的环境。通过降低计算成本，可以使得更多设备能够运行复杂的推理任务，从而推动人工智能在边缘计算领域的应用。此外，该方法还可以用于加速模型开发和部署过程。

## 📄 摘要（原文）

> Distilling the reasoning capabilities from a large language model (LLM) to a smaller student model often involves training on substantial amounts of reasoning data. However, distillation over lengthy sequences with prompt (P), chain-of-thought (CoT), and answer (A) segments makes the process computationally expensive. In this work, we investigate how the allocation of supervision across different segments (P, CoT, A) affects student performance. Our analysis shows that selective knowledge distillation over only the CoT tokens can be effective when the prompt and answer information is encompassed by it. Building on this insight, we establish a truncation protocol to quantify computation-quality tradeoffs as a function of sequence length. We observe that training on only the first $50\%$ of tokens of every training sequence can retain, on average, $\approx94\%$ of full-sequence performance on math benchmarks while reducing training time, memory usage, and FLOPs by about $50\%$ each. These findings suggest that reasoning distillation benefits from prioritizing early reasoning tokens and provides a simple lever for computation-quality tradeoffs. Codes are available at https://github.com/weiruichen01/distilling-the-essence.

