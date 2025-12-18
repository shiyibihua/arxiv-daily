---
layout: default
title: Extracting OPQRST in Electronic Health Records using Large Language Models with Reasoning
---

# Extracting OPQRST in Electronic Health Records using Large Language Models with Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01885" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01885v1</a>
  <a href="https://arxiv.org/pdf/2509.01885.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01885v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01885v1', 'Extracting OPQRST in Electronic Health Records using Large Language Models with Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhimeng Luo, Abhibha Gupta, Adam Frisch, Daqing He

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-02

---

## 💡 一句话要点

**利用大型语言模型与推理能力，从电子病历中提取OPQRST信息。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `电子病历` `信息抽取` `大型语言模型` `文本生成` `医疗人工智能`

## 📋 核心要点

1. 电子病历信息抽取面临数据复杂和非结构化的挑战，传统机器学习方法难以有效捕获关键细节。
2. 论文将信息抽取任务重构为文本生成，利用大型语言模型模拟医生推理过程，提高模型的可解释性。
3. 通过改进NER评估指标，引入语义相似度量，更准确地评估生成文本的临床相关性。

## 📝 摘要（中文）

由于电子病历(EHRs)数据的复杂性和非结构化特性，从中提取关键患者信息面临着巨大的挑战。传统的机器学习方法通常无法有效地捕获相关细节，使得临床医生难以在患者护理中有效地利用这些工具。本文提出了一种新方法，利用大型语言模型(LLMs)的能力从EHRs中提取OPQRST评估信息。我们将任务从序列标注重新定义为文本生成，使模型能够提供模仿医生认知过程的推理步骤。这种方法增强了解释性，并适应了医疗环境中标记数据的有限可用性。此外，我们通过提出对传统命名实体识别(NER)指标的修改，解决了评估机器生成文本在临床环境中准确性的挑战，包括整合语义相似性度量(如BERT Score)，以评估生成文本与原始记录的临床意图之间的一致性。我们的贡献展示了人工智能在医疗保健领域的显著进步，提供了一种可扩展的解决方案，提高了从EHRs中提取信息的准确性和可用性，从而帮助临床医生做出更明智的决策，并改善患者的护理结果。

## 🔬 方法详解

**问题定义**：论文旨在解决从电子病历（EHRs）中准确提取OPQRST评估信息的问题。现有方法，特别是传统的机器学习方法，难以有效处理EHRs中复杂且非结构化的数据，导致信息提取的准确性和效率低下，无法满足临床医生的需求。

**核心思路**：论文的核心思路是将OPQRST信息抽取任务从传统的序列标注问题转化为文本生成问题。通过让大型语言模型（LLMs）生成类似于医生进行诊断推理的文本，不仅可以提取信息，还能提供推理过程，从而提高模型的可解释性和可靠性。

**技术框架**：该方法的核心是利用大型语言模型（LLMs）进行文本生成。首先，将EHRs数据输入到LLM中；然后，LLM根据输入生成包含OPQRST信息的文本，并提供相应的推理步骤；最后，使用改进的NER评估指标（包括语义相似性度量）评估生成文本的质量。

**关键创新**：该方法最重要的创新点在于将信息抽取任务转化为文本生成任务，并利用LLM的推理能力来提高信息抽取的准确性和可解释性。此外，针对临床文本的特殊性，论文还提出了改进的NER评估指标，更准确地评估生成文本的临床相关性。

**关键设计**：论文的关键设计包括：1) 使用大型语言模型作为文本生成器；2) 设计合适的prompt，引导LLM生成包含OPQRST信息的文本；3) 采用BERT Score等语义相似性度量来评估生成文本与原始记录的临床意图之间的一致性；4) 对传统的NER指标进行修改，使其更适合评估临床文本的生成质量。具体参数设置和网络结构等细节在论文中可能未详细描述，属于未知信息。

## 📊 实验亮点

论文通过将信息抽取任务转化为文本生成任务，并利用大型语言模型的推理能力，显著提高了从电子病历中提取OPQRST信息的准确性和可解释性。具体性能数据和对比基线在摘要中未明确提及，属于未知信息。但论文强调了该方法在医疗保健领域的显著进步。

## 🎯 应用场景

该研究成果可应用于智能医疗领域，辅助临床医生快速准确地从电子病历中提取关键信息，提高诊断效率和准确性，减少医疗错误。未来，该方法有望扩展到其他类型的医疗文本信息抽取任务，并与其他医疗AI系统集成，构建更智能化的医疗服务。

## 📄 摘要（原文）

> The extraction of critical patient information from Electronic Health Records (EHRs) poses significant challenges due to the complexity and unstructured nature of the data. Traditional machine learning approaches often fail to capture pertinent details efficiently, making it difficult for clinicians to utilize these tools effectively in patient care. This paper introduces a novel approach to extracting the OPQRST assessment from EHRs by leveraging the capabilities of Large Language Models (LLMs). We propose to reframe the task from sequence labeling to text generation, enabling the models to provide reasoning steps that mimic a physician's cognitive processes. This approach enhances interpretability and adapts to the limited availability of labeled data in healthcare settings. Furthermore, we address the challenge of evaluating the accuracy of machine-generated text in clinical contexts by proposing a modification to traditional Named Entity Recognition (NER) metrics. This includes the integration of semantic similarity measures, such as the BERT Score, to assess the alignment between generated text and the clinical intent of the original records. Our contributions demonstrate a significant advancement in the use of AI in healthcare, offering a scalable solution that improves the accuracy and usability of information extraction from EHRs, thereby aiding clinicians in making more informed decisions and enhancing patient care outcomes.

