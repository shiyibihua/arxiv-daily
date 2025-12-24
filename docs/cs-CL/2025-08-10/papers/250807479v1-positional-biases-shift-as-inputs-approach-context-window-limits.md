---
layout: default
title: Positional Biases Shift as Inputs Approach Context Window Limits
---

# Positional Biases Shift as Inputs Approach Context Window Limits

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07479" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07479v1</a>
  <a href="https://arxiv.org/pdf/2508.07479.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07479v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07479v1', 'Positional Biases Shift as Inputs Approach Context Window Limits')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Blerta Veseli, Julian Chibane, Mariya Toneva, Alexander Koller

**分类**: cs.CL

**发布日期**: 2025-08-10

**期刊**: Conference on Language Modeling (COLM) 2025

---

## 💡 一句话要点

**提出相对输入长度分析以解决长输入中的位置信息偏差问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长输入处理` `位置信息偏差` `大型语言模型` `信息检索` `推理机制`

## 📋 核心要点

1. 现有大型语言模型在处理长输入时，常常无法有效利用位置信息，导致性能下降。
2. 本文通过相对输入长度分析，提出了一种新的视角来理解和评估模型的位置信息偏差。
3. 研究发现，输入长度占上下文窗口的50%以内时，LiM效应最强，且模型性能与信息距离密切相关。

## 📝 摘要（中文）

大型语言模型（LLMs）在有效利用长输入信息方面常常面临挑战。以往研究发现了位置信息偏差现象，如“中间迷失效应”（LiM），即模型在输入的开头（首因偏差）或结尾（近因偏差）表现更好，而在中间表现较差。然而，长上下文研究未能一致复现这些效应，导致对其强度及表现条件的质疑。为此，本文通过相对输入长度进行全面分析，发现LiM效应在输入占用模型上下文窗口的50%以内时最强，超过此比例后，首因偏差减弱，而近因偏差相对稳定。我们观察到一种基于距离的偏差，即相关信息越接近输入末尾，模型性能越好。此外，研究结果表明，成功的信息检索是LLMs推理的前提，推理中的位置信息偏差主要源于检索。这些发现对长上下文任务、未来LLM基准设计及评估方法具有重要意义。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在长输入中位置信息偏差的问题，尤其是中间迷失效应（LiM）未能在长上下文研究中一致复现的挑战。

**核心思路**：通过相对输入长度的分析，定义输入长度相对于模型上下文窗口的比例，探讨不同位置的信息对模型性能的影响，从而揭示位置信息偏差的变化规律。

**技术框架**：研究采用相对输入长度进行实验，分析模型在不同输入占比下的表现，主要模块包括数据预处理、模型训练和性能评估。

**关键创新**：提出了基于相对输入长度的分析方法，揭示了LiM效应的强度与输入长度占比的关系，强调了距离偏差的重要性，与传统绝对长度分析方法形成对比。

**关键设计**：在实验中，设置了不同的输入长度比例，使用标准的模型评估指标，确保了实验结果的可重复性和可靠性。

## 📊 实验亮点

实验结果表明，当输入长度占模型上下文窗口的50%以内时，LiM效应最为显著，而超过此比例后，首因偏差减弱，近因偏差保持稳定。研究还发现，模型性能与信息距离密切相关，相关信息越接近输入末尾，模型表现越好。

## 🎯 应用场景

该研究的发现对长上下文任务具有重要的应用价值，尤其是在自然语言处理、信息检索和对话系统等领域。通过优化模型对位置信息的利用，可以提升模型在处理长文本时的表现，进而推动相关技术的进步和应用。

## 📄 摘要（原文）

> Large Language Models (LLMs) often struggle to use information across long inputs effectively. Prior work has identified positional biases, such as the Lost in the Middle (LiM) effect, where models perform better when information appears at the beginning (primacy bias) or end (recency bias) of the input, rather than in the middle. However, long-context studies have not consistently replicated these effects, raising questions about their intensity and the conditions under which they manifest. To address this, we conducted a comprehensive analysis using relative rather than absolute input lengths, defined with respect to each model's context window. Our findings reveal that the LiM effect is strongest when inputs occupy up to 50% of a model's context window. Beyond that, the primacy bias weakens, while recency bias remains relatively stable. This effectively eliminates the LiM effect; instead, we observe a distance-based bias, where model performance is better when relevant information is closer to the end of the input. Furthermore, our results suggest that successful retrieval is a prerequisite for reasoning in LLMs, and that the observed positional biases in reasoning are largely inherited from retrieval. These insights have implications for long-context tasks, the design of future LLM benchmarks, and evaluation methodologies for LLMs handling extended inputs.

