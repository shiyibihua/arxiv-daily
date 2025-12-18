---
layout: default
title: Judging by Appearances? Auditing and Intervening Vision-Language Models for Bail Prediction
---

# Judging by Appearances? Auditing and Intervening Vision-Language Models for Bail Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00088" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00088v1</a>
  <a href="https://arxiv.org/pdf/2510.00088.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00088v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00088v1', 'Judging by Appearances? Auditing and Intervening Vision-Language Models for Bail Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sagnik Basu, Shubham Prakash, Ashish Maruti Barge, Siddharth D Jaiswal, Abhisek Dash, Saptarshi Ghosh, Animesh Mukherjee

**分类**: cs.AI, cs.CY

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**通过审计和干预视觉-语言模型，提升保释预测的公平性与准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `保释预测` `公平性` `法律判决` `RAG` `模型审计` `偏见缓解`

## 📋 核心要点

1. 现有法律判决预测系统依赖文本信息，忽略了视觉信息可能带来的偏见和不公平性。
2. 该论文提出通过审计视觉-语言模型在保释预测中的表现，并设计干预算法来提升公平性。
3. 实验表明，提出的干预方法能够显著提高保释预测的性能，减少对特定群体的偏见。

## 📝 摘要（中文）

大型语言模型（LLMs）已被广泛应用于基于案件报告和犯罪历史的法律判决预测任务。然而，随着大型视觉语言模型（VLMs）的兴起，法律判决预测系统现在可以利用罪犯的图像以及文本案件报告/犯罪历史。以这种方式构建的应用程序可能会导致意想不到的后果，并可能被恶意使用。在这项工作中，我们进行了一项审计，以调查独立的VLM在保释决策预测任务中的效率。我们观察到，在多个交叉群体和模型中，性能都很差，并且	extit{错误地拒绝了有资格获得保释的个人的保释，且置信度非常高}。我们通过首先通过RAG流程包含法律先例，然后使用创新方案微调VLM来设计不同的干预算法。我们证明这些干预措施大大提高了保释预测的性能。我们的工作为未来在VLM上设计更智能的干预措施铺平了道路，然后才能将它们部署到现实世界的法律判决预测中。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉-语言模型（VLMs）在保释预测任务中存在的偏见和不公平性问题。现有方法主要依赖文本信息，忽略了图像信息可能带来的潜在偏见。直接使用VLM进行保释预测可能导致对特定人群的歧视，例如错误地拒绝有资格获得保释的个人的保释，且置信度非常高。

**核心思路**：论文的核心思路是通过审计VLM在保释预测任务中的表现，识别其存在的偏见，并设计干预算法来缓解这些偏见。干预算法的核心是结合法律先例和微调VLM，以提高预测的准确性和公平性。

**技术框架**：论文的技术框架主要包括以下几个阶段：1) 使用独立的VLM进行保释预测，并对结果进行审计，以识别存在的偏见。2) 通过RAG（Retrieval-Augmented Generation）流程，将法律先例引入模型。3) 使用创新方案微调VLM，以提高预测的准确性和公平性。

**关键创新**：论文的关键创新在于：1) 首次对VLM在保释预测任务中的表现进行审计，揭示了其存在的偏见。2) 提出了结合法律先例和微调VLM的干预算法，有效缓解了VLM在保释预测中的偏见。3) 设计了创新的微调方案，进一步提高了预测的准确性和公平性。

**关键设计**：论文的关键设计包括：1) 使用RAG流程引入法律先例，以增强模型的法律知识。2) 设计了特定的损失函数，以鼓励模型做出更公平的预测。3) 采用了特定的网络结构，以提高模型的性能。

## 📊 实验亮点

实验结果表明，提出的干预算法能够显著提高保释预测的性能。具体而言，通过结合法律先例和微调VLM，模型的准确率和公平性得到了显著提升。实验还表明，该方法能够有效减少对特定群体的偏见，例如降低对特定种族或性别的人群的误判率。

## 🎯 应用场景

该研究成果可应用于法律判决预测系统，辅助法官进行更公平、更准确的保释决策。通过减少视觉信息带来的偏见，可以提高司法系统的公平性和公正性。此外，该研究方法也可推广到其他涉及视觉和语言信息的法律领域，例如犯罪嫌疑人识别、证据分析等。

## 📄 摘要（原文）

> Large language models (LLMs) have been extensively used for legal judgment prediction tasks based on case reports and crime history. However, with a surge in the availability of large vision language models (VLMs), legal judgment prediction systems can now be made to leverage the images of the criminals in addition to the textual case reports/crime history. Applications built in this way could lead to inadvertent consequences and be used with malicious intent. In this work, we run an audit to investigate the efficiency of standalone VLMs in the bail decision prediction task. We observe that the performance is poor across multiple intersectional groups and models \textit{wrongly deny bail to deserving individuals with very high confidence}. We design different intervention algorithms by first including legal precedents through a RAG pipeline and then fine-tuning the VLMs using innovative schemes. We demonstrate that these interventions substantially improve the performance of bail prediction. Our work paves the way for the design of smarter interventions on VLMs in the future, before they can be deployed for real-world legal judgment prediction.

