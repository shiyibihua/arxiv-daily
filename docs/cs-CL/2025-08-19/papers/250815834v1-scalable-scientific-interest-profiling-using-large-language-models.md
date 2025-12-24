---
layout: default
title: Scalable Scientific Interest Profiling Using Large Language Models
---

# Scalable Scientific Interest Profiling Using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15834" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15834v1</a>
  <a href="https://arxiv.org/pdf/2508.15834.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15834v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15834v1', 'Scalable Scientific Interest Profiling Using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yilun Liang, Gongbo Zhang, Edward Sun, Betina Idnay, Yilu Fang, Fangyi Chen, Casey Ta, Yifan Peng, Chunhua Weng

**分类**: cs.CL, cs.DL, cs.IR, q-bio.OT

**发布日期**: 2025-08-19

---

## 💡 一句话要点

**提出基于大语言模型的科学兴趣画像生成方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `科学兴趣画像` `医学主题词` `PubMed摘要` `自动评估` `可读性` `研究者简介`

## 📋 核心要点

1. 现有的研究者个人简介往往过时，无法准确反映其专业领域和研究兴趣。
2. 本文提出了两种基于大语言模型的方法，通过总结PubMed摘要和使用MeSH术语生成科学兴趣画像。
3. 实验结果表明，MeSH基础画像在可读性和评审评分上优于摘要基础画像，显示出大语言模型在生成研究者画像方面的潜力。

## 📝 摘要（中文）

研究者的个人简介有助于展示其专业领域，但往往过时。本文开发并评估了两种基于大语言模型的方法来生成科学兴趣画像：一种是总结PubMed摘要，另一种是使用医学主题词（MeSH）。我们对595名哥伦比亚大学医学中心的教职工进行了数据收集，并与167名研究者的自撰简介进行了比较。使用GPT-4o-mini生成的画像在自动评估指标和盲人评审中表现出较低的词汇重叠，但在语义相似性上表现中等。手动评审中，77.78%的MeSH基础画像被评为良好或优秀，93.44%的案例中可读性受到青睐。总体而言，大语言模型能够大规模生成研究者画像，MeSH基础画像的可读性优于摘要基础画像。

## 🔬 方法详解

**问题定义**：本文旨在解决现有研究者个人简介过时的问题，现有方法无法有效反映研究者的最新研究兴趣和专业领域。

**核心思路**：论文提出通过大语言模型生成科学兴趣画像，利用PubMed摘要和MeSH术语进行总结，以提高画像的准确性和可读性。

**技术框架**：整体流程包括数据收集、模型训练和评估。首先收集595名教职工的标题、MeSH术语和摘要，然后使用GPT-4o-mini生成画像，最后通过自动指标和人工评审进行评估。

**关键创新**：最重要的创新在于使用MeSH术语生成画像，显示出比摘要生成方法更高的可读性和评审评分，体现了模型在科学领域的适用性。

**关键设计**：在模型训练中，使用了TF-IDF Kullback-Leibler散度来评估关键词选择的独特性，并通过ROUGE-L、BLEU和METEOR等指标进行自动评估，确保生成内容的质量和相关性。

## 📊 实验亮点

实验结果显示，MeSH基础画像在手动评审中有77.78%的好评率，93.44%的案例中可读性受到青睐。此外，BERTScore显示MeSH基础画像的语义相似性为0.542，摘要基础画像为0.555，表明MeSH方法在生成质量上的优势。

## 🎯 应用场景

该研究的潜在应用领域包括学术界、科研机构和专业社交平台。通过生成准确且易读的研究者画像，可以帮助科研人员更好地展示其专业领域，促进学术交流与合作，提升科研效率。未来，该方法还可扩展至其他领域的专业画像生成。

## 📄 摘要（原文）

> Research profiles help surface scientists' expertise but are often outdated. We develop and evaluate two large language model-based methods to generate scientific interest profiles: one summarizing PubMed abstracts and one using Medical Subject Headings (MeSH) terms, and compare them with researchers' self-written profiles. We assembled titles, MeSH terms, and abstracts for 595 faculty at Columbia University Irving Medical Center; self-authored profiles were available for 167. Using GPT-4o-mini, we generated profiles and assessed them with automatic metrics and blinded human review. Lexical overlap with self-written profiles was low (ROUGE-L, BLEU, METEOR), while BERTScore indicated moderate semantic similarity (F1: 0.542 for MeSH-based; 0.555 for abstract-based). Paraphrased references yielded 0.851, highlighting metric sensitivity. TF-IDF Kullback-Leibler divergence (8.56 for MeSH-based; 8.58 for abstract-based) suggested distinct keyword choices. In manual review, 77.78 percent of MeSH-based profiles were rated good or excellent, readability was favored in 93.44 percent of cases, and panelists preferred MeSH-based over abstract-based profiles in 67.86 percent of comparisons. Overall, large language models can generate researcher profiles at scale; MeSH-derived profiles tend to be more readable than abstract-derived ones. Machine-generated and self-written profiles differ conceptually, with human summaries introducing more novel ideas.

