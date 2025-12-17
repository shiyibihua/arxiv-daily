---
layout: default
title: Beyond Darkness: Thermal-Supervised 3D Gaussian Splatting for Low-Light Novel View Synthesis
---

# Beyond Darkness: Thermal-Supervised 3D Gaussian Splatting for Low-Light Novel View Synthesis

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.13011" target="_blank" class="toolbar-btn">arXiv: 2511.13011v1</a>
    <a href="https://arxiv.org/pdf/2511.13011.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.13011v1" 
            onclick="toggleFavorite(this, '2511.13011v1', 'Beyond Darkness: Thermal-Supervised 3D Gaussian Splatting for Low-Light Novel View Synthesis')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Qingsen Ma, Chen Zou, Dianyun Wang, Jia Wang, Liuyu Xiang, Zhaofeng He

**分类**: cs.CV

**发布日期**: 2025-11-17

---

## 💡 一句话要点

**提出DTGS：一种热监督3D高斯溅射方法，用于低光照下的新视角合成。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `低光照增强` `新视角合成` `3D高斯溅射` `Retinex分解` `热监督`

## 📋 核心要点

1. 现有方法在极低光照下进行新视角合成时，由于光照不一致和几何失真，导致3D高斯溅射(3DGS)等方法失效。
2. DTGS通过Retinex启发的照明分解和热引导的3D高斯溅射，实现光照不变的重建，并进行增强、几何和热监督的联合优化。
3. DTGS在新建的多视角低光照热数据集RGBT-LOW上，显著优于现有低光照增强和3D重建基线，实现了更好的辐射一致性。

## 📝 摘要（中文）

在极低光照条件下，新视角合成(NVS)在几何结构、颜色一致性和辐射稳定性方面面临严重退化。标准的3D高斯溅射(3DGS)管道直接应用于曝光不足的输入时会失效，因为跨视角的独立增强会导致光照不一致和几何失真。为了解决这个问题，我们提出了DTGS，一个统一的框架，它将Retinex启发的照明分解与热引导的3D高斯溅射紧密结合，以实现光照不变的重建。与先前将增强作为预处理步骤的方法不同，DTGS通过循环增强-重建机制执行增强、几何和热监督的联合优化。一个热监督分支通过动态平衡增强、结构和热损失来稳定颜色恢复和几何学习。此外，嵌入在3DGS循环中的基于Retinex的分解模块提供了物理上可解释的反射率-照度分离，确保了跨视点的一致颜色和纹理。为了评估我们的方法，我们构建了RGBT-LOW，一个新的多视角低光照热数据集，捕捉了严重的光照退化。大量的实验表明，DTGS显著优于现有的低光照增强和3D重建基线，在极端光照下实现了卓越的辐射一致性、几何保真度和颜色稳定性。

## 🔬 方法详解

**问题定义**：论文旨在解决极低光照条件下新视角合成(NVS)中存在的几何结构失真、颜色不一致和辐射稳定性差的问题。现有方法，如直接应用3D高斯溅射(3DGS)，在低光照图像上表现不佳，因为独立的图像增强预处理步骤会引入跨视角的不一致性，导致重建质量下降。

**核心思路**：论文的核心思路是将Retinex理论引入3DGS框架，通过解耦光照和反射率，实现光照不变的场景重建。同时，利用热成像数据作为监督信号，稳定颜色恢复和几何学习过程，从而在低光照条件下获得更准确、更一致的3D场景表示。

**技术框架**：DTGS框架包含以下几个主要模块：1) Retinex分解模块：将输入图像分解为反射率和照度分量，以实现光照不变性。2) 3D高斯溅射模块：使用高斯分布表示3D场景，并通过渲染生成新视角的图像。3) 热监督模块：利用热成像数据作为监督信号，约束重建的几何结构和颜色信息。4) 循环增强-重建机制：通过联合优化增强、几何和热监督，实现端到端的训练。

**关键创新**：论文的关键创新在于：1) 将Retinex分解集成到3DGS循环中，实现光照不变的重建。2) 引入热成像数据作为监督信号，稳定低光照条件下的几何和颜色学习。3) 提出循环增强-重建机制，实现增强、几何和热监督的联合优化，避免了传统方法中预处理增强带来的问题。

**关键设计**：1) Retinex分解模块采用可学习的网络结构，以更好地适应低光照环境。2) 热监督模块通过动态平衡增强损失、结构损失和热损失，实现对颜色恢复和几何学习的有效约束。3) 3DGS模块采用标准的3D高斯表示，并通过可微分渲染实现端到端的训练。

## 📊 实验亮点

DTGS在RGBT-LOW数据集上进行了广泛的实验，结果表明，DTGS在辐射一致性、几何保真度和颜色稳定性方面显著优于现有的低光照增强和3D重建基线。具体性能数据未知，但论文强调了DTGS在极端光照条件下的优越性，证明了其在低光照新视角合成方面的有效性。

## 🎯 应用场景

该研究成果可应用于安防监控、自动驾驶、机器人导航等领域，尤其是在夜间或低光照环境下。通过提升低光照场景下的3D重建质量，可以提高这些应用在恶劣光照条件下的性能和可靠性。此外，该方法还可以用于增强现实和虚拟现实等应用，提供更逼真的低光照场景体验。

## 📄 摘要（原文）

> Under extremely low-light conditions, novel view synthesis (NVS) faces severe degradation in terms of geometry, color consistency, and radiometric stability. Standard 3D Gaussian Splatting (3DGS) pipelines fail when applied directly to underexposed inputs, as independent enhancement across views causes illumination inconsistencies and geometric distortion. To address this, we present DTGS, a unified framework that tightly couples Retinex-inspired illumination decomposition with thermal-guided 3D Gaussian Splatting for illumination-invariant reconstruction. Unlike prior approaches that treat enhancement as a pre-processing step, DTGS performs joint optimization across enhancement, geometry, and thermal supervision through a cyclic enhancement-reconstruction mechanism. A thermal supervisory branch stabilizes both color restoration and geometry learning by dynamically balancing enhancement, structural, and thermal losses. Moreover, a Retinex-based decomposition module embedded within the 3DGS loop provides physically interpretable reflectance-illumination separation, ensuring consistent color and texture across viewpoints. To evaluate our method, we construct RGBT-LOW, a new multi-view low-light thermal dataset capturing severe illumination degradation. Extensive experiments show that DTGS significantly outperforms existing low-light enhancement and 3D reconstruction baselines, achieving superior radiometric consistency, geometric fidelity, and color stability under extreme illumination.

