---
layout: default
title: Generative Artificial Intelligence Extracts Structure-Function Relationships from Plants for New Materials
---

# Generative Artificial Intelligence Extracts Structure-Function Relationships from Plants for New Materials

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06591" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06591v1</a>
  <a href="https://arxiv.org/pdf/2508.06591.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06591v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06591v1', 'Generative Artificial Intelligence Extracts Structure-Function Relationships from Plants for New Materials')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rachel K. Luu, Jingyu Deng, Mohammed Shahrudin Ibrahim, Nam-Joon Cho, Ming Dao, Subra Suresh, Markus J. Buehler

**分类**: cs.LG, cond-mat.dis-nn, cond-mat.mtrl-sci, cond-mat.other, cs.AI, cs.CL

**发布日期**: 2025-08-08

---

## 💡 一句话要点

**提出生成性人工智能框架以提取植物结构-功能关系**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `生成性人工智能` `材料科学` `植物科学` `生物仿生` `结构-功能关系` `实验设计` `多学科交叉`

## 📋 核心要点

1. 现有方法在材料科学领域的应用受限，尤其是在多学科交叉的实验科学中，缺乏有效的知识整合与实验设计工具。
2. 论文提出了一种将生成性人工智能与植物科学等领域结合的框架，利用AI工具提取结构-属性关系并设计新材料。
3. 通过实际实验验证，成功制造出一种新型花粉基粘合剂，展示了AI辅助创意在材料设计中的实际应用潜力。

## 📝 摘要（中文）

大型语言模型（LLMs）通过新颖的知识检索和创意构思方法重塑了研究领域。然而，它们在材料科学等高度多学科领域的应用仍然有限。本文提出了一种首创框架，将生成性人工智能与植物科学、生物仿生学和材料工程等尚未连接的领域文献整合，以提取洞察并设计材料实验。我们聚焦于响应湿度的系统，如基于花粉的材料和广叶棕榈叶，这些材料表现出自激励和适应性能。通过一系列AI工具，包括微调模型（BioinspiredLLM）、增强检索生成（RAG）、代理系统和分层采样策略，我们提取结构-属性关系并将其转化为新型生物仿生材料。通过实际实施验证了我们的方法，LLM生成的程序、材料设计和机械预测在实验室中进行了测试，最终成功制造出一种具有可调形态和测量剪切强度的新型基于花粉的粘合剂，为未来植物衍生粘合剂设计奠定了基础。

## 🔬 方法详解

**问题定义**：本文旨在解决材料科学中知识整合不足的问题，现有方法无法有效利用植物科学等领域的知识来设计新材料。

**核心思路**：通过将生成性人工智能与多学科文献结合，提取植物的结构-功能关系，进而设计出新型材料。这样的设计能够促进不同领域知识的交叉应用。

**技术框架**：整体架构包括多个模块：首先是文献检索与知识提取，其次是生成性模型（BioinspiredLLM）进行结构-属性关系的提取，最后通过实验验证生成的材料设计。

**关键创新**：最重要的创新点在于将生成性AI与植物科学结合，形成了一个新的知识提取与材料设计的框架，突破了传统材料科学的局限。

**关键设计**：在技术细节上，采用了微调的生成模型、增强检索生成（RAG）策略，以及分层采样方法，以确保从单一查询中生成和评估大量假设。

## 📊 实验亮点

实验结果表明，LLM生成的材料设计和程序在实验室中得到了验证，成功制造出一种具有可调形态的新型花粉基粘合剂，其剪切强度经过测量，展示了显著的性能提升，为未来的材料设计提供了新的方向。

## 🎯 应用场景

该研究的潜在应用领域包括新型材料的设计与开发，尤其是在生物仿生材料和智能材料方面。通过有效整合不同学科的知识，未来可能推动植物衍生材料的广泛应用，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> Large language models (LLMs) have reshaped the research landscape by enabling new approaches to knowledge retrieval and creative ideation. Yet their application in discipline-specific experimental science, particularly in highly multi-disciplinary domains like materials science, remains limited. We present a first-of-its-kind framework that integrates generative AI with literature from hitherto-unconnected fields such as plant science, biomimetics, and materials engineering to extract insights and design experiments for materials. We focus on humidity-responsive systems such as pollen-based materials and Rhapis excelsa (broadleaf lady palm) leaves, which exhibit self-actuation and adaptive performance. Using a suite of AI tools, including a fine-tuned model (BioinspiredLLM), Retrieval-Augmented Generation (RAG), agentic systems, and a Hierarchical Sampling strategy, we extract structure-property relationships and translate them into new classes of bioinspired materials. Structured inference protocols generate and evaluate hundreds of hypotheses from a single query, surfacing novel and experimentally tractable ideas. We validate our approach through real-world implementation: LLM-generated procedures, materials designs, and mechanical predictions were tested in the laboratory, culminating in the fabrication of a novel pollen-based adhesive with tunable morphology and measured shear strength, establishing a foundation for future plant-derived adhesive design. This work demonstrates how AI-assisted ideation can drive real-world materials design and enable effective human-AI collaboration.

