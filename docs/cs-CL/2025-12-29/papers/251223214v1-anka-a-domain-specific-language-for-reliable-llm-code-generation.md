---
layout: default
title: "Anka: A Domain-Specific Language for Reliable LLM Code Generation"
---

# Anka: A Domain-Specific Language for Reliable LLM Code Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23214" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23214v1</a>
  <a href="https://arxiv.org/pdf/2512.23214.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23214v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23214v1', 'Anka: A Domain-Specific Language for Reliable LLM Code Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Saif Khalfan Saif Al Mazrouei

**分类**: cs.CL, cs.LG, cs.PL, cs.SE

**发布日期**: 2025-12-29

**备注**: 11 pages, 1 figure, 4 tables. Code and benchmarks available at https://github.com/BleBlo/Anka

---

## 💡 一句话要点

**提出领域特定语言Anka，提升LLM在复杂数据转换任务中的代码生成可靠性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `领域特定语言` `代码生成` `大型语言模型` `数据转换` `可靠性` `语法约束` `基准测试`

## 📋 核心要点

1. 通用编程语言的灵活性导致LLM在复杂多步骤编程任务中产生系统性错误，如操作排序和变量管理错误。
2. 提出领域特定语言Anka，通过显式和受约束的语法来减少代码生成中的歧义，从而提高LLM代码生成的可靠性。
3. 实验表明，Anka在多步骤数据转换任务上显著优于Python，并且LLM可以从上下文提示中快速学习并应用Anka。

## 📝 摘要（中文）

大型语言模型（LLMs）在代码生成方面表现出卓越的能力，但在复杂的多步骤编程任务中存在系统性错误。我们假设这些错误源于通用语言的灵活性，它允许多种有效方法并需要隐式状态管理。为了验证这一假设，我们引入了Anka，一种用于数据转换管道的领域特定语言（DSL），它具有显式、受约束的语法，从而减少了代码生成中的歧义。尽管之前没有接受过Anka的训练，Claude 3.5 Haiku在100个基准问题中实现了99.9%的解析成功率和95.8%的总体任务准确率。关键的是，Anka在多步骤管道任务上比Python表现出40个百分点的准确率优势（100% vs. 60%），其中Python的灵活语法导致操作排序和变量管理中频繁出现错误。使用GPT-4o-mini进行的跨模型验证证实了这一优势（在多步骤任务上+26.7个百分点）。我们的结果表明：（1）LLM可以完全从上下文提示中学习新的DSL，达到接近原生准确率；（2）受约束的语法显著减少了复杂任务中的错误；（3）专门为LLM生成而设计的领域特定语言可以胜过LLM接受过广泛训练的通用语言。我们发布完整的语言实现、基准测试套件和评估框架，以促进进一步研究。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）在执行复杂、多步骤数据转换任务时代码生成可靠性不足的问题。现有通用编程语言（如Python）的灵活性导致LLMs在操作排序、变量管理等方面容易出错，从而降低了任务的整体准确率。

**核心思路**：论文的核心思路是设计一种领域特定语言（DSL），即Anka，它具有显式且受约束的语法，从而减少LLM在代码生成过程中的歧义。通过限制语言的表达方式，可以引导LLM生成更可靠、更符合预期的代码。

**技术框架**：Anka的设计目标是简化数据转换管道的构建。其整体框架包括：定义明确的数据类型和操作符；使用显式语法来指定数据流和操作顺序；提供一套完整的基准测试套件和评估框架，用于评估LLM在Anka上的代码生成能力。

**关键创新**：该论文的关键创新在于提出了一种专门为LLM代码生成设计的DSL，并验证了其在复杂任务上的有效性。与现有方法不同，Anka不是试图改进LLM本身，而是通过约束编程语言来提高LLM的性能。

**关键设计**：Anka的关键设计包括：1) 显式的数据类型声明，减少类型推断错误；2) 受限的操作符集合，避免不必要的复杂性；3) 强制性的数据流定义，确保操作顺序的正确性；4) 简洁的语法结构，降低LLM的学习难度。论文未提及具体的参数设置或损失函数，因为Anka本身是一种编程语言，而非机器学习模型。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23214v1/complexity_advantage.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Claude 3.5 Haiku在Anka上实现了99.9%的解析成功率和95.8%的总体任务准确率。在多步骤管道任务上，Anka比Python表现出40个百分点的准确率优势（100% vs. 60%）。使用GPT-4o-mini进行的跨模型验证也证实了Anka的优势（在多步骤任务上+26.7个百分点）。

## 🎯 应用场景

该研究成果可应用于需要高可靠性代码生成的领域，例如数据清洗、ETL流程、自动化报告生成等。通过使用领域特定语言，可以降低开发成本，提高代码质量，并减少人工干预。未来，可以进一步扩展Anka的功能，支持更复杂的数据转换场景，并将其应用于其他领域。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated remarkable capabilities in code generation, yet they exhibit systematic errors on complex, multi-step programming tasks. We hypothesize that these errors stem from the flexibility of general-purpose languages, which permits multiple valid approaches and requires implicit state management. To test this hypothesis, we introduce Anka, a domain-specific language (DSL) for data transformation pipelines designed with explicit, constrained syntax that reduces ambiguity in code generation. Despite having zero prior training exposure to Anka, Claude 3.5 Haiku achieves 99.9% parse success and 95.8% overall task accuracy across 100 benchmark problems. Critically, Anka demonstrates a 40 percentage point accuracy advantage over Python on multi-step pipeline tasks (100% vs. 60%), where Python's flexible syntax leads to frequent errors in operation sequencing and variable management. Cross-model validation with GPT-4o-mini confirms this advantage (+26.7 percentage points on multi-step tasks). Our results demonstrate that: (1) LLMs can learn novel DSLs entirely from in-context prompts, achieving near-native accuracy; (2) constrained syntax significantly reduces errors on complex tasks; and (3) domain-specific languages purposefully designed for LLM generation can outperform general-purpose languages on which the LLM has extensive training. We release the complete language implementation, benchmark suite, and evaluation framework to facilitate further research.

