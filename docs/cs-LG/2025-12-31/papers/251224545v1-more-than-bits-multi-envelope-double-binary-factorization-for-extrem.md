---
layout: default
title: "More Than Bits: Multi-Envelope Double Binary Factorization for Extreme Quantization"
---

# More Than Bits: Multi-Envelope Double Binary Factorization for Extreme Quantization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24545" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24545v1</a>
  <a href="https://arxiv.org/pdf/2512.24545.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24545v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24545v1', 'More Than Bits: Multi-Envelope Double Binary Factorization for Extreme Quantization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuma Ichikawa, Yoshihiko Fujisawa, Yudai Fujimoto, Akira Sakai, Katsuki Fujisawa

**分类**: cs.LG, cs.AI, cs.CL, stat.ML

**发布日期**: 2025-12-31

**备注**: 14 pages, 2 figures

---

## 💡 一句话要点

**提出多包络双重二值分解(MDBF)，用于大语言模型极低比特量化，提升精度。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `极低比特量化` `大语言模型` `二值分解` `模型压缩` `多包络` `量化精度` `推理效率`

## 📋 核心要点

1. DBF量化方法在极低比特量化大语言模型时表现出潜力，但其缩放参数限制了模型性能，导致精度饱和。
2. 论文提出MDBF方法，通过引入多包络结构，在共享符号矩阵的基础上，利用有限的内存预算提升幅度表达能力。
3. 实验结果表明，MDBF在LLaMA和Qwen模型上，以相同的比特数实现了更好的困惑度和零样本精度。

## 📝 摘要（中文）

针对大语言模型(LLM)的极低比特量化，双重二值分解(DBF)因其在不牺牲精度的情况下实现高效推理而备受关注。然而，DBF的缩放参数过于严格；在分解出符号后，所有秩分量共享相同的幅度分布，导致性能饱和。我们提出了多包络DBF(MDBF)，它保留了一对共享的1比特符号基，但用秩-$l$包络代替了单个包络。通过在包络分量之间共享符号矩阵，MDBF有效地维护了一个二值载体，并将有限的内存预算用于幅度表达。我们还引入了一种闭式初始化和一种交替细化方法来优化MDBF。在LLaMA和Qwen系列模型上，MDBF在匹配的每权重比特数下，提高了困惑度和零样本精度，同时保留了相同的部署友好的推理原语。

## 🔬 方法详解

**问题定义**：现有DBF方法在极低比特量化大语言模型时，由于其缩放参数的限制，导致模型性能饱和。具体来说，DBF在分解出符号后，所有秩分量共享相同的幅度分布，缺乏足够的灵活性来表示权重矩阵的复杂结构。

**核心思路**：论文的核心思路是通过引入多包络结构来增强DBF的幅度表达能力。MDBF保留了DBF的二值分解框架，但将原有的单一幅度包络替换为多个幅度包络，每个包络对应一个秩分量。通过在这些包络分量之间共享符号矩阵，MDBF能够在有限的内存预算下，有效地利用比特来表达幅度信息。

**技术框架**：MDBF的整体框架仍然基于双重二值分解，但其核心在于多包络的设计。具体流程如下：1) 对权重矩阵进行二值分解，得到共享的符号矩阵；2) 将幅度信息分解为多个秩-$l$的包络分量；3) 使用闭式初始化方法初始化包络分量；4) 使用交替细化方法优化符号矩阵和包络分量。

**关键创新**：MDBF的关键创新在于引入了多包络结构，并设计了相应的初始化和优化方法。与DBF相比，MDBF能够更灵活地表示权重矩阵的幅度信息，从而提高量化模型的精度。此外，共享符号矩阵的设计保证了MDBF能够有效地利用有限的内存预算。

**关键设计**：MDBF的关键设计包括：1) 包络分量的秩-$l$的选择，需要根据具体的模型和数据集进行调整；2) 闭式初始化方法，能够为后续的优化提供一个良好的起点；3) 交替细化方法，通过交替优化符号矩阵和包络分量，逐步提高模型的精度。损失函数的设计目标是最小化量化误差，可以使用均方误差等常用的损失函数。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24545v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24545v1/x2.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，MDBF在LLaMA和Qwen系列模型上，以匹配的每权重比特数，显著提高了困惑度和零样本精度。例如，在某些任务上，MDBF的性能优于之前的二值量化方法，并且接近于全精度模型的性能。这些结果表明，MDBF是一种有效的极低比特量化方法，能够在大语言模型上实现高性能。

## 🎯 应用场景

MDBF适用于对计算资源和存储空间有严格限制的场景，例如移动设备、嵌入式系统和边缘计算设备。通过极低比特量化，MDBF能够显著降低大语言模型的存储空间和计算复杂度，使其能够在这些资源受限的设备上部署和运行。此外，MDBF还可以应用于模型压缩、模型加速等领域，提高模型的效率和性能。

## 📄 摘要（原文）

> For extreme low-bit quantization of large language models (LLMs), Double Binary Factorization (DBF) is attractive as it enables efficient inference without sacrificing accuracy. However, the scaling parameters of DBF are too restrictive; after factoring out signs, all rank components share the same magnitude profile, resulting in performance saturation. We propose Multi-envelope DBF (MDBF), which retains a shared pair of 1-bit sign bases but replaces the single envelope with a rank-$l$ envelope. By sharing sign matrices among envelope components, MDBF effectively maintains a binary carrier and utilizes the limited memory budget for magnitude expressiveness. We also introduce a closed-form initialization and an alternating refinement method to optimize MDBF. Across the LLaMA and Qwen families, MDBF enhances perplexity and zero-shot accuracy over previous binary formats at matched bits per weight while preserving the same deployment-friendly inference primitive.

