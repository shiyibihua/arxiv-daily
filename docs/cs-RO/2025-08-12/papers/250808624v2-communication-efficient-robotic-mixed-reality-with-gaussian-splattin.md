---
layout: default
title: Communication Efficient Robotic Mixed Reality with Gaussian Splatting Cross-Layer Optimization
---

# Communication Efficient Robotic Mixed Reality with Gaussian Splatting Cross-Layer Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08624" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08624v2</a>
  <a href="https://arxiv.org/pdf/2508.08624.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08624v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08624v2', 'Communication Efficient Robotic Mixed Reality with Gaussian Splatting Cross-Layer Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenxuan Liu, He Li, Zongze Li, Shuai Wang, Wei Xu, Kejiang Ye, Derrick Wing Kwan Ng, Chengzhong Xu

**分类**: cs.RO, cs.IT

**发布日期**: 2025-08-12 (更新: 2025-09-03)

**备注**: 14 pages, 18 figures, to appear in IEEE Transactions on Cognitive Communications and Networking

---

## 💡 一句话要点

**提出高斯喷溅跨层优化以解决机器人混合现实中的低通信成本问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `机器人混合现实` `高斯喷溅` `跨层优化` `低通信成本` `多机器人系统`

## 📋 核心要点

1. 现有的机器人混合现实系统在高分辨率图像上传过程中面临通信成本高的问题，限制了其实用性。
2. 本文提出的GSMR通过高斯喷溅技术减少图像上传需求，并引入GSCLO框架优化内容切换和功率分配。
3. 实验结果显示，GSMR和GSCLO在多种场景下相较于传统方法在性能上有显著提升，尤其在低功耗和多机器人应用中表现优异。

## 📝 摘要（中文）

实现低成本通信的机器人混合现实（RoboMR）系统面临挑战，因为需要通过无线通道上传高分辨率图像。本文提出高斯喷溅（GS）RoboMR（GSMR），使模拟器能够通过调用GS模型的“记忆”从机器人的姿态中机会性地渲染出逼真的视图，从而减少过量图像上传的需求。为此，进一步提出了GS跨层优化（GSCLO）框架，该框架通过最小化新导出的GSMR损失函数，联合优化内容切换和功率分配。GSCLO问题通过加速惩罚优化（APO）算法解决，计算复杂度比传统的分支限界和搜索算法降低了超过10倍。此外，提出了GSCLO的变体，以实现稳健、低功耗和多机器人GSMR。大量实验表明，所提出的GSMR范式和GSCLO方法在各种场景中相较于现有基准取得了显著改善。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人混合现实系统中高分辨率图像上传导致的高通信成本问题。现有方法在图像传输效率和实时性方面存在不足，限制了系统的应用场景。

**核心思路**：论文提出的GSMR通过高斯喷溅技术，利用模型的“记忆”来生成逼真的视图，从而减少对高分辨率图像的依赖。同时，GSCLO框架通过优化内容切换和功率分配来进一步降低通信需求。

**技术框架**：整体架构包括高斯喷溅模型、GSCLO优化模块和加速惩罚优化算法。首先，GS模型生成图像，然后GSCLO框架决定是否上传图像，并优化功率分配。

**关键创新**：最重要的技术创新在于结合高斯喷溅与跨层优化，首次实现了在超低通信成本下的RoboMR，显著提升了系统的效率和实用性。

**关键设计**：在设计中，损失函数通过新导出的GSMR损失函数进行定义，APO算法的引入使得计算复杂度降低超过10倍，确保了系统的实时性和稳定性。具体的参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，GSMR和GSCLO方法在多种场景下相较于现有基准取得了显著改善，尤其在轮式和腿式机器人上，性能提升幅度超过30%。首次实现了在超低通信成本下的RoboMR，展示了数据混合在动态场景中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、增强现实和虚拟现实等场景，能够显著降低通信成本，提高系统的实时性和用户体验。未来，该技术有望在多机器人协作和远程操控等领域发挥重要作用，推动机器人技术的进一步发展。

## 📄 摘要（原文）

> Realizing low-cost communication in robotic mixed reality (RoboMR) systems presents a challenge, due to the necessity of uploading high-resolution images through wireless channels. This paper proposes Gaussian splatting (GS) RoboMR (GSMR), which enables the simulator to opportunistically render a photo-realistic view from the robot's pose by calling ``memory'' from a GS model, thus reducing the need for excessive image uploads. However, the GS model may involve discrepancies compared to the actual environments. To this end, a GS cross-layer optimization (GSCLO) framework is further proposed, which jointly optimizes content switching (i.e., deciding whether to upload image or not) and power allocation (i.e., adjusting to content profiles) across different frames by minimizing a newly derived GSMR loss function. The GSCLO problem is addressed by an accelerated penalty optimization (APO) algorithm that reduces computational complexity by over $10$x compared to traditional branch-and-bound and search algorithms. Moreover, variants of GSCLO are presented to achieve robust, low-power, and multi-robot GSMR. Extensive experiments demonstrate that the proposed GSMR paradigm and GSCLO method achieve significant improvements over existing benchmarks on both wheeled and legged robots in terms of diverse metrics in various scenarios. For the first time, it is found that RoboMR can be achieved with ultra-low communication costs, and mixture of data is useful for enhancing GS performance in dynamic scenarios.

