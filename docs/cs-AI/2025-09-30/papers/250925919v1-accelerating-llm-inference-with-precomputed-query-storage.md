---
layout: default
title: Accelerating LLM Inference with Precomputed Query Storage
---

# Accelerating LLM Inference with Precomputed Query Storage

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25919" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25919v1</a>
  <a href="https://arxiv.org/pdf/2509.25919.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25919v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25919v1', 'Accelerating LLM Inference with Precomputed Query Storage')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jay H. Park, Youngju Cho, Choungsol Lee, Moonwook Oh, Euiseong Seo

**分类**: cs.DC, cs.AI

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**StorInfer：利用预计算查询存储加速LLM推理，尤其适用于资源受限环境**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM推理加速` `预计算` `存储辅助推理` `向量数据库` `低延迟` `资源受限环境` `自适应查询生成`

## 📋 核心要点

1. LLM推理在资源受限设备上延迟高昂，传统方法依赖昂贵的GPU计算。
2. StorInfer预计算并存储查询-响应对，通过语义匹配直接返回结果，避免实时推理。
3. 实验表明，StorInfer在保证质量的前提下，显著降低了推理延迟，提升了效率。

## 📝 摘要（中文）

大型语言模型（LLM）推理通常面临高延迟问题，尤其是在设备端或边缘部署等资源受限环境中。为了解决这一挑战，我们提出了StorInfer，一种新颖的存储辅助LLM推理系统，通过离线预计算和存储可预测的查询-响应对来加速响应时间。当用户查询在语义上与预计算查询匹配时，StorInfer绕过昂贵的GPU推理，立即返回存储的响应，从而显著降低延迟和计算成本。为了最大化覆盖率和有效性，StorInfer采用LLM驱动的生成器，该生成器基于给定的知识库自适应地生成多样化和去重的查询。这通过两种技术实现：自适应查询掩码，防止重新生成相似查询；自适应采样，动态调整生成参数以促进语义多样性。生成的查询-响应对被嵌入并使用磁盘支持的向量数据库进行索引，以实现运行时快速的基于相似性的检索。使用这种方法，我们生成了15万个独特的预计算对（占用高达830 MB的存储空间），实现了高达17.3%的延迟降低，且不损失响应质量。我们在多个QA数据集上的评估证明了存储辅助推理的实用性和可扩展性，尤其是在具有可预测查询分布的场景中。StorInfer突出了利用存储作为高效、低延迟LLM部署的主要推动因素的有希望的方向。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在资源受限设备上推理延迟高的问题。现有方法依赖于实时计算，计算量大，延迟高，难以满足实时性要求。尤其是在查询分布相对固定的场景下，重复计算造成了资源浪费。

**核心思路**：论文的核心思路是利用预计算和存储来加速LLM推理。通过离线预先计算并存储常见的查询及其对应的响应，在推理时，直接检索预计算结果，避免重复计算，从而降低延迟和计算成本。这种方法尤其适用于查询分布相对固定的场景。

**技术框架**：StorInfer系统包含离线预计算和在线推理两个主要阶段。离线预计算阶段，利用LLM驱动的生成器，基于知识库生成多样化的查询，并计算对应的响应，将查询-响应对存储在向量数据库中。在线推理阶段，接收用户查询，通过向量数据库检索相似的预计算查询，如果匹配成功，则直接返回预计算的响应，否则进行实时推理。

**关键创新**：StorInfer的关键创新在于利用LLM驱动的生成器自适应地生成多样化和去重的查询，以及使用向量数据库进行快速相似性检索。自适应查询掩码防止生成相似查询，自适应采样动态调整生成参数以促进语义多样性。

**关键设计**：在查询生成阶段，采用了自适应查询掩码和自适应采样两种技术。自适应查询掩码通过记录已生成的查询，避免重复生成相似查询。自适应采样通过动态调整生成参数（如temperature），控制生成查询的多样性。向量数据库采用磁盘存储，以支持大规模的查询-响应对存储。

## 📊 实验亮点

实验结果表明，StorInfer在多个QA数据集上实现了显著的延迟降低，最高可达17.3%，且不损失响应质量。通过生成15万个独特的预计算对，占用830MB存储空间，证明了该方法在实际应用中的可行性和有效性。该方法尤其适用于具有可预测查询分布的场景。

## 🎯 应用场景

StorInfer适用于资源受限的边缘设备和移动设备上的LLM应用，例如智能客服、智能家居、车载助手等。通过降低推理延迟和计算成本，可以提升用户体验，并降低部署成本。未来，该方法可以扩展到更广泛的LLM应用场景，例如文档检索、知识问答等。

## 📄 摘要（原文）

> Large language model (LLM) inference often suffers from high latency, particularly in resource-constrained environments such as on-device or edge deployments. To address this challenge, we present StorInfer, a novel storage-assisted LLM inference system that accelerates response time by precomputing and storing predictable query-response pairs offline. When a user query semantically matches a precomputed query, StorInfer bypasses expensive GPU inference and instantly returns the stored response, significantly reducing latency and compute costs. To maximize coverage and effectiveness, StorInfer employs an LLM-driven generator that adaptively produces diverse and deduplicated queries based on a given knowledge base. This is achieved via two techniques: adaptive query masking, which prevents regeneration of similar queries, and adaptive sampling, which dynamically tunes generation parameters to promote semantic diversity. The resulting query-response pairs are embedded and indexed using a disk-backed vector database to enable fast, similarity-based retrieval at runtime. Using this approach, we generated 150K unique precomputed pairs (taking up to 830 MB of storage space), achieving up to 17.3% latency reduction with no loss in response quality. Our evaluation across multiple QA datasets demonstrates the practicality and scalability of storage-assisted inference, especially in scenarios with predictable query distributions. StorInfer highlights a promising direction in leveraging storage as a primary enabler for efficient, low-latency LLM deployment.

