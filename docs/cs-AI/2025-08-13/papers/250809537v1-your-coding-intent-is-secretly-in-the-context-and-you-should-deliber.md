---
layout: default
title: Your Coding Intent is Secretly in the Context and You Should Deliberately Infer It Before Completion
---

# Your Coding Intent is Secretly in the Context and You Should Deliberately Infer It Before Completion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09537" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09537v1</a>
  <a href="https://arxiv.org/pdf/2508.09537.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09537v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09537v1', 'Your Coding Intent is Secretly in the Context and You Should Deliberately Infer It Before Completion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanzhou Li, Tianlin Li, Yiran Zhang, Shangqing Liu, Aishan Liu, Yang Liu

**分类**: cs.SE, cs.AI

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出三阶段推理框架以提升代码补全的准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码补全` `意图推断` `大型语言模型` `交互式精炼` `软件开发` `自动化测试` `机器学习`

## 📋 核心要点

1. 现有方法在缺乏明确注释时，代码补全的准确性显著下降，影响开发效率。
2. 本文提出三阶段推理框架，首先进行意图推断，然后通过交互式精炼机制，最后生成目标函数。
3. 在DevEval和ComplexCodeEval上的实验结果显示，本文方法在参考基准和执行基准上均实现了超过20%的相对提升。

## 📝 摘要（中文）

大型语言模型（LLMs）在代码库的函数补全中应用越来越广泛。以往研究表明，当提供明确的指令（如文档字符串）时，这些模型能够生成高精度的实现。然而，在实际代码库中，这些注释往往缺失，导致性能显著下降。为了解决这一问题，本文将任务框架化为三个阶段：首先，通过分析目标函数之前的代码进行意图推断；其次，提供可选的交互式精炼机制以处理不足的上下文；最后，基于最终确定的意图生成目标函数。实验结果表明，该方法在多个LLM上均实现了超过20%的相对提升。

## 🔬 方法详解

**问题定义**：本文旨在解决在缺乏明确注释的情况下，如何有效推断代码意图并进行准确的函数补全。现有方法在此情境下表现不佳，导致开发者效率降低。

**核心思路**：论文提出通过分析目标函数之前的代码来推断开发者的意图，并设计了一个推理驱动的提示框架，以逐步提取和综合这些信号，确保生成的代码符合实际需求。

**技术框架**：整体流程分为三个阶段：第一阶段为意图推断，分析上下文；第二阶段为交互式精炼，允许开发者选择或编辑意图；第三阶段为基于最终意图生成目标函数。

**关键创新**：最重要的创新在于引入了交互式精炼机制，使得模型能够在上下文不足时，通过开发者的反馈进一步调整推断的意图，从而提高代码生成的准确性。

**关键设计**：在数据集构建上，本文整理了40,000个示例，包含中间推理轨迹和对应的文档字符串，确保模型训练的多样性和有效性。

## 📊 实验亮点

实验结果表明，本文方法在DevEval和ComplexCodeEval上对多个大型语言模型均实现了超过20%的相对提升，尤其是在参考基准和执行基准上均表现出显著的性能改进，验证了方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发、自动化测试和代码审查等。通过提升代码补全的准确性，能够显著提高开发者的工作效率，减少错误率，进而推动软件开发的自动化进程。未来，该方法还可以扩展到其他编程语言和开发环境中，具有广泛的应用前景。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly used for function completion in repository-scale codebases. Prior studies demonstrate that when explicit instructions--such as docstrings--are provided, these models can generate highly accurate implementations. However, in real-world repositories, such annotations are frequently absent, and performance drops substantially without them. To address this gap, we frame the task as a three-stage process. The first stage focuses on intent inference, where the model analyzes the code preceding the target function to uncover cues about the desired functionality. Such preceding context often encodes subtle but critical information, and we design a reasoning-based prompting framework to guide the LLM through step-by-step extraction and synthesis of these signals before any code is generated. The second stage introduces an optional interactive refinement mechanism to handle cases where preceding context alone is insufficient for intent recovery. In this stage, the model proposes a small set of candidate intentions, enabling the developer to select or edit them so that the inferred intent closely matches the actual requirement. Finally, in the third stage, the LLM generates the target function conditioned on the finalized intent. To support this pipeline, we curate a dataset of 40,000 examples annotated with intermediate reasoning traces and corresponding docstrings. Extensive experiments on DevEval and ComplexCodeEval show that our approach consistently boosts multiple LLMs, achieving over 20\% relative gains in both reference-based and execution-based metrics, with the interactive refinement stage delivering additional improvements beyond these gains.

