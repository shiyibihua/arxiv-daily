---
layout: default
title: Physics-Embedded Neural ODEs for Sim2Real Edge Digital Twins of Hybrid Power Electronics Systems
---

# Physics-Embedded Neural ODEs for Sim2Real Edge Digital Twins of Hybrid Power Electronics Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02887" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02887v1</a>
  <a href="https://arxiv.org/pdf/2508.02887.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02887v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02887v1', 'Physics-Embedded Neural ODEs for Sim2Real Edge Digital Twins of Hybrid Power Electronics Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jialin Zheng, Haoyu Wang, Yangbin Zeng, Di Mou, Xin Zhang, Hong Li, Sergio Vazquez, Leopoldo G. Franquelo

**分类**: cs.LG, eess.SY

**发布日期**: 2025-08-04

---

## 💡 一句话要点

**提出物理嵌入神经ODE以解决混合动力电子系统的Sim2Real问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `边缘数字双胞胎` `物理嵌入神经ODE` `电力电子系统` `Sim2Real` `混合动态` `实时控制` `FPGA部署`

## 📋 核心要点

1. 现有建模方法难以有效捕捉电力电子系统中复杂的混合动态，影响了在边缘设备上的应用效果。
2. 本文提出的物理嵌入神经ODE（PENODE）通过嵌入事件自动机和直接注入ODE成分，提升了模型的准确性和可解释性。
3. 实验结果显示，PENODE在不同场景下的准确性显著提高，同时神经元数量减少了75%，验证了其高效性。

## 📝 摘要（中文）

边缘数字双胞胎（EDTs）在电力电子系统（PES）的监控与控制中至关重要。然而，现有建模方法难以持续捕捉PES中固有的混合动态，导致在资源受限的边缘设备上Sim-to-Real泛化能力下降。为了解决这些挑战，本文提出了一种物理嵌入神经ODE（PENODE），该方法将混合操作机制嵌入事件自动机中，以明确控制离散切换，并将已知的ODE成分直接注入未建模动态的神经参数化中。这种统一设计实现了可微分的端到端可训练架构，保持了物理可解释性，同时减少了冗余，并支持高效的FPGA部署的云到边缘工具链。实验结果表明，PENODE在白盒、灰盒和黑盒场景下的基准测试中显著提高了准确性，神经元数量减少了75%，验证了所提PENODE保持了物理可解释性、高效边缘部署和实时控制增强。

## 🔬 方法详解

**问题定义**：本文旨在解决现有电力电子系统建模方法在捕捉混合动态方面的不足，导致Sim-to-Real泛化能力差的问题。

**核心思路**：提出物理嵌入神经ODE（PENODE），通过将混合操作机制嵌入事件自动机和直接注入已知ODE成分，来增强模型的物理可解释性和准确性。

**技术框架**：PENODE的整体架构包括事件自动机模块和神经网络模块，前者负责控制离散切换，后者负责处理未建模的动态。该架构支持端到端的可微分训练。

**关键创新**：PENODE的主要创新在于将物理知识与神经网络相结合，形成一种新的建模方式，使得模型在保持物理可解释性的同时，减少了冗余参数。

**关键设计**：在设计中，采用了特定的损失函数来平衡物理约束与数据驱动学习，同时优化了网络结构以减少神经元数量，从而实现高效的边缘部署。

## 📊 实验亮点

实验结果表明，PENODE在白盒、灰盒和黑盒场景下的准确性显著提高，神经元数量减少了75%，显示出其在高效边缘部署和实时控制方面的优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能电网、自动化控制系统和机器人等，能够为实时监控和控制提供更高效的解决方案。未来，PENODE有望在资源受限的边缘设备上实现更广泛的应用，推动智能电力系统的发展。

## 📄 摘要（原文）

> Edge Digital Twins (EDTs) are crucial for monitoring and control of Power Electronics Systems (PES). However, existing modeling approaches struggle to consistently capture continuously evolving hybrid dynamics that are inherent in PES, degrading Sim-to-Real generalization on resource-constrained edge devices. To address these challenges, this paper proposes a Physics-Embedded Neural ODEs (PENODE) that (i) embeds the hybrid operating mechanism as an event automaton to explicitly govern discrete switching and (ii) injects known governing ODE components directly into the neural parameterization of unmodeled dynamics. This unified design yields a differentiable end-to-end trainable architecture that preserves physical interpretability while reducing redundancy, and it supports a cloud-to-edge toolchain for efficient FPGA deployment. Experimental results demonstrate that PENODE achieves significantly higher accuracy in benchmarks in white-box, gray-box, and black-box scenarios, with a 75% reduction in neuron count, validating that the proposed PENODE maintains physical interpretability, efficient edge deployment, and real-time control enhancement.

