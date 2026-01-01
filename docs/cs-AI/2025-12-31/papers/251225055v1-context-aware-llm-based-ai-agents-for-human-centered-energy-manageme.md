---
layout: default
title: Context-aware LLM-based AI Agents for Human-centered Energy Management Systems in Smart Buildings
---

# Context-aware LLM-based AI Agents for Human-centered Energy Management Systems in Smart Buildings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.25055" class="toolbar-btn" target="_blank">📄 arXiv: 2512.25055v1</a>
  <a href="https://arxiv.org/pdf/2512.25055.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.25055v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.25055v1', 'Context-aware LLM-based AI Agents for Human-centered Energy Management Systems in Smart Buildings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianzhi He, Farrokh Jazizadeh

**分类**: cs.AI, cs.HC

**发布日期**: 2025-12-31

---

## 💡 一句话要点

**提出基于LLM的智能建筑能源管理AI Agent，实现情境感知能源管理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `智能建筑` `能源管理系统` `大型语言模型` `AI Agent` `情境感知` `自然语言交互` `能源效率`

## 📋 核心要点

1. 现有能源管理系统缺乏情境感知能力，难以根据用户需求和环境变化进行智能调节。
2. 利用LLM的自然语言处理和数据分析能力，构建情境感知的BEMS AI Agent，实现智能能源管理。
3. 实验结果表明，该Agent在设备控制、记忆任务和能源分析方面表现良好，但在成本估算方面仍需改进。

## 📝 摘要（中文）

本研究提出了一个基于大型语言模型（LLM）的建筑能源管理系统（BEMS）AI Agent的概念框架和一个原型评估，旨在通过自然语言交互促进智能建筑中的情境感知能源管理。该框架包含感知（传感）、中央控制（大脑）和行动（驱动和用户交互）三个模块，形成一个闭环反馈系统，捕获、分析和解释能源数据，从而智能地响应用户查询并管理连接的设备。通过利用LLM的自主数据分析能力，BEMS AI Agent旨在提供关于能源消耗、成本预测和设备调度的情境感知洞察，从而解决现有能源管理系统的局限性。使用120个用户查询，在四个不同的真实住宅能源数据集上，通过延迟、功能、能力、准确性和成本效益等指标评估了原型的性能。使用方差分析（ANOVA）测试证明了该框架的通用性。结果显示出良好的性能，设备控制的响应准确率为86%，记忆相关任务为97%，调度和自动化为74%，能源分析为77%，而更复杂的成本估算任务的准确率为49%，表明仍有改进空间。这项基准研究旨在规范基于LLM的BEMS AI Agent的评估，并确定未来的研究方向，强调响应准确性和计算效率之间的权衡。

## 🔬 方法详解

**问题定义**：现有建筑能源管理系统（BEMS）在情境感知和用户交互方面存在不足。传统系统难以理解用户的自然语言指令，无法根据用户的具体需求和环境变化进行智能调节，导致能源浪费和用户体验不佳。此外，现有系统的数据分析能力有限，难以提供深入的能源消耗洞察和准确的成本预测。

**核心思路**：本研究的核心思路是利用大型语言模型（LLM）的强大自然语言处理和数据分析能力，构建一个情境感知的BEMS AI Agent。该Agent能够理解用户的自然语言查询，分析建筑的能源数据，并根据用户的需求和环境变化智能地控制连接的设备，从而实现更高效、更智能的能源管理。这样设计的目的是为了弥合现有BEMS在用户交互和情境感知方面的差距。

**技术框架**：该框架包含三个主要模块：感知（sensing）、中央控制（brain）和行动（actuation and user interaction）。感知模块负责收集建筑的能源数据和用户输入；中央控制模块，即基于LLM的AI Agent，负责分析数据、理解用户意图并生成控制指令；行动模块负责执行控制指令，例如调节设备或向用户提供反馈。这三个模块形成一个闭环反馈系统，持续优化能源管理策略。

**关键创新**：最重要的技术创新点在于将LLM应用于BEMS，赋予系统自然语言交互和情境感知能力。与传统的基于规则或机器学习的BEMS相比，该方法能够更好地理解用户的需求，并根据环境变化进行自适应调节。此外，LLM的自主数据分析能力能够提供更深入的能源消耗洞察，帮助用户更好地了解和控制能源使用。

**关键设计**：该研究使用了预训练的LLM，并通过微调使其适应BEMS的应用场景。用户通过自然语言与Agent交互，Agent将用户的查询转化为可执行的指令。研究中使用了不同的评估指标，包括延迟、功能、能力、准确性和成本效益，以全面评估Agent的性能。此外，研究还使用了方差分析（ANOVA）测试来验证框架的通用性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.25055v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.25055v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.25055v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该Agent在设备控制方面达到了86%的准确率，在记忆相关任务中达到了97%的准确率，在调度和自动化方面达到了74%的准确率，在能源分析方面达到了77%的准确率。虽然在成本估算方面准确率较低（49%），但整体性能表明基于LLM的BEMS AI Agent具有很大的潜力。

## 🎯 应用场景

该研究成果可应用于智能家居、智能办公楼等各种建筑环境，实现更高效、更智能的能源管理。通过自然语言交互，用户可以轻松地控制和优化能源使用，降低能源成本，提高生活质量。未来，该技术有望与智能电网等基础设施集成，实现更广泛的能源优化和可持续发展。

## 📄 摘要（原文）

> This study presents a conceptual framework and a prototype assessment for Large Language Model (LLM)-based Building Energy Management System (BEMS) AI agents to facilitate context-aware energy management in smart buildings through natural language interaction. The proposed framework comprises three modules: perception (sensing), central control (brain), and action (actuation and user interaction), forming a closed feedback loop that captures, analyzes, and interprets energy data to respond intelligently to user queries and manage connected appliances. By leveraging the autonomous data analytics capabilities of LLMs, the BEMS AI agent seeks to offer context-aware insights into energy consumption, cost prediction, and device scheduling, thereby addressing limitations in existing energy management systems. The prototype's performance was evaluated using 120 user queries across four distinct real-world residential energy datasets and different evaluation metrics, including latency, functionality, capability, accuracy, and cost-effectiveness. The generalizability of the framework was demonstrated using ANOVA tests. The results revealed promising performance, measured by response accuracy in device control (86%), memory-related tasks (97%), scheduling and automation (74%), and energy analysis (77%), while more complex cost estimation tasks highlighted areas for improvement with an accuracy of 49%. This benchmarking study moves toward formalizing the assessment of LLM-based BEMS AI agents and identifying future research directions, emphasizing the trade-off between response accuracy and computational efficiency.

