---
layout: default
title: On the Geometric Accuracy of Implicit and Primitive-based Representations Derived from View Rendering Constraints
---

# On the Geometric Accuracy of Implicit and Primitive-based Representations Derived from View Rendering Constraints

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10241" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10241v2</a>
  <a href="https://arxiv.org/pdf/2509.10241.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10241v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10241v2', 'On the Geometric Accuracy of Implicit and Primitive-based Representations Derived from View Rendering Constraints')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Elias De Smijter, Renaud Detry, Christophe De Vleeschouwer

**分类**: cs.CV

**发布日期**: 2025-09-12 (更新: 2025-09-15)

**备注**: 9 pages, 3 figures, to be presented at ASTRA25,

---

## 💡 一句话要点

**针对空间机器人应用，对比隐式与显式新视角合成方法的几何精度**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `新视角合成` `三维重建` `空间机器人` `几何精度` `外观嵌入`

## 📋 核心要点

1. 现有新视角合成方法在空间机器人等几何精度要求高的场景中表现不足，外观嵌入对几何精度的提升效果有待考察。
2. 通过对比K-Planes、Gaussian Splatting和Convex Splatting等方法，评估外观嵌入对几何重建的影响，并分析不同表示方法的优劣。
3. 实验表明，外观嵌入主要减少了显式方法的图元数量，凸溅射在紧凑性和无杂波方面优于高斯溅射，更适合安全关键应用。

## 📝 摘要（中文）

本文首次系统性地比较了隐式和显式新视角合成方法在基于空间的3D物体重建中的几何精度，并评估了外观嵌入的作用。虽然嵌入通过建模光照变化提高了光度保真度，但研究表明它们并未转化为有意义的几何精度提升，而几何精度是空间机器人应用的关键要求。使用SPEED+数据集，比较了K-Planes、Gaussian Splatting和Convex Splatting，结果表明嵌入主要减少了显式方法所需的图元数量，而不是增强了几何保真度。此外，凸溅射比高斯溅射实现了更紧凑和无杂波的表示，为交互和避碰等安全关键应用提供了优势。研究结果阐明了外观嵌入在以几何为中心任务中的局限性，并强调了空间场景中重建质量和表示效率之间的权衡。

## 🔬 方法详解

**问题定义**：论文旨在解决空间机器人应用中，基于新视角合成的3D物体重建的几何精度问题。现有方法虽然在光度保真度上有所提升，但几何精度仍然不足，尤其是在复杂光照条件下。此外，现有方法在表示效率和紧凑性方面存在挑战，不利于安全关键应用，例如交互和避碰。

**核心思路**：论文的核心思路是通过系统性地比较隐式和显式新视角合成方法，并评估外观嵌入对几何精度的影响，从而找到更适合空间机器人应用的重建方法。论文认为，虽然外观嵌入可以提高光度保真度，但其对几何精度的贡献有限。

**技术框架**：论文的技术框架主要包括以下几个步骤：1) 选择代表性的隐式方法（K-Planes）和显式方法（Gaussian Splatting和Convex Splatting）；2) 在SPEED+数据集上进行实验，该数据集专门为空间应用设计；3) 评估不同方法在几何精度、光度保真度、表示效率和紧凑性方面的表现；4) 分析外观嵌入对几何精度的影响。

**关键创新**：论文的关键创新在于首次系统性地比较了隐式和显式新视角合成方法在空间机器人应用中的几何精度，并揭示了外观嵌入对几何精度的有限贡献。此外，论文还提出了使用Convex Splatting来实现更紧凑和无杂波的表示，这对于安全关键应用具有重要意义。

**关键设计**：论文使用了SPEED+数据集进行评估，该数据集包含各种空间场景和光照条件。论文采用标准的评估指标来衡量几何精度（例如Chamfer Distance）和光度保真度（例如PSNR、SSIM）。对于Convex Splatting，论文可能采用了特定的凸包算法来生成紧凑的表示。具体的损失函数和网络结构细节可能因所使用的具体方法而异，但论文重点在于比较不同方法的整体性能。

## 📊 实验亮点

实验结果表明，外观嵌入主要减少了显式方法所需的图元数量，而不是显著提升几何精度。Convex Splatting在表示紧凑性和无杂波方面优于Gaussian Splatting，更适合安全关键应用。具体性能数据（例如Chamfer Distance的降低幅度）需要在论文中查找。

## 🎯 应用场景

该研究成果可应用于空间机器人、卫星遥感、行星探测等领域。更精确的3D重建可以提高空间机器人的自主导航、目标识别和操作能力。紧凑且无杂波的表示方法有利于碰撞避免和安全交互。此外，该研究还可以促进新视角合成技术在其他几何精度要求高的领域的应用，例如医学影像和工业检测。

## 📄 摘要（原文）

> We present the first systematic comparison of implicit and explicit Novel View Synthesis methods for space-based 3D object reconstruction, evaluating the role of appearance embeddings. While embeddings improve photometric fidelity by modeling lighting variation, we show they do not translate into meaningful gains in geometric accuracy - a critical requirement for space robotics applications. Using the SPEED+ dataset, we compare K-Planes, Gaussian Splatting, and Convex Splatting, and demonstrate that embeddings primarily reduce the number of primitives needed for explicit methods rather than enhancing geometric fidelity. Moreover, convex splatting achieves more compact and clutter-free representations than Gaussian splatting, offering advantages for safety-critical applications such as interaction and collision avoidance. Our findings clarify the limits of appearance embeddings for geometry-centric tasks and highlight trade-offs between reconstruction quality and representation efficiency in space scenarios.

