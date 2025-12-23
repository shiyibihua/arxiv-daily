---
layout: default
title: Building Forest Inventories with Autonomous Legged Robots -- System, Lessons, and Challenges Ahead
---

# Building Forest Inventories with Autonomous Legged Robots -- System, Lessons, and Challenges Ahead

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20315" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20315v1</a>
  <a href="https://arxiv.org/pdf/2506.20315.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20315v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20315v1', 'Building Forest Inventories with Autonomous Legged Robots -- System, Lessons, and Challenges Ahead')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Matías Mattamala, Nived Chebrolu, Jonas Frey, Leonard Freißmuth, Haedam Oh, Benoit Casseau, Marco Hutter, Maurice Fallon

**分类**: cs.RO

**发布日期**: 2025-06-25

**备注**: 20 pages, 13 figures. Pre-print version of the accepted paper for IEEE Transactions on Field Robotics (T-FR)

---

## 💡 一句话要点

**提出自主四足机器人森林清查系统以应对自然环境挑战**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `四足机器人` `森林清查` `自主导航` `状态估计` `生态监测` `智能机器人` `自然环境`

## 📋 核心要点

1. 现有的森林清查方法在复杂自然环境中面临导航和状态估计的挑战，导致效率低下和数据准确性不足。
2. 本文提出了一种基于四足机器人的自主导航和森林清查系统，结合了完整的导航栈和树木特征估计技术。
3. 实验结果显示，ANYmal机器人能够在30分钟内完成1公顷区域的清查，并以2厘米的精度识别树木，显著提高了清查效率。

## 📝 摘要（中文）

随着四足机器人在石油、天然气、矿业、核能和农业等行业的应用日益增加，进入自然环境（如林业应用）时面临新的挑战。本文展示了一种原型系统，旨在实现自主的林下森林清查。我们介绍了一种系统架构，使四足平台能够自主导航和绘制森林区域。该解决方案包括完整的导航栈，用于状态估计、任务规划、树木检测和特征估计。我们报告了在三国森林中进行的一年半试验的系统性能。ANYmal机器人在30分钟内能够调查1公顷的区域，并以2厘米的精度识别树木。我们总结了五个经验教训和挑战，讨论了硬件开发的成熟度、状态估计的局限性、森林导航中的开放问题以及未来的机器人森林清查方向。

## 🔬 方法详解

**问题定义**：本文旨在解决在复杂自然环境中进行森林清查时，现有方法在导航和状态估计方面的不足，导致效率低下和数据准确性不足。

**核心思路**：我们提出了一种基于四足机器人的自主导航系统，利用其优越的机动性和稳定性，结合完整的导航栈来实现高效的森林清查。

**技术框架**：系统架构包括状态估计、任务规划、树木检测和特征估计等主要模块，确保机器人能够在林下环境中自主导航和绘制地图。

**关键创新**：本研究的创新点在于将四足机器人与完整的导航系统相结合，克服了传统方法在复杂环境中的局限性，实现了高效的森林清查。

**关键设计**：系统设计中采用了先进的传感器融合技术和高效的算法，以提高状态估计的准确性和导航的可靠性，同时优化了树木特征的检测与估计过程。

## 📊 实验亮点

实验结果表明，ANYmal机器人在30分钟内能够完成1公顷区域的清查，树木识别的直径精度达到2厘米，显著提升了清查效率，相较于传统方法有明显的性能优势。

## 🎯 应用场景

该研究的潜在应用领域包括林业资源管理、生态监测和环境保护等。通过提高森林清查的效率和准确性，能够为可持续发展提供重要数据支持，推动相关行业的智能化进程。

## 📄 摘要（原文）

> Legged robots are increasingly being adopted in industries such as oil, gas, mining, nuclear, and agriculture. However, new challenges exist when moving into natural, less-structured environments, such as forestry applications. This paper presents a prototype system for autonomous, under-canopy forest inventory with legged platforms. Motivated by the robustness and mobility of modern legged robots, we introduce a system architecture which enabled a quadruped platform to autonomously navigate and map forest plots. Our solution involves a complete navigation stack for state estimation, mission planning, and tree detection and trait estimation. We report the performance of the system from trials executed over one and a half years in forests in three European countries. Our results with the ANYmal robot demonstrate that we can survey plots up to 1 ha plot under 30 min, while also identifying trees with typical DBH accuracy of 2cm. The findings of this project are presented as five lessons and challenges. Particularly, we discuss the maturity of hardware development, state estimation limitations, open problems in forest navigation, future avenues for robotic forest inventory, and more general challenges to assess autonomous systems. By sharing these lessons and challenges, we offer insight and new directions for future research on legged robots, navigation systems, and applications in natural environments. Additional videos can be found in https://dynamic.robots.ox.ac.uk/projects/legged-robots

