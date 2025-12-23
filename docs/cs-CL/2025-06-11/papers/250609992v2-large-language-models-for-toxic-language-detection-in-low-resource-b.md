---
layout: default
title: Large Language Models for Toxic Language Detection in Low-Resource Balkan Languages
---

# Large Language Models for Toxic Language Detection in Low-Resource Balkan Languages

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09992" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09992v2</a>
  <a href="https://arxiv.org/pdf/2506.09992.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09992v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09992v2', 'Large Language Models for Toxic Language Detection in Low-Resource Balkan Languages')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Amel Muminovic, Amela Kadric Muminovic

**分类**: cs.CL

**发布日期**: 2025-06-11 (更新: 2025-06-13)

**备注**: 8 pages

---

## 💡 一句话要点

**利用大型语言模型检测低资源巴尔干语言中的有毒语言**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `有毒语言检测` `大型语言模型` `低资源语言` `上下文增强` `社交媒体评论` `性能评估` `巴尔干语言` `机器学习`

## 📋 核心要点

1. 现有方法在低资源语言环境中缺乏有效的有毒语言检测工具，导致在线有毒语言的监管不足。
2. 本文提出利用大型语言模型，通过添加上下文信息来提升对有毒评论的检测能力，尤其是在数据稀缺的情况下。
3. 实验结果表明，Gemini模型在上下文增强模式下达到0.82的F1分数，且零样本的GPT-4.1在精确度上表现最佳，显示出显著的性能提升。

## 📝 摘要（中文）

在线有毒语言对社会造成了实际伤害，尤其是在缺乏有效监管工具的地区。本文评估了大型语言模型在塞尔维亚语、克罗地亚语和波斯尼亚语中处理有毒评论的能力。我们构建并手动标注了一个包含4500条来自YouTube和TikTok评论的数据集，涵盖音乐、政治、体育等多种类别。测试了四种模型（GPT-3.5 Turbo、GPT-4.1、Gemini 1.5 Pro和Claude 3 Opus），并在零样本和上下文增强两种模式下进行评估。结果显示，添加短上下文片段平均提高了0.12的召回率，并使F1分数提高了最高0.10，尽管有时会增加误报。Gemini在上下文增强模式下表现最佳，F1分数和准确率均达到0.82，而零样本的GPT-4.1在精确度上领先，且误报率最低。研究表明，最小上下文的添加可以改善低资源环境中的有毒语言检测，并建议改进提示设计和阈值校准等实际策略。

## 🔬 方法详解

**问题定义**：本文旨在解决在低资源巴尔干语言（如塞尔维亚语、克罗地亚语和波斯尼亚语）中，有毒语言检测的有效性不足的问题。现有方法在缺乏标注数据的情况下，难以准确识别有毒评论。

**核心思路**：论文的核心思路是利用大型语言模型的强大能力，通过添加上下文信息来提升有毒语言的检测效果。这种设计旨在利用上下文信息来提高模型的召回率和F1分数。

**技术框架**：整体架构包括数据集构建、模型选择与训练、性能评估等多个阶段。首先，手动标注数据集，然后在不同的模型（如GPT-3.5 Turbo、GPT-4.1等）上进行零样本和上下文增强的测试，最后评估模型的精确度、召回率等指标。

**关键创新**：最重要的技术创新点在于通过上下文增强的方式显著提高了有毒语言检测的性能，尤其是在数据稀缺的情况下。这与传统的仅依赖于模型本身的检测方法有本质区别。

**关键设计**：在实验中，关键的参数设置包括上下文片段的长度、模型的选择以及评估指标的定义。损失函数和网络结构的具体细节未在摘要中详细说明，需参考原文获取更多信息。

## 📊 实验亮点

实验结果显示，Gemini模型在上下文增强模式下达到了0.82的F1分数和准确率，而零样本的GPT-4.1在精确度上表现最佳，且误报率最低。这表明，通过优化提示设计和上下文信息的使用，可以显著提升有毒语言检测的效果。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体平台、在线评论系统和内容审核工具，尤其是在巴尔干地区的低资源语言环境中。通过有效检测有毒语言，可以改善用户体验，促进健康的在线交流环境。未来，该方法还可以扩展到其他低资源语言的有毒语言检测中，具有广泛的社会价值。

## 📄 摘要（原文）

> Online toxic language causes real harm, especially in regions with limited moderation tools. In this study, we evaluate how large language models handle toxic comments in Serbian, Croatian, and Bosnian, languages with limited labeled data. We built and manually labeled a dataset of 4,500 YouTube and TikTok comments drawn from videos across diverse categories, including music, politics, sports, modeling, influencer content, discussions of sexism, and general topics. Four models (GPT-3.5 Turbo, GPT-4.1, Gemini 1.5 Pro, and Claude 3 Opus) were tested in two modes: zero-shot and context-augmented. We measured precision, recall, F1 score, accuracy and false positive rates. Including a short context snippet raised recall by about 0.12 on average and improved F1 score by up to 0.10, though it sometimes increased false positives. The best balance came from Gemini in context-augmented mode, reaching an F1 score of 0.82 and accuracy of 0.82, while zero-shot GPT-4.1 led on precision and had the lowest false alarms. We show how adding minimal context can improve toxic language detection in low-resource settings and suggest practical strategies such as improved prompt design and threshold calibration. These results show that prompt design alone can yield meaningful gains in toxicity detection for underserved Balkan language communities.

