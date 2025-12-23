---
layout: default
title: Evaluation of LLM-based Strategies for the Extraction of Food Product Information from Online Shops
---

# Evaluation of LLM-based Strategies for the Extraction of Food Product Information from Online Shops

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21585" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21585v1</a>
  <a href="https://arxiv.org/pdf/2506.21585.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21585v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21585v1', 'Evaluation of LLM-based Strategies for the Extraction of Food Product Information from Online Shops')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Christoph Brosch, Sian Brumm, Rolf Krieger, Jonas Scheffler

**分类**: cs.CL, cs.IR, cs.LG

**发布日期**: 2025-06-17

**备注**: Preprint for paper presented at DATA 2025 in Bilbao, Spain. Corrected -2.27 to -1.61 in abstract and +2.27 to +1.61 in discussion. Reference to journal and publication will follow

**期刊**: In Proceedings of the 14th International Conference on Data Science, Technology and Applications, 2025, ISBN 978-989-758-758-0, ISSN 2184-285X, pages 709-715

**DOI**: [10.5220/0013647300003967](https://doi.org/10.5220/0013647300003967)

---

## 💡 一句话要点

**提出基于LLM的间接提取策略以优化食品产品信息获取**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `信息提取` `生成式人工智能` `食品产品` `在线零售` `效率优化` `成本降低`

## 📋 核心要点

1. 现有方法在提取食品产品信息时面临准确性和效率的挑战，尤其是在处理大量网页时。
2. 本研究提出了一种基于LLM的间接提取策略，通过生成函数来优化信息提取过程，减少LLM调用次数。
3. 实验结果表明，间接提取方法在保持高准确率的同时，显著提高了效率，降低了运营成本。

## 📝 摘要（中文）

生成式人工智能和大型语言模型（LLMs）在自动化提取网页结构化信息方面具有显著潜力。本研究聚焦于在线零售商的食品产品页面，探索受模式约束的提取方法，以获取关键产品属性，如成分列表和营养表。我们比较了两种基于LLM的方法：直接提取和通过生成函数的间接提取，并在一个包含3000个食品产品页面的精心策划数据集上评估它们的准确性、效率和成本。结果显示，尽管间接提取的准确性略低（96.48%，比直接提取低1.61%），但其所需的LLM调用次数减少了95.82%，从而实现了显著的效率提升和更低的运营成本。这些发现表明，间接提取方法可以为基于模板的网页大规模信息提取任务提供可扩展且具有成本效益的解决方案。

## 🔬 方法详解

**问题定义**：本论文旨在解决从在线食品产品页面提取结构化信息的效率和准确性问题。现有方法在处理大量数据时，往往需要频繁调用LLM，导致成本高昂且效率低下。

**核心思路**：论文提出的间接提取策略通过生成函数来优化信息提取过程，减少对LLM的直接调用，从而提高整体效率和降低成本。

**技术框架**：整体架构包括数据预处理、LLM调用、信息提取和结果后处理四个主要模块。数据预处理阶段负责清洗和格式化输入数据，LLM调用阶段则根据生成函数进行信息提取，最后通过后处理模块整理和输出结果。

**关键创新**：最重要的技术创新在于提出了间接提取方法，该方法通过生成函数减少了对LLM的直接调用，显著提升了信息提取的效率和可扩展性。

**关键设计**：在设计中，关键参数包括生成函数的构建方式和LLM调用的频率设置。损失函数采用了适应性调整策略，以平衡准确性和效率之间的关系。

## 📊 实验亮点

实验结果显示，间接提取方法的准确率为96.48%，相比直接提取方法仅低1.61%。同时，该方法减少了95.82%的LLM调用次数，显著提高了效率并降低了运营成本，展示了其在大规模信息提取任务中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括电子商务、食品安全监测和营养信息管理等。通过优化信息提取过程，在线零售商可以更高效地获取和更新产品信息，从而提升用户体验和市场竞争力。未来，该方法还可能扩展到其他类型的网页信息提取任务中，具有广泛的实际价值。

## 📄 摘要（原文）

> Generative AI and large language models (LLMs) offer significant potential for automating the extraction of structured information from web pages. In this work, we focus on food product pages from online retailers and explore schema-constrained extraction approaches to retrieve key product attributes, such as ingredient lists and nutrition tables. We compare two LLM-based approaches, direct extraction and indirect extraction via generated functions, evaluating them in terms of accuracy, efficiency, and cost on a curated dataset of 3,000 food product pages from three different online shops. Our results show that although the indirect approach achieves slightly lower accuracy (96.48\%, $-1.61\%$ compared to direct extraction), it reduces the number of required LLM calls by 95.82\%, leading to substantial efficiency gains and lower operational costs. These findings suggest that indirect extraction approaches can provide scalable and cost-effective solutions for large-scale information extraction tasks from template-based web pages using LLMs.

