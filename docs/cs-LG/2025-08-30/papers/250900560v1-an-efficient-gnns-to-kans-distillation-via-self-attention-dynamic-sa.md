---
layout: default
title: An Efficient GNNs-to-KANs Distillation via Self-Attention Dynamic Sampling with Potential for Consumer Electronics Edge Deployment
---

# An Efficient GNNs-to-KANs Distillation via Self-Attention Dynamic Sampling with Potential for Consumer Electronics Edge Deployment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00560" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00560v1</a>
  <a href="https://arxiv.org/pdf/2509.00560.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00560v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00560v1', 'An Efficient GNNs-to-KANs Distillation via Self-Attention Dynamic Sampling with Potential for Consumer Electronics Edge Deployment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Can Cui, Zilong Fu, Penghe Huang, Yuanyuan Li, Wu Deng, Dongyan Li

**分类**: cs.LG, cs.PF

**发布日期**: 2025-08-30

---

## 💡 一句话要点

**提出SA-DSD框架以提升GNN知识蒸馏至KAN的效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `知识蒸馏` `图神经网络` `Kolmogorov-Arnold网络` `自注意力机制` `动态采样` `边缘计算` `模型压缩`

## 📋 核心要点

1. 现有的多层感知器（MLP）在捕捉GNN学习的复杂邻域依赖性方面存在局限，影响了其在边缘环境中的性能。
2. 本文提出的SA-DSD框架通过动态采样和自注意力机制，优化了GNN到KAN的知识蒸馏过程，提升了模型的表达能力。
3. 实验结果显示，SA-DSD在六个真实数据集上相较于GNN教师模型提升了3.05%-3.62%的性能，并在参数数量和推理时间上有显著减少。

## 📝 摘要（中文）

知识蒸馏（KD）在资源受限的边缘环境中部署深度学习模型至关重要，尤其是在消费电子领域。本文提出了一种创新的知识蒸馏框架——自注意力动态采样蒸馏（SA-DSD），旨在将图神经网络（GNN）中的知识有效转移至更高效的Kolmogorov-Arnold网络（KAN）。通过引入可学习的频率基和相位偏移机制，FR-KAN显著提高了非线性拟合能力并降低了计算复杂度。实验结果表明，SA-DSD在多个数据集上显著提升了模型性能，并在参数数量和推理时间上实现了显著优化。

## 🔬 方法详解

**问题定义**：本文旨在解决多层感知器（MLP）在捕捉图神经网络（GNN）复杂邻域依赖性方面的不足，导致其在边缘计算环境中的性能受限。

**核心思路**：通过引入自注意力机制和动态采样，构建自注意力动态采样蒸馏（SA-DSD）框架，旨在有效转移GNN的知识至更高效的Kolmogorov-Arnold网络（KAN）。

**技术框架**：SA-DSD框架包括教师模型（GNN）、学生模型（FR-KAN+）、动态采样概率矩阵和自适应加权损失机制等模块，形成一个完整的知识蒸馏流程。

**关键创新**：引入可学习的频率基和相位偏移机制，显著提升FR-KAN的非线性拟合能力，同时通过动态采样策略优化知识转移过程，克服了MLP的固定激活函数限制。

**关键设计**：设计了基于教师-学生预测一致性的边际级别采样概率矩阵，并采用自适应加权损失机制，以减轻学生模型因缺乏显式邻域聚合而导致的性能下降。

## 📊 实验亮点

SA-DSD在六个真实数据集上相较于三种GNN教师模型实现了3.05%-3.62%的性能提升，相较于FR-KAN+模型提升了15.61%。此外，SA-DSD在参数数量上减少了16.96倍，推理时间减少了55.75%。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其是在智能家居设备、可穿戴技术和移动终端等消费电子领域。通过优化模型的推理速度和参数效率，SA-DSD能够在资源受限的边缘计算环境中实现更高效的深度学习应用，推动智能设备的智能化和普及。未来，该方法还可能扩展到其他需要高效模型部署的领域。

## 📄 摘要（原文）

> Knowledge distillation (KD) is crucial for deploying deep learning models in resource-constrained edge environments, particularly within the consumer electronics sector, including smart home devices, wearable technology, and mobile terminals. These applications place higher demands on model compression and inference speed, necessitating the transfer of knowledge from Graph Neural Networks (GNNs) to more efficient Multi-Layer Perceptron (MLP) models. However, due to their fixed activation functions and fully connected architecture, MLPs face challenges in rapidly capturing the complex neighborhood dependencies learned by GNNs, thereby limiting their performance in edge environments. To address these limitations, this paper introduces an innovative from GNNs to Kolmogorov-Arnold Networks (KANs) knowledge distillation framework-Self Attention Dynamic Sampling Distillation (SA-DSD). This study improved Fourier KAN (FR-KAN) and replaced MLP with the improved FR-KAN+ as the student model. Through the incorporation of learnable frequency bases and phase-shift mechanisms, along with algorithmic optimization, FR-KAN significantly improves its nonlinear fitting capability while effectively reducing computational complexity. Building on this, a margin-level sampling probability matrix, based on teacher-student prediction consistency, is constructed, and an adaptive weighted loss mechanism is designed to mitigate performance degradation in the student model due to the lack of explicit neighborhood aggregation. Extensive experiments conducted on six real-world datasets demonstrate that SA-DSD achieves performance improvements of 3.05%-3.62% over three GNN teacher models and 15.61% over the FR-KAN+ model. Moreover, when compared with key benchmark models, SA-DSD achieves a 16.96x reduction in parameter count and a 55.75% decrease in inference time.

