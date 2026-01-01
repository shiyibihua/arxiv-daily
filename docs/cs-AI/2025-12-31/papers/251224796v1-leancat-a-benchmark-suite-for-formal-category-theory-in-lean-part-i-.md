---
layout: default
title: "LeanCat: A Benchmark Suite for Formal Category Theory in Lean (Part I: 1-Categories)"
---

# LeanCat: A Benchmark Suite for Formal Category Theory in Lean (Part I: 1-Categories)

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24796" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24796v1</a>
  <a href="https://arxiv.org/pdf/2512.24796.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24796v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24796v1', 'LeanCat: A Benchmark Suite for Formal Category Theory in Lean (Part I: 1-Categories)')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rongge Xu, Hui Dai, Yiming Fu, Jiedong Jiang, Tianjiao Nie, Hongwei Wang, Junkai Wang, Holiverse Yang, Jiatong Yang, Zhi-Hao Zhang

**分类**: cs.LO, cs.AI, cs.FL, cs.LG, math.CT

**发布日期**: 2025-12-31

**备注**: 11 pages, 4 figures, 1 table

---

## 💡 一句话要点

**提出LeanCat基准测试集，用于评估LLM在范畴论形式化证明中的能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `形式化验证` `范畴论` `基准测试` `大型语言模型` `定理证明` `Lean` `数学推理`

## 📋 核心要点

1. 现有形式化定理证明基准缺乏对抽象和库介导推理的充分评估，无法真实反映现代数学的复杂性。
2. LeanCat通过构建范畴论形式化的基准测试集，着重考察模型在结构化和接口级推理方面的能力。
3. 实验结果表明，现有最佳模型在LeanCat上的表现仍有很大提升空间，突显了该基准的挑战性。

## 📝 摘要（中文）

大型语言模型（LLM）在形式化定理证明方面取得了快速进展，但目前的基准测试低估了组织现代数学的抽象和库介导推理。与FATE强调前沿代数并行，我们引入LeanCat，一个用于范畴论形式化的Lean基准——一种数学结构的统一语言和现代证明工程的核心层——作为结构化、接口级推理的压力测试。第一部分：1-范畴包含100个完全形式化的语句级任务，通过LLM辅助+人工分级过程整理成主题族和三个难度等级。最佳模型在pass@1时解决了8.25%的任务（简单/中等/高难度分别为32.50%/4.17%/0.00%），在pass@4时解决了12.00%的任务（简单/中等/高难度分别为50.00%/4.76%/0.00%）。我们还评估了使用LeanExplore搜索Mathlib的LeanBridge，并观察到相对于单模型基线的持续提升。LeanCat旨在作为一个紧凑、可重用的检查点，用于跟踪人工智能和人类在Lean中实现可靠的、研究级别的形式化的进展。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在形式化定理证明中，对抽象概念和库函数的使用能力不足的问题。现有的基准测试无法充分评估模型在现代数学中常见的结构化推理和接口级推理能力，尤其是在范畴论这样的高度抽象领域。

**核心思路**：论文的核心思路是构建一个专门针对范畴论形式化的基准测试集LeanCat。通过提供一系列精心设计的、难度分级的范畴论问题，来评估LLM在形式化证明方面的能力，特别是其对数学结构和接口的理解和运用。

**技术框架**：LeanCat基准测试集包含100个完全形式化的语句级任务，这些任务被组织成不同的主题族，并根据难度分为简单、中等和高三个等级。难度分级由LLM辅助和人工评估相结合的方式完成。论文还评估了LeanBridge，它使用LeanExplore来搜索Mathlib库，以辅助证明过程。

**关键创新**：LeanCat的关键创新在于其专注于范畴论这一高度抽象的数学领域，并提供了一个结构化的、难度分级的基准测试集。这使得研究人员能够更精确地评估LLM在形式化证明中对抽象概念和库函数的使用能力。此外，LLM辅助的人工分级方法也保证了基准测试的质量和难度分布。

**关键设计**：LeanCat基准测试集中的任务涵盖了1-范畴论的各种基本概念和定理。难度分级标准主要考虑了证明的长度、涉及的抽象概念的数量以及对Mathlib库的依赖程度。LeanBridge使用LeanExplore来搜索Mathlib库，并利用搜索结果来指导证明过程。具体的参数设置和损失函数等技术细节未在摘要中提及，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24796v1/formal-accuracy_pass4.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24796v1/accuracy_comparison_300dpi.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24796v1/x1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

最佳模型在LeanCat基准测试集上的pass@1准确率为8.25%，pass@4准确率为12.00%。其中，简单难度任务的解决率较高（pass@1: 32.50%, pass@4: 50.00%），而中等和高难度任务的解决率较低（中等难度pass@1: 4.17%, pass@4: 4.76%; 高难度pass@1: 0.00%, pass@4: 0.00%）。使用LeanBridge可以获得相对于单模型基线的持续提升。

## 🎯 应用场景

LeanCat可用于评估和提升人工智能在形式化数学和软件验证等领域的应用能力。通过提供一个标准化的测试平台，它可以促进LLM在定理证明、程序验证和知识表示等方面的研究进展，并最终推动人工智能在科学发现和工程设计中的应用。

## 📄 摘要（原文）

> Large language models (LLMs) have made rapid progress in formal theorem proving, yet current benchmarks under-measure the kind of abstraction and library-mediated reasoning that organizes modern mathematics. In parallel with FATE's emphasis on frontier algebra, we introduce LeanCat, a Lean benchmark for category-theoretic formalization -- a unifying language for mathematical structure and a core layer of modern proof engineering -- serving as a stress test of structural, interface-level reasoning. Part I: 1-Categories contains 100 fully formalized statement-level tasks, curated into topic families and three difficulty tiers via an LLM-assisted + human grading process. The best model solves 8.25% of tasks at pass@1 (32.50%/4.17%/0.00% by Easy/Medium/High) and 12.00% at pass@4 (50.00%/4.76%/0.00%). We also evaluate LeanBridge which use LeanExplore to search Mathlib, and observe consistent gains over single-model baselines. LeanCat is intended as a compact, reusable checkpoint for tracking both AI and human progress toward reliable, research-level formalization in Lean.

