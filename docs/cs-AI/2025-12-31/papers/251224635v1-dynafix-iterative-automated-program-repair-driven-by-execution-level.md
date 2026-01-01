---
layout: default
title: "DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information"
---

# DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24635" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24635v1</a>
  <a href="https://arxiv.org/pdf/2512.24635.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24635v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24635v1', 'DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhili Huang, Ling Xu, Chao Liu, Weifeng Sun, Xu Zhang, Yan Lei, Meng Yan, Hongyu Zhang

**分类**: cs.SE, cs.AI

**发布日期**: 2025-12-31

**备注**: 22 pages, 7 figures, preprint version

---

## 💡 一句话要点

**DynaFix：一种执行级动态信息驱动的迭代式自动程序修复方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动程序修复` `动态分析` `大型语言模型` `迭代修复` `执行级信息`

## 📋 核心要点

1. 现有APR方法依赖静态分析或粗粒度动态反馈，无法充分利用程序运行时信息，限制了复杂错误的修复能力。
2. DynaFix通过迭代地收集和利用执行级动态信息（如变量状态、控制流），指导LLM生成和改进补丁。
3. 实验表明，DynaFix在Defects4J基准上修复了186个单函数错误，比现有方法提高了10%，并显著减少了搜索空间。

## 📝 摘要（中文）

自动程序修复(APR)旨在为有缺陷的程序自动生成正确的补丁。最近利用大型语言模型(LLM)的方法显示出潜力，但也面临局限性。大多数方法仅依赖于静态分析，忽略了运行时行为。一些方法尝试结合动态信号，但这些信号通常仅限于训练或微调，或者仅一次性注入到修复提示中，而没有迭代使用，无法充分捕获程序执行。当前的迭代修复框架通常依赖于粗粒度的反馈，例如通过/失败结果或异常类型，并且没有有效地利用细粒度的执行级信息。因此，模型难以模拟人类逐步调试，限制了其在多步骤推理和复杂错误修复中的有效性。为了解决这些挑战，我们提出DynaFix，一种执行级动态信息驱动的APR方法，它迭代地利用运行时信息来改进修复过程。在每个修复轮次中，DynaFix捕获执行级动态信息，例如变量状态、控制流路径和调用堆栈，将它们转换为结构化提示，以指导LLM生成候选补丁。如果补丁未能通过验证，DynaFix会重新执行修改后的程序，以收集新的执行信息以供下一次尝试。这种迭代循环基于更新的反馈逐步改进补丁，类似于人类开发人员的逐步调试实践。我们在Defects4J v1.2和v2.0基准上评估DynaFix。DynaFix修复了186个单函数错误，比最先进的基线提高了10%，其中包括38个以前未修复的错误。它在最多35次尝试内实现了正确的补丁，与现有方法相比，减少了70%的补丁搜索空间，从而证明了修复复杂错误的有效性和效率。

## 🔬 方法详解

**问题定义**：自动程序修复旨在自动生成程序缺陷的正确补丁。现有方法，特别是基于大型语言模型的方法，主要依赖静态分析，忽略了程序运行时的动态行为。即使一些方法尝试利用动态信息，也往往是粗粒度的（例如，测试用例通过/失败）或者仅在初始阶段使用，无法充分指导迭代修复过程。这导致模型难以进行多步骤推理和修复复杂错误。

**核心思路**：DynaFix的核心思路是模拟人类开发者的调试过程，通过迭代地收集和利用程序运行时的细粒度动态信息来指导LLM生成和改进补丁。每次修复尝试后，DynaFix都会重新执行修改后的程序，收集新的执行信息，并将其作为反馈用于下一次修复尝试。这种迭代过程允许模型逐步逼近正确的补丁。

**技术框架**：DynaFix的整体框架包含以下几个主要阶段：1) **程序执行**：执行待修复的程序，并收集执行级动态信息，例如变量状态、控制流路径和调用堆栈。2) **信息转换**：将收集到的动态信息转换为结构化的提示，以便LLM理解和利用。3) **补丁生成**：使用LLM根据提示生成候选补丁。4) **补丁验证**：使用测试用例验证生成的补丁。如果补丁通过验证，则修复成功；否则，返回第一步，重新执行程序并收集新的动态信息。

**关键创新**：DynaFix的关键创新在于其迭代地利用执行级动态信息来指导LLM进行程序修复。与现有方法相比，DynaFix能够更充分地利用程序运行时信息，从而更有效地修复复杂错误。此外，DynaFix的迭代修复过程允许模型逐步逼近正确的补丁，减少了搜索空间。

**关键设计**：DynaFix的关键设计包括：1) 如何有效地收集和表示执行级动态信息；2) 如何将动态信息转换为LLM能够理解的结构化提示；3) 如何设计迭代修复过程，以便模型能够逐步逼近正确的补丁。论文中具体使用的LLM模型和提示工程方法未明确说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24635v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24635v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24635v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

DynaFix在Defects4J v1.2和v2.0基准上进行了评估，修复了186个单函数错误，比最先进的基线提高了10%，其中包括38个以前未修复的错误。此外，DynaFix在最多35次尝试内实现了正确的补丁，与现有方法相比，减少了70%的补丁搜索空间，表明其在修复复杂错误方面的效率。

## 🎯 应用场景

DynaFix具有广泛的应用前景，可以应用于软件开发的各个阶段，例如单元测试、集成测试和系统测试。它可以帮助开发人员自动修复程序中的错误，提高软件质量和开发效率。此外，DynaFix还可以用于教育领域，帮助学生学习程序调试和修复技术。未来，DynaFix可以扩展到支持更复杂的程序和错误类型，并与其他自动化软件工程工具集成。

## 📄 摘要（原文）

> Automated Program Repair (APR) aims to automatically generate correct patches for buggy programs. Recent approaches leveraging large language models (LLMs) have shown promise but face limitations. Most rely solely on static analysis, ignoring runtime behaviors. Some attempt to incorporate dynamic signals, but these are often restricted to training or fine-tuning, or injected only once into the repair prompt, without iterative use. This fails to fully capture program execution. Current iterative repair frameworks typically rely on coarse-grained feedback, such as pass/fail results or exception types, and do not leverage fine-grained execution-level information effectively. As a result, models struggle to simulate human stepwise debugging, limiting their effectiveness in multi-step reasoning and complex bug repair.
>   To address these challenges, we propose DynaFix, an execution-level dynamic information-driven APR method that iteratively leverages runtime information to refine the repair process. In each repair round, DynaFix captures execution-level dynamic information such as variable states, control-flow paths, and call stacks, transforming them into structured prompts to guide LLMs in generating candidate patches. If a patch fails validation, DynaFix re-executes the modified program to collect new execution information for the next attempt. This iterative loop incrementally improves patches based on updated feedback, similar to the stepwise debugging practices of human developers. We evaluate DynaFix on the Defects4J v1.2 and v2.0 benchmarks. DynaFix repairs 186 single-function bugs, a 10% improvement over state-of-the-art baselines, including 38 bugs previously unrepaired. It achieves correct patches within at most 35 attempts, reducing the patch search space by 70% compared with existing methods, thereby demonstrating both effectiveness and efficiency in repairing complex bugs.

