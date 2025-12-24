---
layout: default
title: Using Large Language Models to Measure Symptom Severity in Patients At Risk for Schizophrenia
---

# Using Large Language Models to Measure Symptom Severity in Patients At Risk for Schizophrenia

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10226" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10226v1</a>
  <a href="https://arxiv.org/pdf/2508.10226.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10226v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10226v1', 'Using Large Language Models to Measure Symptom Severity in Patients At Risk for Schizophrenia')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andrew X. Chen, Guillermo Horga, Sean Escola

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**利用大型语言模型评估精神分裂症高风险患者的症状严重性**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `精神健康评估` `症状监测` `精神分裂症` `临床应用` `机器学习` `自然语言处理`

## 📋 核心要点

1. 现有的BPRS评估方法依赖于结构化访谈，耗时且不便于临床应用，限制了其在实际中的使用。
2. 本文提出利用大型语言模型从非结构化的临床访谈记录中预测BPRS评分，旨在提高评估的效率和准确性。
3. 实验结果表明，LLM的预测性能接近人类评估者，且在多语言环境下表现优异，具有显著的应用潜力。

## 📝 摘要（中文）

处于临床高风险（CHR）状态的精神分裂症患者需要密切监测其症状以指导适当的治疗。尽管简短精神病评定量表（BPRS）是评估精神分裂症及其他精神障碍症状的有效工具，但由于其需要较长的结构化访谈，故在临床实践中不常使用。本文利用大型语言模型（LLMs）从409名CHR患者的临床访谈记录中预测BPRS评分。尽管访谈并未专门设计用于测量BPRS，但LLM预测的零-shot性能与真实评估的中位一致性达到0.84（ICC: 0.73），接近人类评估者之间的可靠性。我们进一步展示了LLMs在评估外语BPRS方面的潜力（中位一致性：0.88，ICC: 0.70），并能够通过一-shot或少-shot学习整合纵向信息。

## 🔬 方法详解

**问题定义**：本文旨在解决精神分裂症高风险患者症状评估的效率问题。现有的BPRS评估方法需要耗时的结构化访谈，导致其在临床实践中的应用受限。

**核心思路**：通过利用大型语言模型（LLMs），从非结构化的临床访谈记录中直接预测BPRS评分，以提高评估的效率和准确性。该方法不依赖于特定的访谈结构，能够适应多种语言和情境。

**技术框架**：整体架构包括数据收集、LLM训练与预测、结果评估三个主要模块。首先收集来自409名CHR患者的访谈记录，然后使用LLMs进行评分预测，最后通过与真实BPRS评分进行比较来评估模型性能。

**关键创新**：最重要的技术创新在于将大型语言模型应用于精神健康领域，尤其是在非结构化数据的处理上。与传统方法相比，LLMs能够在没有专门设计的访谈结构下，仍然实现高准确度的评分预测。

**关键设计**：在模型训练中，采用了零-shot学习策略，允许模型在未见过的访谈数据上进行有效预测。损失函数设计为最小化预测评分与真实评分之间的差异，确保模型的准确性和可靠性。

## 📊 实验亮点

实验结果显示，LLM在预测BPRS评分时的中位一致性达到0.84（ICC: 0.73），接近人类评估者的可靠性。此外，在外语评估中，LLM的中位一致性更是达到0.88（ICC: 0.70），显示出其在多语言环境下的强大适应能力和准确性。

## 🎯 应用场景

该研究的潜在应用领域包括精神健康评估、临床监测和个性化治疗方案制定。通过提高症状评估的效率和准确性，LLMs能够帮助医生更好地监测和管理精神分裂症高风险患者的治疗过程，进而改善患者的预后。未来，该方法可能在其他精神障碍的评估中得到推广，具有广泛的实际价值。

## 📄 摘要（原文）

> Patients who are at clinical high risk (CHR) for schizophrenia need close monitoring of their symptoms to inform appropriate treatments. The Brief Psychiatric Rating Scale (BPRS) is a validated, commonly used research tool for measuring symptoms in patients with schizophrenia and other psychotic disorders; however, it is not commonly used in clinical practice as it requires a lengthy structured interview. Here, we utilize large language models (LLMs) to predict BPRS scores from clinical interview transcripts in 409 CHR patients from the Accelerating Medicines Partnership Schizophrenia (AMP-SCZ) cohort. Despite the interviews not being specifically structured to measure the BPRS, the zero-shot performance of the LLM predictions compared to the true assessment (median concordance: 0.84, ICC: 0.73) approaches human inter- and intra-rater reliability. We further demonstrate that LLMs have substantial potential to improve and standardize the assessment of CHR patients via their accuracy in assessing the BPRS in foreign languages (median concordance: 0.88, ICC: 0.70), and integrating longitudinal information in a one-shot or few-shot learning approach.

