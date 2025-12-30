---
layout: default
title: "Towards the Automation in the Space Station: Feasibility Study and Ground Tests of a Multi-Limbed Intra-Vehicular Robot"
---

# Towards the Automation in the Space Station: Feasibility Study and Ground Tests of a Multi-Limbed Intra-Vehicular Robot

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23153" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23153v1</a>
  <a href="https://arxiv.org/pdf/2512.23153.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23153v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23153v1', 'Towards the Automation in the Space Station: Feasibility Study and Ground Tests of a Multi-Limbed Intra-Vehicular Robot')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seiko Piotr Yamaguchi, Kentaro Uno, Yasumaru Fujii, Masazumi Imai, Kazuki Takada, Taku Okawara, Kazuya Yoshida

**分类**: cs.RO

**发布日期**: 2025-12-29

**备注**: Author's version of a manuscript accepted at the 2025 IEEE/SICE International Symposium on System Integration (SII). (c) IEEE. The final published version is available at https://doi.org/10.1109/SII59315.2025.10870890

**DOI**: [10.1109/SII59315.2025.10870890](https://doi.org/10.1109/SII59315.2025.10870890)

---

## 💡 一句话要点

**面向空间站的自动化：多臂舱内机器人的可行性研究与地面测试**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `空间站自动化` `多臂机器人` `移动操作` `运动规划` `微重力环境`

## 📋 核心要点

1. 宇航员在空间站的后勤任务耗费大量时间，降低了执行关键任务的效率，亟需自动化解决方案。
2. 论文提出一种多臂舱内机器人（MLIVR），旨在通过自主移动操作来辅助宇航员完成物资运输等任务。
3. 通过仿真和2D桌面原型测试，验证了MLIVR在微重力环境下执行运输任务的可行性，减少人工干预。

## 📝 摘要（中文）

本文提出了一项关于多臂舱内机器人（MLIVR）自主运行的可行性研究，包括仿真和原型测试。该机器人旨在协助国际空间站（ISS）上的宇航员完成后勤任务。宇航员花费大量时间在准备、结束、以及物资的收集和运输等任务上，从而减少了关键任务的可用时间。我们的研究探讨了移动机械臂支持这些操作的潜力，强调自主功能对于最大限度地减少宇航员和地面操作员的工作量，同时实现实时任务执行的必要性。我们专注于机器人的运输能力，在3D空间中模拟其运动规划。实际的运动执行通过在2D桌面上使用原型来模拟微重力环境进行测试。结果表明，在最少的人工干预下执行这些任务是可行的，为提高国际空间站的运行效率提供了一个有希望的解决方案。

## 🔬 方法详解

**问题定义**：论文旨在解决国际空间站内宇航员在后勤任务中耗时过长的问题。现有方法依赖于宇航员手动操作，效率低下，且占用了宇航员执行关键任务的时间。因此，需要一种自动化解决方案来减轻宇航员的负担，提高空间站的整体运行效率。

**核心思路**：论文的核心思路是利用多臂移动机器人（MLIVR）的自主移动和操作能力，代替宇航员完成重复性的后勤任务，如物资的收集、运输和整理。通过自主运动规划和控制，MLIVR能够在空间站内部自主导航，并利用机械臂抓取和搬运物体。

**技术框架**：该研究的技术框架主要包括以下几个阶段：1) 任务需求分析：确定空间站内需要自动化的后勤任务类型和操作要求。2) 机器人设计：设计具有多臂和移动底盘的MLIVR，使其具备足够的灵活性和操作能力。3) 运动规划与控制：开发自主运动规划算法，使MLIVR能够在空间站内部安全、高效地导航和操作。4) 仿真验证：在3D仿真环境中模拟MLIVR的运动和操作，验证其可行性和性能。5) 原型测试：构建MLIVR原型，并在2D桌面环境中模拟微重力环境，进行实际的运动和操作测试。

**关键创新**：该研究的关键创新在于将多臂移动机器人应用于空间站内部的后勤任务自动化。与传统的固定式机器人相比，MLIVR具有更强的灵活性和适应性，能够适应空间站内部复杂的环境。此外，该研究还探索了在微重力环境下进行机器人运动规划和控制的方法。

**关键设计**：论文中没有详细说明具体的参数设置、损失函数或网络结构等技术细节。但是，可以推断，运动规划算法需要考虑空间站内部的障碍物和约束条件，以及机器人的运动学和动力学特性。控制算法需要保证机器人的稳定性和精度，并能够适应微重力环境的影响。原型测试中，2D桌面模拟微重力环境的方式是关键设计，需要保证摩擦力等因素与真实环境尽可能接近。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23153v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23153v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23153v1/fig/flow-r1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该研究通过仿真和2D桌面原型测试，验证了多臂舱内机器人（MLIVR）在空间站内部执行运输任务的可行性。虽然没有给出具体的性能数据，但实验结果表明，MLIVR能够在最少的人工干预下完成任务，为空间站的自动化操作提供了一种有希望的解决方案。

## 🎯 应用场景

该研究成果可应用于国际空间站及未来的深空探测任务中，减轻宇航员的后勤负担，提高任务效率。此外，该技术还可应用于其他受限空间内的自动化操作，如核电站维护、灾难救援等领域，具有重要的实际应用价值和广阔的发展前景。

## 📄 摘要（原文）

> This paper presents a feasibility study, including simulations and prototype tests, on the autonomous operation of a multi-limbed intra-vehicular robot (mobile manipulator), shortly MLIVR, designed to assist astronauts with logistical tasks on the International Space Station (ISS). Astronauts spend significant time on tasks such as preparation, close-out, and the collection and transportation of goods, reducing the time available for critical mission activities. Our study explores the potential for a mobile manipulator to support these operations, emphasizing the need for autonomous functionality to minimize crew and ground operator effort while enabling real-time task execution. We focused on the robot's transportation capabilities, simulating its motion planning in 3D space. The actual motion execution was tested with a prototype on a 2D table to mimic a microgravity environment. The results demonstrate the feasibility of performing these tasks with minimal human intervention, offering a promising solution to enhance operational efficiency on the ISS.

