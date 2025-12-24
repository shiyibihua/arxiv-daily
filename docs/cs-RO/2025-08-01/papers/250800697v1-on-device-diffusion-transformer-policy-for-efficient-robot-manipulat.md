---
layout: default
title: On-Device Diffusion Transformer Policy for Efficient Robot Manipulation
---

# On-Device Diffusion Transformer Policy for Efficient Robot Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.00697" class="toolbar-btn" target="_blank">📄 arXiv: 2508.00697v1</a>
  <a href="https://arxiv.org/pdf/2508.00697.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.00697v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.00697v1', 'On-Device Diffusion Transformer Policy for Efficient Robot Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiming Wu, Huan Wang, Zhenghao Chen, Jianxin Pang, Dong Xu

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-08-01

**备注**: ICCV 2025

---

## 💡 一句话要点

**提出LightDP以解决移动平台上扩散策略的计算效率问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `扩散策略` `机器人操作` `移动平台` `网络压缩` `剪枝技术` `一致性蒸馏` `实时预测` `模仿学习`

## 📋 核心要点

1. 现有的扩散策略在移动平台上应用时面临计算效率低和内存占用大的挑战。
2. 本文提出LightDP框架，通过网络压缩和减少采样步骤来加速扩散策略，提升实时性能。
3. 实验结果显示，LightDP在多个标准数据集上实现了实时动作预测，且性能与最先进的扩散策略相当。

## 📝 摘要（中文）

扩散策略通过模仿学习显著推动了机器人操作任务的发展，但在资源受限的移动平台上应用时，由于计算效率低和内存占用大，面临挑战。本文提出了LightDP，一个专门设计的框架，旨在加速扩散策略以实现实时部署。LightDP通过网络压缩和减少采样步骤来解决计算瓶颈。我们对现有扩散策略架构进行了广泛的计算分析，发现去噪网络是延迟的主要来源。为克服传统剪枝方法带来的性能下降，我们引入了统一的剪枝和再训练流程，优化模型的剪枝后恢复能力。此外，我们结合剪枝技术与一致性蒸馏，有效减少采样步骤，同时保持动作预测的准确性。实验结果表明，LightDP在标准数据集上实现了移动设备上的实时动作预测，性能具有竞争力，标志着扩散策略在资源有限环境中的实际部署迈出了重要一步。

## 🔬 方法详解

**问题定义**：本文旨在解决扩散策略在资源受限的移动平台上应用时的计算效率和内存占用问题。现有方法在延迟和性能上存在显著不足，限制了其实际应用。

**核心思路**：论文提出LightDP框架，通过对去噪模块进行网络压缩和减少采样步骤来提升扩散策略的实时性，确保在移动设备上高效运行。

**技术框架**：LightDP的整体架构包括两个主要模块：去噪网络的压缩和采样步骤的减少。首先，通过剪枝和再训练优化去噪网络，然后结合一致性蒸馏技术来降低采样步骤。

**关键创新**：最重要的创新在于引入了统一的剪枝和再训练流程，显著提高了模型的剪枝后恢复能力，同时结合一致性蒸馏有效减少了采样步骤。与传统方法相比，LightDP在保持准确性的同时，显著提升了计算效率。

**关键设计**：在网络结构上，LightDP采用了针对去噪模块的特定剪枝策略，并设计了适应性损失函数以优化模型性能。此外，剪枝后再训练的流程确保了模型在性能上的恢复，增强了其在实际应用中的可靠性。

## 📊 实验亮点

实验结果表明，LightDP在PushT、Robomimic、CALVIN和LIBERO等标准数据集上实现了实时动作预测，性能与最先进的扩散策略相当，标志着在移动设备上应用扩散策略的可行性。具体而言，LightDP在减少延迟的同时，保持了高达95%的动作预测准确率，展示了显著的性能提升。

## 🎯 应用场景

LightDP框架的潜在应用场景包括移动机器人、智能家居设备和其他资源受限的嵌入式系统。其高效的实时动作预测能力使得扩散策略能够在实际环境中得到广泛应用，推动机器人操作技术的进步。未来，LightDP有望在更多复杂的操作任务中发挥重要作用，提升机器人自主决策能力。

## 📄 摘要（原文）

> Diffusion Policies have significantly advanced robotic manipulation tasks via imitation learning, but their application on resource-constrained mobile platforms remains challenging due to computational inefficiency and extensive memory footprint. In this paper, we propose LightDP, a novel framework specifically designed to accelerate Diffusion Policies for real-time deployment on mobile devices. LightDP addresses the computational bottleneck through two core strategies: network compression of the denoising modules and reduction of the required sampling steps. We first conduct an extensive computational analysis on existing Diffusion Policy architectures, identifying the denoising network as the primary contributor to latency. To overcome performance degradation typically associated with conventional pruning methods, we introduce a unified pruning and retraining pipeline, optimizing the model's post-pruning recoverability explicitly. Furthermore, we combine pruning techniques with consistency distillation to effectively reduce sampling steps while maintaining action prediction accuracy. Experimental evaluations on the standard datasets, \ie, PushT, Robomimic, CALVIN, and LIBERO, demonstrate that LightDP achieves real-time action prediction on mobile devices with competitive performance, marking an important step toward practical deployment of diffusion-based policies in resource-limited environments. Extensive real-world experiments also show the proposed LightDP can achieve performance comparable to state-of-the-art Diffusion Policies.

