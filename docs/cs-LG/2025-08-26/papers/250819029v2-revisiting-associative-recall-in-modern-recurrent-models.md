---
layout: default
title: Revisiting associative recall in modern recurrent models
---

# Revisiting associative recall in modern recurrent models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19029" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19029v2</a>
  <a href="https://arxiv.org/pdf/2508.19029.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19029v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19029v2', 'Revisiting associative recall in modern recurrent models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Destiny Okpekpe, Antonio Orvieto

**分类**: cs.LG

**发布日期**: 2025-08-26 (更新: 2025-10-10)

---

## 💡 一句话要点

**探讨现代递归模型中的联想回忆问题及其优化策略**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `联想回忆` `递归模型` `变换器` `学习率优化` `模型扩展` `深度学习`

## 📋 核心要点

1. 现有的现代递归模型在推理和记忆任务上表现不如变换器，尤其是在联想回忆基准测试中。
2. 论文提出通过优化学习率和分析模型扩展策略，来改善现代递归模型在联想回忆任务中的表现。
3. 实验结果显示，学习率对模型性能影响显著，且递归模型在宽度扩展时表现优于深度扩展。

## 📝 摘要（中文）

尽管现代递归深度学习模型（如状态空间模型）在复杂度上具有优势，但近期研究指出其在推理和记忆任务上相较于变换器存在不足。本文深入探讨联想回忆（AR）基准，分析了标定和优化问题对新提出的令牌混合策略的影响。研究表明，学习率的选择对现代递归模型的性能至关重要，并且递归模型与基于注意力的模型在宽度与深度扩展时表现出不同的优势。通过架构消融实验，研究了不同组件对变换器和Mamba性能及优化稳定性的影响。

## 🔬 方法详解

**问题定义**：本文旨在解决现代递归模型在联想回忆任务中的性能不足，尤其是学习率选择对模型训练的影响。现有方法在这方面的研究较少，导致性能波动较大。

**核心思路**：通过深入分析学习率和模型结构对联想回忆任务的影响，提出优化策略以提升现代递归模型的稳定性和性能。

**技术框架**：研究首先分析了学习率对模型性能的影响，然后比较了递归模型与注意力模型在宽度和深度扩展时的表现，最后通过架构消融实验评估不同组件的影响。

**关键创新**：论文的创新点在于揭示了学习率在现代递归模型中的重要性，以及递归模型与注意力模型在不同扩展策略下的性能差异，尤其是注意力模型在单层情况下无法有效解决联想回忆问题。

**关键设计**：研究中对学习率进行了系统的调优，并通过实验验证了不同层数的变换器在训练动态上的相似性，尤其是1层变换器的训练动态与2层变换器的归纳头形成相似。

## 📊 实验亮点

实验结果表明，优化学习率后，现代递归模型在联想回忆任务中的性能显著提升，尤其是在宽度扩展时表现优于深度扩展。此外，1层变换器的训练动态与2层变换器相似，尽管其性能较差，这一发现为后续研究提供了新的视角。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、机器翻译和对话系统等。通过优化递归模型的性能，可以提升这些领域中的模型表现，尤其是在需要记忆和推理的任务中。未来，这些优化策略可能会推动更高效的模型设计和训练方法的发展。

## 📄 摘要（原文）

> Despite the advantageous subquadratic complexity of modern recurrent deep learning models -- such as state-space models (SSMs) -- recent studies have highlighted their potential shortcomings compared to transformers on reasoning and memorization tasks. In this paper, we dive deeper into one of such benchmarks: associative recall (AR), which has been shown to correlate well with language modeling performance, and inspect in detail the effects of scaling and optimization issues in recently proposed token mixing strategies. We first demonstrate that, unlike standard transformers, the choice of learning rate plays a critical role in the performance of modern recurrent models: an issue that can severely affect reported performance in previous works and suggests further research is needed to stabilize training. Next, we show that recurrent and attention-based models exhibit contrasting benefits when scaling in width as opposed to depth, with attention being notably unable to solve AR when limited to a single layer. We then further inspect 1-layer transformers, revealing that despite their poor performance, their training dynamics surprisingly resemble the formation of induction heads, a phenomenon previously observed only in their 2-layer counterparts. Finally, through architectural ablations, we study how components affects Transformer and Mamba's performance and optimization stability.

