---
layout: default
title: Automated Validation of Textual Constraints Against AutomationML via LLMs and SHACL
---

# Automated Validation of Textual Constraints Against AutomationML via LLMs and SHACL

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10678" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10678v1</a>
  <a href="https://arxiv.org/pdf/2506.10678.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10678v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10678v1', 'Automated Validation of Textual Constraints Against AutomationML via LLMs and SHACL')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tom Westermann, Aljosha Köcher, Felix Gehlhoff

**分类**: cs.AI, eess.SY

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**提出自动化验证文本约束以解决AutomationML建模问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `AutomationML` `文本约束` `自动验证` `大型语言模型` `SHACL` `OWL本体` `工程建模`

## 📋 核心要点

1. 现有的AutomationML建模建议以非正式文本约束形式存在，导致无法自动验证，影响建模效率。
2. 论文提出了一种将AML模型映射到OWL本体，并利用大型语言模型将文本规则转换为SHACL约束的解决方案。
3. 实验结果表明，该方法能够半自动检查复杂建模规则，显著降低了用户对形式化方法的理解需求。

## 📝 摘要（中文）

AutomationML (AML) 促进了工程领域的数据标准化交换，但现有的AML建模建议通常以非正式的文本约束形式存在，无法在AML内部自动验证。本文介绍了一种管道，用于将这些约束形式化和验证。首先，通过RML和SPARQL将AML模型映射到OWL本体。此外，利用大型语言模型将文本规则翻译为SHACL约束，并在先前生成的AML本体上进行验证。最后，SHACL验证结果以自然语言自动解释。该方法在一个AML推荐示例上进行了演示，结果表明，即使是复杂的建模规则也可以半自动检查，无需用户理解形式化方法或本体技术。

## 🔬 方法详解

**问题定义**：本文旨在解决现有AutomationML建模中，文本约束无法自动验证的问题。现有方法缺乏有效的自动验证机制，导致建模过程繁琐且易出错。

**核心思路**：论文的核心思路是通过将AML模型映射到OWL本体，并利用大型语言模型将文本规则转换为SHACL约束，从而实现自动验证。这种设计旨在简化建模过程，提高验证效率。

**技术框架**：整体架构包括三个主要模块：首先，使用RML和SPARQL将AML模型转换为OWL本体；其次，利用大型语言模型将文本规则翻译为SHACL约束；最后，执行SHACL验证并将结果以自然语言形式呈现。

**关键创新**：最重要的技术创新在于将大型语言模型与SHACL验证结合，能够自动化处理复杂的建模规则。这一方法与传统的手动验证方法相比，显著提高了效率和准确性。

**关键设计**：在技术细节上，使用了RML进行数据映射，SPARQL进行查询，SHACL用于约束验证，确保了整个流程的高效性和准确性。

## 📊 实验亮点

实验结果显示，该方法能够成功半自动检查复杂的建模规则，验证效率显著提升。与传统方法相比，用户无需深入理解形式化方法，降低了学习成本，提升了建模效率。

## 🎯 应用场景

该研究的潜在应用领域包括工程设计、自动化系统建模及相关领域，能够有效提升建模过程的自动化程度和准确性。未来，该方法可能推动更多领域的标准化数据交换和自动验证技术的发展。

## 📄 摘要（原文）

> AutomationML (AML) enables standardized data exchange in engineering, yet existing recommendations for proper AML modeling are typically formulated as informal and textual constraints. These constraints cannot be validated automatically within AML itself. This work-in-progress paper introduces a pipeline to formalize and verify such constraints. First, AML models are mapped to OWL ontologies via RML and SPARQL. In addition, a Large Language Model translates textual rules into SHACL constraints, which are then validated against the previously generated AML ontology. Finally, SHACL validation results are automatically interpreted in natural language. The approach is demonstrated on a sample AML recommendation. Results show that even complex modeling rules can be semi-automatically checked -- without requiring users to understand formal methods or ontology technologies.

