---
layout: default
title: Evaluating the Limits of Large Language Models in Multilingual Legal Reasoning
---

# Evaluating the Limits of Large Language Models in Multilingual Legal Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22472" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22472v1</a>
  <a href="https://arxiv.org/pdf/2509.22472.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22472v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22472v1', 'Evaluating the Limits of Large Language Models in Multilingual Legal Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Antreas Ioannou, Andreas Shiamishis, Nora Hollenstein, Nezihe Merve Gürel

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-26

**备注**: 39 pages, 36 figures. Code and evaluation pipeline available at https://github.com/RobustML-Lab/Legal-Multilingual-Evaluation-of-LLMs

---

## 💡 一句话要点

**评估大语言模型在多语言法律推理中的局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `法律推理` `多语言` `对抗鲁棒性` `基准测试` `LLM评估` `法律科技`

## 📋 核心要点

1. 现有大语言模型在多语言、跨司法管辖区的法律推理任务中表现不足，尤其是在对抗性攻击下。
2. 论文提出一个开源、模块化的评估流程，用于多语言、任务多样的法律任务基准测试，评估LLM的性能。
3. 实验表明，法律任务对LLM构成挑战，且模型在不同语言和对抗性攻击下的表现存在差异。

## 📝 摘要（中文）

在大语言模型（LLMs）主导的时代，理解它们的能力和局限性至关重要，尤其是在法律等高风险领域。尽管Meta的LLaMA、OpenAI的ChatGPT、Google的Gemini、DeepSeek和其他新兴模型越来越多地被整合到法律工作流程中，但它们在多语言、跨司法管辖区和对抗性环境中的表现仍未得到充分探索。本研究评估了LLaMA和Gemini在多语言法律和非法律基准上的表现，并通过字符和单词级别的扰动评估了它们在法律任务中的对抗鲁棒性。我们使用LLM-as-a-Judge方法进行与人类对齐的评估。此外，我们提出了一个开源的、模块化的评估流程，旨在支持对任意LLM和数据集组合进行多语言、任务多样化的基准测试，特别关注法律任务，包括分类、总结、开放性问题和一般推理。我们的研究结果证实，法律任务对LLM提出了重大挑战，在LEXam等法律推理基准上的准确率通常低于50%，而在XNLI等通用任务上的准确率超过70%。此外，虽然英语通常产生更稳定的结果，但并不总是能带来更高的准确率。提示敏感性和对抗脆弱性也持续存在于各种语言中。最后，我们发现了一种语言的性能与其与英语的句法相似性之间存在相关性。我们还观察到LLaMA比Gemini弱，后者在同一任务中平均有约24个百分点的优势。尽管较新的LLM有所改进，但在关键的多语言法律应用中可靠地部署它们仍然存在挑战。

## 🔬 方法详解

**问题定义**：论文旨在评估大型语言模型（LLMs）在多语言法律推理任务中的性能和局限性。现有方法缺乏对LLMs在法律领域的深入评估，尤其是在多语言环境、跨司法管辖区以及对抗性攻击下的鲁棒性。现有评估方法难以全面衡量LLMs在法律领域的实际应用能力。

**核心思路**：论文的核心思路是通过构建多语言法律基准测试，并采用LLM-as-a-Judge的评估方法，全面评估LLMs在法律任务中的性能。通过对抗性攻击，分析LLMs的鲁棒性。通过分析不同语言的表现，揭示语言特性对LLMs性能的影响。

**技术框架**：该研究的技术框架主要包括以下几个模块：1) 多语言法律基准测试数据集的构建，涵盖分类、总结、开放性问题和一般推理等任务；2) 基于LLM-as-a-Judge的评估方法，利用LLM对其他LLM的输出进行评估，以实现与人类对齐的评估；3) 对抗性攻击模块，通过字符和单词级别的扰动，评估LLMs的鲁棒性；4) 性能分析模块，分析LLMs在不同语言和任务上的表现，并探究影响性能的因素。

**关键创新**：论文的关键创新在于：1) 构建了一个开源、模块化的多语言法律基准测试平台，方便研究人员进行LLM的评估和比较；2) 采用LLM-as-a-Judge的评估方法，提高了评估的效率和一致性；3) 深入分析了LLMs在多语言法律任务中的性能瓶颈，为未来的研究方向提供了指导。

**关键设计**：论文的关键设计包括：1) 多语言法律基准测试数据集的选取和构建，保证了数据集的多样性和代表性；2) 对抗性攻击策略的设计，包括字符级别和单词级别的扰动，以模拟真实的对抗性环境；3) LLM-as-a-Judge评估方法的具体实现，包括提示词的设计和评估指标的选择。

## 📊 实验亮点

实验结果表明，LLM在法律任务上的准确率通常低于50%，远低于通用任务的70%。Gemini的表现优于LLaMA，平均有24个百分点的优势。研究还发现，语言的句法结构与英语的相似性与LLM在该语言上的性能相关。对抗性攻击显著降低了LLM的性能，表明其鲁棒性有待提高。

## 🎯 应用场景

该研究成果可应用于法律咨询、合同审查、法律文书生成等领域，有助于提高法律服务的效率和质量。通过评估LLM在多语言法律任务中的性能，可以为开发更可靠、更智能的法律AI系统提供指导，促进法律科技的发展。

## 📄 摘要（原文）

> In an era dominated by Large Language Models (LLMs), understanding their capabilities and limitations, especially in high-stakes fields like law, is crucial. While LLMs such as Meta's LLaMA, OpenAI's ChatGPT, Google's Gemini, DeepSeek, and other emerging models are increasingly integrated into legal workflows, their performance in multilingual, jurisdictionally diverse, and adversarial contexts remains insufficiently explored. This work evaluates LLaMA and Gemini on multilingual legal and non-legal benchmarks, and assesses their adversarial robustness in legal tasks through character and word-level perturbations. We use an LLM-as-a-Judge approach for human-aligned evaluation. We moreover present an open-source, modular evaluation pipeline designed to support multilingual, task-diverse benchmarking of any combination of LLMs and datasets, with a particular focus on legal tasks, including classification, summarization, open questions, and general reasoning. Our findings confirm that legal tasks pose significant challenges for LLMs with accuracies often below 50% on legal reasoning benchmarks such as LEXam, compared to over 70% on general-purpose tasks like XNLI. In addition, while English generally yields more stable results, it does not always lead to higher accuracy. Prompt sensitivity and adversarial vulnerability is also shown to persist across languages. Finally, a correlation is found between the performance of a language and its syntactic similarity to English. We also observe that LLaMA is weaker than Gemini, with the latter showing an average advantage of about 24 percentage points across the same task. Despite improvements in newer LLMs, challenges remain in deploying them reliably for critical, multilingual legal applications.

