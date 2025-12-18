---
layout: default
title: LLM Analysis of 150+ years of German Parliamentary Debates on Migration Reveals Shift from Post-War Solidarity to Anti-Solidarity in the Last Decade
---

# LLM Analysis of 150+ years of German Parliamentary Debates on Migration Reveals Shift from Post-War Solidarity to Anti-Solidarity in the Last Decade

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07274" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07274v1</a>
  <a href="https://arxiv.org/pdf/2509.07274.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07274v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07274v1', 'LLM Analysis of 150+ years of German Parliamentary Debates on Migration Reveals Shift from Post-War Solidarity to Anti-Solidarity in the Last Decade')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aida Kostikova, Ole Pütz, Steffen Eger, Olga Sabelfeld, Benjamin Paassen

**分类**: cs.CL, cs.CY, cs.LG

**发布日期**: 2025-09-08

---

## 💡 一句话要点

**利用LLM分析德国议会百年辩论，揭示从战后团结到反团结的转变**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `政治文本分析` `移民政策` `情感分析` `德国议会辩论`

## 📋 核心要点

1. 传统政治文本分析依赖人工标注，耗时费力且规模受限，难以捕捉长期趋势。
2. 利用LLM自动标注议会辩论中的团结/反团结倾向，考察模型大小、提示策略和数据时期的影响。
3. 揭示德国议会自2015年以来对移民的反团结倾向增强，验证LLM在政治分析中的潜力。

## 📝 摘要（中文）

本研究利用大型语言模型（LLM）分析了德国议会150多年来关于移民问题的辩论，涵盖了从二战后数百万流离失所者到近期难民潮等广泛现象。传统上，深入研究此类政治言论需要大量的人工标注，限制了分析范围。LLM有潜力部分自动化复杂的标注任务。本文对多个LLM在标注德国议会辩论中的（反）团结亚型进行了广泛评估，并与数千个人工参考标注进行了比较。评估了模型大小、提示差异、微调、历史与当代数据的影响，并研究了系统性误差。除了方法论评估，还从社会科学角度解释了由此产生的标注，从而更深入地了解二战后至今德国议会对移民的（反）团结趋势。数据显示，战后时期对移民的团结程度很高，但自2015年以来，德国议会中出现了强烈的反团结趋势，这激发了进一步的研究。这些发现突显了LLM在政治文本分析中的前景，以及移民辩论在德国的重要性，德国面临人口下降和劳动力短缺，同时也面临日益严重的社会两极分化。

## 🔬 方法详解

**问题定义**：本研究旨在解决政治文本分析中人工标注成本高昂、分析规模受限的问题。现有方法难以对大规模历史政治辩论数据进行深入分析，无法有效追踪政治立场和态度的长期演变趋势。特别是对于像移民问题这样复杂且具有时间敏感性的议题，需要一种能够自动化分析并揭示细粒度情感倾向的方法。

**核心思路**：本研究的核心思路是利用大型语言模型（LLM）的文本理解和生成能力，自动化标注德国议会辩论中关于移民问题的言论，识别其中蕴含的团结或反团结倾向。通过比较不同模型、提示策略和数据时期，评估LLM在政治文本分析中的有效性和可靠性。

**技术框架**：整体框架包括数据收集、LLM标注、人工标注验证和趋势分析四个主要阶段。首先，收集德国议会150多年的辩论数据。然后，使用不同的LLM（包括不同大小的模型和经过微调的模型）对数据进行标注，识别（反）团结亚型。接着，与大量人工标注进行比较，评估LLM的性能。最后，分析标注结果，揭示德国议会对移民态度的长期演变趋势。

**关键创新**：本研究的关键创新在于将LLM应用于大规模历史政治文本分析，并系统性地评估了LLM在标注政治情感倾向方面的能力。与传统的人工标注方法相比，LLM能够显著提高分析效率和规模。此外，研究还深入探讨了不同LLM、提示策略和数据时期对标注结果的影响，为LLM在政治文本分析中的应用提供了宝贵的经验。

**关键设计**：研究中使用了多种LLM，并针对不同的模型设计了不同的提示策略。为了提高标注的准确性，研究人员还对LLM进行了微调。此外，研究还采用了多种评估指标，包括准确率、召回率和F1值，以全面评估LLM的性能。在分析结果时，研究人员使用了统计方法来识别显著的趋势和模式。

## 📊 实验亮点

实验结果表明，LLM在标注政治情感倾向方面具有一定的能力，但其性能受到模型大小、提示策略和数据时期的影响。研究发现，自2015年以来，德国议会中对移民的反团结倾向显著增强。该研究为LLM在政治文本分析中的应用提供了有价值的参考，并揭示了德国移民政策的演变趋势。

## 🎯 应用场景

该研究成果可应用于政治科学、社会学和历史学等领域，帮助研究人员更深入地了解政治立场和态度的演变。此外，该方法还可以推广到其他类型的政治文本分析，例如新闻报道、社交媒体帖子等，为舆情监测、政策评估和政治传播研究提供支持。该研究也为利用AI技术进行社会科学研究提供了新的思路。

## 📄 摘要（原文）

> Migration has been a core topic in German political debate, from millions of expellees post World War II over labor migration to refugee movements in the recent past. Studying political speech regarding such wide-ranging phenomena in depth traditionally required extensive manual annotations, limiting the scope of analysis to small subsets of the data. Large language models (LLMs) have the potential to partially automate even complex annotation tasks. We provide an extensive evaluation of a multiple LLMs in annotating (anti-)solidarity subtypes in German parliamentary debates compared to a large set of thousands of human reference annotations (gathered over a year). We evaluate the influence of model size, prompting differences, fine-tuning, historical versus contemporary data; and we investigate systematic errors. Beyond methodological evaluation, we also interpret the resulting annotations from a social science lense, gaining deeper insight into (anti-)solidarity trends towards migrants in the German post-World War II period and recent past. Our data reveals a high degree of migrant-directed solidarity in the postwar period, as well as a strong trend towards anti-solidarity in the German parliament since 2015, motivating further research. These findings highlight the promise of LLMs for political text analysis and the importance of migration debates in Germany, where demographic decline and labor shortages coexist with rising polarization.

