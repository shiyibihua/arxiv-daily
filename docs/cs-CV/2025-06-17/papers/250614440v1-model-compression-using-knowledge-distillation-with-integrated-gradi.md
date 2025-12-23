---
layout: default
title: Model compression using knowledge distillation with integrated gradients
---

# Model compression using knowledge distillation with integrated gradients

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14440" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14440v1</a>
  <a href="https://arxiv.org/pdf/2506.14440.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14440v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14440v1', 'Model compression using knowledge distillation with integrated gradients')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: David E. Hernandez, Jose Chang, Torbjörn E. M. Nordling

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-06-17

**备注**: 49 pages, 12 figures

---

## 💡 一句话要点

**提出基于集成梯度的知识蒸馏方法以实现模型压缩**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `模型压缩` `知识蒸馏` `集成梯度` `深度学习` `数据增强` `边缘计算` `CIFAR-10` `推理效率`

## 📋 核心要点

1. 现有模型压缩方法在资源受限设备上部署深度学习模型时面临准确率与效率的权衡挑战。
2. 本文提出通过集成梯度增强知识蒸馏，利用IG图作为数据增强策略，提升学生模型对教师模型决策的理解。
3. 实验结果显示，IG增强的知识蒸馏在CIFAR-10上实现92.6%的准确率，压缩因子4.1x，相较于未蒸馏模型提升1.1个百分点。

## 📝 摘要（中文）

模型压缩对于在资源受限设备上部署深度学习模型至关重要。本文提出了一种新颖的方法，通过集成梯度（IG）增强知识蒸馏，作为数据增强策略。在训练过程中，我们将IG图叠加到输入图像上，使学生模型更深入地理解教师模型的决策过程。在CIFAR-10上的广泛评估表明，IG增强的知识蒸馏实现了92.6%的测试准确率，压缩因子为4.1x，相较于未蒸馏模型（91.5%）有显著提升（p<0.001）。该方法将推理时间从140毫秒减少到13毫秒，并将IG图的预计算转化为一次性预处理步骤。综合实验包括与注意力转移的比较、蒙特卡洛模拟的统计稳健性验证、压缩因子与准确率的系统评估，以及在与CIFAR-10类对齐的ImageNet子集上的验证，证明了该方法的广泛适用性。

## 🔬 方法详解

**问题定义**：本文旨在解决在资源受限设备上部署深度学习模型时，模型准确率与推理效率之间的矛盾。现有的模型压缩方法往往无法在保持高准确率的同时实现显著的压缩效果。

**核心思路**：我们提出了一种基于集成梯度（IG）的知识蒸馏方法，通过将IG图叠加到输入图像上，增强学生模型对教师模型决策过程的理解，从而提升模型性能。

**技术框架**：整体方法包括两个主要阶段：首先，在训练前预计算IG图；其次，在训练过程中将IG图作为数据增强输入到学生模型中。这一流程使得学生模型能够更好地学习教师模型的知识。

**关键创新**：本研究的主要创新在于将集成梯度与知识蒸馏相结合，利用IG图作为数据增强手段，显著提升了模型的压缩效果和准确率。这一方法与传统的知识蒸馏方法相比，提供了更深入的模型理解。

**关键设计**：在实验中，我们设置了不同的压缩因子，并使用了交叉熵损失函数来优化学生模型。同时，采用了多种网络结构进行验证，以确保方法的广泛适用性。

## 📊 实验亮点

实验结果表明，IG增强的知识蒸馏方法在CIFAR-10数据集上达到了92.6%的测试准确率，压缩因子为4.1x，相较于未蒸馏模型提升了1.1个百分点（p<0.001），并将推理时间从140毫秒减少到13毫秒，展现了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括移动设备、物联网设备及边缘计算等资源受限环境。通过有效的模型压缩，能够在保证模型性能的同时，显著降低计算和存储需求，推动深度学习技术在实际应用中的普及与发展。

## 📄 摘要（原文）

> Model compression is critical for deploying deep learning models on resource-constrained devices. We introduce a novel method enhancing knowledge distillation with integrated gradients (IG) as a data augmentation strategy. Our approach overlays IG maps onto input images during training, providing student models with deeper insights into teacher models' decision-making processes. Extensive evaluation on CIFAR-10 demonstrates that our IG-augmented knowledge distillation achieves 92.6% testing accuracy with a 4.1x compression factor-a significant 1.1 percentage point improvement ($p<0.001$) over non-distilled models (91.5%). This compression reduces inference time from 140 ms to 13 ms. Our method precomputes IG maps before training, transforming substantial runtime costs into a one-time preprocessing step. Our comprehensive experiments include: (1) comparisons with attention transfer, revealing complementary benefits when combined with our approach; (2) Monte Carlo simulations confirming statistical robustness; (3) systematic evaluation of compression factor versus accuracy trade-offs across a wide range (2.2x-1122x); and (4) validation on an ImageNet subset aligned with CIFAR-10 classes, demonstrating generalisability beyond the initial dataset. These extensive ablation studies confirm that IG-based knowledge distillation consistently outperforms conventional approaches across varied architectures and compression ratios. Our results establish this framework as a viable compression technique for real-world deployment on edge devices while maintaining competitive accuracy.

