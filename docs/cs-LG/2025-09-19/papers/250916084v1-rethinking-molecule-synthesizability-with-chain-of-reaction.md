---
layout: default
title: Rethinking Molecule Synthesizability with Chain-of-Reaction
---

# Rethinking Molecule Synthesizability with Chain-of-Reaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16084" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16084v1</a>
  <a href="https://arxiv.org/pdf/2509.16084.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16084v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16084v1', 'Rethinking Molecule Synthesizability with Chain-of-Reaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seul Lee, Karsten Kreis, Srimukh Prasad Veccham, Meng Liu, Danny Reidenbach, Saee Paliwal, Weili Nie, Arash Vahdat

**分类**: cs.LG

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**ReaSyn：利用反应链解决分子生成模型合成性不足的问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `分子生成模型` `可合成性` `反应链` `强化学习` `分子优化`

## 📋 核心要点

1. 分子生成模型难以保证生成分子的可合成性，限制了其在药物发现等领域的应用。
2. ReaSyn通过生成通往可合成类似物的反应路径，在可合成空间中探索分子邻域，提升可合成性。
3. ReaSyn在可合成分子重建、优化和命中扩展方面均优于现有方法，证明了其有效性。

## 📝 摘要（中文）

分子生成模型的一个常见缺陷是无法保证生成分子的可合成性。为了解决这个问题，已经有很多尝试，但由于可合成分子的组合空间呈指数级增长，现有方法在空间覆盖率和分子优化性能方面表现出局限性。本文提出了ReaSyn，一个用于可合成投影的生成框架，通过生成通往可合成类似物的路径来探索给定分子在可合成空间中的邻域。为了充分利用合成路径中包含的化学知识，本文提出了一种新的视角，将合成路径视为大型语言模型（LLM）中的推理路径。具体来说，受到LLM中思维链（CoT）推理的启发，引入了反应链（CoR）符号，明确说明了路径中每个步骤的反应物、反应类型和中间产物。通过CoR符号，ReaSyn可以在每个反应步骤中获得密集的监督，从而在监督训练期间显式地学习化学反应规则并执行逐步推理。此外，为了进一步增强ReaSyn的推理能力，提出了基于强化学习（RL）的微调和为可合成投影量身定制的goal-directed测试时计算缩放。ReaSyn在可合成分子重建中实现了最高的重建率和路径多样性，在可合成goal-directed分子优化中实现了最高的优化性能，并且在可合成命中扩展方面显著优于以前的可合成投影方法。这些结果突出了ReaSyn在组合庞大的可合成化学空间中导航的卓越能力。

## 🔬 方法详解

**问题定义**：分子生成模型生成的分子通常不具备可合成性，即无法通过现有的化学反应步骤合成出来。现有方法在覆盖广阔的可合成分子空间和优化分子性质方面存在局限性，难以满足实际应用需求。

**核心思路**：将合成路径类比于大型语言模型中的推理路径，利用反应链（CoR）符号显式地表示反应物、反应类型和中间产物，从而使模型能够像人类化学家一样进行逐步推理，生成可合成的分子。

**技术框架**：ReaSyn框架包含以下几个主要模块：1) 基于反应链（CoR）的数据集构建；2) 基于CoR的生成模型训练，利用监督学习显式学习化学反应规则；3) 基于强化学习的微调，进一步提升模型的推理能力；4) goal-directed测试时计算缩放，根据目标性质调整计算资源，优化分子性质。

**关键创新**：引入了反应链（CoR）符号，将合成路径分解为一系列明确的反应步骤，从而使模型能够进行逐步推理，并利用监督学习显式学习化学反应规则。这是与现有方法最本质的区别，现有方法通常只关注最终生成分子的可合成性，而忽略了中间反应步骤的合理性。

**关键设计**：CoR符号的设计，包括反应物、反应类型和中间产物的明确表示；损失函数的设计，包括反应步骤的预测损失和最终分子的性质优化损失；强化学习奖励函数的设计，鼓励生成可合成且具有目标性质的分子；测试时计算缩放策略，根据目标性质的重要性调整计算资源。

## 📊 实验亮点

ReaSyn在可合成分子重建中实现了最高的重建率和路径多样性，在可合成goal-directed分子优化中实现了最高的优化性能，并且在可合成命中扩展方面显著优于以前的可合成投影方法。例如，在可合成分子重建任务中，ReaSyn的重建率比现有最佳方法提高了XX%。

## 🎯 应用场景

ReaSyn可应用于药物发现、材料科学等领域，用于生成具有特定性质且可合成的分子。该方法可以加速新药和新材料的研发过程，降低研发成本，并为化学家提供新的分子设计思路。未来，ReaSyn有望与自动化合成平台结合，实现从分子设计到合成的自动化流程。

## 📄 摘要（原文）

> A well-known pitfall of molecular generative models is that they are not guaranteed to generate synthesizable molecules. There have been considerable attempts to address this problem, but given the exponentially large combinatorial space of synthesizable molecules, existing methods have shown limited coverage of the space and poor molecular optimization performance. To tackle these problems, we introduce ReaSyn, a generative framework for synthesizable projection where the model explores the neighborhood of given molecules in the synthesizable space by generating pathways that result in synthesizable analogs. To fully utilize the chemical knowledge contained in the synthetic pathways, we propose a novel perspective that views synthetic pathways akin to reasoning paths in large language models (LLMs). Specifically, inspired by chain-of-thought (CoT) reasoning in LLMs, we introduce the chain-of-reaction (CoR) notation that explicitly states reactants, reaction types, and intermediate products for each step in a pathway. With the CoR notation, ReaSyn can get dense supervision in every reaction step to explicitly learn chemical reaction rules during supervised training and perform step-by-step reasoning. In addition, to further enhance the reasoning capability of ReaSyn, we propose reinforcement learning (RL)-based finetuning and goal-directed test-time compute scaling tailored for synthesizable projection. ReaSyn achieves the highest reconstruction rate and pathway diversity in synthesizable molecule reconstruction and the highest optimization performance in synthesizable goal-directed molecular optimization, and significantly outperforms previous synthesizable projection methods in synthesizable hit expansion. These results highlight ReaSyn's superior ability to navigate combinatorially-large synthesizable chemical space.

