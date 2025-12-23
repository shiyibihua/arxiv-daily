---
layout: default
title: Towards Robust Multimodal Emotion Recognition under Missing Modalities and Distribution Shifts
---

# Towards Robust Multimodal Emotion Recognition under Missing Modalities and Distribution Shifts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10452" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10452v1</a>
  <a href="https://arxiv.org/pdf/2506.10452.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10452v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10452v1', 'Towards Robust Multimodal Emotion Recognition under Missing Modalities and Distribution Shifts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guowei Zhong, Ruohong Huan, Mingzhen Wu, Ronghua Liang, Peng Chen

**分类**: cs.CV, cs.CL, cs.LG, cs.MM

**发布日期**: 2025-06-12

**备注**: Submitted to TAC. The code is available at https://github.com/gw-zhong/CIDer

**🔗 代码/项目**: [GITHUB](https://github.com/gw-zhong/CIDer)

---

## 💡 一句话要点

**提出CIDer框架以解决多模态情感识别中的缺失模态和分布偏移问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态情感识别` `模态缺失` `分布偏移` `因果推断` `自蒸馏` `深度学习` `情感分析`

## 📋 核心要点

1. 现有的多模态情感识别方法在处理模态缺失和分布偏移时存在局限性，通常依赖特定模型或引入过多参数。
2. 本文提出CIDer框架，通过模型特定自蒸馏和模型无关因果推断模块，解决模态缺失和OOD问题。
3. 实验结果显示，CIDer在RMFM和OOD场景下表现优异，参数更少，训练速度更快，相较于现有方法有显著提升。

## 📝 摘要（中文）

近年来，多模态情感识别（MER）在处理模态缺失和分布偏移（OOD）数据方面面临挑战。现有方法通常依赖特定模型或引入过多参数，限制了其实用性。为了解决这些问题，本文提出了一种新颖的鲁棒MER框架CIDer，并引入了随机模态特征缺失（RMFM）这一新任务，以推广模态缺失的定义。CIDer集成了模型特定自蒸馏（MSSD）模块和模型无关因果推断（MACI）模块，前者通过权重共享自蒸馏方法增强了在RMFM任务下的鲁棒性，后者则利用因果图缓解标签和语言偏见。实验结果表明，CIDer在RMFM和OOD场景下均表现出色，参数更少，训练速度更快，且实现代码已公开。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态情感识别中模态缺失和分布偏移的问题。现有方法往往依赖特定模型，导致在处理缺失模态和OOD数据时的鲁棒性不足，且引入过多参数使得实际应用受限。

**核心思路**：CIDer框架通过引入随机模态特征缺失（RMFM）任务，推广模态缺失的定义，并结合模型特定自蒸馏（MSSD）和模型无关因果推断（MACI）模块，增强模型在不同场景下的鲁棒性。

**技术框架**：CIDer的整体架构包括MSSD模块和MACI模块。MSSD通过权重共享自蒸馏方法，增强低层特征、注意力图和高层表示的鲁棒性；MACI则利用因果图和多模态因果模块（MCM）来缓解标签和语言偏见。

**关键创新**：CIDer的主要创新在于其模块化设计，使得在处理模态缺失和OOD问题时，能够独立提升模型的泛化能力，且仅需少量额外参数。

**关键设计**：在MSSD模块中，采用权重共享的自蒸馏策略，降低计算复杂度；WSAM模块用于减少计算负担；MCT模块则实现高效的多模态融合。

## 📊 实验亮点

实验结果表明，CIDer在RMFM和OOD场景下的表现优于现有最先进的方法，参数更少，训练速度更快。具体而言，CIDer在OOD任务中实现了显著的性能提升，验证了其高效性和鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括情感分析、社交媒体监测和人机交互等。通过提升多模态情感识别的鲁棒性，CIDer能够在实际应用中更好地处理模态缺失和分布偏移问题，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advancements in Multimodal Emotion Recognition (MER) face challenges in addressing both modality missing and Out-Of-Distribution (OOD) data simultaneously. Existing methods often rely on specific models or introduce excessive parameters, which limits their practicality. To address these issues, we propose a novel robust MER framework, Causal Inference Distiller (CIDer), and introduce a new task, Random Modality Feature Missing (RMFM), to generalize the definition of modality missing. CIDer integrates two key components: a Model-Specific Self-Distillation (MSSD) module and a Model-Agnostic Causal Inference (MACI) module. MSSD enhances robustness under the RMFM task through a weight-sharing self-distillation approach applied across low-level features, attention maps, and high-level representations. Additionally, a Word-level Self-aligned Attention Module (WSAM) reduces computational complexity, while a Multimodal Composite Transformer (MCT) facilitates efficient multimodal fusion. To tackle OOD challenges, MACI employs a tailored causal graph to mitigate label and language biases using a Multimodal Causal Module (MCM) and fine-grained counterfactual texts. Notably, MACI can independently enhance OOD generalization with minimal additional parameters. Furthermore, we also introduce the new repartitioned MER OOD datasets. Experimental results demonstrate that CIDer achieves robust performance in both RMFM and OOD scenarios, with fewer parameters and faster training compared to state-of-the-art methods. The implementation of this work is publicly accessible at https://github.com/gw-zhong/CIDer.

