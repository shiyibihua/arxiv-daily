---
layout: default
title: Execution Guided Line-by-Line Code Generation
---

# Execution Guided Line-by-Line Code Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10948" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10948v2</a>
  <a href="https://arxiv.org/pdf/2506.10948.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10948v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10948v2', 'Execution Guided Line-by-Line Code Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Boaz Lavon, Shahar Katz, Lior Wolf

**分类**: cs.LG

**发布日期**: 2025-06-12 (更新: 2025-10-23)

**备注**: Accepted to NeurIPS 2026

**🔗 代码/项目**: [GITHUB](https://github.com/boazlavon/eg_cfg)

---

## 💡 一句话要点

**提出执行引导的逐行代码生成方法以提升代码生成性能**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码生成` `执行反馈` `神经网络` `机器学习` `编程辅助` `自动化工具`

## 📋 核心要点

1. 现有的大型语言模型在代码生成时未能有效利用执行反馈，导致生成的代码可执行性不足。
2. 论文提出的EG-CFG方法通过动态引入执行信号，逐行引导代码生成，提升了生成的代码质量。
3. 实验结果显示，EG-CFG在基础问题到复杂的编程和数据科学任务中均显著提高了代码生成性能。

## 📝 摘要（中文）

我们提出了一种新颖的神经代码生成方法，该方法在语言模型生成过程中融入实时执行信号。尽管大型语言模型（LLMs）在代码生成方面表现出色，但通常在推理过程中未利用执行反馈，这一信号是人类程序员常用的。我们的执行引导无分类器引导（EG-CFG）方法在生成代码时动态地将执行信号纳入其中，提供逐行反馈，引导生成过程朝向可执行的解决方案。EG-CFG采用多阶段流程：首先，通过束搜索为每一行采样候选程序完成；其次，通过对这些候选程序进行测试用例执行来提取执行信号；最后，在生成过程中将这些信号纳入提示中。我们的实验表明，EG-CFG在多种编码任务中显著提升了代码生成性能，达到了各类复杂度下的最新成果。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有代码生成方法未能有效利用执行反馈的问题。传统的大型语言模型在推理时缺乏对执行结果的实时反馈，导致生成的代码往往不可执行，影响了代码生成的实用性和效率。

**核心思路**：EG-CFG方法的核心在于将执行信号动态融入代码生成过程，通过逐行反馈引导生成，使得生成的代码更具可执行性。这种设计模仿了人类程序员在编写代码时的思维过程，利用实时反馈进行调整。

**技术框架**：EG-CFG的整体架构包括三个主要阶段：首先，使用束搜索为每一行生成候选程序；其次，执行这些候选程序并提取执行信号；最后，将提取的信号融入生成提示中，以指导后续的代码生成。

**关键创新**：EG-CFG的主要创新在于动态引入执行信号，并在生成过程中保持信号的一致性。这一方法与传统的静态生成方法本质上不同，能够更好地反映代码的可执行性。

**关键设计**：在技术细节上，EG-CFG保持了同一行内的信号一致性，并在行边界处刷新信号，以确保生成过程的连贯性。此外，该方法支持任务级的原生并行性，允许多个代理并行操作，探索多样的推理路径。

## 📊 实验亮点

实验结果表明，EG-CFG在多种编码任务中显著提高了代码生成性能，相较于标准方法，达到了最新的性能水平，尤其在复杂度较高的编程和数据科学任务中表现尤为突出。

## 🎯 应用场景

该研究的潜在应用领域包括自动化代码生成、编程辅助工具和教育领域。通过提升代码生成的可执行性，EG-CFG可以帮助开发者更高效地编写和调试代码，降低编程的门槛，促进编程教育的发展。未来，该方法可能在软件开发和数据科学等领域产生深远影响。

## 📄 摘要（原文）

> We present a novel approach to neural code generation that incorporates real-time execution signals into the language model generation process. While large language models (LLMs) have demonstrated impressive code generation capabilities, they typically do not utilize execution feedback during inference, a critical signal that human programmers regularly leverage. Our method, Execution-Guided Classifier-Free Guidance (EG-CFG), dynamically incorporates execution signals as the model generates code, providing line-by-line feedback that guides the generation process toward executable solutions. EG-CFG employs a multi-stage process: first, we conduct beam search to sample candidate program completions for each line; second, we extract execution signals by executing these candidates against test cases; and finally, we incorporate these signals into the prompt during generation. By maintaining consistent signals across tokens within the same line and refreshing signals at line boundaries, our approach provides coherent guidance while preserving syntactic structure. Moreover, the method naturally supports native parallelism at the task level in which multiple agents operate in parallel, exploring diverse reasoning paths and collectively generating a broad set of candidate solutions. Our experiments across diverse coding tasks demonstrate that EG-CFG significantly improves code generation performance compared to standard approaches, achieving state-of-the-art results across various levels of complexity, from foundational problems to challenging competitive programming and data science tasks. Our code is available at: https://github.com/boazlavon/eg_cfg

