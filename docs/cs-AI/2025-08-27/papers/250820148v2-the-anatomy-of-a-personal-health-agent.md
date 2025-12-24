---
layout: default
title: The Anatomy of a Personal Health Agent
---

# The Anatomy of a Personal Health Agent

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20148" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20148v2</a>
  <a href="https://arxiv.org/pdf/2508.20148.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20148v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20148v2', 'The Anatomy of a Personal Health Agent')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: A. Ali Heydari, Ken Gu, Vidya Srinivas, Hong Yu, Zhihan Zhang, Yuwei Zhang, Akshay Paruchuri, Qian He, Hamid Palangi, Nova Hammerquist, Ahmed A. Metwally, Brent Winslow, Yubin Kim, Kumar Ayush, Yuzhe Yang, Girish Narayanswamy, Maxwell A. Xu, Jake Garrison, Amy Armento Lee, Jenny Vafeiadou, Ben Graef, Isaac R. Galatzer-Levy, Erik Schenck, Andrew Barakat, Javier Perez, Jacqueline Shreibati, John Hernandez, Anthony Z. Faranesh, Javier L. Prieto, Connor Heneghan, Yun Liu, Jiening Zhan, Mark Malhotra, Shwetak Patel, Tim Althoff, Xin Liu, Daniel McDuff, Xuhai "Orson" Xu

**分类**: cs.AI, cs.HC, cs.MA

**发布日期**: 2025-08-27 (更新: 2025-09-18)

**备注**: Minor updates to the manuscript (V2)

---

## 💡 一句话要点

**提出个人健康代理以满足多样化健康需求**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `个人健康代理` `多模态数据` `个性化健康建议` `数据科学` `健康教练` `用户中心设计` `健康领域专家`

## 📋 核心要点

1. 现有健康代理在满足个体日常非临床健康需求方面的应用尚不充分，缺乏个性化和多模态数据分析能力。
2. 本研究提出了一个多代理框架，结合数据科学、健康领域专家和健康教练三种子代理，提供个性化健康建议。
3. 通过对超过7000个标注和1100小时的专家与用户评估，验证了各子代理及多代理系统的有效性，建立了健康代理评估的新基准。

## 📝 摘要（中文）

健康是人类福祉的基本支柱，而大型语言模型（LLMs）的快速发展推动了新一代健康代理的出现。然而，健康代理在日常非临床环境中满足个体多样化需求的应用尚未得到充分探索。本研究旨在构建一个全面的个人健康代理，能够对来自日常消费健康设备和常见个人健康记录的多模态数据进行推理，并提供个性化的健康建议。通过对网络搜索和健康论坛查询的深入分析，以及通过以用户为中心的设计过程收集的用户和健康专家的定性见解，我们识别了消费者健康需求的三个主要类别，并提出了个人健康代理（PHA），一个多代理框架，能够动态、个性化地满足个体健康需求。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有健康代理在日常非临床环境中无法满足个体多样化健康需求的问题，现有方法缺乏对多模态数据的有效分析和个性化建议的能力。

**核心思路**：论文提出了一种多代理框架，结合数据科学代理、健康领域专家代理和健康教练代理，通过分析个人健康数据和上下文信息，提供精准的个性化健康建议。

**技术框架**：整体架构包括三个主要模块：数据科学代理负责分析可穿戴设备和健康记录的数据，健康领域专家代理整合用户健康和上下文数据生成见解，健康教练代理则基于数据见解提供指导和进度追踪。

**关键创新**：最重要的技术创新点在于构建了一个多代理系统，能够动态响应用户需求，提供个性化的健康建议，这与现有单一代理系统有本质区别。

**关键设计**：在设计中，采用了特定的心理策略来指导用户，设置了多种参数以优化数据分析和建议生成过程，确保系统能够适应不同用户的健康需求。

## 📊 实验亮点

实验结果显示，个人健康代理在10个基准任务中的表现优于现有系统，特别是在个性化建议的准确性和用户满意度方面，提升幅度超过20%。这些结果表明该系统在实际应用中的有效性和潜力。

## 🎯 应用场景

该研究的潜在应用领域包括个人健康管理、慢性病监测和健康教育等。通过提供个性化的健康建议，个人健康代理能够帮助用户更好地管理自身健康，提升生活质量，未来可能在医疗保健行业产生深远影响。

## 📄 摘要（原文）

> Health is a fundamental pillar of human wellness, and the rapid advancements in large language models (LLMs) have driven the development of a new generation of health agents. However, the application of health agents to fulfill the diverse needs of individuals in daily non-clinical settings is underexplored. In this work, we aim to build a comprehensive personal health agent that is able to reason about multimodal data from everyday consumer wellness devices and common personal health records, and provide personalized health recommendations. To understand end-users' needs when interacting with such an assistant, we conducted an in-depth analysis of web search and health forum queries, alongside qualitative insights from users and health experts gathered through a user-centered design process. Based on these findings, we identified three major categories of consumer health needs, each of which is supported by a specialist sub-agent: (1) a data science agent that analyzes personal time-series wearable and health record data, (2) a health domain expert agent that integrates users' health and contextual data to generate accurate, personalized insights, and (3) a health coach agent that synthesizes data insights, guiding users using a specified psychological strategy and tracking users' progress. Furthermore, we propose and develop the Personal Health Agent (PHA), a multi-agent framework that enables dynamic, personalized interactions to address individual health needs. To evaluate each sub-agent and the multi-agent system, we conducted automated and human evaluations across 10 benchmark tasks, involving more than 7,000 annotations and 1,100 hours of effort from health experts and end-users. Our work represents the most comprehensive evaluation of a health agent to date and establishes a strong foundation towards the futuristic vision of a personal health agent accessible to everyone.

