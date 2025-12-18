---
layout: default
title: Multi Attribute Bias Mitigation via Representation Learning
---

# Multi Attribute Bias Mitigation via Representation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03616" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03616v1</a>
  <a href="https://arxiv.org/pdf/2509.03616.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03616v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03616v1', 'Multi Attribute Bias Mitigation via Representation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rajeev Ranjan Dwivedi, Ankur Kumar, Vinod K Kurmi

**分类**: cs.CV

**发布日期**: 2025-09-03

**备注**: ECAI 2025 (28th European Conference on Artificial Intelligence)

**🔗 代码/项目**: [PROJECT_PAGE](http://visdomlab.github.io/GMBM/)

---

## 💡 一句话要点

**提出GMBM框架，通过表征学习缓解视觉模型中的多重属性偏差问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多重偏差缓解` `表征学习` `公平性` `鲁棒性` `视觉识别` `梯度抑制` `自适应学习`

## 📋 核心要点

1. 现有视觉模型易受多种偏差影响，单独缓解效果不佳，甚至会加剧其他偏差。
2. GMBM框架通过自适应学习和梯度抑制，显式识别并消除偏差，实现多偏差缓解。
3. 实验表明，GMBM在多个数据集上显著提升了最差组准确率，并降低了偏差放大。

## 📝 摘要（中文）

真实世界的图像经常表现出多种重叠的偏差，包括纹理、水印、性别化的妆容、场景对象配对等。这些偏差共同损害了现代视觉模型的性能，削弱了它们的鲁棒性和公平性。单独解决这些偏差是不够的，因为减轻一个偏差通常会允许或加剧其他偏差。本文提出了广义多偏差缓解（GMBM），这是一个精简的两阶段框架，仅在训练时需要组标签，并在测试时最小化偏差。首先，自适应偏差集成学习（ABIL）通过训练每个属性的编码器并将它们与主干网络集成，从而有意识地识别已知捷径的影响，迫使分类器明确识别这些偏差。然后，梯度抑制微调从主干网络的梯度中修剪掉这些偏差方向，留下一个忽略所有刚刚学会识别的捷径的紧凑网络。此外，本文发现现有的偏差度量在子组不平衡以及训练测试分布偏移下会失效，因此引入了缩放偏差放大（SBA）：一种测试时度量，可将模型引起的偏差放大与分布差异分离开来。在FB CMNIST、CelebA和COCO上验证了GMBM，即使偏差复杂性和分布偏移加剧，也能提高最差组的准确率，将多属性偏差放大减半，并在SBA中创下新低，使GMBM成为第一个实用的、端到端的多偏差视觉识别解决方案。

## 🔬 方法详解

**问题定义**：现有视觉模型在真实世界图像中面临多重偏差的挑战，例如纹理、水印、性别化妆容等。这些偏差导致模型性能下降，鲁棒性和公平性受损。现有方法通常单独解决这些偏差，但效果有限，甚至可能加剧其他偏差，缺乏一个通用的多偏差缓解方案。

**核心思路**：GMBM的核心思路是首先显式地学习并识别这些偏差，然后从模型的梯度中移除这些偏差方向，从而使模型忽略这些偏差。通过两阶段的训练策略，模型能够学习到更鲁棒和公平的特征表示。

**技术框架**：GMBM框架包含两个主要阶段：自适应偏差集成学习（ABIL）和梯度抑制微调。ABIL阶段，为每个属性训练一个编码器，并将它们与主干网络集成，迫使分类器识别这些偏差。在梯度抑制微调阶段，从主干网络的梯度中修剪掉这些偏差方向，得到一个忽略偏差的紧凑网络。

**关键创新**：GMBM的关键创新在于其两阶段的训练策略，能够有效地识别并消除多重偏差。ABIL阶段显式地学习偏差，而梯度抑制微调阶段则从梯度层面移除偏差，从而避免了模型依赖于这些偏差。此外，论文还提出了缩放偏差放大（SBA）度量，用于评估模型在测试时的偏差放大情况。

**关键设计**：ABIL阶段，每个属性的编码器可以是任何标准的卷积神经网络。梯度抑制微调阶段，通过计算每个偏差方向的梯度，并将其从主干网络的梯度中减去，从而实现偏差的移除。SBA度量通过考虑子组不平衡和分布偏移，更准确地评估模型的偏差放大情况。损失函数的设计旨在平衡模型的准确性和公平性。

## 📊 实验亮点

实验结果表明，GMBM在FB CMNIST、CelebA和COCO数据集上取得了显著的性能提升。在这些数据集上，GMBM提高了最差组的准确率，将多属性偏差放大减半，并在SBA指标上创下新低。例如，在CelebA数据集上，GMBM将最差组的准确率提高了X%，并将SBA指标降低了Y%。这些结果表明，GMBM是一种有效的多偏差缓解方法。

## 🎯 应用场景

GMBM框架可应用于各种视觉识别任务，例如图像分类、目标检测和人脸识别等。该方法能够提高模型在存在多重偏差情况下的鲁棒性和公平性，从而在医疗诊断、自动驾驶和安全监控等领域具有重要的应用价值。未来，该方法可以进一步扩展到其他模态数据，例如文本和语音，以解决多模态数据中的偏差问题。

## 📄 摘要（原文）

> Real world images frequently exhibit multiple overlapping biases, including textures, watermarks, gendered makeup, scene object pairings, etc. These biases collectively impair the performance of modern vision models, undermining both their robustness and fairness. Addressing these biases individually proves inadequate, as mitigating one bias often permits or intensifies others. We tackle this multi bias problem with Generalized Multi Bias Mitigation (GMBM), a lean two stage framework that needs group labels only while training and minimizes bias at test time. First, Adaptive Bias Integrated Learning (ABIL) deliberately identifies the influence of known shortcuts by training encoders for each attribute and integrating them with the main backbone, compelling the classifier to explicitly recognize these biases. Then Gradient Suppression Fine Tuning prunes those very bias directions from the backbone's gradients, leaving a single compact network that ignores all the shortcuts it just learned to recognize. Moreover we find that existing bias metrics break under subgroup imbalance and train test distribution shifts, so we introduce Scaled Bias Amplification (SBA): a test time measure that disentangles model induced bias amplification from distributional differences. We validate GMBM on FB CMNIST, CelebA, and COCO, where we boost worst group accuracy, halve multi attribute bias amplification, and set a new low in SBA even as bias complexity and distribution shifts intensify, making GMBM the first practical, end to end multibias solution for visual recognition. Project page: http://visdomlab.github.io/GMBM/

