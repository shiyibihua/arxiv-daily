---
layout: default
title: Do We Talk to Robots Like Therapists, and Do They Respond Accordingly? Language Alignment in AI Emotional Support
---

# Do We Talk to Robots Like Therapists, and Do They Respond Accordingly? Language Alignment in AI Emotional Support

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16473" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16473v1</a>
  <a href="https://arxiv.org/pdf/2506.16473.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16473v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16473v1', 'Do We Talk to Robots Like Therapists, and Do They Respond Accordingly? Language Alignment in AI Emotional Support')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sophie Chiang, Guy Laban, Hatice Gunes

**分类**: cs.HC, cs.AI, cs.CL

**发布日期**: 2025-06-19

---

## 💡 一句话要点

**探讨情感支持机器人与人类治疗师对话的相似性与响应机制**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感支持` `对话代理` `心理健康` `人机交互` `主题聚类` `语义分析` `机器人治疗`

## 📋 核心要点

1. 现有的情感支持机器人与人类治疗师之间的对话相似性尚未得到充分研究，缺乏系统的比较分析。
2. 本研究通过分析用户与治疗师及机器人之间的对话数据，采用句子嵌入和K均值聚类方法，评估对话主题的一致性。
3. 实验结果表明，机器人对话内容与人类治疗师的主题结构高度一致，且在回应相似主题时具有显著的语义重叠。

## 📝 摘要（中文）

随着对话代理在情感支持对话中的应用日益增多，理解其互动与传统治疗环境的相似性变得至关重要。本研究调查了与机器人分享的关注点是否与人际治疗会话中的关注点一致，以及机器人响应是否在语义上与人类治疗师的响应相似。通过分析用户与专业治疗师的互动数据集和与社交机器人QTrobot的支持性对话数据集，研究发现90.88%的机器人对话内容可以映射到人类治疗数据集的主题结构，表明两者在主题结构上的共享。结果显示，机器人和人类治疗师在回应相似主题时的语义重叠显著，突显了机器人支持对话的潜力及其在心理健康干预中的应用前景。

## 🔬 方法详解

**问题定义**：本研究旨在解决情感支持机器人与人类治疗师之间对话内容和响应机制的相似性问题。现有方法缺乏对这两者互动的系统性比较，无法明确其在心理支持中的有效性。

**核心思路**：通过分析用户与专业治疗师的对话数据集与社交机器人QTrobot的对话数据集，研究者采用句子嵌入和K均值聚类方法，评估机器人与人类治疗师在主题和响应上的一致性。

**技术框架**：研究分为数据收集、主题聚类和语义比较三个主要阶段。首先收集人类治疗师与用户的对话数据，然后对机器人与用户的对话进行聚类分析，最后比较两者在主题和响应上的相似性。

**关键创新**：本研究的创新点在于采用距离基础的聚类拟合方法，评估不同代理类型的响应是否能够映射到另一代理的主题聚类中，从而揭示了机器人与人类治疗师之间的语义重叠。

**关键设计**：使用Transformer、Word2Vec和BERT嵌入对对话内容进行语义分析，结合欧几里得距离验证聚类结果的有效性，确保了分析的准确性和可靠性。

## 📊 实验亮点

实验结果显示，90.88%的机器人对话内容能够映射到人类治疗数据集的主题聚类，表明两者在主题结构上的高度一致性。此外，机器人和人类治疗师在回应相似主题时的语义重叠显著，进一步验证了机器人在情感支持中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括心理健康干预、情感支持机器人开发及人机交互设计。通过提高机器人在情感支持对话中的有效性，可能为心理健康领域提供新的辅助工具，帮助更多需要支持的人群。未来，情感支持机器人有望在临床和家庭环境中发挥更大作用。

## 📄 摘要（原文）

> As conversational agents increasingly engage in emotionally supportive dialogue, it is important to understand how closely their interactions resemble those in traditional therapy settings. This study investigates whether the concerns shared with a robot align with those shared in human-to-human (H2H) therapy sessions, and whether robot responses semantically mirror those of human therapists. We analyzed two datasets: one of interactions between users and professional therapists (Hugging Face's NLP Mental Health Conversations), and another involving supportive conversations with a social robot (QTrobot from LuxAI) powered by a large language model (LLM, GPT-3.5). Using sentence embeddings and K-means clustering, we assessed cross-agent thematic alignment by applying a distance-based cluster-fitting method that evaluates whether responses from one agent type map to clusters derived from the other, and validated it using Euclidean distances. Results showed that 90.88% of robot conversation disclosures could be mapped to clusters from the human therapy dataset, suggesting shared topical structure. For matched clusters, we compared the subjects as well as therapist and robot responses using Transformer, Word2Vec, and BERT embeddings, revealing strong semantic overlap in subjects' disclosures in both datasets, as well as in the responses given to similar human disclosure themes across agent types (robot vs. human therapist). These findings highlight both the parallels and boundaries of robot-led support conversations and their potential for augmenting mental health interventions.

