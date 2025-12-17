---
layout: default
title: D$^2$GSLAM: 4D Dynamic Gaussian Splatting SLAM
---

# D$^2$GSLAM: 4D Dynamic Gaussian Splatting SLAM

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.09411" target="_blank" class="toolbar-btn">arXiv: 2512.09411v1</a>
    <a href="https://arxiv.org/pdf/2512.09411.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.09411v1" 
            onclick="toggleFavorite(this, '2512.09411v1', 'D$^2$GSLAM: 4D Dynamic Gaussian Splatting SLAM')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Siting Zhu, Yuxiang Huang, Wenhua Wu, Chaokang Jiang, Yongbo Chen, I-Ming Chen, Hesheng Wang

**分类**: cs.RO

**发布日期**: 2025-12-10

---

## 💡 一句话要点

**D$^2$GSLAM：基于高斯表示的动态场景4D SLAM系统，实现动态环境下的精确重建与鲁棒跟踪。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `动态SLAM` `高斯表示` `动态场景重建` `相机跟踪` `运动建模`

## 📋 核心要点

1. 现有稠密SLAM方法在动态环境中表现不佳，通常直接移除动态物体，忽略了其中包含的运动信息。
2. D$^2$GSLAM利用高斯表示，通过几何提示动态分离、动态-静态复合表示等方法，实现动态场景的精确重建和鲁棒跟踪。
3. 实验结果表明，D$^2$GSLAM在动态场景的映射和跟踪精度方面表现优异，并具备精确的动态建模能力。

## 📝 摘要（中文）

本文提出了一种名为D$^2$GSLAM的动态SLAM系统，该系统利用高斯表示，在动态环境中同时实现精确的动态重建和鲁棒的跟踪。该系统由四个关键部分组成：（i）提出了一种几何提示动态分离方法，用于区分场景中的静态和动态元素。该方法利用高斯表示的几何一致性和场景几何来获得粗略的动态区域，然后这些区域作为提示来指导粗略掩码的细化，从而实现精确的运动掩码。（ii）为了促进动态场景的精确和高效映射，引入了动态-静态复合表示，该表示将静态3D高斯与动态4D高斯相结合。这种表示允许对场景中物体的静态和动态状态之间的转换进行建模，以进行复合映射和优化。（iii）采用渐进式姿态细化策略，该策略利用静态场景几何的多视图一致性和来自动态物体的运动信息来实现精确的相机跟踪。（iv）引入了运动一致性损失，该损失利用物体运动中的时间连续性来实现精确的动态建模。D$^2$GSLAM在动态场景的映射和跟踪精度方面表现出卓越的性能，同时也展示了在精确动态建模方面的能力。

## 🔬 方法详解

**问题定义**：现有稠密SLAM方法在动态环境下难以兼顾精确重建和鲁棒跟踪，通常简单地移除动态物体，损失了重要的运动信息。这些方法无法有效地建模动态物体的运动状态，导致重建精度下降和跟踪失败。

**核心思路**：D$^2$GSLAM的核心思路是利用高斯表示同时建模静态和动态场景，并利用动态物体的运动信息辅助相机跟踪。通过几何提示动态分离，区分静态和动态元素，并使用动态-静态复合表示来建模物体状态的转换。运动一致性损失则用于约束动态物体的运动轨迹，提高动态建模的精度。

**技术框架**：D$^2$GSLAM系统包含四个主要模块：1) 几何提示动态分离模块，用于区分静态和动态区域；2) 动态-静态复合表示模块，使用3D高斯表示静态场景，4D高斯表示动态场景；3) 渐进式姿态细化模块，利用静态场景几何和动态物体运动信息进行相机跟踪；4) 运动一致性损失模块，约束动态物体的运动轨迹。整体流程是先进行动态分离，然后构建复合表示，再进行姿态估计和地图优化。

**关键创新**：D$^2$GSLAM的关键创新在于：1) 提出了几何提示动态分离方法，能够更准确地识别动态区域；2) 引入了动态-静态复合表示，能够有效地建模动态物体的运动状态和状态转换；3) 利用动态物体的运动信息辅助相机跟踪，提高了跟踪的鲁棒性。与现有方法相比，D$^2$GSLAM能够更全面地利用场景信息，实现更精确的动态重建和更鲁棒的跟踪。

**关键设计**：几何提示动态分离模块利用高斯表示的几何一致性来获得粗略的动态区域，然后使用这些区域作为提示来指导掩码细化。动态-静态复合表示使用3D高斯表示静态场景，4D高斯表示动态场景，并允许它们之间进行转换。运动一致性损失基于时间连续性约束动态物体的运动轨迹，具体形式未知。

## 📊 实验亮点

D$^2$GSLAM在动态场景的映射和跟踪精度方面表现出卓越的性能。具体性能数据未知，但论文强调了其在精确动态建模方面的能力。通过与现有方法的对比，D$^2$GSLAM在动态环境下的重建精度和跟踪鲁棒性方面均有显著提升。实验结果验证了所提出的几何提示动态分离、动态-静态复合表示和运动一致性损失的有效性。

## 🎯 应用场景

D$^2$GSLAM在机器人导航、自动驾驶、增强现实等领域具有广泛的应用前景。它可以帮助机器人在动态环境中进行更精确的定位和地图构建，从而实现更安全、更可靠的自主导航。此外，该系统还可以用于动态场景的三维重建，为虚拟现实和游戏开发提供更逼真的场景模型。

## 📄 摘要（原文）

> Recent advances in Dense Simultaneous Localization and Mapping (SLAM) have demonstrated remarkable performance in static environments. However, dense SLAM in dynamic environments remains challenging. Most methods directly remove dynamic objects and focus solely on static scene reconstruction, which ignores the motion information contained in these dynamic objects. In this paper, we present D$^2$GSLAM, a novel dynamic SLAM system utilizing Gaussian representation, which simultaneously performs accurate dynamic reconstruction and robust tracking within dynamic environments. Our system is composed of four key components: (i) We propose a geometric-prompt dynamic separation method to distinguish between static and dynamic elements of the scene. This approach leverages the geometric consistency of Gaussian representation and scene geometry to obtain coarse dynamic regions. The regions then serve as prompts to guide the refinement of the coarse mask for achieving accurate motion mask. (ii) To facilitate accurate and efficient mapping of the dynamic scene, we introduce dynamic-static composite representation that integrates static 3D Gaussians with dynamic 4D Gaussians. This representation allows for modeling the transitions between static and dynamic states of objects in the scene for composite mapping and optimization. (iii) We employ a progressive pose refinement strategy that leverages both the multi-view consistency of static scene geometry and motion information from dynamic objects to achieve accurate camera tracking. (iv) We introduce a motion consistency loss, which leverages the temporal continuity in object motions for accurate dynamic modeling. Our D$^2$GSLAM demonstrates superior performance on dynamic scenes in terms of mapping and tracking accuracy, while also showing capability in accurate dynamic modeling.

