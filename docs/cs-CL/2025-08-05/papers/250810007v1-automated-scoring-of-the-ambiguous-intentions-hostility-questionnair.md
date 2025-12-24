---
layout: default
title: Automated scoring of the Ambiguous Intentions Hostility Questionnaire using fine-tuned large language models
---

# Automated scoring of the Ambiguous Intentions Hostility Questionnaire using fine-tuned large language models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10007" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10007v1</a>
  <a href="https://arxiv.org/pdf/2508.10007.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10007v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10007v1', 'Automated scoring of the Ambiguous Intentions Hostility Questionnaire using fine-tuned large language models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Y. Lyu, D. Combs, D. Neumann, Y. C. Leong

**分类**: cs.CL, stat.ME

**发布日期**: 2025-08-05

**备注**: We have no known conflict of interest

---

## 💡 一句话要点

**利用微调的大型语言模型自动评分AIHQ问卷**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `敌意归因` `自动评分` `大型语言模型` `心理测量` `开放式问题`

## 📋 核心要点

1. 现有的AIHQ评分依赖人工评估，耗时且容易受到主观因素影响，限制了其在临床和研究中的应用。
2. 本文提出利用微调的大型语言模型自动评分AIHQ问卷的开放式回答，旨在提高评分效率和一致性。
3. 实验结果显示，微调后的模型在敌意和攻击性反应的评分上与人工评分高度一致，且在不同人群中具有良好的泛化能力。

## 📝 摘要（中文）

敌意归因偏差是将社会互动解读为故意敌对的倾向。模糊意图敌意问卷（AIHQ）用于测量这种偏差，包含开放式问题，要求参与者描述对负面社交情境的理解及反应。传统评分依赖人工评估，耗时且主观。本文研究了大型语言模型在自动评分AIHQ开放式回答中的应用。通过对已有数据集进行微调，结果表明模型生成的评分与人工评分高度一致，且在不同情境类型中表现稳定。研究还提供了便捷的评分接口，支持更广泛的应用，显示出大型语言模型在心理评估中的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决模糊意图敌意问卷（AIHQ）开放式回答的人工评分耗时且主观的问题。现有方法依赖训练有素的人工评分者，限制了其在大规模心理评估中的应用。

**核心思路**：通过微调大型语言模型，使其能够自动生成AIHQ问卷开放式回答的评分，从而提高评分的效率和一致性。模型的设计旨在捕捉人类评分者的评分标准。

**技术框架**：研究使用了一个包含创伤性脑损伤（TBI）和健康对照（HC）个体的已有数据集。首先，利用一半的开放式回答对模型进行微调，然后在剩余的回答上进行测试。模型的评分结果与人工评分进行比较。

**关键创新**：本研究的主要创新在于将大型语言模型应用于心理测量的自动评分，展示了其在处理开放式问题中的有效性，与传统人工评分方法相比，显著提高了评分的一致性和效率。

**关键设计**：在模型微调过程中，使用了人类评分者的评分作为训练目标，采用了适当的损失函数以优化模型输出的评分与人类评分的一致性。模型架构基于现有的语言模型，经过调整以适应特定的评分任务。

## 📊 实验亮点

实验结果表明，微调后的模型在敌意和攻击性反应的评分上与人工评分的对齐度显著提高，尤其在模糊、故意和意外情境类型中均表现出一致性。模型在独立的非临床数据集上也展现了良好的泛化能力，表明其适用性广泛。

## 🎯 应用场景

该研究的潜在应用领域包括心理健康评估、临床心理学研究及社会心理学调查等。通过自动化评分，能够显著提高评估效率，降低人力成本，促进心理评估工具的广泛应用，尤其是在资源有限的环境中。未来，该方法可能推动更多心理测量工具的自动化发展，提升心理健康服务的可及性。

## 📄 摘要（原文）

> Hostile attribution bias is the tendency to interpret social interactions as intentionally hostile. The Ambiguous Intentions Hostility Questionnaire (AIHQ) is commonly used to measure hostile attribution bias, and includes open-ended questions where participants describe the perceived intentions behind a negative social situation and how they would respond. While these questions provide insights into the contents of hostile attributions, they require time-intensive scoring by human raters. In this study, we assessed whether large language models can automate the scoring of AIHQ open-ended responses. We used a previously collected dataset in which individuals with traumatic brain injury (TBI) and healthy controls (HC) completed the AIHQ and had their open-ended responses rated by trained human raters. We used half of these responses to fine-tune the two models on human-generated ratings, and tested the fine-tuned models on the remaining half of AIHQ responses. Results showed that model-generated ratings aligned with human ratings for both attributions of hostility and aggression responses, with fine-tuned models showing higher alignment. This alignment was consistent across ambiguous, intentional, and accidental scenario types, and replicated previous findings on group differences in attributions of hostility and aggression responses between TBI and HC groups. The fine-tuned models also generalized well to an independent nonclinical dataset. To support broader adoption, we provide an accessible scoring interface that includes both local and cloud-based options. Together, our findings suggest that large language models can streamline AIHQ scoring in both research and clinical contexts, revealing their potential to facilitate psychological assessments across different populations.

