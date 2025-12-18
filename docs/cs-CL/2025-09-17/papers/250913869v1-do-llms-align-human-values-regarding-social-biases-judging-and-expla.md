---
layout: default
title: Do LLMs Align Human Values Regarding Social Biases? Judging and Explaining Social Biases with LLMs
---

# Do LLMs Align Human Values Regarding Social Biases? Judging and Explaining Social Biases with LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13869" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13869v1</a>
  <a href="https://arxiv.org/pdf/2509.13869.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13869v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13869v1', 'Do LLMs Align Human Values Regarding Social Biases? Judging and Explaining Social Biases with LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yang Liu, Chenhui Chu

**分类**: cs.CL

**发布日期**: 2025-09-17

**备注**: 38 pages, 31 figures

---

## 💡 一句话要点

**评估大语言模型在社会偏见场景下的人类价值观对齐程度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `社会偏见` `价值观对齐` `模型评估` `可解释性`

## 📋 核心要点

1. 现有方法依赖专家设计或模拟场景评估LLM的社会偏见，缺乏对不同类型偏见场景的细致分析。
2. 该研究通过分析LLM在不同类型社会偏见场景中的表现，评估其与人类价值观的对齐程度。
3. 实验表明，模型规模与对齐程度并非线性相关，且模型对特定场景有偏好，同系列模型一致性更高。

## 📝 摘要（中文）

大型语言模型（LLMs）若与人类价值观不一致，尤其是在涉及复杂和敏感的社会偏见场景中，可能会导致不良后果。以往研究已通过专家设计或基于代理的模拟偏见场景揭示了LLMs与人类价值观的不一致性。然而，LLMs与人类价值观的对齐程度是否因不同类型的场景（例如，包含负面问题与非负面问题的场景）而异，目前尚不清楚。本研究调查了LLMs在不同类型偏见场景中，关于社会偏见（HVSB）的人类价值观对齐程度。通过对来自四个模型系列的12个LLMs和四个数据集的广泛分析，我们证明了具有大型模型参数规模的LLMs不一定具有较低的错位率和攻击成功率。此外，LLMs对特定类型的场景表现出一定程度的对齐偏好，并且来自同一模型系列的LLMs往往具有更高的判断一致性。此外，我们研究了LLMs通过其对HVSB的解释所表现出的理解能力。我们发现不同LLMs在对HVSB的理解方面没有显着差异。我们还发现LLMs更喜欢自己生成的解释。此外，我们赋予较小的语言模型（LMs）解释HVSB的能力。生成结果表明，微调后的较小LMs生成的解释更具可读性，但模型一致性相对较低。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型(LLMs)在涉及社会偏见时，与人类价值观对齐程度的问题。现有方法主要依赖于专家设计的场景或基于代理的模拟，这些方法可能无法全面捕捉不同类型的偏见场景，并且缺乏对LLM解释能力的深入分析。因此，现有方法难以准确评估LLM在复杂社会偏见场景中的安全性和可靠性。

**核心思路**：论文的核心思路是通过构建包含不同类型社会偏见场景的数据集，并分析LLM在这些场景中的判断和解释，来评估其与人类价值观的对齐程度。通过比较不同模型家族和不同规模的LLM，以及分析它们对偏见场景的解释，可以更全面地了解LLM在社会偏见方面的潜在风险和局限性。

**技术框架**：该研究的技术框架主要包括以下几个阶段：1) 构建包含不同类型社会偏见场景的数据集；2) 使用不同的LLM对这些场景进行判断，并分析其判断结果；3) 分析LLM对判断结果的解释，评估其理解能力；4) 对较小的语言模型进行微调，使其具备解释社会偏见的能力，并评估其生成解释的质量。

**关键创新**：该研究的关键创新在于：1) 系统性地分析了LLM在不同类型社会偏见场景中的表现，揭示了模型规模与对齐程度并非线性相关；2) 深入研究了LLM对社会偏见的解释能力，发现模型更倾向于自己生成的解释；3) 探索了赋予较小语言模型解释社会偏见能力的方法，为构建更安全可靠的LLM提供了新的思路。

**关键设计**：研究中使用了四个数据集，涵盖不同类型的社会偏见场景。选择了来自四个模型系列的12个LLM进行评估，包括不同规模的模型。评估指标包括错位率和攻击成功率，用于衡量LLM与人类价值观的对齐程度。此外，还分析了LLM生成的解释的可读性和模型一致性。

## 📊 实验亮点

实验结果表明，LLM的模型参数规模与人类价值观对齐程度并非线性相关。不同LLM对特定类型的社会偏见场景表现出不同的偏好。来自同一模型家族的LLM在判断上具有较高的一致性。微调后的较小语言模型能够生成更具可读性的解释，但模型一致性相对较低。

## 🎯 应用场景

该研究成果可应用于评估和改进大型语言模型在涉及社会偏见时的安全性，帮助开发者构建更符合人类价值观的AI系统。此外，该研究也为开发能够解释自身判断的AI模型提供了思路，增强了AI系统的透明度和可信度，可应用于内容审核、招聘筛选等敏感领域。

## 📄 摘要（原文）

> Large language models (LLMs) can lead to undesired consequences when misaligned with human values, especially in scenarios involving complex and sensitive social biases. Previous studies have revealed the misalignment of LLMs with human values using expert-designed or agent-based emulated bias scenarios. However, it remains unclear whether the alignment of LLMs with human values differs across different types of scenarios (e.g., scenarios containing negative vs. non-negative questions). In this study, we investigate the alignment of LLMs with human values regarding social biases (HVSB) in different types of bias scenarios. Through extensive analysis of 12 LLMs from four model families and four datasets, we demonstrate that LLMs with large model parameter scales do not necessarily have lower misalignment rate and attack success rate. Moreover, LLMs show a certain degree of alignment preference for specific types of scenarios and the LLMs from the same model family tend to have higher judgment consistency. In addition, we study the understanding capacity of LLMs with their explanations of HVSB. We find no significant differences in the understanding of HVSB across LLMs. We also find LLMs prefer their own generated explanations. Additionally, we endow smaller language models (LMs) with the ability to explain HVSB. The generation results show that the explanations generated by the fine-tuned smaller LMs are more readable, but have a relatively lower model agreeability.

