---
layout: default
title: Unlocking Post-hoc Dataset Inference with Synthetic Data
---

# Unlocking Post-hoc Dataset Inference with Synthetic Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15271" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15271v1</a>
  <a href="https://arxiv.org/pdf/2506.15271.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15271v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15271v1', 'Unlocking Post-hoc Dataset Inference with Synthetic Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bihe Zhao, Pratyush Maini, Franziska Boenisch, Adam Dziedzic

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-18

**备注**: Accepted at ICML 2025

**🔗 代码/项目**: [GITHUB](https://github.com/sprintml/PostHocDatasetInference)

---

## 💡 一句话要点

**提出合成数据生成方法以解决数据集推断问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数据集推断` `合成数据` `版权保护` `机器学习` `数据隐私` `法律诉讼` `文本分析`

## 📋 核心要点

1. 现有的数据集推断方法依赖于与受损数据集分布相匹配的私有数据集，这在实际中难以获得。
2. 本文提出了一种合成数据生成方法，通过训练数据生成器来创建高质量的持出数据集，以支持数据集推断。
3. 实验结果显示，使用合成数据作为持出集，数据集推断的检测准确率显著提高，同时误报率保持在较低水平。

## 📝 摘要（中文）

大型语言模型（LLMs）的卓越能力主要归功于其庞大的训练数据集，这些数据集通常未经数据所有者同意而从互联网抓取。数据集推断（DI）提供了一种潜在的解决方案，通过识别可疑数据集是否用于训练，使数据所有者能够验证未经授权的使用。然而，现有DI方法需要一个与受损数据集分布相匹配的私有数据集，这种数据在实践中很少可得。本文通过合成生成所需的持出集来解决这一挑战。我们的方法克服了两个关键障碍：一是创建高质量、多样化的合成数据，二是通过后期校准弥补真实数据与合成数据之间的可能性差距。实验表明，使用我们生成的数据作为持出集可以高效地检测原始训练集，同时保持较低的误报率。

## 🔬 方法详解

**问题定义**：本文旨在解决数据集推断（DI）中缺乏与受损数据集分布匹配的持出数据集的问题。现有方法在实际应用中受到限制，因为很难获得合适的私有数据集。

**核心思路**：我们提出了一种合成数据生成的方法，通过训练一个数据生成器来创建高质量的持出数据集，从而支持数据集推断的有效性。该方法的设计旨在确保合成数据能够准确反映原始数据的分布特征。

**技术框架**：整体架构包括两个主要模块：首先是基于后缀的完成任务训练数据生成器，生成多样化的合成数据；其次是后期校准模块，用于弥补真实数据与合成数据之间的可能性差距。

**关键创新**：本文的核心创新在于通过合成数据生成来解决DI中的数据缺失问题，显著提高了DI的适用性和准确性。这一方法与现有依赖真实数据集的DI方法本质上不同。

**关键设计**：在技术细节上，我们设计了特定的损失函数以优化数据生成器的性能，并采用了多样化的训练样本以确保生成数据的质量和多样性。

## 📊 实验亮点

实验结果表明，使用合成生成的数据作为持出集，数据集推断的检测准确率达到了高水平，同时误报率保持在较低水平。这一方法在多样化文本数据集上的表现尤为突出，显示出其在实际应用中的可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括版权保护、数据使用合规性验证等。通过提供一种有效的工具，数据所有者可以更好地维护其知识产权，减少未经授权的数据使用。未来，该方法可能在法律诉讼中发挥重要作用，帮助数据所有者提出合法的索赔。

## 📄 摘要（原文）

> The remarkable capabilities of Large Language Models (LLMs) can be mainly attributed to their massive training datasets, which are often scraped from the internet without respecting data owners' intellectual property rights. Dataset Inference (DI) offers a potential remedy by identifying whether a suspect dataset was used in training, thereby enabling data owners to verify unauthorized use. However, existing DI methods require a private set-known to be absent from training-that closely matches the compromised dataset's distribution. Such in-distribution, held-out data is rarely available in practice, severely limiting the applicability of DI. In this work, we address this challenge by synthetically generating the required held-out set. Our approach tackles two key obstacles: (1) creating high-quality, diverse synthetic data that accurately reflects the original distribution, which we achieve via a data generator trained on a carefully designed suffix-based completion task, and (2) bridging likelihood gaps between real and synthetic data, which is realized through post-hoc calibration. Extensive experiments on diverse text datasets show that using our generated data as a held-out set enables DI to detect the original training sets with high confidence, while maintaining a low false positive rate. This result empowers copyright owners to make legitimate claims on data usage and demonstrates our method's reliability for real-world litigations. Our code is available at https://github.com/sprintml/PostHocDatasetInference.

