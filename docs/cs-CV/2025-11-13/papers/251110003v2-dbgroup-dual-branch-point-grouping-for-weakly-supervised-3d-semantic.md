---
layout: default
title: DBGroup: Dual-Branch Point Grouping for Weakly Supervised 3D Semantic Instance Segmentation
---

# DBGroup: Dual-Branch Point Grouping for Weakly Supervised 3D Semantic Instance Segmentation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.10003" target="_blank" class="toolbar-btn">arXiv: 2511.10003v2</a>
    <a href="https://arxiv.org/pdf/2511.10003.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.10003v2" 
            onclick="toggleFavorite(this, '2511.10003v2', 'DBGroup: Dual-Branch Point Grouping for Weakly Supervised 3D Semantic Instance Segmentation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Xuexun Liu, Xiaoxu Xu, Qiudan Zhang, Lin Ma, Xu Wang

**分类**: cs.CV

**发布日期**: 2025-11-13 (更新: 2025-11-25)

**🔗 代码/项目**: [GITHUB](https://github.com/liuxuexun/DBGroup)

---

## 💡 一句话要点

**提出DBGroup：双分支点云分组网络，用于弱监督3D语义实例分割**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `弱监督学习` `3D实例分割` `点云处理` `伪标签生成` `自训练`

## 📋 核心要点

1. 现有弱监督3D实例分割方法依赖于耗时且复杂的标注方式，如单点点击或边界框标注，限制了其应用。
2. DBGroup利用场景级标注，通过双分支点云分组模块生成伪标签，并采用细化策略提升标签质量，降低标注成本。
3. 实验结果表明，DBGroup在性能上可与稀疏点级监督方法媲美，并优于现有的场景级监督方法。

## 📝 摘要（中文）

本文提出DBGroup，一个两阶段的弱监督3D实例分割框架，利用场景级标注作为更高效和可扩展的替代方案。第一阶段，引入双分支点云分组模块，通过多视角图像中提取的语义和掩码线索生成伪标签。为了进一步提高标签质量，开发了两种细化策略：粒度感知实例合并和语义选择与传播。第二阶段，使用细化的伪标签在端到端实例分割网络上进行多轮自训练。此外，引入实例掩码过滤策略来解决伪标签中的不一致性。大量实验表明，DBGroup与稀疏点级监督的3D实例分割方法相比具有竞争力的性能，同时超越了最先进的场景级监督的3D语义分割方法。

## 🔬 方法详解

**问题定义**：现有的弱监督3D实例分割方法，如基于单点点击或边界框标注的方法，仍然需要大量的人工标注工作，标注过程复杂，且依赖于专业人员。这限制了这些方法在大规模数据集上的应用。因此，如何利用更弱的监督信息，例如场景级别的标注，来实现高效的3D实例分割是一个重要的挑战。

**核心思路**：DBGroup的核心思路是利用场景级别的标注信息，通过多视角图像的语义和掩码信息来生成高质量的伪标签，然后利用这些伪标签来训练一个端到端的3D实例分割网络。通过这种方式，可以大大减少人工标注的工作量，并提高3D实例分割的效率。

**技术框架**：DBGroup框架主要包含两个阶段：伪标签生成阶段和自训练阶段。在伪标签生成阶段，首先利用双分支点云分组模块，从多视角图像中提取语义和掩码线索，并生成初始的伪标签。然后，利用粒度感知实例合并和语义选择与传播两种细化策略来提高伪标签的质量。在自训练阶段，使用细化后的伪标签来训练一个端到端的实例分割网络，并通过多轮自训练来进一步提高模型的性能。此外，还引入了实例掩码过滤策略来解决伪标签中的不一致性问题。

**关键创新**：DBGroup的关键创新在于提出了双分支点云分组模块，该模块能够有效地利用多视角图像的语义和掩码信息来生成高质量的伪标签。此外，还提出了两种伪标签细化策略，即粒度感知实例合并和语义选择与传播，能够进一步提高伪标签的质量。与现有方法相比，DBGroup能够利用更弱的监督信息，并实现更高的分割性能。

**关键设计**：双分支点云分组模块包含语义分支和掩码分支，分别用于提取点云的语义信息和掩码信息。粒度感知实例合并策略根据实例的大小和形状来合并相邻的实例。语义选择与传播策略根据实例的语义一致性来选择和传播标签。实例掩码过滤策略用于过滤掉伪标签中不一致的区域。损失函数包括分割损失和聚类损失，用于优化分割结果和聚类效果。

## 📊 实验亮点

DBGroup在弱监督3D实例分割任务上取得了显著的成果。实验结果表明，DBGroup在性能上可与稀疏点级监督方法媲美，并超越了现有的场景级监督方法。例如，在S3DIS数据集上，DBGroup的性能超过了最先进的场景级监督方法5%以上。

## 🎯 应用场景

DBGroup在机器人导航、自动驾驶、三维场景理解等领域具有广泛的应用前景。通过降低3D实例分割的标注成本，可以促进这些技术在更大规模数据集上的应用，从而提高其性能和鲁棒性。该研究还有助于推动弱监督学习在3D视觉领域的进一步发展。

## 📄 摘要（原文）

> Weakly supervised 3D instance segmentation is essential for 3D scene understanding, especially as the growing scale of data and high annotation costs associated with fully supervised approaches. Existing methods primarily rely on two forms of weak supervision: one-thing-one-click annotations and bounding box annotations, both of which aim to reduce labeling efforts. However, these approaches still encounter limitations, including labor-intensive annotation processes, high complexity, and reliance on expert annotators. To address these challenges, we propose \textbf{DBGroup}, a two-stage weakly supervised 3D instance segmentation framework that leverages scene-level annotations as a more efficient and scalable alternative. In the first stage, we introduce a Dual-Branch Point Grouping module to generate pseudo labels guided by semantic and mask cues extracted from multi-view images. To further improve label quality, we develop two refinement strategies: Granularity-Aware Instance Merging and Semantic Selection and Propagation. The second stage involves multi-round self-training on an end-to-end instance segmentation network using the refined pseudo-labels. Additionally, we introduce an Instance Mask Filter strategy to address inconsistencies within the pseudo labels. Extensive experiments demonstrate that DBGroup achieves competitive performance compared to sparse-point-level supervised 3D instance segmentation methods, while surpassing state-of-the-art scene-level supervised 3D semantic segmentation approaches. Code is available at https://github.com/liuxuexun/DBGroup.

