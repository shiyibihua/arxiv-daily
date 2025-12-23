---
layout: default
title: Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement
---

# Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.18950" class="toolbar-btn" target="_blank">📄 arXiv: 2512.18950v1</a>
  <a href="https://arxiv.org/pdf/2512.18950.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.18950v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.18950v1', 'Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Saman Forouzandeh, Wei Peng, Parham Moradi, Xinghuo Yu, Mahdi Jalili

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-22

**备注**: Accepted at The 25th International Conference on Autonomous Agents and Multi-Agent Systems (AAMAS 2026). 21 pages including references, with 7 figures and 8 tables. Code is publicly available at the authors GitHub repository: https://github.com/S-Forouzandeh/MACLA-LLM-Agents-AAMAS-Conference

---

## 💡 一句话要点

**MACLA：通过贝叶斯选择和对比精炼学习LLM Agent的分层程序记忆**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM Agent` `程序记忆` `贝叶斯选择` `对比学习` `分层记忆` `知识复用` `强化学习`

## 📋 核心要点

1. 现有LLM Agent在复杂任务中面临样本效率低和泛化能力弱的挑战，需要大量训练数据和参数调整。
2. MACLA通过维护冻结的LLM和外部分层程序记忆，解耦推理和学习过程，实现高效的知识复用和泛化。
3. 实验表明，MACLA在多个基准测试中显著优于现有方法，尤其在未见任务上表现出良好的泛化能力和效率。

## 📝 摘要（中文）

本文提出MACLA，一个将推理与学习解耦的框架，它维护一个冻结的大语言模型，并在外部分层程序记忆中执行所有适应。MACLA从轨迹中提取可重用的程序，通过贝叶斯后验跟踪可靠性，通过期望效用评分选择动作，并通过对比成功和失败来改进程序。在四个基准测试（ALFWorld、WebShop、TravelPlanner、InterCodeSQL）中，MACLA实现了78.1%的平均性能，优于所有基线。在ALFWorld的未见任务中，MACLA达到90.3%的性能，具有3.1%的正泛化能力。该系统在56秒内构建记忆，比最先进的LLM参数训练基线快2800倍，并将2851条轨迹压缩为187个程序。实验结果表明，具有贝叶斯选择和对比精炼的结构化外部记忆能够实现样本高效、可解释且持续改进的Agent，而无需LLM参数更新。

## 🔬 方法详解

**问题定义**：现有的大语言模型Agent在处理复杂任务时，通常需要大量的训练数据进行参数调整，导致样本效率低下。此外，模型难以泛化到未见过的任务，需要针对特定任务进行重新训练。现有的方法难以在效率、泛化性和可解释性之间取得平衡。

**核心思路**：MACLA的核心思路是将LLM的推理能力与外部程序记忆的学习能力解耦。LLM负责进行高层次的推理和决策，而外部程序记忆则负责存储和复用从经验中学习到的程序。通过这种方式，LLM可以专注于推理，而程序记忆可以不断地学习和改进，从而提高样本效率和泛化能力。

**技术框架**：MACLA的整体框架包括以下几个主要模块：1) 轨迹提取：从Agent的交互轨迹中提取可重用的程序。2) 可靠性跟踪：使用贝叶斯后验来跟踪每个程序的可靠性。3) 动作选择：通过期望效用评分来选择最佳的动作。4) 程序精炼：通过对比成功和失败的经验来改进程序。整个流程无需更新LLM参数。

**关键创新**：MACLA最重要的创新点在于其结构化的外部记忆和贝叶斯选择与对比精炼机制。结构化外部记忆允许Agent存储和复用程序，而贝叶斯选择机制则允许Agent根据程序的可靠性来选择最佳的动作。对比精炼机制则允许Agent通过对比成功和失败的经验来不断改进程序。与现有方法相比，MACLA无需对LLM进行参数更新，从而大大提高了效率。

**关键设计**：MACLA使用分层程序记忆，允许Agent存储不同粒度的程序。贝叶斯后验的计算基于程序的成功和失败次数。期望效用评分则基于程序的可靠性和预期收益。对比精炼机制通过比较成功和失败的轨迹来识别需要改进的程序。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18950v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18950v1/Figures/fig_memory_size.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18950v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

MACLA在四个基准测试中取得了显著的性能提升，平均性能达到78.1%，优于所有基线。在ALFWorld的未见任务中，MACLA达到了90.3%的性能，具有3.1%的正泛化能力。此外，MACLA构建记忆的速度比最先进的LLM参数训练基线快2800倍，并将2851条轨迹压缩为187个程序。这些结果表明，MACLA具有很高的效率和泛化能力。

## 🎯 应用场景

MACLA框架具有广泛的应用前景，可应用于机器人控制、游戏AI、智能助手等领域。通过学习和复用经验，Agent可以更有效地完成复杂任务，并适应新的环境。该研究有助于开发更智能、更高效、更具适应性的AI系统。

## 📄 摘要（原文）

> We present MACLA, a framework that decouples reasoning from learning by maintaining a frozen large language model while performing all adaptation in an external hierarchical procedural memory. MACLA extracts reusable procedures from trajectories, tracks reliability via Bayesian posteriors, selects actions through expected-utility scoring, and refines procedures by contrasting successes and failures. Across four benchmarks (ALFWorld, WebShop, TravelPlanner, InterCodeSQL), MACLA achieves 78.1 percent average performance, outperforming all baselines. On ALFWorld unseen tasks, MACLA reaches 90.3 percent with 3.1 percent positive generalization. The system constructs memory in 56 seconds, 2800 times faster than the state-of-the-art LLM parameter-training baseline, compressing 2851 trajectories into 187 procedures. Experimental results demonstrate that structured external memory with Bayesian selection and contrastive refinement enables sample-efficient, interpretable, and continually improving agents without LLM parameter updates.

