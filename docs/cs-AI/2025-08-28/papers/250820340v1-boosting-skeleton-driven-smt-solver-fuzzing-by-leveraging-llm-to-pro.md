---
layout: default
title: Boosting Skeleton-Driven SMT Solver Fuzzing by Leveraging LLM to Produce Formula Generators
---

# Boosting Skeleton-Driven SMT Solver Fuzzing by Leveraging LLM to Produce Formula Generators

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20340" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20340v1</a>
  <a href="https://arxiv.org/pdf/2508.20340.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20340v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20340v1', 'Boosting Skeleton-Driven SMT Solver Fuzzing by Leveraging LLM to Produce Formula Generators')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maolin Sun, Yibiao Yang, Yuming Zhou

**分类**: cs.SE, cs.AI, cs.PL

**发布日期**: 2025-08-28

---

## 💡 一句话要点

**提出Chimera框架以解决SMT求解器模糊测试中的生成公式有效性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `SMT求解器` `模糊测试` `大型语言模型` `逻辑表达生成` `上下文无关文法` `漏洞发现` `自动验证`

## 📋 核心要点

1. 现有的模糊测试技术在快速发展的SMT求解器特性面前，生成的测试公式中近一半是语法无效的，导致测试效果不佳。
2. Chimera框架通过合成可重用的逻辑表达生成器，利用LLM自动提取上下文无关文法，并生成符合这些文法的布尔表达式，确保生成公式的有效性。
3. 在对Z3和cvc5两个领先的SMT求解器进行评估时，Chimera成功识别了43个确认的漏洞，其中40个已被开发者修复，显示出显著的测试效果提升。

## 📝 摘要（中文）

可满足性模组理论(SMT)求解器是现代系统和编程语言研究的基础，确保其正确性至关重要，而高质量的测试公式是发现漏洞的关键。尽管现有测试技术在早期求解器版本上表现良好，但在快速发展的特性面前却显得力不从心。基于大型语言模型(LLM)的最新方法虽然展现出探索高级求解器能力的潜力，但生成的公式中近一半是语法无效的，同时与LLM的迭代交互也带来了显著的计算开销。本研究提出了Chimera，一个新颖的LLM辅助模糊测试框架，通过从直接生成公式转向合成可重用的逻辑表达生成器，解决了这两个问题。Chimera在模糊测试过程中确保语法有效性并促进语义多样性，且仅需一次LLM交互投资，显著降低了运行成本。

## 🔬 方法详解

**问题定义**：本论文旨在解决SMT求解器模糊测试中生成公式的有效性问题。现有方法在快速发展的求解器特性面前，生成的测试公式中近一半是语法无效的，且与LLM的迭代交互带来了较大的计算开销。

**核心思路**：论文提出的Chimera框架通过合成可重用的逻辑表达生成器，转变了直接生成公式的方式。利用LLM自动提取上下文无关文法(CFG)，并生成符合这些文法的布尔表达式，从而确保生成公式的语法有效性。

**技术框架**：Chimera框架的整体架构包括两个主要模块：首先是从文档中提取SMT理论的上下文无关文法，其次是合成符合这些文法的布尔表达式生成器。在模糊测试阶段，Chimera将现有公式的结构骨架与生成的布尔表达式进行组合。

**关键创新**：Chimera的核心创新在于通过合成可重用的生成器来替代直接生成公式的方式，这一设计显著降低了生成公式的语法无效性，并减少了与LLM的交互次数，从而降低了运行成本。

**关键设计**：在Chimera中，关键的参数设置包括上下文无关文法的提取策略和布尔表达式生成器的合成方法。具体的网络结构和损失函数的设计细节在论文中进行了详细描述，以确保生成的表达式既符合语法又具备语义多样性。

## 📊 实验亮点

在对Z3和cvc5两个领先的SMT求解器的实验中，Chimera成功识别了43个确认的漏洞，其中40个已被开发者修复，显示出其在漏洞发现方面的显著效果提升。这一结果表明，Chimera在模糊测试中的有效性和实用性。

## 🎯 应用场景

Chimera框架在SMT求解器的模糊测试中具有广泛的应用潜力，能够有效提高求解器的测试效率和漏洞发现率。这一研究不仅对编程语言和系统的自动验证具有重要价值，还可能推动相关领域的进一步研究与发展，提升软件系统的安全性和可靠性。

## 📄 摘要（原文）

> Satisfiability Modulo Theory (SMT) solvers are foundational to modern systems and programming languages research, providing the foundation for tasks like symbolic execution and automated verification. Because these solvers sit on the critical path, their correctness is essential, and high-quality test formulas are key to uncovering bugs. However, while prior testing techniques performed well on earlier solver versions, they struggle to keep pace with rapidly evolving features. Recent approaches based on Large Language Models (LLMs) show promise in exploring advanced solver capabilities, but two obstacles remain: nearly half of the generated formulas are syntactically invalid, and iterative interactions with the LLMs introduce substantial computational overhead. In this study, we present Chimera, a novel LLM-assisted fuzzing framework that addresses both issues by shifting from direct formula generation to the synthesis of reusable term (i.e., logical expression) generators. Particularly, Chimera uses LLMs to (1) automatically extract context-free grammars (CFGs) for SMT theories, including solver-specific extensions, from documentation, and (2) synthesize composable Boolean term generators that adhere to these grammars. During fuzzing, Chimera populates structural skeletons derived from existing formulas with the terms iteratively produced by the LLM-synthesized generators. This design ensures syntactic validity while promoting semantic diversity. Notably, Chimera requires only one-time LLM interaction investment, dramatically reducing runtime cost. We evaluated Chimera on two leading SMT solvers: Z3 and cvc5. Our experiments show that Chimera has identified 43 confirmed bugs, 40 of which have already been fixed by developers.

