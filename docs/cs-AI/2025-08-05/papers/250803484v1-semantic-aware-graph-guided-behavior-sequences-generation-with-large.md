---
layout: default
title: Semantic-aware Graph-guided Behavior Sequences Generation with Large Language Models for Smart Homes
---

# Semantic-aware Graph-guided Behavior Sequences Generation with Large Language Models for Smart Homes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03484" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03484v1</a>
  <a href="https://arxiv.org/pdf/2508.03484.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03484v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03484v1', 'Semantic-aware Graph-guided Behavior Sequences Generation with Large Language Models for Smart Homes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiyao Xu, Dan Zhao, Qingsong Zou, Qing Li, Yong Jiang, Yuhang Wang, Jingyu Xiao

**分类**: cs.AI

**发布日期**: 2025-08-05

**🔗 代码/项目**: [GITHUB](https://github.com/horizonsinzqs/SmartGen)

---

## 💡 一句话要点

**提出SmartGen以解决智能家居行为数据生成问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `智能家居` `行为预测` `异常检测` `大型语言模型` `数据合成` `图引导生成` `持续适应`

## 📋 核心要点

1. 现有智能家居模型在静态数据集上训练，容易受到行为漂移的影响，导致性能下降。
2. SmartGen通过合成上下文感知的用户行为数据，支持智能家居模型的持续适应，提升模型的鲁棒性。
3. 在三个真实世界数据集上的实验表明，SmartGen在异常检测和行为预测任务上分别提升了85.43%和70.51%的性能。

## 📝 摘要（中文）

随着智能家居的普及，智能模型在异常检测和行为预测等任务中得到广泛应用。然而，这些模型通常在静态数据集上训练，容易受到季节变化、生活方式转变或日常习惯演变导致的行为漂移影响。收集新行为数据进行再训练往往不切实际，因其速度慢、成本高且涉及隐私问题。本文提出了SmartGen，一个基于大型语言模型的框架，合成上下文感知的用户行为数据，以支持下游智能家居模型的持续适应。SmartGen由四个关键组件组成，实验结果表明其在异常检测和行为预测任务中的表现显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决智能家居模型在行为漂移情况下的性能下降问题。现有方法依赖静态数据集，难以适应用户行为的动态变化。

**核心思路**：SmartGen框架通过合成上下文感知的用户行为数据，利用大型语言模型生成适应性强的行为序列，从而提升模型的鲁棒性和准确性。

**技术框架**：SmartGen包括四个主要模块：时间和语义感知分割模块、语义感知序列压缩、图引导序列合成和双阶段异常值过滤器。这些模块协同工作，确保生成的数据既符合上下文变化，又保留核心行为模式。

**关键创新**：最重要的创新在于引入图引导序列合成，通过构建行为关系图并编码频繁转移，指导大型语言模型生成符合上下文的行为数据。这一方法显著提高了生成序列的语义一致性和行为有效性。

**关键设计**：在设计中，时间和语义感知分割模块通过双时间跨度约束实现对长序列的合理分割；语义感知序列压缩通过聚类行为映射来减少输入长度；双阶段异常值过滤器则用于识别和去除不合理或语义不一致的输出。整体设计注重生成数据的质量和实用性。

## 📊 实验亮点

实验结果显示，SmartGen在三个真实世界数据集上的异常检测性能提升了85.43%，行为预测性能提升了70.51%。这些显著的提升表明，SmartGen能够有效应对行为漂移带来的挑战，增强智能家居模型的适应性和准确性。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居系统、智能监控和个性化服务等。通过合成用户行为数据，SmartGen能够帮助智能家居模型更好地适应用户的动态需求，提升用户体验和系统的智能化水平。未来，该技术有望在更广泛的智能环境中得到应用，推动智能家居的进一步发展。

## 📄 摘要（原文）

> As smart homes become increasingly prevalent, intelligent models are widely used for tasks such as anomaly detection and behavior prediction. These models are typically trained on static datasets, making them brittle to behavioral drift caused by seasonal changes, lifestyle shifts, or evolving routines. However, collecting new behavior data for retraining is often impractical due to its slow pace, high cost, and privacy concerns. In this paper, we propose SmartGen, an LLM-based framework that synthesizes context-aware user behavior data to support continual adaptation of downstream smart home models. SmartGen consists of four key components. First, we design a Time and Semantic-aware Split module to divide long behavior sequences into manageable, semantically coherent subsequences under dual time-span constraints. Second, we propose Semantic-aware Sequence Compression to reduce input length while preserving representative semantics by clustering behavior mapping in latent space. Third, we introduce Graph-guided Sequence Synthesis, which constructs a behavior relationship graph and encodes frequent transitions into prompts, guiding the LLM to generate data aligned with contextual changes while retaining core behavior patterns. Finally, we design a Two-stage Outlier Filter to identify and remove implausible or semantically inconsistent outputs, aiming to improve the factual coherence and behavioral validity of the generated sequences. Experiments on three real-world datasets demonstrate that SmartGen significantly enhances model performance on anomaly detection and behavior prediction tasks under behavioral drift, with anomaly detection improving by 85.43% and behavior prediction by 70.51% on average. The code is available at https://github.com/horizonsinzqs/SmartGen.

