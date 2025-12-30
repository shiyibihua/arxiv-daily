---
layout: default
title: "The Gaining Paths to Investment Success: Information-Driven LLM Graph Reasoning for Venture Capital Prediction"
---

# The Gaining Paths to Investment Success: Information-Driven LLM Graph Reasoning for Venture Capital Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23489" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23489v1</a>
  <a href="https://arxiv.org/pdf/2512.23489.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23489v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23489v1', 'The Gaining Paths to Investment Success: Information-Driven LLM Graph Reasoning for Venture Capital Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyu Pei, Zhongyang Liu, Xiangyi Xiao, Xiaocong Du, Haipeng Zhang, Kunpeng Zhang, Suting Hong

**分类**: cs.AI

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**MIRAGE-VC：信息增益驱动的LLM图推理，用于风险投资预测**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `风险投资预测` `图神经网络` `大型语言模型` `信息增益` `图推理`

## 📋 核心要点

1. 现有方法难以有效利用复杂关系证据进行风险投资预测，缺乏显式推理能力。
2. MIRAGE-VC通过信息增益驱动的路径检索和多智能体架构，实现对投资网络的有效推理。
3. 实验表明，MIRAGE-VC在风险投资预测任务上显著提升了F1和PrecisionAt5指标。

## 📝 摘要（中文）

风险投资(VC)中，多数投资失败，少数带来超额回报。准确预测初创公司成功需要综合复杂的关联证据，包括公司披露信息、投资者业绩记录和投资网络结构，并通过显式推理形成连贯、可解释的投资论点。传统机器学习和图神经网络都缺乏这种推理能力。大型语言模型(LLM)具有强大的推理能力，但与图存在模态不匹配。现有的图-LLM方法主要针对图内任务，而VC预测是图外任务，目标存在于网络之外。核心挑战是选择最大化外部目标预测性能的图路径，同时实现逐步推理。我们提出了MIRAGE-VC，一个多视角检索增强生成框架，解决了路径爆炸（数千条候选路径使LLM上下文不堪重负）和异构证据融合（不同的初创公司需要不同的分析重点）两个难题。我们的信息增益驱动的路径检索器迭代地选择高价值邻居，将投资网络提炼成紧凑的链条以进行显式推理。一个多智能体架构通过基于公司属性的可学习门控机制整合了三个证据流。在严格的反泄露控制下，MIRAGE-VC实现了+5.0%的F1和+16.6%的PrecisionAt5，并为推荐和风险评估等其他图外预测任务提供了启示。

## 🔬 方法详解

**问题定义**：风险投资预测是一个典型的图外预测问题，需要利用公司信息、投资者信息以及投资网络结构等复杂关系证据来预测初创公司的成功率。现有方法，如传统机器学习和图神经网络，难以进行有效的推理，无法充分利用这些关系信息。大型语言模型虽然具有强大的推理能力，但与图数据存在模态不匹配的问题。

**核心思路**：MIRAGE-VC的核心思路是利用信息增益来指导图路径的检索，从而将复杂的投资网络提炼成紧凑的、具有高信息量的路径，然后利用大型语言模型对这些路径进行推理，最终实现对初创公司成功率的预测。这种方法能够有效地解决路径爆炸问题，并能够根据不同的初创公司选择不同的分析重点。

**技术框架**：MIRAGE-VC的整体架构是一个多视角检索增强生成框架，主要包含两个模块：信息增益驱动的路径检索器和多智能体架构。路径检索器负责从投资网络中选择高价值的邻居，构建紧凑的推理路径。多智能体架构负责整合来自不同证据流的信息，并利用可学习的门控机制来调整不同证据流的权重。

**关键创新**：MIRAGE-VC最重要的技术创新点在于其信息增益驱动的路径检索器。该检索器能够迭代地选择高价值的邻居，从而将复杂的投资网络提炼成紧凑的链条，避免了路径爆炸问题。与现有方法相比，MIRAGE-VC能够更有效地利用图结构信息，并能够进行显式的推理。

**关键设计**：MIRAGE-VC的关键设计包括：1) 使用信息增益作为路径选择的指标；2) 设计了一个多智能体架构来整合来自不同证据流的信息；3) 使用可学习的门控机制来调整不同证据流的权重。具体的参数设置、损失函数和网络结构等技术细节在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23489v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23489v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23489v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

MIRAGE-VC在风险投资预测任务上取得了显著的性能提升。在严格的反泄露控制下，MIRAGE-VC的F1值提高了5.0%，PrecisionAt5提高了16.6%。这些结果表明，MIRAGE-VC能够有效地利用图结构信息和大型语言模型的推理能力，从而提高风险投资预测的准确性。

## 🎯 应用场景

MIRAGE-VC的研究成果可以应用于风险投资领域的项目评估、投资组合管理和风险控制。此外，该方法还可以推广到其他图外预测任务，如推荐系统和风险评估，具有广泛的应用前景和实际价值。通过提升投资决策的准确性，有望促进创新和经济发展。

## 📄 摘要（原文）

> Most venture capital (VC) investments fail, while a few deliver outsized returns. Accurately predicting startup success requires synthesizing complex relational evidence, including company disclosures, investor track records, and investment network structures, through explicit reasoning to form coherent, interpretable investment theses. Traditional machine learning and graph neural networks both lack this reasoning capability. Large language models (LLMs) offer strong reasoning but face a modality mismatch with graphs. Recent graph-LLM methods target in-graph tasks where answers lie within the graph, whereas VC prediction is off-graph: the target exists outside the network. The core challenge is selecting graph paths that maximize predictor performance on an external objective while enabling step-by-step reasoning. We present MIRAGE-VC, a multi-perspective retrieval-augmented generation framework that addresses two obstacles: path explosion (thousands of candidate paths overwhelm LLM context) and heterogeneous evidence fusion (different startups need different analytical emphasis). Our information-gain-driven path retriever iteratively selects high-value neighbors, distilling investment networks into compact chains for explicit reasoning. A multi-agent architecture integrates three evidence streams via a learnable gating mechanism based on company attributes. Under strict anti-leakage controls, MIRAGE-VC achieves +5.0% F1 and +16.6% PrecisionAt5, and sheds light on other off-graph prediction tasks such as recommendation and risk assessment. Code: https://anonymous.4open.science/r/MIRAGE-VC-323F.

