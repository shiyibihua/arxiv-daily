---
layout: default
title: Control of a commercial vehicle by a tetraplegic human using a bimanual brain-computer interface
---

# Control of a commercial vehicle by a tetraplegic human using a bimanual brain-computer interface

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11805" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11805v1</a>
  <a href="https://arxiv.org/pdf/2508.11805.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11805v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11805v1', 'Control of a commercial vehicle by a tetraplegic human using a bimanual brain-computer interface')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinyun Zou, Jorge Gamez, Meghna Menon, Phillip Ring, Chadwick Boulay, Likhith Chitneni, Jackson Brennecke, Shana R. Melby, Gracy Kureel, Kelsie Pejsa, Emily R. Rosario, Ausaf A. Bari, Aniruddh Ravindran, Tyson Aflalo, Spencer S. Kellis, Dimitar Filev, Florian Solzbacher, Richard A. Andersen

**分类**: eess.SY, cs.NE, cs.RO

**发布日期**: 2025-08-15

**备注**: 41 pages, 7 figures, 1 table. 22 supplementary pages, 6 supplementary figures, 11 supplementary tables, 9 supplementary movies available as ancillary files

---

## 💡 一句话要点

**提出双手脑机接口以解决四肢瘫痪者驾驶问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `脑机接口` `四肢瘫痪` `车辆驾驶` `神经信号解码` `远程控制` `智能交通` `康复技术`

## 📋 核心要点

1. 现有脑机接口技术主要应用于实验室，缺乏实际驾驶场景的有效实现。
2. 论文提出了一种双手BCI系统，能够在模拟和真实环境中实现车辆驾驶，提升了四肢瘫痪者的独立性。
3. 实验结果显示，BCI参与者的驾驶反应速度和精确度与正常运动者相当，且能够成功进行远程驾驶。

## 📝 摘要（中文）

脑机接口（BCI）直接读取大脑神经信号以推断运动规划和执行。然而，该技术的应用主要局限于实验室，实际应用较少。我们开发了一种双手BCI系统，能够在模拟和真实环境中驾驶车辆。研究表明，植入后部顶叶皮层和运动皮层手部区域的四肢瘫痪个体，其反应速度和精确度与正常运动者相当，能够熟练驾驶模拟车辆。此外，该BCI参与者还能够远程驾驶位于密歇根的福特Mustang Mach-E。该系统的创新之处在于实现了双手光标和点击控制，确保了在虚拟和真实环境中的安全驾驶。这一首创的植入式BCI应用展示了BCI的多样性和创新潜力，为恢复因神经损伤而失去独立性的人们提供了希望。

## 🔬 方法详解

**问题定义**：本研究旨在解决四肢瘫痪者在实际驾驶中的能力缺失，现有脑机接口技术多局限于实验室环境，缺乏实际应用场景。

**核心思路**：论文的核心思路是开发一种双手脑机接口系统，使四肢瘫痪者能够通过大脑信号控制车辆的速度和方向，从而实现独立驾驶。

**技术框架**：整体架构包括信号采集模块（植入式电极）、信号处理模块（解码神经信号）、控制模块（光标和点击控制）以及反馈模块（驾驶反馈）。

**关键创新**：最重要的技术创新在于实现了双手控制的光标和点击功能，使得四肢瘫痪者能够在复杂环境中安全驾驶，这在现有BCI研究中尚属首次。

**关键设计**：关键设计包括对植入电极的选择、信号解码算法的优化、以及驾驶控制策略的设计，确保系统在真实环境中的稳定性和安全性。

## 📊 实验亮点

实验结果表明，四肢瘫痪的BCI参与者在模拟驾驶中，其反应速度和精确度与正常运动者相当，成功完成远程驾驶任务，展示了BCI系统的安全性和可行性。这一创新的驾驶方式为未来的脑机接口应用开辟了新的方向。

## 🎯 应用场景

该研究的潜在应用领域包括为四肢瘫痪者提供独立驾驶的解决方案，能够显著提升他们的生活质量和自主性。此外，该技术也可扩展至其他需要脑机接口的领域，如医疗康复和智能交通系统。

## 📄 摘要（原文）

> Brain-computer interfaces (BCIs) read neural signals directly from the brain to infer motor planning and execution. However, the implementation of this technology has been largely limited to laboratory settings, with few real-world applications. We developed a bimanual BCI system to drive a vehicle in both simulated and real-world environments. We demonstrate that an individual with tetraplegia, implanted with intracortical BCI electrodes in the posterior parietal cortex (PPC) and the hand knob region of the motor cortex (MC), reacts at least as fast and precisely as motor intact participants, and drives a simulated vehicle as proficiently as the same control group. This BCI participant, living in California, could also remotely drive a Ford Mustang Mach-E vehicle in Michigan. Our first teledriving task relied on cursor control for speed and steering in a closed urban test facility. However, the final BCI system added click control for full-stop braking and thus enabled bimanual cursor-and-click control for both simulated driving through a virtual town with traffic and teledriving through an obstacle course without traffic in the real world. We also demonstrate the safety and feasibility of BCI-controlled driving. This first-of-its-kind implantable BCI application not only highlights the versatility and innovative potentials of BCIs but also illuminates the promising future for the development of life-changing solutions to restore independence to those who suffer catastrophic neurological injury.

