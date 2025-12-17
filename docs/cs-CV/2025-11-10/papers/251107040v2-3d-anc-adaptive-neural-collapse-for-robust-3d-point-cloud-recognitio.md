---
layout: default
title: 3D-ANC: Adaptive Neural Collapse for Robust 3D Point Cloud Recognition
---

# 3D-ANC: Adaptive Neural Collapse for Robust 3D Point Cloud Recognition

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.07040" target="_blank" class="toolbar-btn">arXiv: 2511.07040v2</a>
    <a href="https://arxiv.org/pdf/2511.07040.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.07040v2" 
            onclick="toggleFavorite(this, '2511.07040v2', '3D-ANC: Adaptive Neural Collapse for Robust 3D Point Cloud Recognition')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yuanmin Huang, Wenxuan Li, Mi Zhang, Xiaohan Zhang, Xiaoyu You, Min Yang

**分类**: cs.CV, cs.CR

**发布日期**: 2025-11-10 (更新: 2025-12-08)

**备注**: AAAI 2026

---

## 💡 一句话要点

**提出3D-ANC，利用神经崩溃机制提升3D点云识别的鲁棒性，对抗恶意攻击。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D点云识别` `对抗攻击` `神经崩溃` `鲁棒性` `特征解耦`

## 📋 核心要点

1. 现有3D点云识别模型易受对抗攻击影响，传统防御方法因特征空间纠缠而效果不佳。
2. 提出3D-ANC，利用神经崩溃（NC）机制，通过ETF对齐和自适应训练，解耦特征空间。
3. 实验表明，3D-ANC显著提升了模型在对抗攻击下的鲁棒性，例如DGCNN在ModelNet40上的精度提升了53.7%。

## 📝 摘要（中文）

深度神经网络在3D点云识别方面取得了显著进展，但其对对抗扰动的脆弱性给实际部署带来了严重的安全挑战。传统的防御机制难以应对不断演变的多方面攻击模式。通过对现有防御措施的系统分析，我们发现其性能不佳的主要原因是特征空间纠缠，导致容易进行对抗攻击。为此，我们提出了3D-ANC，一种利用神经崩溃（NC）机制来协调判别性特征学习的新方法。NC描述了最后一层特征和分类器权重共同演变为单纯形等角紧框架（ETF）排列，从而建立最大程度可分离的类原型。然而，在3D识别中利用这种优势面临两个重大挑战：（1）点云数据集中普遍存在的类别不平衡，以及（2）对象类别之间复杂的几何相似性。为了解决这些障碍，我们的解决方案将ETF对齐的分类模块与自适应训练框架相结合，该框架包括表示平衡学习（RBL）和动态特征方向损失（FDL）。3D-ANC无缝地增强了现有模型，使其能够在3D数据分布的复杂性下开发解耦的特征空间。综合评估表明，3D-ANC显著提高了具有各种结构的模型的鲁棒性。例如，在ModelNet40上，DGCNN的分类精度从27.2%提高到80.9%，绝对增益为53.7%，超过了领先的基线34.0%。

## 🔬 方法详解

**问题定义**：现有的3D点云识别模型在面对对抗攻击时表现出脆弱性，即使是微小的扰动也可能导致模型性能急剧下降。传统的防御方法往往难以有效应对不断涌现的各种攻击策略，其根本原因在于模型学习到的特征表示是纠缠的，不同类别的特征混杂在一起，使得攻击者更容易找到有效的对抗样本。

**核心思路**：本文的核心思路是利用神经崩溃（Neural Collapse, NC）现象来解耦特征空间，提高模型的鲁棒性。NC理论表明，在训练的最后阶段，最后一层特征和分类器权重会收敛到一种特殊的结构，即单纯形等角紧框架（Simplex Equiangular Tight Frame, ETF）。这种结构具有最大程度的可分离性，可以有效区分不同的类别。通过引导模型学习到这种ETF结构，可以提高模型对对抗攻击的抵抗能力。

**技术框架**：3D-ANC主要包含两个核心模块：ETF对齐的分类模块和自适应训练框架。ETF对齐的分类模块旨在将最后一层的特征和分类器权重推向ETF结构。自适应训练框架则包含表示平衡学习（Representation-Balanced Learning, RBL）和动态特征方向损失（Dynamic Feature Direction Loss, FDL）。RBL用于解决点云数据集中常见的类别不平衡问题，FDL用于进一步约束特征的方向，使其更加具有判别性。整个训练过程是一个迭代优化的过程，通过不断调整模型的参数，使其逐渐收敛到期望的ETF结构。

**关键创新**：该论文的关键创新在于将神经崩溃理论应用于3D点云识别领域，并针对3D数据的特点，提出了RBL和FDL两种自适应训练策略。与传统的防御方法相比，3D-ANC不是直接对抗对抗样本，而是通过优化特征空间的结构，提高模型的内在鲁棒性。这种方法更加通用，可以有效应对各种类型的对抗攻击。

**关键设计**：在ETF对齐的分类模块中，使用了余弦相似度作为特征和权重之间的距离度量，并设计了相应的损失函数来引导模型学习ETF结构。RBL通过调整不同类别的样本权重，平衡了不同类别对损失函数的贡献。FDL则通过计算特征方向之间的夹角，并惩罚夹角过小的特征，从而提高了特征的判别性。具体的损失函数形式和参数设置在论文中有详细描述。

## 📊 实验亮点

实验结果表明，3D-ANC能够显著提高3D点云识别模型在对抗攻击下的鲁棒性。在ModelNet40数据集上，DGCNN模型的分类精度从27.2%提升到80.9%，绝对增益高达53.7%，超过了现有最佳基线方法34.0%。此外，3D-ANC还能够有效提高其他模型的鲁棒性，例如PointNet和PointNet++。

## 🎯 应用场景

该研究成果可广泛应用于对安全性要求较高的3D点云识别场景，例如自动驾驶、机器人导航、安防监控等。通过提高模型对对抗攻击的鲁棒性，可以有效防止恶意攻击者篡改识别结果，保障系统的安全稳定运行。未来，该方法还可以扩展到其他类型的3D数据处理任务中，例如3D目标检测、3D场景分割等。

## 📄 摘要（原文）

> Deep neural networks have recently achieved notable progress in 3D point cloud recognition, yet their vulnerability to adversarial perturbations poses critical security challenges in practical deployments. Conventional defense mechanisms struggle to address the evolving landscape of multifaceted attack patterns. Through systematic analysis of existing defenses, we identify that their unsatisfactory performance primarily originates from an entangled feature space, where adversarial attacks can be performed easily. To this end, we present 3D-ANC, a novel approach that capitalizes on the Neural Collapse (NC) mechanism to orchestrate discriminative feature learning. In particular, NC depicts where last-layer features and classifier weights jointly evolve into a simplex equiangular tight frame (ETF) arrangement, establishing maximally separable class prototypes. However, leveraging this advantage in 3D recognition confronts two substantial challenges: (1) prevalent class imbalance in point cloud datasets, and (2) complex geometric similarities between object categories. To tackle these obstacles, our solution combines an ETF-aligned classification module with an adaptive training framework consisting of representation-balanced learning (RBL) and dynamic feature direction loss (FDL). 3D-ANC seamlessly empowers existing models to develop disentangled feature spaces despite the complexity in 3D data distribution. Comprehensive evaluations state that 3D-ANC significantly improves the robustness of models with various structures on two datasets. For instance, DGCNN's classification accuracy is elevated from 27.2% to 80.9% on ModelNet40 -- a 53.7% absolute gain that surpasses leading baselines by 34.0%.

