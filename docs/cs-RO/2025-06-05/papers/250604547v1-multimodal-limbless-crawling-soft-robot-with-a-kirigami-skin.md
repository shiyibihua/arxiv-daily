---
layout: default
title: Multimodal Limbless Crawling Soft Robot with a Kirigami Skin
---

# Multimodal Limbless Crawling Soft Robot with a Kirigami Skin

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04547" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04547v1</a>
  <a href="https://arxiv.org/pdf/2506.04547.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04547v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04547v1', 'Multimodal Limbless Crawling Soft Robot with a Kirigami Skin')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jonathan Tirado, Aida Parvaresh, Burcu Seyidoğlu, Darryl A. Bedford, Jonas Jørgensen, Ahmad Rafsanjani

**分类**: cs.RO

**发布日期**: 2025-06-05

**备注**: Cyborg and Bionic Systems (2025)

**DOI**: [10.34133/cbsystems.0301](https://doi.org/10.34133/cbsystems.0301)

---

## 💡 一句话要点

**提出一种多模态无肢软机器人以解决复杂地形导航问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无肢机器人` `软机器人` `生物启发` `切纸皮` `复杂地形` `自适应控制` `环境监测`

## 📋 核心要点

1. 现有的无肢机器人在复杂地形中的导航能力有限，难以适应多样化的环境和障碍物。
2. 本文提出了一种新型软机器人，结合直线运动与不对称转向步态，能够灵活应对复杂地形。
3. 实验结果表明，该机器人在障碍物丰富的环境中表现出良好的移动能力，能够有效避免碰撞。

## 📝 摘要（中文）

无肢生物能够通过变形身体与地面粗糙度相互作用在平坦表面上爬行，为设计高效的无肢机器人提供了生物启示。受此自然运动的启发，本文提出了一种软机器人，能够通过直线运动和不对称转向步态组合在复杂地形中导航。该机器人由一对对抗性充气软驱动器构成，外覆具有不对称摩擦特性的柔性切纸皮。通过内部腔室的周期性充气和精确的相位偏移实现直线运动，而不对称步态则用于转向，支持原地旋转和大幅转弯。为了验证其在障碍丰富环境中的移动能力，我们在一个包含粗糙基底和多个障碍物的场地中进行了测试。集成在机器人上的实时反馈传感器与人机界面（HMI）结合，实现了自适应控制以避免碰撞。该研究突显了生物启发的软机器人在狭窄或非结构化环境中的应用潜力，如搜索与救援、环境监测和工业检查。

## 🔬 方法详解

**问题定义**：本文旨在解决现有无肢机器人在复杂地形中导航能力不足的问题，现有方法在适应性和灵活性上存在明显不足。

**核心思路**：论文提出了一种结合直线运动和不对称转向步态的软机器人设计，利用生物启示的运动机制来提高导航能力。

**技术框架**：整体架构包括两个主要模块：对抗性充气软驱动器和柔性切纸皮。通过内部腔室的周期性充气实现直线运动，而不对称步态用于实现转向。

**关键创新**：最重要的创新在于采用了不对称摩擦特性的切纸皮，增强了机器人的运动灵活性和适应性，与传统的无肢机器人相比，能够更好地应对复杂环境。

**关键设计**：关键设计包括充气驱动器的相位控制和切纸皮的摩擦特性调节，这些设计使得机器人能够实现高效的直线运动和灵活的转向。实验中采用了实时反馈机制，以优化运动控制。

## 📊 实验亮点

实验结果显示，该软机器人在复杂障碍环境中的移动能力显著提升，能够有效避免碰撞，表现出良好的适应性和灵活性，验证了其在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括搜索与救援、环境监测和工业检查等场景，尤其是在狭窄或复杂的环境中，软机器人能够提供更高的灵活性和适应性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Limbless creatures can crawl on flat surfaces by deforming their bodies and interacting with asperities on the ground, offering a biological blueprint for designing efficient limbless robots. Inspired by this natural locomotion, we present a soft robot capable of navigating complex terrains using a combination of rectilinear motion and asymmetric steering gaits. The robot is made of a pair of antagonistic inflatable soft actuators covered with a flexible kirigami skin with asymmetric frictional properties. The robot's rectilinear locomotion is achieved through cyclic inflation of internal chambers with precise phase shifts, enabling forward progression. Steering is accomplished using an asymmetric gait, allowing for both in-place rotation and wide turns. To validate its mobility in obstacle-rich environments, we tested the robot in an arena with coarse substrates and multiple obstacles. Real-time feedback from onboard proximity sensors, integrated with a human-machine interface (HMI), allowed adaptive control to avoid collisions. This study highlights the potential of bioinspired soft robots for applications in confined or unstructured environments, such as search-and-rescue operations, environmental monitoring, and industrial inspections.

