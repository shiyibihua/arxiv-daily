---
layout: default
title: LLM-Based Instance-Driven Heuristic Bias In the Context of a Biased Random Key Genetic Algorithm
---

# LLM-Based Instance-Driven Heuristic Bias In the Context of a Biased Random Key Genetic Algorithm

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09707" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09707v1</a>
  <a href="https://arxiv.org/pdf/2509.09707.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09707v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09707v1', 'LLM-Based Instance-Driven Heuristic Bias In the Context of a Biased Random Key Genetic Algorithm')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Camilo Chacón Sartori, Martín Isla Pino, Pedro Pinacho-Davidson, Christian Blum

**分类**: cs.NE, cs.AI, cs.CL

**发布日期**: 2025-09-05

**备注**: Submitted to a journal for review

---

## 💡 一句话要点

**提出基于LLM的实例驱动启发式偏置BRKGA算法，解决NP难的最长运行子序列问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `元启发式算法` `遗传算法` `组合优化` `启发式偏置` `实例驱动` `最长运行子序列`

## 📋 核心要点

1. 现有方法忽略了问题实例的结构属性，无法充分利用LLM在元启发式算法中的潜力。
2. 提出一种人与LLM协作的方法，共同设计实例相关的度量，并利用LLM生成启发式偏置，引导BRKGA搜索。
3. 实验表明，该方法在复杂实例上显著优于标准BRKGA基线，验证了LLM驱动的启发式偏置的有效性。

## 📝 摘要（中文）

本文提出了一种新颖的框架，将大型语言模型（LLM）集成到元启发式算法中，以解决复杂的组合优化问题。该方法利用LLM与带偏好的随机密钥遗传算法（BRKGA）相结合，解决NP难的最长运行子序列问题。通过人与LLM的协作，共同设计并实现了一组计算高效的度量。LLM分析这些特定于实例的度量，生成定制的启发式偏置，引导BRKGA搜索有希望的区域。实验评估表明，与标准BRKGA基线相比，最佳混合方法BRKGA+Llama-4-Maverick在最复杂的实例上实现了显著的统计改进。研究结果证实，利用LLM生成先验的、实例驱动的启发式偏置是增强复杂优化领域元启发式算法的有效方法。

## 🔬 方法详解

**问题定义**：论文旨在解决NP难的最长运行子序列（Longest Run Subsequence）问题。现有方法，特别是基于元启发式算法的方法，通常缺乏对问题实例特性的自适应性，难以有效利用LLM的知识来指导搜索过程。

**核心思路**：论文的核心思路是利用LLM的强大分析能力，根据特定问题实例的特征，生成定制化的启发式偏置。这种偏置能够引导BRKGA算法更有针对性地搜索解空间，从而提高求解效率和质量。通过人与LLM的协作，共同设计能够反映实例特征的度量，使得LLM能够更好地理解问题实例。

**技术框架**：整体框架包含以下几个主要阶段：1) 人工与LLM协作，设计并实现一组计算高效的、描述问题实例特征的度量；2) LLM分析这些度量，生成针对该实例的启发式偏置；3) 将该启发式偏置融入BRKGA算法中，指导其搜索过程。BRKGA算法使用随机密钥编码解，并通过遗传操作进行迭代优化。

**关键创新**：最重要的技术创新点在于将LLM用于生成实例驱动的启发式偏置。与传统的启发式算法或基于LLM的代码生成方法不同，该方法不是直接生成代码或规则，而是利用LLM的推理能力，根据实例特征生成一个偏置，从而更灵活地指导元启发式算法的搜索。

**关键设计**：关键设计包括：1) 如何设计能够有效反映问题实例特征的度量；2) 如何利用LLM将这些度量转化为有效的启发式偏置；3) 如何将启发式偏置融入BRKGA算法中，例如，可以通过调整选择概率或交叉概率来实现。论文中使用了Llama-4-Maverick作为LLM，并针对最长运行子序列问题设计了特定的度量。

## 📊 实验亮点

实验结果表明，BRKGA+Llama-4-Maverick方法在解决最长运行子序列问题上，显著优于标准BRKGA基线。特别是在最复杂的实例上，该方法取得了统计意义上的显著改进，验证了LLM驱动的实例驱动启发式偏置的有效性。实验涵盖了1050个不同复杂度的生成实例，保证了结果的可靠性。

## 🎯 应用场景

该研究成果可应用于各种组合优化问题，尤其是在问题实例具有显著差异性的场景下。例如，在生产调度、资源分配、路径规划等领域，可以利用LLM分析具体实例的特征，生成定制化的启发式偏置，从而提高优化算法的效率和效果。未来，该方法有望扩展到更复杂的优化问题和更强大的LLM模型。

## 📄 摘要（原文）

> Integrating Large Language Models (LLMs) within metaheuristics opens a novel path for solving complex combinatorial optimization problems. While most existing approaches leverage LLMs for code generation to create or refine specific heuristics, they often overlook the structural properties of individual problem instances. In this work, we introduce a novel framework that integrates LLMs with a Biased Random-Key Genetic Algorithm (BRKGA) to solve the NP-hard Longest Run Subsequence problem. Our approach extends the instance-driven heuristic bias paradigm by introducing a human-LLM collaborative process to co-design and implement a set of computationally efficient metrics. The LLM analyzes these instance-specific metrics to generate a tailored heuristic bias, which steers the BRKGA toward promising areas of the search space. We conduct a comprehensive experimental evaluation, including rigorous statistical tests, convergence and behavioral analyses, and targeted ablation studies, comparing our method against a standard BRKGA baseline across 1,050 generated instances of varying complexity. Results show that our top-performing hybrid, BRKGA+Llama-4-Maverick, achieves statistically significant improvements over the baseline, particularly on the most complex instances. Our findings confirm that leveraging an LLM to produce an a priori, instance-driven heuristic bias is a valuable approach for enhancing metaheuristics in complex optimization domains.

