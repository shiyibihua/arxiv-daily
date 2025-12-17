---
layout: default
title: HDCNet: A Hybrid Depth Completion Network for Grasping Transparent and Reflective Objects
---

# HDCNet: A Hybrid Depth Completion Network for Grasping Transparent and Reflective Objects

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.07081" target="_blank" class="toolbar-btn">arXiv: 2511.07081v1</a>
    <a href="https://arxiv.org/pdf/2511.07081.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.07081v1" 
            onclick="toggleFavorite(this, '2511.07081v1', 'HDCNet: A Hybrid Depth Completion Network for Grasping Transparent and Reflective Objects')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Guanghu Xie, Mingxu Li, Songwei Wu, Yang Liu, Zongwu Xie, Baoshi Cao, Hong Liu

**分类**: cs.RO

**发布日期**: 2025-11-10

---

## 💡 一句话要点

**HDCNet：用于抓取透明和反射物体的混合深度补全网络**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度补全` `透明物体` `反射物体` `机器人抓取` `Transformer` `CNN` `Mamba` `多模态融合`

## 📋 核心要点

1. 传统深度传感器难以准确感知透明和反射物体，导致机器人抓取此类物体时性能受限。
2. HDCNet采用Transformer、CNN和Mamba混合架构，通过双分支编码器和多模态融合模块，提升深度补全的准确性和鲁棒性。
3. 实验结果表明，HDCNet在深度补全任务中达到SOTA性能，并显著提高了机器人抓取透明和反射物体的成功率，提升高达60%。

## 📝 摘要（中文）

本文提出了一种新颖的深度补全网络HDCNet，旨在解决机器人操作中透明和反射物体深度感知的难题。传统深度传感器在这些物体表面上通常无法提供可靠的测量结果，限制了机器人在感知和抓取任务中的性能。HDCNet集成了Transformer、CNN和Mamba架构的互补优势。具体而言，编码器被设计为双分支Transformer-CNN框架，以提取特定模态的特征。在编码器的浅层，引入了一个轻量级多模态融合模块，以有效地整合低级特征。在网络瓶颈处，开发了一个Transformer-Mamba混合融合模块，以实现高级语义和全局上下文信息的深度融合，从而显著提高深度补全的准确性和鲁棒性。在多个公共数据集上的大量评估表明，HDCNet在深度补全任务中实现了最先进的(SOTA)性能。此外，机器人抓取实验表明，HDCNet显著提高了透明和反射物体的抓取成功率，提升幅度高达60%。

## 🔬 方法详解

**问题定义**：论文旨在解决透明和反射物体深度感知的难题。传统深度传感器在这些物体表面上无法提供可靠的深度信息，导致机器人难以准确抓取这些物体。现有方法在处理此类物体时，深度补全的准确性和鲁棒性不足。

**核心思路**：论文的核心思路是结合Transformer、CNN和Mamba架构的优势，利用它们各自擅长的特征提取和信息融合能力，构建一个混合深度补全网络。通过多模态融合，充分利用不同模态的信息，提高深度补全的准确性和鲁棒性。

**技术框架**：HDCNet的整体架构是一个编码器-解码器结构。编码器采用双分支Transformer-CNN框架，分别提取图像的全局和局部特征。在编码器的浅层，使用轻量级多模态融合模块融合低级特征。在网络瓶颈处，使用Transformer-Mamba混合融合模块进行深度融合。解码器则负责将融合后的特征映射回深度图。

**关键创新**：HDCNet的关键创新在于Transformer-Mamba混合融合模块。该模块结合了Transformer的全局上下文建模能力和Mamba的序列建模能力，能够更有效地融合高级语义和全局上下文信息，从而显著提高深度补全的准确性和鲁棒性。此外，双分支Transformer-CNN编码器和轻量级多模态融合模块也是重要的创新点。

**关键设计**：Transformer-Mamba混合融合模块的具体实现细节未知，但可以推测其设计目标是充分利用Transformer和Mamba的互补优势。损失函数的设计可能包括深度图重建损失和一些正则化项，以提高模型的泛化能力。双分支Transformer-CNN编码器的具体网络结构和参数设置也需要根据具体任务进行调整。

## 📊 实验亮点

HDCNet在多个公共数据集上实现了最先进的(SOTA)深度补全性能。更重要的是，机器人抓取实验表明，HDCNet显著提高了透明和反射物体的抓取成功率，提升幅度高达60%。这表明HDCNet在实际应用中具有显著的优势。

## 🎯 应用场景

该研究成果可广泛应用于机器人操作领域，尤其是在需要抓取透明和反射物体的场景中，例如：工业自动化、医疗机器人、家庭服务机器人等。通过提高机器人对透明和反射物体的感知能力，可以显著提升其操作效率和可靠性，拓展其应用范围。

## 📄 摘要（原文）

> Depth perception of transparent and reflective objects has long been a critical challenge in robotic manipulation.Conventional depth sensors often fail to provide reliable measurements on such surfaces, limiting the performance of robots in perception and grasping tasks. To address this issue, we propose a novel depth completion network,HDCNet,which integrates the complementary strengths of Transformer,CNN and Mamba architectures.Specifically,the encoder is designed as a dual-branch Transformer-CNN framework to extract modality-specific features. At the shallow layers of the encoder, we introduce a lightweight multimodal fusion module to effectively integrate low-level features. At the network bottleneck,a Transformer-Mamba hybrid fusion module is developed to achieve deep integration of high-level semantic and global contextual information, significantly enhancing depth completion accuracy and robustness. Extensive evaluations on multiple public datasets demonstrate that HDCNet achieves state-of-the-art(SOTA) performance in depth completion tasks.Furthermore,robotic grasping experiments show that HDCNet substantially improves grasp success rates for transparent and reflective objects,achieving up to a 60% increase.

