---
layout: default
title: ViTaMIn-B: A Reliable and Efficient Visuo-Tactile Bimanual Manipulation Interface
---

# ViTaMIn-B: A Reliable and Efficient Visuo-Tactile Bimanual Manipulation Interface

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.05858" target="_blank" class="toolbar-btn">arXiv: 2511.05858v2</a>
    <a href="https://arxiv.org/pdf/2511.05858.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.05858v2" 
            onclick="toggleFavorite(this, '2511.05858v2', 'ViTaMIn-B: A Reliable and Efficient Visuo-Tactile Bimanual Manipulation Interface')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Chuanyu Li, Chaoyi Liu, Daotan Wang, Shuyu Zhang, Lusong Li, Zecui Zeng, Fangchen Liu, Jing Xu, Rui Chen

**分类**: cs.RO

**发布日期**: 2025-11-08 (更新: 2025-12-02)

**备注**: Project page: https://chuanyune.github.io/ViTaMIn-B_page/

**🔗 代码/项目**: [PROJECT_PAGE](https://chuanyune.github.io/ViTaMIn-B_page/)

---

## 💡 一句话要点

**ViTaMIn-B：一种可靠高效的双手视觉触觉操作交互界面**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视觉触觉融合` `双手操作` `数据采集` `机器人学习` `柔顺传感器`

## 📋 核心要点

1. 现有手持数据采集系统在复杂交互场景下，尤其是在双手和富接触任务中，缺乏鲁棒的触觉感知和可靠的姿态跟踪。
2. ViTaMIn-B系统通过新型柔顺视觉触觉传感器DuoTact和基于Meta Quest控制器的6自由度双手姿态获取流程，提升了数据采集的可靠性和效率。
3. 用户研究和实验表明，ViTaMIn-B系统易于使用，并且在双手操作任务中表现出优于现有系统的性能。

## 📝 摘要（中文）

本文提出了一种更强大、更高效的手持数据采集系统ViTaMIn-B，用于处理复杂的交互场景，特别是双手和富接触任务。该系统设计了一种新型柔顺的视觉触觉传感器DuoTact，它具有灵活的框架，可以承受操作过程中较大的接触力，同时捕获高分辨率的接触几何形状。为了增强跨传感器的泛化能力，论文提出重建传感器的全局变形为3D点云，并将其用作策略输入。此外，还开发了一种稳健的统一的6自由度双手姿态获取流程，使用Meta Quest控制器，消除了常见基于SLAM的方法中的轨迹漂移问题。全面的用户研究证实了ViTaMIn-B在新手和专家操作员中的效率和高可用性。在四个双手操作任务上的实验表明，相对于现有系统，ViTaMIn-B具有卓越的任务性能。

## 🔬 方法详解

**问题定义**：现有手持设备数据采集系统在处理复杂的、富含接触的双手操作任务时，面临着触觉感知不鲁棒和姿态跟踪不准确的问题。基于SLAM的姿态估计方法容易出现轨迹漂移，而现有的触觉传感器难以承受操作过程中的大接触力，且泛化能力有限。

**核心思路**：ViTaMIn-B的核心思路是设计一种能够承受大接触力并提供高分辨率接触几何信息的柔顺视觉触觉传感器DuoTact，并结合一种稳健的、无漂移的双手姿态获取方法。通过将传感器形变重建为3D点云，增强策略的跨传感器泛化能力。

**技术框架**：ViTaMIn-B系统主要包含两个核心模块：DuoTact视觉触觉传感器和基于Meta Quest控制器的双手姿态获取系统。DuoTact传感器负责感知接触力和接触几何信息，并将形变重建为3D点云。姿态获取系统利用Meta Quest控制器提供精确的6自由度双手姿态信息，避免了SLAM方法的漂移问题。整个系统将触觉和视觉信息融合，为双手操作任务提供可靠的数据。

**关键创新**：该论文的关键创新在于DuoTact传感器的设计和基于3D点云的触觉信息表示方法。DuoTact传感器采用柔顺框架，能够承受较大的接触力，同时保持较高的触觉感知分辨率。将传感器形变重建为3D点云，可以有效提高策略的跨传感器泛化能力，使得训练得到的策略能够更好地适应不同的传感器。

**关键设计**：DuoTact传感器的关键设计在于其柔顺框架和内部的视觉标记。柔顺框架允许传感器在受到较大接触力时发生形变，从而保护内部的视觉元件。内部的视觉标记用于捕捉传感器表面的形变，并通过算法将其重建为3D点云。Meta Quest控制器被用于提供精确的6自由度双手姿态信息，避免了SLAM方法的漂移问题。具体的参数设置、损失函数和网络结构等技术细节在论文中未详细描述，属于未知信息。

## 📊 实验亮点

用户研究表明，ViTaMIn-B系统在新手和专家操作员中都具有很高的可用性和效率。在四个双手操作任务上的实验结果表明，ViTaMIn-B系统相对于现有系统具有显著的性能提升，但具体的性能数据和提升幅度在摘要中未明确给出，属于未知信息。

## 🎯 应用场景

ViTaMIn-B系统可应用于机器人灵巧操作、远程操作、虚拟现实交互等领域。该系统能够高效地采集高质量的双手操作数据，为训练机器人策略、开发新型人机交互界面提供有力支持。未来，该系统有望在医疗、制造、教育等领域发挥重要作用。

## 📄 摘要（原文）

> Handheld devices have opened up unprecedented opportunities to collect large-scale, high-quality demonstrations efficiently. However, existing systems often lack robust tactile sensing or reliable pose tracking to handle complex interaction scenarios, especially for bimanual and contact-rich tasks. In this work, we propose ViTaMIn-B, a more capable and efficient handheld data collection system for such tasks. We first design DuoTact, a novel compliant visuo-tactile sensor built with a flexible frame to withstand large contact forces during manipulation while capturing high-resolution contact geometry. To enhance the cross-sensor generalizability, we propose reconstructing the sensor's global deformation as a 3D point cloud and using it as the policy input. We further develop a robust, unified 6-DoF bimanual pose acquisition process using Meta Quest controllers, which eliminates the trajectory drift issue in common SLAM-based methods. Comprehensive user studies confirm the efficiency and high usability of ViTaMIn-B among novice and expert operators. Furthermore, experiments on four bimanual manipulation tasks demonstrate its superior task performance relative to existing systems. Project page: https://chuanyune.github.io/ViTaMIn-B_page/

