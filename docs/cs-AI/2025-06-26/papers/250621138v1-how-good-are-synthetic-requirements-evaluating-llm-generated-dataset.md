---
layout: default
title: How Good Are Synthetic Requirements ? Evaluating LLM-Generated Datasets for AI4RE
---

# How Good Are Synthetic Requirements ? Evaluating LLM-Generated Datasets for AI4RE

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21138" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21138v1</a>
  <a href="https://arxiv.org/pdf/2506.21138.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21138v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21138v1', 'How Good Are Synthetic Requirements ? Evaluating LLM-Generated Datasets for AI4RE')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abdelkarim El-Hajjami, Camille Salinesi

**分类**: cs.SE, cs.AI

**发布日期**: 2025-06-26

---

## 💡 一句话要点

**提出Synthline v1以解决AI4RE数据集匮乏问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `合成数据生成` `需求工程` `人工智能` `数据质量优化` `多样本提示` `自动化优化` `软件开发` `机器学习`

## 📋 核心要点

1. 现有的公开标注需求数据集稀缺，限制了人工智能在需求工程中的应用与发展。
2. 提出Synthline v1，通过改进的生成策略和数据整理技术，系统性地生成合成需求数据。
3. 实验结果显示，多样本提示显著提升数据质量，合成需求在多个任务上超越人类数据，尤其在安全性和缺陷分类任务上表现突出。

## 📝 摘要（中文）

现有公开标注的需求数据集短缺，严重制约了需求工程领域的人工智能发展。本文提出Synthline v1，一个增强的产品线方法，通过先进的生成策略和数据整理技术生成合成需求数据。研究了提示策略、自动化提示优化和后生成整理对数据质量的影响，结果表明多样本提示显著提升了数据的效用和多样性，F1分数提升6至44点。使用PACE进行自动化提示优化在功能分类任务上提升了32.5点，但在其他任务上表现不佳。合成需求在特定任务上可与人类撰写的需求相媲美，甚至在安全性和缺陷分类任务上超越人类数据。此研究为AI4RE提供了实用见解，并为合成数据生成提供了可行路径。

## 🔬 方法详解

**问题定义**：本研究旨在解决需求工程领域中公开标注需求数据集的短缺问题。现有方法在生成合成数据时缺乏系统性控制和优化，导致生成数据质量不高。

**核心思路**：论文提出Synthline v1，通过增强的产品线方法，结合先进的生成策略和数据整理技术，系统性地生成高质量的合成需求数据。

**技术框架**：整体架构包括数据生成、提示策略优化和后生成整理三个主要模块。首先，通过多样本提示生成合成需求；其次，使用PACE技术进行提示优化；最后，对生成的数据进行整理以提升质量。

**关键创新**：最重要的创新点在于引入了多样本提示和自动化提示优化策略，显著提升了合成数据的效用和多样性，与传统的单样本生成方法相比，效果更佳。

**关键设计**：在提示策略中，采用了多样本提示以增加数据多样性；在自动化优化中，使用了PACE方法，针对不同任务调整优化策略；数据整理过程中，采用相似性基础的整理方法，尽管可能影响分类性能，但提升了数据多样性。

## 📊 实验亮点

实验结果显示，多样本提示在数据生成中显著提升了F1分数，提升幅度从6到44点不等。使用PACE进行自动化提示优化在功能分类任务上提升了32.5点，而合成需求在安全性和缺陷分类任务上分别超越人类数据7.8点和15.4点，显示出合成数据的强大潜力。

## 🎯 应用场景

该研究的潜在应用领域包括需求工程、软件开发和人工智能系统设计。通过生成高质量的合成需求数据，可以有效缓解数据集稀缺问题，推动相关领域的研究与应用，提升人工智能在需求分析中的表现，未来可能影响软件工程的整个生命周期。

## 📄 摘要（原文）

> The shortage of publicly available, labeled requirements datasets remains a major barrier to advancing Artificial Intelligence for Requirements Engineering (AI4RE). While Large Language Models offer promising capabilities for synthetic data generation, systematic approaches to control and optimize the quality of generated requirements remain underexplored. This paper presents Synthline v1, an enhanced Product Line approach for generating synthetic requirements data that extends our earlier v0 version with advanced generation strategies and curation techniques. We investigate four research questions assessing how prompting strategies, automated prompt optimization, and post-generation curation affect data quality across four classification tasks: defect detection, functional vs. non-functional, quality vs. non-quality, and security vs. non-security. Our evaluation shows that multi-sample prompting significantly boosts both utility and diversity over single-sample generation, with F1-score gains from 6 to 44 points. The use of PACE (Prompt Actor-Critic Editing) for automated prompt optimization yields task-dependent results, greatly improving functional classification (+32.5 points) but reducing performance on others. Interestingly, similarity-based curation improves diversity but often harms classification performance, indicating that some redundancy may help ML models. Most importantly, our results show that synthetic requirements can match or outperform human-authored ones for specific tasks, with synthetic data surpassing human data for security (+7.8 points) and defect classification (+15.4 points). These findings offer practical insights for AI4RE and chart a viable path to mitigating dataset scarcity through systematic synthetic generation.

