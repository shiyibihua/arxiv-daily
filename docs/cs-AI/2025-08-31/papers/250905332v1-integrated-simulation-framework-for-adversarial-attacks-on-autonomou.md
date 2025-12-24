---
layout: default
title: Integrated Simulation Framework for Adversarial Attacks on Autonomous Vehicles
---

# Integrated Simulation Framework for Adversarial Attacks on Autonomous Vehicles

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05332" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05332v1</a>
  <a href="https://arxiv.org/pdf/2509.05332.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05332v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05332v1', 'Integrated Simulation Framework for Adversarial Attacks on Autonomous Vehicles')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Christos Anagnostopoulos, Ioulia Kapsali, Alexandros Gkillas, Nikos Piperigkos, Aris S. Lalos

**分类**: cs.CR, cs.AI

**发布日期**: 2025-08-31

**备注**: 6 pages, 2 figures

---

## 💡 一句话要点

**提出集成仿真框架以应对自动驾驶车辆的对抗攻击问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `自动驾驶` `对抗攻击` `仿真框架` `感知系统` `通信安全` `ROS 2` `安全性测试`

## 📋 核心要点

1. 现有仿真框架在建模多领域对抗攻击场景方面存在不足，无法全面测试自动驾驶车辆的鲁棒性。
2. 本文提出的集成仿真框架能够生成针对感知和通信层的对抗攻击，支持高保真度的环境建模。
3. 实验结果显示，生成的对抗场景对先进3D目标检测器造成显著性能下降，验证了框架的有效性。

## 📝 摘要（中文）

自动驾驶车辆（AV）依赖复杂的感知和通信系统，使其易受对抗攻击，影响安全性。虽然仿真提供了可扩展且安全的环境用于鲁棒性测试，但现有框架通常缺乏对多领域对抗场景的全面建模支持。本文提出了一种新颖的开源集成仿真框架，旨在生成针对AV感知和通信层的对抗攻击。该框架提供高保真度的物理环境、交通动态和V2X网络建模，通过统一核心协调多个模拟器，基于单一配置文件进行同步。我们的实现支持对LiDAR传感器数据的多样化感知级攻击，以及V2X消息操控和GPS欺骗等通信级威胁。此外，ROS 2集成确保与第三方AV软件栈的无缝兼容。我们通过评估生成的对抗场景对先进3D目标检测器的影响，展示了框架的有效性，揭示在现实条件下显著的性能下降。

## 🔬 方法详解

**问题定义**：本文旨在解决现有自动驾驶车辆仿真框架在对抗攻击建模方面的不足，尤其是缺乏对多领域场景的全面支持。现有方法无法有效测试AV在复杂环境下的鲁棒性，导致安全隐患。

**核心思路**：论文提出了一种集成仿真框架，通过高保真度的环境建模和多种攻击场景的生成，增强对抗攻击的测试能力。设计上，框架通过统一核心协调多个模拟器，简化了配置和操作。

**技术框架**：整体架构包括物理环境建模、交通动态模拟和V2X网络集成三个主要模块。框架通过单一配置文件实现对多个模拟器的同步，确保各模块间的高效协作。

**关键创新**：最重要的技术创新在于框架的开放性和集成性，能够同时针对感知和通信层进行攻击模拟，与现有方法相比，提供了更全面的测试能力。

**关键设计**：框架支持多种感知级攻击（如对LiDAR数据的干扰）和通信级威胁（如V2X消息操控和GPS欺骗），并通过ROS 2实现与第三方软件的兼容性，确保灵活性和可扩展性。

## 📊 实验亮点

实验结果表明，生成的对抗场景对先进3D目标检测器造成了显著的性能下降，具体表现为在真实条件下检测精度降低了XX%。这一发现强调了对抗攻击在自动驾驶系统中的潜在威胁，验证了框架的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶车辆的安全性测试、对抗攻击的防御策略开发以及智能交通系统的安全评估。通过提供一个全面的仿真环境，研究者和开发者可以更好地理解和应对自动驾驶技术面临的安全挑战，推动行业的健康发展。

## 📄 摘要（原文）

> Autonomous vehicles (AVs) rely on complex perception and communication systems, making them vulnerable to adversarial attacks that can compromise safety. While simulation offers a scalable and safe environment for robustness testing, existing frameworks typically lack comprehensive supportfor modeling multi-domain adversarial scenarios. This paper introduces a novel, open-source integrated simulation framework designed to generate adversarial attacks targeting both perception and communication layers of AVs. The framework provides high-fidelity modeling of physical environments, traffic dynamics, and V2X networking, orchestrating these components through a unified core that synchronizes multiple simulators based on a single configuration file. Our implementation supports diverse perception-level attacks on LiDAR sensor data, along with communication-level threats such as V2X message manipulation and GPS spoofing. Furthermore, ROS 2 integration ensures seamless compatibility with third-party AV software stacks. We demonstrate the framework's effectiveness by evaluating the impact of generated adversarial scenarios on a state-of-the-art 3D object detector, revealing significant performance degradation under realistic conditions.

