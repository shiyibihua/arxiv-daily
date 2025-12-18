---
layout: default
title: Tracing and Mitigating Hallucinations in Multimodal LLMs via Dynamic Attention Localization
---

# Tracing and Mitigating Hallucinations in Multimodal LLMs via Dynamic Attention Localization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07864" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07864v2</a>
  <a href="https://arxiv.org/pdf/2509.07864.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07864v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07864v2', 'Tracing and Mitigating Hallucinations in Multimodal LLMs via Dynamic Attention Localization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tiancheng Yang, Lin Zhang, Jiaye Lin, Guimin Hu, Di Wang, Lijie Hu

**分类**: cs.CV

**发布日期**: 2025-09-09 (更新: 2025-11-17)

---

## 💡 一句话要点

**提出D-LEAF以解决多模态LLM中的幻觉问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大型语言模型` `幻觉抑制` `动态注意力` `图像描述` `视觉问答` `模型优化` `注意力机制`

## 📋 核心要点

1. 现有多模态大型语言模型在生成文本时容易出现幻觉现象，导致生成内容与视觉输入不一致，影响模型的可靠性。
2. 本文提出了动态层次熵和注意力融合（D-LEAF）方法，通过动态定位和修正模型中的错误，显著提高了模型的性能。
3. 实验结果显示，D-LEAF在图像描述任务上相对提升53%，在视觉问答任务中准确率和F1分数均提高约4%。

## 📝 摘要（中文）

多模态大型语言模型（MLLMs）在图像描述和视觉问答等任务中表现出色，但仍然容易出现幻觉现象，即生成的文本与视觉输入不一致。现有方法通常将注意力调整均匀应用于各层和头，导致无法准确定位错误来源。本文首先指出这些方法在定位问题层时的不足，接着引入了层图像注意力熵（LIAE）和图像注意力聚焦（IAF）两个诊断工具，前者用于标记异常层，后者用于评分这些层内的注意力头。基于这些信号，提出了一种动态层次熵和注意力融合（D-LEAF）的方法，在推理过程中动态定位和修正错误，且开销极小。实验结果表明，D-LEAF在标准描述基准上实现了53%的相对提升，在视觉问答任务中准确率和F1分数均提高约4%。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大型语言模型中生成文本与视觉输入不一致的问题，即幻觉现象。现有方法在调整注意力时未能准确定位问题层，导致错误难以修正。

**核心思路**：提出的D-LEAF方法通过引入层图像注意力熵（LIAE）和图像注意力聚焦（IAF）两个诊断工具，动态定位并修正模型中的错误，从而提高生成文本的准确性。

**技术框架**：D-LEAF的整体架构包括两个主要模块：LIAE用于识别异常层，IAF用于评分注意力头。通过这两个模块的协同作用，模型能够在推理过程中实时调整注意力分配。

**关键创新**：D-LEAF的核心创新在于其动态调整机制，能够在推理时根据实时反馈修正注意力分配，而不是采用静态的均匀调整方式。这一设计使得模型在处理复杂输入时更具灵活性和准确性。

**关键设计**：在D-LEAF中，LIAE和IAF的计算方法经过精心设计，以确保能够有效识别和评分注意力头。此外，模型的损失函数和参数设置经过优化，以实现最佳的性能提升。

## 📊 实验亮点

实验结果显示，D-LEAF在标准图像描述基准上实现了53%的相对提升，在视觉问答任务中，准确率和F1分数均提高约4%。这些结果表明，D-LEAF在抑制幻觉现象的同时，保持了模型的高效性。

## 🎯 应用场景

该研究的潜在应用领域包括图像描述、视觉问答和其他多模态任务。通过提高模型在这些任务中的准确性和可靠性，D-LEAF能够为实际应用提供更高质量的生成结果，进而推动智能助手、自动内容生成等领域的发展。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) achieve strong performance on tasks like image captioning and visual question answering, but remain prone to hallucinations, where generated text conflicts with the visual input. Prior work links this partly to insufficient visual attention, but existing attention-based detectors and mitigation typically apply uniform adjustments across layers and heads, obscuring where errors originate. In this paper, we first show these methods fail to accurately localize problematic layers. Then, we introduce two diagnostics: Layer Image Attention Entropy (LIAE) which flags anomalous layers, and Image Attention Focus (IAF) which scores attention heads within those layers. Analysis shows that LIAE pinpoints faulty layers and IAF reliably ranks heads that warrant correction. Guided by these signals, we propose Dynamic Layer-wise Entropy and Attention Fusion (D-LEAF), a task-agnostic, attention-guided method that dynamically localizes and corrects errors during inference with negligible overhead. Furthermore, by establishing a connection between D-LEAF and DPO, we provide theoretical justification for the effectiveness of D-LEAF. Results show our D-LEAF delivers a 53\% relative improvement on standard captioning benchmarks, and on VQA both accuracy and F1-score improve by approximately 4\%, substantially suppressing hallucinations while preserving efficiency.

