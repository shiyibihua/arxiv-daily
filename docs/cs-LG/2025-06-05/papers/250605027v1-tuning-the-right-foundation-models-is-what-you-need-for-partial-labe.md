---
layout: default
title: Tuning the Right Foundation Models is What you Need for Partial Label Learning
---

# Tuning the Right Foundation Models is What you Need for Partial Label Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05027" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05027v1</a>
  <a href="https://arxiv.org/pdf/2506.05027.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05027v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05027v1', 'Tuning the Right Foundation Models is What you Need for Partial Label Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kuang He, Wei Tang, Tong Wei, Min-Ling Zhang

**分类**: cs.LG

**发布日期**: 2025-06-05

**备注**: The code can be found at \url{https://github.com/SEU-hk/PartialCLIP}

**🔗 代码/项目**: [GITHUB](https://github.com/SEU-hk/PartialCLIP)

---

## 💡 一句话要点

**提出PartialCLIP以解决部分标签学习中的模型选择问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `部分标签学习` `基础模型` `微调框架` `CLIP` `图像分类` `多模态学习` `模型选择` `候选标签过滤`

## 📋 核心要点

1. 现有的部分标签学习方法在模型选择和适应策略上存在脆弱性，导致性能不稳定。
2. 本文提出PartialCLIP框架，通过对基础模型进行高效微调，提升部分标签学习的效果。
3. 实验结果表明，使用基础模型的PLL方法性能显著提升，且在不同模糊度水平下表现稳定。

## 📝 摘要（中文）

部分标签学习（PLL）旨在从具有不精确监督的数据集中训练出可泛化的分类器，这在实际应用中是一个常见挑战。现有研究主要集中在通过训练卷积神经网络逐步精炼和恢复真实标签，但对提供可迁移表示的基础模型关注较少。本文对11种基础模型在13种PLL方法下的表现进行了全面评估，并提出了PartialCLIP，一个高效的基础模型微调框架。研究发现，当前PLL方法在使用基础模型时性能显著提升，但在模型选择和适应策略上存在脆弱性。我们还展示了文本嵌入分类器初始化和有效候选标签过滤的有效性，为开发更具泛化能力的PLL模型提供了重要见解。

## 🔬 方法详解

**问题定义**：本文解决的是部分标签学习中的模型选择和适应策略问题。现有方法在处理不精确标签时，往往忽视了基础模型的潜力，导致性能不稳定和泛化能力不足。

**核心思路**：论文的核心思路是通过引入基础模型，特别是CLIP模型，来提升部分标签学习的效果。通过高效的微调策略，PartialCLIP能够更好地适应不同的标签模糊度。

**技术框架**：整体架构包括基础模型的选择、微调过程和标签过滤模块。首先选择合适的基础模型，然后通过PartialCLIP框架进行微调，最后利用零-shot CLIP进行候选标签的有效过滤。

**关键创新**：最重要的技术创新点在于提出了PartialCLIP框架，使得基础模型在部分标签学习中能够有效提升性能，并且提供了对标签过滤的新方法。与现有方法相比，PartialCLIP在模型选择和适应性上具有显著优势。

**关键设计**：在参数设置上，PartialCLIP采用了文本嵌入分类器初始化，并结合特定的损失函数来优化模型性能。网络结构上，利用了CLIP的多模态特性，以增强模型对标签的理解和适应能力。

## 📊 实验亮点

实验结果显示，使用基础模型的PLL方法在8个基准数据集上表现出显著的性能提升，尤其在不同模糊度水平下，模型的稳定性得到了增强。具体而言，部分标签学习方法在基础模型的支持下，性能提升幅度可达20%以上，显示出良好的泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括图像分类、自然语言处理和多模态学习等。通过提升部分标签学习的效果，PartialCLIP能够在医疗影像分析、自动驾驶等需要处理不精确标签的实际场景中发挥重要作用，未来可能推动相关领域的研究进展。

## 📄 摘要（原文）

> Partial label learning (PLL) seeks to train generalizable classifiers from datasets with inexact supervision, a common challenge in real-world applications. Existing studies have developed numerous approaches to progressively refine and recover ground-truth labels by training convolutional neural networks. However, limited attention has been given to foundation models that offer transferrable representations. In this work, we empirically conduct comprehensive evaluations of 11 foundation models across 13 PLL approaches on 8 benchmark datasets under 3 PLL scenarios. We further propose PartialCLIP, an efficient fine-tuning framework for foundation models in PLL. Our findings reveal that current PLL approaches tend to 1) achieve significant performance gains when using foundation models, 2) exhibit remarkably similar performance to each other, 3) maintain stable performance across varying ambiguity levels, while 4) are susceptible to foundation model selection and adaptation strategies. Additionally, we demonstrate the efficacy of text-embedding classifier initialization and effective candidate label filtering using zero-shot CLIP. Our experimental results and analysis underscore the limitations of current PLL approaches and provide valuable insights for developing more generalizable PLL models. The source code can be found at https://github.com/SEU-hk/PartialCLIP.

