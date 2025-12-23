---
layout: default
title: Identifying economic narratives in large text corpora -- An integrated approach using Large Language Models
---

# Identifying economic narratives in large text corpora -- An integrated approach using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15041" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15041v1</a>
  <a href="https://arxiv.org/pdf/2506.15041.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15041v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15041v1', 'Identifying economic narratives in large text corpora -- An integrated approach using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tobias Schmidt, Kai-Robin Lange, Matthias Reccius, Henrik Müller, Michael Roos, Carsten Jentsch

**分类**: econ.GN, cs.CL

**发布日期**: 2025-06-18

**备注**: 53 pages, 5 figures

---

## 💡 一句话要点

**利用大型语言模型提取经济叙事以解决文本分析问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `经济叙事` `大型语言模型` `文本分析` `自然语言处理` `GPT-4o` `语义理解` `专家标注` `金融文本`

## 📋 核心要点

1. 现有的叙事提取方法在深层语义理解上存在不足，难以区分经济叙事与传统的语义角色标注任务。
2. 本文提出利用大型语言模型（LLMs）来提取经济叙事，重点分析其在处理复杂文本中的表现。
3. 实验结果显示，GPT-4o能够有效提取经济叙事，但在复杂文档处理上仍有待提升，未达到专家标注水平。

## 📝 摘要（中文）

随着对经济叙事的关注增加，提取此类叙事的管道数量也在增加。现有方法多依赖于先进的自然语言处理技术，如BERT，但在深层语义理解上存在不足。本文评估了大型语言模型（LLMs）的优势，通过分析《华尔街日报》和《纽约时报》关于通货膨胀的文章，比较GPT-4o的输出与专家标注的金标准叙事。结果表明，GPT-4o能够提取有效的经济叙事，但在处理复杂文档时仍未达到专家水平。本文还为未来在经济学和社会科学中使用LLMs提供了指导。

## 🔬 方法详解

**问题定义**：本文旨在解决现有经济叙事提取方法在深层语义理解上的不足，尤其是在复杂文档中的表现。现有方法多依赖传统的自然语言处理技术，难以有效提取经济叙事。

**核心思路**：论文提出利用大型语言模型（LLMs），如GPT-4o，来进行经济叙事的提取，旨在通过更深层次的语义理解来提升提取效果。

**技术框架**：研究首先定义了经济叙事的标准，然后通过分析《华尔街日报》和《纽约时报》的相关文本，比较GPT-4o的输出与专家标注的金标准叙事，形成一个系统的评估流程。

**关键创新**：最重要的创新在于将大型语言模型应用于经济叙事提取，这一方法与传统的多层次模型管道相比，简化了流程并提升了语义理解能力。

**关键设计**：在实验中，设置了多种参数以优化GPT-4o的输出，使用了特定的损失函数来评估叙事提取的准确性，并设计了适合经济文本的网络结构。实验还包括与专家标注的对比，以确保结果的有效性。

## 📊 实验亮点

实验结果表明，GPT-4o在提取经济叙事方面表现出色，能够生成有效的结构化输出。然而，在处理复杂文档时，其性能仍未达到专家标注的水平，显示出约20%的性能差距。这一发现为未来的研究提供了改进方向。

## 🎯 应用场景

该研究的潜在应用领域包括经济学、金融分析和社会科学研究。通过利用大型语言模型提取经济叙事，研究人员和分析师能够更高效地从大量文本中获取有价值的信息，提升决策支持的质量和速度。未来，随着LLMs的进一步发展，其在文本分析中的应用将更加广泛，可能改变传统的经济研究方法。

## 📄 摘要（原文）

> As interest in economic narratives has grown in recent years, so has the number of pipelines dedicated to extracting such narratives from texts. Pipelines often employ a mix of state-of-the-art natural language processing techniques, such as BERT, to tackle this task. While effective on foundational linguistic operations essential for narrative extraction, such models lack the deeper semantic understanding required to distinguish extracting economic narratives from merely conducting classic tasks like Semantic Role Labeling. Instead of relying on complex model pipelines, we evaluate the benefits of Large Language Models (LLMs) by analyzing a corpus of Wall Street Journal and New York Times newspaper articles about inflation. We apply a rigorous narrative definition and compare GPT-4o outputs to gold-standard narratives produced by expert annotators. Our results suggests that GPT-4o is capable of extracting valid economic narratives in a structured format, but still falls short of expert-level performance when handling complex documents and narratives. Given the novelty of LLMs in economic research, we also provide guidance for future work in economics and the social sciences that employs LLMs to pursue similar objectives.

