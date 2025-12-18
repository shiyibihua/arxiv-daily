---
layout: default
title: Can Large Language Models Robustly Perform Natural Language Inference for Japanese Comparatives?
---

# Can Large Language Models Robustly Perform Natural Language Inference for Japanese Comparatives?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13695" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13695v1</a>
  <a href="https://arxiv.org/pdf/2509.13695.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13695v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13695v1', 'Can Large Language Models Robustly Perform Natural Language Inference for Japanese Comparatives?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yosuke Mikami, Daiki Matsuoka, Hitomi Yanaka

**分类**: cs.CL

**发布日期**: 2025-09-17

**备注**: To appear in Proceedings of the 16th International Conference on Computational Semantics (IWCS 2025)

---

## 💡 一句话要点

**构建日语比较句NLI数据集，评估大语言模型在此任务上的鲁棒性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自然语言推理` `日语` `比较句` `大型语言模型` `数据集` `零样本学习` `少样本学习`

## 📋 核心要点

1. 现有NLI方法在处理包含数值和逻辑表达式的比较句推理时面临挑战，尤其是在日语等非主流语言上。
2. 论文构建了一个日语比较句NLI数据集，用于评估LLMs在此任务上的鲁棒性，并探索有效的提示方法。
3. 实验表明，LLMs的性能受提示格式和少样本示例标签的影响，且难以处理日语特有的语言现象。

## 📝 摘要（中文）

大型语言模型（LLMs）在自然语言推理（NLI）方面表现出色。然而，涉及数值和逻辑表达式的NLI仍然具有挑战性。比较句是与此类推理相关的关键语言现象，但LLMs处理比较句的鲁棒性，尤其是在模型训练数据中不占主导地位的语言（如日语）方面，尚未得到充分探索。为了弥补这一差距，我们构建了一个专注于比较句的日语NLI数据集，并在零样本和少样本设置中评估了各种LLMs。结果表明，模型的性能对零样本设置中的提示格式敏感，并受到少样本示例中黄金标签的影响。LLMs也难以处理日语特有的语言现象。此外，我们观察到，包含逻辑语义表示的提示有助于模型预测正确标签，即使在少样本示例中难以解决的推理问题也能得到解决。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）在日语比较句自然语言推理（NLI）任务上的鲁棒性问题。现有方法在处理涉及数值和逻辑表达式的比较句时表现不佳，尤其是在日语这种训练数据相对较少的语言上，缺乏针对性的数据集和评估。

**核心思路**：论文的核心思路是通过构建一个专门针对日语比较句的NLI数据集，来系统地评估LLMs在此任务上的表现。同时，探索不同的提示方法，包括零样本、少样本以及包含逻辑语义表示的提示，以提高LLMs的推理能力。

**技术框架**：论文主要包含以下几个阶段：1) 构建日语比较句NLI数据集；2) 在零样本和少样本设置下，使用不同的提示格式评估各种LLMs；3) 分析LLMs在处理日语特有语言现象时的表现；4) 探索包含逻辑语义表示的提示对模型性能的影响。

**关键创新**：论文的关键创新在于构建了一个专门针对日语比较句的NLI数据集，填补了该领域的空白。此外，论文还探索了包含逻辑语义表示的提示方法，并验证了其在提高LLMs推理能力方面的有效性。

**关键设计**：论文的关键设计包括：1) 数据集的构建，需要仔细设计比较句的类型和难度，以及对应的推理标签；2) 提示格式的选择，需要考虑不同格式对模型性能的影响；3) 逻辑语义表示的构建，需要选择合适的表示方法，并将其融入到提示中。

## 📊 实验亮点

实验结果表明，LLMs在日语比较句NLI任务上的性能对提示格式非常敏感。在少样本学习中，黄金标签会影响模型的预测结果。此外，LLMs难以处理日语特有的语言现象。然而，包含逻辑语义表示的提示可以显著提高模型在困难推理问题上的性能。

## 🎯 应用场景

该研究成果可应用于智能问答系统、机器翻译、文本摘要等自然语言处理领域，尤其是在需要处理日语比较句的场景下。通过提高LLMs在比较句推理方面的鲁棒性，可以提升相关应用的准确性和可靠性，并为未来研究提供基准和思路。

## 📄 摘要（原文）

> Large Language Models (LLMs) perform remarkably well in Natural Language Inference (NLI). However, NLI involving numerical and logical expressions remains challenging. Comparatives are a key linguistic phenomenon related to such inference, but the robustness of LLMs in handling them, especially in languages that are not dominant in the models' training data, such as Japanese, has not been sufficiently explored. To address this gap, we construct a Japanese NLI dataset that focuses on comparatives and evaluate various LLMs in zero-shot and few-shot settings. Our results show that the performance of the models is sensitive to the prompt formats in the zero-shot setting and influenced by the gold labels in the few-shot examples. The LLMs also struggle to handle linguistic phenomena unique to Japanese. Furthermore, we observe that prompts containing logical semantic representations help the models predict the correct labels for inference problems that they struggle to solve even with few-shot examples.

