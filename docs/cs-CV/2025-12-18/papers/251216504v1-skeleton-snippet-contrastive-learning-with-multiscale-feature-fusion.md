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

**关键词**: `骨骼动作定位` `对比学习` `自监督学习` `多尺度特征融合` `时间敏感特征`

## 📋 核心要点

1. 现有基于骨骼的动作定位方法缺乏对时间敏感特征的有效学习，难以准确检测动作边界。
2. 论文提出片段判别预训练任务，通过对比学习区分不同视频片段，学习时间敏感特征。
3. 采用U型模块融合多尺度特征，提升特征分辨率，并在BABEL和PKUMMD数据集上验证有效性。

## 📝 摘要（中文）

本文针对基于骨骼的动作定位任务，提出了一种自监督预训练范式，旨在学习更有效的3D动作表示。与视频级别的动作识别不同，动作定位需要对时间敏感的特征，以捕捉相邻帧之间细微的标签变化。为此，我们设计了一个片段判别预训练任务，将骨骼序列密集地投影到非重叠的片段中，并通过对比学习来区分不同视频中的片段。此外，我们利用U型模块融合中间特征，增强特征分辨率，从而提升帧级别的定位性能。实验结果表明，我们的方法在BABEL数据集上，针对不同的子集和评估协议，均能持续改进现有的基于骨骼的对比学习方法。通过在NTU RGB+D和BABEL数据集上进行预训练，我们在PKUMMD数据集上实现了最先进的迁移学习性能。

## 🔬 方法详解

**问题定义**：现有基于骨骼的动作定位方法在学习时间敏感特征方面存在不足，难以准确区分相邻帧之间细微的动作变化，导致动作边界检测不准确。现有的对比学习方法主要集中在视频级别的动作识别，缺乏对帧级别动作定位的优化。

**核心思路**：论文的核心思路是通过片段判别任务进行自监督预训练，学习对时间变化敏感的特征表示。通过将骨骼序列分割成多个非重叠的片段，并利用对比学习来区分不同视频中的片段，从而使模型能够捕捉到动作边界的细微变化。同时，通过多尺度特征融合增强特征分辨率，进一步提升定位精度。

**技术框架**：整体框架包含两个主要部分：片段判别预训练和多尺度特征融合。首先，将输入的骨骼序列分割成多个非重叠的片段。然后，利用编码器将每个片段映射到特征空间。接着，通过对比学习损失函数，鼓励模型区分不同视频中的片段。在下游任务中，利用预训练的编码器作为骨干网络，并添加U型模块进行多尺度特征融合，以增强特征分辨率。

**关键创新**：论文的关键创新在于提出了片段判别预训练任务，该任务专门为基于骨骼的动作定位设计，能够有效地学习时间敏感特征。与传统的视频级别对比学习方法不同，片段判别任务关注的是相邻帧之间的细微变化，从而更适合于动作定位任务。此外，多尺度特征融合模块也进一步提升了特征分辨率，增强了模型的定位能力。

**关键设计**：片段判别任务的关键在于如何选择合适的片段长度和对比学习策略。论文中采用了非重叠的片段分割方式，并使用InfoNCE损失函数进行对比学习。U型模块的关键在于如何选择合适的中间特征进行融合，以及如何设计融合的方式。具体的网络结构和参数设置在论文中有详细描述，但此处未提供具体数值。

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

实验结果表明，该方法在BABEL数据集上显著提升了现有基于骨骼的对比学习方法的动作定位性能。此外，通过在NTU RGB+D和BABEL数据集上进行预训练，该方法在PKUMMD数据集上实现了最先进的迁移学习性能，表明了其良好的泛化能力。具体的性能提升数据需要在论文中查找。

## 🎯 应用场景

该研究成果可应用于智能监控、人机交互、医疗康复等领域。例如，在智能监控中，可以利用该方法实现对异常行为的自动检测和定位；在医疗康复中，可以用于评估患者的运动功能和康复效果；在人机交互中，可以实现对人体动作的精确识别和理解。

## 📄 摘要（原文）

> The self-supervised pretraining paradigm has achieved great success in learning 3D action representations for skeleton-based action recognition using contrastive learning. However, learning effective representations for skeleton-based temporal action localization remains challenging and underexplored. Unlike video-level {action} recognition, detecting action boundaries requires temporally sensitive features that capture subtle differences between adjacent frames where labels change. To this end, we formulate a snippet discrimination pretext task for self-supervised pretraining, which densely projects skeleton sequences into non-overlapping segments and promotes features that distinguish them across videos via contrastive learning. Additionally, we build on strong backbones of skeleton-based action recognition models by fusing intermediate features with a U-shaped module to enhance feature resolution for frame-level localization. Our approach consistently improves existing skeleton-based contrastive learning methods for action localization on BABEL across diverse subsets and evaluation protocols. We also achieve state-of-the-art transfer learning performance on PKUMMD with pretraining on NTU RGB+D and BABEL.

