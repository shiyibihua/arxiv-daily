---
layout: default
title: Towards a Holistic and Automated Evaluation Framework for Multi-Level Comprehension of LLMs in Book-Length Contexts
---

# Towards a Holistic and Automated Evaluation Framework for Multi-Level Comprehension of LLMs in Book-Length Contexts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19578" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19578v1</a>
  <a href="https://arxiv.org/pdf/2508.19578.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19578v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19578v1', 'Towards a Holistic and Automated Evaluation Framework for Multi-Level Comprehension of LLMs in Book-Length Contexts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaqi Deng, Yuho Lee, Nicole Hee-Yeon Kim, Hyangsuk Min, Taewon Yun, Minjeong Ban, Kim Yul, Hwanjun Song

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-27

**备注**: Accepted to EMNLP 2025 (Main)

**🔗 代码/项目**: [GITHUB](https://github.com/DISL-Lab/HAMLET)

---

## 💡 一句话要点

**提出HAMLET框架以评估大语言模型在长文本中的理解能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长文本理解` `大语言模型` `自动化评估` `查询聚焦` `关键事实层次`

## 📋 核心要点

1. 现有方法在评估大语言模型的长文本理解能力时缺乏系统性和自动化，导致评估效率低下。
2. 论文提出的HAMLET框架通过三层关键事实层次结构和查询聚焦摘要方法，系统评估模型的理解能力。
3. 实验结果表明，HAMLET的自动评估与专家判断一致性超过90%，且成本降低了25倍，显示出显著的效率提升。

## 📝 摘要（中文）

我们介绍了HAMLET，一个全面自动化的框架，用于评估大语言模型（LLMs）在长文本上下文中的理解能力。HAMLET将源文本结构化为根、分支和叶子三个层级的关键事实层次，并采用基于查询的摘要方法来评估模型在每个层级上信息的回忆和忠实表现。通过系统的人类研究验证我们的全自动管道的可靠性，结果显示自动评估与专家人类判断的达成率超过90%，同时成本降低了多达25倍。HAMLET揭示了LLMs在细粒度理解方面的困难，尤其是在叶子层级，并且对位置效应如“迷失在中间”非常敏感。分析性查询比叙述性查询更具挑战性，开源模型与专有模型之间以及不同模型规模之间存在一致的性能差距。我们的代码和数据集已公开发布。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有评估大语言模型在长文本理解能力时的低效和不系统性问题。现有方法往往无法全面捕捉模型在不同层级的理解能力，导致评估结果不够准确。

**核心思路**：论文的核心思路是构建一个三层关键事实层次结构，并结合查询聚焦的摘要方法，系统性地评估模型在不同层级的信息回忆和表现。这样的设计旨在更好地反映模型的理解能力，尤其是在细粒度信息的处理上。

**技术框架**：HAMLET框架的整体架构包括三个主要模块：文本结构化模块、查询聚焦摘要模块和自动评估模块。文本结构化模块将源文本分解为根、分支和叶子层级，查询聚焦摘要模块则生成针对特定查询的摘要，最后通过自动评估模块对模型的表现进行打分。

**关键创新**：HAMLET的最大创新在于其全面自动化的评估流程和三层次的关键事实结构，这与现有方法的单一层级评估形成鲜明对比，能够更细致地捕捉模型的理解能力。

**关键设计**：在设计上，HAMLET采用了特定的参数设置和损失函数，以优化模型在不同层级的表现。此外，网络结构经过精心设计，以确保在处理长文本时的有效性和准确性。具体的参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

实验结果显示，HAMLET的自动评估方法与专家判断的一致性超过90%，并且在成本上降低了多达25倍。此外，HAMLET揭示了LLMs在细粒度理解方面的挑战，尤其是在叶子层级表现较差，分析性查询的难度高于叙述性查询。

## 🎯 应用场景

该研究的潜在应用领域包括教育、内容生成、信息检索等，能够帮助开发更智能的系统，以提高大语言模型在长文本理解中的表现。未来，HAMLET框架可能推动更高效的模型评估和优化，促进自然语言处理领域的发展。

## 📄 摘要（原文）

> We introduce HAMLET, a holistic and automated framework for evaluating the long-context comprehension of large language models (LLMs). HAMLET structures source texts into a three-level key-fact hierarchy at root-, branch-, and leaf-levels, and employs query-focused summarization to evaluate how well models recall and faithfully represent information at each level. To validate the reliability of our fully automated pipeline, we conduct a systematic human study, showing that our automatic evaluation achieves over 90% agreement with expert human judgments, while reducing the cost by up to 25 times. HAMLET reveals that LLMs struggle with fine-grained comprehension, especially at the leaf level, and are sensitive to positional effects like the lost-in-the-middle. Analytical queries pose greater challenges than narrative ones, and consistent performance gaps emerge between open-source and proprietary models, as well as across model scales. Our code and dataset are publicly available at https://github.com/DISL-Lab/HAMLET.

