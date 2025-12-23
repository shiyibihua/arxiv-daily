---
layout: default
title: Context-Informed Grounding Supervision
---

# Context-Informed Grounding Supervision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15480" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15480v1</a>
  <a href="https://arxiv.org/pdf/2506.15480.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15480v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15480v1', 'Context-Informed Grounding Supervision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hyunji Lee, Seunghyun Yoon, Yunjae Won, Hanseok Oh, Geewook Kim, Trung Bui, Franck Dernoncourt, Elias Stengel-Eskin, Mohit Bansal, Minjoon Seo

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-18

---

## 💡 一句话要点

**提出上下文信息引导监督以解决生成模型的基础问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `上下文信息引导` `生成模型` `后训练监督` `多模态学习` `信息检索`

## 📋 核心要点

1. 现有方法在推理时简单附加上下文，无法确保生成内容的基础性，导致幻觉现象频发。
2. 本文提出上下文信息引导监督（CINGS），通过在响应前添加上下文并仅对响应计算损失，增强模型的基础生成能力。
3. 实验结果显示，CINGS在11个信息检索数据集上超越其他训练方法，并在视觉-语言领域中有效减少幻觉现象。

## 📝 摘要（中文）

大型语言模型（LLMs）常常需要外部知识来提供未编码的信息或减少幻觉现象。然而，简单地在推理时附加上下文并不能确保生成的内容是有依据的。为此，本文提出了上下文信息引导监督（CINGS），通过在响应前添加相关上下文进行后训练监督，仅对响应标记计算损失，并屏蔽上下文。实验表明，使用CINGS训练的模型在文本和视觉领域的基础生成能力上优于标准的指令调优模型，并且在视觉-语言领域中，CINGS训练的模型在四个基准测试中减少了幻觉现象，同时保持了生成内容的事实一致性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在生成过程中对外部上下文的依赖不足，现有方法在推理时简单附加上下文，无法确保生成内容的基础性，导致幻觉现象频发。

**核心思路**：提出上下文信息引导监督（CINGS），通过在响应前添加相关上下文进行后训练监督，计算损失时仅针对响应标记，屏蔽上下文，以增强模型对外部信息的依赖。

**技术框架**：CINGS的整体架构包括两个主要阶段：首先是模型训练阶段，在此阶段将上下文与响应结合；其次是推理阶段，模型生成响应时依赖于训练中学习到的上下文信息。

**关键创新**：CINGS的核心创新在于其训练策略，通过仅对响应计算损失，促使模型在生成时更好地利用外部上下文，从而显著减少幻觉现象。

**关键设计**：在损失函数设计上，CINGS采用了屏蔽上下文的策略，确保模型在训练时专注于响应的生成，同时保持了对上下文的潜在依赖。

## 📊 实验亮点

实验结果显示，CINGS在文本领域的11个信息检索数据集上超越了其他训练方法，并且在视觉-语言领域中，CINGS训练的模型在四个基准测试中减少了幻觉现象，保持了生成内容的事实一致性，未对下游任务的整体性能造成负面影响。

## 🎯 应用场景

该研究的潜在应用领域包括信息检索、对话系统和多模态生成任务。通过增强模型对外部上下文的依赖，CINGS能够提高生成内容的准确性和一致性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models (LLMs) are often supplemented with external knowledge to provide information not encoded in their parameters or to reduce hallucination. In such cases, we expect the model to generate responses by grounding its response in the provided external context. However, prior work has shown that simply appending context at inference time does not ensure grounded generation. To address this, we propose Context-INformed Grounding Supervision (CINGS), a post-training supervision in which the model is trained with relevant context prepended to the response, while computing the loss only over the response tokens and masking out the context. Our experiments demonstrate that models trained with CINGS exhibit stronger grounding in both textual and visual domains compared to standard instruction-tuned models. In the text domain, CINGS outperforms other training methods across 11 information-seeking datasets and is complementary to inference-time grounding techniques. In the vision-language domain, replacing a vision-language model's LLM backbone with a CINGS-trained model reduces hallucinations across four benchmarks and maintains factual consistency throughout the generated response. This improved grounding comes without degradation in general downstream performance. Finally, we analyze the mechanism underlying the enhanced grounding in CINGS and find that it induces a shift in the model's prior knowledge and behavior, implicitly encouraging greater reliance on the external context.

