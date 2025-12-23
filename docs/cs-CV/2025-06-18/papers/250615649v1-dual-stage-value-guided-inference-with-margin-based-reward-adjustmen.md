---
layout: default
title: Dual-Stage Value-Guided Inference with Margin-Based Reward Adjustment for Fast and Faithful VLM Captioning
---

# Dual-Stage Value-Guided Inference with Margin-Based Reward Adjustment for Fast and Faithful VLM Captioning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15649" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15649v1</a>
  <a href="https://arxiv.org/pdf/2506.15649.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15649v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15649v1', 'Dual-Stage Value-Guided Inference with Margin-Based Reward Adjustment for Fast and Faithful VLM Captioning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ankan Deria, Adinath Madhavrao Dukre, Feilong Tang, Sara Atito, Sudipta Roy, Muhammad Awais, Muhammad Haris Khan, Imran Razzak

**分类**: cs.CV, cs.LG

**发布日期**: 2025-06-18

---

## 💡 一句话要点

**提出ViMaR以解决视觉语言模型生成低置信度问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `推理优化` `奖励调整` `多模态学习` `自动描述生成`

## 📋 核心要点

1. 现有视觉语言模型在推理时计算开销大，且容易生成低置信度的描述，导致信息不准确。
2. ViMaR通过双阶段推理框架，结合价值模型与边际奖励调整，提升生成效率与描述质量。
3. 实验结果显示，ViMaR在多个VLM架构上生成的描述更可靠、准确，且速度提升超过4倍。

## 📝 摘要（中文）

尽管视觉语言模型（VLM）在推理时间搜索方面取得了显著进展，但现有方法仍然计算开销大且容易产生低置信度的生成，导致持续的幻觉现象。本文提出了双阶段的价值引导推理框架ViMaR，通过结合时间差分价值模型与基于边际的奖励调整，提高了效率和输出的真实性。在第一阶段，识别出多样候选中最高价值的描述；在第二阶段，仅对被忽视或视觉基础薄弱的片段进行选择性细化。大量实验表明，ViMaR生成的描述在可靠性、准确性和细节上显著优于现有方法，同时速度提升超过4倍。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉语言模型在推理过程中计算开销大和低置信度生成的问题，导致生成的描述常常不准确或缺乏信息量。

**核心思路**：ViMaR的核心思路是通过双阶段推理框架，首先识别出最高价值的描述，然后对被忽视或基础薄弱的片段进行细化，从而提高生成的描述质量和效率。

**技术框架**：ViMaR的整体架构分为两个主要阶段：第一阶段进行单次推理以识别最高价值的描述，第二阶段则对特定的片段进行选择性细化。

**关键创新**：ViMaR的关键创新在于引入了基于边际的奖励调整机制，能够有效抑制低置信度的生成，同时保持描述的丰富性，这与现有方法的设计有本质区别。

**关键设计**：在设计中，ViMaR采用了时间差分价值模型，并设置了经过校准的边际惩罚，以鼓励高置信度的生成，确保生成的描述在准确性和信息量上都有所提升。

## 📊 实验亮点

实验结果表明，ViMaR生成的描述在可靠性、准确性和细节上显著优于现有方法，速度提升超过4倍。此外，ViMaR在不同模型间的迁移能力也得到了验证，显示出其灵活性和模块化特性。

## 🎯 应用场景

该研究的潜在应用领域包括自动图像描述生成、视频理解和人机交互等。通过提高视觉语言模型的生成质量和效率，ViMaR能够为多模态学习和智能系统提供更强大的支持，推动相关技术的实际应用和发展。

## 📄 摘要（原文）

> Despite significant advances in inference-time search for vision-language models (VLMs), existing approaches remain both computationally expensive and prone to unpenalized, low-confidence generations which often lead to persistent hallucinations. We introduce \textbf{Value-guided Inference with Margin-based Reward (ViMaR)}, a two-stage inference framework that improves both efficiency and output fidelity by combining a temporal-difference value model with a margin-aware reward adjustment. In the first stage, we perform a single pass to identify the highest-value caption among diverse candidates. In the second stage, we selectively refine only those segments that were overlooked or exhibit weak visual grounding, thereby eliminating frequently rewarded evaluations. A calibrated margin-based penalty discourages low-confidence continuations while preserving descriptive richness. Extensive experiments across multiple VLM architectures demonstrate that ViMaR generates captions that are significantly more reliable, factually accurate, detailed, and explanatory, while achieving over 4$\times$ speedup compared to existing value-guided methods. Specifically, we show that ViMaR trained solely on LLaVA Mistral-7B, \textit{generalizes effectively to guide decoding in a stronger unseen model}. To further validate this, we adapt the ViMaR to steer generation in LLaVA-OneVision-Qwen2-7B, leading to consistent improvements in caption quality and demonstrating robust cross-model guidance. This cross-model generalization highlights ViMaR's flexibility and modularity, positioning it as a scalable and transferable inference-time decoding strategy. Furthermore, when ViMaR-generated captions are used for self-training, the underlying models achieve substantial gains across a broad suite of visual comprehension benchmarks, underscoring the potential of fast, accurate, and self-improving VLM pipelines.

