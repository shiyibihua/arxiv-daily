---
layout: default
title: Isolating Culture Neurons in Multilingual Large Language Models
---

# Isolating Culture Neurons in Multilingual Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02241" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02241v2</a>
  <a href="https://arxiv.org/pdf/2508.02241.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02241v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02241v2', 'Isolating Culture Neurons in Multilingual Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Danial Namazifard, Lukas Galke Poech

**分类**: cs.CL

**发布日期**: 2025-08-04 (更新: 2025-11-11)

**备注**: Accepted at IJCNLP-AACL 2025

**🔗 代码/项目**: [GITHUB](https://github.com/namazifard/Culture_Neurons)

---

## 💡 一句话要点

**提出一种方法以识别多语言大语言模型中的文化神经元**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言模型` `文化神经元` `语言特定神经元` `MUREL数据集` `公平性` `包容性` `人工智能`

## 📋 核心要点

1. 现有方法未能明确识别多语言大语言模型中文化信息的编码位置和方式。
2. 论文提出通过识别语言特定神经元的方法，定位和隔离文化特定神经元，探讨其与语言神经元的关系。
3. 实验结果显示，LLMs在不同神经元群体中编码文化，且文化神经元可独立调节，具有重要的社会影响。

## 📝 摘要（中文）

语言与文化密切相关，但多语言大语言模型中如何编码文化仍不明确。本文基于已有的方法，识别语言特定神经元，定位和隔离文化特定神经元，清晰区分其与语言特定神经元的重叠与交互。为此，我们引入了MUREL，一个涵盖六种不同文化的8500万标记的精心策划数据集。我们的定位和干预实验表明，LLMs在不同的神经元群体中编码不同文化，主要集中在上层，并且这些文化神经元可以在很大程度上独立于语言特定神经元或其他文化特定神经元进行调节。这些发现表明，多语言模型中的文化知识和倾向可以被选择性地隔离和编辑，对公平性、包容性和一致性具有重要影响。

## 🔬 方法详解

**问题定义**：本文旨在解决多语言大语言模型中文化信息的编码问题，现有方法未能有效识别文化特定神经元与语言特定神经元的关系。

**核心思路**：通过构建MUREL数据集，利用已有的语言特定神经元识别方法，定位和隔离文化特定神经元，探讨其独立性和交互性。

**技术框架**：整体流程包括数据集构建、神经元定位、干预实验三个主要阶段，首先通过MUREL数据集进行训练，然后识别文化神经元，最后进行调节实验。

**关键创新**：最重要的创新在于成功识别和隔离文化特定神经元，证明其在多语言模型中的独立性，这与现有方法的混合性有本质区别。

**关键设计**：在实验中，采用了特定的损失函数和网络结构，确保文化神经元的有效识别与调节，同时对不同文化的神经元进行独立分析。

## 📊 实验亮点

实验结果表明，LLMs在不同神经元群体中编码文化，主要集中在上层，文化神经元的调节能力显著独立于语言特定神经元，展示了文化知识的可编辑性。这一发现为模型的公平性和包容性提供了新的视角。

## 🎯 应用场景

该研究的潜在应用领域包括多语言翻译、文化适应性AI系统和公平性评估工具。通过识别和调节文化神经元，能够提升模型在不同文化背景下的表现，促进更具包容性的人工智能应用。未来可能影响AI系统的设计和社会责任。

## 📄 摘要（原文）

> Language and culture are deeply intertwined, yet it has been unclear how and where multilingual large language models encode culture. Here, we build on an established methodology for identifying language-specific neurons to localize and isolate culture-specific neurons, carefully disentangling their overlap and interaction with language-specific neurons. To facilitate our experiments, we introduce MUREL, a curated dataset of 85.2 million tokens spanning six different cultures. Our localization and intervention experiments show that LLMs encode different cultures in distinct neuron populations, predominantly in upper layers, and that these culture neurons can be modulated largely independently of language-specific neurons or those specific to other cultures. These findings suggest that cultural knowledge and propensities in multilingual language models can be selectively isolated and edited, with implications for fairness, inclusivity, and alignment. Code and data are available at https://github.com/namazifard/Culture_Neurons.

