---
layout: default
title: A Comparative Benchmark of Large Language Models for Labelling Wind Turbine Maintenance Logs
---

# A Comparative Benchmark of Large Language Models for Labelling Wind Turbine Maintenance Logs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06813" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06813v1</a>
  <a href="https://arxiv.org/pdf/2509.06813.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06813v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06813v1', 'A Comparative Benchmark of Large Language Models for Labelling Wind Turbine Maintenance Logs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Max Malyi, Jonathan Shek, Alasdair McDonald, Andre Biscaya

**分类**: cs.CL

**发布日期**: 2025-09-08

**备注**: Associated GitHub repository: https://github.com/mvmalyi/wind-farm-maintenance-logs-labelling-with-llms

---

## 💡 一句话要点

**提出风机维护日志标注的LLM基准测试框架，助力运维数据分析**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `风机维护` `运维数据分析` `基准测试` `人机协作`

## 📋 核心要点

1. 风机维护日志的非结构化特性阻碍了自动化分析，影响运维效率和成本控制。
2. 论文提出一个开源的LLM基准测试框架，用于评估LLM在风机维护日志分类任务上的性能。
3. 实验结果表明，LLM在客观组件识别上表现更好，但模型校准差异大，人机协作是更优方案。

## 📝 摘要（中文）

有效的运维（O&M）对于降低风电的度电成本（LCOE）至关重要，但风机维护日志的非结构化自由文本性质给自动化分析带来了巨大障碍。本文提出了一个新颖且可复现的框架，用于对大型语言模型（LLM）在分类这些复杂工业记录的任务上进行基准测试。为了提高透明度并鼓励进一步研究，该框架已作为开源工具公开发布。我们系统地评估了一套多样化的最先进的专有和开源LLM，为它们在可靠性、运营效率和模型校准方面的权衡提供了基础评估。我们的结果量化了一个清晰的性能等级，确定了与基准标准高度一致且具有可信、良好校准的置信度分数的顶级模型。我们还证明了分类性能高度依赖于任务的语义模糊性，所有模型在客观组件识别方面比在解释性维护操作方面表现出更高的共识。鉴于没有模型能达到完美的准确性，并且校准差异很大，我们得出结论，最有效和负责任的近期应用是人机协作系统，其中LLM充当强大的助手，加速和标准化人类专家的数据标注，从而提高O&M数据质量和下游可靠性分析。

## 🔬 方法详解

**问题定义**：论文旨在解决风机维护日志的自动化分类问题。现有方法难以处理日志的非结构化和自由文本特性，导致运维数据分析效率低下，影响风电度电成本的降低。现有的痛点在于缺乏一个系统性的方法来评估不同LLM在处理此类工业数据上的能力，以及缺乏对模型可靠性和校准的深入理解。

**核心思路**：论文的核心思路是构建一个可复现的基准测试框架，用于评估各种LLM在风机维护日志分类任务上的性能。通过系统性的评估，可以量化不同LLM在可靠性、运营效率和模型校准方面的权衡，从而为实际应用提供指导。此外，论文强调了人机协作的重要性，认为LLM可以作为人类专家的助手，加速和标准化数据标注过程。

**技术框架**：该框架包含以下主要模块：1) 数据集构建：收集和整理风机维护日志数据，并进行标注。2) 模型选择：选择一系列具有代表性的LLM，包括专有模型和开源模型。3) 评估指标：定义用于评估模型性能的指标，例如准确率、召回率、F1值和校准误差。4) 基准测试：使用框架对选定的LLM进行基准测试，并记录其性能数据。5) 结果分析：分析基准测试结果，比较不同LLM的性能，并识别最佳模型。

**关键创新**：论文的关键创新在于提出了一个公开可用的、可复现的LLM基准测试框架，专门用于评估风机维护日志的分类任务。该框架不仅提供了一个系统性的评估方法，还关注了模型的可靠性和校准，这在以往的研究中往往被忽略。此外，论文强调了人机协作的重要性，并提出了将LLM作为人类专家助手的应用模式。

**关键设计**：论文的关键设计包括：1) 选择多样化的LLM，以覆盖不同的模型架构和训练数据。2) 使用多个评估指标，以全面评估模型的性能。3) 关注模型的校准，以确保模型输出的置信度是可靠的。4) 设计人机协作流程，以充分利用LLM和人类专家的优势。

## 📊 实验亮点

实验结果表明，不同LLM在风机维护日志分类任务上的性能存在显著差异。部分模型在客观组件识别方面表现出较高的准确率和一致性，但所有模型在解释性维护操作方面都面临挑战。模型校准差异显著，表明需要谨慎选择和使用LLM。研究强调了人机协作的重要性，认为LLM可以作为人类专家的助手，提高数据标注效率和质量。

## 🎯 应用场景

该研究成果可应用于风电行业的智能运维领域，通过LLM辅助分析风机维护日志，提升数据质量和分析效率，降低运维成本，提高风电场的可靠性和发电效率。未来可扩展到其他工业领域，例如石油化工、航空航天等，用于故障诊断、预测性维护等任务。

## 📄 摘要（原文）

> Effective Operation and Maintenance (O&M) is critical to reducing the Levelised Cost of Energy (LCOE) from wind power, yet the unstructured, free-text nature of turbine maintenance logs presents a significant barrier to automated analysis. Our paper addresses this by presenting a novel and reproducible framework for benchmarking Large Language Models (LLMs) on the task of classifying these complex industrial records. To promote transparency and encourage further research, this framework has been made publicly available as an open-source tool. We systematically evaluate a diverse suite of state-of-the-art proprietary and open-source LLMs, providing a foundational assessment of their trade-offs in reliability, operational efficiency, and model calibration. Our results quantify a clear performance hierarchy, identifying top models that exhibit high alignment with a benchmark standard and trustworthy, well-calibrated confidence scores. We also demonstrate that classification performance is highly dependent on the task's semantic ambiguity, with all models showing higher consensus on objective component identification than on interpretive maintenance actions. Given that no model achieves perfect accuracy and that calibration varies dramatically, we conclude that the most effective and responsible near-term application is a Human-in-the-Loop system, where LLMs act as a powerful assistant to accelerate and standardise data labelling for human experts, thereby enhancing O&M data quality and downstream reliability analysis.

