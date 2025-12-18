---
layout: default
title: Training Matryoshka Mixture-of-Experts for Elastic Inference-Time Expert Utilization
---

# Training Matryoshka Mixture-of-Experts for Elastic Inference-Time Expert Utilization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26520" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26520v1</a>
  <a href="https://arxiv.org/pdf/2509.26520.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26520v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26520v1', 'Training Matryoshka Mixture-of-Experts for Elastic Inference-Time Expert Utilization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yaoxiang Wang, Qingguo Hu, Yucheng Ding, Ruizhe Wang, Yeyun Gong, Jian Jiao, Yelong Shen, Peng Cheng, Jinsong Su

**分类**: cs.CL

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出Matryoshka MoE，实现MoE模型在推理时专家利用的弹性调整**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家模型` `弹性推理` `模型训练` `模型压缩` `大语言模型`

## 📋 核心要点

1. 现有MoE模型采用Top-K路由，推理时专家数量调整会导致性能急剧下降，缺乏弹性。
2. M-MoE通过训练时专家数量随机化，使模型学习粗到细的专家排序，实现弹性推理。
3. 实验表明，M-MoE模型在不同专家数量下性能接近专门训练的模型，显著降低训练成本。

## 📝 摘要（中文）

混合专家模型(MoE)已成为有效扩展大型语言模型的一种有前景的范例，它无需成比例地增加计算成本。然而，Top-K路由器的标准训练策略阻碍了MoE模型充分发挥其弹性推理的潜力。当在推理时改变激活专家的数量时，这些模型会表现出急剧的性能下降。本文介绍Matryoshka MoE (M-MoE)，一个训练框架，将粗到细的结构直接灌输到专家集成中。通过在训练期间系统地改变激活专家的数量，M-MoE迫使模型学习有意义的排序：排名靠前的专家协同提供必要的、粗粒度的能力，而随后的专家逐步添加更细粒度的细节。我们在多个粒度上探索了这一原则，确定了一种逐层随机化策略是最有效的。实验表明，单个M-MoE模型实现了卓越的弹性，其在各种专家数量下的性能与整个专家模型套件的性能非常匹配，但仅需总训练成本的一小部分。这种灵活性不仅解锁了弹性推理，而且还能够通过为不同的模型层分配不同的计算预算来优化性能。这项工作为大规模MoE模型更实用和更具适应性的部署铺平了道路。

## 🔬 方法详解

**问题定义**：现有MoE模型在训练时通常采用固定的Top-K路由策略，导致模型过度依赖于特定数量的专家组合。当在推理阶段需要调整激活的专家数量时（例如，为了适应不同的计算资源限制），模型的性能会显著下降，无法实现真正的弹性推理。现有方法的痛点在于缺乏对专家重要性的排序和对不同专家组合的适应能力。

**核心思路**：M-MoE的核心思路是在训练过程中引入专家数量的随机性，迫使模型学习一种粗到细的专家结构。排名靠前的专家提供核心功能，后续专家逐步添加细节。通过这种方式，模型能够适应不同数量的激活专家，并在各种计算预算下保持良好的性能。这种设计借鉴了俄罗斯套娃（Matryoshka）的概念，每一层都包含更精细的信息。

**技术框架**：M-MoE的整体框架与标准的MoE模型类似，主要区别在于训练阶段。在每个训练步骤中，M-MoE随机选择一个激活专家数量K，然后使用Top-K路由选择K个专家进行计算。通过在不同的层使用不同的K值，可以进一步增强模型的弹性。模型的其他部分，如路由网络和专家网络，可以采用现有的MoE架构。

**关键创新**：M-MoE最重要的创新点在于其训练策略，即在训练过程中随机改变激活专家的数量。这种策略迫使模型学习一种专家重要性的排序，使得模型能够适应不同的计算预算，并在各种专家数量下保持良好的性能。与现有方法相比，M-MoE不需要为每种专家数量训练单独的模型，从而显著降低了训练成本。

**关键设计**：M-MoE的关键设计包括：1) 逐层随机化策略，即在不同的模型层使用不同的激活专家数量，以进一步增强模型的弹性；2) 激活专家数量的采样策略，例如均匀采样或基于某种分布进行采样；3) 损失函数的设计，需要确保模型在各种专家数量下都能学习到有效的表示。

## 📊 实验亮点

实验结果表明，单个M-MoE模型在不同专家数量下的性能与专门训练的模型套件的性能非常接近，但训练成本仅为后者的几分之一。例如，在某个具体任务上，M-MoE模型在激活不同数量的专家时，性能下降幅度远小于传统的MoE模型，并且能够达到与专门训练的模型相当的精度。这证明了M-MoE在实现弹性推理方面的有效性。

## 🎯 应用场景

M-MoE具有广泛的应用前景，例如在资源受限的设备上部署大型语言模型、根据用户需求动态调整模型计算量、以及在云端提供弹性推理服务。该技术可以显著降低MoE模型的部署成本，并提高其在实际应用中的灵活性和适应性。未来，M-MoE可以与其他模型压缩技术相结合，进一步优化模型的性能和效率。

## 📄 摘要（原文）

> Mixture-of-Experts (MoE) has emerged as a promising paradigm for efficiently scaling large language models without a proportional increase in computational cost. However, the standard training strategy of Top-K router prevents MoE models from realizing their full potential for elastic inference. When the number of activated experts is altered at inference time, these models exhibit precipitous performance degradation. In this work, we introduce Matryoshka MoE (M-MoE), a training framework that instills a coarse-to-fine structure directly into the expert ensemble. By systematically varying the number of activated experts during training, M-MoE compels the model to learn a meaningful ranking: top-ranked experts collaborate to provide essential, coarse-grained capabilities, while subsequent experts add progressively finer-grained detail. We explore this principle at multiple granularities, identifying a layer-wise randomization strategy as the most effective. Our experiments demonstrate that a single M-MoE model achieves remarkable elasticity, with its performance at various expert counts closely matching that of an entire suite of specialist models, but at only a fraction of the total training cost. This flexibility not only unlocks elastic inference but also enables optimizing performance by allocating different computational budgets to different model layers. Our work paves the way for more practical and adaptable deployments of large-scale MoE models.

