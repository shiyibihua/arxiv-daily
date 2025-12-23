---
layout: default
title: Comparison between External and Internal Single Stage Planetary gearbox actuators for legged robots
---

# Comparison between External and Internal Single Stage Planetary gearbox actuators for legged robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16356" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16356v1</a>
  <a href="https://arxiv.org/pdf/2506.16356.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16356v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16356v1', 'Comparison between External and Internal Single Stage Planetary gearbox actuators for legged robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aman Singh, Deepak Kapa, Prasham Chedda, Shishir N. Y. Kolathaya

**分类**: cs.RO

**发布日期**: 2025-06-19

**备注**: 6 pages, 5 figures, Accepted at Advances in Robotics 2025

---

## 💡 一句话要点

**提出优化设计框架以比较行走机器人用单级行星齿轮驱动器**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `行走机器人` `单级行星齿轮` `驱动器设计` `优化框架` `性能比较` `机械工程` `机器人技术`

## 📋 核心要点

1. 现有的行星齿轮驱动器设计缺乏系统性的优化，通常依赖启发式方法，导致性能不一致。
2. 本文提出了一种设计框架，旨在根据特定性能需求和电机规格，系统地选择驱动器参数并优化设计。
3. 实验结果显示，ISSPG在低齿比范围内表现优越，而在高齿比情况下，ESSPG则是更好的选择，验证了优化模型的有效性。

## 📝 摘要（中文）

行走机器人（如四足和类人机器人）需要高性能的驱动器以实现高效的运动。本文比较了内部单级行星齿轮（ISSPG）和外部单级行星齿轮（ESSPG）驱动器，提出了一种基于性能要求和电机规格的优化设计框架。研究结果表明，在5:1到7:1的低齿比范围内，ISSPG更轻便，而在超过7:1的齿比范围内，ESSPG则表现更佳。通过设计和优化两个驱动器，验证了该方法的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决行走机器人驱动器设计中缺乏系统性比较的问题，现有方法往往依赖启发式设计，导致性能不稳定和效率低下。

**核心思路**：论文提出了一种基于性能需求和电机规格的优化设计框架，通过系统性分析不同齿轮设计，选择最佳驱动器架构。

**技术框架**：整体架构包括性能需求分析、参数选择、设计优化和实验验证四个主要模块，确保设计的科学性和实用性。

**关键创新**：最重要的创新在于提出了一种系统化的设计框架，能够客观比较ISSPG与ESSPG的性能，填补了现有研究的空白。

**关键设计**：在设计过程中，关键参数包括齿比选择、材料强度和驱动器重量等，优化模型通过实验验证与理论预测相符，确保设计的可靠性。

## 📊 实验亮点

实验结果表明，针对T-motor U12电机，ISSPG在5:1到7:1的齿比范围内表现出更轻的设计，而在7:1到11:1的范围内，ESSPG则是更优选择。设计的ISSPG和ESSPG驱动器的质量与优化模型预测值高度一致，验证了方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括四足机器人、类人机器人及其他需要高效驱动的自动化系统。通过优化驱动器设计，可以显著提升机器人的运动效率和负载能力，推动机器人技术的进一步发展。

## 📄 摘要（原文）

> Legged robots, such as quadrupeds and humanoids, require high-performance actuators for efficient locomotion. Quasi-Direct-Drive (QDD) actuators with single-stage planetary gearboxes offer low inertia, high efficiency, and transparency. Among planetary gearbox architectures, Internal (ISSPG) and External Single-Stage Planetary Gearbox (ESSPG) are the two predominant designs. While ISSPG is often preferred for its compactness and high torque density at certain gear ratios, no objective comparison between the two architectures exists. Additionally, existing designs rely on heuristics rather than systematic optimization. This paper presents a design framework for optimally selecting actuator parameters based on given performance requirements and motor specifications. Using this framework, we generate and analyze various optimized gearbox designs for both architectures. Our results demonstrate that for the T-motor U12, ISSPG is the superior choice within the lower gear ratio range of 5:1 to 7:1, offering a lighter design. However, for gear ratios exceeding 7:1, ISSPG becomes infeasible, making ESSPG the better option in the 7:1 to 11:1 range. To validate our approach, we designed and optimized two actuators for manufacturing: an ISSPG with a 6.0:1 gear ratio and an ESSPG with a 7.2:1 gear ratio. Their respective masses closely align with our optimization model predictions, confirming the effectiveness of our methodology.

