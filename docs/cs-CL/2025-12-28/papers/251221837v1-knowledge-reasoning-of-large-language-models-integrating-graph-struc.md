---
layout: default
title: Knowledge Reasoning of Large Language Models Integrating Graph-Structured Information for Pest and Disease Control in Tobacco
---

# Knowledge Reasoning of Large Language Models Integrating Graph-Structured Information for Pest and Disease Control in Tobacco

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21837" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21837v1</a>
  <a href="https://arxiv.org/pdf/2512.21837.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21837v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21837v1', 'Knowledge Reasoning of Large Language Models Integrating Graph-Structured Information for Pest and Disease Control in Tobacco')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siyu Li, Chenwei Song, Wan Zhou, Xinyi Liu

**分类**: cs.CL

**发布日期**: 2025-12-26

---

## 💡 一句话要点

**提出GraphRAG框架，融合图结构信息增强大型语言模型在烟草病虫害防治中的知识推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `知识推理` `知识图谱` `图神经网络` `烟草病虫害防治`

## 📋 核心要点

1. 现有方法在烟草病虫害防治知识推理方面，缺乏对领域知识的有效利用和结构化信息的整合。
2. 论文提出GraphRAG框架，将领域知识图谱融入LLM，提升知识检索和推理的准确性。
3. 实验结果表明，该方法在多项指标上优于基线，显著提升了复杂推理场景下的性能。

## 📝 摘要（中文）

本文提出了一种融合图结构信息的大型语言模型（LLM）方法，用于烟草病虫害防治中的知识推理。该方法构建于GraphRAG框架之上，通过显式地整合领域特定知识图谱中的结构化信息，增强知识检索和推理能力。具体而言，首先利用LLM辅助构建烟草病虫害知识图谱，该图谱组织了疾病、症状、防治方法及其关系等关键实体。基于该图谱，检索相关知识并将其整合到推理过程中，以支持准确的答案生成。Transformer架构被用作核心推理模型，而图神经网络（GNN）用于学习富有表现力的节点表示，从而捕获知识图谱中的局部和全局关系信息。基于ChatGLM的模型作为主干LLM，并使用LoRA进行微调，以实现参数高效的适应。大量实验结果表明，所提出的方法在多个评估指标上始终优于基线方法，显著提高了推理的准确性和深度，尤其是在复杂的多跳和比较推理场景中。

## 🔬 方法详解

**问题定义**：论文旨在解决烟草病虫害防治领域中，大型语言模型在知识推理方面面临的挑战。现有方法难以有效利用领域知识，特别是结构化的知识图谱信息，导致推理准确性和深度不足，尤其是在复杂的多跳推理和比较推理场景下。

**核心思路**：论文的核心思路是将领域知识图谱融入到大型语言模型的推理过程中。通过构建烟草病虫害知识图谱，并利用图神经网络学习节点表示，从而使模型能够更好地理解和利用结构化信息，提高推理的准确性和深度。

**技术框架**：整体框架基于GraphRAG，包含以下主要模块：1) 知识图谱构建模块，利用LLM辅助构建烟草病虫害知识图谱；2) 知识检索模块，基于知识图谱检索相关知识；3) 推理模块，采用Transformer架构进行推理，并融合图神经网络学习到的节点表示；4) 微调模块，使用LoRA对ChatGLM进行参数高效的微调。

**关键创新**：最重要的技术创新点在于将图结构信息显式地融入到大型语言模型的知识推理过程中。通过图神经网络学习节点表示，使模型能够捕获知识图谱中的局部和全局关系信息，从而提高推理的准确性和深度。与现有方法相比，该方法更有效地利用了领域知识，并能够处理更复杂的推理任务。

**关键设计**：论文采用Transformer作为核心推理模型，GNN用于学习节点表示。ChatGLM作为backbone LLM，并使用LoRA进行微调，以减少计算开销。知识图谱的构建和维护是关键，需要仔细设计实体和关系类型。损失函数的设计需要考虑知识图谱的结构信息，例如可以使用图注意力机制来学习节点的重要性。

## 📊 实验亮点

实验结果表明，所提出的方法在多个评估指标上始终优于基线方法，显著提高了推理的准确性和深度。尤其是在复杂的多跳和比较推理场景中，性能提升更为明显。具体数据未在摘要中给出，但强调了在复杂推理场景下的显著优势。

## 🎯 应用场景

该研究成果可应用于智能农业领域，为烟草种植者提供病虫害防治的决策支持。通过整合领域知识和推理能力，可以帮助用户快速准确地诊断病虫害，并推荐合适的防治方法。未来，该方法可扩展到其他农业领域，提高农业生产效率和质量。

## 📄 摘要（原文）

> This paper proposes a large language model (LLM) approach that integrates graph-structured information for knowledge reasoning in tobacco pest and disease control. Built upon the GraphRAG framework, the proposed method enhances knowledge retrieval and reasoning by explicitly incorporating structured information from a domain-specific knowledge graph. Specifically, LLMs are first leveraged to assist in the construction of a tobacco pest and disease knowledge graph, which organizes key entities such as diseases, symptoms, control methods, and their relationships. Based on this graph, relevant knowledge is retrieved and integrated into the reasoning process to support accurate answer generation. The Transformer architecture is adopted as the core inference model, while a graph neural network (GNN) is employed to learn expressive node representations that capture both local and global relational information within the knowledge graph. A ChatGLM-based model serves as the backbone LLM and is fine-tuned using LoRA to achieve parameter-efficient adaptation. Extensive experimental results demonstrate that the proposed approach consistently outperforms baseline methods across multiple evaluation metrics, significantly improving both the accuracy and depth of reasoning, particularly in complex multi-hop and comparative reasoning scenarios.

