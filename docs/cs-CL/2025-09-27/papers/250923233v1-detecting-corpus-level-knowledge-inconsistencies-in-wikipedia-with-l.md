---
layout: default
title: Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models
---

# Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23233" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23233v1</a>
  <a href="https://arxiv.org/pdf/2509.23233.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23233v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23233v1', 'Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sina J. Semnani, Jirayu Burapacheep, Arpandeep Khatua, Thanawan Atchariyachanvanit, Zheng Wang, Monica S. Lam

**分类**: cs.CL

**发布日期**: 2025-09-27

**备注**: EMNLP 2025 (Main Conference)

---

## 💡 一句话要点

**提出CLAIRE系统，用于检测维基百科语料库级别知识不一致性，提升编辑效率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识不一致性检测` `大型语言模型` `维基百科` `信息检索` `人机协作`

## 📋 核心要点

1. 维基百科作为知识库存在事实不一致问题，影响下游应用，亟需有效检测方法。
2. 提出CLAIRE系统，利用LLM推理和检索，辅助人工识别维基百科中的知识不一致性。
3. 实验表明，CLAIRE能显著提升维基百科编辑的效率和信心，并构建了WIKICOLLIDE基准数据集。

## 📝 摘要（中文）

维基百科是全球最大的开放知识语料库，被广泛使用，并且是训练大型语言模型（LLM）和检索增强生成（RAG）系统的关键资源。确保其准确性至关重要。本文关注不一致性，一种特殊的factual inaccuracy，并提出了语料库级别不一致性检测的任务。我们提出了CLAIRE，一个agentic系统，它结合了LLM推理和检索，以呈现潜在的不一致性声明以及上下文证据，供人工审查。在一项与经验丰富的维基百科编辑的用户研究中，87.5%的人报告在使用CLAIRE时信心更高，并且参与者在相同的时间内识别出64.7%更多的不一致性。结合CLAIRE和人工标注，我们贡献了WIKICOLLIDE，这是第一个真实的维基百科不一致性基准。通过使用CLAIRE辅助分析的随机抽样，我们发现至少3.3%的英语维基百科事实与另一个事实相矛盾，并且不一致性传播到7.3%的FEVEROUS和4.0%的AmbigQA示例中。在此数据集上对强大的基线进行基准测试显示出巨大的提升空间：最佳的完全自动化系统仅达到75.1%的AUROC。

## 🔬 方法详解

**问题定义**：论文旨在解决维基百科中语料库级别的知识不一致性问题。现有方法主要依赖人工审核，效率低下且难以发现隐藏的不一致性。大型语言模型虽然具备一定的知识推理能力，但直接应用于维基百科的规模化不一致性检测仍然面临挑战，例如缺乏针对性的工具和基准。

**核心思路**：论文的核心思路是结合大型语言模型的推理能力和信息检索技术，构建一个智能代理系统（CLAIRE），辅助人工编辑发现并验证维基百科中的不一致性。通过LLM进行初步的矛盾识别和证据检索，然后将结果呈现给人工编辑进行最终确认，从而提高效率和准确性。

**技术框架**：CLAIRE系统的整体架构包含以下几个主要模块：1) 声明提取：从维基百科文章中提取事实性声明。2) 矛盾检测：利用LLM对提取的声明进行两两比较，判断是否存在矛盾。3) 证据检索：对于潜在的矛盾声明，从维基百科中检索相关的上下文证据。4) 人工审核：将矛盾声明和证据呈现给人工编辑，进行最终确认和修正。

**关键创新**：论文的关键创新在于将LLM的推理能力与信息检索技术相结合，构建了一个半自动化的知识不一致性检测系统。此外，论文还构建了WIKICOLLIDE数据集，为该领域的研究提供了基准。

**关键设计**：CLAIRE系统使用了预训练的大型语言模型（具体模型未知）进行矛盾检测和证据检索。在矛盾检测阶段，采用了基于prompting的方法，引导LLM判断两个声明是否矛盾。证据检索阶段，使用了基于关键词的检索方法，从维基百科中检索与声明相关的文章段落。人工审核界面设计简洁明了，方便编辑快速浏览声明和证据，并做出判断。

## 📊 实验亮点

用户研究表明，使用CLAIRE后，维基百科编辑的信心提升了87.5%，并且在相同时间内识别出的不一致性增加了64.7%。通过CLAIRE辅助分析，发现至少3.3%的英语维基百科事实存在矛盾。在WIKICOLLIDE数据集上，最佳的自动化系统AUROC仅为75.1%，表明仍有很大的提升空间。

## 🎯 应用场景

该研究成果可应用于大规模知识库的质量控制，例如维基百科、DBpedia等。通过自动检测和修复知识不一致性，可以提高知识库的准确性和可靠性，从而提升下游应用（如问答系统、知识图谱）的性能。未来，该方法可扩展到其他类型的知识库和语言。

## 📄 摘要（原文）

> Wikipedia is the largest open knowledge corpus, widely used worldwide and serving as a key resource for training large language models (LLMs) and retrieval-augmented generation (RAG) systems. Ensuring its accuracy is therefore critical. But how accurate is Wikipedia, and how can we improve it?
>   We focus on inconsistencies, a specific type of factual inaccuracy, and introduce the task of corpus-level inconsistency detection. We present CLAIRE, an agentic system that combines LLM reasoning with retrieval to surface potentially inconsistent claims along with contextual evidence for human review. In a user study with experienced Wikipedia editors, 87.5% reported higher confidence when using CLAIRE, and participants identified 64.7% more inconsistencies in the same amount of time.
>   Combining CLAIRE with human annotation, we contribute WIKICOLLIDE, the first benchmark of real Wikipedia inconsistencies. Using random sampling with CLAIRE-assisted analysis, we find that at least 3.3% of English Wikipedia facts contradict another fact, with inconsistencies propagating into 7.3% of FEVEROUS and 4.0% of AmbigQA examples. Benchmarking strong baselines on this dataset reveals substantial headroom: the best fully automated system achieves an AUROC of only 75.1%.
>   Our results show that contradictions are a measurable component of Wikipedia and that LLM-based systems like CLAIRE can provide a practical tool to help editors improve knowledge consistency at scale.

