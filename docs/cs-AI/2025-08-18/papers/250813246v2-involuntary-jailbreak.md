---
layout: default
title: Involuntary Jailbreak
---

# Involuntary Jailbreak

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13246" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13246v2</a>
  <a href="https://arxiv.org/pdf/2508.13246.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13246v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13246v2', 'Involuntary Jailbreak')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yangyang Guo, Yangyan Li, Mohan Kankanhalli

**分类**: cs.CR, cs.AI

**发布日期**: 2025-08-18 (更新: 2025-11-30)

---

## 💡 一句话要点

**揭示大型语言模型的新型脆弱性：非自愿越狱**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `安全性评估` `越狱攻击` `防护机制` `人工智能安全`

## 📋 核心要点

1. 现有的越狱攻击主要集中在LLM的局部防护组件，未能有效评估整体防护结构的脆弱性。
2. 本研究提出了一种简单的通用提示策略，能够引导LLMs生成通常被拒绝的问题及其详细回答，从而实现越狱。
3. 实验结果表明，该方法能有效越狱大多数主流LLMs，显示出其在安全性评估中的重要性。

## 📝 摘要（中文）

本研究揭示了大型语言模型（LLMs）中的一种新型脆弱性，称为“非自愿越狱”。与现有的越狱攻击不同，该脆弱性并不针对特定的攻击目标，例如生成制造炸弹的指令。以往的攻击方法主要集中在LLM防护机制的局部组件上，而非自愿越狱可能会危及整个防护结构。我们仅使用一个通用提示即可实现这一目标，指示LLMs生成通常会被拒绝的问题及其深入回答。令人惊讶的是，这一简单的提示策略在大多数领先的LLMs中都能有效越狱，包括Claude Opus 4.1、Grok 4、Gemini 2.5 Pro和GPT 4.1。我们希望这一问题能促使研究人员和从业者重新评估LLM防护机制的稳健性，并为未来的安全对齐做出贡献。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型（LLMs）中存在的脆弱性，尤其是现有越狱攻击方法未能全面评估防护机制的整体稳健性。

**核心思路**：提出了一种通用提示策略，利用该策略引导LLMs生成通常会被拒绝的问题及其深入回答，从而实现对防护机制的突破。

**技术框架**：整体流程包括输入一个通用提示，LLMs根据该提示生成问题和回答，进而评估防护机制的有效性。主要模块包括提示生成、问题识别和回答生成。

**关键创新**：最重要的创新在于通过单一提示实现对整个防护结构的越狱，而非仅针对局部组件，这一方法显示了现有防护机制的脆弱性。

**关键设计**：在参数设置上，使用了通用提示的设计，确保能够引导LLMs生成拒绝的问题，且在损失函数上未做特别调整，主要依赖于模型本身的生成能力。

## 📊 实验亮点

实验结果显示，该通用提示策略能够在大多数主流LLMs中成功实现越狱，包括Claude Opus 4.1、Grok 4、Gemini 2.5 Pro和GPT 4.1，表明其在安全性评估中的有效性和重要性。

## 🎯 应用场景

该研究的潜在应用领域包括安全性评估、模型训练和防护机制设计等。通过揭示LLMs的脆弱性，研究者可以更好地理解和改进模型的安全性，从而在未来的应用中提升人工智能系统的可靠性和安全性。

## 📄 摘要（原文）

> In this study, we disclose a worrying new vulnerability in Large Language Models (LLMs), which we term \textbf{involuntary jailbreak}. Unlike existing jailbreak attacks, this weakness is distinct in that it does not involve a specific attack objective, such as generating instructions for \textit{building a bomb}. Prior attack methods predominantly target localized components of the LLM guardrail. In contrast, involuntary jailbreaks may potentially compromise the entire guardrail structure, which our method reveals to be surprisingly fragile. We merely employ a single universal prompt to achieve this goal. In particular, we instruct LLMs to generate several questions that would typically be rejected, along with their corresponding in-depth responses (rather than a refusal). Remarkably, this simple prompt strategy consistently jailbreaks the majority of leading LLMs, including Claude Opus 4.1, Grok 4, Gemini 2.5 Pro, and GPT 4.1. We hope this problem can motivate researchers and practitioners to re-evaluate the robustness of LLM guardrails and contribute to stronger safety alignment in future.

