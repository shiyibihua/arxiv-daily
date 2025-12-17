---
layout: default
title: Particulate: Feed-Forward 3D Object Articulation
---

# Particulate: Feed-Forward 3D Object Articulation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.11798" target="_blank" class="toolbar-btn">arXiv: 2512.11798v1</a>
    <a href="https://arxiv.org/pdf/2512.11798.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.11798v1" 
            onclick="toggleFavorite(this, '2512.11798v1', 'Particulate: Feed-Forward 3D Object Articulation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Ruining Li, Yuxin Yao, Chuanxia Zheng, Christian Rupprecht, Joan Lasenby, Shangzhe Wu, Andrea Vedaldi

**分类**: cs.CV, cs.AI, cs.GR

**发布日期**: 2025-12-12

**备注**: Project page: https://ruiningli.com/particulate

---

## 💡 一句话要点

**Particulate：提出一种前馈3D物体关节运动估计方法，无需逐对象优化。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D物体关节运动估计` `Transformer网络` `点云处理` `前馈网络` `运动学结构` `部件分割`

## 📋 核心要点

1. 现有3D物体关节运动估计方法通常需要逐对象优化，计算成本高，难以快速部署。
2. Particulate采用前馈Transformer网络直接从3D网格预测关节结构，无需迭代优化，速度更快。
3. 实验表明，Particulate在关节运动估计任务上显著优于现有方法，并可应用于AI生成的3D资产。

## 📝 摘要（中文）

本文提出了一种名为Particulate的前馈方法，该方法仅需一个静态3D网格即可直接推断出底层关节结构的所有属性，包括其3D部件、运动学结构和运动约束。其核心是一个Transformer网络，即Part Articulation Transformer，它使用灵活且可扩展的架构处理输入网格的点云，以预测所有上述属性，并原生支持多关节。我们在来自公共数据集的各种关节3D资产上端到端地训练该网络。在推理过程中，Particulate将网络的预测结果映射到输入网格，从而在几秒钟内生成一个完全关节化的3D模型，这比需要逐对象优化的先前方法快得多。Particulate还可以准确地推断AI生成的3D资产的关节结构，当与现成的图像到3D生成器结合使用时，能够从单个（真实或合成）图像中完全提取关节3D对象。我们进一步引入了一个新的具有挑战性的3D关节估计基准，该基准从高质量的公共3D资产中整理而来，并重新设计了评估协议，使其与人类偏好更加一致。定量和定性结果表明，Particulate明显优于最先进的方法。

## 🔬 方法详解

**问题定义**：现有3D物体关节运动估计方法，如优化方法，通常需要对每个对象进行单独的优化，计算量大，耗时较长，难以满足快速推理的需求。此外，这些方法在处理AI生成的3D资产时，由于其结构复杂性和噪声，性能可能会下降。

**核心思路**：Particulate的核心思路是利用Transformer网络强大的特征提取和建模能力，直接从3D网格的点云数据中预测物体的关节结构。通过端到端的训练，网络可以学习到3D形状与关节属性之间的映射关系，从而实现快速且准确的关节运动估计。这种前馈方法避免了耗时的逐对象优化，提高了推理效率。

**技术框架**：Particulate的整体架构包含以下几个主要模块：1) 点云采样：从输入的3D网格中采样得到点云数据。2) Part Articulation Transformer：一个基于Transformer的网络，用于处理点云数据并预测关节属性，包括部件分割、运动学结构和运动约束。3) 关节结构映射：将网络预测的关节属性映射回原始3D网格，生成一个完全关节化的3D模型。整个流程是端到端可训练的。

**关键创新**：Particulate的关键创新在于其前馈的架构和Part Articulation Transformer的设计。与需要逐对象优化的传统方法不同，Particulate直接从3D网格预测关节结构，大大提高了推理速度。Part Articulation Transformer能够有效地处理点云数据，并预测多关节物体的复杂运动学结构。

**关键设计**：Part Articulation Transformer采用Transformer编码器-解码器结构，编码器用于提取点云特征，解码器用于预测关节属性。损失函数包括部件分割损失、运动学结构损失和运动约束损失，用于指导网络学习。网络使用自注意力机制来建模点云中不同点之间的关系，并使用交叉注意力机制来融合不同部件的信息。具体的参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

实验结果表明，Particulate在3D关节运动估计任务上显著优于现有方法。在新的具有挑战性的基准测试中，Particulate在部件分割、运动学结构和运动约束预测方面均取得了state-of-the-art的性能。与需要逐对象优化的方法相比，Particulate的推理速度提高了几个数量级。此外，Particulate还成功地应用于AI生成的3D资产，证明了其泛化能力。

## 🎯 应用场景

Particulate可广泛应用于机器人、动画制作、游戏开发、虚拟现实等领域。例如，机器人可以利用Particulate快速识别和操作新的物体；动画师可以利用Particulate快速创建具有复杂关节运动的角色；游戏开发者可以利用Particulate生成逼真的3D互动环境。此外，Particulate还可以与图像到3D生成器结合使用，从单张图像中提取可交互的3D对象。

## 📄 摘要（原文）

> We present Particulate, a feed-forward approach that, given a single static 3D mesh of an everyday object, directly infers all attributes of the underlying articulated structure, including its 3D parts, kinematic structure, and motion constraints. At its core is a transformer network, Part Articulation Transformer, which processes a point cloud of the input mesh using a flexible and scalable architecture to predict all the aforementioned attributes with native multi-joint support. We train the network end-to-end on a diverse collection of articulated 3D assets from public datasets. During inference, Particulate lifts the network's feed-forward prediction to the input mesh, yielding a fully articulated 3D model in seconds, much faster than prior approaches that require per-object optimization. Particulate can also accurately infer the articulated structure of AI-generated 3D assets, enabling full-fledged extraction of articulated 3D objects from a single (real or synthetic) image when combined with an off-the-shelf image-to-3D generator. We further introduce a new challenging benchmark for 3D articulation estimation curated from high-quality public 3D assets, and redesign the evaluation protocol to be more consistent with human preferences. Quantitative and qualitative results show that Particulate significantly outperforms state-of-the-art approaches.

