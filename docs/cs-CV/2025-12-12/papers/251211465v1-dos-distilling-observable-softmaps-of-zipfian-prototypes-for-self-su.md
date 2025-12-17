---
layout: default
title: DOS: Distilling Observable Softmaps of Zipfian Prototypes for Self-Supervised Point Representation
---

# DOS: Distilling Observable Softmaps of Zipfian Prototypes for Self-Supervised Point Representation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.11465" target="_blank" class="toolbar-btn">arXiv: 2512.11465v1</a>
    <a href="https://arxiv.org/pdf/2512.11465.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.11465v1" 
            onclick="toggleFavorite(this, '2512.11465v1', 'DOS: Distilling Observable Softmaps of Zipfian Prototypes for Self-Supervised Point Representation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Mohamed Abdelsamad, Michael Ulrich, Bin Yang, Miao Zhang, Yakov Miron, Abhinav Valada

**分类**: cs.CV, cs.LG

**发布日期**: 2025-12-12

**备注**: AAAI-26

---

## 💡 一句话要点

**DOS：通过Zipfian原型蒸馏可观测软标签，实现自监督点云表示学习**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `自监督学习` `点云表示` `语义分割` `3D目标检测` `Zipfian原型` `软标签蒸馏` `Sinkhorn算法`

## 📋 核心要点

1. 现有3D点云自监督学习方法面临几何结构不规则、易于产生捷径的重建以及语义分布不平衡等挑战。
2. DOS框架通过仅在可观测点上蒸馏语义相关性软标签，避免信息泄露，并利用Zipfian原型解决语义不平衡问题。
3. 实验表明，DOS在多个数据集的语义分割和3D目标检测任务上超越了现有最佳方法，无需额外数据或标注。

## 📝 摘要（中文）

本文提出了一种新的自监督学习框架DOS（Distilling Observable Softmaps），用于学习3D点云表示。该框架仅在可观测（未掩码）点上自蒸馏语义相关性软标签，避免了来自掩码区域的信息泄露，并提供了比离散token-to-prototype分配更丰富的监督信息。为了解决无监督环境下语义不平衡的挑战，我们引入了Zipfian原型，并使用改进的Sinkhorn-Knopp算法（Zipf-Sinkhorn）将其整合，该算法对原型使用强制执行幂律先验，并在训练期间调节目标软标签的锐度。在nuScenes、Waymo、SemanticKITTI、ScanNet和ScanNet200等多个基准测试中，DOS在语义分割和3D目标检测方面优于当前最先进的方法，且不依赖于额外的数据或标注。结果表明，可观测点软标签蒸馏为学习鲁棒的3D表示提供了一种可扩展且有效的范例。

## 🔬 方法详解

**问题定义**：现有的3D点云自监督学习方法在学习点云表示时，面临着三个主要问题：不规则的几何结构使得学习难度增加；重建任务容易学习到捷径，导致模型泛化能力差；以及数据集中普遍存在的语义不平衡问题，使得模型对少数类别的学习效果不佳。这些问题限制了自监督学习在3D点云领域的应用。

**核心思路**：DOS的核心思路是利用可观测点（即未被掩码的点）的语义相关性软标签进行自蒸馏。通过只关注可观测点，避免了从被掩码区域泄露信息，从而迫使模型学习更鲁棒的特征。此外，引入Zipfian原型来解决语义不平衡问题，通过调整原型的使用频率，使得模型能够更好地学习到各个类别的特征。

**技术框架**：DOS框架主要包含以下几个模块：1) 点云掩码模块，用于随机掩码部分点云；2) 特征提取模块，用于提取未掩码点云的特征；3) 原型学习模块，用于学习Zipfian原型；4) 软标签生成模块，基于特征和原型生成软标签；5) 蒸馏模块，利用可观测点的软标签进行自蒸馏学习。整个流程通过最小化蒸馏损失和原型损失来优化模型。

**关键创新**：DOS的关键创新在于两个方面：一是提出了可观测点软标签蒸馏策略，避免了信息泄露，提高了学习效率；二是引入了Zipfian原型和Zipf-Sinkhorn算法，有效地解决了语义不平衡问题。与现有方法相比，DOS能够学习到更鲁棒、更平衡的3D点云表示。

**关键设计**：Zipf-Sinkhorn算法是关键设计之一，它在标准的Sinkhorn-Knopp算法基础上，引入了幂律先验，用于控制原型的使用频率。具体来说，Zipf-Sinkhorn算法通过迭代地更新原型分配矩阵，使得原型的使用频率符合Zipf定律。此外，损失函数的设计也至关重要，DOS采用了交叉熵损失和KL散度损失相结合的方式，用于衡量预测软标签和目标软标签之间的差异。

## 📊 实验亮点

DOS在多个3D点云数据集上取得了显著的性能提升。例如，在SemanticKITTI数据集的语义分割任务中，DOS的mIoU指标超过了现有最佳方法。在nuScenes和Waymo数据集的3D目标检测任务中，DOS也取得了具有竞争力的结果，证明了其在不同场景下的泛化能力。重要的是，这些提升是在没有使用额外数据或标注的情况下实现的。

## 🎯 应用场景

DOS框架学习到的鲁棒3D点云表示，可广泛应用于自动驾驶、机器人导航、场景理解、三维重建等领域。通过自监督学习，减少了对人工标注数据的依赖，降低了模型训练成本。未来，该方法可以进一步扩展到其他3D数据类型，如网格、体素等，并与其他模态的数据进行融合，提升3D感知的性能。

## 📄 摘要（原文）

> Recent advances in self-supervised learning (SSL) have shown tremendous potential for learning 3D point cloud representations without human annotations. However, SSL for 3D point clouds still faces critical challenges due to irregular geometry, shortcut-prone reconstruction, and unbalanced semantics distribution. In this work, we propose DOS (Distilling Observable Softmaps), a novel SSL framework that self-distills semantic relevance softmaps only at observable (unmasked) points. This strategy prevents information leakage from masked regions and provides richer supervision than discrete token-to-prototype assignments. To address the challenge of unbalanced semantics in an unsupervised setting, we introduce Zipfian prototypes and incorporate them using a modified Sinkhorn-Knopp algorithm, Zipf-Sinkhorn, which enforces a power-law prior over prototype usage and modulates the sharpness of the target softmap during training. DOS outperforms current state-of-the-art methods on semantic segmentation and 3D object detection across multiple benchmarks, including nuScenes, Waymo, SemanticKITTI, ScanNet, and ScanNet200, without relying on extra data or annotations. Our results demonstrate that observable-point softmaps distillation offers a scalable and effective paradigm for learning robust 3D representations.

