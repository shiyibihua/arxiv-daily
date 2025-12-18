---
layout: default
title: How to Make Large Language Models Generate 100% Valid Molecules?
---

# How to Make Large Language Models Generate 100% Valid Molecules?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23099" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23099v1</a>
  <a href="https://arxiv.org/pdf/2509.23099.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23099v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23099v1', 'How to Make Large Language Models Generate 100% Valid Molecules?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wen Tao, Jing Tang, Alvin Chan, Bryan Hooi, Baolong Bi, Nanyun Peng, Yuansheng Liu, Yiwei Wang

**分类**: cs.CL, cs.LG

**发布日期**: 2025-09-27

**备注**: EMNLP 2025 Main

**🔗 代码/项目**: [GITHUB](https://github.com/wentao228/SmiSelf)

---

## 💡 一句话要点

**提出SmiSelf框架，确保大语言模型100%生成有效分子**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `分子生成` `大语言模型` `SMILES` `SELFIES` `化学信息学` `药物发现` `材料科学`

## 📋 核心要点

1. 现有方法难以保证大语言模型生成分子的有效性，尤其是在少样本学习场景下，SMILES表示的分子生成容易出错。
2. SmiSelf框架通过将无效SMILES转换为SELFIES，利用SELFIES的特性进行纠正，从而确保生成分子的100%有效性。
3. 实验结果表明，SmiSelf不仅保证了分子有效性，还保留了分子特性，并在其他性能指标上有所提升，具有实际应用价值。

## 📝 摘要（中文）

分子生成是药物发现和材料科学的关键，它能够设计具有特定性质的新型化合物。大型语言模型（LLM）可以通过少量示例学习执行各种任务。然而，对于LLM来说，在少样本设置中使用SMILES等表示生成有效的分子具有挑战性。本文探讨了LLM如何生成100%有效的分子。我们评估了LLM是否可以使用SELFIES（一种每个字符串都对应于有效分子的表示）进行有效分子生成，但发现LLM在使用SELFIES时的表现比使用SMILES时更差。然后，我们检查了LLM纠正无效SMILES的能力，发现它们的能力有限。最后，我们引入了SmiSelf，一个用于无效SMILES校正的跨化学语言框架。SmiSelf使用语法规则将无效SMILES转换为SELFIES，利用SELFIES的机制来纠正无效的SMILES。实验表明，SmiSelf在确保100%有效性的同时，保留了分子特性，并保持甚至提高了其他指标的性能。SmiSelf有助于扩展LLM在生物医学中的实际应用，并且与所有基于SMILES的生成模型兼容。代码可在https://github.com/wentao228/SmiSelf 获取。

## 🔬 方法详解

**问题定义**：论文旨在解决大语言模型（LLM）在分子生成任务中，使用SMILES表示时难以保证生成分子100%有效性的问题。现有的基于SMILES的分子生成方法，即使借助LLM强大的学习能力，仍然容易产生无效的分子结构，这限制了LLM在药物发现和材料科学等领域的应用。

**核心思路**：论文的核心思路是利用SELFIES表示的特性，即任何SELFIES字符串都对应一个有效的分子。通过将无效的SMILES字符串转换为SELFIES，然后利用SELFIES的机制进行校正，最终再转换回SMILES，从而保证生成分子的有效性。这种方法巧妙地结合了SMILES和SELFIES的优点，避免了直接使用LLM生成SELFIES效果不佳的问题。

**技术框架**：SmiSelf框架主要包含以下几个阶段：1) 输入无效的SMILES字符串；2) 使用语法规则将无效SMILES转换为SELFIES；3) 利用SELFIES的内在机制进行校正；4) 将校正后的SELFIES转换回SMILES表示。整个框架是一个跨化学语言的转换过程，核心在于利用SELFIES的有效性保证。

**关键创新**：SmiSelf的关键创新在于提出了一个跨化学语言的框架，巧妙地利用了SELFIES的特性来校正无效的SMILES。与直接使用LLM生成SMILES或SELFIES相比，SmiSelf能够确保100%的分子有效性，同时保留了分子的特性。此外，SmiSelf框架具有通用性，可以与任何基于SMILES的生成模型兼容。

**关键设计**：SmiSelf的关键设计在于SMILES到SELFIES的转换规则和SELFIES到SMILES的转换规则。这些规则需要保证转换过程的可逆性，并且能够有效地利用SELFIES的特性进行校正。具体的转换规则和校正机制在论文中可能没有详细描述，需要参考代码实现。

## 📊 实验亮点

实验结果表明，SmiSelf框架能够确保100%的分子有效性，显著优于直接使用LLM生成SMILES的方法。同时，SmiSelf在保留分子特性方面表现良好，并在某些性能指标上有所提升。这些结果表明SmiSelf是一个有效的分子生成工具，具有实际应用价值。

## 🎯 应用场景

SmiSelf框架在药物发现、材料科学等领域具有广泛的应用前景。它可以帮助研究人员利用大语言模型设计和生成具有特定性质的新型分子，加速新药研发和新材料的发现过程。通过确保生成分子的有效性，SmiSelf可以减少实验验证的成本和时间，提高研发效率。

## 📄 摘要（原文）

> Molecule generation is key to drug discovery and materials science, enabling the design of novel compounds with specific properties. Large language models (LLMs) can learn to perform a wide range of tasks from just a few examples. However, generating valid molecules using representations like SMILES is challenging for LLMs in few-shot settings. In this work, we explore how LLMs can generate 100% valid molecules. We evaluate whether LLMs can use SELFIES, a representation where every string corresponds to a valid molecule, for valid molecule generation but find that LLMs perform worse with SELFIES than with SMILES. We then examine LLMs' ability to correct invalid SMILES and find their capacity limited. Finally, we introduce SmiSelf, a cross-chemical language framework for invalid SMILES correction. SmiSelf converts invalid SMILES to SELFIES using grammatical rules, leveraging SELFIES' mechanisms to correct the invalid SMILES. Experiments show that SmiSelf ensures 100% validity while preserving molecular characteristics and maintaining or even enhancing performance on other metrics. SmiSelf helps expand LLMs' practical applications in biomedicine and is compatible with all SMILES-based generative models. Code is available at https://github.com/wentao228/SmiSelf.

