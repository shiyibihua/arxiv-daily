---
layout: default
title: Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall
---

# Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15214" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15214v2</a>
  <a href="https://arxiv.org/pdf/2508.15214.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15214v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15214v2', 'Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sijia Cui, Aiyao He, Shuai Xu, Hongming Zhang, Yanna Wang, Qingyang Zhang, Yajing Wang, Bo Xu

**分类**: cs.CL

**发布日期**: 2025-08-21 (更新: 2025-09-17)

**备注**: Accepted to EMNLP 2025

---

## 💡 一句话要点

**提出自指导函数调用方法以解决多步骤工具使用问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `函数调用` `经验回忆` `工具选择` `多步骤任务`

## 📋 核心要点

1. 现有方法在多步骤工具使用中面临工具选择、参数生成和工具链规划的挑战，导致效率低下。
2. 本文提出的逐步经验回忆（SEER）方法，通过从动态更新的经验池中进行细粒度检索，解决了上述问题。
3. 在ToolQA基准测试中，SEER在简单和困难问题上分别提升了6.1%和4.7%的准确率，展现了显著的性能改进。

## 📝 摘要（中文）

函数调用使大型语言模型（LLMs）能够通过工具和API与外部系统交互。然而，在多步骤工具使用中，LLMs在工具选择、参数生成和工具链规划方面仍然面临挑战。现有方法通常依赖于手动设计的特定任务演示或从策划库中检索，这些方法需要大量专家努力，并且随着工具多样性和任务难度的增加，提示工程变得越来越复杂和低效。为了解决这些挑战，本文提出了一种自指导方法——逐步经验回忆（SEER），该方法从不断更新的经验池中进行细粒度的逐步检索。SEER通过增量地扩展经验池，利用过去成功的轨迹，能够持续提高模型性能。在ToolQA基准测试中，SEER在简单和困难问题上分别实现了6.1%和4.7%的平均提升。进一步在包含两个真实世界领域的$τ$-bench上测试，SEER在Qwen2.5-7B和Qwen2.5-72B模型上分别展示了7.44%和23.38%的显著准确性提升。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在多步骤工具使用中面临的工具选择、参数生成和工具链规划等具体问题。现有方法依赖于手动设计的任务特定演示或静态库，导致效率低下和灵活性不足。

**核心思路**：论文提出的逐步经验回忆（SEER）方法，通过动态更新的经验池进行细粒度检索，利用过去成功的轨迹来增强模型的决策能力，从而提高工具使用的效率和准确性。

**技术框架**：SEER的整体架构包括经验池的构建、动态更新和逐步检索三个主要模块。经验池不断吸收成功的历史轨迹，模型在需要时从中检索相关信息，以指导当前任务的执行。

**关键创新**：SEER的核心创新在于其自指导的检索机制，区别于传统的静态库方法，能够根据实时反馈不断扩展和优化经验池，从而实现持续的性能提升。

**关键设计**：在技术细节上，SEER采用了增量更新策略，确保经验池的实时性和相关性，同时设计了高效的检索算法，以快速响应模型的需求。

## 📊 实验亮点

在ToolQA基准测试中，SEER方法在简单问题上实现了6.1%的准确率提升，在困难问题上提升了4.7%。在$τ$-bench测试中，使用Qwen2.5-7B和Qwen2.5-72B模型分别获得了7.44%和23.38%的显著准确性提升，展示了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化客服和复杂任务管理等场景。通过提高大型语言模型在多步骤任务中的表现，SEER能够显著提升用户体验和系统效率，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Function calling enables large language models (LLMs) to interact with external systems by leveraging tools and APIs. When faced with multi-step tool usage, LLMs still struggle with tool selection, parameter generation, and tool-chain planning. Existing methods typically rely on manually designing task-specific demonstrations, or retrieving from a curated library. These approaches demand substantial expert effort and prompt engineering becomes increasingly complex and inefficient as tool diversity and task difficulty scale. To address these challenges, we propose a self-guided method, Stepwise Experience Recall (SEER), which performs fine-grained, stepwise retrieval from a continually updated experience pool. Instead of relying on static or manually curated library, SEER incrementally augments the experience pool with past successful trajectories, enabling continuous expansion of the pool and improved model performance over time. Evaluated on the ToolQA benchmark, SEER achieves an average improvement of 6.1% on easy and 4.7% on hard questions. We further test SEER on $τ$-bench, which includes two real-world domains. Powered by Qwen2.5-7B and Qwen2.5-72B models, SEER demonstrates substantial accuracy gains of 7.44% and 23.38%, respectively.

