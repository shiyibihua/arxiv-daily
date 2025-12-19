---
layout: default
title: Coarse-to-Fine Open-Set Graph Node Classification with Large Language Models
---

# Coarse-to-Fine Open-Set Graph Node Classification with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16244" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16244v1</a>
  <a href="https://arxiv.org/pdf/2512.16244.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16244v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16244v1', 'Coarse-to-Fine Open-Set Graph Node Classification with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xueqi Ma, Xingjun Ma, Sarah Monazam Erfani, Danilo Mandic, James Bailey

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-18

**备注**: Accepted to AAAI 2026

---

## 💡 一句话要点

**提出CFC框架，利用大语言模型实现图节点开放集分类与细粒度OOD识别。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `开放集分类` `图神经网络` `大语言模型` `分布外检测` `OOD分类`

## 📋 核心要点

1. 现有开放集图节点分类方法将所有OOD样本视为一类，缺乏对OOD样本的细粒度理解。
2. CFC框架利用大语言模型进行粗粒度OOD检测和标签生成，再用GNN进行细粒度分类，提升OOD识别能力。
3. 实验表明，CFC在图和文本数据上OOD检测性能提升10%，OOD分类准确率在图数据上高达70%。

## 📝 摘要（中文）

开发能够对分布内(ID)数据进行分类，同时检测分布外(OOD)样本的开放集分类方法，对于在开放世界场景中部署图神经网络(GNN)至关重要。现有方法通常将所有OOD样本视为单个类别，然而现实应用，尤其是在欺诈检测和医疗诊断等高风险环境中，需要对OOD样本进行更深入的分析，包括其可能的标签。这提出了一个关键问题：能否在没有真实标签信息的情况下，将OOD检测扩展到OOD分类？为了解决这个问题，我们提出了一个粗到细的开放集分类(CFC)框架，该框架利用大型语言模型(LLM)处理图数据集。CFC由三个关键组件组成：一个粗分类器，它使用LLM提示进行OOD检测和异常值标签生成；一个基于GNN的细分类器，该分类器使用粗分类器识别的OOD样本进行训练，以增强OOD检测和ID分类；以及通过LLM提示和后处理OOD标签实现的精细化OOD分类。与依赖合成或辅助OOD样本的方法不同，CFC采用基于其内在含义的语义OOD实例，这些实例是真正分布外的，从而提高了可解释性和实用性。实验结果表明，CFC在图和文本领域将OOD检测提高了10%，并且在图数据集上的OOD分类准确率高达70%。

## 🔬 方法详解

**问题定义**：现有图神经网络的开放集分类方法主要关注区分已知类别和未知类别（OOD检测），但忽略了对OOD样本的进一步分类。在实际应用中，例如欺诈检测或医疗诊断，仅仅识别出异常样本是不够的，还需要了解这些异常样本可能属于的类别。因此，论文旨在解决如何在没有OOD样本真实标签的情况下，对OOD样本进行分类的问题。

**核心思路**：论文的核心思路是利用大语言模型（LLM）的语义理解能力，对OOD样本进行粗粒度的分类，生成伪标签，然后利用这些伪标签训练图神经网络，从而实现细粒度的OOD分类。这种“粗到细”的方法能够充分利用LLM的先验知识和GNN的图结构学习能力。

**技术框架**：CFC框架包含三个主要阶段：1) **粗分类器**：使用LLM对图节点进行分类，同时检测OOD样本，并为OOD样本生成伪标签。LLM通过特定的prompt进行引导，例如“这个节点最可能属于哪个类别？”。2) **细分类器**：使用GNN，结合原始ID数据和带有伪标签的OOD数据进行训练，提升ID分类和OOD检测的性能。3) **OOD分类优化**：使用LLM对GNN的OOD分类结果进行优化，通过prompt和后处理，进一步提升OOD分类的准确率。

**关键创新**：CFC框架的关键创新在于：1) 利用LLM进行OOD样本的伪标签生成，避免了依赖合成或辅助OOD样本的传统方法，从而提高了OOD样本的语义相关性和可解释性。2) 提出了一种粗到细的分类框架，将LLM的语义理解能力和GNN的图结构学习能力相结合，实现了更准确的OOD分类。

**关键设计**：在粗分类器阶段，LLM的prompt设计至关重要，需要根据具体的图数据集和任务进行调整。在细分类器阶段，GNN的选择和训练策略需要仔细考虑，以平衡ID分类和OOD检测的性能。OOD分类优化阶段，LLM的prompt和后处理规则也需要根据实验结果进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16244v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16244v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16244v1/ood-prompt.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，CFC框架在图和文本领域上的OOD检测性能比现有方法提高了10%。在图数据集上，CFC框架的OOD分类准确率高达70%。这些结果表明，CFC框架能够有效地利用LLM和GNN的优势，实现更准确的开放集分类。

## 🎯 应用场景

该研究成果可应用于欺诈检测、医疗诊断、金融风控等领域。在这些场景中，识别异常行为或病例至关重要，而对异常情况进行分类可以帮助专家更快地定位问题并采取相应的措施。此外，该方法还可以用于网络安全领域，识别和分类恶意软件或网络攻击。

## 📄 摘要（原文）

> Developing open-set classification methods capable of classifying in-distribution (ID) data while detecting out-of-distribution (OOD) samples is essential for deploying graph neural networks (GNNs) in open-world scenarios. Existing methods typically treat all OOD samples as a single class, despite real-world applications, especially high-stake settings such as fraud detection and medical diagnosis, demanding deeper insights into OOD samples, including their probable labels. This raises a critical question: can OOD detection be extended to OOD classification without true label information? To address this question, we propose a Coarse-to-Fine open-set Classification (CFC) framework that leverages large language models (LLMs) for graph datasets. CFC consists of three key components: a coarse classifier that uses LLM prompts for OOD detection and outlier label generation, a GNN-based fine classifier trained with OOD samples identified by the coarse classifier for enhanced OOD detection and ID classification, and refined OOD classification achieved through LLM prompts and post-processed OOD labels. Unlike methods that rely on synthetic or auxiliary OOD samples, CFC employs semantic OOD instances that are genuinely out-of-distribution based on their inherent meaning, improving interpretability and practical utility. Experimental results show that CFC improves OOD detection by ten percent over state-of-the-art methods on graph and text domains and achieves up to seventy percent accuracy in OOD classification on graph datasets.

