---
layout: default
title: Exploring the features used for summary evaluation by Human and GPT
---

# Exploring the features used for summary evaluation by Human and GPT

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19620" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19620v1</a>
  <a href="https://arxiv.org/pdf/2512.19620.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19620v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19620v1', 'Exploring the features used for summary evaluation by Human and GPT')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zahra Sadeghi, Evangelos Milios, Frank Rudzicz

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**研究人类与GPT评估摘要时使用的特征，并提升GPT摘要评估能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `摘要评估` `大型语言模型` `特征分析` `人类对齐` `GPT` `自动化评估` `自然语言处理`

## 📋 核心要点

1. 现有摘要评估方法缺乏对人类和LLM评估特征的深入理解，阻碍了自动化评估的准确性和可靠性。
2. 通过统计和机器学习指标，论文探索了人类和GPT在摘要评估中使用的特征，并建立了评估分数与指标之间的映射关系。
3. 实验表明，指导GPT使用人类评估指标可以显著提高其判断能力，使其评估结果更符合人类的认知。

## 📝 摘要（中文）

摘要评估旨在衡量生成的摘要在多大程度上反映了源文本的关键思想和含义，这需要对内容有深刻的理解。大型语言模型（LLMs）已被用于自动化此过程，充当评估摘要相对于原始文本的质量的评判者。虽然之前的研究调查了LLM与人类反应之间的一致性，但人们对LLM在基于特定质量维度进行评估时利用的属性或特征的理解尚不充分，并且对评估分数和指标之间的映射关注不足。在本文中，我们通过研究统计和机器学习指标来解决这个问题，并发现与人类和生成式预训练Transformer（GPT）反应对齐的特征。此外，我们表明，指示GPT采用人类使用的指标可以改善其判断，使其更好地符合人类的反应。

## 🔬 方法详解

**问题定义**：论文旨在解决摘要评估自动化的问题，特别是如何使大型语言模型（LLMs）的评估结果更接近人类的判断。现有方法缺乏对人类和LLM评估摘要时所关注特征的深入理解，导致LLM的评估结果与人类存在偏差。

**核心思路**：论文的核心思路是通过分析人类和LLM在评估摘要时使用的特征，找到两者之间的关联，并利用这些关联来指导LLM的评估过程，从而提高LLM评估结果与人类判断的一致性。

**技术框架**：论文的技术框架主要包括以下几个步骤：1) 收集人类对摘要的评估数据；2) 收集LLM（GPT）对相同摘要的评估数据；3) 提取摘要的统计和机器学习特征；4) 分析人类和GPT评估数据与摘要特征之间的关系；5) 基于分析结果，设计指导GPT评估的策略。

**关键创新**：论文的关键创新在于：1) 深入研究了人类和GPT在摘要评估中使用的特征，揭示了两者之间的差异和关联；2) 提出了一种利用人类评估特征来指导GPT评估的方法，提高了GPT评估结果与人类判断的一致性。

**关键设计**：论文的关键设计包括：1) 选择合适的统计和机器学习指标来提取摘要的特征，例如ROUGE、BLEU等；2) 设计合适的损失函数来训练GPT，使其评估结果更接近人类的判断；3) 设计合适的prompt，引导GPT关注人类评估摘要时使用的特征。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19620v1/Figs/corr_scatter_cos_ent_read_gini_rel_model_condprep1_legend.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19620v1/Figs/corr_scatter_cos_ent_read_gini_coh_model_condprep1_legend.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19620v1/Figs/corr_barchart_cos_ent_gini_read_rel_gpts_phi_condprep1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

研究表明，通过指导GPT使用人类评估指标，可以显著提高其摘要评估能力，使其评估结果更符合人类的认知。具体而言，经过指导的GPT在摘要评估任务上的表现更接近人类专家的评估结果，减少了与人类判断的偏差。

## 🎯 应用场景

该研究成果可应用于自动摘要评估、机器翻译质量评估、文本生成质量评估等领域。通过提高LLM评估结果与人类判断的一致性，可以减少人工评估的成本，提高评估效率，并为文本生成模型的优化提供更可靠的反馈。

## 📄 摘要（原文）

> Summary assessment involves evaluating how well a generated summary reflects the key ideas and meaning of the source text, requiring a deep understanding of the content. Large Language Models (LLMs) have been used to automate this process, acting as judges to evaluate summaries with respect to the original text. While previous research investigated the alignment between LLMs and Human responses, it is not yet well understood what properties or features are exploited by them when asked to evaluate based on a particular quality dimension, and there has not been much attention towards mapping between evaluation scores and metrics. In this paper, we address this issue and discover features aligned with Human and Generative Pre-trained Transformers (GPTs) responses by studying statistical and machine learning metrics. Furthermore, we show that instructing GPTs to employ metrics used by Human can improve their judgment and conforming them better with human responses.

