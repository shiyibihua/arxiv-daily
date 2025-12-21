---
layout: default
title: Impacts of Racial Bias in Historical Training Data for News AI
---

# Impacts of Racial Bias in Historical Training Data for News AI

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16901" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16901v1</a>
  <a href="https://arxiv.org/pdf/2512.16901.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16901v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16901v1', 'Impacts of Racial Bias in Historical Training Data for News AI')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rahul Bhargava, Malene Hornstrup Jespersen, Emily Boardman Ndulue, Vivica Dsouza

**分类**: cs.LG, cs.AI, cs.CL, cs.CY

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**揭示新闻AI中历史数据偏见：以纽约时报语料库为例，分析种族标签的影响。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `新闻AI` `种族偏见` `历史数据` `可解释AI` `自然语言处理`

## 📋 核心要点

1. 现有新闻AI模型训练于历史数据，可能内嵌过时的态度和刻板印象，导致偏见。
2. 通过分析《纽约时报》语料库训练的多标签分类器，研究“黑人”标签的潜在偏见。
3. 发现该标签在特定情境下表现不佳，揭示了新闻AI应用中重现历史偏见的风险。

## 📝 摘要（中文）

人工智能技术已迅速应用于涉及大型文本语料库的商业和研究应用，包括计算新闻研究和新闻编辑室环境。这些模型在来自各种来源的现有数据上进行训练，可以被概念化为编码了数十年历史态度和刻板印象的历史产物。本文研究了一个这样的例子，该例子在广泛使用的《纽约时报》注释语料库上进行训练，以创建一个多标签分类器。我们在研究环境中的使用浮现了令人担忧的“黑人”主题标签。通过定量和定性的方法，我们调查了该标签在训练语料库中的使用情况，它可能在训练后的分类器中编码了哪些概念，以及这些概念如何影响我们的模型使用。通过应用可解释人工智能方法，我们发现“黑人”标签在一定程度上充当了针对一些少数族裔群体的通用“种族主义检测器”。然而，它在现代例子（如COVID-19时代的反亚裔仇恨故事和关于“黑人的命也是命”运动的报道）上的表现不尽如人意。这个对模型中嵌入的偏见进行调查的案例研究揭示了新闻编辑室环境中类似的应用如何导致意想不到的输出，这些输出可能会影响任何大型语言模型的各种潜在用途——故事发现、受众定位、摘要等。这为新闻编辑室暴露出的根本矛盾是：如何在采用人工智能支持的工作流程工具的同时，降低在新闻报道中重现历史偏见的风险。

## 🔬 方法详解

**问题定义**：论文旨在解决新闻AI模型中由于历史训练数据偏差而产生的种族偏见问题。现有方法未能充分识别和减轻这些偏差，导致模型在处理涉及种族议题的新闻时产生不准确或带有偏见的输出。这种偏见会影响新闻报道的客观性和公正性，损害公众信任。

**核心思路**：论文的核心思路是通过深入分析训练数据和模型行为，揭示和量化模型中存在的种族偏见。通过可解释AI方法，探究特定标签（如“黑人”）在模型中的作用，并评估其在不同情境下的表现。这种分析有助于理解模型如何编码和传播历史偏见。

**技术框架**：论文采用的框架包括以下几个主要阶段：1) 数据分析：对《纽约时报》注释语料库中“黑人”标签的使用情况进行定量和定性分析。2) 模型训练：使用该语料库训练一个多标签分类器。3) 可解释性分析：应用可解释AI方法（具体方法未知）来理解“黑人”标签在模型中的作用。4) 案例研究：评估模型在现代新闻事件（如COVID-19期间的反亚裔仇恨和“黑人的命也是命”运动）上的表现。

**关键创新**：论文的关键创新在于将可解释AI方法应用于新闻AI模型的偏见分析，并以“黑人”标签为例，深入研究了历史数据偏差对模型行为的影响。与以往研究相比，该论文更注重揭示偏见的具体表现形式和潜在影响，而不仅仅是检测偏见的存在。

**关键设计**：论文的关键设计包括选择《纽约时报》注释语料库作为训练数据，因为它具有广泛的应用和代表性。此外，选择“黑人”标签作为研究对象，因为它在新闻报道中具有重要的社会和政治意义。具体的可解释AI方法、损失函数和网络结构等技术细节未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16901v1/figures/fig1-blacks-use.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16901v1/figures/fig2-boxplots.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16901v1/figures/fig3-terms-grid.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

研究发现，在《纽约时报》语料库上训练的模型中，“黑人”标签在一定程度上充当了“种族主义检测器”，但其表现并不稳定，在COVID-19期间的反亚裔仇恨和“黑人的命也是命”运动等现代案例中表现不佳，揭示了历史数据偏差对模型泛化能力的影响。

## 🎯 应用场景

该研究成果可应用于新闻编辑室，帮助记者和编辑识别和减轻AI模型中的偏见，提高新闻报道的客观性和公正性。此外，该研究也为其他领域（如法律、教育等）的AI应用提供了借鉴，促进了负责任的AI开发和部署。

## 📄 摘要（原文）

> AI technologies have rapidly moved into business and research applications that involve large text corpora, including computational journalism research and newsroom settings. These models, trained on extant data from various sources, can be conceptualized as historical artifacts that encode decades-old attitudes and stereotypes. This paper investigates one such example trained on the broadly-used New York Times Annotated Corpus to create a multi-label classifier. Our use in research settings surfaced the concerning "blacks" thematic topic label. Through quantitative and qualitative means we investigate this label's use in the training corpus, what concepts it might be encoding in the trained classifier, and how those concepts impact our model use. Via the application of explainable AI methods, we find that the "blacks" label operates partially as a general "racism detector" across some minoritized groups. However, it performs poorly against expectations on modern examples such as COVID-19 era anti-Asian hate stories, and reporting on the Black Lives Matter movement. This case study of interrogating embedded biases in a model reveals how similar applications in newsroom settings can lead to unexpected outputs that could impact a wide variety of potential uses of any large language model-story discovery, audience targeting, summarization, etc. The fundamental tension this exposes for newsrooms is how to adopt AI-enabled workflow tools while reducing the risk of reproducing historical biases in news coverage.

