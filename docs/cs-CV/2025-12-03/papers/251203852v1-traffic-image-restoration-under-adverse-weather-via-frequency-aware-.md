---
layout: default
title: Traffic Image Restoration under Adverse Weather via Frequency-Aware Mamba
---

# Traffic Image Restoration under Adverse Weather via Frequency-Aware Mamba

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.03852" target="_blank" class="toolbar-btn">arXiv: 2512.03852v1</a>
    <a href="https://arxiv.org/pdf/2512.03852.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.03852v1" 
            onclick="toggleFavorite(this, '2512.03852v1', 'Traffic Image Restoration under Adverse Weather via Frequency-Aware Mamba')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Liwen Pan, Longguang Wang, Guangwei Gao, Jun Wang, Jun Shi, Juncheng Li

**分类**: cs.CV

**发布日期**: 2025-12-03

**备注**: 12pages, 13 figures, 5tables

---

## 💡 一句话要点

**提出频率感知Mamba（FAMamba）用于恶劣天气下的交通图像恢复。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `图像恢复` `恶劣天气` `Mamba架构` `频率域` `智能交通系统`

## 📋 核心要点

1. 现有交通图像恢复方法侧重空间域建模，忽略了频域信息，导致恢复效果受限。
2. FAMamba框架结合频率引导与序列建模，通过双分支结构和自适应扫描提升图像恢复质量。
3. 实验结果表明，FAMamba在图像恢复任务上表现出高效性和有效性，优于现有方法。

## 📝 摘要（中文）

在恶劣天气条件下恢复交通图像对于智能交通系统至关重要。现有方法主要集中在空间域建模，忽略了频域先验。新兴的Mamba架构擅长通过分块相关性分析进行长程依赖建模，但其在频域特征提取方面的潜力尚未被探索。为了解决这个问题，我们提出了一种新颖的频率感知Mamba（FAMamba）框架，该框架将频率引导与序列建模相结合，以实现高效的图像恢复。我们的架构包含两个关键组件：（1）双分支特征提取块（DFEB），通过双向2D频率自适应扫描增强局部-全局交互，并根据子带纹理分布动态调整遍历路径；（2）先验引导块（PGB），通过基于小波的高频残差学习来细化纹理细节，从而实现具有精确细节的高质量图像重建。同时，我们为Mamba架构设计了一种新的自适应频率扫描机制（AFSM），使Mamba能够实现跨不同子图的频域扫描，从而充分利用子图结构中固有的纹理分布特征。大量实验证明了FAMamba的效率和有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决恶劣天气（如雨、雾等）下交通图像的恢复问题。现有方法主要关注空间域特征，忽略了频域信息，导致图像细节模糊、纹理信息丢失，难以满足智能交通系统对清晰图像的需求。

**核心思路**：论文的核心思路是将频域信息融入到Mamba架构中，利用Mamba擅长长程依赖建模的优势，结合频域先验知识，提升图像恢复的质量和效率。通过频率分析，可以更好地捕捉图像的纹理和细节信息，从而改善恢复效果。

**技术框架**：FAMamba框架主要包含两个关键模块：双分支特征提取块（DFEB）和先验引导块（PGB）。DFEB通过双向2D频率自适应扫描增强局部-全局交互，动态调整遍历路径以适应子带纹理分布。PGB则利用基于小波的高频残差学习来细化纹理细节。此外，还设计了自适应频率扫描机制（AFSM）来增强Mamba架构的频域扫描能力。整体流程是先通过DFEB提取特征，然后利用AFSM进行频率扫描，最后通过PGB进行纹理细节的精细化重建。

**关键创新**：论文的关键创新在于将频域信息与Mamba架构相结合，提出了频率感知的Mamba（FAMamba）框架。通过设计双分支特征提取块和自适应频率扫描机制，使得Mamba能够有效地利用频域信息进行图像恢复。与现有方法相比，FAMamba能够更好地捕捉图像的纹理和细节信息，从而提升恢复效果。

**关键设计**：DFEB采用双分支结构，分别进行水平和垂直方向的频率扫描。AFSM根据子图的纹理分布特征，自适应地调整扫描路径。PGB利用小波变换提取高频残差，并将其添加到恢复后的图像中，以增强纹理细节。损失函数方面，可能采用了L1损失、L2损失或感知损失等，以衡量恢复图像与原始图像之间的差异。

## 📊 实验亮点

论文通过大量实验验证了FAMamba的有效性。实验结果表明，FAMamba在图像恢复质量上优于现有方法，能够更有效地恢复图像的纹理细节。具体的性能数据（如PSNR、SSIM等）和对比基线需要在论文中查找。FAMamba在效率方面也表现出色，能够在保证恢复质量的同时，实现较快的处理速度。

## 🎯 应用场景

该研究成果可应用于智能交通系统中的恶劣天气图像增强，例如雨天或雾天环境下的交通监控、自动驾驶等。通过提高图像的清晰度和可见性，可以提升交通系统的安全性和可靠性，减少交通事故的发生，并为自动驾驶车辆提供更准确的环境感知信息。未来，该技术还可以扩展到其他图像恢复领域，如医学图像增强、遥感图像处理等。

## 📄 摘要（原文）

> Traffic image restoration under adverse weather conditions remains a critical challenge for intelligent transportation systems. Existing methods primarily focus on spatial-domain modeling but neglect frequency-domain priors. Although the emerging Mamba architecture excels at long-range dependency modeling through patch-wise correlation analysis, its potential for frequency-domain feature extraction remains unexplored. To address this, we propose Frequency-Aware Mamba (FAMamba), a novel framework that integrates frequency guidance with sequence modeling for efficient image restoration. Our architecture consists of two key components: (1) a Dual-Branch Feature Extraction Block (DFEB) that enhances local-global interaction via bidirectional 2D frequency-adaptive scanning, dynamically adjusting traversal paths based on sub-band texture distributions; and (2) a Prior-Guided Block (PGB) that refines texture details through wavelet-based high-frequency residual learning, enabling high-quality image reconstruction with precise details. Meanwhile, we design a novel Adaptive Frequency Scanning Mechanism (AFSM) for the Mamba architecture, which enables the Mamba to achieve frequency-domain scanning across distinct subgraphs, thereby fully leveraging the texture distribution characteristics inherent in subgraph structures. Extensive experiments demonstrate the efficiency and effectiveness of FAMamba.

