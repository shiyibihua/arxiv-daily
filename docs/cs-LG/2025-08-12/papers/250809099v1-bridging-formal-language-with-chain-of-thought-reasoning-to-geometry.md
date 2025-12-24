---
layout: default
title: Bridging Formal Language with Chain-of-Thought Reasoning to Geometry Problem Solving
---

# Bridging Formal Language with Chain-of-Thought Reasoning to Geometry Problem Solving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09099" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09099v1</a>
  <a href="https://arxiv.org/pdf/2508.09099.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09099v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09099v1', 'Bridging Formal Language with Chain-of-Thought Reasoning to Geometry Problem Solving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianyun Yang, Yunwen Li, Ziniu Li, Zhihang Lin, Ruoyu Sun, Tian Ding

**分类**: cs.LG

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出GF-Reasoner以解决几何问题求解中的推理不足**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `几何问题求解` `链式推理` `形式语言` `强化学习` `自然语言处理` `模型优化` `推理透明性`

## 📋 核心要点

1. 现有几何问题求解方法在图形解释和自然语言推理方面存在显著不足，导致决策过程不透明且易出错。
2. 本文提出将链式推理与形式语言结合，模型通过交替生成自然语言推理和可执行代码，增强推理过程的透明度。
3. GF-Reasoner在标准GPS基准上实现了高达15%的准确率提升，表现优于同类7B规模模型及更大规模的Qwen2.5-VL-72B。

## 📝 摘要（中文）

大型视觉语言模型在几何问题求解（GPS）中表现出显著的局限性，主要体现在图形解释不可靠和自然语言推理的不足。为了解决这一问题，本文提出了一种新的方法，将链式推理（CoT）与形式语言相结合，模型在自然语言推理与可执行代码的逐步生成之间交替进行，从而生成混合推理轨迹，关键推导以形式语言表达。通过对新开发的11K合成数据集进行监督微调，并结合基于结果的强化学习，新的模型GF-Reasoner在标准GPS基准上实现了高达15%的准确率提升，超越了同类模型和更大规模的模型Qwen2.5-VL-72B。

## 🔬 方法详解

**问题定义**：本文旨在解决大型视觉语言模型在几何问题求解中的推理不足，现有方法缺乏中间推理，导致决策过程不透明且容易出错。

**核心思路**：通过将链式推理（CoT）与形式语言结合，模型在自然语言推理与可执行代码生成之间交替进行，从而形成清晰的推理轨迹。

**技术框架**：整体架构包括两个主要模块：1) 监督微调模块，利用新开发的合成数据集进行训练；2) 强化学习模块，通过与求解器的交互优化推理过程和生成的程序。

**关键创新**：最重要的创新点在于将链式推理与形式语言结合，生成的推理轨迹更短且更清晰，显著提高了模型的准确性和可解释性。

**关键设计**：在训练过程中，采用了基于结果的奖励机制，优化了链式推理叙述和生成程序的质量，同时对数据合成和训练周期进行了精细设计，以确保模型的有效性。

## 📊 实验亮点

GF-Reasoner在标准几何问题求解基准上实现了高达15%的准确率提升，超越了同类7B规模模型及更大规模的Qwen2.5-VL-72B，展示了其在推理效率和准确性上的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动化设计和智能辅导系统，能够帮助学生和专业人士更好地理解和解决几何问题。未来，该方法可能推动更广泛的形式语言与自然语言结合的研究，提升智能系统的推理能力和应用范围。

## 📄 摘要（原文）

> Large vision language models exhibit notable limitations on Geometry Problem Solving (GPS) because of their unreliable diagram interpretation and pure natural-language reasoning. A recent line of work mitigates this by using symbolic solvers: the model directly generates a formal program that a geometry solver can execute. However, this direct program generation lacks intermediate reasoning, making the decision process opaque and prone to errors. In this work, we explore a new approach that integrates Chain-of-Thought (CoT) with formal language. The model interleaves natural language reasoning with incremental emission of solver-executable code, producing a hybrid reasoning trace in which critical derivations are expressed in formal language. To teach this behavior at scale, we combine (1) supervised fine-tuning on an 11K newly developed synthetic dataset with interleaved natural language reasoning and automatic formalization, and (2) solver-in-the-loop reinforcement learning that jointly optimizes both the CoT narrative and the resulting program through outcome-based rewards. Built on Qwen2.5-VL-7B, our new model, named GF-Reasoner, achieves up to 15% accuracy improvements on standard GPS benchmarks, surpassing both 7B-scale peers and the much larger model Qwen2.5-VL-72B. By exploiting high-order geometric knowledge and offloading symbolic computation to the solver, the generated reasoning traces are noticeably shorter and cleaner. Furthermore, we present a comprehensive analysis of method design choices (e.g., reasoning paradigms, data synthesis, training epochs, etc.), providing actionable insights for future research.

