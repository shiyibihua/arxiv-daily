---
layout: default
title: A Systematic Study of Code Obfuscation Against LLM-based Vulnerability Detection
---

# A Systematic Study of Code Obfuscation Against LLM-based Vulnerability Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16538" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16538v1</a>
  <a href="https://arxiv.org/pdf/2512.16538.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16538v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16538v1', 'A Systematic Study of Code Obfuscation Against LLM-based Vulnerability Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiao Li, Yue Li, Hao Wu, Yue Zhang, Yechao Zhang, Fengyuan Xu, Sheng Zhong

**分类**: cs.CR, cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**系统性研究代码混淆对基于LLM的漏洞检测的影响，揭示其有效性边界**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码混淆` `漏洞检测` `大型语言模型` `LLM` `软件安全`

## 📋 核心要点

1. 现有代码混淆工具在技术、粒度和语言支持上存在差异，缺乏统一框架评估其对LLM漏洞检测的影响。
2. 论文系统性地对代码混淆技术进行分类，并在统一框架下评估其对多种LLM漏洞检测的影响。
3. 实验揭示了代码混淆对LLM漏洞检测的正反两方面影响，并分析了影响因素，为提升LLM鲁棒性提供方向。

## 📝 摘要（中文）

随着大型语言模型（LLM）越来越多地应用于代码漏洞检测，其在各种漏洞类型上的可靠性和鲁棒性日益受到关注。代码混淆作为一种绕过审计工具的通用策略，长期以来被用于传统的对抗环境中，它在不篡改工具本身的情况下保留了可利用性。现有的混淆方法和工具在支持的技术、粒度和编程语言方面存在差异，这使得系统性地评估它们对基于LLM的漏洞检测的影响变得困难。为了弥补这一差距，本文对混淆技术进行了结构化的系统化研究，并在统一的框架下评估了它们。具体来说，我们将现有的混淆方法分为三大类（布局、数据流和控制流），涵盖11个子类别和19个具体技术。我们使用一致的LLM驱动方法在四种编程语言（Solidity、C、C++和Python）中实现了这些技术，并评估了它们对跨越四个模型系列（DeepSeek、OpenAI、Qwen和LLaMA）的15个LLM以及两个编码代理（GitHub Copilot和Codex）的影响。我们的研究结果揭示了代码混淆对基于LLM的漏洞检测的积极和消极影响，突出了混淆导致性能提升或下降的条件。我们进一步分析了这些结果与漏洞特征、代码属性和模型属性的关系。最后，我们概述了几个开放性问题，并提出了未来方向，以增强LLM在实际漏洞检测中的鲁棒性。

## 🔬 方法详解

**问题定义**：论文旨在解决现有代码混淆方法缺乏系统性评估，难以衡量其对基于LLM的漏洞检测工具的影响的问题。现有方法的痛点在于混淆技术种类繁多，缺乏统一的评估标准和框架，导致无法有效评估其对不同LLM模型和漏洞类型的影响。

**核心思路**：论文的核心思路是对现有的代码混淆技术进行系统性的分类和整理，构建一个统一的评估框架，并在该框架下评估不同混淆技术对多种LLM漏洞检测工具的影响。通过这种方式，可以揭示不同混淆技术对LLM漏洞检测的有效性边界，并为提升LLM的鲁棒性提供指导。

**技术框架**：论文构建的评估框架主要包含以下几个模块：1) 代码混淆技术分类模块：将现有的代码混淆技术分为布局、数据流和控制流三大类，并细分为11个子类别和19个具体技术。2) 代码混淆实现模块：在四种编程语言（Solidity、C、C++和Python）中实现这些混淆技术。3) LLM漏洞检测模块：使用15个LLM模型和2个编码代理进行漏洞检测。4) 评估模块：评估不同混淆技术对LLM漏洞检测的影响，并分析影响因素。

**关键创新**：论文最重要的技术创新点在于对代码混淆技术进行了系统性的分类和整理，并构建了一个统一的评估框架。该框架可以用于评估不同混淆技术对多种LLM漏洞检测工具的影响，从而揭示不同混淆技术对LLM漏洞检测的有效性边界。与现有方法相比，该方法更加系统和全面，可以为提升LLM的鲁棒性提供更有效的指导。

**关键设计**：论文的关键设计包括：1) 代码混淆技术的分类标准：基于布局、数据流和控制流三个维度进行分类。2) 评估指标：使用漏洞检测的准确率、召回率等指标来评估混淆技术的影响。3) 实验设置：选择具有代表性的LLM模型和编码代理，以及多种漏洞类型进行评估。

## 📊 实验亮点

实验结果表明，代码混淆对LLM漏洞检测的影响是双面的，某些混淆技术可以提升检测性能，而另一些则会降低性能。研究发现，混淆效果与漏洞特征、代码属性和模型属性密切相关。例如，某些混淆技术对特定类型的漏洞更有效，而某些LLM模型对特定混淆技术的抵抗能力更强。

## 🎯 应用场景

该研究成果可应用于提升软件安全性和LLM的鲁棒性。开发者可以利用研究结果选择合适的混淆技术来保护代码，同时避免过度混淆导致LLM漏洞检测失效。研究结果也能帮助LLM开发者提升模型对混淆代码的识别能力，增强其在实际应用中的可靠性。

## 📄 摘要（原文）

> As large language models (LLMs) are increasingly adopted for code vulnerability detection, their reliability and robustness across diverse vulnerability types have become a pressing concern. In traditional adversarial settings, code obfuscation has long been used as a general strategy to bypass auditing tools, preserving exploitability without tampering with the tools themselves. Numerous efforts have explored obfuscation methods and tools, yet their capabilities differ in terms of supported techniques, granularity, and programming languages, making it difficult to systematically assess their impact on LLM-based vulnerability detection. To address this gap, we provide a structured systematization of obfuscation techniques and evaluate them under a unified framework. Specifically, we categorize existing obfuscation methods into three major classes (layout, data flow, and control flow) covering 11 subcategories and 19 concrete techniques. We implement these techniques across four programming languages (Solidity, C, C++, and Python) using a consistent LLM-driven approach, and evaluate their effects on 15 LLMs spanning four model families (DeepSeek, OpenAI, Qwen, and LLaMA), as well as on two coding agents (GitHub Copilot and Codex). Our findings reveal both positive and negative impacts of code obfuscation on LLM-based vulnerability detection, highlighting conditions under which obfuscation leads to performance improvements or degradations. We further analyze these outcomes with respect to vulnerability characteristics, code properties, and model attributes. Finally, we outline several open problems and propose future directions to enhance the robustness of LLMs for real-world vulnerability detection.

