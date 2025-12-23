---
layout: default
title: Scalable Medication Extraction and Discontinuation Identification from Electronic Health Records Using Large Language Models
---

# Scalable Medication Extraction and Discontinuation Identification from Electronic Health Records Using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11137" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11137v3</a>
  <a href="https://arxiv.org/pdf/2506.11137.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11137v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11137v3', 'Scalable Medication Extraction and Discontinuation Identification from Electronic Health Records Using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chong Shao, Douglas Snyder, Chiran Li, Bowen Gu, Kerry Ngan, Chun-Ting Yang, Jiageng Wu, Richard Wyss, Kueiyu Joshua Lin, Jie Yang

**分类**: cs.CL

**发布日期**: 2025-06-10 (更新: 2025-11-06)

---

## 💡 一句话要点

**利用大型语言模型提取电子健康记录中的药物信息与停药识别**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `电子健康记录` `药物信息提取` `停药识别` `大型语言模型` `无人工标注` `开源模型` `临床决策支持`

## 📋 核心要点

1. 现有方法在提取电子健康记录中的药物信息时，常因信息分散在非结构化文本中而面临挑战。
2. 本研究通过评估多种大型语言模型，提出了一种无人工标注的药物信息提取和停药识别方法。
3. 实验结果表明，GPT-4o在药物提取和停药分类任务中表现优异，尤其在零样本设置下的F1分数达到94.0%。

## 📝 摘要（中文）

识别电子健康记录（EHR）中的药物停用情况对患者安全至关重要，但常因信息埋藏在非结构化笔记中而受到阻碍。本研究旨在评估先进的开源和专有大型语言模型（LLMs）在提取药物信息及分类其状态方面的能力，重点关注无人工标注的药物信息提取的可扩展性。我们收集了来自不同来源的三个EHR数据集以构建评估基准，系统比较了12个先进LLMs在药物提取、药物状态分类及其联合任务上的表现。结果显示，LLMs在EHR笔记中的药物提取和停药分类表现出良好的潜力，尤其是GPT-4o在所有任务中均取得了最高的平均F1分数。

## 🔬 方法详解

**问题定义**：本研究旨在解决电子健康记录中药物信息提取和停药识别的难题，现有方法往往无法有效处理非结构化文本中的信息，导致患者安全风险增加。

**核心思路**：论文提出利用大型语言模型（LLMs）进行药物信息的自动提取和状态分类，重点在于无人工标注的可扩展性，以提高处理效率和准确性。

**技术框架**：研究构建了一个评估基准，包含三个来自不同来源的EHR数据集，并对12个先进的LLMs进行了系统比较，探索了多种提示策略。主要模块包括药物提取、状态分类和联合任务处理。

**关键创新**：本研究的创新点在于利用LLMs进行药物信息提取和停药识别，尤其是在零样本设置下，展示了开源模型在实际应用中的潜力，超越了传统方法的限制。

**关键设计**：在实验中，采用了多种提示策略和少量样本学习，优化了模型的性能，特别是GPT-4o和Llama-3.1-70B-Instruct在不同任务中的表现显著提升。

## 📊 实验亮点

实验结果显示，GPT-4o在药物提取任务中取得了94.0%的F1分数，在停药分类任务中为78.1%，而在联合任务中为72.7%。开源模型Llama-3.1-70B-Instruct在药物状态分类和联合任务中也表现出色，分别达到了68.7%和76.2%的F1分数，显示出LLMs在医疗数据处理中的强大潜力。

## 🎯 应用场景

该研究的成果可广泛应用于医疗健康领域，尤其是在电子健康记录的管理和分析中。通过自动化药物信息提取和停药识别，可以提高临床决策的准确性，降低医疗错误的风险，进而提升患者安全。此外，开源模型的可扩展性使得其在资源有限的医疗机构中也能得到应用，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Identifying medication discontinuations in electronic health records (EHRs) is vital for patient safety but is often hindered by information being buried in unstructured notes. This study aims to evaluate the capabilities of advanced open-sourced and proprietary large language models (LLMs) in extracting medications and classifying their medication status from EHR notes, focusing on their scalability on medication information extraction without human annotation. We collected three EHR datasets from diverse sources to build the evaluation benchmark. We evaluated 12 advanced LLMs and explored multiple LLM prompting strategies. Performance on medication extraction, medication status classification, and their joint task (extraction then classification) was systematically compared across all experiments. We found that LLMs showed promising performance on the medication extraction and discontinuation classification from EHR notes. GPT-4o consistently achieved the highest average F1 scores in all tasks under zero-shot setting - 94.0% for medication extraction, 78.1% for discontinuation classification, and 72.7% for the joint task. Open-sourced models followed closely, Llama-3.1-70B-Instruct achieved the highest performance in medication status classification on the MIV-Med dataset (68.7%) and in the joint task on both the Re-CASI (76.2%) and MIV-Med (60.2%) datasets. Medical-specific LLMs demonstrated lower performance compared to advanced general-domain LLMs. Few-shot learning generally improved performance, while CoT reasoning showed inconsistent gains. LLMs demonstrate strong potential for medication extraction and discontinuation identification on EHR notes, with open-sourced models offering scalable alternatives to proprietary systems and few-shot can further improve LLMs' capability.

