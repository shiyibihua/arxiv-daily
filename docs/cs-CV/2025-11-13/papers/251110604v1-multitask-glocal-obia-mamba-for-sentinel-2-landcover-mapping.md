---
layout: default
title: Multitask GLocal OBIA-Mamba for Sentinel-2 Landcover Mapping
---

# Multitask GLocal OBIA-Mamba for Sentinel-2 Landcover Mapping

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.10604" target="_blank" class="toolbar-btn">arXiv: 2511.10604v1</a>
    <a href="https://arxiv.org/pdf/2511.10604.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.10604v1" 
            onclick="toggleFavorite(this, '2511.10604v1', 'Multitask GLocal OBIA-Mamba for Sentinel-2 Landcover Mapping')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zack Dewis, Yimin Zhu, Zhengsen Xu, Mabel Heffring, Saeid Taleghanidoozdoozan, Kaylee Xiao, Motasem Alkayid, Lincoln Linlin Xu

**分类**: cs.CV, cs.LG

**发布日期**: 2025-11-13

---

## 💡 一句话要点

**提出多任务GLocal OBIA-Mamba模型，提升Sentinel-2土地覆盖分类精度。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `土地覆盖分类` `Sentinel-2` `对象图像分析` `Mamba模型` `全局-局部网络` `多任务学习` `遥感影像处理`

## 📋 核心要点

1. Sentinel-2土地覆盖分类面临空间异质性和光谱特征模糊等挑战，现有方法难以兼顾全局上下文和局部细节。
2. 论文提出GLocal OBIA-Mamba模型，利用超像素降低计算量，并设计双分支网络融合全局上下文和局部细节。
3. 实验结果表明，该方法在Sentinel-2影像分类中，相比现有方法，实现了更高的分类精度和更精细的细节。

## 📝 摘要（中文）

本文提出了一种新颖的多任务GLocal OBIA-Mamba (MSOM) 模型，用于增强Sentinel-2影像的土地利用和土地覆盖 (LULC) 分类。针对Sentinel-2数据在LULC分类中面临的空间异质性、上下文信息利用和光谱特征模糊等挑战，该方法具有以下贡献：首先，设计了一种基于对象图像分析 (OBIA) 的Mamba模型 (OBIA-Mamba)，通过使用超像素作为Mamba tokens来减少冗余计算，同时保留精细的细节。其次，构建了一个全局-局部 (GLocal) 双分支卷积神经网络 (CNN)-Mamba架构，用于联合建模局部空间细节和全局上下文信息。第三，采用多任务优化框架，利用双重损失函数来平衡局部精度和全局一致性。在加拿大阿尔伯塔省的Sentinel-2影像上进行了测试，并与几种先进的分类方法进行了比较，结果表明，该方法实现了更高的分类精度和更精细的细节。

## 🔬 方法详解

**问题定义**：Sentinel-2影像的土地覆盖分类任务面临着空间异质性、上下文信息利用不足以及光谱特征模糊等问题。现有的方法难以有效地提取和利用全局上下文信息，同时保持局部细节的精细度，导致分类精度受限。

**核心思路**：论文的核心思路是结合对象图像分析（OBIA）和Mamba模型，并设计一个全局-局部（GLocal）双分支架构，以同时捕捉全局上下文信息和局部空间细节。通过OBIA将像素聚合成超像素，减少Mamba模型的计算量，同时保留图像的结构信息。GLocal双分支结构则分别处理全局上下文和局部细节，最后通过多任务学习框架进行融合。

**技术框架**：MSOM模型的整体框架包括以下几个主要模块：1) 超像素分割：使用OBIA方法将Sentinel-2影像分割成超像素，每个超像素作为一个token输入Mamba模型。2) GLocal双分支网络：该网络包含两个分支，一个分支使用卷积神经网络（CNN）提取局部空间细节，另一个分支使用Mamba模型提取全局上下文信息。3) 多任务优化：使用双重损失函数，一个损失函数关注局部精度，另一个损失函数关注全局一致性。

**关键创新**：该论文的关键创新在于：1) 将Mamba模型引入到OBIA框架中，利用超像素作为token，降低了计算复杂度，同时保留了图像的结构信息。2) 提出了GLocal双分支架构，能够同时建模局部空间细节和全局上下文信息。3) 设计了多任务优化框架，平衡了局部精度和全局一致性。

**关键设计**：在OBIA-Mamba模块中，超像素的大小是一个关键参数，需要根据具体的数据集进行调整。GLocal双分支网络中，CNN分支的网络结构可以采用ResNet等经典结构，Mamba分支则需要根据输入token的维度进行调整。多任务优化框架中，两个损失函数的权重需要根据实验结果进行调整，以平衡局部精度和全局一致性。

## 📊 实验亮点

实验结果表明，提出的MSOM模型在Sentinel-2影像分类任务中取得了显著的性能提升。与几种先进的分类方法相比，MSOM模型实现了更高的分类精度和更精细的细节。具体性能数据（如总体精度、Kappa系数等）在论文中进行了详细的对比和分析，证明了该方法的有效性。

## 🎯 应用场景

该研究成果可应用于各种环境监测应用，例如土地利用规划、森林资源管理、城市扩张监测、农业生产评估和自然灾害评估等。通过提高Sentinel-2影像的土地覆盖分类精度，可以为相关领域的决策提供更可靠的数据支持，并促进可持续发展。

## 📄 摘要（原文）

> Although Sentinel-2 based land use and land cover (LULC) classification is critical for various environmental monitoring applications, it is a very difficult task due to some key data challenges (e.g., spatial heterogeneity, context information, signature ambiguity). This paper presents a novel Multitask Glocal OBIA-Mamba (MSOM) for enhanced Sentinel-2 classification with the following contributions. First, an object-based image analysis (OBIA) Mamba model (OBIA-Mamba) is designed to reduce redundant computation without compromising fine-grained details by using superpixels as Mamba tokens. Second, a global-local (GLocal) dual-branch convolutional neural network (CNN)-mamba architecture is designed to jointly model local spatial detail and global contextual information. Third, a multitask optimization framework is designed to employ dual loss functions to balance local precision with global consistency. The proposed approach is tested on Sentinel-2 imagery in Alberta, Canada, in comparison with several advanced classification approaches, and the results demonstrate that the proposed approach achieves higher classification accuracy and finer details that the other state-of-the-art methods.

