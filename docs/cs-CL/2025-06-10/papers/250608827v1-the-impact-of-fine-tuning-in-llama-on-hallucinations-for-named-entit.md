---
layout: default
title: The impact of fine tuning in LLaMA on hallucinations for named entity extraction in legal documentation
---

# The impact of fine tuning in LLaMA on hallucinations for named entity extraction in legal documentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.08827" class="toolbar-btn" target="_blank">📄 arXiv: 2506.08827v1</a>
  <a href="https://arxiv.org/pdf/2506.08827.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.08827v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.08827v1', 'The impact of fine tuning in LLaMA on hallucinations for named entity extraction in legal documentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Francisco Vargas, Alejandro González Coene, Gaston Escalante, Exequiel Lobón, Manuel Pulido

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-10

**期刊**: Electronic Journal of SADIO; vol. 24 (2025), no. 1

---

## 💡 一句话要点

**提出基于LLaMA微调的命名实体提取方法以减少法律文档中的幻觉现象**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `命名实体提取` `法律文档分析` `大型语言模型` `微调技术` `信息提取` `机器学习` `文本处理`

## 📋 核心要点

1. 现有方法在法律文档中提取命名实体时容易产生幻觉，导致提取结果不准确。
2. 论文提出了一种两步法，首先进行文档分段，然后利用大型语言模型进行实体提取，旨在提高准确性。
3. 实验结果显示，微调后的LLaMA-2 70B模型准确率达到79.4%，显著高于经典方法的39.5%。

## 📝 摘要（中文）

从法律文档中提取交通事故信息对于量化保险公司成本至关重要。提取诸如身体和/或心理残疾的百分比及相关赔偿金额等实体的过程充满挑战，尤其是在法庭判决中存在微妙的论证和推理。本文提出了一种两步程序：首先对文档进行分段，识别最相关的部分，然后提取实体。通过比较经典的正则表达式方法与基于n-token块的向量化方法，结合多语言模型进行语义搜索，最终应用大型语言模型（如LLaMA和GPT-4 Turbo）进行实体提取。研究发现，经过LoRA微调的LLaMA模型在减少幻觉现象方面表现显著，LLaMA-2 70B的准确率达到79.4%，超越了基线的61.7%。

## 🔬 方法详解

**问题定义**：本文旨在解决从法律文档中提取命名实体时出现的幻觉现象，现有方法在处理复杂的法律语言时准确性不足，导致提取结果不可靠。

**核心思路**：提出一种两步法，首先对法律文档进行分段，识别出最相关的部分，然后利用大型语言模型进行实体提取，特别是对LLaMA模型进行微调以减少幻觉现象。

**技术框架**：整体流程包括文档分段、向量化、实体提取三个主要模块。文档分段采用经典的正则表达式方法与基于n-token块的向量化方法进行比较，随后使用LLaMA和GPT-4 Turbo等大型语言模型进行实体提取。

**关键创新**：通过对LLaMA模型进行LoRA微调，显著减少了在实体提取过程中出现的幻觉现象，提升了模型的准确性。与传统方法相比，微调后的模型在处理复杂法律文本时表现出更高的鲁棒性。

**关键设计**：在微调过程中，采用了特定的超参数设置和损失函数，以优化模型在法律文档中的表现，确保提取结果的准确性和可靠性。

## 📊 实验亮点

实验结果表明，微调后的LLaMA-2 70B模型在命名实体提取任务中准确率达到79.4%，显著高于经典方法的39.5%。此外，基线LLaMA-3 8B模型的表现也相当出色，达到76.6%，而GPT-4 Turbo则以86.1%的准确率成为最高表现者，展示了模型发展的快速进步。

## 🎯 应用场景

该研究可广泛应用于法律文档分析、保险索赔处理及其他需要从复杂文本中提取关键信息的领域。通过提高命名实体提取的准确性，能够有效降低保险公司的运营成本，并提升法律服务的效率。未来，该方法还可以扩展到其他类型的文档分析中，具有重要的实际价值。

## 📄 摘要（原文）

> The extraction of information about traffic accidents from legal documents is crucial for quantifying insurance company costs. Extracting entities such as percentages of physical and/or psychological disability and the involved compensation amounts is a challenging process, even for experts, due to the subtle arguments and reasoning in the court decision. A two-step procedure is proposed: first, segmenting the document identifying the most relevant segments, and then extracting the entities. For text segmentation, two methodologies are compared: a classic method based on regular expressions and a second approach that divides the document into blocks of n-tokens, which are then vectorized using multilingual models for semantic searches (text-embedding-ada-002/MiniLM-L12-v2 ). Subsequently, large language models (LLaMA-2 7b, 70b, LLaMA-3 8b, and GPT-4 Turbo) are applied with prompting to the selected segments for entity extraction. For the LLaMA models, fine-tuning is performed using LoRA. LLaMA-2 7b, even with zero temperature, shows a significant number of hallucinations in extractions which are an important contention point for named entity extraction. This work shows that these hallucinations are substantially reduced after finetuning the model. The performance of the methodology based on segment vectorization and subsequent use of LLMs significantly surpasses the classic method which achieves an accuracy of 39.5%. Among open-source models, LLaMA-2 70B with finetuning achieves the highest accuracy 79.4%, surpassing its base version 61.7%. Notably, the base LLaMA-3 8B model already performs comparably to the finetuned LLaMA-2 70B model, achieving 76.6%, highlighting the rapid progress in model development. Meanwhile, GPT-4 Turbo achieves the highest accuracy at 86.1%.

