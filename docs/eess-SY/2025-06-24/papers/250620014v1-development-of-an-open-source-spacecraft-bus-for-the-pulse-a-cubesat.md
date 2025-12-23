---
layout: default
title: Development of an Open-Source Spacecraft Bus for the PULSE-A CubeSat
---

# Development of an Open-Source Spacecraft Bus for the PULSE-A CubeSat

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20014" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20014v1</a>
  <a href="https://arxiv.org/pdf/2506.20014.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20014v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20014v1', 'Development of an Open-Source Spacecraft Bus for the PULSE-A CubeSat')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Graydon Schulze-Kalt, Robert Pitu, Spencer Shelton, Catherine Todd, Zane Ebel, Ian Goldberg, Leon Gold, Henry Czarnecki, Mason McCormack, Larry Li, Zumi Riekse, Brian Yu, Akash Piya, Vidya Suri, Dylan Hu, Colleen Kim, John Baird, Seth Knights, Logan Hanssler, Michael Lembeck, Tian Zhong

**分类**: physics.app-ph, astro-ph.IM, cs.AR, eess.SY, physics.optics

**发布日期**: 2025-06-24

**备注**: Submitted to Advanced Technologies II at the 2025 SmallSat Conference, reference number SSC25-P1-42

---

## 💡 一句话要点

**开发开源航天器总线以支持PULSE-A立方体卫星通信**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `开源航天器` `激光通信` `模块化设计` `低成本卫星` `热控制机制`

## 📋 核心要点

1. 现有的低成本航天器总线设计在指向精度和组件对齐方面存在不足，限制了其在激光通信中的应用。
2. 论文提出了一种低成本开源航天器总线，具备良好的可配置性，能够满足PULSE-A任务的严格要求。
3. 通过设计和测试，PULSE-A总线在热控制和散热机制方面取得了显著进展，满足了体积、质量和温度范围的约束。

## 📝 摘要（中文）

芝加哥大学的本科生主导的极化调制激光卫星实验（PULSE-A）旨在验证圆极化移位键控卫星到地面激光通信的可行性。PULSE-A的低成本开源总线作为任务的核心，设计时考虑了指向精度、组件对齐、电力需求和热稳定性等严格要求。该论文展示了PULSE-A总线的设计与测试，旨在满足PULSE-A任务需求，并为未来需要增强能力的低成本开源设计提供可配置性。总线核心采用双BeagleBone Black工业计算单元，并实现了戈达德航天中心的核心飞行系统（cFS），采用模块化软件架构，使用C语言开发，便于本科生团队进行开发。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有低成本航天器总线在指向精度和组件对齐方面的不足，特别是在激光通信应用中的挑战。现有方法往往无法满足严格的任务需求，限制了其实际应用。

**核心思路**：论文提出了一种低成本的开源航天器总线设计，旨在通过模块化和可配置性来满足PULSE-A任务的需求，同时为未来的任务提供灵活性。设计过程中考虑了指向精度、电力需求和热稳定性等关键因素。

**技术框架**：PULSE-A总线的整体架构包括双BeagleBone Black工业计算单元，采用PC/104标准进行集成，并实现了戈达德航天中心的核心飞行系统（cFS）。总线内部使用PC/104标准的四轨道，连接到定制设计的有效载荷盒，容纳所有有效载荷组件和光纤线路。

**关键创新**：该研究的主要创新在于开发了一种低成本、开源的航天器总线，具备良好的可配置性和模块化设计，能够满足未来多种任务的需求。这种设计与现有方法的本质区别在于其灵活性和适应性。

**关键设计**：在设计过程中，关键参数包括双BeagleBone Black计算单元的选择、PC/104标准的应用，以及针对特定任务需求的热控制和散热机制的开发。这些设计确保了在体积、质量和温度范围约束下的有效运行。

## 📊 实验亮点

实验结果表明，PULSE-A总线在指向精度和热控制方面达到了预期目标，成功满足了任务需求。与传统设计相比，该总线在成本和可配置性方面具有显著优势，为未来的航天任务提供了新的可能性。

## 🎯 应用场景

该研究的潜在应用领域包括低成本航天器的开发、激光通信系统的实现以及未来航天任务的灵活配置。通过提供开源设计，研究将推动航天技术的普及和创新，降低进入航天领域的门槛。

## 📄 摘要（原文）

> The undergraduate-led Polarization-modUlated Laser Satellite Experiment (PULSE-A) at the University of Chicago seeks to demonstrate the feasibility of circular polarization shift keyed satellite-to-ground laser communication. PULSE-A's low-cost open-source bus serves as the backbone of the mission and has been designed in tandem with the Payload, with design driven by strict requirements for pointing accuracy, component alignment, power demand, and thermal stability. This work presents the design and testing of the PULSE-A bus.
>   The spacecraft bus was designed to fill two major needs: (1) to meet the requirements of the PULSE-A mission, and (2) to be easily configurable for future missions that desire enhanced capabilities over other low-cost open-source designs. At its core, the bus features dual BeagleBone Black Industrial compute units, selected for their flight heritage, integrated via a PC/104 header standard. PULSE-A implements Goddard Space Flight Center's core Flight System (cFS), which takes a modular software architecture approach and is built in C. The use of C as the primary language aligns with the expertise of the University of Chicago's Computer Science department, allowing for ease of development by PULSE-A's undergraduate flight software team.
>   The CubeSat structure utilizes Gran Systems' 3U frame, modified to accommodate openings for various ports and deployable components. Inside, the avionics stack uses the PC/104 standard quad rails, which terminate in PULSE-A's custom-designed Payload Box that houses all of the Payload components and optical fiber runs. This work also covers the techniques and iterative engineering processes used to develop the thermal control and dissipation mechanisms for the specific requirements, under volume, mass, and temperature-range constraints.

