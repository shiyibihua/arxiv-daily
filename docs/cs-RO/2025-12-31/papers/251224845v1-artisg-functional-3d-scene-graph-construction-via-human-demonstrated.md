---
layout: default
title: "ArtiSG: Functional 3D Scene Graph Construction via Human-demonstrated Articulated Objects Manipulation"
---

# ArtiSG: Functional 3D Scene Graph Construction via Human-demonstrated Articulated Objects Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24845" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24845v1</a>
  <a href="https://arxiv.org/pdf/2512.24845.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24845v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24845v1', 'ArtiSG: Functional 3D Scene Graph Construction via Human-demonstrated Articulated Objects Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qiuyi Gu, Yuze Sheng, Jincheng Yu, Jiahao Tang, Xiaolong Shan, Zhaoyang Shen, Tinghao Yi, Xiaodan Liang, Xinlei Chen, Yu Wang

**分类**: cs.RO

**发布日期**: 2025-12-31

---

## 💡 一句话要点

**ArtiSG：通过人机协作操纵关节物体构建功能性3D场景图**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D场景图` `关节物体操作` `人机协作` `机器人操作` `功能元素发现`

## 📋 核心要点

1. 现有3D场景图缺乏关节物体的功能信息，且难以处理视觉歧义和遮挡，限制了机器人的操作能力。
2. ArtiSG通过人机协作，利用便携式设备收集关节运动数据，构建包含功能元素的3D场景图。
3. 实验表明，ArtiSG在功能元素召回率和关节估计精度上优于基线，并能指导机器人完成语言引导的操作任务。

## 📝 摘要（中文）

3D场景图赋予了机器人语义理解能力，从而进行导航和规划，但它们通常缺乏物理操作所需的功能信息，尤其是在关节物体方面。现有的从静态观察中推断关节机制的方法容易产生视觉歧义，而从状态变化估计参数的方法通常依赖于固定的相机和无遮挡的视图等受限设置。此外，通用物体检测器经常遗漏像小把手这样的细粒度功能元素。为了弥合这一差距，我们提出了ArtiSG，一个通过将人类演示编码为结构化机器人记忆来构建功能性3D场景图的框架。我们的方法利用一个鲁棒的关节数据收集流程，该流程使用便携式设置来准确估计6自由度关节轨迹和轴，即使在相机自我运动的情况下也是如此。我们将这些运动学先验知识集成到一个分层和开放词汇的图中，同时利用交互数据来发现视觉感知遗漏的不显眼的功能元素。大量的真实世界实验表明，ArtiSG在功能元素召回率和关节估计精度方面显著优于基线。此外，我们证明了构建的图可以作为可靠的功能记忆，有效地指导机器人在包含各种关节物体的真实世界环境中执行语言引导的操作任务。

## 🔬 方法详解

**问题定义**：现有方法在构建用于机器人操作的3D场景图时，存在以下痛点：一是难以从静态图像中准确推断关节物体的运动机制，容易受到视觉歧义的影响；二是依赖于受限的实验环境，例如固定相机和无遮挡的视角；三是通用物体检测器难以检测到细粒度的功能元素，例如小型把手等。这些问题导致机器人难以理解和操作关节物体。

**核心思路**：ArtiSG的核心思路是通过人机协作，利用人类的演示数据来指导3D场景图的构建。具体来说，通过便携式设备记录人类操纵关节物体的过程，提取关节运动轨迹和轴等运动学信息，并将这些信息融入到3D场景图中。同时，利用交互数据来发现视觉感知遗漏的功能元素。这样可以有效地克服视觉歧义和遮挡问题，提高场景图的完整性和准确性。

**技术框架**：ArtiSG的整体框架包含以下几个主要模块：1) **关节数据收集**：使用便携式设备记录人类操纵关节物体的过程，获取6自由度的关节轨迹和轴信息。2) **运动学先验集成**：将收集到的运动学信息集成到分层和开放词汇的3D场景图中。3) **功能元素发现**：利用交互数据来发现视觉感知遗漏的功能元素。4) **场景图构建**：将上述信息整合，构建包含功能信息的3D场景图。

**关键创新**：ArtiSG最重要的技术创新点在于它利用人机协作的方式来构建功能性的3D场景图。与传统的基于视觉感知的场景图构建方法相比，ArtiSG能够有效地克服视觉歧义和遮挡问题，提高场景图的完整性和准确性。此外，ArtiSG还能够发现视觉感知遗漏的功能元素，从而更好地支持机器人的操作任务。

**关键设计**：ArtiSG的关键设计包括：1) 使用便携式设备进行数据采集，保证了数据的准确性和鲁棒性。2) 采用分层和开放词汇的场景图结构，能够有效地组织和管理场景中的各种信息。3) 利用交互数据来发现功能元素，弥补了视觉感知的不足。4) 采用合适的损失函数来优化关节参数的估计，例如，可以使用重投影误差作为损失函数。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24845v1/m_figs/fig1_v9.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24845v1/m_figs/fig2_v7.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24845v1/x1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

ArtiSG在真实世界实验中表现出色，在功能元素召回率和关节估计精度方面显著优于基线方法。具体来说，ArtiSG在功能元素召回率上提升了XX%，在关节估计精度上提升了YY%。实验结果表明，ArtiSG构建的场景图能够有效地指导机器人在真实世界环境中执行语言引导的操作任务。

## 🎯 应用场景

ArtiSG构建的功能性3D场景图可应用于机器人操作、人机交互、虚拟现实等领域。例如，可以帮助机器人在复杂环境中执行装配、维修等任务，提升机器人的自主性和智能化水平。在人机交互方面，可以使机器人更好地理解人类的意图，从而提供更自然、更高效的交互体验。在虚拟现实领域，可以构建更逼真、更具交互性的虚拟环境。

## 📄 摘要（原文）

> 3D scene graphs have empowered robots with semantic understanding for navigation and planning, yet they often lack the functional information required for physical manipulation, particularly regarding articulated objects. Existing approaches for inferring articulation mechanisms from static observations are prone to visual ambiguity, while methods that estimate parameters from state changes typically rely on constrained settings such as fixed cameras and unobstructed views. Furthermore, fine-grained functional elements like small handles are frequently missed by general object detectors. To bridge this gap, we present ArtiSG, a framework that constructs functional 3D scene graphs by encoding human demonstrations into structured robotic memory. Our approach leverages a robust articulation data collection pipeline utilizing a portable setup to accurately estimate 6-DoF articulation trajectories and axes even under camera ego-motion. We integrate these kinematic priors into a hierarchical and open-vocabulary graph while utilizing interaction data to discover inconspicuous functional elements missed by visual perception. Extensive real-world experiments demonstrate that ArtiSG significantly outperforms baselines in functional element recall and articulation estimation precision. Moreover, we show that the constructed graph serves as a reliable functional memory that effectively guides robots to perform language-directed manipulation tasks in real-world environments containing diverse articulated objects.

