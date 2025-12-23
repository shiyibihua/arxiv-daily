---
layout: default
title: Does It Run and Is That Enough? Revisiting Text-to-Chart Generation with a Multi-Agent Approach
---

# Does It Run and Is That Enough? Revisiting Text-to-Chart Generation with a Multi-Agent Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06175" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06175v1</a>
  <a href="https://arxiv.org/pdf/2506.06175.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06175v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06175v1', 'Does It Run and Is That Enough? Revisiting Text-to-Chart Generation with a Multi-Agent Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: James Ford, Anthony Rios

**分类**: cs.CL

**发布日期**: 2025-06-06

**备注**: 8 pages

---

## 💡 一句话要点

**提出多代理方法以降低文本到图表生成中的执行错误率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到图表生成` `多代理方法` `执行错误率` `数据可视化` `大型语言模型`

## 📋 核心要点

1. 现有方法在将自然语言描述转换为图表代码时，仍存在约15%的执行失败率，影响了实际应用效果。
2. 本文提出了一种多代理管道，分离了草拟、执行、修复和判断过程，以提高生成代码的执行成功率。
3. 在Text2Chart31和ChartX基准上，系统的执行错误率分别降至4.5%和4.6%，显著优于现有微调方法，且计算资源需求更低。

## 📝 摘要（中文）

大型语言模型能够将自然语言图表描述转换为可运行的代码，但生成的脚本仍有约15%的执行失败率。本文探讨这一错误率是否源于模型局限性或单一提示设计的依赖。为此，提出了一种轻量级的多代理管道，分离了草拟、执行、修复和判断过程，使用现成的GPT-4o-mini模型。在Text2Chart31基准上，系统将执行错误率降低至4.5%，超越最强的微调基线近5个百分点，同时计算需求显著降低。在ChartX基准上也观察到类似表现，错误率为4.6%，显示出良好的泛化能力。尽管执行成功率已大幅提升，但手动审查发现100个样本中有6个图表存在虚构内容，且无障碍审计显示生成图表在色盲指南的合规性上表现不佳。这表明未来工作应关注图表美学、语义准确性和无障碍性改进。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在文本到图表生成中的执行错误率高的问题。现有方法依赖单一提示设计，导致生成代码的执行失败率较高。

**核心思路**：提出的多代理管道通过将生成过程分为草拟、执行、修复和判断四个阶段，旨在提高生成代码的执行成功率和可靠性。

**技术框架**：整体架构包括四个主要模块：草拟模块负责生成初始代码，执行模块运行代码，修复模块处理执行错误，判断模块评估生成结果的质量。

**关键创新**：最重要的创新在于采用多代理设计，允许不同模块专注于特定任务，从而提高了整体系统的效率和准确性。这与传统的单一模型生成方法形成鲜明对比。

**关键设计**：在参数设置上，使用了现成的GPT-4o-mini模型，优化了每个模块的输入输出格式，并在修复阶段引入了迭代机制以降低错误率。

## 📊 实验亮点

实验结果显示，提出的多代理方法在Text2Chart31基准上将执行错误率降低至4.5%，在ChartX基准上为4.6%，相比最强微调基线提升近5个百分点，且计算资源需求显著减少，展示了良好的泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括数据可视化、商业智能和教育等领域，能够帮助用户更准确地生成图表，提高数据分析的效率和准确性。未来，随着对图表美学和无障碍性的关注，该方法有望在更广泛的应用场景中发挥重要作用。

## 📄 摘要（原文）

> Large language models can translate natural-language chart descriptions into runnable code, yet approximately 15\% of the generated scripts still fail to execute, even after supervised fine-tuning and reinforcement learning. We investigate whether this persistent error rate stems from model limitations or from reliance on a single-prompt design. To explore this, we propose a lightweight multi-agent pipeline that separates drafting, execution, repair, and judgment, using only an off-the-shelf GPT-4o-mini model. On the \textsc{Text2Chart31} benchmark, our system reduces execution errors to 4.5\% within three repair iterations, outperforming the strongest fine-tuned baseline by nearly 5 percentage points while requiring significantly less compute. Similar performance is observed on the \textsc{ChartX} benchmark, with an error rate of 4.6\%, demonstrating strong generalization. Under current benchmarks, execution success appears largely solved. However, manual review reveals that 6 out of 100 sampled charts contain hallucinations, and an LLM-based accessibility audit shows that only 33.3\% (\textsc{Text2Chart31}) and 7.2\% (\textsc{ChartX}) of generated charts satisfy basic colorblindness guidelines. These findings suggest that future work should shift focus from execution reliability toward improving chart aesthetics, semantic fidelity, and accessibility.

