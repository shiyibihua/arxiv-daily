---
layout: default
title: HCC-3D: Hierarchical Compensatory Compression for 98% 3D Token Reduction in Vision-Language Models
---

# HCC-3D: Hierarchical Compensatory Compression for 98% 3D Token Reduction in Vision-Language Models

**arXiv**: [2511.09883v1](https://arxiv.org/abs/2511.09883) | [PDF](https://arxiv.org/pdf/2511.09883.pdf)

**作者**: Liheng Zhang, Jin Wang, Hui Li, Bingfeng Zhang, Weifeng Liu

**分类**: cs.CV

**发布日期**: 2025-11-13

---

## 💡 一句话要点

**提出HCC-3D，通过分层补偿压缩实现3D视觉语言模型中98%的Token缩减**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D视觉语言模型` `点云处理` `Token压缩` `分层压缩` `自适应细节挖掘`

## 📋 核心要点

1. 现有3D-VLMs直接处理大量3D tokens导致计算成本高昂，限制了其应用，亟需高效的3D token压缩方法。
2. HCC-3D通过全局结构压缩保留整体结构信息，并利用自适应细节挖掘补偿压缩过程中的信息损失。
3. 实验表明，HCC-3D实现了98%的token压缩率，并在多个任务上取得了state-of-the-art的性能。

## 📝 摘要（中文）

本文提出了一种名为分层补偿压缩（HCC-3D）的方法，旨在高效压缩3D视觉语言模型（VLMs）中的3D tokens，同时保留关键细节信息。现有3D-VLMs直接将3D点云嵌入到3D tokens中，计算成本高昂，限制了其应用。HCC-3D首先采用全局结构压缩（GSC），设计全局查询将所有3D tokens压缩为少量关键tokens，保留整体结构信息。然后，为了补偿GSC中的信息损失，进一步提出自适应细节挖掘（ADM）模块，通过互补评分选择性地重新压缩显著但未充分关注的特征。实验结果表明，HCC-3D不仅实现了极高的压缩率（约98%），而且达到了新的state-of-the-art性能，在效率和性能上均有显著提升。

## 🔬 方法详解

**问题定义**：现有3D视觉语言模型直接将3D点云转换为大量的3D tokens，然后输入到大型语言模型（LLM）中进行处理。这种方法计算成本非常高，严重限制了3D-VLMs的应用。主要的痛点在于LLM需要处理大量的3D tokens，导致计算瓶颈。

**核心思路**：论文的核心思路是通过分层压缩的方式，在尽可能保留关键信息的前提下，大幅度减少3D tokens的数量。首先进行全局结构压缩，保留整体的结构信息；然后，针对压缩过程中可能丢失的细节信息，进行自适应的细节挖掘和补偿。这样既能降低计算量，又能保证模型的性能。

**技术框架**：HCC-3D包含两个主要模块：全局结构压缩（GSC）和自适应细节挖掘（ADM）。GSC模块使用全局查询来压缩所有3D tokens，提取少量关键tokens，保留整体结构信息。ADM模块则通过互补评分机制，选择性地重新压缩显著但未被充分关注的特征，以补偿GSC中可能丢失的细节信息。整个流程是先进行全局压缩，再进行局部细节补偿，从而实现高效的token压缩。

**关键创新**：该方法最重要的创新点在于分层补偿压缩的策略。传统的压缩方法往往会造成信息损失，而HCC-3D通过全局结构压缩和自适应细节挖掘相结合，能够在大幅度压缩tokens的同时，尽可能地保留关键信息。这种分层补偿的策略是与现有方法最本质的区别。

**关键设计**：GSC模块中，全局查询的设计至关重要，需要能够有效地提取全局结构信息。ADM模块中，互补评分机制的设计需要能够准确地识别出显著但未被充分关注的特征。具体的网络结构和损失函数细节论文中未明确给出，属于未知信息。推测可能使用了注意力机制相关的网络结构，损失函数可能包含重建损失和对比损失等。

## 📊 实验亮点

HCC-3D实现了高达98%的3D token压缩率，显著降低了计算成本。同时，在多个3D视觉语言任务上取得了state-of-the-art的性能，表明该方法在效率和性能上均有显著提升。具体的性能数据和对比基线在摘要中未给出，属于未知信息。

## 🎯 应用场景

HCC-3D具有广泛的应用前景，例如在自动驾驶、机器人导航、三维场景理解等领域。通过降低3D-VLMs的计算成本，可以使其更容易部署在资源受限的设备上，从而加速这些技术的落地和应用。此外，该方法还可以应用于其他需要处理大量tokens的多模态任务中，具有一定的通用性。

## 📄 摘要（原文）

> 3D understanding has drawn significant attention recently, leveraging Vision-Language Models (VLMs) to enable multi-modal reasoning between point cloud and text data. Current 3D-VLMs directly embed the 3D point clouds into 3D tokens, following large 2D-VLMs with powerful reasoning capabilities. However, this framework has a great computational cost limiting its application, where we identify that the bottleneck lies in processing all 3D tokens in the Large Language Model (LLM) part. This raises the question: how can we reduce the computational overhead introduced by 3D tokens while preserving the integrity of their essential information? To address this question, we introduce Hierarchical Compensatory Compression (HCC-3D) to efficiently compress 3D tokens while maintaining critical detail retention. Specifically, we first propose a global structure compression (GSC), in which we design global queries to compress all 3D tokens into a few key tokens while keeping overall structural information. Then, to compensate for the information loss in GSC, we further propose an adaptive detail mining (ADM) module that selectively recompresses salient but under-attended features through complementary scoring. Extensive experiments demonstrate that HCC-3D not only achieves extreme compression ratios (approximately 98%) compared to previous 3D-VLMs, but also achieves new state-of-the-art performance, showing the great improvements on both efficiency and performance.

