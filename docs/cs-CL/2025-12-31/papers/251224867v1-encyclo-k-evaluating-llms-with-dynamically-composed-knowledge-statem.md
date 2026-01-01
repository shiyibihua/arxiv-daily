---
layout: default
title: "Encyclo-K: Evaluating LLMs with Dynamically Composed Knowledge Statements"
---

# Encyclo-K: Evaluating LLMs with Dynamically Composed Knowledge Statements

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24867" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24867v1</a>
  <a href="https://arxiv.org/pdf/2512.24867.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24867v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24867v1', 'Encyclo-K: Evaluating LLMs with Dynamically Composed Knowledge Statements')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiming Liang, Yizhi Li, Yantao Du, Ge Zhang, Jiayi Zhou, Yuchen Wu, Yinzhu Piao, Denghui Cao, Tong Sun, Ziniu Li, Li Du, Bo Lei, Jiaheng Liu, Chenghua Lin, Zhaoxiang Zhang, Wenhao Huang, Jiajun Zhang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-31

---

## 💡 一句话要点

**提出Encyclo-K，通过动态组合知识语句评估LLM的综合理解能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `基准测试` `知识评估` `动态评估` `综合理解` `知识语句` `数据污染`

## 📋 核心要点

1. 现有LLM基准测试易受数据污染，评估范围局限于单知识点，且依赖昂贵的专家标注。
2. Encyclo-K以知识语句为单位构建基准，动态组合成问题，避免记忆，实现多知识点评估。
3. 实验表明，即使是顶尖LLM在Encyclo-K上表现仍有提升空间，验证了其挑战性和区分度。

## 📝 摘要（中文）

基准测试在追踪大型语言模型（LLMs）的快速发展和识别其能力边界方面起着至关重要的作用。然而，现有的基准测试主要在问题层面策划问题，存在三个根本性的局限性：容易受到数据污染、限制于单知识点评估以及依赖于昂贵的领域专家标注。我们提出了Encyclo-K，这是一个基于语句的基准测试，从根本上重新思考了基准测试的构建。我们的关键见解是，知识语句，而不是问题，可以作为策划的单元，然后可以从中构建问题。我们从权威教科书中提取独立的知识语句，并通过在测试时随机抽样将它们动态地组合成评估问题。这种设计直接解决了所有三个局限性：组合空间太大而无法记忆，并且模型排名在动态生成的问题集中保持稳定，从而能够可靠地定期刷新数据集；每个问题聚合8-10个语句以进行全面的多知识评估；注释者仅验证格式合规性，而无需领域专业知识，从而大大降低了注释成本。对50多个LLM的实验表明，Encyclo-K提出了巨大的挑战，并具有很强的区分能力。即使是表现最佳的OpenAI-GPT-5.1也仅达到62.07％的准确率，并且模型性能显示出清晰的梯度分布-推理模型的范围从16.04％到62.07％，而聊天模型的范围从9.71％到50.40％。这些结果验证了动态评估和多语句综合理解所带来的挑战。这些发现将Encyclo-K确立为一个可扩展的框架，用于动态评估LLM对多个细粒度学科知识语句的综合理解。

## 🔬 方法详解

**问题定义**：现有LLM基准测试主要存在三个问题：一是容易受到数据污染，模型可能已经见过或学习过测试数据；二是评估通常只针对单个知识点，无法考察模型综合运用知识的能力；三是依赖于领域专家进行标注，成本高昂且难以扩展。这些问题限制了对LLM能力的全面和可靠评估。

**核心思路**：Encyclo-K的核心思路是将知识语句作为基准测试的基本单元，而不是直接使用问题。通过从权威教科书中提取独立的知识语句，并在测试时动态地将这些语句组合成问题，可以创建一个巨大的问题空间，从而降低数据污染的风险。同时，每个问题包含多个知识语句，可以更全面地评估模型的综合理解能力。此外，标注者只需要验证语句的格式合规性，无需领域专业知识，大大降低了标注成本。

**技术框架**：Encyclo-K的整体框架包括以下几个主要步骤：1. **知识语句提取**：从权威教科书中提取独立的、可验证的知识语句。2. **问题生成**：在测试时，随机抽取8-10个知识语句，将它们组合成一个问题。3. **模型评估**：将生成的问题输入到LLM中，评估其回答的准确性。4. **性能分析**：分析LLM在不同知识领域和不同难度级别的问题上的表现。

**关键创新**：Encyclo-K的关键创新在于其动态组合知识语句的评估方法。与传统的静态基准测试相比，Encyclo-K可以生成几乎无限数量的问题，从而大大降低了数据污染的风险。此外，通过组合多个知识语句，Encyclo-K可以更全面地评估模型的综合理解能力。

**关键设计**：在知识语句提取方面，论文强调从权威教科书中提取，以保证知识的准确性和可靠性。在问题生成方面，论文采用随机抽样的方法，以保证问题的多样性和随机性。在模型评估方面，论文采用准确率作为评估指标，并对不同知识领域和不同难度级别的问题进行细致的分析。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24867v1/figures/DynamicGPQA_pipeline.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24867v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24867v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，即使是顶尖的LLM，如OpenAI-GPT-5.1，在Encyclo-K上的准确率也仅为62.07%，表明该基准测试具有很强的挑战性。同时，不同模型的性能表现出明显的梯度分布，验证了Encyclo-K的区分能力，能够有效区分不同LLM的综合理解能力。

## 🎯 应用场景

Encyclo-K可用于全面评估LLM在各个学科领域的知识掌握程度和综合理解能力，帮助开发者改进模型性能。此外，该方法可应用于教育领域，辅助学生学习和知识巩固，或用于构建智能问答系统，提供更准确和全面的答案。

## 📄 摘要（原文）

> Benchmarks play a crucial role in tracking the rapid advancement of large language models (LLMs) and identifying their capability boundaries. However, existing benchmarks predominantly curate questions at the question level, suffering from three fundamental limitations: vulnerability to data contamination, restriction to single-knowledge-point assessment, and reliance on costly domain expert annotation. We propose Encyclo-K, a statement-based benchmark that rethinks benchmark construction from the ground up. Our key insight is that knowledge statements, not questions, can serve as the unit of curation, and questions can then be constructed from them. We extract standalone knowledge statements from authoritative textbooks and dynamically compose them into evaluation questions through random sampling at test time. This design directly addresses all three limitations: the combinatorial space is too vast to memorize, and model rankings remain stable across dynamically generated question sets, enabling reliable periodic dataset refresh; each question aggregates 8-10 statements for comprehensive multi-knowledge assessment; annotators only verify formatting compliance without requiring domain expertise, substantially reducing annotation costs. Experiments on over 50 LLMs demonstrate that Encyclo-K poses substantial challenges with strong discriminative power. Even the top-performing OpenAI-GPT-5.1 achieves only 62.07% accuracy, and model performance displays a clear gradient distribution--reasoning models span from 16.04% to 62.07%, while chat models range from 9.71% to 50.40%. These results validate the challenges introduced by dynamic evaluation and multi-statement comprehensive understanding. These findings establish Encyclo-K as a scalable framework for dynamic evaluation of LLMs' comprehensive understanding over multiple fine-grained disciplinary knowledge statements.

