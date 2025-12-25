---
layout: default
title: Neural Probe-Based Hallucination Detection for Large Language Models
---

# Neural Probe-Based Hallucination Detection for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20949" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20949v1</a>
  <a href="https://arxiv.org/pdf/2512.20949.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20949v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20949v1', 'Neural Probe-Based Hallucination Detection for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shize Liang, Hongzhi Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**提出基于神经探针的大语言模型幻觉检测框架，提升低误报率下的检测性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `幻觉检测` `神经探针` `非线性建模` `多目标学习`

## 📋 核心要点

1. 现有幻觉检测方法在高置信度下仍会出错，且依赖外部知识检索，限制了其在高风险领域的应用。
2. 该论文提出一种基于神经网络探针的幻觉检测框架，利用轻量级MLP探针进行非线性建模，提升检测性能。
3. 实验结果表明，该方法在准确率、召回率和检测能力方面显著优于现有方法，尤其是在低误报条件下。

## 📝 摘要（中文）

大型语言模型(LLMs)在文本生成和知识问答任务中表现出色，但容易产生幻觉内容，严重限制了其在高风险领域的应用。目前基于不确定性估计和外部知识检索的幻觉检测方法存在局限性，即在高置信度下仍然会产生错误内容，并且严重依赖于检索效率和知识覆盖率。相比之下，利用模型隐藏层状态的探针方法具有实时和轻量级的优势。然而，传统的线性探针难以捕捉深度语义空间中的非线性结构。为了克服这些限制，我们提出了一种基于神经网络的token级别幻觉检测框架。通过冻结语言模型参数，我们采用轻量级MLP探针来对高层隐藏状态进行非线性建模。设计了一种多目标联合损失函数，以增强检测稳定性和语义消歧。此外，我们建立了一个层位置-探针性能响应模型，使用贝叶斯优化自动搜索最佳探针插入层，并获得卓越的训练结果。在LongFact、HealthBench和TriviaQA上的实验结果表明，MLP探针在低误报条件下，在准确率、召回率和检测能力方面显著优于最先进的方法。

## 🔬 方法详解

**问题定义**：大语言模型容易产生幻觉内容，严重限制其在高风险领域的应用。现有的基于不确定性估计和外部知识检索的方法，在高置信度下仍然会产生错误内容，并且严重依赖于检索效率和知识覆盖率。传统的线性探针方法虽然轻量级，但难以捕捉深度语义空间中的非线性结构。

**核心思路**：该论文的核心思路是利用神经网络（MLP）探针，对大语言模型的高层隐藏状态进行非线性建模，从而更准确地检测幻觉。通过冻结语言模型参数，保证探针的轻量级和实时性。同时，设计多目标联合损失函数，增强检测的稳定性和语义消歧能力。

**技术框架**：整体框架包括以下几个主要模块：1) 冻结参数的大语言模型；2) 轻量级MLP探针，用于对隐藏层状态进行非线性建模；3) 多目标联合损失函数，用于训练探针；4) 层位置-探针性能响应模型，用于自动搜索最佳探针插入层。流程是：首先，将文本输入大语言模型，获取隐藏层状态；然后，将隐藏层状态输入MLP探针，得到幻觉检测结果；最后，使用多目标联合损失函数训练探针，并使用贝叶斯优化搜索最佳探针插入层。

**关键创新**：最重要的技术创新点在于使用神经网络（MLP）探针进行非线性建模，克服了传统线性探针无法捕捉深度语义空间中非线性结构的局限性。此外，多目标联合损失函数和层位置-探针性能响应模型也提升了检测的稳定性和效率。与现有方法的本质区别在于，该方法不依赖于外部知识检索，而是直接利用模型内部的隐藏层状态进行幻觉检测。

**关键设计**：关键设计包括：1) MLP探针的网络结构，例如层数、神经元数量等；2) 多目标联合损失函数的具体形式，例如各个损失项的权重；3) 贝叶斯优化的搜索空间和目标函数，用于自动搜索最佳探针插入层；4) 冻结大语言模型参数，保证探针的轻量级和实时性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20949v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20949v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20949v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在LongFact、HealthBench和TriviaQA数据集上，显著优于现有的幻觉检测方法。具体来说，在低误报条件下，该方法在准确率、召回率和检测能力方面均取得了显著提升。这表明该方法能够更有效地检测大语言模型生成的幻觉内容，并降低误报率。

## 🎯 应用场景

该研究成果可应用于各种需要高可靠性的自然语言处理任务中，例如医疗诊断、金融分析、法律咨询等。通过提高大语言模型生成内容的真实性和可靠性，可以降低其在高风险领域的应用风险，并促进其更广泛的应用。未来，该方法可以进一步扩展到其他类型的语言模型和任务中。

## 📄 摘要（原文）

> Large language models(LLMs) excel at text generation and knowledge question-answering tasks, but they are prone to generating hallucinated content, severely limiting their application in high-risk domains. Current hallucination detection methods based on uncertainty estimation and external knowledge retrieval suffer from the limitation that they still produce erroneous content at high confidence levels and rely heavily on retrieval efficiency and knowledge coverage. In contrast, probe methods that leverage the model's hidden-layer states offer real-time and lightweight advantages. However, traditional linear probes struggle to capture nonlinear structures in deep semantic spaces.To overcome these limitations, we propose a neural network-based framework for token-level hallucination detection. By freezing language model parameters, we employ lightweight MLP probes to perform nonlinear modeling of high-level hidden states. A multi-objective joint loss function is designed to enhance detection stability and semantic disambiguity. Additionally, we establish a layer position-probe performance response model, using Bayesian optimization to automatically search for optimal probe insertion layers and achieve superior training results.Experimental results on LongFact, HealthBench, and TriviaQA demonstrate that MLP probes significantly outperform state-of-the-art methods in accuracy, recall, and detection capability under low false-positive conditions.

