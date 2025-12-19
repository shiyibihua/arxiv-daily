---
layout: default
title: OPENTOUCH: Bringing Full-Hand Touch to Real-World Interaction
---

# OPENTOUCH: Bringing Full-Hand Touch to Real-World Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16842" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16842v1</a>
  <a href="https://arxiv.org/pdf/2512.16842.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16842v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16842v1', 'OPENTOUCH: Bringing Full-Hand Touch to Real-World Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxin Ray Song, Jinzhou Li, Rao Fu, Devin Murphy, Kaichen Zhou, Rishi Shiv, Yaqi Li, Haoyu Xiong, Crystal Elaine Owens, Yilun Du, Yiyue Luo, Xianyi Cheng, Antonio Torralba, Wojciech Matusik, Paul Pu Liang

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-12-18

**备注**: https://opentouch-tactile.github.io/

---

## 💡 一句话要点

**OpenTouch：构建真实场景下完整手部触觉交互数据集与基准**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `触觉感知` `多模态学习` `具身智能` `机器人操作` `第一人称视觉` `数据集` `人机交互`

## 📋 核心要点

1. 现有方法缺乏在真实场景下同步第一人称视频与完整手部触觉的数据集，阻碍了视觉感知与物理交互的研究。
2. OpenTouch数据集通过同步视频、触觉和姿势数据，并提供详细文本注释，弥合了视觉感知和物理交互之间的差距。
3. 实验表明，触觉信号在抓取理解、跨模态对齐和视频检索方面表现出强大的能力，为相关研究提供了新的基准。

## 📝 摘要（中文）

人手是与物理世界交互的主要界面，但自我中心感知很少知道何时、何地或以多大力度进行接触。目前缺乏稳健的可穿戴触觉传感器，并且没有现有的真实场景数据集将第一人称视频与完整手部触觉对齐。为了弥合视觉感知和物理交互之间的差距，我们提出了OpenTouch，这是第一个真实场景下的自我中心完整手部触觉数据集，包含5.1小时的同步视频-触觉-姿势数据和2,900个带有详细文本注释的精选片段。利用OpenTouch，我们引入了检索和分类基准，以探究触觉如何扎根于感知和行动。我们表明，触觉信号为抓取理解提供了一个紧凑而强大的线索，加强了跨模态对齐，并且可以从真实场景的视频查询中可靠地检索。通过发布这个带注释的视觉-触觉-姿势数据集和基准，我们的目标是推进多模态自我中心感知、具身学习和富含接触的机器人操作。

## 🔬 方法详解

**问题定义**：现有方法缺乏真实场景下同步的视觉和触觉数据，导致难以研究视觉感知与物理交互之间的关系。特别是在机器人操作和具身智能领域，缺乏高质量的触觉数据阻碍了算法的开发和评估。现有可穿戴触觉传感器不够鲁棒，且缺乏大规模的、带有详细注释的数据集。

**核心思路**：OpenTouch的核心思路是构建一个大规模的、真实场景下的自我中心完整手部触觉数据集，包含同步的视频、触觉和姿势数据，并提供详细的文本注释。通过这个数据集，可以训练和评估多模态模型，从而更好地理解触觉在感知和行动中的作用。

**技术框架**：OpenTouch数据集的构建流程包括数据采集、数据同步、数据标注和数据发布。数据采集使用可穿戴触觉传感器、第一人称相机和姿势捕捉设备，同步记录手部的触觉、视觉和姿势信息。数据标注包括对视频片段进行文本描述，以及对触觉数据进行语义标注。最终，数据集以标准格式发布，方便研究人员使用。

**关键创新**：OpenTouch的关键创新在于它是第一个真实场景下的自我中心完整手部触觉数据集。与现有的数据集相比，OpenTouch具有更大的规模、更丰富的场景和更详细的注释。此外，OpenTouch还提供了一系列的基准测试，方便研究人员评估自己的算法。

**关键设计**：OpenTouch数据集包含5.1小时的同步视频-触觉-姿势数据和2,900个带有详细文本注释的精选片段。触觉传感器采用高分辨率的触觉阵列，能够捕捉手部各个部位的触觉信息。视频数据采用高帧率的第一人称相机，能够清晰地记录手部的动作。姿势数据采用高精度的姿势捕捉设备，能够准确地估计手部的姿势。数据集的标注采用人工标注和自动标注相结合的方式，保证了标注的质量和效率。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16842v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16842v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16842v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

OpenTouch数据集被用于检索和分类基准测试，结果表明触觉信号在抓取理解方面表现出强大的能力。触觉信息能够有效提升跨模态对齐的性能，并且可以从真实场景的视频查询中可靠地检索。这些实验结果验证了OpenTouch数据集的价值和潜力。

## 🎯 应用场景

OpenTouch数据集的应用场景广泛，包括机器人操作、具身智能、人机交互、虚拟现实和增强现实等领域。例如，可以利用OpenTouch数据集训练机器人，使其能够更好地理解和操作物体。还可以利用OpenTouch数据集开发更自然、更直观的人机交互界面。此外，OpenTouch数据集还可以用于研究人类的触觉感知机制。

## 📄 摘要（原文）

> The human hand is our primary interface to the physical world, yet egocentric perception rarely knows when, where, or how forcefully it makes contact. Robust wearable tactile sensors are scarce, and no existing in-the-wild datasets align first-person video with full-hand touch. To bridge the gap between visual perception and physical interaction, we present OpenTouch, the first in-the-wild egocentric full-hand tactile dataset, containing 5.1 hours of synchronized video-touch-pose data and 2,900 curated clips with detailed text annotations. Using OpenTouch, we introduce retrieval and classification benchmarks that probe how touch grounds perception and action. We show that tactile signals provide a compact yet powerful cue for grasp understanding, strengthen cross-modal alignment, and can be reliably retrieved from in-the-wild video queries. By releasing this annotated vision-touch-pose dataset and benchmark, we aim to advance multimodal egocentric perception, embodied learning, and contact-rich robotic manipulation.

