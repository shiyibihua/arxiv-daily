---
layout: default
title: Benchmarking Gaslighting Negation Attacks Against Reasoning Models
---

# Benchmarking Gaslighting Negation Attacks Against Reasoning Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09677" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09677v2</a>
  <a href="https://arxiv.org/pdf/2506.09677.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09677v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09677v2', 'Benchmarking Gaslighting Negation Attacks Against Reasoning Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bin Zhu, Hailong Yin, Jingjing Chen, Yu-Gang Jiang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-11 (更新: 2025-12-16)

---

## 💡 一句话要点

**提出GaslightingBench-R以评估推理模型对否定攻击的抵抗力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推理模型` `气体灯否定攻击` `鲁棒性评估` `对抗性攻击` `GaslightingBench-R` `自然语言处理` `智能助手`

## 📋 核心要点

1. 现有推理模型在面对气体灯否定攻击时表现不佳，准确率显著下降，显示出其脆弱性。
2. 本文提出GaslightingBench-R基准，旨在评估推理模型在气体灯否定攻击下的防御能力。
3. 实验结果显示，使用GaslightingBench-R后，模型的准确率平均下降超过53%，揭示了模型的脆弱性。

## 📝 摘要（中文）

近年来，推理中心模型的进展通过链式思维提示和测试时缩放等机制承诺提高鲁棒性。然而，它们在面对气体灯否定攻击时的表现仍未得到充分探索。本文系统评估了三种最先进的推理模型，发现其在气体灯否定攻击后准确率显著下降（平均下降25-29%），表明即使是顶尖模型也难以在操控性用户反馈下保持正确答案。为进一步探讨这一脆弱性，我们引入了GaslightingBench-R，一个新诊断基准，专门设计用于评估推理模型在气体灯否定攻击下的防御能力。该基准通过筛选和整理1,025个具有挑战性的样本，导致准确率平均下降超过53%。我们的发现突显了逐步推理与抵抗对抗性操控之间的根本差距，呼吁开发新的鲁棒性策略以保护推理模型。

## 🔬 方法详解

**问题定义**：本文旨在解决推理模型在气体灯否定攻击下的脆弱性，现有方法未能有效应对这种对抗性操控，导致准确率显著下降。

**核心思路**：论文通过引入GaslightingBench-R基准，系统评估推理模型在气体灯否定攻击下的表现，旨在揭示模型的防御能力不足。

**技术框架**：研究首先对三种最先进的推理模型进行评估，随后构建GaslightingBench-R基准，包含1,025个经过筛选的样本，最后分析模型在该基准下的表现。

**关键创新**：GaslightingBench-R是一个新颖的诊断基准，专门设计用于评估推理模型在气体灯否定攻击下的脆弱性，与现有基准相比，能够更有效地揭示模型的不足。

**关键设计**：在构建GaslightingBench-R时，研究者对样本进行了严格筛选，确保其挑战性和代表性，从而引发更显著的准确率下降。

## 📊 实验亮点

实验结果显示，在气体灯否定攻击下，三种推理模型的准确率平均下降25-29%。使用GaslightingBench-R基准后，模型的准确率平均下降超过53%，揭示了模型在对抗性操控下的脆弱性，强调了开发新鲁棒性策略的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能助手等，能够帮助开发更鲁棒的推理模型，抵御对抗性攻击，提升用户体验和系统安全性。未来，研究成果可能推动相关领域的技术进步，促进更安全的人工智能应用。

## 📄 摘要（原文）

> Recent advances in reasoning-centric models promise improved robustness through mechanisms such as chain-of-thought prompting and test-time scaling. However, their ability to withstand gaslighting negation attacks-adversarial prompts that confidently deny correct answers-remains underexplored. In this paper, we conduct a systematic evaluation of three state-of-the-art reasoning models, i.e., OpenAI's o4-mini, Claude-3.7-Sonnet and Gemini-2.5-Flash, across three multimodal benchmarks: MMMU, MathVista, and CharXiv. Our evaluation reveals significant accuracy drops (25-29% on average) following gaslighting negation attacks, indicating that even top-tier reasoning models struggle to preserve correct answers under manipulative user feedback. Built upon the insights of the evaluation and to further probe this vulnerability, we introduce GaslightingBench-R, a new diagnostic benchmark specifically designed to evaluate reasoning models' susceptibility to defend their belief under gaslighting negation attacks. Constructed by filtering and curating 1,025 challenging samples from the existing benchmarks, GaslightingBench-R induces even more dramatic failures, with accuracy drops exceeding 53% on average. Our findings highlight a fundamental gap between step-by-step reasoning and resistance to adversarial manipulation, calling for new robustness strategies that safeguard reasoning models against gaslighting negation attacks.

