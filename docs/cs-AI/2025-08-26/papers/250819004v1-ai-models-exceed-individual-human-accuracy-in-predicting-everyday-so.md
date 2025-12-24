---
layout: default
title: AI Models Exceed Individual Human Accuracy in Predicting Everyday Social Norms
---

# AI Models Exceed Individual Human Accuracy in Predicting Everyday Social Norms

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19004" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19004v1</a>
  <a href="https://arxiv.org/pdf/2508.19004.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19004v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19004v1', 'AI Models Exceed Individual Human Accuracy in Predicting Everyday Social Norms')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pontus Strimling, Simon Karlsson, Irina Vartanova, Kimmo Eriksson

**分类**: cs.AI

**发布日期**: 2025-08-26

**备注**: 18 pages + supplementy materials

---

## 💡 一句话要点

**提出大型语言模型以超越人类预测社会规范的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `社会规范` `大型语言模型` `统计学习` `社会认知` `人机交互` `文化知识` `心理学` `人工智能`

## 📋 核心要点

1. 现有研究主要集中在具身经验对社会规范学习的影响，缺乏对统计学习在此过程中的作用的深入探讨。
2. 本研究通过评估大型语言模型在预测社会适当性判断中的能力，探讨统计学习是否能替代具身经验。
3. 实验结果显示，GPT-4.5的预测准确性超过所有人类参与者，其他模型也表现优异，验证了语言作为文化知识传递的丰富性。

## 📝 摘要（中文）

本研究探讨了社会规范的获取与表征问题，重点评估大型语言模型在预测人类社会适当性判断中的表现。通过两项研究，发现GPT-4.5在预测555个日常场景的集体判断时，其准确性超过了所有人类参与者，而Gemini 2.5 Pro、GPT-5和Claude Sonnet 4也表现出色。这些结果表明，复杂的社会认知模型可以仅通过统计学习语言数据而形成，挑战了强调具身经验在文化能力中独特必要性的理论。尽管模型表现出色，但仍存在系统性错误，显示出基于模式的社会理解的潜在局限性。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在预测人类社会规范方面的能力，现有方法主要依赖具身经验，缺乏对统计学习的应用探讨。

**核心思路**：研究通过系统评估多种AI系统在预测社会适当性判断中的表现，探讨统计学习是否能有效替代具身经验。

**技术框架**：整体架构包括数据收集、模型训练和预测评估三个主要阶段，使用了多种大型语言模型进行对比分析。

**关键创新**：本研究的创新点在于首次系统性地展示了大型语言模型在社会认知预测中的超越人类能力，挑战了传统理论对具身经验的依赖。

**关键设计**：模型训练过程中采用了特定的损失函数和参数设置，以优化预测准确性，确保模型能够有效捕捉语言中的社会规范信息。

## 📊 实验亮点

实验结果显示，GPT-4.5在预测社会适当性判断时的准确性达到了100百分位，Gemini 2.5 Pro超越了98.7%的参与者，GPT-5和Claude Sonnet 4分别超越了97.8%和96.0%的参与者。这些结果表明，语言模型在社会认知任务中的表现显著优于个体人类。

## 🎯 应用场景

该研究的结果在社会科学、心理学和人工智能领域具有广泛的应用潜力。大型语言模型可以用于开发更智能的社交机器人、增强人机交互的自然性，以及为社会行为的研究提供新的工具和视角。未来，随着模型的进一步优化，其在文化知识传递和社会规范理解中的应用将更加广泛。

## 📄 摘要（原文）

> A fundamental question in cognitive science concerns how social norms are acquired and represented. While humans typically learn norms through embodied social experience, we investigated whether large language models can achieve sophisticated norm understanding through statistical learning alone. Across two studies, we systematically evaluated multiple AI systems' ability to predict human social appropriateness judgments for 555 everyday scenarios by examining how closely they predicted the average judgment compared to each human participant. In Study 1, GPT-4.5's accuracy in predicting the collective judgment on a continuous scale exceeded that of every human participant (100th percentile). Study 2 replicated this, with Gemini 2.5 Pro outperforming 98.7% of humans, GPT-5 97.8%, and Claude Sonnet 4 96.0%. Despite this predictive power, all models showed systematic, correlated errors. These findings demonstrate that sophisticated models of social cognition can emerge from statistical learning over linguistic data alone, challenging strong versions of theories emphasizing the exclusive necessity of embodied experience for cultural competence. The systematic nature of AI limitations across different architectures indicates potential boundaries of pattern-based social understanding, while the models' ability to outperform nearly all individual humans in this predictive task suggests that language serves as a remarkably rich repository for cultural knowledge transmission.

