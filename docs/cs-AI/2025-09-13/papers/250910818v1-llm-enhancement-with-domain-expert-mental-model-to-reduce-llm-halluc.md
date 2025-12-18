---
layout: default
title: LLM Enhancement with Domain Expert Mental Model to Reduce LLM Hallucination with Causal Prompt Engineering
---

# LLM Enhancement with Domain Expert Mental Model to Reduce LLM Hallucination with Causal Prompt Engineering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10818" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10818v1</a>
  <a href="https://arxiv.org/pdf/2509.10818.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10818v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10818v1', 'LLM Enhancement with Domain Expert Mental Model to Reduce LLM Hallucination with Causal Prompt Engineering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Boris Kovalerchuk, Brent D. Fegley

**分类**: cs.AI, cs.HC

**发布日期**: 2025-09-13

**备注**: 25 pages,4 figures, 2 tables

---

## 💡 一句话要点

**提出基于领域专家心智模型的因果提示工程，减少LLM幻觉**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `领域专家知识` `心智模型` `提示工程` `决策支持` `人机对话` `知识表示`

## 📋 核心要点

1. 现有LLM在决策支持中面临幻觉问题，源于训练数据缺失和无法有效利用领域专家知识。
2. 论文提出一种基于人机对话和单调函数优化的专家心智模型（EMM）构建方法，用于LLM提示工程。
3. 该方法通过结构化领域知识，生成更有效的提示，旨在减少LLM在决策任务中的幻觉现象。

## 📝 摘要（中文）

各种学科和领域都存在困难的决策问题。生成技术，特别是大型语言模型（LLM）的普及，激发了人们使用它们进行决策支持的兴趣。然而，LLM无法解决训练数据中的缺失问题，导致幻觉。检索增强生成（RAG）通过整合外部信息检索来增强LLM，减少幻觉并提高准确性。然而，RAG及相关方法只是部分解决方案，因为它们可能无法访问所有必要的来源或关键的缺失信息。即使是日常问题也常常挑战LLM的能力。提交包含上下文和示例的更长提示是解决知识差距的一种方法，但设计有效的提示并非易事，并且可能无法捕捉领域专家的复杂心智模型。对于缺少关键信息的任务，LLM是不够的，许多现有系统在可用文档中的表示也很差。本文探讨了LLM如何使决策更有效率，使用评估是否回应征集建议书的运行示例。我们提出了一种基于优化人机对话以及单调布尔和k值函数的技术，以发现计算上易于处理的个人专家心智模型（EMM）用于决策。我们的用于LLM提示工程的EMM算法有四个步骤：（1）因素识别，（2）因素的层次结构化，（3）生成广义专家心智模型规范，以及（4）从该规范生成详细的广义专家心智模型。

## 🔬 方法详解

**问题定义**：LLM在复杂决策问题中，由于训练数据不完整和缺乏领域知识，容易产生幻觉，导致决策质量下降。现有方法如RAG虽然能引入外部信息，但无法完全解决知识缺失和专家知识难以有效融入的问题。因此，如何利用领域专家的知识来指导LLM进行更准确的决策是一个关键问题。

**核心思路**：论文的核心思路是通过构建领域专家的心智模型（EMM），并将其转化为LLM可以理解和利用的提示信息，从而提高LLM在决策任务中的准确性和可靠性。这种方法旨在弥合LLM的知识差距，并使其能够更好地模拟专家的决策过程。

**技术框架**：该方法包含四个主要步骤：1) 因素识别：确定影响决策的关键因素；2) 因素的层次结构化：将因素组织成层次结构，反映它们之间的关系；3) 生成广义专家心智模型规范：基于因素和结构，生成EMM的规范；4) 生成详细的广义专家心智模型：从规范中生成具体的EMM，用于LLM提示工程。整个流程旨在将专家的隐性知识显性化，并转化为LLM可用的形式。

**关键创新**：该方法的关键创新在于将领域专家的心智模型显式地构建出来，并用于指导LLM的提示工程。与传统的提示工程方法相比，该方法更加结构化和系统化，能够更好地捕捉专家的决策逻辑和知识。此外，该方法还利用人机对话和单调函数优化技术，提高了EMM构建的效率和准确性。

**关键设计**：论文中提到的单调布尔和k值函数在EMM的构建过程中起着关键作用，用于表示因素之间的逻辑关系和影响程度。具体的技术细节，例如参数设置、损失函数等，在摘要中没有详细说明，属于未知信息。

## 📊 实验亮点

摘要中没有提供具体的实验结果和性能数据，因此无法总结实验亮点。具体的性能提升幅度、对比基线等信息未知。

## 🎯 应用场景

该研究成果可应用于各种需要专家知识的决策支持系统，例如风险评估、投资决策、医疗诊断等。通过将领域专家的知识融入LLM，可以提高决策的准确性和效率，并为用户提供更可靠的决策建议。未来，该方法有望扩展到更广泛的领域，并与其他技术相结合，构建更智能化的决策支持系统。

## 📄 摘要（原文）

> Difficult decision-making problems abound in various disciplines and domains. The proliferation of generative techniques, especially large language models (LLMs), has excited interest in using them for decision support. However, LLMs cannot yet resolve missingness in their training data, leading to hallucinations. Retrieval-Augmented Generation (RAG) enhances LLMs by incorporating external information retrieval, reducing hallucinations and improving accuracy. Yet, RAG and related methods are only partial solutions, as they may lack access to all necessary sources or key missing information. Even everyday issues often challenge LLMs' abilities. Submitting longer prompts with context and examples is one approach to address knowledge gaps, but designing effective prompts is non-trivial and may not capture complex mental models of domain experts. For tasks with missing critical information, LLMs are insufficient, as are many existing systems poorly represented in available documents. This paper explores how LLMs can make decision-making more efficient, using a running example of evaluating whether to respond to a call for proposals. We propose a technology based on optimized human-machine dialogue and monotone Boolean and k-valued functions to discover a computationally tractable personal expert mental model (EMM) of decision-making. Our EMM algorithm for LLM prompt engineering has four steps: (1) factor identification, (2) hierarchical structuring of factors, (3) generating a generalized expert mental model specification, and (4) generating a detailed generalized expert mental model from that specification.

