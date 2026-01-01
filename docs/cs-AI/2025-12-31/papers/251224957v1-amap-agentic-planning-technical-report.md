---
layout: default
title: AMAP Agentic Planning Technical Report
---

# AMAP Agentic Planning Technical Report

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24957" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24957v1</a>
  <a href="https://arxiv.org/pdf/2512.24957.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24957v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24957v1', 'AMAP Agentic Planning Technical Report')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yulan Hu, Xiangwen Zhang, Sheng Ouyang, Hao Yi, Lu Xu, Qinglin Lang, Lide Tan, Xiang Cheng, Tianchen Ye, Zhicong Li, Ge Chen, Wenjin Yang, Zheng Pan, Shaopan Xiong, Siran Yang, Ju Huang, Yan Zhang, Jiamang Wang, Yong Liu, Yinfeng Huang, Tucheng Lin, Xin Li, Ning Guo

**分类**: cs.AI

**发布日期**: 2025-12-31

---

## 💡 一句话要点

**提出STAgent，一个用于时空理解的Agentic大语言模型，解决复杂任务如POI发现和行程规划。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Agentic模型` `时空理解` `大语言模型` `行程规划` `兴趣点发现`

## 📋 核心要点

1. 现有方法在解决复杂时空任务（如POI发现和行程规划）时，缺乏有效的工具交互和推理能力。
2. STAgent通过构建可交互的工具环境、分层数据管理和级联训练方案，提升模型在时空理解和推理方面的能力。
3. 实验表明，STAgent在TravelBench上表现出色，同时保持了通用能力，验证了所提出agentic模型的有效性。

## 📝 摘要（中文）

本文介绍STAgent，一个专为时空理解设计的agentic大语言模型，旨在解决受约束的兴趣点发现和行程规划等复杂任务。STAgent是一个专门的模型，能够与时空场景中的十种不同的工具进行交互，使其能够在复杂推理过程中探索、验证和改进中间步骤。值得注意的是，STAgent有效地保留了其通用能力。我们通过三个关键贡献赋予STAgent这些能力：（1）一个稳定的工具环境，支持十多种特定领域的工具，实现异步推出和训练；（2）一个分层数据管理框架，像大海捞针一样识别高质量数据，以1:10,000的过滤比例管理高质量查询，强调多样性和难度；（3）一个级联训练方案，首先是一个作为守护者的种子SFT阶段，用于衡量查询难度，然后是第二个SFT阶段，对具有高确定性的查询进行微调，以及最终的RL阶段，利用低确定性的数据。STAgent使用Qwen3-30B-A3B初始化，以建立强大的SFT基础并利用对样本难度的洞察力，在TravelBench上产生了有希望的性能，同时保持了其在各种通用基准测试中的通用能力，从而证明了我们提出的agentic模型的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决复杂时空任务，例如在特定约束条件下发现兴趣点（POI）和规划行程。现有方法通常难以有效地利用外部工具进行探索、验证和改进中间步骤，导致推理能力不足，难以处理复杂场景。

**核心思路**：论文的核心思路是构建一个agentic大语言模型STAgent，使其能够与多个领域特定的工具进行交互，并通过分层数据管理和级联训练方案，提升模型在时空理解和推理方面的能力。通过工具交互，模型可以探索、验证和改进中间步骤，从而更有效地解决复杂任务。

**技术框架**：STAgent的技术框架主要包含三个部分：1) 稳定的工具环境，支持十多种领域特定工具的异步训练；2) 分层数据管理框架，用于筛选高质量训练数据，强调多样性和难度；3) 级联训练方案，包括种子SFT阶段（评估查询难度）、高置信度SFT阶段和低置信度RL阶段。整体流程是先通过种子SFT阶段评估数据难度，然后分别使用高置信度和低置信度数据进行SFT和RL训练，最终提升模型性能。

**关键创新**：论文的关键创新在于提出了一个完整的agentic框架，包括工具环境、数据管理和训练方案，使得大语言模型能够有效地应用于复杂时空任务。与现有方法相比，STAgent能够更好地利用外部工具进行探索和推理，并且通过分层数据管理和级联训练，能够更有效地利用不同难度的数据。

**关键设计**：在数据管理方面，论文采用1:10,000的过滤比例筛选高质量查询，并强调数据的多样性和难度。在训练方面，论文采用级联训练方案，首先使用种子SFT阶段评估查询难度，然后分别使用高置信度和低置信度数据进行SFT和RL训练。模型初始化使用Qwen3-30B-A3B，以建立强大的SFT基础。

## 📊 实验亮点

STAgent在TravelBench上取得了有希望的性能，同时保持了其在各种通用基准测试中的通用能力。这表明该模型在解决特定领域问题的同时，没有牺牲其通用性，验证了所提出agentic模型的有效性。具体性能数据和对比基线未在摘要中明确给出，属于未知信息。

## 🎯 应用场景

该研究成果可应用于智能出行、城市规划、物流优化、旅游推荐等领域。通过STAgent，用户可以更方便地进行个性化行程规划、POI推荐和路径导航，从而提升出行效率和用户体验。未来，该技术有望进一步扩展到更多时空相关的应用场景。

## 📄 摘要（原文）

> We present STAgent, an agentic large language model tailored for spatio-temporal understanding, designed to solve complex tasks such as constrained point-of-interest discovery and itinerary planning. STAgent is a specialized model capable of interacting with ten distinct tools within spatio-temporal scenarios, enabling it to explore, verify, and refine intermediate steps during complex reasoning. Notably, STAgent effectively preserves its general capabilities. We empower STAgent with these capabilities through three key contributions: (1) a stable tool environment that supports over ten domain-specific tools, enabling asynchronous rollout and training; (2) a hierarchical data curation framework that identifies high-quality data like a needle in a haystack, curating high-quality queries with a filter ratio of 1:10,000, emphasizing both diversity and difficulty; and (3) a cascaded training recipe that starts with a seed SFT stage acting as a guardian to measure query difficulty, followed by a second SFT stage fine-tuned on queries with high certainty, and an ultimate RL stage that leverages data of low certainty. Initialized with Qwen3-30B-A3B to establish a strong SFT foundation and leverage insights into sample difficulty, STAgent yields promising performance on TravelBench while maintaining its general capabilities across a wide range of general benchmarks, thereby demonstrating the effectiveness of our proposed agentic model.

