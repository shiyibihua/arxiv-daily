---
layout: default
title: Compass-Thinker-7B Technical Report
---

# Compass-Thinker-7B Technical Report

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08909" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08909v2</a>
  <a href="https://arxiv.org/pdf/2508.08909.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08909v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08909v2', 'Compass-Thinker-7B Technical Report')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anxiang Zeng, Haibo Zhang, Kaixiang Mo, Long Zhang, Shuman Liu, Yanhui Huang, Yawen Liu, Yuepeng Sheng, Yuwei Huang

**分类**: cs.AI

**发布日期**: 2025-08-12 (更新: 2025-08-14)

---

## 💡 一句话要点

**提出Compass-Thinker-7B以降低大规模模型的RL实验成本**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大规模模型` `数学推理` `模型训练` `计算效率`

## 📋 核心要点

1. 现有方法在超大规模模型上进行强化学习实验面临高计算成本和资源需求的挑战。
2. Compass-Thinker-7B通过专门设计的强化学习管道，旨在以较低的计算资源探索强化学习的潜力。
3. 实验结果表明，Compass-Thinker-7B在数学推理上表现优异，尤其在AIME2024评估中达到了40%的准确率。

## 📝 摘要（中文）

近期的R1-Zero类研究进一步证明了推理扩展赋予大型语言模型（LLMs）前所未有的推理能力，而强化学习是引导其复杂推理的核心技术。然而，直接在超大规模模型上进行RL实验涉及高计算成本和资源需求，存在显著风险。我们提出了Compass-Thinker-7B模型，旨在探索在较低计算资源和成本下的强化学习潜力，并为更大模型的RL配方研究提供见解。Compass-Thinker-7B通过专门设计的强化学习管道从开源模型训练而来。我们为强化学习管道策划了3万个可验证的数学问题数据集。通过为不同阶段配置不同难度分布的数据和训练设置，模型的潜力逐步释放，训练效率得到提升。广泛评估显示，Compass-Thinker-7B具有卓越的推理潜力，在数学问题上表现优于同规模的RL模型，尤其在具有挑战性的AIME2024评估中，Compass-Thinker-7B达到了40%的准确率。

## 🔬 方法详解

**问题定义**：论文要解决的问题是如何在高计算成本和资源需求的情况下进行大规模模型的强化学习实验。现有方法在这一方面存在显著的局限性，导致研究进展缓慢。

**核心思路**：论文的核心解决思路是通过设计一个强化学习管道，利用较小的模型进行实验，从而降低计算资源的消耗，并逐步释放模型的推理潜力。

**技术框架**：整体架构包括数据集的策划、强化学习管道的设计和训练设置的配置。数据集包含3万个可验证的数学问题，训练设置根据不同阶段的难度分布进行调整。

**关键创新**：最重要的技术创新点在于通过精心设计的强化学习管道，使得在较小模型上进行有效的强化学习实验成为可能，这与传统方法直接在超大规模模型上进行实验的方式有本质区别。

**关键设计**：关键设计包括数据集的构建、不同阶段的难度配置、训练参数的调整等，确保模型在训练过程中能够逐步提高推理能力和训练效率。

## 📊 实验亮点

实验结果显示，Compass-Thinker-7B在数学推理任务上表现优异，尤其在AIME2024评估中达到了40%的准确率，显著优于同规模的强化学习模型。这一成果展示了在较低计算资源下进行有效强化学习的可能性，具有重要的研究和应用价值。

## 🎯 应用场景

该研究的潜在应用领域包括教育、智能辅导系统和自动化数学问题解决等。通过提高模型的推理能力，Compass-Thinker-7B可以在教育技术中提供更智能的学习支持，帮助学生解决复杂的数学问题，提升学习效果。未来，该模型的设计理念和方法也可扩展到其他领域的强化学习研究中。

## 📄 摘要（原文）

> Recent R1-Zero-like research further demonstrates that reasoning extension has given large language models (LLMs) unprecedented reasoning capabilities, and Reinforcement Learning is the core technology to elicit its complex reasoning. However, conducting RL experiments directly on hyperscale models involves high computational costs and resource demands, posing significant risks. We propose the Compass-Thinker-7B model, which aims to explore the potential of Reinforcement Learning with less computational resources and costs, and provides insights for further research into RL recipes for larger models. Compass-Thinker-7B is trained from an open source model through a specially designed Reinforcement Learning Pipeline. We curate a dataset of 30k verifiable mathematics problems for the Reinforcement Learning Pipeline. By configuring data and training settings with different difficulty distributions for different stages, the potential of the model is gradually released and the training efficiency is improved. Extensive evaluations show that Compass-Thinker-7B possesses exceptional reasoning potential, and achieves superior performance on mathematics compared to the same-sized RL model. Especially in the challenging AIME2024 evaluation, Compass-Thinker-7B achieves 40% accuracy.

