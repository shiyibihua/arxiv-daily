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

**关键词**: `新闻AI` `种族偏见` `历史数据` `可解释AI` `文本分类`

## 📋 核心要点

1. 现有新闻AI模型训练于历史数据，可能内嵌过时的偏见和刻板印象，影响新闻报道的客观性。
2. 通过分析《纽约时报》语料库训练的模型中“黑人”标签的使用，揭示其潜在的偏见编码。
3. 实验表明该标签在某些情况下充当“种族主义检测器”，但在现代事件中表现不佳，存在局限性。

## 📝 摘要（中文）

人工智能技术正迅速应用于涉及大型文本语料库的商业和研究领域，包括计算新闻学研究和新闻编辑室环境。这些模型在现有数据上训练，可以被视为编码了几十年前的态度和刻板印象的历史产物。本文研究了一个基于广泛使用的《纽约时报》标注语料库训练的多标签分类器。研究中浮现了令人担忧的“黑人”主题标签。通过定量和定性的方法，我们调查了这个标签在训练语料库中的使用情况，它可能在训练后的分类器中编码了哪些概念，以及这些概念如何影响模型的应用。通过可解释人工智能方法，我们发现“黑人”标签在一定程度上充当了针对一些少数族裔群体的通用“种族主义检测器”。然而，在诸如COVID-19时代的反亚裔仇恨故事以及对“黑人的命也是命”运动的报道等现代例子中，它的表现不尽如人意。这个对模型中嵌入偏见的案例研究揭示了新闻编辑室环境中类似的应用如何导致意想不到的输出，这可能会影响任何大型语言模型的各种潜在用途——故事发现、受众定位、摘要等。这为新闻编辑室暴露出的根本矛盾是，如何在采用人工智能支持的工作流程工具的同时，降低在新闻报道中重现历史偏见的风险。

## 🔬 方法详解

**问题定义**：论文旨在揭示新闻AI模型中由于历史训练数据造成的种族偏见问题。现有方法忽略了训练数据中可能存在的偏见，导致模型在实际应用中产生不公平或不准确的结果，尤其是在涉及种族相关议题时。这种偏见会影响新闻报道的客观性和公正性。

**核心思路**：论文的核心思路是通过分析一个在《纽约时报》标注语料库上训练的多标签分类器，特别是其中的“黑人”标签，来揭示模型中潜在的种族偏见。通过定量和定性分析，研究人员试图理解该标签在语料库中的使用方式，以及它在模型中编码了哪些概念。

**技术框架**：该研究的技术框架主要包括以下几个阶段：1) 选择《纽约时报》标注语料库作为研究对象；2) 分析语料库中“黑人”标签的使用情况，包括其频率、上下文等；3) 使用该语料库训练一个多标签分类器；4) 使用可解释人工智能（XAI）方法，如LIME或SHAP，来分析模型对“黑人”标签的预测行为，并识别影响预测的关键特征；5) 在现代新闻事件（如COVID-19期间的反亚裔仇恨事件和“黑人的命也是命”运动）上测试模型的表现，评估其泛化能力和潜在偏见。

**关键创新**：该研究的关键创新在于其对新闻AI模型中历史数据偏见的系统性分析。它不仅揭示了偏见的存在，还尝试理解偏见的来源和影响。此外，该研究还强调了可解释人工智能方法在识别和减轻模型偏见中的作用。

**关键设计**：研究的关键设计包括：1) 选择《纽约时报》语料库，因为它是一个广泛使用的新闻文本资源；2) 使用多标签分类器，以便捕捉文本中多个主题之间的关系；3) 应用可解释人工智能方法，以便理解模型的预测行为；4) 在现代新闻事件上进行测试，以便评估模型的泛化能力和潜在偏见。

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

研究发现，在《纽约时报》语料库训练的模型中，“黑人”标签在一定程度上充当了“种族主义检测器”，但其性能在现代事件中表现不佳。例如，在COVID-19期间的反亚裔仇恨事件和“黑人的命也是命”运动的报道中，该标签的预测结果与预期不符，表明模型存在泛化能力不足和潜在偏见问题。

## 🎯 应用场景

该研究成果可应用于新闻编辑室，帮助新闻从业者识别和减轻AI模型中的偏见，提高新闻报道的客观性和公正性。此外，该研究也为其他领域（如法律、教育等）的AI应用提供了借鉴，有助于开发更公平、更负责任的AI系统。该研究强调了在AI应用中考虑历史数据偏见的重要性，并为未来的研究方向提供了指导。

## 📄 摘要（原文）

> AI technologies have rapidly moved into business and research applications that involve large text corpora, including computational journalism research and newsroom settings. These models, trained on extant data from various sources, can be conceptualized as historical artifacts that encode decades-old attitudes and stereotypes. This paper investigates one such example trained on the broadly-used New York Times Annotated Corpus to create a multi-label classifier. Our use in research settings surfaced the concerning "blacks" thematic topic label. Through quantitative and qualitative means we investigate this label's use in the training corpus, what concepts it might be encoding in the trained classifier, and how those concepts impact our model use. Via the application of explainable AI methods, we find that the "blacks" label operates partially as a general "racism detector" across some minoritized groups. However, it performs poorly against expectations on modern examples such as COVID-19 era anti-Asian hate stories, and reporting on the Black Lives Matter movement. This case study of interrogating embedded biases in a model reveals how similar applications in newsroom settings can lead to unexpected outputs that could impact a wide variety of potential uses of any large language model-story discovery, audience targeting, summarization, etc. The fundamental tension this exposes for newsrooms is how to adopt AI-enabled workflow tools while reducing the risk of reproducing historical biases in news coverage.

