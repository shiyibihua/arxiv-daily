---
layout: default
title: An Interpretable Benchmark for Clickbait Detection and Tactic Attribution
---

# An Interpretable Benchmark for Clickbait Detection and Tactic Attribution

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10937" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10937v1</a>
  <a href="https://arxiv.org/pdf/2509.10937.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10937v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10937v1', 'An Interpretable Benchmark for Clickbait Detection and Tactic Attribution')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lihi Nofar, Tomer Portal, Aviv Elbaz, Alexander Apartsin, Yehudit Aperstein

**分类**: cs.CL

**发布日期**: 2025-09-13

**备注**: 7 pages

**🔗 代码/项目**: [GITHUB](https://github.com/LLM-HITCS25S/ClickbaitTacticsDetection)

---

## 💡 一句话要点

**提出一种可解释的点击诱饵检测与策略归因基准方法，提升信息可信度。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `点击诱饵检测` `可解释性AI` `自然语言处理` `BERT` `大型语言模型`

## 📋 核心要点

1. 现有点击诱饵检测方法缺乏可解释性，难以实际应用，用户难以理解判断依据。
2. 提出一种两阶段框架，首先检测点击诱饵，然后将检测结果归因于特定的语言操纵策略。
3. 构建合成数据集，通过系统性地扩充真实新闻标题，实现受控实验和模型行为分析。

## 📝 摘要（中文）

点击诱饵标题的泛滥对信息的可靠性和用户对数字媒体的信任构成了重大挑战。虽然机器学习的最新进展提高了对操纵性内容的检测能力，但缺乏可解释性限制了它们的实际应用。本文提出了一种可解释的点击诱饵检测模型，该模型不仅可以识别点击诱饵标题，还可以将其归因于特定的语言操纵策略。我们引入了一个合成数据集，该数据集通过使用预定义的点击诱饵策略目录系统地扩充真实新闻标题而生成。该数据集支持受控实验和模型行为的详细分析。我们提出了一个用于自动点击诱饵分析的两阶段框架，包括检测和策略归因。在第一阶段，我们将微调的BERT分类器与大型语言模型（LLM），特别是GPT-4.0和Gemini 2.4 Flash，在零样本提示和少量样本提示下进行比较，这些提示富含说明性的点击诱饵标题及其相关的说服策略。在第二阶段，一个专用的基于BERT的分类器预测每个标题中存在的特定点击诱饵策略。这项工作推进了透明和值得信赖的AI系统的开发，以打击操纵性媒体内容。我们在https://github.com/LLM-HITCS25S/ClickbaitTacticsDetection与研究社区分享该数据集。

## 🔬 方法详解

**问题定义**：该论文旨在解决点击诱饵检测的可解释性问题。现有方法虽然能检测点击诱饵，但无法解释其判断依据，导致用户难以信任，也难以进一步分析点击诱饵的生成机制。

**核心思路**：核心思路是将点击诱饵检测分解为两个阶段：首先检测标题是否为点击诱饵，然后识别标题中使用的具体点击诱饵策略。通过策略归因，提高模型的可解释性，使用户能够理解模型判断的依据。

**技术框架**：该框架包含两个主要阶段：1) 点击诱饵检测：使用微调的BERT分类器以及大型语言模型（GPT-4.0和Gemini 2.4 Flash）进行零样本和少量样本提示学习。2) 策略归因：使用一个专门的基于BERT的分类器，预测每个标题中存在的特定点击诱饵策略。该框架使用一个合成数据集进行训练和评估，该数据集通过系统地扩充真实新闻标题生成。

**关键创新**：关键创新在于提出了一个可解释的点击诱饵检测框架，该框架不仅能检测点击诱饵，还能将其归因于特定的语言操纵策略。此外，构建了一个合成数据集，用于训练和评估模型，并促进了对模型行为的详细分析。与现有方法相比，该方法更注重可解释性，能够提供更深入的分析。

**关键设计**：在点击诱饵检测阶段，使用了微调的BERT模型，并尝试了大型语言模型（GPT-4.0和Gemini 2.4 Flash）的零样本和少量样本提示学习。在策略归因阶段，使用了一个专门的基于BERT的分类器，针对不同的点击诱饵策略进行训练。数据集通过预定义的点击诱饵策略目录系统地扩充真实新闻标题生成，保证了数据的质量和多样性。

## 📊 实验亮点

论文构建了一个合成数据集，并在此基础上评估了BERT和大型语言模型在点击诱饵检测和策略归因任务上的性能。实验结果表明，微调的BERT模型在检测任务上表现良好，而大型语言模型在少量样本学习中也展现出潜力。策略归因任务的性能也达到了可接受的水平，验证了该方法的可行性。

## 🎯 应用场景

该研究成果可应用于新闻推荐系统、社交媒体平台和搜索引擎等领域，帮助用户识别和过滤点击诱饵内容，提高信息的可信度。同时，该研究也有助于媒体平台打击虚假信息和操纵性内容，维护健康的在线环境。未来，该技术可进一步发展为自动化的内容审核工具，减轻人工审核的负担。

## 📄 摘要（原文）

> The proliferation of clickbait headlines poses significant challenges to the credibility of information and user trust in digital media. While recent advances in machine learning have improved the detection of manipulative content, the lack of explainability limits their practical adoption. This paper presents a model for explainable clickbait detection that not only identifies clickbait titles but also attributes them to specific linguistic manipulation strategies. We introduce a synthetic dataset generated by systematically augmenting real news headlines using a predefined catalogue of clickbait strategies. This dataset enables controlled experimentation and detailed analysis of model behaviour. We present a two-stage framework for automatic clickbait analysis comprising detection and tactic attribution. In the first stage, we compare a fine-tuned BERT classifier with large language models (LLMs), specifically GPT-4.0 and Gemini 2.4 Flash, under both zero-shot prompting and few-shot prompting enriched with illustrative clickbait headlines and their associated persuasive tactics. In the second stage, a dedicated BERT-based classifier predicts the specific clickbait strategies present in each headline. This work advances the development of transparent and trustworthy AI systems for combating manipulative media content. We share the dataset with the research community at https://github.com/LLM-HITCS25S/ClickbaitTacticsDetection

