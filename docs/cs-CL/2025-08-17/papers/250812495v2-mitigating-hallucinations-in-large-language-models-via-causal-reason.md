---
layout: default
title: Mitigating Hallucinations in Large Language Models via Causal Reasoning
---

# Mitigating Hallucinations in Large Language Models via Causal Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12495" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12495v2</a>
  <a href="https://arxiv.org/pdf/2508.12495.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12495v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12495v2', 'Mitigating Hallucinations in Large Language Models via Causal Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuangang Li, Yiqing Shen, Yi Nian, Jiechao Gao, Ziyi Wang, Chenxiao Yu, Shawn Li, Jie Wang, Xiyang Hu, Yue Zhao

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-17 (更新: 2025-11-12)

**🔗 代码/项目**: [GITHUB](https://github.com/MrLYG/CDCR-SFT)

---

## 💡 一句话要点

**提出CDCR-SFT以解决大语言模型的幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `因果推理` `大型语言模型` `有向无环图` `逻辑一致性` `监督微调` `自然语言处理` `推理能力`

## 📋 核心要点

1. 现有的推理方法在处理因果关系时存在不足，无法有效表示条件独立性和满足因果识别假设。
2. 本文提出CDCR-SFT框架，通过显式构建变量级DAG来增强LLMs的因果推理能力。
3. 实验结果显示，CDCR-SFT在多个任务上显著提升了因果推理能力，并有效减少了幻觉现象。

## 📝 摘要（中文）

大型语言模型（LLMs）常常出现逻辑不一致的幻觉现象，这些幻觉看似连贯却违反推理原则。近期研究表明，因果推理能力与幻觉现象之间存在反向关系。现有的推理方法如链式思维（CoT）主要在语言符号层面操作，未能有效建模变量之间的因果关系。为此，本文提出了一种因果DAG构建与推理的监督微调框架（CDCR-SFT），该框架训练LLMs显式构建变量级有向无环图（DAG），并在其上进行推理。此外，本文还构建了一个包含25,368个样本的数据集（CausalDR），每个样本包括输入问题、显式因果DAG、基于图的推理轨迹和验证答案。实验结果表明，CDCR-SFT在CLADDER任务上达到了95.33%的准确率，首次超越人类表现的94.8%，并在HaluEval上减少了10%的幻觉现象。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型中存在的逻辑不一致幻觉问题。现有的推理方法如链式思维（CoT）在语言符号层面操作，未能有效建模变量之间的因果关系，导致推理能力不足。

**核心思路**：论文提出的CDCR-SFT框架通过显式构建变量级的有向无环图（DAG），使模型能够在因果结构上进行推理，从而提升因果推理能力并减少幻觉现象。

**技术框架**：CDCR-SFT框架包括两个主要模块：首先是因果DAG的构建模块，模型根据输入问题生成相应的DAG；其次是推理模块，模型在构建的DAG上进行推理，输出最终答案。

**关键创新**：最重要的技术创新在于显式因果结构建模，区别于现有方法仅在语言层面进行推理，CDCR-SFT能够有效捕捉变量之间的因果关系，提升推理的准确性和一致性。

**关键设计**：在模型训练中，采用监督微调策略，损失函数设计为结合推理准确性和因果结构的损失，确保模型在学习过程中能够有效构建和利用DAG。

## 📊 实验亮点

实验结果显示，CDCR-SFT在CLADDER任务上达到了95.33%的准确率，首次超越人类表现的94.8%。此外，在HaluEval任务上，模型的幻觉现象减少了10%，显著提升了推理的可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和自动推理等。通过提升大型语言模型的因果推理能力，可以在更复杂的推理任务中提供更准确的答案，减少逻辑不一致的现象，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models (LLMs) exhibit logically inconsistent hallucinations that appear coherent yet violate reasoning principles, with recent research suggesting an inverse relationship between causal reasoning capabilities and such hallucinations. However, existing reasoning approaches in LLMs, such as Chain-of-Thought (CoT) and its graph-based variants, operate at the linguistic token level rather than modeling the underlying causal relationships between variables, lacking the ability to represent conditional independencies or satisfy causal identification assumptions. To bridge this gap, we introduce causal-DAG construction and reasoning (CDCR-SFT), a supervised fine-tuning framework that trains LLMs to explicitly construct variable-level directed acyclic graph (DAG) and then perform reasoning over it. Moreover, we present a dataset comprising 25,368 samples (CausalDR), where each sample includes an input question, explicit causal DAG, graph-based reasoning trace, and validated answer. Experiments on four LLMs across eight tasks show that CDCR-SFT improves the causal reasoning capability with the state-of-the-art 95.33% accuracy on CLADDER (surpassing human performance of 94.8% for the first time) and reduces the hallucination on HaluEval with 10% improvements. It demonstrates that explicit causal structure modeling in LLMs can effectively mitigate logical inconsistencies in LLM outputs. Code is available at https://github.com/MrLYG/CDCR-SFT.

