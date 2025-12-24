---
layout: default
title: Prompt-Based One-Shot Exact Length-Controlled Generation with LLMs
---

# Prompt-Based One-Shot Exact Length-Controlled Generation with LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13805" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13805v1</a>
  <a href="https://arxiv.org/pdf/2508.13805.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13805v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13805v1', 'Prompt-Based One-Shot Exact Length-Controlled Generation with LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Juncheng Xie, Hung-yi Lee

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-19

**备注**: 18 pages

---

## 💡 一句话要点

**提出基于提示的一次性精确长度控制生成方法以解决LLMs文本生成问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `文本生成` `长度控制` `提示工程` `自然语言处理`

## 📋 核心要点

1. 现有方法在控制生成文本长度方面存在不足，模型常常无法准确遵循长度指令，导致生成结果不符合预期。
2. 论文提出了一种基于提示的策略，通过附加倒计时标记和计数规则，使模型在生成文本时能够精确控制生成长度。
3. 实验结果显示，使用倒计时提示后，GPT-4.1在严格长度合规性上显著提升，达到了95%以上，且保持了生成文本的质量。

## 📝 摘要（中文）

控制大型语言模型（LLMs）生成文本的长度仍然具有挑战性：模型常常无法准确遵循长度指令，导致生成的文本超出或不足预期长度。本文提出了一种基于提示的一次性策略，强制现成的LLM生成确切数量的标记（英文单词或中文字符），无需任何微调或迭代采样。该提示附加了倒计时标记和明确的计数规则，使模型在生成文本的同时进行计数。我们在四个设置上进行了评估：开放式生成（1-1000个标记）、XSUM摘要、MT-Bench-LI指令跟随和LIFEBENCH等长轨道。在MT-Bench-LI上，使用倒计时提示后，GPT-4.1的严格长度合规性从30%以下跃升至95%以上，超越了流行的草拟-再修订基线，同时保持了答案质量。这些结果表明，通过提示工程可以实现精确的长度控制，为训练或解码方法提供了一种轻量级替代方案。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在生成文本时无法准确控制长度的问题。现有方法常常导致生成文本超出或不足预期长度，缺乏有效的内部计数机制。

**核心思路**：论文的核心思路是通过设计特定的提示，强制模型在生成文本的同时进行计数，从而实现精确的长度控制。这种方法不需要对模型进行微调或复杂的迭代采样。

**技术框架**：整体架构包括生成提示的设计和模型的调用。提示中包含倒计时标记和明确的计数规则，模型在生成过程中遵循这些规则进行文本生成。

**关键创新**：最重要的技术创新点在于通过提示工程实现精确的长度控制，这与现有的训练或解码方法有本质区别，提供了一种轻量级的解决方案。

**关键设计**：提示设计中包含倒计时标记和计数规则，这些设计使得模型能够在生成过程中实时进行长度计数，从而确保生成文本的长度符合预期。

## 📊 实验亮点

实验结果显示，使用倒计时提示后，GPT-4.1在MT-Bench-LI上的严格长度合规性从30%以下提升至95%以上，显著超越了传统的草拟-再修订基线，同时保持了生成文本的质量，展示了提示工程的有效性。

## 🎯 应用场景

该研究的潜在应用场景包括自动文本生成、摘要生成和指令遵循等领域。通过精确控制生成文本的长度，可以提高生成内容的质量和可用性，满足特定应用需求，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Controlling the length of text produced by large language models (LLMs) remains challenging: models frequently overshoot or undershoot explicit length instructions because they cannot reliably keep an internal token count. We present a prompt-based, one-shot strategy that compels an off-the-shelf LLM to generate exactly a desired number of tokens - words (English) or characters (Chinese) - without any fine-tuning or iterative sampling. The prompt appends countdown markers and explicit counting rules so that the model "writes while counting." We evaluate on four settings: open-ended generation (1-1000 tokens), XSUM summarization, MT-Bench-LI instruction following, and the LIFEBENCH equal-length track. On MT-Bench-LI, strict length compliance with GPT-4.1 leaps from below 30% under naive prompts to above 95% with our countdown prompt, surpassing the popular draft-then-revise baseline, while judged answer quality is preserved. These results show that precise length control can be achieved through prompt engineering alone, offering a lightweight alternative to training- or decoding-based methods.

