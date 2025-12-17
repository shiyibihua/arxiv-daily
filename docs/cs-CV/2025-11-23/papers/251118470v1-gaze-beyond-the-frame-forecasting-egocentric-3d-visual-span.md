---
layout: default
title: Gaze Beyond the Frame: Forecasting Egocentric 3D Visual Span
---

# Gaze Beyond the Frame: Forecasting Egocentric 3D Visual Span

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.18470" target="_blank" class="toolbar-btn">arXiv: 2511.18470v1</a>
    <a href="https://arxiv.org/pdf/2511.18470.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18470v1" 
            onclick="toggleFavorite(this, '2511.18470v1', 'Gaze Beyond the Frame: Forecasting Egocentric 3D Visual Span')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Heeseung Yun, Joonil Na, Jaeyeon Kim, Calvin Murdock, Gunhee Kim

**分类**: cs.CV

**发布日期**: 2025-11-23

**备注**: NeurIPS 2025 Spotlight

---

## 💡 一句话要点

**EgoSpanLift：预测第一人称视角下的3D视觉范围，提升AR/VR体验。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `第一人称视角` `3D视觉范围预测` `SLAM` `深度学习` `时空融合`

## 📋 核心要点

1. 现有第一人称视角研究主要关注运动和交互，忽略了视觉感知预测在引导行为中的作用及其在AR/VR中的潜力。
2. 论文提出EgoSpanLift，将2D视觉范围预测提升到3D场景，利用SLAM关键点和体积视觉区域进行预测。
3. 实验表明，该方法在3D视觉范围预测上优于现有基线，并在2D投影上达到可比结果，验证了有效性。

## 📝 摘要（中文）

本文提出了一种预测第一人称视角下3D视觉范围的方法，旨在预测个体在三维环境中接下来视觉关注的焦点。现有研究主要集中在基于运动和接触的交互，而对人类视觉感知本身的预测研究较少。为此，论文提出了EgoSpanLift，一种将第一人称视觉范围预测从2D图像平面转换到3D场景的新方法。EgoSpanLift将SLAM导出的关键点转换为与注视兼容的几何体，并提取体积视觉范围区域。此外，EgoSpanLift与3D U-Net和单向Transformer相结合，实现了时空融合，从而有效地预测3D网格中未来的视觉范围。论文还整理了一个来自原始第一人称多传感器数据的综合基准，创建了一个包含364.6K样本的3D视觉范围预测测试平台。该方法在第一人称2D注视预测和3D定位方面优于竞争基线，即使在没有额外2D特定训练的情况下投影回2D图像平面时，也能获得相当的结果。

## 🔬 方法详解

**问题定义**：论文旨在解决第一人称视角下3D视觉范围预测问题。现有方法主要集中在2D图像平面上的注视预测，缺乏对3D场景几何信息的有效利用，难以准确预测个体在3D空间中的视觉关注点。此外，缺乏大规模的3D视觉范围预测数据集也限制了相关研究的进展。

**核心思路**：论文的核心思路是将2D图像平面上的视觉范围预测问题转化为3D场景中的体积预测问题。通过利用SLAM技术获取的3D场景几何信息，将2D注视预测结果提升到3D空间，从而更准确地预测个体在3D环境中的视觉关注区域。这种方法能够更好地捕捉场景的3D结构信息，提高预测的准确性。

**技术框架**：整体框架包括以下几个主要阶段：1) 利用SLAM技术重建3D场景，并提取关键点；2) 将SLAM关键点转换为与注视兼容的几何体；3) 提取体积视觉范围区域；4) 利用3D U-Net和单向Transformer进行时空特征融合，预测未来的3D视觉范围。该框架将SLAM、计算机视觉和深度学习技术相结合，实现了从2D到3D的视觉范围预测。

**关键创新**：论文最重要的技术创新点在于提出了EgoSpanLift方法，该方法能够将2D图像平面上的视觉范围预测问题转化为3D场景中的体积预测问题。与现有方法相比，EgoSpanLift能够更好地利用3D场景的几何信息，从而更准确地预测个体在3D环境中的视觉关注区域。此外，论文还构建了一个大规模的3D视觉范围预测数据集，为相关研究提供了数据支持。

**关键设计**：论文的关键设计包括：1) 使用SLAM技术获取3D场景几何信息；2) 设计了一种将SLAM关键点转换为与注视兼容的几何体的方法；3) 利用3D U-Net提取空间特征，利用单向Transformer提取时间特征；4) 设计了一种损失函数，用于优化3D视觉范围预测模型。具体的网络结构和参数设置在论文中有详细描述。

## 📊 实验亮点

实验结果表明，EgoSpanLift方法在第一人称2D注视预测和3D定位方面优于竞争基线。具体而言，在3D视觉范围预测任务上，EgoSpanLift的性能显著优于现有方法。此外，即使在没有额外2D特定训练的情况下，将EgoSpanLift的预测结果投影回2D图像平面时，也能获得与现有2D注视预测方法相当的结果，验证了该方法的有效性和泛化能力。

## 🎯 应用场景

该研究成果可应用于增强现实（AR）和虚拟现实（VR）领域，例如，可以根据用户的视觉关注点动态调整AR/VR场景的渲染质量，提高用户体验。此外，该技术还可以应用于辅助技术领域，例如，可以帮助视力障碍者更好地理解周围环境，提高生活质量。未来，该技术有望在机器人导航、智能监控等领域发挥重要作用。

## 📄 摘要（原文）

> People continuously perceive and interact with their surroundings based on underlying intentions that drive their exploration and behaviors. While research in egocentric user and scene understanding has focused primarily on motion and contact-based interaction, forecasting human visual perception itself remains less explored despite its fundamental role in guiding human actions and its implications for AR/VR and assistive technologies. We address the challenge of egocentric 3D visual span forecasting, predicting where a person's visual perception will focus next within their three-dimensional environment. To this end, we propose EgoSpanLift, a novel method that transforms egocentric visual span forecasting from 2D image planes to 3D scenes. EgoSpanLift converts SLAM-derived keypoints into gaze-compatible geometry and extracts volumetric visual span regions. We further combine EgoSpanLift with 3D U-Net and unidirectional transformers, enabling spatio-temporal fusion to efficiently predict future visual span in the 3D grid. In addition, we curate a comprehensive benchmark from raw egocentric multisensory data, creating a testbed with 364.6K samples for 3D visual span forecasting. Our approach outperforms competitive baselines for egocentric 2D gaze anticipation and 3D localization while achieving comparable results even when projected back onto 2D image planes without additional 2D-specific training.

