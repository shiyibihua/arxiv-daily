---
layout: default
title: A Comprehensive Survey on Trustworthiness in Reasoning with Large Language Models
---

# A Comprehensive Survey on Trustworthiness in Reasoning with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03871" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03871v1</a>
  <a href="https://arxiv.org/pdf/2509.03871.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03871v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03871v1', 'A Comprehensive Survey on Trustworthiness in Reasoning with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanbo Wang, Yongcan Yu, Jian Liang, Ran He

**分类**: cs.CL, cs.AI, cs.CR

**发布日期**: 2025-09-04

**备注**: 38 pages. This survey considers papers published up to June 30, 2025. Work in progress

**🔗 代码/项目**: [GITHUB](https://github.com/ybwang119/Awesome-reasoning-safety)

---

## 💡 一句话要点

**综述性研究：全面评估大型语言模型推理过程中的可信度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `可信推理` `长链思维` `人工智能安全` `模型评估`

## 📋 核心要点

1. 现有方法在理解CoT推理如何影响大型语言模型的可信度方面存在不足，缺乏全面评估。
2. 该论文对推理模型和CoT技术进行了综述，聚焦真实性、安全性、鲁棒性、公平性和隐私五个可信推理维度。
3. 研究表明，推理技术在增强模型可信度方面有潜力，但推理模型本身也可能存在安全、鲁棒性和隐私漏洞。

## 📝 摘要（中文）

长链思维(Long-CoT)推理的发展显著提升了大型语言模型在语言理解、复杂问题解决和代码生成等任务中的性能。这种范式使模型能够生成中间推理步骤，从而提高准确性和可解释性。然而，尽管取得了这些进展，但对于基于CoT的推理如何影响语言模型的可信度的全面理解仍然不足。本文综述了最近关于推理模型和CoT技术的研究，重点关注可信推理的五个核心维度：真实性、安全性、鲁棒性、公平性和隐私。对于每个方面，我们按时间顺序对最近的研究进行了清晰而结构化的概述，并详细分析了它们的方法、发现和局限性。最后还附上了未来的研究方向，以供参考和讨论。总的来说，虽然推理技术有望通过减少幻觉、检测有害内容和提高鲁棒性来增强模型的可信度，但前沿的推理模型本身在安全性、鲁棒性和隐私方面常常存在相当甚至更大的漏洞。通过综合这些见解，我们希望这项工作能够成为人工智能安全社区及时了解推理可信度最新进展的宝贵资源。相关论文的完整列表可在https://github.com/ybwang119/Awesome-reasoning-safety找到。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在推理过程中可信度评估不足的问题。现有方法缺乏对CoT推理如何影响LLM的真实性、安全性、鲁棒性、公平性和隐私等关键维度的全面理解。现有研究往往只关注单一维度，缺乏系统性的分析和整合。

**核心思路**：论文的核心思路是对现有关于LLM推理可信度的研究进行系统性的梳理和归纳，构建一个统一的框架，从真实性、安全性、鲁棒性、公平性和隐私五个维度来评估LLM的推理能力。通过分析现有方法的优缺点，为未来的研究方向提供指导。

**技术框架**：该论文采用综述研究的方法，没有提出新的技术框架。其主要工作是：
1.  收集和整理近年来关于LLM推理和CoT技术的研究论文。
2.  将这些论文按照真实性、安全性、鲁棒性、公平性和隐私五个维度进行分类。
3.  对每个维度下的研究进行详细分析，包括其方法、发现和局限性。
4.  总结现有研究的不足，并提出未来的研究方向。

**关键创新**：该论文的关键创新在于其系统性的视角和全面的分析框架。它首次将LLM推理的可信度分解为五个核心维度，并对每个维度下的研究进行了深入的分析和比较。这为研究人员提供了一个清晰的蓝图，帮助他们更好地理解LLM推理的优势和局限性，并为未来的研究方向提供指导。

**关键设计**：该论文没有涉及具体的技术设计，而是在综述的基础上，对每个维度下的研究方法进行了总结和分类。例如，在真实性方面，论文分析了各种减少幻觉的方法；在安全性方面，论文讨论了如何检测和防止LLM生成有害内容。这些总结和分类为研究人员提供了宝贵的参考。

## 📊 实验亮点

该综述论文系统地分析了大型语言模型推理的五个关键可信度维度：真实性、安全性、鲁棒性、公平性和隐私。研究揭示了现有推理模型在提升某些维度可信度的同时，可能在其他维度上存在更大的漏洞。例如，CoT技术虽然能提高准确性，但也可能放大安全和隐私风险。

## 🎯 应用场景

该研究成果可应用于人工智能安全评估、模型风险管理、以及提升大型语言模型在各个领域的可靠性。通过更全面地理解和评估LLM推理的可信度，可以促进其在医疗、金融、法律等高风险领域的安全应用，并为未来的模型改进提供指导。

## 📄 摘要（原文）

> The development of Long-CoT reasoning has advanced LLM performance across various tasks, including language understanding, complex problem solving, and code generation. This paradigm enables models to generate intermediate reasoning steps, thereby improving both accuracy and interpretability. However, despite these advancements, a comprehensive understanding of how CoT-based reasoning affects the trustworthiness of language models remains underdeveloped. In this paper, we survey recent work on reasoning models and CoT techniques, focusing on five core dimensions of trustworthy reasoning: truthfulness, safety, robustness, fairness, and privacy. For each aspect, we provide a clear and structured overview of recent studies in chronological order, along with detailed analyses of their methodologies, findings, and limitations. Future research directions are also appended at the end for reference and discussion. Overall, while reasoning techniques hold promise for enhancing model trustworthiness through hallucination mitigation, harmful content detection, and robustness improvement, cutting-edge reasoning models themselves often suffer from comparable or even greater vulnerabilities in safety, robustness, and privacy. By synthesizing these insights, we hope this work serves as a valuable and timely resource for the AI safety community to stay informed on the latest progress in reasoning trustworthiness. A full list of related papers can be found at \href{https://github.com/ybwang119/Awesome-reasoning-safety}{https://github.com/ybwang119/Awesome-reasoning-safety}.

