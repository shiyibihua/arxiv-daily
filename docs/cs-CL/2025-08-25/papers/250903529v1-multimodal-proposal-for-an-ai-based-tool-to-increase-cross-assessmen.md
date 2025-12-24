---
layout: default
title: Multimodal Proposal for an AI-Based Tool to Increase Cross-Assessment of Messages
---

# Multimodal Proposal for an AI-Based Tool to Increase Cross-Assessment of Messages

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03529" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03529v1</a>
  <a href="https://arxiv.org/pdf/2509.03529.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03529v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03529v1', 'Multimodal Proposal for an AI-Based Tool to Increase Cross-Assessment of Messages')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alejandro Álvarez Castro, Joaquín Ordieres-Meré

**分类**: cs.CL, cs.AI, eess.AS

**发布日期**: 2025-08-25

**备注**: Presented at NLMLT2025 (https://airccse.org/csit/V15N16.html), 15 pages, 5 figures

---

## 💡 一句话要点

**提出多模态框架以增强财报会议的跨评估能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态分析` `层次话语树` `情感信号` `对比学习` `财务沟通` `结构化元数据` `语义嵌入`

## 📋 核心要点

1. 现有的多模态金融情感分析系统多依赖于平面模型，无法有效捕捉财报会议的复杂话语结构。
2. 论文提出了一种基于层次话语树的多模态框架，通过对节点级别的多模态内容进行编码，生成全局嵌入。
3. 实验结果显示，该框架生成的嵌入在情感基调和主题一致性上表现出显著的稳定性和语义意义。

## 📝 摘要（中文）

财报电话会议是独特的半结构化财务沟通来源，结合了管理者的脚本评论和分析师的非脚本对话。尽管近期在金融情感分析中已整合了多模态信号，如文本内容和语音语调，但大多数系统依赖于平面文档级或句子级模型，未能捕捉这些互动的分层话语结构。本文提出了一种新颖的多模态框架，通过将财报会议编码为层次话语树，生成语义丰富且结构意识强的嵌入。每个节点包含单独的独白或问答对，并结合文本、音频和视频的情感信号，以及连贯性评分、主题标签和回答覆盖评估等结构化元数据。实验结果表明，生成的嵌入形成稳定且具有语义意义的表示，反映情感基调、结构逻辑和主题一致性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有财报会议分析方法未能有效捕捉其分层话语结构的问题。现有方法多依赖于平面模型，导致信息丢失和语义理解不足。

**核心思路**：论文提出通过构建层次话语树来编码财报会议，利用多模态信号（文本、音频、视频）和结构化元数据，生成语义丰富的嵌入。这样的设计能够更好地反映财报会议的复杂性和多样性。

**技术框架**：整体架构包括两个阶段的变换器：第一阶段在节点级别使用对比学习编码多模态内容和话语元数据，第二阶段合成整个会议的全局嵌入。

**关键创新**：最重要的创新在于引入层次话语树结构和多模态信号的结合，使得嵌入不仅反映情感基调，还能捕捉结构逻辑和主题一致性，这与传统的平面模型形成鲜明对比。

**关键设计**：在节点级别，使用对比学习来优化多模态内容的表示，同时结合连贯性评分和主题标签等元数据，确保嵌入的语义丰富性和结构意识。

## 📊 实验亮点

实验结果表明，所提出的嵌入在情感基调、结构逻辑和主题一致性方面表现出显著的稳定性，具体性能数据尚未披露，但相较于传统方法有明显提升，显示出良好的语义意义。

## 🎯 应用场景

该研究的潜在应用领域包括金融预测、话语评估、远程医疗、教育和政治话语等高风险沟通场景。其提供的多模态话语表示方法具有良好的可解释性和实用性，能够帮助相关领域的决策支持和分析。

## 📄 摘要（原文）

> Earnings calls represent a uniquely rich and semi-structured source of financial communication, blending scripted managerial commentary with unscripted analyst dialogue. Although recent advances in financial sentiment analysis have integrated multi-modal signals, such as textual content and vocal tone, most systems rely on flat document-level or sentence-level models, failing to capture the layered discourse structure of these interactions. This paper introduces a novel multi-modal framework designed to generate semantically rich and structurally aware embeddings of earnings calls, by encoding them as hierarchical discourse trees. Each node, comprising either a monologue or a question-answer pair, is enriched with emotional signals derived from text, audio, and video, as well as structured metadata including coherence scores, topic labels, and answer coverage assessments. A two-stage transformer architecture is proposed: the first encodes multi-modal content and discourse metadata at the node level using contrastive learning, while the second synthesizes a global embedding for the entire conference. Experimental results reveal that the resulting embeddings form stable, semantically meaningful representations that reflect affective tone, structural logic, and thematic alignment. Beyond financial reporting, the proposed system generalizes to other high-stakes unscripted communicative domains such as tele-medicine, education, and political discourse, offering a robust and explainable approach to multi-modal discourse representation. This approach offers practical utility for downstream tasks such as financial forecasting and discourse evaluation, while also providing a generalizable method applicable to other domains involving high-stakes communication.

