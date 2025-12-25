---
layout: default
title: "TICON: A Slide-Level Tile Contextualizer for Histopathology Representation Learning"
---

# TICON: A Slide-Level Tile Contextualizer for Histopathology Representation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21331" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21331v1</a>
  <a href="https://arxiv.org/pdf/2512.21331.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21331v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21331v1', 'TICON: A Slide-Level Tile Contextualizer for Histopathology Representation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Varun Belagali, Saarthak Kapse, Pierre Marza, Srijan Das, Zilinghan Li, Sofiène Boutaj, Pushpak Pati, Srikar Yellapragada, Tarak Nath Nandi, Ravi K Madduri, Joel Saltz, Prateek Prasanna, Stergios Christodoulidis Maria Vakalopoulou, Dimitris Samaras

**分类**: cs.CV

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**TICON：一种用于组织病理学表征学习的切片级上下文建模方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `组织病理学` `全切片图像` `表征学习` `Transformer` `上下文建模`

## 📋 核心要点

1. 现有方法缺乏对WSI中切片间上下文信息的有效建模，限制了病理图像分析的性能。
2. TICON通过Transformer架构，对切片表征进行上下文建模，从而捕获切片间的依赖关系和全局信息。
3. 实验表明，TICON在多个切片和WSI级别的病理图像分析任务上，均取得了显著的性能提升。

## 📝 摘要（中文）

在大型全切片图像(WSI)中，小切片的判读通常需要更大的图像上下文。我们提出了TICON，一种基于Transformer的切片表征上下文建模器，为计算病理学中的“任何”应用生成丰富的、上下文相关的嵌入。标准的基于切片编码器的流程，提取的切片嵌入缺乏上下文信息，无法对局部和全局任务至关重要的切片级信息进行建模。此外，不同的切片编码器擅长不同的下游任务。因此，需要一个统一的模型来对来自“任何”切片级基础模型的嵌入进行上下文建模。TICON通过一个共享的编码器来满足这一需求，该编码器使用掩码建模目标进行预训练，以同时统一和上下文建模来自不同切片级病理学基础模型的表征。实验表明，TICON上下文嵌入显著提高了各种任务的性能，在切片级基准(HEST-Bench、THUNDER、CATCH)和切片级基准(Patho-Bench)上建立了新的最先进结果。最后，我们仅使用1.1万张WSI在TICON上预训练了一个聚合器，形成了一个切片级基础模型，其性能优于使用高达35万张WSI预训练的最先进的切片级基础模型。

## 🔬 方法详解

**问题定义**：现有基于切片编码器的病理图像分析方法，通常将切片从其原始WSI上下文中剥离，导致无法有效利用切片间的空间关系和全局信息。此外，不同的切片编码器适用于不同的下游任务，缺乏一个通用的上下文建模框架。

**核心思路**：TICON的核心思路是利用Transformer架构对切片表征进行上下文建模。通过将切片表征视为序列，并利用Transformer的自注意力机制，TICON能够捕获切片间的依赖关系，从而生成更具信息量的上下文嵌入。

**技术框架**：TICON的整体框架包括三个主要模块：切片编码器、Transformer上下文建模器和下游任务适配器。首先，使用预训练的切片编码器提取每个切片的表征。然后，将这些表征输入到Transformer上下文建模器中，以生成上下文嵌入。最后，将上下文嵌入输入到下游任务适配器中，以完成特定的病理图像分析任务。

**关键创新**：TICON的关键创新在于其Transformer上下文建模器。该模块能够有效地捕获切片间的依赖关系，从而生成更具信息量的上下文嵌入。此外，TICON采用了一种掩码建模目标进行预训练，使得模型能够学习到更鲁棒的表征。

**关键设计**：TICON使用标准的Transformer架构作为上下文建模器。为了提高训练效率，TICON采用了相对位置编码。此外，TICON使用AdamW优化器进行训练，并采用余弦退火学习率策略。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21331v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21331v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21331v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

TICON在多个病理图像分析基准测试中取得了显著的性能提升。例如，在HEST-Bench、THUNDER和CATCH等切片级基准测试中，TICON均取得了最先进的结果。此外，TICON在Patho-Bench切片级基准测试中也表现出色，甚至超越了使用更大规模数据集预训练的模型。

## 🎯 应用场景

TICON可广泛应用于计算病理学领域，例如肿瘤亚型分类、淋巴结转移检测、免疫组化评分等。通过提供更具上下文信息的切片表征，TICON能够提高病理图像分析的准确性和效率，辅助病理医生进行诊断和治疗决策，具有重要的临床应用价值。

## 📄 摘要（原文）

> The interpretation of small tiles in large whole slide images (WSI) often needs a larger image context. We introduce TICON, a transformer-based tile representation contextualizer that produces rich, contextualized embeddings for ''any'' application in computational pathology. Standard tile encoder-based pipelines, which extract embeddings of tiles stripped from their context, fail to model the rich slide-level information essential for both local and global tasks. Furthermore, different tile-encoders excel at different downstream tasks. Therefore, a unified model is needed to contextualize embeddings derived from ''any'' tile-level foundation model. TICON addresses this need with a single, shared encoder, pretrained using a masked modeling objective to simultaneously unify and contextualize representations from diverse tile-level pathology foundation models. Our experiments demonstrate that TICON-contextualized embeddings significantly improve performance across many different tasks, establishing new state-of-the-art results on tile-level benchmarks (i.e., HEST-Bench, THUNDER, CATCH) and slide-level benchmarks (i.e., Patho-Bench). Finally, we pretrain an aggregator on TICON to form a slide-level foundation model, using only 11K WSIs, outperforming SoTA slide-level foundation models pretrained with up to 350K WSIs.

