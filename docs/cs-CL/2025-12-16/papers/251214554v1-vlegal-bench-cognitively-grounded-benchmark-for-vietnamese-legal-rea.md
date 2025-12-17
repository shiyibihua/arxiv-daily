---
layout: default
title: VLegal-Bench: Cognitively Grounded Benchmark for Vietnamese Legal Reasoning of Large Language Models
---

# VLegal-Bench: Cognitively Grounded Benchmark for Vietnamese Legal Reasoning of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14554" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14554v1</a>
  <a href="https://arxiv.org/pdf/2512.14554.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14554v1" onclick="toggleFavorite(this, '2512.14554v1', 'VLegal-Bench: Cognitively Grounded Benchmark for Vietnamese Legal Reasoning of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nguyen Tien Dong, Minh-Anh Nguyen, Thanh Dat Hoang, Nguyen Tuan Ngoc, Dao Xuan Quang Minh, Phan Phi Hai, Nguyen Thi Ngoc Anh, Dang Van Tu, Binh Vu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出VLegal-Bench，用于评估LLM在越南法律推理任务中的能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `越南法律` `大型语言模型` `法律推理` `基准数据集` `认知评估`

## 📋 核心要点

1. 现有方法难以评估LLM在复杂、层级化且频繁修订的越南法律环境中的推理能力。
2. VLegal-Bench通过模拟实际法律场景，从认知角度系统评估LLM对越南法律的理解和应用。
3. VLegal-Bench包含10,450个样本，覆盖多种法律任务，为LLM在越南法律领域的应用提供基准。

## 📝 摘要（中文）

大型语言模型（LLM）的快速发展为人工智能在法律领域的应用带来了新的可能性。然而，越南法律的复杂性、层级结构和频繁修订对评估这些模型解释和利用法律知识的能力提出了巨大挑战。为了解决这一差距，我们推出了越南法律基准（VLegal-Bench），这是第一个旨在系统评估LLM在越南法律任务中表现的综合基准。VLegal-Bench以Bloom的认知分类学为基础，通过反映实际使用场景的任务，涵盖了多个层次的法律理解。该基准包含10,450个样本，这些样本通过严格的标注流程生成，法律专家使用我们的标注系统对每个实例进行标注和交叉验证，以确保每个样本都基于权威的法律文件，并反映了真实的法律助理工作流程，包括一般法律问答、检索增强生成、多步骤推理和针对越南法律的基于场景的问题解决。通过提供一个标准化、透明和认知驱动的评估框架，VLegal-Bench为评估LLM在越南法律环境中的性能奠定了坚实的基础，并支持开发更可靠、可解释和符合伦理的人工智能辅助法律系统。

## 🔬 方法详解

**问题定义**：论文旨在解决现有方法在评估大型语言模型（LLM）在越南法律领域的推理能力方面的不足。越南法律体系复杂，层级结构明显，且修订频繁，这使得现有的通用LLM评估方法难以准确衡量模型对越南法律的理解和应用能力。现有方法缺乏针对越南法律特点的基准数据集和评估框架，无法有效评估LLM在实际法律场景中的表现。

**核心思路**：论文的核心思路是构建一个专门针对越南法律的综合性基准数据集VLegal-Bench，并设计相应的评估框架。该基准数据集的设计受到Bloom认知分类学的启发，旨在从多个认知层次评估LLM的法律理解能力。通过模拟实际的法律助理工作流程，VLegal-Bench能够更真实地反映LLM在实际应用中的表现。

**技术框架**：VLegal-Bench的构建流程主要包括以下几个阶段：1）法律专家团队根据Bloom认知分类学设计不同层次的法律任务，包括一般法律问答、检索增强生成、多步骤推理和基于场景的问题解决；2）法律专家使用专门的标注系统对每个实例进行标注和交叉验证，确保每个样本都基于权威的法律文件；3）构建包含10,450个样本的VLegal-Bench数据集；4）使用VLegal-Bench评估LLM在不同法律任务上的表现。

**关键创新**：VLegal-Bench的主要创新点在于：1）它是第一个专门针对越南法律的综合性基准数据集，填补了该领域的空白；2）它基于Bloom认知分类学设计，能够从多个认知层次评估LLM的法律理解能力；3）它模拟实际的法律助理工作流程，能够更真实地反映LLM在实际应用中的表现。与现有方法相比，VLegal-Bench更具针对性和实用性。

**关键设计**：VLegal-Bench的关键设计包括：1）样本的多样性：涵盖了不同类型的法律问题和任务，以全面评估LLM的法律理解能力；2）标注的准确性：由法律专家进行标注和交叉验证，确保每个样本都基于权威的法律文件；3）评估的全面性：从多个认知层次评估LLM的法律理解能力，包括记忆、理解、应用、分析、评估和创造。

## 📊 实验亮点

VLegal-Bench包含10,450个样本，覆盖多种法律任务，并通过法律专家的严格标注和交叉验证，保证了数据的质量和可靠性。该基准数据集为评估LLM在越南法律领域的性能提供了一个标准化的平台，并为未来的研究奠定了基础。具体性能数据和对比基线将在后续研究中公布。

## 🎯 应用场景

VLegal-Bench可用于评估和提升LLM在越南法律领域的应用能力，例如智能法律咨询、法律文书生成、案件分析等。该基准数据集能够促进开发更可靠、可解释和符合伦理的人工智能辅助法律系统，提高法律服务的效率和质量，并为法律从业者提供更强大的工具。

## 📄 摘要（原文）

> The rapid advancement of large language models (LLMs) has enabled new possibilities for applying artificial intelligence within the legal domain. Nonetheless, the complexity, hierarchical organization, and frequent revisions of Vietnamese legislation pose considerable challenges for evaluating how well these models interpret and utilize legal knowledge. To address this gap, Vietnamese Legal Benchmark (VLegal-Bench) is introduced, the first comprehensive benchmark designed to systematically assess LLMs on Vietnamese legal tasks. Informed by Bloom's cognitive taxonomy, VLegal-Bench encompasses multiple levels of legal understanding through tasks designed to reflect practical usage scenarios. The benchmark comprises 10,450 samples generated through a rigorous annotation pipeline, where legal experts label and cross-validate each instance using our annotation system to ensure every sample is grounded in authoritative legal documents and mirrors real-world legal assistant workflows, including general legal questions and answers, retrieval-augmented generation, multi-step reasoning, and scenario-based problem solving tailored to Vietnamese law. By providing a standardized, transparent, and cognitively informed evaluation framework, VLegal-Bench establishes a solid foundation for assessing LLM performance in Vietnamese legal contexts and supports the development of more reliable, interpretable, and ethically aligned AI-assisted legal systems.

