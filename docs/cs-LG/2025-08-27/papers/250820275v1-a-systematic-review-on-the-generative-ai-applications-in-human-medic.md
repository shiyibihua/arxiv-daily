---
layout: default
title: A Systematic Review on the Generative AI Applications in Human Medical Genomics
---

# A Systematic Review on the Generative AI Applications in Human Medical Genomics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20275" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20275v1</a>
  <a href="https://arxiv.org/pdf/2508.20275.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20275v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20275v1', 'A Systematic Review on the Generative AI Applications in Human Medical Genomics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anton Changalidis, Yury Barbitoff, Yulia Nasykhova, Andrey Glotov

**分类**: cs.LG, cs.CL, q-bio.QM

**发布日期**: 2025-08-27

**备注**: 31 pages, 5 figures

---

## 💡 一句话要点

**系统评估生成性AI在医学基因组学中的应用**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `生成性AI` `医学基因组学` `大型语言模型` `遗传疾病诊断` `多模态数据整合` `深度学习` `医学影像分析`

## 📋 核心要点

1. 现有的统计和机器学习方法在处理复杂高维数据时存在局限，难以满足遗传学的需求。
2. 论文通过系统评估大型语言模型在遗传研究和诊断中的应用，提出了基于变换器的深度学习方法。
3. 分析结果显示，变换器模型在疾病分层和医学影像分析中取得显著进展，但多模态数据整合仍面临挑战。

## 📝 摘要（中文）

尽管传统统计技术和机器学习方法在遗传学及遗传疾病诊断中贡献显著，但在处理复杂的高维数据时常常面临挑战。基于变换器架构的大型语言模型（LLMs）在理解非结构化医学数据方面表现优异。本系统评估回顾了LLMs在遗传研究和诊断中的作用，分析了172项研究，重点关注基因变异识别、注释和解释，以及通过视觉变换器推动的医学影像进展。研究发现，尽管变换器模型在疾病和风险分层、变异解释、医学影像分析和报告生成方面取得了显著进展，但在将多模态数据（基因组序列、影像和临床记录）整合为统一且临床稳健的流程中仍面临重大挑战，限制了其在临床环境中的普遍适用性和实际实施。此评估为导航这一快速发展的领域提供了全面的分类和评估。

## 🔬 方法详解

**问题定义**：本论文旨在解决传统统计和机器学习方法在遗传学中处理复杂高维数据的不足，特别是在遗传疾病诊断中的应用痛点。

**核心思路**：通过系统评估大型语言模型（LLMs）在遗传研究和诊断中的应用，利用其在理解非结构化医学数据方面的优势，推动遗传学领域的进步。

**技术框架**：研究采用自动化关键词搜索方法，分析来自PubMed、bioRxiv、medRxiv和arXiv的172项相关研究，重点关注LLMs在基因变异识别、注释和医学影像分析中的应用。

**关键创新**：论文的主要创新在于系统性地评估和分类LLMs在遗传学中的应用，特别是在疾病诊断和教育支持方面的潜力，填补了现有文献的空白。

**关键设计**：研究中采用了多种数据源进行分析，重点关注变换器模型在处理多模态数据时的表现，尽管在实际应用中仍面临整合和通用性方面的挑战。

## 📊 实验亮点

研究表明，变换器模型在疾病和风险分层、变异解释及医学影像分析中显著提升了性能，尽管在多模态数据整合方面仍存在挑战。具体性能数据和对比基线未在摘要中提供，需查阅完整论文以获取详细信息。

## 🎯 应用场景

该研究的潜在应用领域包括遗传疾病的诊断、基因组变异的识别与解释，以及医学教育的支持。通过推动大型语言模型在这些领域的应用，可以提高遗传学研究的效率和准确性，促进个性化医疗的发展。

## 📄 摘要（原文）

> Although traditional statistical techniques and machine learning methods have contributed significantly to genetics and, in particular, inherited disease diagnosis, they often struggle with complex, high-dimensional data, a challenge now addressed by state-of-the-art deep learning models. Large language models (LLMs), based on transformer architectures, have excelled in tasks requiring contextual comprehension of unstructured medical data. This systematic review examines the role of LLMs in the genetic research and diagnostics of both rare and common diseases. Automated keyword-based search in PubMed, bioRxiv, medRxiv, and arXiv was conducted, targeting studies on LLM applications in diagnostics and education within genetics and removing irrelevant or outdated models. A total of 172 studies were analyzed, highlighting applications in genomic variant identification, annotation, and interpretation, as well as medical imaging advancements through vision transformers. Key findings indicate that while transformer-based models significantly advance disease and risk stratification, variant interpretation, medical imaging analysis, and report generation, major challenges persist in integrating multimodal data (genomic sequences, imaging, and clinical records) into unified and clinically robust pipelines, facing limitations in generalizability and practical implementation in clinical settings. This review provides a comprehensive classification and assessment of the current capabilities and limitations of LLMs in transforming hereditary disease diagnostics and supporting genetic education, serving as a guide to navigate this rapidly evolving field.

