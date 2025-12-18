---
layout: default
title: Generating Energy-Efficient Code via Large-Language Models -- Where are we now?
---

# Generating Energy-Efficient Code via Large-Language Models -- Where are we now?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10099" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10099v1</a>
  <a href="https://arxiv.org/pdf/2509.10099.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10099v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10099v1', 'Generating Energy-Efficient Code via Large-Language Models -- Where are we now?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Radu Apsan, Vincenzo Stoico, Michel Albonico, Rudra Dhar, Karthik Vaidhyanathan, Ivano Malavolta

**分类**: cs.SE, cs.AI

**发布日期**: 2025-09-12

---

## 💡 一句话要点

**评估LLM生成代码的能效：与人类专家代码的对比分析**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `代码生成` `能源效率` `绿色软件工程` `实证研究`

## 📋 核心要点

1. 大型语言模型在软件开发流程中被广泛采用，但其能效表现尚不明确，需要进行深入评估。
2. 该研究通过对比LLM生成代码、人类编写代码和绿色软件专家代码的能耗，评估LLM在节能方面的能力。
3. 实验结果表明，LLM在特定硬件上表现出一定优势，但总体能效仍低于绿色软件专家编写的代码。

## 📝 摘要（中文）

本文旨在评估大型语言模型（LLM）生成的Python代码在能效方面的表现，并将其与人类编写的代码以及绿色软件专家开发的代码进行对比。研究人员使用了EvoEval基准测试中的9个编程问题，测试了6种常见的LLM，并采用了4种不同的提示技术。能耗测量在服务器、PC和Raspberry Pi三个不同的硬件平台上进行，总计耗时约881小时。结果表明，人类解决方案在服务器上能效高16%，在Raspberry Pi上高3%，而LLM在PC上优于人类开发者25%。提示对节能没有一致的影响，最具节能效果的提示因硬件平台而异。绿色软件专家开发的代码在所有硬件平台上始终比所有LLM节能至少17%至30%。结论是，尽管LLM表现出相对良好的代码生成能力，但没有LLM生成的代码比经验丰富的绿色软件开发人员的代码更节能，这表明目前在开发节能Python代码方面仍然非常需要人类专业知识。

## 🔬 方法详解

**问题定义**：论文旨在评估由大型语言模型（LLM）生成的Python代码的能源效率，并将其与人类编写的代码以及绿色软件专家编写的代码进行比较。现有方法缺乏对LLM生成代码能效的系统性评估，尤其是在不同硬件平台和提示策略下的表现。

**核心思路**：核心思路是通过实验对比不同来源（LLM、人类开发者、绿色软件专家）的代码在不同硬件平台上的能耗，从而量化LLM在生成节能代码方面的能力。同时，研究还考察了不同提示策略对LLM生成代码能效的影响。

**技术框架**：该研究的技术框架主要包括以下几个步骤：1) 选择EvoEval基准测试中的9个编程问题；2) 使用6种常见的LLM生成代码，并采用4种不同的提示技术；3) 收集人类开发者和绿色软件专家的解决方案；4) 在服务器、PC和Raspberry Pi三个硬件平台上测量所有解决方案的能耗；5) 对比分析不同来源代码的能耗数据，评估LLM的能效表现。

**关键创新**：该研究的关键创新在于对LLM生成代码的能效进行了全面的实证评估，并将其与人类专家编写的代码进行了直接对比。此外，该研究还考察了不同提示策略和硬件平台对LLM能效的影响，为理解LLM在节能代码生成方面的能力提供了更深入的见解。

**关键设计**：研究中使用了EvoEval基准测试，该基准包含了一系列具有代表性的编程问题。选择了6种广泛使用的LLM，并采用了4种常见的提示技术，以确保实验结果的代表性。能耗测量在三个不同的硬件平台上进行，以考察硬件平台对能效的影响。实验过程中，对所有解决方案的能耗进行了精确测量，并进行了统计分析，以确保结果的可靠性。

## 📊 实验亮点

实验结果表明，人类解决方案在服务器上能效高16%，在Raspberry Pi上高3%，而LLM在PC上优于人类开发者25%。绿色软件专家开发的代码在所有硬件平台上始终比所有LLM节能至少17%至30%。这些数据突显了LLM在特定场景下的优势，以及绿色软件专家在节能方面的专业性。

## 🎯 应用场景

该研究结果可应用于指导软件开发人员选择合适的代码生成工具，并优化LLM的提示策略，以提高代码的能源效率。此外，该研究还可以促进绿色软件工程的发展，推动开发更加节能环保的软件系统。未来的研究可以探索更先进的LLM和更有效的节能技术，进一步提高代码的能源效率。

## 📄 摘要（原文）

> Context. The rise of Large Language Models (LLMs) has led to their widespread adoption in development pipelines. Goal. We empirically assess the energy efficiency of Python code generated by LLMs against human-written code and code developed by a Green software expert. Method. We test 363 solutions to 9 coding problems from the EvoEval benchmark using 6 widespread LLMs with 4 prompting techniques, and comparing them to human-developed solutions. Energy consumption is measured on three different hardware platforms: a server, a PC, and a Raspberry Pi for a total of ~881h (36.7 days). Results. Human solutions are 16% more energy-efficient on the server and 3% on the Raspberry Pi, while LLMs outperform human developers by 25% on the PC. Prompting does not consistently lead to energy savings, where the most energy-efficient prompts vary by hardware platform. The code developed by a Green software expert is consistently more energy-efficient by at least 17% to 30% against all LLMs on all hardware platforms. Conclusions. Even though LLMs exhibit relatively good code generation capabilities, no LLM-generated code was more energy-efficient than that of an experienced Green software developer, suggesting that as of today there is still a great need of human expertise for developing energy-efficient Python code.

