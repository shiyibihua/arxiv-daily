---
layout: default
title: Assessing Classical Machine Learning and Transformer-based Approaches for Detecting AI-Generated Research Text
---

# Assessing Classical Machine Learning and Transformer-based Approaches for Detecting AI-Generated Research Text

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20375" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20375v1</a>
  <a href="https://arxiv.org/pdf/2509.20375.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20375v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20375v1', 'Assessing Classical Machine Learning and Transformer-based Approaches for Detecting AI-Generated Research Text')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sharanya Parimanoharan, Ruwan D. Nawarathna

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-20

---

## 💡 一句话要点

**评估经典机器学习与Transformer模型在AI生成研究文本检测中的性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `AI文本检测` `自然语言处理` `机器学习` `Transformer模型` `DistilBERT` `学术诚信` `内容审核`

## 📋 核心要点

1. 大型语言模型模糊了人类与AI生成文本的界限，对学术诚信和信息安全构成挑战。
2. 论文对比了经典机器学习和Transformer模型，用于区分AI生成的学术摘要和人类撰写的摘要。
3. 实验表明DistilBERT模型表现最佳，而模型集成未能显著提升性能，表明模型表示的重要性。

## 📝 摘要（中文）

随着ChatGPT等大型语言模型（LLM）的快速普及，人类撰写文本和AI生成文本之间的界限变得模糊，引发了关于学术诚信、知识产权和虚假信息传播的紧迫问题。因此，需要可靠的AI文本检测技术来进行公平评估，以维护人类创作的真实性，并在数字通信中培养信任。本研究探讨了当前机器学习（ML）方法区分ChatGPT-3.5生成的文本与人类撰写文本的能力，使用了包含250对来自广泛研究主题的摘要的标记数据集。我们测试并比较了经典方法（配备经典词袋模型、词性标注和TF-IDF特征的Logistic回归）和基于Transformer的方法（使用N-gram增强的BERT、DistilBERT、带有轻量级自定义分类器的BERT以及基于LSTM的N-gram模型）。我们旨在评估每种模型在检测AI生成研究文本方面的性能，并测试这些模型的集成是否能优于任何单一检测器。结果表明，DistilBERT实现了总体最佳性能，而Logistic回归和BERT-Custom提供了可靠且平衡的替代方案；LSTM和BERT-N-gram方法表现较差。三个最佳模型的最大投票集成未能超过DistilBERT本身，突出了单个基于Transformer的表示优于单纯的模型多样性。通过全面评估这些AI文本检测方法的优缺点，这项工作为更强大的Transformer框架奠定了基础，这些框架具有更大、更丰富的数据集，以跟上不断改进的生成式AI模型的步伐。

## 🔬 方法详解

**问题定义**：论文旨在解决如何有效区分AI（特别是ChatGPT-3.5）生成的学术研究文本与人类撰写的学术研究文本的问题。现有方法在面对日益强大的生成式AI模型时，区分能力不足，容易造成学术不端行为和虚假信息传播。

**核心思路**：论文的核心思路是比较和评估多种机器学习方法，包括传统的机器学习方法和基于Transformer的深度学习方法，在AI生成文本检测任务中的性能。通过对比不同方法的优缺点，为构建更鲁棒的AI文本检测系统提供指导。论文还尝试了模型集成的方法，以期提高检测性能。

**技术框架**：论文的技术框架主要包括以下几个阶段：1) 数据集构建：收集包含人类撰写和ChatGPT-3.5生成的学术摘要的数据集。2) 特征提取：对于经典机器学习方法，提取词袋模型、词性标注和TF-IDF等特征；对于Transformer模型，使用预训练的BERT、DistilBERT等模型提取文本表示。3) 模型训练：训练Logistic回归、BERT、DistilBERT、LSTM等模型。4) 模型评估：使用准确率、精确率、召回率等指标评估模型的性能。5) 模型集成：尝试将多个模型进行集成，以提高检测性能。

**关键创新**：论文的关键创新在于对多种AI文本检测方法进行了全面的比较和评估，包括经典机器学习方法和基于Transformer的深度学习方法。此外，论文还尝试了模型集成的方法，并分析了模型集成对检测性能的影响。实验结果表明，DistilBERT模型在AI生成文本检测任务中表现最佳，而模型集成未能显著提升性能。

**关键设计**：论文的关键设计包括：1) 使用包含250对学术摘要的数据集进行实验。2) 采用多种特征提取方法，包括词袋模型、词性标注、TF-IDF和预训练的Transformer模型。3) 训练多种机器学习模型，包括Logistic回归、BERT、DistilBERT和LSTM。4) 使用准确率、精确率、召回率等指标评估模型的性能。5) 尝试了最大投票集成方法，将多个模型进行集成。

## 📊 实验亮点

实验结果表明，DistilBERT模型在AI生成文本检测任务中表现最佳，优于其他经典机器学习方法和基于BERT的模型。Logistic回归和BERT-Custom模型也提供了可靠的替代方案。然而，模型集成（最大投票集成）未能超越DistilBERT的性能，表明单个强大的Transformer模型表示比简单的模型多样性更重要。

## 🎯 应用场景

该研究成果可应用于学术诚信检测、内容审核、虚假信息识别等领域。通过自动检测AI生成的文本，可以帮助维护学术研究的真实性和可靠性，防止虚假信息的传播，并促进负责任的AI技术应用。未来，该技术可集成到学术出版平台、社交媒体平台等，以提高内容质量和用户信任度。

## 📄 摘要（原文）

> The rapid adoption of large language models (LLMs) such as ChatGPT has blurred the line between human and AI-generated texts, raising urgent questions about academic integrity, intellectual property, and the spread of misinformation. Thus, reliable AI-text detection is needed for fair assessment to safeguard human authenticity and cultivate trust in digital communication. In this study, we investigate how well current machine learning (ML) approaches can distinguish ChatGPT-3.5-generated texts from human-written texts employing a labeled data set of 250 pairs of abstracts from a wide range of research topics. We test and compare both classical (Logistic Regression armed with classical Bag-of-Words, POS, and TF-IDF features) and transformer-based (BERT augmented with N-grams, DistilBERT, BERT with a lightweight custom classifier, and LSTM-based N-gram models) ML detection techniques. As we aim to assess each model's performance in detecting AI-generated research texts, we also aim to test whether an ensemble of these models can outperform any single detector. Results show DistilBERT achieves the overall best performance, while Logistic Regression and BERT-Custom offer solid, balanced alternatives; LSTM- and BERT-N-gram approaches lag. The max voting ensemble of the three best models fails to surpass DistilBERT itself, highlighting the primacy of a single transformer-based representation over mere model diversity. By comprehensively assessing the strengths and weaknesses of these AI-text detection approaches, this work lays a foundation for more robust transformer frameworks with larger, richer datasets to keep pace with ever-improving generative AI models.

