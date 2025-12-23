---
layout: default
title: Zero-Shot Event Causality Identification via Multi-source Evidence Fuzzy Aggregation with Large Language Models
---

# Zero-Shot Event Causality Identification via Multi-source Evidence Fuzzy Aggregation with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05675" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05675v2</a>
  <a href="https://arxiv.org/pdf/2506.05675.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05675v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05675v2', 'Zero-Shot Event Causality Identification via Multi-source Evidence Fuzzy Aggregation with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zefan Zeng, Xingchen Hu, Qing Cheng, Weiping Ding, Wentao Li, Zhong Liu

**分类**: cs.CL

**发布日期**: 2025-06-06 (更新: 2025-06-09)

---

## 💡 一句话要点

**提出MEFA框架以解决事件因果关系识别中的数据依赖问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `事件因果关系识别` `零样本学习` `多源证据` `模糊聚合` `大型语言模型` `因果推理` `自然语言处理`

## 📋 核心要点

1. 现有的事件因果关系识别模型依赖于大量标注数据，导致其在数据稀缺情况下的性能下降。
2. 本文提出MEFA框架，通过多源证据模糊聚合，分解因果推理任务并引导LLMs生成更可靠的输出。
3. 实验结果显示，MEFA在多个基准测试中显著优于无监督基线，提升了F1-score和精确度，同时减少了因果幻觉错误。

## 📝 摘要（中文）

事件因果关系识别（ECI）旨在检测文本上下文中事件之间的因果关系。现有的ECI模型主要依赖监督方法，受限于大规模标注数据的需求。尽管大型语言模型（LLMs）支持零样本ECI，但容易产生因果幻觉，错误地建立虚假的因果联系。为了解决这些挑战，本文提出了MEFA，一个基于多源证据模糊聚合的零样本框架。该框架将因果推理分解为三个主要任务，并通过精心设计的提示引导LLMs生成不确定和确定的响应。实验结果表明，MEFA在F1-score上比第二好的无监督基线提高了6.2%，在精确度上提高了9.3%，同时显著减少了因果幻觉引发的错误。

## 🔬 方法详解

**问题定义**：本文旨在解决事件因果关系识别中的数据依赖问题，现有方法在缺乏标注数据时表现不佳，且容易产生因果幻觉。

**核心思路**：MEFA框架通过将因果推理分解为多个子任务，结合多源证据模糊聚合，旨在提高因果关系识别的准确性和可靠性。

**技术框架**：MEFA框架包括三个主要任务：时间性判断、必要性分析和充分性验证，并辅以三个辅助任务。通过设计的提示引导LLMs生成不确定和确定的响应，最后通过模糊聚合整合证据进行因果评分和判断。

**关键创新**：MEFA的创新在于其任务分解和模糊聚合方法，这与传统的监督学习方法形成鲜明对比，能够有效减少因果幻觉的发生。

**关键设计**：在设计中，使用了精心构建的提示来引导LLMs的输出，并通过量化子任务的响应来实现模糊聚合，确保因果关系的准确评分。实验中还优化了模型的参数设置和损失函数，以提升整体性能。

## 📊 实验亮点

实验结果表明，MEFA在三个基准测试中均表现优异，F1-score提升6.2%，精确度提升9.3%，同时显著减少了因果幻觉引发的错误，验证了任务分解和模糊聚合的有效性。

## 🎯 应用场景

该研究在事件因果关系识别领域具有广泛的应用潜力，尤其在社交媒体分析、新闻报道和法律文本分析等场景中，能够帮助自动化识别事件之间的因果关系，从而提升信息处理的效率和准确性。未来，MEFA框架有望进一步推广到其他自然语言处理任务中，推动相关领域的发展。

## 📄 摘要（原文）

> Event Causality Identification (ECI) aims to detect causal relationships between events in textual contexts. Existing ECI models predominantly rely on supervised methodologies, suffering from dependence on large-scale annotated data. Although Large Language Models (LLMs) enable zero-shot ECI, they are prone to causal hallucination-erroneously establishing spurious causal links. To address these challenges, we propose MEFA, a novel zero-shot framework based on Multi-source Evidence Fuzzy Aggregation. First, we decompose causality reasoning into three main tasks (temporality determination, necessity analysis, and sufficiency verification) complemented by three auxiliary tasks. Second, leveraging meticulously designed prompts, we guide LLMs to generate uncertain responses and deterministic outputs. Finally, we quantify LLM's responses of sub-tasks and employ fuzzy aggregation to integrate these evidence for causality scoring and causality determination. Extensive experiments on three benchmarks demonstrate that MEFA outperforms second-best unsupervised baselines by 6.2% in F1-score and 9.3% in precision, while significantly reducing hallucination-induced errors. In-depth analysis verify the effectiveness of task decomposition and the superiority of fuzzy aggregation.

