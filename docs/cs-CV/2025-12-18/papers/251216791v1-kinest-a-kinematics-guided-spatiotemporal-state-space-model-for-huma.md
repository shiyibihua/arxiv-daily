---
layout: default
title: KineST: A Kinematics-guided Spatiotemporal State Space Model for Human Motion Tracking from Sparse Signals
---

# KineST: A Kinematics-guided Spatiotemporal State Space Model for Human Motion Tracking from Sparse Signals

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16791" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16791v1</a>
  <a href="https://arxiv.org/pdf/2512.16791.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16791v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16791v1', 'KineST: A Kinematics-guided Spatiotemporal State Space Model for Human Motion Tracking from Sparse Signals')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuting Zhao, Zeyu Xiao, Xinrong Chen

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-18

**备注**: Accepted by AAAI 2026

**🔗 代码/项目**: [PROJECT_PAGE](https://kaka-1314.github.io/KineST/)

---

## 💡 一句话要点

**KineST：一种基于运动学引导的时空状态空间模型，用于从稀疏信号中进行人体运动跟踪**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `人体运动跟踪` `状态空间模型` `运动学引导` `时空表示学习` `AR/VR` `姿态重建` `稀疏信号`

## 📋 核心要点

1. 现有方法难以兼顾精度、时序一致性和效率，无法有效利用AR/VR场景中头显提供的稀疏信号重建全身姿态。
2. KineST通过运动学引导的双向扫描和混合时空表示学习，在状态空间模型中有效提取时空依赖关系。
3. 实验表明，KineST在轻量级框架下，在运动跟踪的准确性和时间一致性方面均表现出优越的性能。

## 📝 摘要（中文）

全身运动跟踪在AR/VR应用中至关重要，它连接了物理交互和虚拟交互。然而，基于头戴式显示器获取的稀疏信号重建逼真且多样化的全身姿势仍然具有挑战性。现有的姿势重建方法通常计算成本高昂，或者依赖于分别建模空间和时间依赖性，难以平衡准确性、时间连贯性和效率。为了解决这个问题，我们提出了一种新颖的运动学引导的状态空间模型KineST，它有效地提取时空依赖性，同时整合局部和全局姿势感知。其创新之处在于两个核心思想：首先，为了更好地捕捉复杂的关节关系，我们将状态空间对偶框架内的扫描策略重新制定为运动学引导的双向扫描，从而嵌入运动学先验。其次，采用混合时空表示学习方法来紧密耦合空间和时间上下文，从而平衡准确性和平滑性。此外，引入了几何角速度损失，对旋转变化施加物理意义上的约束，进一步提高运动稳定性。大量实验表明，KineST在轻量级框架内具有卓越的准确性和时间一致性。

## 🔬 方法详解

**问题定义**：论文旨在解决从稀疏信号（如AR/VR头显提供的信号）中准确、高效地重建全身运动的问题。现有方法的痛点在于：要么计算复杂度高，难以实时应用；要么分别建模空间和时间依赖性，导致重建的运动不连贯、不自然。

**核心思路**：论文的核心思路是利用运动学先验知识来指导时空状态空间模型的构建，从而更有效地提取和利用运动中的时空依赖关系。通过运动学引导的双向扫描，模型能够更好地理解关节之间的相互作用，并结合混合时空表示学习，平衡准确性和平滑性。

**技术框架**：KineST的整体框架基于状态空间模型，主要包含以下几个阶段：1) 稀疏信号输入；2) 运动学引导的双向扫描：利用运动学链的结构，从两个方向扫描状态空间，提取关节间的关系；3) 混合时空表示学习：将空间和时间信息紧密耦合，学习运动的时空表示；4) 姿态重建：基于学习到的时空表示，重建全身姿态。

**关键创新**：论文最重要的创新点在于运动学引导的双向扫描和混合时空表示学习。运动学引导的双向扫描将运动学先验知识融入到状态空间模型的扫描策略中，使得模型能够更好地捕捉关节间的依赖关系。混合时空表示学习则能够有效地平衡重建的准确性和时间一致性。与现有方法相比，KineST能够更有效地利用稀疏信号中的信息，重建更准确、更自然的运动。

**关键设计**：论文的关键设计包括：1) 运动学引导的双向扫描的具体实现方式，例如如何根据运动学链选择扫描方向和顺序；2) 混合时空表示学习的具体网络结构，例如如何将空间和时间信息融合在一起；3) 几何角速度损失的定义和使用，该损失函数用于约束重建运动的旋转变化，提高运动的稳定性。具体参数设置和网络结构细节在论文中应该有更详细的描述（未知）。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16791v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16791v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16791v1/scan2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，KineST在准确性和时间一致性方面均优于现有方法。具体而言，KineST在姿态重建的平均误差方面降低了X%（具体数值未知），并且在时间一致性指标上提升了Y%（具体数值未知）。这些结果证明了KineST在从稀疏信号中进行人体运动跟踪方面的优越性能。

## 🎯 应用场景

KineST具有广泛的应用前景，尤其是在AR/VR领域。它可以用于构建更逼真、更自然的虚拟化身，提升用户在虚拟环境中的沉浸感和交互体验。此外，该技术还可以应用于游戏、动画制作、运动分析、康复训练等领域，具有重要的实际价值和潜在的商业价值。未来，KineST可以进一步扩展到处理更复杂的运动场景，例如多人交互、物体交互等。

## 📄 摘要（原文）

> Full-body motion tracking plays an essential role in AR/VR applications, bridging physical and virtual interactions. However, it is challenging to reconstruct realistic and diverse full-body poses based on sparse signals obtained by head-mounted displays, which are the main devices in AR/VR scenarios. Existing methods for pose reconstruction often incur high computational costs or rely on separately modeling spatial and temporal dependencies, making it difficult to balance accuracy, temporal coherence, and efficiency. To address this problem, we propose KineST, a novel kinematics-guided state space model, which effectively extracts spatiotemporal dependencies while integrating local and global pose perception. The innovation comes from two core ideas. Firstly, in order to better capture intricate joint relationships, the scanning strategy within the State Space Duality framework is reformulated into kinematics-guided bidirectional scanning, which embeds kinematic priors. Secondly, a mixed spatiotemporal representation learning approach is employed to tightly couple spatial and temporal contexts, balancing accuracy and smoothness. Additionally, a geometric angular velocity loss is introduced to impose physically meaningful constraints on rotational variations for further improving motion stability. Extensive experiments demonstrate that KineST has superior performance in both accuracy and temporal consistency within a lightweight framework. Project page: https://kaka-1314.github.io/KineST/

