---
layout: default
title: Real-Time Power electronics Control and Monitoring with TI F28379D DSC and GUI Composer
---

# Real-Time Power electronics Control and Monitoring with TI F28379D DSC and GUI Composer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25008" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25008v1</a>
  <a href="https://arxiv.org/pdf/2509.25008.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25008v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25008v1', 'Real-Time Power electronics Control and Monitoring with TI F28379D DSC and GUI Composer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ilyas Bennia, Lotfi Baghli, Ehsan Jamshidpour, Abdelkader Mechernene, Jean-Philippe Martin, Driss Yousfi

**分类**: eess.SY

**发布日期**: 2025-09-29

**备注**: 10 pages

---

## 💡 一句话要点

**基于TI F28379D DSC和GUI Composer的实时电力电子控制与监测系统**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `电力电子` `电机控制` `实时控制` `TMS320F28379D` `GUI Composer` `磁场定向控制` `V/f控制` `感应电机`

## 📋 核心要点

1. 传统感应电机控制系统在实时性、精度和调试效率方面存在挑战，限制了其在高性能应用中的潜力。
2. 论文提出了一种基于TI F28379D DSC的实时控制系统，结合GUI Composer实现参数调整和数据可视化，提升控制性能和调试效率。
3. 实验结果表明，该系统在速度反转、动态响应和稳定性方面表现出色，验证了V/f和FOC控制策略的有效性。

## 📝 摘要（中文）

本文详细介绍了使用德州仪器TMS320F28379D微控制器实现三相感应电机实时控制系统的过程，并进行了实验验证。该系统集成了脉冲宽度调制（PWM）生成、模数转换（ADC）、数模转换（DAC）和正交编码器反馈，以实现各种控制策略下的精确控制。基于AMC1301隔离放大器和分流电阻的电流传感解决方案确保了反馈回路中电流测量的准确性和安全性。实现了V/f控制和磁场定向控制（FOC）两种控制算法并进行了测试。使用GUI Composer实现了实时参数调整和数据可视化，从而实现了高效的系统调试和交互。实验结果表明，在阶跃和多步输入下，系统具有平稳的速度反转、快速的动态响应和稳定的性能。尽管GUI Composer有效地支持通用监控和控制，但与专业级平台相比，信号带宽存在局限性。结果证实了所实现的控制策略对于高性能感应电机应用的鲁棒性和有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决三相感应电机实时控制问题，现有方法在实时性、控制精度和系统调试方面存在不足。传统控制系统可能难以满足高性能应用的需求，且调试过程复杂，效率较低。

**核心思路**：论文的核心思路是利用TI TMS320F28379D微控制器的强大计算能力和丰富的外设接口，结合GUI Composer的可视化调试功能，构建一个实时、精确且易于调试的电机控制系统。通过硬件加速和软件优化，实现控制算法的快速执行，并通过GUI Composer实现参数的实时调整和数据的可视化监控。

**技术框架**：该系统的整体架构包括以下几个主要模块：1) 电机驱动电路，负责驱动三相感应电机；2) 基于TI F28379D DSC的控制核心，实现控制算法和外设控制；3) 电流传感模块，采用AMC1301隔离放大器和分流电阻实现电流测量；4) 编码器反馈模块，用于获取电机转速信息；5) GUI Composer界面，用于参数调整和数据可视化。控制流程包括：电流采样 -> 控制器计算 -> PWM生成 -> 电机驱动 -> 编码器反馈，形成闭环控制。

**关键创新**：该论文的关键创新在于将TI F28379D DSC和GUI Composer结合，构建了一个完整的实时电机控制和监测系统。与传统方法相比，该系统具有更高的实时性、控制精度和调试效率。此外，采用AMC1301隔离放大器和分流电阻的电流传感方案，提高了电流测量的安全性和准确性。

**关键设计**：在控制算法方面，实现了V/f控制和磁场定向控制（FOC）两种策略。V/f控制简单易实现，适用于对控制精度要求不高的场合；FOC控制能够实现更高的控制精度和动态性能。在硬件设计方面，需要仔细选择分流电阻的阻值，以保证电流测量的精度和范围。GUI Composer界面的设计需要考虑用户体验，提供清晰的数据显示和便捷的参数调整功能。

## 📊 实验亮点

实验结果表明，该系统能够实现平稳的速度反转和快速的动态响应。在阶跃输入和多步输入下，系统均表现出良好的稳定性和控制性能。GUI Composer能够有效地支持实时参数调整和数据可视化，方便系统调试。虽然GUI Composer在信号带宽方面存在一定局限性，但对于一般的电机控制应用来说，已经足够满足需求。

## 🎯 应用场景

该研究成果可应用于工业自动化、机器人、电动汽车等领域。高性能电机控制系统是这些应用的关键组成部分。该系统能够提高电机控制的精度、效率和可靠性，从而提升整体系统的性能。此外，GUI Composer的可视化调试功能可以大大缩短开发周期，降低开发成本，具有重要的实际应用价值。

## 📄 摘要（原文）

> This paper details the implementation and experimental validation of a real-time control system for a three-phase induction motor using the Texas Instruments TMS320F28379D microcontroller. The system integrates pulse-width modulation (PWM) generation, analog-to-digital conversion (ADC), digital-to-analog conversion (DAC), and quadrature encoder feedback to facilitate precise control under various strategies. A current sensing solution based on the AMC1301 isolation amplifier and shunt resistor ensures accurate and safe current measurement for feedback loops. Two control algorithms, V/f and Field-Oriented Control (FOC) are implemented and tested. Real-time parameter tuning and data visualization are achieved using GUI Composer, enabling efficient system debugging and interaction. Experimental results demonstrate smooth speed reversal, fast dynamic response, and stable performance under both step and multi-step inputs. While GUI Composer effectively supports general monitoring and control, limitations in signal bandwidth are noted compared to professional-grade platforms. The results confirm the robustness and effectiveness of the implemented control strategies for high-performance induction motor applications.

