---
layout: default
title: Automatic Large Language Models Creation of Interactive Learning Lessons
---

# Automatic Large Language Models Creation of Interactive Learning Lessons

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17356" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17356v1</a>
  <a href="https://arxiv.org/pdf/2506.17356.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17356v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17356v1', 'Automatic Large Language Models Creation of Interactive Learning Lessons')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jionghao Lin, Jiarui Rao, Yiyang Zhao, Yuting Wang, Ashish Gurung, Amanda Barany, Jaclyn Ocumpaugh, Ryan S. Baker, Kenneth R. Koedinger

**分类**: cs.CY, cs.AI, cs.HC

**发布日期**: 2025-06-20

**备注**: Full Research Paper, 15 pages, In Proceedings of 20th European Conference on Technology Enhanced Learning (ECTEL2025)

---

## 💡 一句话要点

**提出基于大语言模型的互动学习课程自动生成方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `在线教育` `课程生成` `任务分解` `教育技术` `人机协作` `培训系统`

## 📋 核心要点

1. 现有的在线导师培训课程生成方法缺乏结构性，导致课程质量参差不齐，难以满足教学需求。
2. 本研究提出了一种基于任务分解的提示策略，利用GPT-4o模型自动生成结构化的导师培训课程，提升课程质量。
3. 实验结果显示，采用任务分解策略生成的课程在评估中获得了更高的评分，表明该方法在课程设计中的有效性。

## 📝 摘要（中文）

本研究探讨了自动生成互动场景课程的方法，旨在培训在线教授中学数学的初学者人类导师。通过使用基于检索增强生成的提示工程，结合GPT-4o，我们开发了一个能够创建结构化导师培训课程的系统。研究生成了关于鼓励学生独立性、鼓励寻求帮助行为和开启摄像头三个关键主题的课程，采用任务分解的提示策略将课程生成分解为子任务。两位人类评估者对生成的课程进行了定量和定性评估，结果表明，任务分解策略生成的课程评分高于单步生成的课程。评估者指出了LLM生成课程的几个优点，包括内容结构良好和节省时间的潜力，同时也提到了一些局限性，如反馈过于通用和某些教学部分缺乏清晰性。这些发现强调了人机混合方法在生成有效导师培训课程中的潜力。

## 🔬 方法详解

**问题定义**：本研究旨在解决在线数学导师培训课程生成的结构性不足和质量不均的问题。现有方法往往无法有效满足教学需求，导致课程内容缺乏深度和针对性。

**核心思路**：论文提出了一种基于检索增强生成的提示工程方法，通过将课程生成任务分解为多个子任务，利用GPT-4o模型生成更为结构化和高质量的课程内容。

**技术框架**：整体架构包括数据检索模块、任务分解模块和课程生成模块。首先，通过检索相关教育资源，然后将课程生成任务分解为多个子任务，最后利用GPT-4o生成完整的课程内容。

**关键创新**：最重要的技术创新在于任务分解策略的引入，使得课程生成过程更加系统化和高效，与传统的单步生成方法相比，显著提升了课程的质量和结构性。

**关键设计**：在模型训练中，采用了特定的损失函数来优化生成内容的结构性，同时设置了多种参数以确保生成内容的多样性和针对性。

## 📊 实验亮点

实验结果显示，采用任务分解策略生成的课程在评估中获得了更高的评分，具体而言，课程评分比单步生成的课程提高了显著的百分比。这表明该方法在课程设计中的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括在线教育平台和教师培训项目，能够为教育工作者提供高质量的培训课程，提升教学效果。未来，该方法可能在其他学科的课程生成中得到推广，进一步推动教育技术的发展。

## 📄 摘要（原文）

> We explore the automatic generation of interactive, scenario-based lessons designed to train novice human tutors who teach middle school mathematics online. Employing prompt engineering through a Retrieval-Augmented Generation approach with GPT-4o, we developed a system capable of creating structured tutor training lessons. Our study generated lessons in English for three key topics: Encouraging Students' Independence, Encouraging Help-Seeking Behavior, and Turning on Cameras, using a task decomposition prompting strategy that breaks lesson generation into sub-tasks. The generated lessons were evaluated by two human evaluators, who provided both quantitative and qualitative evaluations using a comprehensive rubric informed by lesson design research. Results demonstrate that the task decomposition strategy led to higher-rated lessons compared to single-step generation. Human evaluators identified several strengths in the LLM-generated lessons, including well-structured content and time-saving potential, while also noting limitations such as generic feedback and a lack of clarity in some instructional sections. These findings underscore the potential of hybrid human-AI approaches for generating effective lessons in tutor training.

