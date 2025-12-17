---
layout: default
title: GauDP: Reinventing Multi-Agent Collaboration through Gaussian-Image Synergy in Diffusion Policies
---

# GauDP: Reinventing Multi-Agent Collaboration through Gaussian-Image Synergy in Diffusion Policies

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.00998" target="_blank" class="toolbar-btn">arXiv: 2511.00998v1</a>
    <a href="https://arxiv.org/pdf/2511.00998.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00998v1" 
            onclick="toggleFavorite(this, '2511.00998v1', 'GauDP: Reinventing Multi-Agent Collaboration through Gaussian-Image Synergy in Diffusion Policies')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Ziye Wang, Li Kang, Yiran Qin, Jiahua Ma, Zhanglin Peng, Lei Bai, Ruimao Zhang

**分类**: cs.RO

**发布日期**: 2025-11-02

**备注**: Accepted by NeurIPS 2025. Project page: https://ziyeeee.github.io/gaudp.io/

---

## 💡 一句话要点

**GauDP：通过高斯图像协同的扩散策略重塑多智能体协作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `多智能体协作` `具身智能` `模仿学习` `3D高斯场` `扩散模型`

## 📋 核心要点

1. 现有方法难以平衡多智能体系统中细粒度局部控制与全局场景理解，限制了可扩展性和协作质量。
2. GauDP构建全局一致的3D高斯场，并动态地将高斯属性分配给每个智能体的局部视角，实现自适应特征查询。
3. 在RoboFactory基准测试中，GauDP优于现有图像方法，接近点云方法性能，并保持了良好的可扩展性。

## 📝 摘要（中文）

在具身多智能体系统中，有效的协作一直是一个根本性的挑战，尤其是在智能体必须平衡个体视角与全局环境感知的情况下。现有方法通常难以平衡细粒度的局部控制与全面的场景理解，导致可扩展性受限和协作质量下降。本文提出了GauDP，一种新颖的高斯图像协同表示，它促进了多智能体协作系统中可扩展的、感知驱动的模仿学习。具体来说，GauDP从分散的RGB观测中构建全局一致的3D高斯场，然后动态地将3D高斯属性重新分配给每个智能体的局部视角。这使得所有智能体能够自适应地从共享场景表示中查询任务关键特征，同时保持其个体视角。这种设计在不需要额外的传感模态（例如，3D点云）的情况下，促进了细粒度的控制和全局连贯的行为。我们在RoboFactory基准上评估了GauDP，该基准包括各种多臂操作任务。我们的方法优于现有的基于图像的方法，并接近点云驱动方法的有效性，同时随着智能体数量的增加保持了强大的可扩展性。

## 🔬 方法详解

**问题定义**：多智能体协作任务中，如何让每个智能体在保持自身视角的同时，有效地利用全局信息进行决策是一个关键问题。现有方法要么依赖于额外的传感模态（如点云），增加了系统复杂性；要么难以在细粒度控制和全局一致性之间取得平衡，导致协作效率低下。

**核心思路**：GauDP的核心在于利用3D高斯场作为全局场景的统一表示，并设计了一种机制，允许每个智能体根据自身视角和任务需求，自适应地从高斯场中提取关键特征。这种方法既避免了对额外传感器的依赖，又实现了全局信息和局部视角的有效融合。

**技术框架**：GauDP的整体框架包括以下几个主要阶段：1) 从每个智能体的RGB图像观测中构建局部3D高斯场；2) 将所有局部高斯场融合，构建全局一致的3D高斯场；3) 根据每个智能体的视角，动态地从全局高斯场中提取特征，并将其融入到智能体的局部观测中；4) 使用融合后的观测训练扩散策略，实现多智能体协作。

**关键创新**：GauDP的关键创新在于提出了高斯图像协同表示，它将3D高斯场作为全局场景的统一表示，并通过动态特征重分配机制，实现了全局信息和局部视角的有效融合。与现有方法相比，GauDP无需额外的传感模态，并且能够更好地平衡细粒度控制和全局一致性。

**关键设计**：GauDP的关键设计包括：1) 使用可微分渲染技术，从RGB图像中构建局部3D高斯场；2) 设计了一种基于注意力机制的动态特征重分配模块，用于根据智能体的视角和任务需求，从全局高斯场中提取关键特征；3) 使用扩散模型作为策略网络，实现多智能体协作策略的学习。

## 📊 实验亮点

GauDP在RoboFactory基准测试中取得了显著的性能提升。在多臂操作任务中，GauDP的性能优于现有的基于图像的方法，并且接近于基于点云的方法。此外，实验结果表明，GauDP具有良好的可扩展性，随着智能体数量的增加，性能依然能够保持稳定。

## 🎯 应用场景

GauDP具有广泛的应用前景，例如在自动化装配、协同机器人操作、智能交通等领域。它可以应用于多机器人协同完成复杂任务，提高生产效率和自动化水平。此外，该方法还可以扩展到虚拟现实和增强现实等领域，实现更自然、更高效的人机交互。

## 📄 摘要（原文）

> Recently, effective coordination in embodied multi-agent systems has remained a fundamental challenge, particularly in scenarios where agents must balance individual perspectives with global environmental awareness. Existing approaches often struggle to balance fine-grained local control with comprehensive scene understanding, resulting in limited scalability and compromised collaboration quality. In this paper, we present GauDP, a novel Gaussian-image synergistic representation that facilitates scalable, perception-aware imitation learning in multi-agent collaborative systems. Specifically, GauDP constructs a globally consistent 3D Gaussian field from decentralized RGB observations, then dynamically redistributes 3D Gaussian attributes to each agent's local perspective. This enables all agents to adaptively query task-critical features from the shared scene representation while maintaining their individual viewpoints. This design facilitates both fine-grained control and globally coherent behavior without requiring additional sensing modalities (e.g., 3D point cloud). We evaluate GauDP on the RoboFactory benchmark, which includes diverse multi-arm manipulation tasks. Our method achieves superior performance over existing image-based methods and approaches the effectiveness of point-cloud-driven methods, while maintaining strong scalability as the number of agents increases.

