---
layout: default
title: Automated Structured Radiology Report Generation with Rich Clinical Context
---

# Automated Structured Radiology Report Generation with Rich Clinical Context

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00428" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00428v1</a>
  <a href="https://arxiv.org/pdf/2510.00428.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00428v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00428v1', 'Automated Structured Radiology Report Generation with Rich Clinical Context')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seongjae Kang, Dong Bok Lee, Juho Jung, Dongseop Kim, Won Hwa Kim, Sunghoon Joo

**分类**: cs.LG, cs.AI

**发布日期**: 2025-10-01

**备注**: 34 pages, 30 figures, preprint

**🔗 代码/项目**: [GITHUB](https://github.com/vuno/contextualized-srrg)

---

## 💡 一句话要点

**提出C-SRRG，利用丰富临床上下文自动生成结构化放射报告，提升报告质量。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `放射报告生成` `临床上下文` `多模态学习` `大型语言模型` `医学影像` `结构化报告` `胸部X光`

## 📋 核心要点

1. 现有自动化结构化放射报告生成系统忽略了临床上下文，导致报告质量下降，甚至出现时间幻觉。
2. C-SRRG通过整合多视角X射线图像、临床适应症、成像技术和历史研究等信息，全面利用临床上下文。
3. 实验表明，C-SRRG显著提升了报告生成质量，相关数据集、代码和模型已开源。

## 📝 摘要（中文）

本文提出了一种基于丰富临床上下文的自动化结构化放射报告生成（SRRG）方法，旨在解决现有SRRG系统忽略重要临床信息的问题。现有方法的不足会导致时间幻觉等问题。为了解决这些局限性，我们提出了上下文SRRG（C-SRRG），它全面整合了丰富的临床上下文，包括多视角X射线图像、临床适应症、成像技术以及基于患者历史的先前研究及其比较。我们创建了C-SRRG数据集，并通过与最先进的多模态大型语言模型进行广泛的基准测试，证明了结合临床上下文的C-SRRG显著提高了报告生成质量。我们公开发布数据集、代码和检查点，以促进未来在临床对齐的自动化RRG方面的研究。

## 🔬 方法详解

**问题定义**：现有自动化结构化放射报告生成（SRRG）系统在生成报告时，往往忽略了重要的临床上下文信息，例如患者的既往病史、临床适应症、成像技术等。这种忽略导致生成的报告可能不准确、不完整，甚至出现与实际情况不符的时间幻觉。因此，如何有效地将丰富的临床上下文信息融入到SRRG系统中，是一个亟待解决的问题。

**核心思路**：本文的核心思路是将多模态大型语言模型与丰富的临床上下文信息相结合，从而提升SRRG的性能。具体来说，作者认为放射科医生在诊断时会充分利用临床上下文，因此SRRG系统也应该具备类似的能力。通过将多视角X射线图像、临床适应症、成像技术以及基于患者历史的先前研究及其比较等信息整合到模型中，可以使模型更好地理解图像内容，并生成更准确、更全面的报告。

**技术框架**：C-SRRG的技术框架主要包括以下几个部分：1) 数据收集与整理：构建包含多视角X射线图像、临床适应症、成像技术和历史研究等信息的C-SRRG数据集。2) 模型构建：选择合适的多模态大型语言模型作为基础模型。3) 上下文信息编码：设计有效的上下文信息编码方式，将临床上下文信息融入到模型中。4) 报告生成：利用模型生成结构化放射报告。5) 评估：使用相关指标评估报告的质量。

**关键创新**：本文的关键创新在于提出了C-SRRG，一种全面整合丰富临床上下文的SRRG方法。与现有方法相比，C-SRRG能够更有效地利用临床信息，从而生成更准确、更全面的报告。此外，C-SRRG数据集的构建也是一个重要的贡献，为后续研究提供了宝贵的数据资源。

**关键设计**：论文中没有详细描述关键参数设置、损失函数和网络结构等技术细节。这些细节可能取决于所选择的多模态大型语言模型。但是，上下文信息的编码方式是关键设计之一，具体实现方式未知。

## 📊 实验亮点

实验结果表明，通过整合临床上下文，C-SRRG在报告生成质量上取得了显著提升。具体性能数据和对比基线未在摘要中明确给出，但强调了与最先进的多模态大型语言模型相比，C-SRRG具有明显的优势。数据集、代码和模型已开源，方便后续研究。

## 🎯 应用场景

该研究成果可应用于临床放射科，辅助医生自动生成结构化报告，减轻医生工作负担，提高报告效率和一致性。通过整合患者病史和影像信息，有望提升诊断准确率，减少漏诊误诊。未来可扩展到其他医学影像领域，具有广阔的应用前景。

## 📄 摘要（原文）

> Automated structured radiology report generation (SRRG) from chest X-ray images offers significant potential to reduce workload of radiologists by generating reports in structured formats that ensure clarity, consistency, and adherence to clinical reporting standards. While radiologists effectively utilize available clinical contexts in their diagnostic reasoning, existing SRRG systems overlook these essential elements. This fundamental gap leads to critical problems including temporal hallucinations when referencing non-existent clinical contexts. To address these limitations, we propose contextualized SRRG (C-SRRG) that comprehensively incorporates rich clinical context for SRRG. We curate C-SRRG dataset by integrating comprehensive clinical context encompassing 1) multi-view X-ray images, 2) clinical indication, 3) imaging techniques, and 4) prior studies with corresponding comparisons based on patient histories. Through extensive benchmarking with state-of-the-art multimodal large language models, we demonstrate that incorporating clinical context with the proposed C-SRRG significantly improves report generation quality. We publicly release dataset, code, and checkpoints to facilitate future research for clinically-aligned automated RRG at https://github.com/vuno/contextualized-srrg.

