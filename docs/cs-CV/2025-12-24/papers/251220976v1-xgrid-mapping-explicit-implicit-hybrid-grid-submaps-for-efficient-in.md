---
layout: default
title: "XGrid-Mapping: Explicit Implicit Hybrid Grid Submaps for Efficient Incremental Neural LiDAR Mapping"
---

# XGrid-Mapping: Explicit Implicit Hybrid Grid Submaps for Efficient Incremental Neural LiDAR Mapping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20976" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20976v1</a>
  <a href="https://arxiv.org/pdf/2512.20976.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20976v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20976v1', 'XGrid-Mapping: Explicit Implicit Hybrid Grid Submaps for Efficient Incremental Neural LiDAR Mapping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeqing Song, Zhongmiao Yan, Junyuan Deng, Songpengcheng Xia, Xiang Mu, Jingyi Xu, Qi Wu, Ling Pei

**分类**: cs.CV

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**提出XGrid-Mapping，利用显隐混合网格子图实现高效增量式神经激光雷达建图**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `激光雷达建图` `神经表示` `增量式建图` `显隐混合表示` `子图管理`

## 📋 核心要点

1. 现有神经激光雷达建图方法依赖密集隐式表示，忽略几何结构，或基于体素的方法难以实时运行。
2. XGrid-Mapping结合稀疏显式网格和密集隐式网格，利用VDB结构和子图组织，实现高效增量建图。
3. 引入基于蒸馏的重叠对齐策略和动态移除模块，提升子图一致性、鲁棒性和采样效率。

## 📝 摘要（中文）

大规模增量式建图是构建鲁棒可靠的自主系统的基础，它支撑着利用连续输入进行增量式环境理解，从而为导航和决策提供支持。激光雷达因其精度和鲁棒性而被广泛使用。近年来，神经激光雷达建图表现出令人印象深刻的性能；然而，大多数方法依赖于密集的隐式表示，未能充分利用几何结构，而现有的基于体素的方法难以实现实时性能。为了解决这些挑战，我们提出了XGrid-Mapping，一种混合网格框架，它联合利用显式和隐式表示来实现高效的神经激光雷达建图。具体来说，该策略将提供几何先验和结构指导的稀疏网格与丰富场景表示的隐式密集网格相结合。通过将VDB结构与基于子图的组织相结合，该框架降低了计算负载，并实现了大规模高效的增量式建图。为了减轻子图之间的不连续性，我们引入了一种基于蒸馏的重叠对齐策略，其中先前的子图监督后续的子图，以确保重叠区域的一致性。为了进一步提高鲁棒性和采样效率，我们加入了一个动态移除模块。大量的实验表明，我们的方法提供了卓越的建图质量，同时克服了基于体素的方法的效率限制，从而优于现有的最先进的建图方法。

## 🔬 方法详解

**问题定义**：现有神经激光雷达建图方法主要面临两个挑战：一是基于隐式表示的方法忽略了激光雷达数据的几何结构信息，导致建图精度受限；二是基于体素的方法计算复杂度高，难以实现大规模场景下的实时增量式建图。因此，如何兼顾建图精度和效率，实现大规模场景下的实时增量式神经激光雷达建图是本文要解决的核心问题。

**核心思路**：XGrid-Mapping的核心思路是结合显式和隐式表示的优点。显式表示（稀疏网格）提供几何先验和结构指导，降低学习难度；隐式表示（密集网格）则可以更精细地表达场景细节。通过这种混合表示，可以在保证建图精度的同时，提高建图效率。此外，采用基于子图的组织方式和蒸馏对齐策略，进一步提升了大规模场景下的建图效果。

**技术框架**：XGrid-Mapping的整体框架包括以下几个主要模块：1) 稀疏显式网格：使用VDB结构存储稀疏体素网格，提供几何先验；2) 隐式密集网格：使用MLP网络学习每个体素的占用概率，精细化场景表示；3) 子图管理：将场景划分为多个子图，降低计算负载；4) 蒸馏对齐：利用先前子图监督后续子图，保证子图间一致性；5) 动态移除模块：移除冗余点，提高采样效率。

**关键创新**：XGrid-Mapping的关键创新在于以下几点：1) 显隐混合网格表示：结合了显式和隐式表示的优点，提高了建图精度和效率；2) 基于蒸馏的重叠对齐策略：有效缓解了子图之间的不连续性问题；3) 动态移除模块：提高了采样效率和鲁棒性。与现有方法相比，XGrid-Mapping在保证建图精度的前提下，显著提高了建图效率，更适合大规模场景下的实时应用。

**关键设计**：在显隐混合网格表示中，稀疏网格的分辨率和隐式网络的结构是关键参数。蒸馏损失函数的设计也至关重要，需要平衡精度和效率。动态移除模块的阈值设置会影响采样效率和鲁棒性。具体而言，论文可能采用了交叉熵损失函数来训练隐式网络，并使用L1或L2损失函数进行蒸馏对齐。稀疏网格的分辨率需要根据场景的复杂度进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20976v1/picture_new/intro.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20976v1/picture_new/voxel-raycast.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20976v1/picture_new/approach-pipeline-f.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，XGrid-Mapping在建图质量上优于现有的state-of-the-art方法，同时克服了基于体素的方法的效率限制。具体性能数据未知，但摘要强调了其在效率上的显著提升，表明该方法在保证精度的前提下，能够实现更快的建图速度，更适合大规模场景的应用。

## 🎯 应用场景

XGrid-Mapping在自动驾驶、机器人导航、三维重建等领域具有广泛的应用前景。它可以为自动驾驶车辆提供高精度、实时的环境地图，从而提高导航的准确性和安全性。在机器人导航领域，它可以帮助机器人在复杂环境中进行自主探索和定位。在三维重建领域，它可以用于构建高精度的三维模型，应用于城市规划、文物保护等领域。未来，该研究可以进一步扩展到动态环境下的建图，以及多传感器融合的建图。

## 📄 摘要（原文）

> Large-scale incremental mapping is fundamental to the development of robust and reliable autonomous systems, as it underpins incremental environmental understanding with sequential inputs for navigation and decision-making. LiDAR is widely used for this purpose due to its accuracy and robustness. Recently, neural LiDAR mapping has shown impressive performance; however, most approaches rely on dense implicit representations and underutilize geometric structure, while existing voxel-guided methods struggle to achieve real-time performance. To address these challenges, we propose XGrid-Mapping, a hybrid grid framework that jointly exploits explicit and implicit representations for efficient neural LiDAR mapping. Specifically, the strategy combines a sparse grid, providing geometric priors and structural guidance, with an implicit dense grid that enriches scene representation. By coupling the VDB structure with a submap-based organization, the framework reduces computational load and enables efficient incremental mapping on a large scale. To mitigate discontinuities across submaps, we introduce a distillation-based overlap alignment strategy, in which preceding submaps supervise subsequent ones to ensure consistency in overlapping regions. To further enhance robustness and sampling efficiency, we incorporate a dynamic removal module. Extensive experiments show that our approach delivers superior mapping quality while overcoming the efficiency limitations of voxel-guided methods, thereby outperforming existing state-of-the-art mapping methods.

