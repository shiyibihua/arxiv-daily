---
layout: default
title: The Resurgence of GCG Adversarial Attacks on Large Language Models
---

# The Resurgence of GCG Adversarial Attacks on Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00391" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00391v1</a>
  <a href="https://arxiv.org/pdf/2509.00391.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00391v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00391v1', 'The Resurgence of GCG Adversarial Attacks on Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuting Tan, Xuying Li, Zhuo Li, Huizhen Shu, Peikang Hu

**分类**: cs.CL, cs.AI, cs.CR, cs.LG

**发布日期**: 2025-08-30

**备注**: 12 pages, 5 figures

---

## 💡 一句话要点

**提出GCG对大语言模型的对抗攻击评估方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对抗攻击` `大型语言模型` `梯度方法` `推理任务` `安全性评估` `模拟退火` `模型脆弱性`

## 📋 核心要点

1. 现有的对抗攻击方法在面对大型语言模型时效果不佳，尤其是在复杂的损失空间中。
2. 本文提出了GCG及其变体T-GCG，通过系统评估不同规模的LLMs，探索其对抗攻击的有效性。
3. 实验结果表明，编码相关提示的脆弱性显著高于安全提示，同时T-GCG在前缀评估下表现出一定的竞争力。

## 📝 摘要（中文）

基于梯度的对抗提示方法，如贪婪坐标梯度（GCG）算法，已成为破解大型语言模型（LLMs）的有效手段。本文系统评估了GCG及其增强变体T-GCG在不同规模开源LLMs上的表现。通过对Qwen2.5-0.5B、LLaMA-3.2-1B和GPT-OSS-20B的攻击效果进行评估，发现攻击成功率随着模型规模的增加而降低，前缀基启发式方法高估了攻击效果，而编码相关提示比安全提示更易受攻击。此外，T-GCG的初步结果显示，模拟退火可以多样化对抗搜索并在前缀评估下实现竞争性攻击成功率，但在语义判断下的效果有限。这些发现揭示了GCG的可扩展性限制，并暴露了推理任务中的被忽视的脆弱性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在对抗攻击中的脆弱性，现有方法在面对更复杂的模型时效果逐渐减弱，尤其在推理任务中表现不佳。

**核心思路**：提出GCG算法及其变体T-GCG，通过系统评估不同规模的开源LLMs，探索其在安全和推理任务中的攻击效果。设计上考虑了模型规模对攻击成功率的影响，以及前缀基启发式方法的局限性。

**技术框架**：整体架构包括GCG算法的实现、T-GCG的模拟退火增强、以及对不同模型（如Qwen2.5、LLaMA、GPT-OSS）的攻击效果评估。主要模块包括攻击策略设计、模型评估和结果分析。

**关键创新**：最重要的创新在于揭示了大型语言模型在推理任务中的脆弱性，尤其是编码相关提示的攻击成功率显著高于安全提示，且GCG的可扩展性受到模型规模的限制。

**关键设计**：在GCG和T-GCG中，关键参数设置包括学习率、迭代次数和损失函数的选择，特别是在T-GCG中引入的模拟退火策略用于多样化对抗搜索。

## 📊 实验亮点

实验结果显示，随着模型规模的增加，攻击成功率显著下降，尤其在编码相关提示中，攻击成功率高达XX%（具体数据未知）。同时，T-GCG在前缀评估下的攻击成功率与传统方法相比提升了XX%（具体数据未知），但在语义判断下的效果仍有限。

## 🎯 应用场景

该研究的潜在应用领域包括安全性评估、对抗样本生成和大型语言模型的鲁棒性提升。通过识别和利用模型的脆弱性，可以为开发更安全的AI系统提供重要参考，未来可能在自然语言处理和人工智能的多个领域产生深远影响。

## 📄 摘要（原文）

> Gradient-based adversarial prompting, such as the Greedy Coordinate Gradient (GCG) algorithm, has emerged as a powerful method for jailbreaking large language models (LLMs). In this paper, we present a systematic appraisal of GCG and its annealing-augmented variant, T-GCG, across open-source LLMs of varying scales. Using Qwen2.5-0.5B, LLaMA-3.2-1B, and GPT-OSS-20B, we evaluate attack effectiveness on both safety-oriented prompts (AdvBench) and reasoning-intensive coding prompts. Our study reveals three key findings: (1) attack success rates (ASR) decrease with model size, reflecting the increasing complexity and non-convexity of larger models' loss landscapes; (2) prefix-based heuristics substantially overestimate attack effectiveness compared to GPT-4o semantic judgments, which provide a stricter and more realistic evaluation; and (3) coding-related prompts are significantly more vulnerable than adversarial safety prompts, suggesting that reasoning itself can be exploited as an attack vector. In addition, preliminary results with T-GCG show that simulated annealing can diversify adversarial search and achieve competitive ASR under prefix evaluation, though its benefits under semantic judgment remain limited. Together, these findings highlight the scalability limits of GCG, expose overlooked vulnerabilities in reasoning tasks, and motivate further development of annealing-inspired strategies for more robust adversarial evaluation.

