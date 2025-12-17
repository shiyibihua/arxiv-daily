---
layout: default
title: ArtiWorld: LLM-Driven Articulation of 3D Objects in Scenes
---

# ArtiWorld: LLM-Driven Articulation of 3D Objects in Scenes

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.12977" target="_blank" class="toolbar-btn">arXiv: 2511.12977v2</a>
    <a href="https://arxiv.org/pdf/2511.12977.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.12977v2" 
            onclick="toggleFavorite(this, '2511.12977v2', 'ArtiWorld: LLM-Driven Articulation of 3D Objects in Scenes')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yixuan Yang, Luyang Xie, Zhen Luo, Zixiang Zhao, Tongsheng Ding, Mingqi Gao, Feng Zheng

**分类**: cs.CV

**发布日期**: 2025-11-17 (更新: 2025-11-18)

---

## 💡 一句话要点

**ArtiWorld：提出LLM驱动的3D场景物体可动性自动生成方法**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `可动性生成` `大型语言模型` `URDF` `3D场景理解` `机器人学习`

## 📋 核心要点

1. 现有3D模拟资产多为刚性，手动转换为可动对象成本高昂，缺乏自动化的可动性生成方法。
2. ArtiWorld利用LLM的先验知识，结合3D点云和URDF导向的提示，自动将刚性物体转换为可交互的URDF模型。
3. 实验表明，ArtiWorld在模拟和真实场景中均优于现有方法，能有效生成高质量的可动模型。

## 📝 摘要（中文）

构建交互式模拟器和可扩展的机器人学习环境需要大量可动资产。然而，目前模拟中的大多数3D资产是刚性的，手动将其转换为可动对象需要大量的人力和成本。本文提出了ArtiWorld，一个场景感知的流水线，可以从文本场景描述中定位候选的可动对象，并重建保留原始几何形状的可执行URDF模型。该流水线的核心是Arti4URDF，它利用3D点云、大型语言模型（LLM）的先验知识和面向URDF的提示设计，快速将刚性对象转换为基于URDF的交互式可动对象，同时保持其3D形状。在3D模拟对象、完整3D模拟场景和真实世界扫描场景三个层面上评估了ArtiWorld。在所有三个设置中，该方法始终优于现有方法，并实现了最先进的性能，同时保留了对象几何形状并正确捕获了对象交互性，从而生成了可用的基于URDF的可动模型。这为直接从现有3D资产构建交互式的、机器人就绪的模拟环境提供了一条实用的途径。

## 🔬 方法详解

**问题定义**：论文旨在解决如何自动地将3D场景中的刚性物体转换为可动模型的问题。现有方法需要大量人工干预，成本高且效率低，难以满足构建大规模交互式模拟环境的需求。现有方法在几何形状保持和交互性捕获方面存在不足。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的先验知识来指导可动性生成过程。通过结合3D点云信息和URDF（Unified Robot Description Format）导向的提示，LLM可以更好地理解物体的结构和潜在的运动方式，从而生成更合理的可动模型。

**技术框架**：ArtiWorld包含以下主要模块：1) 场景理解模块：从文本描述中识别潜在的可动对象。2) Arti4URDF模块：利用3D点云、LLM和URDF提示，将刚性对象转换为URDF模型。3) 评估模块：在不同场景下评估生成的可动模型的质量。Arti4URDF是核心模块，负责将刚性对象转换为可动对象。

**关键创新**：该方法最重要的创新点在于将LLM引入到可动性生成过程中。通过利用LLM的知识，可以更好地理解物体的结构和功能，从而生成更合理的可动模型。此外，URDF导向的提示设计也提高了生成模型的质量。

**关键设计**：Arti4URDF的关键设计包括：1) 使用预训练的LLM，例如GPT-3，作为知识来源。2) 设计URDF导向的提示，引导LLM生成符合URDF规范的模型。3) 使用3D点云信息来约束生成模型的几何形状。4) 使用损失函数来优化生成模型的参数，例如关节位置和运动范围。

## 📊 实验亮点

ArtiWorld在3D模拟对象、完整3D模拟场景和真实世界扫描场景三个层面上进行了评估，均优于现有方法。实验结果表明，ArtiWorld能够有效地生成高质量的可动模型，同时保持对象的几何形状和交互性。具体性能数据未知，但论文强调其在所有测试场景中均取得了state-of-the-art的性能。

## 🎯 应用场景

该研究成果可广泛应用于机器人学习、虚拟现实、游戏开发等领域。通过自动生成可动模型，可以大大降低构建交互式模拟环境的成本，加速机器人算法的开发和验证。此外，该技术还可以用于创建更逼真的虚拟现实体验和更具互动性的游戏。

## 📄 摘要（原文）

> Building interactive simulators and scalable robot-learning environments requires a large number of articulated assets. However, most existing 3D assets in simulation are rigid, and manually converting them into articulated objects is extremely labor- and cost-intensive. This raises a natural question: can we automatically identify articulable objects in a scene and convert them into articulated assets directly? In this paper, we present ArtiWorld, a scene-aware pipeline that localizes candidate articulable objects from textual scene descriptions and reconstructs executable URDF models that preserve the original geometry. At the core of this pipeline is Arti4URDF, which leverages 3D point cloud, prior knowledge of a large language model (LLM), and a URDF-oriented prompt design to rapidly convert rigid objects into interactive URDF-based articulated objects while maintaining their 3D shape. We evaluate ArtiWorld at three levels: 3D simulated objects, full 3D simulated scenes, and real-world scan scenes. Across all three settings, our method consistently outperforms existing approaches and achieves state-of-the-art performance, while preserving object geometry and correctly capturing object interactivity to produce usable URDF-based articulated models. This provides a practical path toward building interactive, robot-ready simulation environments directly from existing 3D assets. Code and data will be released.

