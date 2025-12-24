---
layout: default
title: Can Large Models Teach Student Models to Solve Mathematical Problems Like Human Beings? A Reasoning Distillation Method via Multi-LoRA Interaction
---

# Can Large Models Teach Student Models to Solve Mathematical Problems Like Human Beings? A Reasoning Distillation Method via Multi-LoRA Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13037" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13037v1</a>
  <a href="https://arxiv.org/pdf/2508.13037.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13037v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13037v1', 'Can Large Models Teach Student Models to Solve Mathematical Problems Like Human Beings? A Reasoning Distillation Method via Multi-LoRA Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinhe Li, Jiajun Liu, Peng Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-18

**备注**: Accepted by IJCAI2025

---

## 💡 一句话要点

**提出多LoRA交互的蒸馏方法以提升小模型数学推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数学推理` `小型语言模型` `蒸馏训练` `多LoRA交互` `知识生成` `深度推理` `人工智能`

## 📋 核心要点

1. 现有方法通常依赖于大型语言模型生成数据，导致小型语言模型在数学推理上表现不佳。
2. 本文提出的LoRID方法通过多LoRA交互，结合直观推理和知识生成，模仿人类的两种思维模式。
3. 实验结果表明，LoRID在GSM8K数据集上超越了第二名方法，准确率提升幅度达到2.3%至16.1%。

## 📝 摘要（中文）

近期研究表明，大型语言模型（LLMs）在数学推理方面表现出色，但其依赖于数百亿参数。为了解决小型语言模型（SLMs）推理能力不足的问题，现有方法通常利用LLMs生成大量数据进行训练。本文提出了一种基于多LoRA交互的数学推理蒸馏方法（LoRID），通过输入问题和推理生成知识增强数据集，训练直观推理器（IR）和知识生成器（KG）、深度推理器（DR）以模仿人类的两种思维模式。实验结果显示，LoRID在GSM8K数据集上取得了最先进的性能，显著超越了第二名方法。

## 🔬 方法详解

**问题定义**：本文旨在解决小型语言模型在数学推理方面的不足，现有方法主要依赖大型语言模型生成数据，导致推理能力有限。

**核心思路**：提出的LoRID方法通过多LoRA交互，模拟人类的直观推理（System 1）和深度推理（System 2），从而提升小型模型的推理能力。

**技术框架**：整体架构包括三个主要模块：直观推理器（IR）生成链式思维，知识生成器（KG）输出知识，深度推理器（DR）基于知识进行推理。

**关键创新**：LoRID的创新在于通过多LoRA交互实现知识的相互反馈，增强了小型模型的推理能力，与传统方法相比，提供了更为系统的学习机制。

**关键设计**：在训练过程中，IR、KG和DR之间的输出需要进行一致性评估，若不一致则需迭代推理过程，以确保生成结果的可靠性。

## 📊 实验亮点

LoRID在GSM8K数据集上取得了显著的实验结果，准确率分别提升了2.3%、16.1%、2.4%、12.3%和1.8%，超越了第二名方法，展示了其在数学推理任务中的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、智能辅导系统和自动化数学问题解决等。通过提升小型模型的数学推理能力，可以在资源受限的环境中实现高效的学习和推理，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent studies have demonstrated that Large Language Models (LLMs) have strong mathematical reasoning abilities but rely on hundreds of billions of parameters. To tackle the challenge of poor reasoning in Small Language Models (SLMs), existing methods typically leverage LLMs to generate massive amounts of data for cramming training. In psychology, they are akin to System 1 thinking, which resolves reasoning problems rapidly based on experience and intuition. However, human learning also requires System 2 thinking, where knowledge is first acquired and then reinforced through practice. Inspired by such two distinct modes of thinking, we propose a novel method based on the multi-LoRA Interaction for mathematical reasoning Distillation (LoRID). First, we input the question and reasoning of each sample into an LLM to create knowledge-enhanced datasets. Subsequently, we train a LoRA block on the student model as an Intuitive Reasoner (IR), which directly generates Chain-of-Thoughts for problem-solving. Then, to imitate System 2 thinking, we train the Knowledge Generator (KG) and Deep Reasoner (DR), respectively. The former outputs only knowledge after receiving problems, while the latter uses that knowledge to perform reasoning. Finally, to address the randomness in the generation of IR and DR, we evaluate whether their outputs are consistent, and the inference process needs to be iterated if not. This step can enhance the mathematical reasoning ability of SLMs through mutual feedback. Experimental results show that LoRID achieves state-of-the-art performance, especially on the GSM8K dataset, where it outperforms the second-best method by 2.3%, 16.1%, 2.4%, 12.3%, and 1.8% accuracy across the five base models, respectively.

