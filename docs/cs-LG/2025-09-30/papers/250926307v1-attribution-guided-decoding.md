---
layout: default
title: Attribution-Guided Decoding
---

# Attribution-Guided Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26307" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26307v1</a>
  <a href="https://arxiv.org/pdf/2509.26307.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26307v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26307v1', 'Attribution-Guided Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Piotr Komorowski, Elena Golimblevskaia, Reduan Achtibat, Thomas Wiegand, Sebastian Lapuschkin, Wojciech Samek

**分类**: cs.LG

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出基于归因引导的解码方法AGD，提升LLM指令遵循和知识准确性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `可解释性` `归因分析` `解码策略` `指令遵循` `知识密集型任务` `事实准确性`

## 📋 核心要点

1. 现有LLM解码方法在指令遵循和知识准确性方面存在不足，控制技术又容易降低生成质量。
2. AGD通过选择对用户定义ROI归因最高的token，引导LLM生成过程，实现更可靠的输出。
3. 实验表明，AGD显著提升了LLM在指令遵循和知识密集型任务中的性能，并降低了幻觉。

## 📝 摘要（中文）

大型语言模型（LLM）遵循复杂指令和生成准确文本的能力至关重要。然而，标准解码方法难以满足这些要求，现有的控制技术又会降低输出质量。本文提出了一种基于可解释性的解码策略——归因引导解码（AGD）。AGD不直接操纵模型激活，而是考虑一组高概率的候选输出token，并选择对用户定义的感兴趣区域（ROI）归因最高的token。ROI可以灵活地定义在模型输入或内部组件的不同部分，从而引导生成过程朝着期望的行为发展。实验表明，AGD在指令遵循、知识密集型任务中均表现出色，能够显著提高指令遵循的成功率，并减少幻觉，提高事实准确性。此外，还提出了一种自适应的、基于熵的AGD变体，通过仅在模型不确定时应用引导，来减轻质量下降并降低计算开销。AGD是一种通用、可解释且有效的方法，可以增强现代LLM的可靠性。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在解码过程中，难以保证生成文本既能准确遵循指令，又能保证事实的准确性。传统的解码方法缺乏对生成过程的有效控制，而直接操纵模型激活的控制方法又容易损害整体的生成质量。因此，如何更可靠、更可控地引导LLM生成高质量的文本是一个关键问题。

**核心思路**：AGD的核心思路是利用模型的可解释性，通过分析候选token对特定区域（ROI）的归因，选择与用户期望行为最相关的token。这种方法避免了直接干预模型内部状态，从而在保证生成质量的同时，实现了对生成过程的有效引导。通过定义不同的ROI，可以灵活地控制LLM的行为，例如，引导其使用特定的知识来源或遵循特定的指令。

**技术框架**：AGD的整体框架包括以下几个主要步骤：1) 生成一组高概率的候选输出token；2) 定义用户感兴趣区域（ROI），ROI可以是输入文本的特定部分，也可以是模型的内部组件；3) 计算每个候选token对ROI的归因值；4) 选择归因值最高的token作为最终的输出。自适应AGD变体则在模型不确定时（高熵）才应用归因引导，降低计算开销和质量损失。

**关键创新**：AGD的关键创新在于将可解释性方法引入到LLM的解码过程中。与传统的解码方法不同，AGD不是直接基于模型的概率分布选择token，而是考虑了token对特定区域的归因。这种方法提供了一种更细粒度的控制方式，可以更精确地引导LLM的行为。此外，自适应AGD变体通过动态调整引导强度，进一步提高了方法的效率和鲁棒性。

**关键设计**：ROI的定义是AGD的关键设计之一，用户可以根据具体的任务需求，灵活地定义ROI。例如，在知识密集型任务中，可以将ROI定义为外部知识库或模型的内部知识表示。归因方法的选择也很重要，论文中可能使用了某种特定的归因算法（具体算法未知）。自适应AGD变体中，熵阈值的设置会影响引导的频率和强度，需要在效率和性能之间进行权衡。

## 📊 实验亮点

实验结果表明，AGD在指令遵循任务中显著提高了Llama 3.1的成功率，从66.0%提升到79.1%。在知识密集型任务中，AGD能够有效减少幻觉，提高事实准确性。自适应AGD变体在保持性能的同时，降低了计算开销。

## 🎯 应用场景

AGD可应用于各种需要可靠和可控文本生成的场景，例如：智能客服、内容创作、机器翻译、代码生成等。通过引导LLM使用特定的知识来源或遵循特定的指令，可以提高生成文本的准确性和可靠性。此外，AGD的可解释性使其更容易调试和优化LLM的行为，从而提高用户信任度。

## 📄 摘要（原文）

> The capacity of Large Language Models (LLMs) to follow complex instructions and generate factually accurate text is critical for their real-world application. However, standard decoding methods often fail to robustly satisfy these requirements, while existing control techniques frequently degrade general output quality. In this work, we introduce Attribution-Guided Decoding (AGD), an interpretability-based decoding strategy. Instead of directly manipulating model activations, AGD considers a set of high-probability output token candidates and selects the one that exhibits the highest attribution to a user-defined Region of Interest (ROI). This ROI can be flexibly defined over different parts of the model's input or internal components, allowing AGD to steer generation towards various desirable behaviors. We demonstrate AGD's efficacy across three challenging domains. For instruction following, we show that AGD significantly boosts adherence (e.g., improving the overall success rate on Llama 3.1 from 66.0% to 79.1%). For knowledge-intensive tasks, we show that guiding generation towards usage of internal knowledge components or contextual sources can reduce hallucinations and improve factual accuracy in both closed-book and open-book settings. Furthermore, we propose an adaptive, entropy-based variant of AGD that mitigates quality degradation and reduces computational overhead by applying guidance only when the model is uncertain. Our work presents a versatile, more interpretable, and effective method for enhancing the reliability of modern LLMs.

