---
layout: default
title: Effect of Gait Design on Proprioceptive Sensing of Terrain Properties in a Quadrupedal Robot
---

# Effect of Gait Design on Proprioceptive Sensing of Terrain Properties in a Quadrupedal Robot

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22065" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22065v1</a>
  <a href="https://arxiv.org/pdf/2509.22065.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22065v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22065v1', 'Effect of Gait Design on Proprioceptive Sensing of Terrain Properties in a Quadrupedal Robot')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ethan Fulcher, J. Diego Caporale, Yifeng Zhang, John Ruck, Feifei Qian

**分类**: cs.RO, eess.SY

**发布日期**: 2025-09-26

**备注**: 7+1 pages, 5 figures, ICRA Submission This work has been submitted to the IEEE for possible publication

---

## 💡 一句话要点

**步态设计影响四足机器人对地形属性的本体感受，提出适用于行星探测的步态设计方案。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `四足机器人` `步态设计` `地形感知` `本体感受` `行星探测`

## 📋 核心要点

1. 现有行星探测机器人难以在松散地形上高效采样，限制了地质研究的进展。
2. 论文提出通过设计特定的步态，使四足机器人在运动中感知地形属性，提高采样效率。
3. 实验对比了爬行和跑步两种步态，验证了爬行步态在感知地形强度和纹理方面的优势。

## 📝 摘要（中文）

原位机器人探测是增进我们对地球和其他行星地质过程认识的重要工具。为了更好地支持这些移动实验室的运行，理解环境的力学属性至关重要，尤其是在松散、可变形的基底上移动时。最近的研究表明，具有直接驱动和低齿轮比致动器的腿式机器人可以灵敏地检测外部力，因此有潜力在运动过程中用腿测量地形属性，从而提供前所未有的采样速度和密度，并进入以前风险过高而无法采样的地形。本文通过研究步态对本体感受地形感知精度的影响来探索这些想法，特别比较了面向感知的步态（Crawl N' Sense）和面向运动的步态（Trot-Walk）。每种步态测量可变形基底的强度和纹理的能力被量化为机器人在实验室样带上移动的过程，该样带由刚性表面、松散的沙子和带有合成表面结皮的松散沙子组成。结果表明，无论是面向感知的爬行步态还是面向运动的小跑步态，机器人都可以测量低阻和高阻基底之间强度（以抗穿透性衡量）的一致差异；然而，面向运动的小跑步态在测量中包含更大的幅度和方差。此外，较慢的爬行步态能够以比更快的小跑步态高得多的精度检测表面结皮的脆性破裂。我们的结果为腿式机器人“运动中感知”步态设计和规划提供了新的见解，用于侦察地形并在其他世界进行科学测量，以增进我们对其地质和形成的理解。

## 🔬 方法详解

**问题定义**：论文旨在解决四足机器人在松散、可变形地形上进行高效、准确的地形属性感知问题。现有方法主要依赖于静态测量或视觉信息，难以在运动过程中快速获取高密度地形数据。此外，传统的运动步态设计并未考虑地形感知需求，导致感知精度较低。

**核心思路**：论文的核心思路是通过优化四足机器人的步态设计，使其在运动过程中能够更有效地利用腿部的本体感受信息来感知地形属性。通过比较不同的步态，找到一种既能保证运动性能，又能提高地形感知精度的步态。

**技术框架**：论文的整体框架包括以下几个步骤：1）设计两种不同的步态：一种是面向感知的爬行步态（Crawl N' Sense），另一种是面向运动的小跑步态（Trot-Walk）。2）在实验室环境中，构建包含不同地形（刚性表面、松散沙子、带有表面结皮的松散沙子）的样带。3）让四足机器人在样带上以不同的步态运动，并记录腿部的力/扭矩传感器数据。4）分析传感器数据，提取地形属性特征，并评估不同步态下的感知精度。

**关键创新**：论文的关键创新在于提出了“运动中感知”的概念，并将步态设计与地形感知相结合。通过优化步态，使四足机器人能够在运动过程中更有效地感知地形属性，从而提高采样效率和数据密度。此外，论文还定量分析了不同步态对地形感知精度的影响，为未来的步态设计提供了指导。

**关键设计**：论文的关键设计包括：1）面向感知的爬行步态（Crawl N' Sense），其特点是速度慢、接触时间长，有利于更精确地感知地形属性。2）面向运动的小跑步态（Trot-Walk），其特点是速度快、效率高，但可能牺牲感知精度。3）实验中，使用力/扭矩传感器测量腿部与地形的相互作用力，并提取抗穿透性等特征来表征地形属性。

## 📊 实验亮点

实验结果表明，无论是爬行步态还是小跑步态，机器人都能区分低阻和高阻基底。但爬行步态在检测表面结皮的脆性破裂方面，精度显著高于小跑步态。这表明，面向感知的步态设计可以提高机器人对地形细节的感知能力。量化结果为未来腿式机器人的步态设计提供了重要参考。

## 🎯 应用场景

该研究成果可应用于行星探测、灾后搜救、农业机器人等领域。通过优化步态设计，机器人可以在复杂地形上自主导航和采样，提高任务效率和安全性。例如，在火星探测中，机器人可以利用该技术快速评估土壤的力学性质，为后续的钻探和采样提供依据。

## 📄 摘要（原文）

> In-situ robotic exploration is an important tool for advancing knowledge of geological processes that describe the Earth and other Planetary bodies. To inform and enhance operations for these roving laboratories, it is imperative to understand the terramechanical properties of their environments, especially for traversing on loose, deformable substrates. Recent research suggested that legged robots with direct-drive and low-gear ratio actuators can sensitively detect external forces, and therefore possess the potential to measure terrain properties with their legs during locomotion, providing unprecedented sampling speed and density while accessing terrains previously too risky to sample. This paper explores these ideas by investigating the impact of gait on proprioceptive terrain sensing accuracy, particularly comparing a sensing-oriented gait, Crawl N' Sense, with a locomotion-oriented gait, Trot-Walk. Each gait's ability to measure the strength and texture of deformable substrate is quantified as the robot locomotes over a laboratory transect consisting of a rigid surface, loose sand, and loose sand with synthetic surface crusts. Our results suggest that with both the sensing-oriented crawling gait and locomotion-oriented trot gait, the robot can measure a consistent difference in the strength (in terms of penetration resistance) between the low- and high-resistance substrates; however, the locomotion-oriented trot gait contains larger magnitude and variance in measurements. Furthermore, the slower crawl gait can detect brittle ruptures of the surface crusts with significantly higher accuracy than the faster trot gait. Our results offer new insights that inform legged robot "sensing during locomotion" gait design and planning for scouting the terrain and producing scientific measurements on other worlds to advance our understanding of their geology and formation.

