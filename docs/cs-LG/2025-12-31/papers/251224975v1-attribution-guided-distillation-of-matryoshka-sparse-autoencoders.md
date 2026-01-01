---
layout: default
title: Attribution-Guided Distillation of Matryoshka Sparse Autoencoders
---

# Attribution-Guided Distillation of Matryoshka Sparse Autoencoders

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24975" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24975v1</a>
  <a href="https://arxiv.org/pdf/2512.24975.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24975v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24975v1', 'Attribution-Guided Distillation of Matryoshka Sparse Autoencoders')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cristina P. Martin-Linares, Jonathan P. Ling

**分类**: cs.LG

**发布日期**: 2025-12-31

---

## 💡 一句话要点

**提出DMSAE，通过归因引导蒸馏Matryoshka稀疏自编码器，提升特征一致性和可迁移性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `稀疏自编码器` `蒸馏学习` `模型解释性` `特征提取` `知识迁移`

## 📋 核心要点

1. 现有稀疏自编码器学习到的特征冗余且不稳定，导致解释性差，难以迁移和复用。
2. DMSAE通过迭代蒸馏，提取并重用一致且有用的特征核心，提升特征的稳定性和可迁移性。
3. 实验表明，使用DMSAE蒸馏出的特征核心训练SAE，能有效提升SAEBench指标，验证了方法有效性。

## 📝 摘要（中文）

稀疏自编码器(SAE)旨在将模型激活解耦为单义的、人类可解释的特征。然而，实践中学习到的特征通常是冗余的，并且在不同的训练运行和稀疏度水平上有所不同，这使得解释难以转移和重用。我们引入了Distilled Matryoshka Sparse Autoencoders (DMSAEs)，这是一种训练流程，它提炼出一个紧凑的、始终有用的特征核心，并重用它来训练新的SAE。DMSAEs运行一个迭代蒸馏循环：训练一个具有共享核心的Matryoshka SAE，使用梯度X激活来测量每个特征对最嵌套重建中下一个token损失的贡献，并且只保留解释固定比例归因的最小子集。只有核心编码器权重向量在循环中传递；核心解码器和所有非核心潜在变量每次都会重新初始化。在Gemma-2-2B第12层残差流激活上，七个循环的蒸馏（500M tokens，65k宽度）产生了一个重复选择的197个特征的蒸馏核心。使用这个蒸馏核心进行训练提高了几个SAEBench指标，并证明了一致的潜在特征集可以在不同的稀疏度水平上传输。

## 🔬 方法详解

**问题定义**：论文旨在解决稀疏自编码器(SAE)训练中特征冗余、不稳定以及难以迁移的问题。现有的SAE训练方法在不同训练轮次和稀疏度下，学习到的特征差异较大，导致模型解释性差，且难以将学到的知识迁移到新的任务或模型上。

**核心思路**：论文的核心思路是通过蒸馏的方式，从多个SAE中提取出一个共享的、一致的特征核心，并利用该核心来指导后续SAE的训练。通过迭代蒸馏，逐步筛选出对模型性能贡献最大的特征，从而获得一个紧凑且稳定的特征表示。

**技术框架**：DMSAE的整体框架是一个迭代蒸馏循环。每个循环包含以下步骤：1) 训练一个Matryoshka SAE，该SAE具有一个共享的核心编码器；2) 使用梯度X激活方法评估每个特征对下一个token预测损失的贡献；3) 选择贡献最大的特征子集作为新的核心；4) 将核心编码器的权重传递到下一个循环，并重新初始化核心解码器和非核心潜在变量。

**关键创新**：DMSAE的关键创新在于使用归因方法（梯度X激活）来指导特征选择，从而确保选择的特征对模型性能具有重要意义。此外，通过迭代蒸馏和核心重用，DMSAE能够学习到更加稳定和可迁移的特征表示。与现有方法相比，DMSAE能够有效地减少特征冗余，并提高特征的一致性。

**关键设计**：DMSAE的关键设计包括：1) 使用Matryoshka SAE作为基础模型，允许在不同稀疏度下进行训练；2) 使用梯度X激活作为归因方法，评估特征的重要性；3) 设置固定的归因比例，控制核心的大小；4) 迭代蒸馏的循环次数和训练tokens数量等超参数。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24975v1/figures/Fig1_DMSAE_Schematic_DynamicNonCoreL0.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24975v1/figures/k320_core_latent_origins_0-1-2-3-4-5-6-7.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24975v1/figures/figure_distilled_vs_random_1panel.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在Gemma-2-2B模型第12层残差流激活上的实验表明，经过七个循环的蒸馏（500M tokens，65k宽度），DMSAE能够提取出一个包含197个特征的蒸馏核心，这些特征在不同的训练轮次中被重复选择。使用该核心进行训练，能够有效提升SAEBench的各项指标，证明了DMSAE能够学习到稳定且可迁移的特征表示。

## 🎯 应用场景

DMSAE可应用于自然语言处理领域，例如提升大型语言模型的解释性和可控性。通过提取模型内部的关键特征，可以更好地理解模型的行为，并进行针对性的干预和优化。此外，DMSAE还可以用于知识迁移和模型压缩，将大型模型的知识迁移到小型模型，并减少模型的计算复杂度。

## 📄 摘要（原文）

> Sparse autoencoders (SAEs) aim to disentangle model activations into monosemantic, human-interpretable features. In practice, learned features are often redundant and vary across training runs and sparsity levels, which makes interpretations difficult to transfer and reuse. We introduce Distilled Matryoshka Sparse Autoencoders (DMSAEs), a training pipeline that distills a compact core of consistently useful features and reuses it to train new SAEs. DMSAEs run an iterative distillation cycle: train a Matryoshka SAE with a shared core, use gradient X activation to measure each feature's contribution to next-token loss in the most nested reconstruction, and keep only the smallest subset that explains a fixed fraction of the attribution. Only the core encoder weight vectors are transferred across cycles; the core decoder and all non-core latents are reinitialized each time. On Gemma-2-2B layer 12 residual stream activations, seven cycles of distillation (500M tokens, 65k width) yielded a distilled core of 197 features that were repeatedly selected. Training using this distilled core improves several SAEBench metrics and demonstrates that consistent sets of latent features can be transferred across sparsity levels

