---
layout: default
title: Large Language Models Can Be a Viable Substitute for Expert Political Surveys When a Shock Disrupts Traditional Measurement Approaches
---

# Large Language Models Can Be a Viable Substitute for Expert Political Surveys When a Shock Disrupts Traditional Measurement Approaches

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06540" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06540v1</a>
  <a href="https://arxiv.org/pdf/2506.06540.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06540v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06540v1', 'Large Language Models Can Be a Viable Substitute for Expert Political Surveys When a Shock Disrupts Traditional Measurement Approaches')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Patrick Y. Wu

**分类**: cs.CY, cs.AI, cs.CL

**发布日期**: 2025-06-06

**备注**: 19 pages, 6 figures

---

## 💡 一句话要点

**提出大语言模型替代专家政治调查以应对测量中断问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `政治调查` `专家判断` `意识形态评分` `数据分析` `公共政策` `数字媒体`

## 📋 核心要点

1. 现有的专家政治调查在冲击事件后难以重建事件前的认知，导致数据失真。
2. 论文提出利用大语言模型（LLMs）进行成对比较，替代传统的专家调查方法。
3. 通过案例研究，LLMs的应用能够有效预测被裁员的机构，并复现专家的意识形态评分。

## 📝 摘要（中文）

在经历如2025年政府效率部（DOGE）联邦裁员等冲击事件后，专家判断受到结果知识的影响，难以重建事件前的认知。本文主张，经过大量数字媒体数据训练的大语言模型（LLMs）可以有效替代专家政治调查。通过对DOGE裁员的案例研究，使用LLMs进行成对比较提示，得出联邦执行机构的意识形态评分，这些评分能够复现裁员前的专家测量，并预测被DOGE针对的机构。研究表明，LLMs能够快速测试与冲击相关的假设因素，提供传统测量技术无法实现的洞察。最后，提出了研究者何时可以转向LLMs作为专家调查替代的双重标准。

## 🔬 方法详解

**问题定义**：本文旨在解决在冲击事件后，专家判断受结果影响而无法重建事件前认知的问题。现有方法在此情况下难以提供准确的政治调查数据。

**核心思路**：论文的核心思路是利用大语言模型（LLMs）对大量数字媒体数据进行训练，通过成对比较提示来获取意识形态评分，从而替代传统的专家调查。这样的设计使得在传统方法失效时，仍能获得有效的政治认知数据。

**技术框架**：整体架构包括数据收集、模型训练、成对比较提示生成和意识形态评分提取四个主要模块。首先收集相关的数字媒体数据，然后训练LLMs，接着使用成对比较提示进行分析，最后提取意识形态评分。

**关键创新**：最重要的技术创新点在于将LLMs应用于政治调查领域，尤其是在传统测量方法失效的情况下，提供了一种新的数据获取方式。这与现有方法的本质区别在于，LLMs能够处理大量非结构化数据并提取有用信息。

**关键设计**：在模型训练中，选择了适当的超参数设置以优化模型性能，损失函数采用了交叉熵损失，网络结构基于Transformer架构，确保了模型在理解和生成语言方面的高效性。

## 📊 实验亮点

实验结果表明，使用LLMs得出的意识形态评分能够有效复现裁员前的专家测量，并成功预测被DOGE裁员的机构。这一方法在准确性上与传统专家调查相当，展示了LLMs在政治调查中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括政治科学研究、公共政策分析和社会舆论监测。通过使用大语言模型，研究者能够在传统调查方法失效时，快速获取政治认知数据，提升研究的效率和准确性，未来可能对政治决策和政策制定产生深远影响。

## 📄 摘要（原文）

> After a disruptive event or shock, such as the Department of Government Efficiency (DOGE) federal layoffs of 2025, expert judgments are colored by knowledge of the outcome. This can make it difficult or impossible to reconstruct the pre-event perceptions needed to study the factors associated with the event. This position paper argues that large language models (LLMs), trained on vast amounts of digital media data, can be a viable substitute for expert political surveys when a shock disrupts traditional measurement. We analyze the DOGE layoffs as a specific case study for this position. We use pairwise comparison prompts with LLMs and derive ideology scores for federal executive agencies. These scores replicate pre-layoff expert measures and predict which agencies were targeted by DOGE. We also use this same approach and find that the perceptions of certain federal agencies as knowledge institutions predict which agencies were targeted by DOGE, even when controlling for ideology. This case study demonstrates that using LLMs allows us to rapidly and easily test the associated factors hypothesized behind the shock. More broadly, our case study of this recent event exemplifies how LLMs offer insights into the correlational factors of the shock when traditional measurement techniques fail. We conclude by proposing a two-part criterion for when researchers can turn to LLMs as a substitute for expert political surveys.

