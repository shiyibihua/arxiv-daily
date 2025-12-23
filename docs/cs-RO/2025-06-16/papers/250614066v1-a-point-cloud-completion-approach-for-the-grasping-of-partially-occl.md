---
layout: default
title: A Point Cloud Completion Approach for the Grasping of Partially Occluded Objects and Its Applications in Robotic Strawberry Harvesting
---

# A Point Cloud Completion Approach for the Grasping of Partially Occluded Objects and Its Applications in Robotic Strawberry Harvesting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14066" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14066v1</a>
  <a href="https://arxiv.org/pdf/2506.14066.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14066v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14066v1', 'A Point Cloud Completion Approach for the Grasping of Partially Occluded Objects and Its Applications in Robotic Strawberry Harvesting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ali Abouzeid, Malak Mansour, Chengsong Hu, Dezhen Song

**分类**: cs.RO

**发布日期**: 2025-06-16

---

## 💡 一句话要点

**提出点云补全方法以解决部分遮挡物体抓取问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `点云补全` `物体抓取` `机器人采摘` `草莓采摘` `3D重建` `运动规划` `碰撞检测`

## 📋 核心要点

1. 现有方法在处理非结构化环境中的物体遮挡时，抓取算法的设计面临重大挑战，导致抓取成功率低。
2. 论文提出了一种端到端的框架，通过点云去噪、分割和补全，提升对部分遮挡物体的抓取能力。
3. 实验结果显示，该方法在形状重建精度和抓取成功率上均显著优于现有技术，提升了自动化采摘的可靠性。

## 📝 摘要（中文）

在机器人水果采摘应用中，管理非结构化环境中的物体遮挡是设计抓取算法的重大挑战。以草莓采摘为案例，我们提出了一个端到端框架，有效进行物体检测、分割和抓取规划，以应对部分遮挡物体带来的问题。我们的策略从点云去噪和分割开始，准确定位水果。为了补偿因遮挡导致的不完整扫描，我们应用点云补全模型，创建草莓的稠密3D重建。目标选择集中在成熟的草莓上，同时将其他草莓分类为障碍物，随后将精细化的点云转换为占用图，以便进行碰撞感知的运动规划。实验结果表明，我们的方法在形状重建精度上表现优异，Chamfer距离为1.10mm，抓取成功率显著提高至79.17%，整体成功尝试比率达到89.58%。此外，我们的方法将障碍物碰撞率从43.33%降低至13.95%，突显了其在提高抓取质量和安全性方面的有效性。

## 🔬 方法详解

**问题定义**：本论文旨在解决在非结构化环境中，部分遮挡物体的抓取问题。现有方法在处理遮挡时，往往导致物体检测和抓取失败，影响采摘效率。

**核心思路**：论文提出的核心思路是通过点云补全技术，重建被遮挡物体的完整形状，从而提高抓取算法的准确性和成功率。该设计旨在克服传统方法在遮挡情况下的局限性。

**技术框架**：整体框架包括点云去噪、物体分割、点云补全和抓取规划四个主要模块。首先进行点云去噪和分割以定位水果，接着应用补全模型重建完整的3D形状，最后生成占用图进行运动规划。

**关键创新**：最重要的创新点在于引入了点云补全模型，能够有效处理因遮挡导致的点云稀疏问题，与现有方法相比，显著提升了抓取的成功率和安全性。

**关键设计**：在技术细节上，采用了特定的损失函数来优化点云补全效果，并设计了适合于草莓形状的网络结构，以确保重建的精度和效率。

## 📊 实验亮点

实验结果显示，该方法在形状重建精度上表现优异，Chamfer距离为1.10mm，抓取成功率达到79.17%，整体成功尝试比率为89.58%。此外，障碍物碰撞率从43.33%降低至13.95%，显示出显著的安全性提升。

## 🎯 应用场景

该研究的潜在应用领域包括农业机器人、自动化采摘系统等，能够显著提高水果采摘的效率和安全性。未来，随着技术的进一步发展，该方法有望推广到其他领域，如复杂环境中的物体抓取和识别。

## 📄 摘要（原文）

> In robotic fruit picking applications, managing object occlusion in unstructured settings poses a substantial challenge for designing grasping algorithms. Using strawberry harvesting as a case study, we present an end-to-end framework for effective object detection, segmentation, and grasp planning to tackle this issue caused by partially occluded objects. Our strategy begins with point cloud denoising and segmentation to accurately locate fruits. To compensate for incomplete scans due to occlusion, we apply a point cloud completion model to create a dense 3D reconstruction of the strawberries. The target selection focuses on ripe strawberries while categorizing others as obstacles, followed by converting the refined point cloud into an occupancy map for collision-aware motion planning. Our experimental results demonstrate high shape reconstruction accuracy, with the lowest Chamfer Distance compared to state-of-the-art methods with 1.10 mm, and significantly improved grasp success rates of 79.17%, yielding an overall success-to-attempt ratio of 89.58\% in real-world strawberry harvesting. Additionally, our method reduces the obstacle hit rate from 43.33% to 13.95%, highlighting its effectiveness in improving both grasp quality and safety compared to prior approaches. This pipeline substantially improves autonomous strawberry harvesting, advancing more efficient and reliable robotic fruit picking systems.

