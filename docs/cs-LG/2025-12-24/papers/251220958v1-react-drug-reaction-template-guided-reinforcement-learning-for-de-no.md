---
layout: default
title: "ReACT-Drug: Reaction-Template Guided Reinforcement Learning for de novo Drug Design"
---

# ReACT-Drug: Reaction-Template Guided Reinforcement Learning for de novo Drug Design

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20958" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20958v1</a>
  <a href="https://arxiv.org/pdf/2512.20958.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20958v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20958v1', 'ReACT-Drug: Reaction-Template Guided Reinforcement Learning for de novo Drug Design')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: R Yadunandan, Nimisha Ghosh

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-24

**🔗 代码/项目**: [GITHUB](https://github.com/YadunandanRaman/ReACT-Drug/)

---

## 💡 一句话要点

**ReACT-Drug：基于反应模板引导的强化学习药物设计**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `药物设计` `强化学习` `反应模板` `蛋白结构` `从头设计`

## 📋 核心要点

1. 现有药物设计方法难以在巨大的化学空间中找到既有高亲和力又易于合成的候选药物。
2. ReACT-Drug利用强化学习，结合蛋白结构信息和反应模板，引导药物分子生成过程。
3. 实验表明，ReACT-Drug生成的药物候选物具有良好的结合亲和力、合成可及性和化学有效性。

## 📝 摘要（中文）

从头药物设计是现代药物开发的关键组成部分，但如何在广阔的化学空间中找到具有合成可及性和高亲和力的候选药物仍然是一个重大挑战。强化学习(RL)通过实现多目标优化和探索新的化学空间来增强这一过程——这是传统监督学习方法所缺乏的能力。本文介绍了一个完全集成、与靶标无关的分子设计框架ReACT-Drug，该框架基于强化学习。与需要针对特定靶标进行微调的模型不同，ReACT-Drug采用了一种通用方法，利用ESM-2蛋白嵌入从蛋白质数据库(PDB)等知识库中识别给定靶标的相似蛋白。然后，将这些蛋白质对应的已知药物配体分解，以初始化基于片段的搜索空间，从而使agent偏向于生物学相关的子空间。对于每个这样的片段，该流程采用近端策略优化(PPO) agent，通过基于ChemBERTa编码分子的化学有效反应模板的动态动作空间来引导分子。这产生了具有竞争性结合亲和力和高合成可及性的从头药物候选物，同时根据MOSES基准测试确保100%的化学有效性和新颖性。该架构突出了整合结构生物学、深度表征学习和化学合成规则以自动化和加速合理药物设计的潜力。数据集和代码可在https://github.com/YadunandanRaman/ReACT-Drug/获取。

## 🔬 方法详解

**问题定义**：论文旨在解决从头药物设计中，如何在巨大的化学空间中高效搜索具有高亲和力和良好合成可及性的药物分子的问题。现有方法，如基于规则或片段拼接的方法，难以保证生成分子的化学有效性和新颖性。而传统的监督学习方法缺乏探索新化学空间的能力，且需要大量特定靶标的数据进行训练。

**核心思路**：论文的核心思路是利用强化学习，通过奖励函数引导agent生成具有期望性质的分子。同时，利用已知的蛋白结构信息和反应模板，缩小搜索空间，提高生成效率和分子质量。通过将药物设计过程建模为一个序列决策问题，agent可以逐步构建分子，并根据奖励信号进行优化。

**技术框架**：ReACT-Drug框架包含以下主要模块：1) **蛋白相似性搜索**：利用ESM-2蛋白嵌入，从PDB等数据库中找到与目标蛋白相似的蛋白。2) **配体片段提取**：从相似蛋白的已知配体中提取片段，作为初始搜索空间。3) **强化学习Agent**：使用PPO算法训练agent，通过ChemBERTa编码分子状态，并根据反应模板选择动作。4) **奖励函数**：设计奖励函数，鼓励生成具有高亲和力、良好合成可及性和化学有效性的分子。

**关键创新**：该方法的主要创新在于：1) **反应模板引导**：使用反应模板作为动作空间，保证生成分子的化学有效性。2) **蛋白结构信息融合**：利用蛋白相似性搜索和配体片段提取，将蛋白结构信息融入到药物设计过程中。3) **通用性**：该框架不依赖于特定靶标的训练数据，具有良好的通用性。

**关键设计**：1) **反应模板选择**：使用预定义的反应模板库，并根据当前分子的结构动态选择可用的反应模板。2) **奖励函数设计**：奖励函数综合考虑了分子的结合亲和力（使用对接软件预测）、合成可及性（使用SA score评估）和化学有效性（通过惩罚不合理的化学结构实现）。3) **PPO Agent**：使用Proximal Policy Optimization (PPO) 算法训练agent，平衡探索和利用，提高训练效率和稳定性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20958v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20958v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20958v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

ReACT-Drug在从头药物设计任务中表现出色，生成的分子具有竞争性的结合亲和力、高合成可及性和100%的化学有效性。与现有方法相比，ReACT-Drug无需针对特定靶标进行微调，具有更好的通用性。该方法在MOSES基准测试中表现出良好的新颖性，表明其能够探索新的化学空间。

## 🎯 应用场景

ReACT-Drug具有广泛的应用前景，可用于加速新药发现过程，降低研发成本。该方法可以用于针对各种疾病靶标设计候选药物，尤其是在缺乏足够训练数据的情况下。此外，该框架还可以用于优化现有药物的性质，例如提高生物利用度或降低毒性。未来，ReACT-Drug可以与其他计算方法（如分子动力学模拟）相结合，进一步提高药物设计的准确性和效率。

## 📄 摘要（原文）

> De novo drug design is a crucial component of modern drug development, yet navigating the vast chemical space to find synthetically accessible, high-affinity candidates remains a significant challenge. Reinforcement Learning (RL) enhances this process by enabling multi-objective optimization and exploration of novel chemical space - capabilities that traditional supervised learning methods lack. In this work, we introduce \textbf{ReACT-Drug}, a fully integrated, target-agnostic molecular design framework based on Reinforcement Learning. Unlike models requiring target-specific fine-tuning, ReACT-Drug utilizes a generalist approach by leveraging ESM-2 protein embeddings to identify similar proteins for a given target from a knowledge base such as Protein Data Base (PDB). Thereafter, the known drug ligands corresponding to such proteins are decomposed to initialize a fragment-based search space, biasing the agent towards biologically relevant subspaces. For each such fragment, the pipeline employs a Proximal Policy Optimization (PPO) agent guiding a ChemBERTa-encoded molecule through a dynamic action space of chemically valid, reaction-template-based transformations. This results in the generation of \textit{de novo} drug candidates with competitive binding affinities and high synthetic accessibility, while ensuring 100\% chemical validity and novelty as per MOSES benchmarking. This architecture highlights the potential of integrating structural biology, deep representation learning, and chemical synthesis rules to automate and accelerate rational drug design. The dataset and code are available at https://github.com/YadunandanRaman/ReACT-Drug/.

