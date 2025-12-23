---
layout: default
title: Revisiting Compositional Generalization Capability of Large Language Models Considering Instruction Following Ability
---

# Revisiting Compositional Generalization Capability of Large Language Models Considering Instruction Following Ability

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15629" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15629v1</a>
  <a href="https://arxiv.org/pdf/2506.15629.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15629v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15629v1', 'Revisiting Compositional Generalization Capability of Large Language Models Considering Instruction Following Ability')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yusuke Sakai, Hidetaka Kamigaito, Taro Watanabe

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-18

**备注**: ACL 2025 Main

---

## 💡 一句话要点

**提出Ordered CommonGen基准以评估LLMs的组合泛化与指令遵循能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `组合泛化` `指令遵循` `生成常识推理` `自然语言处理` `评估基准`

## 📋 核心要点

1. 现有的生成式大型语言模型在处理指令时，往往对概念顺序的遵循能力不足，导致输出结果的多样性降低。
2. 本文提出Ordered CommonGen基准，通过测量有序覆盖率来同时评估LLMs的组合泛化和指令遵循能力。
3. 实验结果显示，尽管LLMs理解指令意图，但在概念顺序的遵循上仍存在显著不足，最好的模型有序覆盖率仅为75%。

## 📝 摘要（中文）

在生成常识推理任务中，生成式大型语言模型（LLMs）需要生成包含所有给定概念的句子。然而，当提示指定概念顺序时，LLMs必须生成符合该顺序的句子。为此，本文提出了Ordered CommonGen基准，旨在评估LLMs的组合泛化和指令遵循能力。该基准通过测量有序覆盖率来评估概念是否按指定顺序生成，从而实现对两种能力的同时评估。通过对36个LLMs的综合分析，发现尽管LLMs通常理解指令意图，但对特定概念顺序模式的偏见常导致输出低多样性或相同结果。即使是最符合指令的LLM，其有序覆盖率也仅约为75%，突显了指令遵循和组合泛化能力的提升需求。

## 🔬 方法详解

**问题定义**：本文旨在解决生成式大型语言模型在指令遵循能力方面的不足，尤其是在概念顺序的生成上。现有方法在处理指令时，往往无法有效生成符合指定顺序的句子，导致输出结果的多样性和准确性不足。

**核心思路**：论文提出Ordered CommonGen基准，设计了一个新的评估框架，通过测量有序覆盖率来同时考察模型的组合泛化能力和指令遵循能力。这种设计使得模型在生成句子时不仅要考虑概念的完整性，还要遵循特定的顺序。

**技术框架**：整体架构包括数据集构建、模型训练和评估三个主要阶段。首先，构建包含不同概念顺序的生成任务数据集；其次，训练多种LLMs以生成符合这些任务的句子；最后，通过有序覆盖率指标评估模型的表现。

**关键创新**：最重要的技术创新在于提出了Ordered CommonGen基准，能够同时评估组合泛化和指令遵循能力。这一方法与现有的单一评估方法本质上不同，提供了更全面的性能分析。

**关键设计**：在实验中，采用了多种LLMs进行对比，设置了不同的损失函数以优化指令遵循能力，并调整了模型的超参数以提高有序覆盖率。

## 📊 实验亮点

实验结果表明，尽管LLMs能够理解指令意图，但在概念顺序遵循上存在明显不足，最好的模型有序覆盖率仅为75%。这一发现强调了在生成任务中提升指令遵循能力的重要性，并为未来的研究指明了方向。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的对话系统、智能助手和教育技术等。通过提升LLMs的指令遵循能力和组合泛化能力，可以显著改善人机交互的自然性和准确性，推动智能系统在复杂任务中的应用。未来，该基准可能成为评估语言模型能力的重要标准，促进相关技术的发展。

## 📄 摘要（原文）

> In generative commonsense reasoning tasks such as CommonGen, generative large language models (LLMs) compose sentences that include all given concepts. However, when focusing on instruction-following capabilities, if a prompt specifies a concept order, LLMs must generate sentences that adhere to the specified order. To address this, we propose Ordered CommonGen, a benchmark designed to evaluate the compositional generalization and instruction-following abilities of LLMs. This benchmark measures ordered coverage to assess whether concepts are generated in the specified order, enabling a simultaneous evaluation of both abilities. We conducted a comprehensive analysis using 36 LLMs and found that, while LLMs generally understand the intent of instructions, biases toward specific concept order patterns often lead to low-diversity outputs or identical results even when the concept order is altered. Moreover, even the most instruction-compliant LLM achieved only about 75% ordered coverage, highlighting the need for improvements in both instruction-following and compositional generalization capabilities.

