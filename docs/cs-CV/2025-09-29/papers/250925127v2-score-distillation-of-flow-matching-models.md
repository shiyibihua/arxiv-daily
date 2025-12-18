---
layout: default
title: Score Distillation of Flow Matching Models
---

# Score Distillation of Flow Matching Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25127" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25127v2</a>
  <a href="https://arxiv.org/pdf/2509.25127.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25127v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25127v2', 'Score Distillation of Flow Matching Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingyuan Zhou, Yi Gu, Huangjie Zheng, Liangchen Song, Guande He, Yizhe Zhang, Wenze Hu, Yinfei Yang

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-09-29 (更新: 2025-12-03)

**🔗 代码/项目**: [PROJECT_PAGE](https://yigu1008.github.io/SiD-DiT)

---

## 💡 一句话要点

**将Score Distillation成功应用于Flow Matching模型，实现快速高质量图像生成。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `Flow Matching` `扩散模型` `Score Distillation` `图像生成` `DiT` `模型加速` `文本到图像生成`

## 📋 核心要点

1. 扩散模型生成图像质量高，但迭代采样速度慢，限制了其应用。
2. 论文基于贝叶斯规则统一了高斯扩散和Flow Matching，无需ODE/SDE公式。
3. 成功将SiD应用于多种Flow Matching模型，无需教师微调或架构修改，实现快速生成。

## 📝 摘要（中文）

扩散模型在图像生成方面表现出色，但受限于缓慢的迭代采样过程。蒸馏方法通过实现单步或少数步生成来缓解这一问题。Flow matching最初作为一个独立的框架被提出，但后来在理论上被证明与高斯假设下的扩散模型等价。这引发了一个问题：诸如score distillation之类的蒸馏技术是否可以直接迁移。我们提供了一个简单的推导——基于贝叶斯规则和条件期望——统一了高斯扩散和flow matching，而无需依赖ODE/SDE公式。在此基础上，我们将Score identity Distillation (SiD)扩展到预训练的文本到图像flow-matching模型，包括SANA、SD3-Medium、SD3.5-Medium/Large和FLUX.1-dev，所有这些模型都具有DiT骨干网络。实验表明，只需对flow-matching和DiT进行适度的调整，SiD就可以在这些模型中开箱即用，无论是在无数据还是数据辅助设置中，而无需教师微调或架构更改。这首次系统地证明了score distillation广泛适用于文本到图像flow matching模型，解决了之前关于稳定性和合理性的担忧，并统一了基于扩散和基于flow的生成器的加速技术。

## 🔬 方法详解

**问题定义**：论文旨在解决扩散模型采样速度慢的问题，并探索score distillation方法在flow matching模型中的适用性。现有扩散模型的迭代采样过程耗时，而flow matching模型虽然理论上与扩散模型等价，但缺乏有效的蒸馏加速方法。

**核心思路**：论文的核心思路是利用score distillation技术，将复杂、多步的flow matching模型“提炼”成一个更简单、单步或少数步即可完成生成的模型。通过最小化学生模型和教师模型之间的score差异，学生模型可以学习到教师模型的生成能力，从而实现快速采样。

**技术框架**：整体框架包括一个预训练的flow matching模型（教师模型）和一个需要训练的学生模型。训练过程使用score distillation损失函数，鼓励学生模型的score函数逼近教师模型的score函数。具体流程为：首先，从数据分布中采样数据点；然后，使用教师模型计算score；最后，使用学生模型预测score，并计算损失函数，更新学生模型的参数。

**关键创新**：论文的关键创新在于证明了score distillation可以有效地应用于flow matching模型，并且只需要对flow matching和DiT架构进行适度的调整。此外，论文还提供了一个基于贝叶斯规则和条件期望的简单推导，统一了高斯扩散和flow matching，无需依赖ODE/SDE公式。

**关键设计**：论文使用了Score identity Distillation (SiD)作为主要的蒸馏方法。针对不同的flow matching模型，论文进行了适度的参数调整，例如学习率和训练步数。此外，论文还使用了DiT作为backbone网络，并针对DiT的特点进行了优化。

## 📊 实验亮点

实验结果表明，SiD可以成功应用于多种预训练的文本到图像flow-matching模型，包括SANA、SD3-Medium、SD3.5-Medium/Large和FLUX.1-dev。在无数据和数据辅助设置下，SiD均表现良好，无需教师微调或架构更改。这证明了score distillation方法在flow matching模型中的有效性和通用性。

## 🎯 应用场景

该研究成果可广泛应用于图像生成领域，例如文本到图像生成、图像编辑、图像修复等。通过加速图像生成过程，可以降低计算成本，提高用户体验。此外，该方法还可以应用于其他生成模型，例如音频生成、视频生成等，具有重要的实际价值和广阔的应用前景。

## 📄 摘要（原文）

> Diffusion models achieve high-quality image generation but are limited by slow iterative sampling. Distillation methods alleviate this by enabling one- or few-step generation. Flow matching, originally introduced as a distinct framework, has since been shown to be theoretically equivalent to diffusion under Gaussian assumptions, raising the question of whether distillation techniques such as score distillation transfer directly. We provide a simple derivation -- based on Bayes' rule and conditional expectations -- that unifies Gaussian diffusion and flow matching without relying on ODE/SDE formulations. Building on this view, we extend Score identity Distillation (SiD) to pretrained text-to-image flow-matching models, including SANA, SD3-Medium, SD3.5-Medium/Large, and FLUX.1-dev, all with DiT backbones. Experiments show that, with only modest flow-matching- and DiT-specific adjustments, SiD works out of the box across these models, in both data-free and data-aided settings, without requiring teacher finetuning or architectural changes. This provides the first systematic evidence that score distillation applies broadly to text-to-image flow matching models, resolving prior concerns about stability and soundness and unifying acceleration techniques across diffusion- and flow-based generators. A project page is available at https://yigu1008.github.io/SiD-DiT.

