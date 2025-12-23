---
layout: default
title: A Multi-Pass Large Language Model Framework for Precise and Efficient Radiology Report Error Detection
---

# A Multi-Pass Large Language Model Framework for Precise and Efficient Radiology Report Error Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20112" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20112v1</a>
  <a href="https://arxiv.org/pdf/2506.20112.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20112v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20112v1', 'A Multi-Pass Large Language Model Framework for Precise and Efficient Radiology Report Error Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Songsoo Kim, Seungtae Lee, See Young Lee, Joonho Kim, Keechan Kan, Dukyong Yoon

**分类**: cs.CL

**发布日期**: 2025-06-25

**备注**: 29 pages, 5 figures, 4 tables. Code available at https://github.com/radssk/mp-rred

---

## 💡 一句话要点

**提出三次通道大型语言模型框架以提升放射学报告错误检测精度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `放射学报告` `错误检测` `阳性预测值` `多通道框架` `医疗影像分析` `质量保证`

## 📋 核心要点

1. 现有基于LLM的放射学报告校对方法的阳性预测值（PPV）较低，难以有效检测错误。
2. 论文提出了一种三次通道LLM框架，通过多阶段处理提高错误检测的准确性和效率。
3. 实验结果显示，框架PPV显著提高至0.159，运营成本降低42.6%，有效减少了人工审核的报告数量。

## 📝 摘要（中文）

背景：基于大型语言模型（LLM）的放射学报告校对的阳性预测值（PPV）因错误发生率低而受到限制。目的：评估三次通道LLM框架是否能提高PPV并降低运营成本。方法：对MIMIC-III数据库中的1000份连续放射学报告进行回顾性分析，测试了三种LLM框架。结果：框架PPV从0.063提升至0.159，运营成本每千份报告降至5.58美元。结论：三次通道LLM框架显著提高了PPV并降低了运营成本，提供了一种有效的AI辅助放射学报告质量保证策略。

## 🔬 方法详解

**问题定义**：本论文旨在解决基于大型语言模型的放射学报告校对中阳性预测值（PPV）低的问题。现有方法在错误发生率低的情况下，难以有效识别和校对报告中的错误。

**核心思路**：论文提出的三次通道LLM框架通过引入多阶段处理机制，增强了错误检测的准确性和效率，旨在提高PPV并降低运营成本。

**技术框架**：整体架构包括三个主要模块：单次提示检测器、提取器加检测器、以及提取器、检测器和假阳性验证器的组合。每个模块在不同阶段对报告进行分析和校对。

**关键创新**：最重要的技术创新在于引入了三次通道的处理流程，使得模型能够在不同层次上进行错误检测，从而显著提高了PPV，与传统单一检测方法相比具有本质区别。

**关键设计**：在模型设计中，采用了多种统计检验方法（如集群自助法、McNemar检验等）来验证结果的显著性，并通过优化模型推理费用和审核人员薪酬来提升效率。

## 📊 实验亮点

实验结果表明，三次通道框架的PPV从0.063提升至0.159，运营成本每千份报告降至5.58美元，较基线方法显著降低42.6%。此外，人工审核的报告数量从192减少至88，显示出该框架在效率上的优势。

## 🎯 应用场景

该研究的潜在应用领域包括医疗影像分析、放射学报告自动校对和质量保证等。通过提高放射学报告的错误检测能力，能够有效提升医疗服务质量，减少误诊风险，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> Background: The positive predictive value (PPV) of large language model (LLM)-based proofreading for radiology reports is limited due to the low error prevalence. Purpose: To assess whether a three-pass LLM framework enhances PPV and reduces operational costs compared with baseline approaches. Materials and Methods: A retrospective analysis was performed on 1,000 consecutive radiology reports (250 each: radiography, ultrasonography, CT, MRI) from the MIMIC-III database. Two external datasets (CheXpert and Open-i) were validation sets. Three LLM frameworks were tested: (1) single-prompt detector; (2) extractor plus detector; and (3) extractor, detector, and false-positive verifier. Precision was measured by PPV and absolute true positive rate (aTPR). Efficiency was calculated from model inference charges and reviewer remuneration. Statistical significance was tested using cluster bootstrap, exact McNemar tests, and Holm-Bonferroni correction. Results: Framework PPV increased from 0.063 (95% CI, 0.036-0.101, Framework 1) to 0.079 (0.049-0.118, Framework 2), and significantly to 0.159 (0.090-0.252, Framework 3; P<.001 vs. baselines). aTPR remained stable (0.012-0.014; P>=.84). Operational costs per 1,000 reports dropped to USD 5.58 (Framework 3) from USD 9.72 (Framework 1) and USD 6.85 (Framework 2), reflecting reductions of 42.6% and 18.5%, respectively. Human-reviewed reports decreased from 192 to 88. External validation supported Framework 3's superior PPV (CheXpert 0.133, Open-i 0.105) and stable aTPR (0.007). Conclusion: A three-pass LLM framework significantly enhanced PPV and reduced operational costs, maintaining detection performance, providing an effective strategy for AI-assisted radiology report quality assurance.

