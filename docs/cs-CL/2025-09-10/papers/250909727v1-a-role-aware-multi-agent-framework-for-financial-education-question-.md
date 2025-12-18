---
layout: default
title: A Role-Aware Multi-Agent Framework for Financial Education Question Answering with LLMs
---

# A Role-Aware Multi-Agent Framework for Financial Education Question Answering with LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09727" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09727v1</a>
  <a href="https://arxiv.org/pdf/2509.09727.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09727v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09727v1', 'A Role-Aware Multi-Agent Framework for Financial Education Question Answering with LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andy Zhu, Yingjun Du

**分类**: cs.CL, cs.CE

**发布日期**: 2025-09-10

**备注**: 8 pages, 6 figures, Underreview

---

## 💡 一句话要点

**提出基于角色感知的多智能体框架，提升LLM在金融教育问答中的准确性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `金融教育` `问答系统` `多智能体` `大型语言模型` `检索增强生成`

## 📋 核心要点

1. 现有LLM在金融问答中缺乏领域知识和多步推理能力，难以满足专业需求。
2. 提出多智能体框架，通过角色扮演和检索增强，提升LLM在金融领域的问答能力。
3. 实验表明，该框架显著提升了金融问答的准确率，并降低了对大型模型的依赖。

## 📝 摘要（中文）

本文提出了一种多智能体框架，旨在提升大型语言模型（LLM）在金融教育问答中的表现。现有LLM方法难以捕捉金融问题求解所需的细致和专业的推理。该框架利用基于角色的提示，包含一个基础生成器、一个证据检索器和一个专家审查器，通过单次迭代生成精炼的答案。在Study.com提供的3532个金融教育问题上进行了评估，并使用检索增强生成（RAG）从6本金融教科书中获取上下文证据。实验结果表明，基于评论的改进使答案准确率比零样本思维链基线提高了6.6-8.3%，Gemini-2.0-Flash表现最佳。此外，该方法使GPT-4o-mini的性能与金融领域微调的FinGPT-mt_Llama3-8B_LoRA相当。结果表明，这是一种经济高效的增强金融问答的方法，并为多智能体金融LLM系统的进一步研究提供了见解。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在金融教育问答中表现不佳的问题。现有方法难以处理金融领域复杂的多步量化推理、专业术语理解以及真实场景应用，导致答案准确率较低。

**核心思路**：论文的核心思路是利用多智能体框架，模拟不同角色的专家协同工作，提升LLM的金融问答能力。通过角色扮演和检索增强，使LLM能够更好地理解和处理金融领域的问题。

**技术框架**：该框架包含三个主要模块：基础生成器（Base Generator）、证据检索器（Evidence Retriever）和专家审查器（Expert Reviewer）。基础生成器负责生成初始答案；证据检索器利用RAG从金融教科书中检索相关证据；专家审查器根据检索到的证据和领域知识，对初始答案进行审查和改进，最终生成精炼的答案。整个流程采用单次迭代的方式进行。

**关键创新**：该框架的关键创新在于引入了基于角色的提示（role-based prompting）和专家审查机制。通过角色扮演，使LLM能够更好地理解问题的背景和要求，并从不同角度进行思考。专家审查机制则能够有效地纠正LLM的错误，提高答案的准确性和可靠性。

**关键设计**：论文使用了Study.com提供的3532个金融教育问题作为数据集。证据检索器使用了6本金融教科书作为知识来源。在提示工程方面，针对每个智能体都设计了特定的角色提示，以引导LLM更好地完成任务。具体参数设置和损失函数等技术细节在论文中未详细描述，属于未知信息。

## 📊 实验亮点

实验结果表明，该框架在金融教育问答任务中取得了显著的性能提升。与零样本思维链基线相比，答案准确率提高了6.6-8.3%，Gemini-2.0-Flash表现最佳。更重要的是，该方法使GPT-4o-mini的性能与金融领域微调的FinGPT-mt_Llama3-8B_LoRA模型相当，表明该框架具有良好的成本效益。

## 🎯 应用场景

该研究成果可应用于在线金融教育平台，为学生提供更准确、更专业的金融知识问答服务。此外，该框架也可扩展到其他专业领域，例如医疗、法律等，提升LLM在这些领域的应用价值。未来，该研究有望推动金融智能客服、智能投顾等领域的发展。

## 📄 摘要（原文）

> Question answering (QA) plays a central role in financial education, yet existing large language model (LLM) approaches often fail to capture the nuanced and specialized reasoning required for financial problem-solving. The financial domain demands multistep quantitative reasoning, familiarity with domain-specific terminology, and comprehension of real-world scenarios. We present a multi-agent framework that leverages role-based prompting to enhance performance on domain-specific QA. Our framework comprises a Base Generator, an Evidence Retriever, and an Expert Reviewer agent that work in a single-pass iteration to produce a refined answer. We evaluated our framework on a set of 3,532 expert-designed finance education questions from Study.com, an online learning platform. We leverage retrieval-augmented generation (RAG) for contextual evidence from 6 finance textbooks and prompting strategies for a domain-expert reviewer. Our experiments indicate that critique-based refinement improves answer accuracy by 6.6-8.3% over zero-shot Chain-of-Thought baselines, with the highest performance from Gemini-2.0-Flash. Furthermore, our method enables GPT-4o-mini to achieve performance comparable to the finance-tuned FinGPT-mt_Llama3-8B_LoRA. Our results show a cost-effective approach to enhancing financial QA and offer insights for further research in multi-agent financial LLM systems.

