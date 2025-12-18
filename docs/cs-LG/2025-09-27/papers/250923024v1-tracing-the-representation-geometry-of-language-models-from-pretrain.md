---
layout: default
title: Tracing the Representation Geometry of Language Models from Pretraining to Post-training
---

# Tracing the Representation Geometry of Language Models from Pretraining to Post-training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23024" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23024v1</a>
  <a href="https://arxiv.org/pdf/2509.23024.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23024v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23024v1', 'Tracing the Representation Geometry of Language Models from Pretraining to Post-training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Melody Zixuan Li, Kumar Krishna Agrawal, Arna Ghosh, Komal Kumar Teru, Adam Santoro, Guillaume Lajoie, Blake A. Richards

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-09-27

**备注**: 33 pages, 14 figures, 9 tables

---

## 💡 一句话要点

**提出几何表示追踪方法以揭示语言模型的复杂能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `几何表示` `预训练` `后训练` `谱方法` `有效秩` `特征谱衰减` `任务性能`

## 📋 核心要点

1. 现有的训练指标如损失函数无法有效解释大型语言模型中复杂能力的出现，导致对模型行为的理解不足。
2. 本文提出了一种谱方法，通过有效秩和特征谱衰减来研究语言模型在预训练和后训练中的表示几何变化。
3. 实验结果表明，模型在自回归预训练过程中经历了三个几何阶段，且后训练进一步影响了模型的几何特性和任务性能。

## 📝 摘要（中文）

标准训练指标如损失无法解释大型语言模型中复杂能力的出现。本文采用谱方法研究预训练和后训练中学习表示的几何特性，测量有效秩（RankMe）和特征谱衰减（$α$-ReQ）。通过对OLMo和Pythia模型的分析，发现自回归预训练过程中存在三个几何阶段：初始的“热身”阶段表现出快速的表示崩溃，接着是“寻求熵”阶段，流形的维度显著扩展，最后是“寻求压缩”阶段，选择性保留主特征方向的方差。后训练进一步改变几何特性，SFT和DPO驱动“寻求熵”动态，而RLVR则增强奖励对齐但降低生成多样性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有训练指标无法解释大型语言模型复杂能力的问题，尤其是在预训练和后训练阶段的几何表示变化。

**核心思路**：通过引入谱方法，测量有效秩和特征谱衰减，分析语言模型在不同训练阶段的几何特性，以揭示其能力的演变过程。

**技术框架**：研究分为预训练和后训练两个主要阶段。在预训练阶段，模型经历“热身”、“寻求熵”和“寻求压缩”三个几何阶段；在后训练阶段，SFT、DPO和RLVR等方法进一步影响几何特性。

**关键创新**：提出了基于有效秩和特征谱衰减的几何表示追踪方法，揭示了语言模型在训练过程中的非单调几何变化，与传统方法相比，提供了更深层次的理解。

**关键设计**：在实验中，使用了OLMo和Pythia模型，重点关注不同训练阶段的表示变化，特别是维度扩展和方差选择性保留的机制。

## 📊 实验亮点

实验结果显示，在自回归预训练过程中，模型经历了三个几何阶段，特别是在“寻求压缩”阶段，模型在下游任务上的性能显著提升，表现出更好的方差选择性。后训练阶段的SFT和DPO方法使得模型在特定数据集上的表现得到改善，但在分布外的鲁棒性上有所下降。

## 🎯 应用场景

该研究为理解大型语言模型的训练过程提供了新的视角，能够帮助研究人员优化模型设计和训练策略，提升模型在特定任务上的性能。未来，该方法可应用于多种自然语言处理任务，推动智能对话系统、文本生成等领域的发展。

## 📄 摘要（原文）

> Standard training metrics like loss fail to explain the emergence of complex capabilities in large language models. We take a spectral approach to investigate the geometry of learned representations across pretraining and post-training, measuring effective rank (RankMe) and eigenspectrum decay ($α$-ReQ). With OLMo (1B-7B) and Pythia (160M-12B) models, we uncover a consistent non-monotonic sequence of three geometric phases during autoregressive pretraining. The initial "warmup" phase exhibits rapid representational collapse. This is followed by an "entropy-seeking" phase, where the manifold's dimensionality expands substantially, coinciding with peak n-gram memorization. Subsequently, a "compression-seeking" phase imposes anisotropic consolidation, selectively preserving variance along dominant eigendirections while contracting others, a transition marked with significant improvement in downstream task performance. We show these phases can emerge from a fundamental interplay of cross-entropy optimization under skewed token frequencies and representational bottlenecks ($d \ll \|V\|$). Post-training further transforms geometry: SFT and DPO drive "entropy-seeking" dynamics to integrate specific instructional or preferential data, improving in-distribution performance while degrading out-of-distribution robustness. Conversely, RLVR induces "compression-seeking", enhancing reward alignment but reducing generation diversity.

