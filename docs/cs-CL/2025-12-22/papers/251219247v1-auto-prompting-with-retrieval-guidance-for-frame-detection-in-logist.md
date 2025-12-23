---
layout: default
title: Auto-Prompting with Retrieval Guidance for Frame Detection in Logistics
---

# Auto-Prompting with Retrieval Guidance for Frame Detection in Logistics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19247" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19247v1</a>
  <a href="https://arxiv.org/pdf/2512.19247.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19247v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19247v1', 'Auto-Prompting with Retrieval Guidance for Frame Detection in Logistics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Do Minh Duc, Quan Xuan Truong, Nguyen Tat Dat, Nguyen Van Vinh

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**提出检索引导的自动Prompt优化方法，提升LLM在物流文本框架检测中的性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Prompt工程` `大型语言模型` `物流文本` `框架检测` `检索增强生成` `思维链` `自动Prompt优化`

## 📋 核心要点

1. 现有方法在将LLM应用于物流文本框架检测时，依赖人工设计的prompt，效率低且效果有限。
2. 论文提出一种基于检索引导的自动prompt优化方法，利用RAG、CoT等技术自动生成和优化prompt。
3. 实验结果表明，该方法在多个LLM上均能显著提升框架检测的准确率，最高提升达15%。

## 📝 摘要（中文）

本文提出了一种新颖的prompt优化流程，用于物流文本中的框架检测。该流程结合了检索增强生成（RAG）、少样本prompting、思维链（CoT）推理和自动CoT合成（Auto-CoT），以生成高效的任务特定prompt。核心是一个基于LLM的prompt优化代理，它使用检索到的示例、性能反馈和内部自我评估来迭代地改进prompt。该框架在实际的物流文本标注任务上进行了评估，实验结果表明，优化的prompt（特别是通过Auto-CoT和RAG增强的prompt）与基线零样本或静态prompt相比，实际推理准确率提高了15%。该系统在多个LLM（包括GPT-4o、Qwen 2.5 (72B)和LLaMA 3.1 (70B)）上表现出一致的改进，验证了其通用性和实用价值。这些发现表明，结构化的prompt优化是完全微调的可行替代方案，为在物流等特定领域的NLP应用中部署LLM提供了可扩展的解决方案。

## 🔬 方法详解

**问题定义**：论文旨在解决物流文本中框架检测任务的prompt工程问题。现有方法依赖人工设计prompt，耗时且效果受限于专家知识。此外，静态prompt难以适应复杂多变的物流场景，导致LLM推理精度不高。

**核心思路**：论文的核心思路是利用LLM自身的能力，通过检索增强和自动优化，生成更有效的任务特定prompt。通过检索相似的示例，为LLM提供上下文信息，并通过迭代优化prompt，使其更好地适应目标任务。

**技术框架**：整体框架包含以下几个主要模块：1) 检索模块：从预定义的语料库中检索与输入文本相关的示例；2) Prompt优化代理：基于LLM，利用检索到的示例、性能反馈和内部自我评估，迭代地改进prompt；3) 推理模块：使用优化后的prompt，利用LLM进行框架检测；4) 评估模块：评估LLM的推理结果，并将评估结果反馈给Prompt优化代理。

**关键创新**：最重要的技术创新点在于Prompt优化代理的设计。该代理能够利用检索增强和自动CoT合成技术，自动生成和优化prompt，无需人工干预。此外，该代理还能够进行内部自我评估，从而更有效地改进prompt。

**关键设计**：Prompt优化代理的关键设计包括：1) 使用RAG技术，从语料库中检索与输入文本相关的示例，为LLM提供上下文信息；2) 使用Auto-CoT技术，自动生成思维链，引导LLM进行推理；3) 使用性能反馈和内部自我评估，迭代地改进prompt；4) 使用特定的损失函数，优化prompt的生成过程（具体损失函数细节未知）。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19247v1/image/wordcloud.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19247v1/image/sentence_length_distribution.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19247v1/image/copy.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在实际物流文本标注任务中，与基线零样本或静态prompt相比，推理准确率提高了15%。该方法在多个LLM（包括GPT-4o、Qwen 2.5 (72B)和LLaMA 3.1 (70B)）上表现出一致的改进，验证了其通用性和实用价值。

## 🎯 应用场景

该研究成果可应用于智能物流领域，例如自动提取物流单据中的关键信息、识别异常物流事件、优化物流路径规划等。通过提升LLM在物流文本理解方面的能力，可以提高物流效率、降低运营成本，并为用户提供更优质的服务。未来，该方法还可以扩展到其他领域，例如金融、医疗等。

## 📄 摘要（原文）

> Prompt engineering plays a critical role in adapting large language models (LLMs) to complex reasoning and labeling tasks without the need for extensive fine-tuning. In this paper, we propose a novel prompt optimization pipeline for frame detection in logistics texts, combining retrieval-augmented generation (RAG), few-shot prompting, chain-of-thought (CoT) reasoning, and automatic CoT synthesis (Auto-CoT) to generate highly effective task-specific prompts. Central to our approach is an LLM-based prompt optimizer agent that iteratively refines the prompts using retrieved examples, performance feedback, and internal self-evaluation. Our framework is evaluated on a real-world logistics text annotation task, where reasoning accuracy and labeling efficiency are critical. Experimental results show that the optimized prompts - particularly those enhanced via Auto-CoT and RAG - improve real-world inference accuracy by up to 15% compared to baseline zero-shot or static prompts. The system demonstrates consistent improvements across multiple LLMs, including GPT-4o, Qwen 2.5 (72B), and LLaMA 3.1 (70B), validating its generalizability and practical value. These findings suggest that structured prompt optimization is a viable alternative to full fine-tuning, offering scalable solutions for deploying LLMs in domain-specific NLP applications such as logistics.

