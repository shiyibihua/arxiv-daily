---
layout: default
title: Skeleton-Snippet Contrastive Learning with Multiscale Feature Fusion for Action Localization
---

# Skeleton-Snippet Contrastive Learning with Multiscale Feature Fusion for Action Localization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16504" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16504v1</a>
  <a href="https://arxiv.org/pdf/2512.16504.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16504v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16504v1', 'Skeleton-Snippet Contrastive Learning with Multiscale Feature Fusion for Action Localization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qiushuo Cheng, Jingjing Liu, Catherine Morgan, Alan Whone, Majid Mirmehdi

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出基于骨骼片段对比学习和多尺度特征融合的动作定位方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `骨骼动作识别` `动作定位` `对比学习` `自监督学习` `多尺度特征融合`

## 📋 核心要点

1. 基于骨骼的动作定位需要捕捉帧间细微差异，现有方法难以有效学习时间敏感特征。
2. 提出片段判别预训练任务，通过对比学习区分不同视频片段，学习更具区分性的特征。
3. 利用U型模块融合多尺度特征，提升特征分辨率，从而改善帧级别动作定位性能。

## 📝 摘要（中文）

本文针对基于骨骼的动作定位任务，提出了一种自监督预训练范式。不同于视频级别的动作识别，动作定位需要对时间敏感的特征，以捕捉相邻帧之间细微的标签变化。为此，我们设计了一个片段判别预训练任务，将骨骼序列密集地投影到非重叠的片段中，并通过对比学习来区分不同视频中的片段特征。此外，我们利用U型模块融合中间特征，增强特征分辨率，从而提升帧级别的定位性能。实验结果表明，我们的方法在BABEL数据集上持续改进了现有的基于骨骼的对比学习方法，并在PKUMMD数据集上实现了最先进的迁移学习性能，预训练数据为NTU RGB+D和BABEL。

## 🔬 方法详解

**问题定义**：论文旨在解决基于骨骼的动作定位问题。现有方法，特别是基于对比学习的方法，在视频级别的动作识别上取得了成功，但直接应用于动作定位时，无法有效捕捉帧与帧之间的细微时间差异，导致定位精度不高。现有方法缺乏对时间敏感特征的有效学习机制。

**核心思路**：论文的核心思路是通过片段判别任务进行自监督预训练，使模型能够学习区分不同时间片段的特征。通过对比学习，模型被训练成能够区分来自不同视频的片段，从而学习到更具区分性的、对时间变化敏感的特征表示。此外，通过融合多尺度特征，增强特征的分辨率，进一步提升定位精度。

**技术框架**：整体框架包含两个主要部分：片段判别预训练和多尺度特征融合。在预训练阶段，输入骨骼序列被分割成非重叠的片段，然后通过编码器提取特征。对比学习模块用于训练模型区分不同视频的片段。在特征融合阶段，使用U型模块融合来自不同层的中间特征，以增强特征的分辨率。最终，融合后的特征被用于帧级别的动作定位。

**关键创新**：论文的关键创新在于提出了片段判别预训练任务，这是一种专门为动作定位设计的自监督学习方法。与传统的视频级别对比学习不同，片段判别任务更加关注局部时间信息，能够更好地捕捉动作边界。此外，多尺度特征融合进一步提升了特征的分辨率，使得模型能够更精确地定位动作。

**关键设计**：片段的划分方式采用非重叠分割，保证了片段之间的独立性。对比学习损失函数采用InfoNCE损失，鼓励模型将来自同一视频的片段拉近，将来自不同视频的片段推远。U型模块的具体结构可以根据不同的骨骼动作识别模型进行调整，通常包含卷积层、池化层和上采样层等。具体的参数设置和损失函数权重需要根据实验结果进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16504v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16504v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16504v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该方法在BABEL数据集上，相较于现有基于骨骼的对比学习方法，在动作定位任务上取得了持续改进。此外，在PKUMMD数据集上，通过在NTU RGB+D和BABEL数据集上进行预训练，实现了最先进的迁移学习性能。这些结果表明，该方法能够有效学习动作定位所需的特征表示，并具有良好的泛化能力。

## 🎯 应用场景

该研究成果可应用于智能监控、人机交互、康复训练等领域。例如，在智能监控中，可以利用该方法自动检测异常行为；在人机交互中，可以识别用户的动作意图；在康复训练中，可以评估患者的运动能力。该研究有助于提升相关系统的智能化水平和用户体验。

## 📄 摘要（原文）

> The self-supervised pretraining paradigm has achieved great success in learning 3D action representations for skeleton-based action recognition using contrastive learning. However, learning effective representations for skeleton-based temporal action localization remains challenging and underexplored. Unlike video-level {action} recognition, detecting action boundaries requires temporally sensitive features that capture subtle differences between adjacent frames where labels change. To this end, we formulate a snippet discrimination pretext task for self-supervised pretraining, which densely projects skeleton sequences into non-overlapping segments and promotes features that distinguish them across videos via contrastive learning. Additionally, we build on strong backbones of skeleton-based action recognition models by fusing intermediate features with a U-shaped module to enhance feature resolution for frame-level localization. Our approach consistently improves existing skeleton-based contrastive learning methods for action localization on BABEL across diverse subsets and evaluation protocols. We also achieve state-of-the-art transfer learning performance on PKUMMD with pretraining on NTU RGB+D and BABEL.

