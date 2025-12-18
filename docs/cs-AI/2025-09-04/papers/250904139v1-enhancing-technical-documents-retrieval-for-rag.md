---
layout: default
title: Enhancing Technical Documents Retrieval for RAG
---

# Enhancing Technical Documents Retrieval for RAG

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04139" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04139v1</a>
  <a href="https://arxiv.org/pdf/2509.04139.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04139v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04139v1', 'Enhancing Technical Documents Retrieval for RAG')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Songjiang Lai, Tsun-Hin Cheung, Ka-Chun Fung, Kaiwen Xue, Kwan-Ho Lin, Yan-Ming Choi, Vincent Ng, Kin-Man Lam

**分类**: cs.IR, cs.AI

**发布日期**: 2025-09-04

---

## 💡 一句话要点

**Technical-Embeddings：增强RAG技术文档检索的框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `技术文档检索` `RAG` `查询扩展` `上下文摘要` `双编码器` `BERT` `软提示微调`

## 📋 核心要点

1. 现有技术文档检索方法难以有效理解和检索复杂的技术内容，用户意图捕捉不足。
2. Technical-Embeddings框架通过查询扩展、上下文摘要和软提示微调，提升技术文档的语义检索能力。
3. 在RAG-EDA和Rust-Docs-QA数据集上的实验表明，该方法在精度和召回率上显著优于基线模型。

## 📝 摘要（中文）

本文介绍了一种名为Technical-Embeddings的新框架，旨在优化技术文档中的语义检索，适用于硬件和软件开发。该方法利用大型语言模型（LLM）的能力，解决理解和检索复杂技术内容的挑战。首先，通过生成扩展表示来增强用户查询，更好地捕捉用户意图并提高数据集多样性，从而丰富嵌入模型的微调过程。其次，应用摘要提取技术来编码关键的上下文信息，从而改进技术文档的表示。为了进一步提高检索性能，我们使用软提示微调了一个双编码器BERT模型，为查询和文档上下文合并单独的学习参数，以捕捉细粒度的语义细微差别。我们在两个公共数据集RAG-EDA和Rust-Docs-QA上评估了我们的方法，结果表明Technical-Embeddings在精度和召回率方面均显著优于基线模型。我们的研究结果突出了集成查询扩展和上下文摘要在增强技术领域信息访问和理解方面的有效性。这项工作推进了检索增强生成（RAG）系统的发展，为工程和产品开发工作流程中高效准确的技术文档检索提供了新的途径。

## 🔬 方法详解

**问题定义**：现有技术文档检索方法在理解复杂技术内容和捕捉用户意图方面存在不足，导致检索精度不高。尤其是在硬件和软件开发领域，技术文档往往包含大量专业术语和上下文信息，传统方法难以有效处理这些信息。

**核心思路**：论文的核心思路是通过增强用户查询和优化文档表示来提高检索性能。具体来说，通过查询扩展来丰富用户意图的表达，并通过上下文摘要来提取文档的关键信息。此外，使用软提示微调双编码器模型，使其能够更好地捕捉查询和文档之间的细粒度语义关系。

**技术框架**：Technical-Embeddings框架主要包含三个模块：1) 查询扩展模块，用于生成更丰富的查询表示；2) 文档摘要模块，用于提取文档的关键上下文信息；3) 微调的双编码器模型，用于计算查询和文档之间的相似度。整体流程是，首先对用户查询进行扩展，然后对技术文档进行摘要提取，最后使用微调的双编码器模型计算扩展后的查询和摘要后的文档之间的相似度，并返回相似度最高的文档。

**关键创新**：该论文的关键创新在于将查询扩展和上下文摘要相结合，并使用软提示微调双编码器模型。与传统的检索方法相比，该方法能够更好地捕捉用户意图和文档的关键信息，从而提高检索精度。此外，软提示微调允许模型学习查询和文档之间更细粒度的语义关系。

**关键设计**：在查询扩展模块中，使用了大型语言模型（LLM）生成查询的扩展表示。在文档摘要模块中，使用了摘要提取技术来提取文档的关键上下文信息。在微调双编码器模型时，使用了软提示技术，并为查询和文档上下文合并单独的学习参数。损失函数使用了对比学习损失，目标是使相似的查询和文档在嵌入空间中更接近，而不相似的查询和文档更远离。

## 📊 实验亮点

实验结果表明，Technical-Embeddings在RAG-EDA和Rust-Docs-QA两个数据集上均显著优于基线模型。具体来说，在精度和召回率方面均取得了明显的提升，证明了该方法在技术文档检索方面的有效性。例如，在RAG-EDA数据集上，该方法的精度提升了X%，召回率提升了Y%（具体数据未知）。

## 🎯 应用场景

该研究成果可应用于各种需要技术文档检索的场景，例如软件开发、硬件设计、产品维护等。通过提高技术文档检索的效率和准确性，可以帮助工程师和开发人员更快地找到所需信息，从而提高工作效率和产品质量。未来，该方法可以进一步扩展到其他领域，例如法律、医学等。

## 📄 摘要（原文）

> In this paper, we introduce Technical-Embeddings, a novel framework designed to optimize semantic retrieval in technical documentation, with applications in both hardware and software development. Our approach addresses the challenges of understanding and retrieving complex technical content by leveraging the capabilities of Large Language Models (LLMs). First, we enhance user queries by generating expanded representations that better capture user intent and improve dataset diversity, thereby enriching the fine-tuning process for embedding models. Second, we apply summary extraction techniques to encode essential contextual information, refining the representation of technical documents. To further enhance retrieval performance, we fine-tune a bi-encoder BERT model using soft prompting, incorporating separate learning parameters for queries and document context to capture fine-grained semantic nuances. We evaluate our approach on two public datasets, RAG-EDA and Rust-Docs-QA, demonstrating that Technical-Embeddings significantly outperforms baseline models in both precision and recall. Our findings highlight the effectiveness of integrating query expansion and contextual summarization to enhance information access and comprehension in technical domains. This work advances the state of Retrieval-Augmented Generation (RAG) systems, offering new avenues for efficient and accurate technical document retrieval in engineering and product development workflows.

