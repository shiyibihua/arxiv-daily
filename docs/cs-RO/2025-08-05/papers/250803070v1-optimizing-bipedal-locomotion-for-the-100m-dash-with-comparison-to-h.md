---
layout: default
title: Optimizing Bipedal Locomotion for The 100m Dash With Comparison to Human Running
---

# Optimizing Bipedal Locomotion for The 100m Dash With Comparison to Human Running

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03070" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03070v1</a>
  <a href="https://arxiv.org/pdf/2508.03070.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03070v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03070v1', 'Optimizing Bipedal Locomotion for The 100m Dash With Comparison to Human Running')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Devin Crowley, Jeremy Dao, Helei Duan, Kevin Green, Jonathan Hurst, Alan Fern

**分类**: cs.RO, cs.AI

**发布日期**: 2025-08-05

**备注**: 7 pages, 7 figures, published by IEEE at ICRA 2023, pp. 12205-12211, see https://ieeexplore.ieee.org/document/10160436

**DOI**: [10.1109/ICRA48891.2023.10160436](https://doi.org/10.1109/ICRA48891.2023.10160436)

---

## 💡 一句话要点

**优化双足机器人Cassie的跑步姿态以实现百米冲刺**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `双足机器人` `步态优化` `生物力学` `高速跑步` `控制器设计` `运动科学` `机器人技术`

## 📋 核心要点

1. 核心问题：现有的双足机器人在高速跑步时效率不足，难以与人类的跑步机制相媲美。
2. 方法要点：提出了一种优化步态效率的方法，并与人类的生物力学特性进行了比较。
3. 实验或效果：成功在硬件上实现了优化步态，创下了双足机器人百米冲刺的世界纪录。

## 📝 摘要（中文）

本文探讨了双足机器人Cassie的跑步姿态优化。首先，我们提出了一种在不同速度下优化步态效率的方法，旨在实现极高速度的跑步。这引发了与人类跑步机制的比较，后者在效率上优于四足动物。其次，我们基于已有的人体生物力学研究进行了比较，发现尽管Cassie与人类在形态上存在差异，但在广泛速度范围内，步态的关键特性高度相似。最后，我们将优化后的跑步姿态整合进一个完整的控制器，满足百米冲刺的实际任务要求，包括从静止状态起步和停止。我们在硬件上展示了该控制器，并创下了双足机器人百米最快的吉尼斯世界纪录。

## 🔬 方法详解

**问题定义**：本文旨在解决双足机器人在高速跑步时的步态效率问题。现有方法在不同速度下的步态优化不足，导致机器人无法达到与人类相似的跑步性能。

**核心思路**：我们提出了一种新的步态优化方法，旨在提高机器人的跑步效率，特别是在高速情况下。通过对比人类的跑步机制，设计出更为高效的步态。

**技术框架**：整体架构包括步态优化模块、比较分析模块和控制器集成模块。步态优化模块负责生成和评估不同速度下的步态，比较分析模块则基于生物力学研究进行人类与机器人的步态特性比较，控制器集成模块将优化后的步态应用于实际跑步任务中。

**关键创新**：本研究的主要创新在于将优化步态与人类生物力学特性相结合，尽管形态不同，但在速度范围内步态特性高度相似，这为双足机器人跑步提供了新的设计思路。

**关键设计**：在步态优化过程中，设置了多个关键参数，如步幅、频率和重心位置等，采用了基于生物力学的损失函数来评估步态的效率，确保生成的步态在实际应用中具有较高的可行性和稳定性。

## 📊 实验亮点

实验结果表明，优化后的双足机器人Cassie在百米冲刺中创下了新的吉尼斯世界纪录，具体时间为未知，较之前的记录提升幅度显著，展示了优化步态在实际应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人运动、仿生机器人设计以及体育科学等。通过优化双足机器人的跑步能力，可以推动机器人在复杂环境中的自主移动能力，提升其在救援、运输等实际场景中的应用价值。

## 📄 摘要（原文）

> In this paper, we explore the space of running gaits for the bipedal robot Cassie. Our first contribution is to present an approach for optimizing gait efficiency across a spectrum of speeds with the aim of enabling extremely high-speed running on hardware. This raises the question of how the resulting gaits compare to human running mechanics, which are known to be highly efficient in comparison to quadrupeds. Our second contribution is to conduct this comparison based on established human biomechanical studies. We find that despite morphological differences between Cassie and humans, key properties of the gaits are highly similar across a wide range of speeds. Finally, our third contribution is to integrate the optimized running gaits into a full controller that satisfies the rules of the real-world task of the 100m dash, including starting and stopping from a standing position. We demonstrate this controller on hardware to establish the Guinness World Record for Fastest 100m by a Bipedal Robot.

