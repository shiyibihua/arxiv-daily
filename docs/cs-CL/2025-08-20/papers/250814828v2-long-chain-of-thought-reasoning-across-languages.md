---
layout: default
title: Long Chain-of-Thought Reasoning Across Languages
---

# Long Chain-of-Thought Reasoning Across Languages

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14828" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14828v2</a>
  <a href="https://arxiv.org/pdf/2508.14828.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14828v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14828v2', 'Long Chain-of-Thought Reasoning Across Languages')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Josh Barua, Seun Eisape, Kayo Yin, Alane Suhr

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-20 (更新: 2025-10-09)

**备注**: v1 is a workshop version accepted to SCALR @ COLM 2025

---

## 💡 一句话要点

**研究多语言长链推理能力的迁移与提升**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长链推理` `多语言处理` `模型扩展` `预训练` `合成数据` `推理效率` `跨语言迁移`

## 📋 核心要点

1. 现有的推理模型在英语中表现优异，但其长链推理能力在其他语言中的迁移性尚不明确。
2. 本文通过比较En-CoT和Target-CoT两种推理设置，探讨模型扩展、预训练等对多语言推理能力的影响。
3. 研究结果表明，模型规模的扩大对En-CoT有利，但Target-CoT的性能提升有限，尤其在复杂任务中表现更为明显。

## 📝 摘要（中文）

尽管大型推理模型在英语中展现了生成长链推理（CoTs）的卓越能力，但我们仍然缺乏对这些能力如何迁移到其他语言的理解。本文系统性地研究了模型开发的四个关键阶段——扩展、预训练、后训练和推理，探讨长链推理能力在九种非英语目标语言中的表现。研究发现，模型规模的扩大提升了En-CoT的多语言任务性能，但Target-CoT的表现仍然滞后，尤其是在需要长多步推理的任务中。我们还探讨了合成数据的后训练方法，并展示了自动翻译的推理轨迹在Fine-tuning中的优势。最后，报告了不同语言推理效率的差异及其特定失败模式。

## 🔬 方法详解

**问题定义**：本文旨在解决大型推理模型在多语言环境下的长链推理能力迁移问题，现有方法在非英语语言中的表现不足。

**核心思路**：通过系统性研究模型的扩展、预训练、后训练和推理阶段，分析不同设置对多语言推理能力的影响，提出合成数据的后训练方法以提升Target-CoT性能。

**技术框架**：研究分为四个主要阶段：1) 扩展模型规模；2) 进行多语言预训练；3) 采用合成数据进行后训练；4) 进行推理效率分析。每个阶段都针对不同语言的推理能力进行评估。

**关键创新**：提出了在多语言环境中进行长链推理的系统性评估框架，并发现了在Target-CoT中性能滞后的现象，强调了合成数据在后训练中的重要性。

**关键设计**：在预训练阶段，采用了广泛的多语言数据集，而在后训练阶段则使用了自动翻译的推理轨迹进行Fine-tuning，以提升模型在目标语言中的表现。

## 📊 实验亮点

实验结果显示，模型规模的扩大在En-CoT中提升了多语言任务性能，但在Target-CoT中表现滞后，尤其在数学推理等复杂任务中，性能差距明显。此外，Fine-tuning使用自动翻译的推理轨迹相较于目标语言轨迹表现更佳，显示出合成数据的重要性。

## 🎯 应用场景

该研究的潜在应用场景包括多语言智能助手、跨语言教育工具以及全球化的自然语言处理系统。通过提升模型在多语言环境中的推理能力，可以更好地服务于不同语言用户的需求，推动人工智能的普及与应用。

## 📄 摘要（原文）

> While large reasoning models have shown remarkable ability to generate long chains-of-thought (CoTs) in English, we still lack understanding of how these long-form reasoning abilities transfer to the vast majority of the world's languages. In this work, we systematically investigate four key stages of model development--scaling, pretraining, post-training, and inference--to understand how long CoT capabilities extend beyond English. We compare two reasoning settings across nine non-English target languages: En-CoT, where models process target-language inputs, but reason in English; and Target-CoT, where models both process inputs and generate long CoTs in the target language. We find that scaling reasoning model size improves multilingual task performance in En-CoT, but Target-CoT performance lags behind. This gap widens for tasks requiring long, multi-step CoTs such as mathematical reasoning. Shifting to pretraining, we find that adding a specialized reasoning stage enhances En-CoT performance but degrades Target-CoT, whereas broad multilingual pretraining improves both modes simultaneously. Given the scarcity of high-quality reasoning traces in languages other than English, we explore synthetic data curation approaches for post-training. We demonstrate that fine-tuning on reasoning traces automatically translated from gold English traces outperforms fine-tuning on target-language traces distilled from large reasoning models. Finally, we report disparities in inference efficiency between languages and uncover language-specific failure modes in CoTs. We release models, datasets, and code to foster further research.

