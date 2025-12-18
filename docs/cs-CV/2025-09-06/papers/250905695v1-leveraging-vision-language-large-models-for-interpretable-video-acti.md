---
layout: default
title: Leveraging Vision-Language Large Models for Interpretable Video Action Recognition with Semantic Tokenization
---

# Leveraging Vision-Language Large Models for Interpretable Video Action Recognition with Semantic Tokenization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05695" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05695v1</a>
  <a href="https://arxiv.org/pdf/2509.05695.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05695v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05695v1', 'Leveraging Vision-Language Large Models for Interpretable Video Action Recognition with Semantic Tokenization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingwei Peng, Zhixuan Qiu, Boyu Jin, Surasakdi Siripong

**分类**: cs.CV

**发布日期**: 2025-09-06

---

## 💡 一句话要点

**LVLM-VAR：利用视觉-语言大模型和语义标记实现可解释的视频行为识别**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频行为识别` `视觉-语言大模型` `语义标记` `可解释性` `动作叙述`

## 📋 核心要点

1. 传统行为识别方法在处理深层语义理解、复杂上下文信息和细粒度区分方面存在局限性。
2. LVLM-VAR通过VST模块将视频转换为语义动作标记，并利用LVLM进行动作分类和语义推理。
3. 实验表明，LVLM-VAR在多个基准测试中取得了显著的性能提升，并提高了模型的可解释性。

## 📝 摘要（中文）

本文提出LVLM-VAR，一种新颖的框架，旨在将预训练的视觉-语言大模型(LVLM)应用于视频行为识别，从而增强准确性和可解释性。该方法的核心是视频到语义标记(VST)模块，它创新性地将原始视频序列转换为离散的、语义和时间上一致的“语义动作标记”，有效地构建了LVLM可理解的“动作叙述”。这些标记与自然语言指令结合，然后由LoRA微调的LVLM（例如LLaVA-13B）处理，以实现鲁棒的动作分类和语义推理。LVLM-VAR在NTU RGB+D和NTU RGB+D 120等具有挑战性的基准测试中取得了最先进或极具竞争力的性能，例如在NTU RGB+D X-Sub上达到94.1%，在NTU RGB+D 120 X-Set上达到90.0%，并且通过生成自然语言解释，显著提高了模型的可解释性。

## 🔬 方法详解

**问题定义**：现有的视频行为识别方法难以捕捉视频中的深层语义信息，对复杂上下文的理解不足，并且在细粒度动作区分方面表现不佳。这些局限性导致模型在处理多样化的视频数据时泛化能力较弱。

**核心思路**：本文的核心思路是将视频转换为一系列具有语义信息的离散标记（semantic tokens），然后利用预训练的视觉-语言大模型（LVLM）理解这些标记，从而实现更准确和可解释的视频行为识别。这种方法借鉴了自然语言处理中利用语言模型理解文本序列的思想，将视频理解问题转化为语言理解问题。

**技术框架**：LVLM-VAR框架主要包含两个模块：视频到语义标记(VST)模块和LoRA微调的LVLM。VST模块负责将原始视频序列转换为语义动作标记。这些标记与自然语言指令一起输入到LoRA微调的LVLM（例如LLaVA-13B）中，LVLM负责进行动作分类和生成自然语言解释。

**关键创新**：该方法最重要的创新点在于提出了视频到语义标记(VST)模块，它能够将原始视频序列转换为离散的、语义和时间上一致的“语义动作标记”。与直接将视频帧输入到模型中相比，这种方法能够更好地提取视频中的关键信息，并将其表示为LVLM可以理解的形式。

**关键设计**：VST模块的具体实现细节未知，论文中可能没有详细描述。LoRA微调的LVLM使用了LLaVA-13B模型，并采用LoRA（Low-Rank Adaptation）技术进行微调，以减少计算成本和提高训练效率。具体的损失函数和网络结构细节未知。

## 📊 实验亮点

LVLM-VAR在NTU RGB+D X-Sub数据集上取得了94.1%的准确率，在NTU RGB+D 120 X-Set数据集上取得了90.0%的准确率，显著优于现有方法。此外，该方法还能够生成自然语言解释，提高了模型的可解释性，为用户提供了更直观的理解。

## 🎯 应用场景

LVLM-VAR在视频监控、智能安防、人机交互、自动驾驶等领域具有广泛的应用前景。该方法能够提高视频行为识别的准确性和可解释性，有助于提升相关系统的智能化水平。未来，该方法还可以应用于更复杂的视频理解任务，例如视频摘要、视频问答等。

## 📄 摘要（原文）

> Human action recognition often struggles with deep semantic understanding, complex contextual information, and fine-grained distinction, limitations that traditional methods frequently encounter when dealing with diverse video data. Inspired by the remarkable capabilities of large language models, this paper introduces LVLM-VAR, a novel framework that pioneers the application of pre-trained Vision-Language Large Models (LVLMs) to video action recognition, emphasizing enhanced accuracy and interpretability. Our method features a Video-to-Semantic-Tokens (VST) Module, which innovatively transforms raw video sequences into discrete, semantically and temporally consistent "semantic action tokens," effectively crafting an "action narrative" that is comprehensible to an LVLM. These tokens, combined with natural language instructions, are then processed by a LoRA-fine-tuned LVLM (e.g., LLaVA-13B) for robust action classification and semantic reasoning. LVLM-VAR not only achieves state-of-the-art or highly competitive performance on challenging benchmarks such as NTU RGB+D and NTU RGB+D 120, demonstrating significant improvements (e.g., 94.1% on NTU RGB+D X-Sub and 90.0% on NTU RGB+D 120 X-Set), but also substantially boosts model interpretability by generating natural language explanations for its predictions.

