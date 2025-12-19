---
layout: default
title: Beyond Blind Spots: Analytic Hints for Mitigating LLM-Based Evaluation Pitfalls
---

# Beyond Blind Spots: Analytic Hints for Mitigating LLM-Based Evaluation Pitfalls

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16272" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16272v1</a>
  <a href="https://arxiv.org/pdf/2512.16272.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16272v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16272v1', 'Beyond Blind Spots: Analytic Hints for Mitigating LLM-Based Evaluation Pitfalls')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ora Nova Fandina, Eitan Farchi, Shmulik Froimovich, Raviv Gal, Wesam Ibraheem, Rami Katan, Alice Podolsky

**分类**: cs.SE, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**利用分析提示缓解LLM代码评估中的盲点，提升COBOL代码生成质量**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `代码评估` `COBOL代码生成` `遗留系统现代化` `分析提示`

## 📋 核心要点

1. 现有LaaJ在代码生成评估中存在领域盲点，无法有效识别特定领域的关键错误，影响评估可靠性。
2. 提出一种分析提示方法，通过轻量级分析检查工具识别领域问题，并将其作为提示注入LaaJ，引导其重新评估。
3. 实验表明，LaaJ+提示配置显著提升错误检测覆盖率，最高可达94%，并生成更准确的解释。

## 📝 摘要（中文）

大型语言模型（LLM）越来越多地被用作代码生成流程中的评估者（LaaJ）。尽管其可扩展性具有吸引力，但LaaJ往往忽略特定领域的关键问题，引发对其在关键评估任务中可靠性的担忧。为了更好地理解这些局限性，本文研究了LaaJ在工业用例中的行为：通过COBOL代码生成实现遗留代码现代化。研究发现，即使是生产环境中部署的LaaJ也会遗漏领域关键错误，揭示其评估能力中存在一致的盲点。为了更好地理解这些盲点，本文分析了生成的COBOL程序和相关的LaaJ判断，并利用专家知识构建了一个初步的分类。基于此分类，开发了一个轻量级的分析检查工具，用于标记实践中观察到的30多个特定领域问题。该工具的输出被用作分析提示，动态地注入到评估者的提示中，以鼓励LaaJ重新审视可能被忽略的方面。在包含100个程序的测试集上，使用四个生产级别的LaaJ进行的实验表明，LaaJ单独检测到的错误仅占代码中存在的错误的约45%（在所有测试的评估者中），而分析检查器本身缺乏解释深度。当结合使用时，LaaJ+提示配置实现了高达94%的覆盖率（对于性能最佳的评估者和注入提示），并产生了质量更高、更准确的解释，表明分析-LLM混合方法可以显著提高已部署流程中的评估可靠性。本文发布了数据集和所有使用的提示。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在评估COBOL代码生成质量时存在的盲点问题。现有方法，即直接使用LLM作为评估者（LaaJ），在评估特定领域（如COBOL）的代码时，容易忽略领域相关的错误，导致评估结果不准确，影响代码质量。现有方法的痛点在于LLM缺乏对特定领域知识的深入理解。

**核心思路**：论文的核心思路是将领域专家的知识融入到LLM的评估过程中。具体来说，通过一个轻量级的分析检查工具，自动检测生成的COBOL代码中存在的特定领域问题，并将这些问题作为“分析提示”注入到LLM的评估提示中。这样，LLM在评估代码时，可以根据这些提示，更加关注可能存在的领域错误，从而提高评估的准确性。

**技术框架**：整体框架包含以下几个主要模块：1) COBOL代码生成器：生成需要评估的COBOL代码。2) 分析检查工具：基于专家知识，对生成的COBOL代码进行静态分析，检测潜在的领域问题，生成分析提示。3) LaaJ：接收生成的COBOL代码和分析提示，根据提示对代码进行评估，并给出评估结果和解释。4) 提示注入模块：将分析检查工具生成的提示动态地注入到LaaJ的评估提示中。

**关键创新**：最重要的技术创新点在于将领域专家的知识以“分析提示”的形式融入到LLM的评估过程中。与现有方法相比，该方法不需要对LLM进行额外的训练或微调，而是通过简单的提示工程，即可显著提高LLM在特定领域代码评估中的准确性。这种方法具有轻量级、易于部署的优点。

**关键设计**：分析检查工具的设计是关键。该工具基于专家知识，定义了30多个COBOL代码中常见的错误模式。这些错误模式被编码为静态分析规则，用于检测生成的COBOL代码中是否存在这些错误。提示注入模块的设计也很重要，需要选择合适的提示格式和注入方式，以确保LLM能够有效地利用这些提示。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16272v1/hint_llaj.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16272v1/taxonomy.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16272v1/hybrid_laaj_issues_triplets_total_native_orange_leftlegend.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，单独使用LaaJ只能检测到约45%的错误，而结合分析提示后，错误检测覆盖率最高可达94%。与单独使用LaaJ相比，LaaJ+提示配置不仅提高了错误检测率，还生成了质量更高、更准确的解释。这些结果表明，分析-LLM混合方法可以显著提高已部署流程中的评估可靠性。

## 🎯 应用场景

该研究成果可应用于遗留系统现代化改造、代码质量保证、自动化代码审查等领域。通过结合领域专家知识和LLM的强大能力，可以显著提高代码评估的准确性和效率，降低人工成本，加速软件开发和维护过程。未来，该方法可以推广到其他领域，例如金融、医疗等，提升LLM在特定领域的应用价值。

## 📄 摘要（原文）

> Large Language Models are increasingly deployed as judges (LaaJ) in code generation pipelines. While attractive for scalability, LaaJs tend to overlook domain specific issues raising concerns about their reliability in critical evaluation tasks. To better understand these limitations in practice, we examine LaaJ behavior in a concrete industrial use case: legacy code modernization via COBOL code generation. In this setting, we find that even production deployed LaaJs can miss domain critical errors, revealing consistent blind spots in their evaluation capabilities.
>   To better understand these blind spots, we analyze generated COBOL programs and associated LaaJs judgments, drawing on expert knowledge to construct a preliminary taxonomy. Based on this taxonomy, we develop a lightweight analytic checker tool that flags over 30 domain specific issues observed in practice. We use its outputs as analytic hints, dynamically injecting them into the judges prompt to encourage LaaJ to revisit aspects it may have overlooked.
>   Experiments on a test set of 100 programs using four production level LaaJs show that LaaJ alone detects only about 45% of the errors present in the code (in all judges we tested), while the analytic checker alone lacks explanatory depth. When combined, the LaaJ+Hints configuration achieves up to 94% coverage (for the best performing judge and injection prompt) and produces qualitatively richer, more accurate explanations, demonstrating that analytic-LLM hybrids can substantially enhance evaluation reliability in deployed pipelines. We release the dataset and all used prompts.

