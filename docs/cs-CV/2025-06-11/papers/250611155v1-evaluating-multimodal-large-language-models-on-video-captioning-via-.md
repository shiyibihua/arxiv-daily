---
layout: default
title: Evaluating Multimodal Large Language Models on Video Captioning via Monte Carlo Tree Search
---

# Evaluating Multimodal Large Language Models on Video Captioning via Monte Carlo Tree Search

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11155" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11155v1</a>
  <a href="https://arxiv.org/pdf/2506.11155.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11155v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11155v1', 'Evaluating Multimodal Large Language Models on Video Captioning via Monte Carlo Tree Search')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Linhao Yu, Xinguang Ji, Yahui Liu, Fanheng Kong, Chenxi Sun, Jingyuan Zhang, Hongzhi Zhang, V. W., Fuzheng Zhang, Deyi Xiong

**分类**: cs.CV

**发布日期**: 2025-06-11

**备注**: 28 pages; ACL 2025(main)

**🔗 代码/项目**: [GITHUB](https://github.com/tjunlp-lab/MCTS-VCB)

---

## 💡 一句话要点

**提出AutoCaption框架以解决视频字幕生成评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频字幕生成` `多模态大语言模型` `蒙特卡洛树搜索` `自动化评估` `视频理解`

## 📋 核心要点

1. 现有的视频字幕生成方法在关键点创建上存在不足，导致评估结果的有效性和多样性受到限制。
2. 本文提出的AutoCaption框架利用蒙特卡洛树搜索（MCTS）迭代生成多样化的描述性句子，全面提升视频内容的表达能力。
3. 实验表明，MCTS-VCB基准能够有效评估多种MLLMs的字幕生成能力，且通过微调，模型性能显著提升。

## 📝 摘要（中文）

视频字幕生成可以用来评估多模态大语言模型（MLLMs）的视频理解能力。然而，现有基准和评估协议存在关键问题，如关键点创建不足或同质化、数据创建成本高以及评估范围有限。为了解决这些问题，本文提出了一种自动化框架AutoCaption，利用蒙特卡洛树搜索（MCTS）以迭代方式构建多样化的描述性句子（即关键点），全面代表视频内容。该策略使得视频细节（如动作、物体属性、环境细节等）得以持续增强。我们将AutoCaption应用于MCTS-VCB，一个涵盖视频细节的细粒度视频字幕基准，从而实现对MLLMs在视频字幕生成任务上的全面评估。实验结果表明，MCTS-VCB能够有效评估视频字幕生成能力，Gemini-1.5-Pro获得最高F1分数71.2。通过AutoCaption生成的数据微调InternVL2.5-8B，模型在MCTS-VCB和DREAM-1K上分别提升了25.0%和16.3%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视频字幕生成评估方法中关键点创建不足、数据创建成本高及评估范围有限的问题。现有方法往往无法全面反映视频内容的多样性和复杂性。

**核心思路**：论文提出的AutoCaption框架通过蒙特卡洛树搜索（MCTS）技术，迭代生成多样化的描述性句子，以全面表达视频内容的细节。这种设计使得生成的字幕更具信息量和多样性。

**技术框架**：AutoCaption框架主要包括数据输入模块、MCTS搜索模块和输出生成模块。数据输入模块负责接收视频数据，MCTS搜索模块通过迭代生成关键点并优化描述，输出生成模块则将最终的描述性句子呈现出来。

**关键创新**：最重要的技术创新在于将MCTS应用于视频字幕生成，通过迭代优化生成的描述性句子，显著提升了字幕的多样性和信息量。这与传统方法的静态生成方式形成了鲜明对比。

**关键设计**：在参数设置上，MCTS的搜索深度和宽度可以根据视频内容的复杂性进行调整。损失函数设计上，考虑了生成句子的多样性和准确性，确保生成的字幕既丰富又符合视频内容。

## 📊 实验亮点

实验结果显示，MCTS-VCB基准能够全面评估视频字幕生成能力，其中Gemini-1.5-Pro获得最高F1分数71.2。通过AutoCaption生成的数据微调InternVL2.5-8B，模型在MCTS-VCB和DREAM-1K上分别提升了25.0%和16.3%，验证了AutoCaption的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括视频内容分析、自动化字幕生成和多模态学习等。通过提升视频理解能力，AutoCaption框架能够为教育、娱乐和社交媒体等行业提供更智能的内容处理方案，未来可能推动视频分析技术的广泛应用。

## 📄 摘要（原文）

> Video captioning can be used to assess the video understanding capabilities of Multimodal Large Language Models (MLLMs). However, existing benchmarks and evaluation protocols suffer from crucial issues, such as inadequate or homogeneous creation of key points, exorbitant cost of data creation, and limited evaluation scopes. To address these issues, we propose an automatic framework, named AutoCaption, which leverages Monte Carlo Tree Search (MCTS) to construct numerous and diverse descriptive sentences (\textit{i.e.}, key points) that thoroughly represent video content in an iterative way. This iterative captioning strategy enables the continuous enhancement of video details such as actions, objects' attributes, environment details, etc. We apply AutoCaption to curate MCTS-VCB, a fine-grained video caption benchmark covering video details, thereby enabling a comprehensive evaluation of MLLMs on the video captioning task. We evaluate more than 20 open- and closed-source MLLMs of varying sizes on MCTS-VCB. Results show that MCTS-VCB can effectively and comprehensively evaluate the video captioning capability, with Gemini-1.5-Pro achieving the highest F1 score of 71.2. Interestingly, we fine-tune InternVL2.5-8B with the AutoCaption-generated data, which helps the model achieve an overall improvement of 25.0% on MCTS-VCB and 16.3% on DREAM-1K, further demonstrating the effectiveness of AutoCaption. The code and data are available at https://github.com/tjunlp-lab/MCTS-VCB.

