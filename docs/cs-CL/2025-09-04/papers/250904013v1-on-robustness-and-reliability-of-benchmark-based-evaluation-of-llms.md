---
layout: default
title: On Robustness and Reliability of Benchmark-Based Evaluation of LLMs
---

# On Robustness and Reliability of Benchmark-Based Evaluation of LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04013" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04013v1</a>
  <a href="https://arxiv.org/pdf/2509.04013.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04013v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04013v1', 'On Robustness and Reliability of Benchmark-Based Evaluation of LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Riccardo Lunardi, Vincenzo Della Mea, Stefano Mizzaro, Kevin Roitero

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-04

**备注**: Accepted at ECAI 2025

---

## 💡 一句话要点

**评估LLM基准测试的鲁棒性和可靠性：探究语言变异对模型性能的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `鲁棒性评估` `基准测试` `语言变异` `释义生成`

## 📋 核心要点

1. 现有LLM评估依赖固定格式的基准测试，忽略了真实世界中普遍存在的语言变异性。
2. 该研究通过生成基准测试问题的多种释义，评估LLM在不同语言表达下的性能鲁棒性。
3. 实验表明，LLM在释义问题上的性能显著下降，引发对其泛化能力和评估方法可靠性的质疑。

## 📝 摘要（中文）

大型语言模型（LLMs）的有效性通常通过MMLU、ARC-C或HellaSwag等基准测试进行评估，这些测试以固定的标准化格式呈现问题。然而，实际应用涉及语言变异，要求模型在同一问题或查询的不同措辞中保持有效性。本研究系统地评估了LLM对释义基准问题的鲁棒性，并调查了基于基准的评估是否提供了模型能力的可靠衡量标准。我们系统地生成了六个不同常见基准测试中所有问题的各种释义，并测量了34个不同大小和有效性的最先进LLM的有效性变化。研究结果表明，虽然LLM排名在释义输入中保持相对稳定，但绝对有效性得分会发生变化并显着下降。这表明LLM在语言变异方面存在困难，引发了对其泛化能力和评估方法的担忧。此外，观察到的性能下降挑战了基于基准的评估的可靠性，表明高基准分数可能无法完全捕捉模型对实际输入变化的鲁棒性。我们讨论了这些发现对LLM评估方法的影响，强调需要更好地反映实际部署场景的鲁棒性感知基准。

## 🔬 方法详解

**问题定义**：现有LLM的评估方式主要依赖于标准化的基准测试，这些测试使用固定和标准化的提问方式。然而，在实际应用中，用户提出的问题具有多样性，相同的语义可以有多种不同的表达方式。因此，现有评估方法无法有效衡量LLM在真实场景下的鲁棒性和泛化能力。现有方法的痛点在于无法模拟真实世界中的语言变异性，导致评估结果可能过于乐观。

**核心思路**：本研究的核心思路是通过对现有基准测试中的问题进行释义，生成多个语义相同但表达方式不同的问题。然后，使用这些释义后的问题来评估LLM的性能，从而衡量LLM对语言变异的鲁棒性。通过比较LLM在原始问题和释义问题上的性能差异，可以更准确地评估LLM的泛化能力。

**技术框架**：该研究的技术框架主要包括以下几个步骤：1) 选择常用的LLM基准测试数据集（如MMLU、ARC-C等）；2) 对每个基准测试数据集中的问题进行释义，生成多个语义相同但表达方式不同的问题；3) 使用原始问题和释义后的问题来评估多个LLM的性能；4) 分析LLM在原始问题和释义问题上的性能差异，并评估LLM对语言变异的鲁棒性。

**关键创新**：本研究的关键创新在于系统性地评估了LLM对语言变异的鲁棒性。通过生成基准测试问题的多种释义，并使用这些释义后的问题来评估LLM的性能，可以更准确地衡量LLM在真实场景下的泛化能力。与现有方法相比，本研究考虑了语言变异性对LLM性能的影响，从而提供了更全面的评估结果。

**关键设计**：在问题释义方面，研究人员使用了多种释义方法，包括基于规则的释义、基于模型的释义等，以确保释义的多样性和质量。在性能评估方面，研究人员使用了常用的评估指标，如准确率、F1值等。此外，研究人员还对LLM的排名进行了分析，以评估LLM在释义问题上的相对性能。

## 📊 实验亮点

实验结果表明，虽然LLM在释义输入下的排名相对稳定，但绝对有效性得分显著下降。例如，在某些基准测试中，LLM的准确率下降了10%以上。这表明LLM在处理语言变异方面存在困难，并且高基准分数可能无法完全捕捉模型对实际输入变化的鲁棒性。该研究对34个最先进的LLM进行了评估，结果具有广泛的代表性。

## 🎯 应用场景

该研究成果可应用于LLM的鲁棒性评估和改进。通过使用释义后的问题进行评估，可以更准确地了解LLM在真实场景下的性能表现，从而指导LLM的训练和优化。此外，该研究还可以促进鲁棒性感知基准测试的开发，为LLM的评估提供更可靠的依据。未来的影响在于推动LLM在实际应用中更加可靠和稳定。

## 📄 摘要（原文）

> Large Language Models (LLMs) effectiveness is usually evaluated by means of benchmarks such as MMLU, ARC-C, or HellaSwag, where questions are presented in their original wording, thus in a fixed, standardized format. However, real-world applications involve linguistic variability, requiring models to maintain their effectiveness across diverse rewordings of the same question or query. In this study, we systematically assess the robustness of LLMs to paraphrased benchmark questions and investigate whether benchmark-based evaluations provide a reliable measure of model capabilities. We systematically generate various paraphrases of all the questions across six different common benchmarks, and measure the resulting variations in effectiveness of 34 state-of-the-art LLMs, of different size and effectiveness. Our findings reveal that while LLM rankings remain relatively stable across paraphrased inputs, absolute effectiveness scores change, and decline significantly. This suggests that LLMs struggle with linguistic variability, raising concerns about their generalization abilities and evaluation methodologies. Furthermore, the observed performance drop challenges the reliability of benchmark-based evaluations, indicating that high benchmark scores may not fully capture a model's robustness to real-world input variations. We discuss the implications of these findings for LLM evaluation methodologies, emphasizing the need for robustness-aware benchmarks that better reflect practical deployment scenarios.

