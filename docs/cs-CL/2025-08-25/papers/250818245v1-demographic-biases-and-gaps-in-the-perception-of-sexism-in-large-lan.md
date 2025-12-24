---
layout: default
title: Demographic Biases and Gaps in the Perception of Sexism in Large Language Models
---

# Demographic Biases and Gaps in the Perception of Sexism in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18245" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18245v1</a>
  <a href="https://arxiv.org/pdf/2508.18245.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18245v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18245v1', 'Demographic Biases and Gaps in the Perception of Sexism in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Judith Tavarez-Rodríguez, Fernando Sánchez-Vega, A. Pastor López-Monroy

**分类**: cs.CL

**发布日期**: 2025-08-25

**备注**: This work was presented as a poster at the Latin American Meeting in Artificial Intelligence KHIPU 2025, Santiago, Chile, March 10th - 14th 2025, https://khipu.ai/khipu2025/poster-sessions-2025/

---

## 💡 一句话要点

**探讨大型语言模型中性别歧视感知的群体偏见与差距**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `性别歧视检测` `人口统计偏见` `社交媒体分析` `模型校准`

## 📋 核心要点

1. 现有大型语言模型在性别歧视检测中存在显著偏见，尤其对少数群体的感知未能准确反映。
2. 本文通过EXIST 2024推文数据集，评估不同LLMs在性别歧视检测中的表现，并分析人口统计特征的影响。
3. 研究发现，虽然LLMs可以检测性别歧视，但未能充分捕捉不同群体的多样化观点，显示出模型校准的必要性。

## 📝 摘要（中文）

大型语言模型（LLMs）在自动检测性别歧视方面展现出潜力，但现有模型存在偏见，未能准确反映少数群体的现实。尽管已有多项努力改善性别歧视内容的检测，但由于任务的主观性及模型中的偏见，这一挑战依然显著。本文利用EXIST 2024推文数据集，评估不同LLMs在社交媒体文本中检测性别歧视的能力，并分析模型中的人口统计偏见，识别影响检测效果的关键人口特征。研究结果表明，LLMs在整体人群意见的基础上能够检测性别歧视，但未能准确再现不同群体的多样化感知，强调了需要更好校准模型以考虑不同人群的观点多样性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在性别歧视检测中的偏见问题，现有方法未能准确反映不同人口群体的感知差异。

**核心思路**：通过分析不同人口特征（如年龄、性别）对性别歧视检测的影响，提出改进模型的策略，以更好地捕捉多样化的观点。

**技术框架**：研究使用EXIST 2024推文数据集，包含六个不同的用户画像对每条推文进行标注，评估LLMs的检测能力。主要模块包括数据收集、模型训练、偏见分析和结果评估。

**关键创新**：本文的创新在于系统性地分析了LLMs在性别歧视检测中的人口统计偏见，强调了模型在不同群体感知上的不足，与现有方法相比，提供了更全面的视角。

**关键设计**：研究中使用了多种LLMs，并通过统计分析识别影响检测效果的关键人口特征，设计了相应的实验以验证模型的有效性。具体的参数设置和损失函数设计未在摘要中详细说明，需参考原文。

## 📊 实验亮点

实验结果表明，尽管LLMs在整体人群意见的基础上能够检测性别歧视，但在不同人口群体的感知上存在显著差异，未能准确再现多样化的观点。这一发现强调了模型校准的重要性，未来需要针对不同群体进行更深入的研究和优化。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容监测、在线平台的内容审核以及性别歧视相关的政策制定。通过改进模型的偏见检测能力，可以更有效地识别和应对性别歧视现象，促进社会公平与包容性。未来，研究成果有望推动更为公正的AI应用和技术发展。

## 📄 摘要（原文）

> The use of Large Language Models (LLMs) has proven to be a tool that could help in the automatic detection of sexism. Previous studies have shown that these models contain biases that do not accurately reflect reality, especially for minority groups. Despite various efforts to improve the detection of sexist content, this task remains a significant challenge due to its subjective nature and the biases present in automated models. We explore the capabilities of different LLMs to detect sexism in social media text using the EXIST 2024 tweet dataset. It includes annotations from six distinct profiles for each tweet, allowing us to evaluate to what extent LLMs can mimic these groups' perceptions in sexism detection. Additionally, we analyze the demographic biases present in the models and conduct a statistical analysis to identify which demographic characteristics (age, gender) contribute most effectively to this task. Our results show that, while LLMs can to some extent detect sexism when considering the overall opinion of populations, they do not accurately replicate the diversity of perceptions among different demographic groups. This highlights the need for better-calibrated models that account for the diversity of perspectives across different populations.

