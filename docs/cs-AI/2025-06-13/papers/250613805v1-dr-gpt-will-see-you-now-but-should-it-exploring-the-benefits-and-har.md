---
layout: default
title: Dr. GPT Will See You Now, but Should It? Exploring the Benefits and Harms of Large Language Models in Medical Diagnosis using Crowdsourced Clinical Cases
---

# Dr. GPT Will See You Now, but Should It? Exploring the Benefits and Harms of Large Language Models in Medical Diagnosis using Crowdsourced Clinical Cases

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13805" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13805v1</a>
  <a href="https://arxiv.org/pdf/2506.13805.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13805v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13805v1', 'Dr. GPT Will See You Now, but Should It? Exploring the Benefits and Harms of Large Language Models in Medical Diagnosis using Crowdsourced Clinical Cases')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bonam Mingole, Aditya Majumdar, Firdaus Ahmed Choudhury, Jennifer L. Kraschnewski, Shyam S. Sundar, Amulya Yadav

**分类**: cs.CY, cs.AI

**发布日期**: 2025-06-13

---

## 💡 一句话要点

**提出众包评估方法以解决大语言模型在医疗诊断中的有效性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `医疗诊断` `众包评估` `健康查询` `人工智能` `临床应用`

## 📋 核心要点

1. 现有研究主要评估LLMs在专家健康查询中的表现，缺乏对普通用户日常健康问题的有效性评估。
2. 本文通过众包比赛的方式，评估LLMs在回答212个真实或虚构健康问题中的表现，填补了这一研究空白。
3. 实验结果显示，76%的LLM回答被医生认为准确，且结合医疗知识库的RAG版本可能进一步提升回答质量。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在医疗自我诊断和初步分诊等高风险应用中的广泛使用，关于这些技术在健康相关问题中的有效性、适当性和潜在危害的伦理和实际担忧日益增加。现有研究主要集中在LLMs对专家撰写的健康查询的回答效果，而忽视了普通用户日常健康问题的评估。为填补这一研究空白，本文通过大学级别的比赛，采用众包方法评估LLMs在回答日常健康查询中的有效性。研究发现，212个LLM生成的回答中，76%被医生认为是准确的。此外，结合医疗专业人士的帮助，研究探讨了RAG版本的LLMs是否能提高回答质量。本文旨在提供LLMs在现实世界健康交流中的表现的更深入理解。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在日常健康查询中有效性评估的不足，现有研究未能涵盖普通用户的实际需求。

**核心思路**：通过众包比赛的方式，收集普通用户的健康问题，并由医生评估LLMs的回答，以获得真实世界的有效性数据。

**技术框架**：研究分为几个主要阶段：首先，招募参与者生成健康查询；其次，使用四个公开的LLMs生成回答；最后，由九位认证医生对这些回答进行评估。

**关键创新**：本研究的创新在于采用众包方法评估LLMs在日常健康问题中的表现，填补了现有研究的空白，提供了更具代表性的有效性数据。

**关键设计**：在实验中，使用了212个健康问题，参与者与医生的反馈机制确保了评估的准确性和可靠性。

## 📊 实验亮点

实验结果显示，212个LLM生成的回答中，76%被医生认为是准确的，表明LLMs在日常健康查询中的有效性。同时，结合医疗知识库的RAG版本可能进一步提升回答质量，具有重要的临床应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括医疗咨询、健康管理和智能助手等，能够为医疗行业提供更可靠的AI工具，帮助医生和患者进行有效沟通。未来，随着技术的进步，LLMs在医疗领域的应用将更加广泛，可能会改变传统的医疗服务模式。

## 📄 摘要（原文）

> The proliferation of Large Language Models (LLMs) in high-stakes applications such as medical (self-)diagnosis and preliminary triage raises significant ethical and practical concerns about the effectiveness, appropriateness, and possible harmfulness of the use of these technologies for health-related concerns and queries. Some prior work has considered the effectiveness of LLMs in answering expert-written health queries/prompts, questions from medical examination banks, or queries based on pre-existing clinical cases. Unfortunately, these existing studies completely ignore an in-the-wild evaluation of the effectiveness of LLMs in answering everyday health concerns and queries typically asked by general users, which corresponds to the more prevalent use case for LLMs. To address this research gap, this paper presents the findings from a university-level competition that leveraged a novel, crowdsourced approach for evaluating the effectiveness of LLMs in answering everyday health queries. Over the course of a week, a total of 34 participants prompted four publicly accessible LLMs with 212 real (or imagined) health concerns, and the LLM generated responses were evaluated by a team of nine board-certified physicians. At a high level, our findings indicate that on average, 76% of the 212 LLM responses were deemed to be accurate by physicians. Further, with the help of medical professionals, we investigated whether RAG versions of these LLMs (powered with a comprehensive medical knowledge base) can improve the quality of responses generated by LLMs. Finally, we also derive qualitative insights to explain our quantitative findings by conducting interviews with seven medical professionals who were shown all the prompts in our competition. This paper aims to provide a more grounded understanding of how LLMs perform in real-world everyday health communication.

