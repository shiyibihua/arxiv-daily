---
layout: default
title: Wave-Former: Through-Occlusion 3D Reconstruction via Wireless Shape Completion
---

# Wave-Former: Through-Occlusion 3D Reconstruction via Wireless Shape Completion

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.14152" target="_blank" class="toolbar-btn">arXiv: 2511.14152v2</a>
    <a href="https://arxiv.org/pdf/2511.14152.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.14152v2" 
            onclick="toggleFavorite(this, '2511.14152v2', 'Wave-Former: Through-Occlusion 3D Reconstruction via Wireless Shape Completion')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Laura Dodds, Maisy Lam, Waleed Akbar, Yibo Cheng, Fadel Adib

**分类**: cs.CV

**发布日期**: 2025-11-18 (更新: 2025-11-19)

---

## 💡 一句话要点

**Wave-Former：利用无线信号形状补全实现穿透遮挡的三维重建**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `毫米波雷达` `三维重建` `形状补全` `Transformer网络` `穿透遮挡` `无线感知` `物理感知`

## 📋 核心要点

1. 现有毫米波三维重建方法存在覆盖范围有限、噪声高等问题，难以准确重建被完全遮挡物体的形状。
2. Wave-Former利用毫米波信号的物理特性，设计了一个三阶段流程，实现对遮挡物体的形状补全和三维重建。
3. 实验结果表明，Wave-Former在真实数据上具有良好的泛化能力，显著提高了重建的召回率和精度。

## 📝 摘要（中文）

本文提出了一种名为Wave-Former的新方法，它能够对完全遮挡的、各种各样的日常物体进行高精度三维形状重建。这种能力可以为机器人、增强现实和物流等领域开辟新的应用。我们的方法利用毫米波(mmWave)无线信号，它可以穿透常见的遮挡物并从隐藏物体上反射。与过去毫米波重建方法相比，Wave-Former引入了一种物理感知形状补全模型，能够推断完整的3D几何形状，克服了覆盖范围有限和噪声高的缺点。Wave-Former设计的核心是一个新颖的三阶段流程，通过结合毫米波信号的物理特性，将原始无线信号与基于视觉的形状补全的最新进展联系起来。该流程提出候选几何表面，采用专门为毫米波信号设计的基于Transformer的形状补全模型，最后执行熵引导的表面选择。这使得Wave-Former能够使用完全合成的点云进行训练，同时展示出对真实世界数据的出色泛化能力。与最先进的基线方法相比，Wave-Former在保持85%高精度的同时，将召回率从54%提高到72%。

## 🔬 方法详解

**问题定义**：论文旨在解决完全遮挡场景下，传统毫米波三维重建方法精度低、覆盖范围有限的问题。现有方法难以有效利用毫米波信号进行形状补全，导致重建效果不佳。

**核心思路**：论文的核心思路是结合毫米波信号的物理特性，设计一个物理感知的形状补全模型。该模型能够从原始无线信号中提取几何信息，并利用Transformer网络进行形状补全，从而实现对遮挡物体的准确重建。

**技术框架**：Wave-Former包含三个主要阶段：1) 候选几何表面生成：从毫米波信号中提取特征，生成可能的几何表面；2) 基于Transformer的形状补全：利用Transformer网络对候选表面进行补全，生成完整的三维形状；3) 熵引导的表面选择：根据熵值选择最合适的表面作为最终重建结果。

**关键创新**：Wave-Former的关键创新在于其物理感知的形状补全模型和三阶段流程。该模型能够有效利用毫米波信号的物理特性，并结合Transformer网络的强大表示能力，实现对遮挡物体的准确重建。此外，该方法使用合成数据进行训练，并成功泛化到真实数据，降低了数据采集成本。

**关键设计**：Transformer网络结构是关键设计之一，用于学习毫米波信号与物体形状之间的映射关系。熵引导的表面选择方法用于选择最合适的重建结果。具体的损失函数和网络参数设置在论文中未详细说明，属于未知信息。

## 📊 实验亮点

Wave-Former在真实世界数据上进行了评估，结果表明，与最先进的基线方法相比，Wave-Former在保持85%高精度的同时，将召回率从54%提高到72%。这表明Wave-Former具有更好的重建性能和泛化能力。

## 🎯 应用场景

Wave-Former在机器人、增强现实和物流等领域具有广泛的应用前景。例如，在机器人领域，它可以帮助机器人识别和抓取被遮挡的物体；在增强现实领域，它可以用于创建更逼真的虚拟环境；在物流领域，它可以用于检测和识别隐藏的包裹。该研究有望推动无线感知技术的发展，并为相关领域带来新的机遇。

## 📄 摘要（原文）

> We present Wave-Former, a novel method capable of high-accuracy 3D shape reconstruction for completely occluded, diverse, everyday objects. This capability can open new applications spanning robotics, augmented reality, and logistics. Our approach leverages millimeter-wave (mmWave) wireless signals, which can penetrate common occlusions and reflect off hidden objects. In contrast to past mmWave reconstruction methods, which suffer from limited coverage and high noise, Wave-Former introduces a physics-aware shape completion model capable of inferring full 3D geometry. At the heart of Wave-Former's design is a novel three-stage pipeline which bridges raw wireless signals with recent advancements in vision-based shape completion by incorporating physical properties of mmWave signals. The pipeline proposes candidate geometric surfaces, employs a transformer-based shape completion model designed specifically for mmWave signals, and finally performs entropy-guided surface selection. This enables Wave-Former to be trained using entirely synthetic point-clouds, while demonstrating impressive generalization to real-world data. In head-to-head comparisons with state-of-the-art baselines, Wave-Former raises recall from 54% to 72% while maintaining a high precision of 85%.

