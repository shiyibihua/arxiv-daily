---
layout: default
title: Georeferencing complex relative locality descriptions with large language models
---

# Georeferencing complex relative locality descriptions with large language models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14228" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14228v1</a>
  <a href="https://arxiv.org/pdf/2512.14228.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14228v1" onclick="toggleFavorite(this, '2512.14228v1', 'Georeferencing complex relative locality descriptions with large language models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aneesha Fernando, Surangika Ranathunga, Kristin Stock, Raj Prasanna, Christopher B. Jones

**分类**: cs.AI

**发布日期**: 2025-12-16

**备注**: Provisionally accepted for publication in the International Journal of Geographical Information Science

---

## 💡 一句话要点

**利用大型语言模型解决生物多样性领域复杂相对位置描述的地理定位问题**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `地理定位` `大型语言模型` `生物多样性` `位置描述` `提示工程`

## 📋 核心要点

1. 现有地理定位方法难以处理包含空间关系的相对位置描述，导致生物标本采集记录等场景定位不准确。
2. 利用大型语言模型理解复杂的位置描述，通过有效的提示模式和微调策略，实现自动地理定位。
3. 实验结果表明，该方法在生物多样性数据集上优于现有基线，显著提高了地理定位的准确性。

## 📝 摘要（中文）

本文探讨了利用大型语言模型（LLM）自动地理定位复杂位置描述的潜力，重点关注生物多样性收集领域。传统的地理定位方法依赖于地名词典或语言模型，难以处理包含空间关系的相对位置描述，这在生物标本采集记录中尤为常见。为了解决这个问题，我们首先确定了有效的提示模式，然后使用量化低秩适应（QLoRA）在来自多个地区和语言的生物多样性数据集上微调LLM。结果表明，对于固定数量的训练数据，我们的方法优于现有基线，平均有65%的记录位于10公里半径范围内。在纽约州数据集上取得了最佳结果，85%的记录位于10公里范围内，67%的记录位于1公里范围内。实验表明，所选LLM能够很好地处理冗长、复杂的位置描述，突显了其在地理定位复杂位置描述方面的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决生物多样性领域中，由于历史生物标本采集记录常使用复杂、相对的位置描述，导致传统地理定位方法失效的问题。现有方法主要依赖地名词典或简单的语言模型，无法有效理解和处理包含空间关系的描述，人工地理定位耗时耗力。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）强大的语言理解能力，将复杂的位置描述转化为地理坐标。通过提示工程（Prompt Engineering）引导LLM理解位置描述中的空间关系，并利用微调（Fine-tuning）使其适应特定领域的知识和表达方式。

**技术框架**：整体框架包括以下几个主要阶段：1) 数据准备：收集包含复杂位置描述的生物多样性数据集；2) 提示工程：设计有效的提示模板，引导LLM理解位置描述；3) 模型微调：使用QLoRA方法在LLM上进行微调，使其适应生物多样性领域的地理定位任务；4) 模型评估：使用测试数据集评估模型的地理定位准确性。

**关键创新**：最重要的技术创新点在于将大型语言模型应用于复杂相对位置描述的地理定位任务。与传统方法相比，LLM能够更好地理解自然语言描述中的空间关系和上下文信息，从而实现更准确的地理定位。QLoRA微调方法降低了微调LLM的计算成本。

**关键设计**：论文中关键的设计包括：1) 提示模板的设计，需要能够有效地引导LLM理解位置描述；2) QLoRA微调方法的参数设置，例如秩的大小、学习率等；3) 损失函数的选择，用于指导模型学习地理定位任务。具体参数和损失函数细节在论文中未明确给出，属于未知信息。

## 📊 实验亮点

实验结果表明，该方法在生物多样性数据集上优于现有基线。在所有数据集上的平均表现是，65%的记录定位在距离真实位置10公里范围内。在纽约州数据集上，85%的记录定位在10公里范围内，67%的记录定位在1公里范围内。这些结果表明，该方法能够有效地处理复杂的位置描述，并实现较高的地理定位准确性。

## 🎯 应用场景

该研究成果可应用于生物多样性研究、生态环境保护、自然资源管理等领域。通过自动地理定位历史生物标本采集记录，可以更准确地了解物种分布和演化规律，为生物多样性保护提供科学依据。此外，该方法还可应用于其他需要处理复杂位置描述的场景，例如历史文献研究、考古学研究等。

## 📄 摘要（原文）

> Georeferencing text documents has typically relied on either gazetteer-based methods to assign geographic coordinates to place names, or on language modelling approaches that associate textual terms with geographic locations. However, many location descriptions specify positions relatively with spatial relationships, making geocoding based solely on place names or geo-indicative words inaccurate. This issue frequently arises in biological specimen collection records, where locations are often described through narratives rather than coordinates if they pre-date GPS. Accurate georeferencing is vital for biodiversity studies, yet the process remains labour-intensive, leading to a demand for automated georeferencing solutions. This paper explores the potential of Large Language Models (LLMs) to georeference complex locality descriptions automatically, focusing on the biodiversity collections domain. We first identified effective prompting patterns, then fine-tuned an LLM using Quantized Low-Rank Adaptation (QLoRA) on biodiversity datasets from multiple regions and languages. Our approach outperforms existing baselines with an average, across datasets, of 65% of records within a 10 km radius, for a fixed amount of training data. The best results (New York state) were 85% within 10km and 67% within 1km. The selected LLM performs well for lengthy, complex descriptions, highlighting its potential for georeferencing intricate locality descriptions.

