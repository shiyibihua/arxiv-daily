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

**关键词**: `图神经网络` `开放集分类` `分布外检测` `大语言模型` `节点分类`

## 📋 核心要点

1. 现有开放集图节点分类方法难以提供OOD样本的细粒度信息，限制了其在高风险场景的应用。
2. CFC框架利用大语言模型进行粗粒度OOD检测和标签生成，再用GNN进行细粒度分类，提升OOD识别能力。
3. 实验表明，CFC在图和文本数据上显著提升了OOD检测性能，并在图数据上实现了较高的OOD分类准确率。

## 📝 摘要（中文）

开发能够在识别分布内(ID)数据的同时检测分布外(OOD)样本的开放集分类方法，对于在开放世界场景中部署图神经网络(GNN)至关重要。现有方法通常将所有OOD样本视为单个类别，然而现实应用，特别是欺诈检测和医疗诊断等高风险场景，需要对OOD样本进行更深入的分析，包括其可能的标签。这提出了一个关键问题：能否在没有真实标签信息的情况下将OOD检测扩展到OOD分类？为了解决这个问题，我们提出了一种粗到细的开放集分类(CFC)框架，该框架利用大型语言模型(LLM)处理图数据集。CFC由三个关键组件组成：一个使用LLM提示进行OOD检测和异常值标签生成的粗分类器，一个使用粗分类器识别的OOD样本训练的基于GNN的细分类器，用于增强OOD检测和ID分类，以及通过LLM提示和后处理OOD标签实现的精细化OOD分类。与依赖合成或辅助OOD样本的方法不同，CFC采用基于其内在含义的语义OOD实例，这些实例是真正分布外的，从而提高了可解释性和实用性。实验结果表明，CFC在图和文本领域将OOD检测提高了10%，并且在图数据集上实现了高达70%的OOD分类准确率。

## 🔬 方法详解

**问题定义**：论文旨在解决图节点分类中的开放集识别问题，即区分已知类别（ID）和未知类别（OOD）。现有方法通常将所有OOD样本视为一个类别，无法提供OOD样本的细粒度信息，这在需要深入理解OOD样本的应用中（如欺诈检测）是不够的。

**核心思路**：论文的核心思路是利用大语言模型（LLM）的语义理解能力，对OOD样本进行粗粒度的分类和标签生成，然后利用这些信息训练图神经网络（GNN），从而提升GNN在OOD检测和分类方面的性能。通过LLM的先验知识，为GNN提供关于OOD样本的语义信息，弥补了传统方法仅依赖数据分布的不足。

**技术框架**：CFC框架包含三个主要阶段：1) **粗分类器**：利用LLM对图节点进行分类，并生成OOD样本的标签。通过设计合适的prompt，让LLM判断节点是否属于已知类别，并为OOD节点生成可能的标签。2) **细分类器**：使用GNN对节点进行分类，GNN的训练数据包括ID样本和由粗分类器识别并标记的OOD样本。GNN的目标是提升ID分类的准确率，并更好地区分ID和OOD样本。3) **OOD分类优化**：利用LLM对GNN的OOD分类结果进行优化，通过prompt和后处理，进一步提升OOD分类的准确率。

**关键创新**：CFC的关键创新在于将大语言模型引入到图节点开放集分类中，利用LLM的语义理解能力来辅助GNN进行OOD检测和分类。与传统方法依赖合成或辅助OOD样本不同，CFC利用LLM生成语义相关的OOD标签，提高了OOD分类的可解释性和实用性。

**关键设计**：在粗分类器中，关键在于设计有效的LLM prompt，prompt需要能够引导LLM准确判断节点是否属于已知类别，并为OOD节点生成合理的标签。在细分类器中，GNN的网络结构和训练方式需要能够有效利用LLM提供的OOD标签信息。在OOD分类优化阶段，需要设计合适的后处理方法，对LLM的输出进行修正，以提高OOD分类的准确率。

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

实验结果表明，CFC框架在图和文本数据集上显著提升了OOD检测的性能，相比现有方法提升了10%。在图数据集上，CFC实现了高达70%的OOD分类准确率，表明其能够有效识别和分类未知类型的节点。这些结果验证了CFC框架的有效性和优越性。

## 🎯 应用场景

该研究成果可应用于欺诈检测、医疗诊断、金融风控等领域。在这些领域中，识别和理解未知类型的异常行为至关重要。CFC框架能够帮助识别新型欺诈手段、罕见疾病或潜在风险，从而提高决策的准确性和效率，具有重要的实际应用价值。

## 📄 摘要（原文）

> Developing open-set classification methods capable of classifying in-distribution (ID) data while detecting out-of-distribution (OOD) samples is essential for deploying graph neural networks (GNNs) in open-world scenarios. Existing methods typically treat all OOD samples as a single class, despite real-world applications, especially high-stake settings such as fraud detection and medical diagnosis, demanding deeper insights into OOD samples, including their probable labels. This raises a critical question: can OOD detection be extended to OOD classification without true label information? To address this question, we propose a Coarse-to-Fine open-set Classification (CFC) framework that leverages large language models (LLMs) for graph datasets. CFC consists of three key components: a coarse classifier that uses LLM prompts for OOD detection and outlier label generation, a GNN-based fine classifier trained with OOD samples identified by the coarse classifier for enhanced OOD detection and ID classification, and refined OOD classification achieved through LLM prompts and post-processed OOD labels. Unlike methods that rely on synthetic or auxiliary OOD samples, CFC employs semantic OOD instances that are genuinely out-of-distribution based on their inherent meaning, improving interpretability and practical utility. Experimental results show that CFC improves OOD detection by ten percent over state-of-the-art methods on graph and text domains and achieves up to seventy percent accuracy in OOD classification on graph datasets.

