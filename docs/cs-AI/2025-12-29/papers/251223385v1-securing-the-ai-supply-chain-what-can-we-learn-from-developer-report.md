---
layout: default
title: "Securing the AI Supply Chain: What Can We Learn From Developer-Reported Security Issues and Solutions of AI Projects?"
---

# Securing the AI Supply Chain: What Can We Learn From Developer-Reported Security Issues and Solutions of AI Projects?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23385" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23385v1</a>
  <a href="https://arxiv.org/pdf/2512.23385.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23385v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23385v1', 'Securing the AI Supply Chain: What Can We Learn From Developer-Reported Security Issues and Solutions of AI Projects?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: The Anh Nguyen, Triet Huynh Minh Le, M. Ali Babar

**分类**: cs.SE, cs.AI, cs.CR, cs.HC

**发布日期**: 2025-12-29

**备注**: Accepted at the 48th IEEE/ACM International Conference on Software Engineering (ICSE 2026) - Research Track

---

## 💡 一句话要点

**通过分析开发者报告的安全问题与解决方案，提升AI供应链安全性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `AI供应链安全` `安全漏洞分析` `开发者报告` `自然语言处理` `深度学习` `安全分类` `Hugging Face` `GitHub`

## 📋 核心要点

1. AI供应链面临传统软件安全问题之外，还存在AI模型和数据带来的新型安全威胁，现有研究对这些威胁的理解不足。
2. 该研究通过分析Hugging Face和GitHub上的开发者讨论，识别并分类AI项目中的安全问题和解决方案。
3. 研究构建了一个包含31万余条安全讨论的数据集，并对753个帖子进行主题分析，揭示了32个安全问题和24个解决方案。

## 📝 摘要（中文）

人工智能模型和应用的快速增长导致安全形势日益复杂。AI项目开发者不仅要应对传统的软件供应链问题，还要应对新型的、AI特有的安全威胁。然而，对于常见的安全问题以及实际的解决方案，我们知之甚少。为了弥合这一差距，我们基于Hugging Face和GitHub上的讨论，对开发者报告的问题和解决方案进行了实证研究。为了识别与安全相关的讨论，我们开发了一个管道，将关键词匹配与优化的微调distilBERT分类器相结合，该分类器在我们对各种深度学习和大型语言模型的广泛比较中取得了最佳性能。该管道生成了一个包含312,868个安全讨论的数据集，提供了对AI应用和项目安全报告实践的见解。我们对从数据集中抽样的753个帖子进行了主题分析，揭示了一个细粒度的分类法，涵盖四个主题的32个安全问题和24个解决方案：（1）系统和软件，（2）外部工具和生态系统，（3）模型，以及（4）数据。我们发现，许多安全问题源于AI组件的复杂依赖关系和黑盒特性。值得注意的是，与模型和数据相关的挑战往往缺乏具体的解决方案。我们的见解可以为开发者和研究人员提供基于证据的指导，以应对AI供应链中的实际安全威胁。

## 🔬 方法详解

**问题定义**：论文旨在解决AI供应链中存在的安全问题，这些问题源于AI模型和应用的复杂性，以及对AI组件（如模型和数据）的依赖。现有方法未能充分识别和解决这些AI特有的安全威胁，导致开发者缺乏有效的安全措施指导。

**核心思路**：论文的核心思路是通过挖掘开发者在Hugging Face和GitHub等平台上的讨论，来了解AI项目中实际遇到的安全问题和解决方案。通过分析这些真实世界的案例，可以更准确地识别AI供应链中的安全风险，并为开发者提供有针对性的安全建议。

**技术框架**：该研究的技术框架主要包括以下几个阶段：1) 数据收集：从Hugging Face和GitHub收集开发者讨论数据。2) 安全讨论识别：开发一个管道，结合关键词匹配和微调的distilBERT分类器，识别与安全相关的讨论。3) 主题分析：对识别出的安全讨论进行抽样，并进行人工主题分析，提取安全问题和解决方案。4) 分类构建：根据主题分析的结果，构建一个细粒度的安全问题和解决方案分类体系。

**关键创新**：该研究的关键创新在于：1) 利用开发者报告的数据，更贴近实际应用场景，避免了传统安全研究的局限性。2) 结合关键词匹配和微调的distilBERT分类器，提高了安全讨论识别的准确率。3) 构建了一个细粒度的AI供应链安全问题和解决方案分类体系，为后续研究提供了基础。

**关键设计**：在安全讨论识别阶段，研究人员对distilBERT模型进行了微调，使其能够更准确地识别与安全相关的文本。此外，在主题分析阶段，研究人员采用了迭代式的编码方法，确保分类体系的完整性和准确性。具体参数设置和损失函数等细节未在论文中详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23385v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23385v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23385v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

研究构建了一个包含312,868个安全讨论的数据集，并对753个帖子进行了主题分析，揭示了32个安全问题和24个解决方案，涵盖系统软件、外部工具、模型和数据四个主题。研究发现，与模型和数据相关的安全问题往往缺乏具体的解决方案，这突显了AI安全研究的挑战。

## 🎯 应用场景

该研究成果可应用于AI开发的安全审计、漏洞挖掘和安全加固。通过了解AI供应链中常见的安全问题和解决方案，开发者可以更有针对性地采取安全措施，降低AI系统的安全风险。研究结果还可以为安全研究人员提供参考，促进AI安全领域的发展。

## 📄 摘要（原文）

> The rapid growth of Artificial Intelligence (AI) models and applications has led to an increasingly complex security landscape. Developers of AI projects must contend not only with traditional software supply chain issues but also with novel, AI-specific security threats. However, little is known about what security issues are commonly encountered and how they are resolved in practice. This gap hinders the development of effective security measures for each component of the AI supply chain. We bridge this gap by conducting an empirical investigation of developer-reported issues and solutions, based on discussions from Hugging Face and GitHub. To identify security-related discussions, we develop a pipeline that combines keyword matching with an optimal fine-tuned distilBERT classifier, which achieved the best performance in our extensive comparison of various deep learning and large language models. This pipeline produces a dataset of 312,868 security discussions, providing insights into the security reporting practices of AI applications and projects. We conduct a thematic analysis of 753 posts sampled from our dataset and uncover a fine-grained taxonomy of 32 security issues and 24 solutions across four themes: (1) System and Software, (2) External Tools and Ecosystem, (3) Model, and (4) Data. We reveal that many security issues arise from the complex dependencies and black-box nature of AI components. Notably, challenges related to Models and Data often lack concrete solutions. Our insights can offer evidence-based guidance for developers and researchers to address real-world security threats across the AI supply chain.

