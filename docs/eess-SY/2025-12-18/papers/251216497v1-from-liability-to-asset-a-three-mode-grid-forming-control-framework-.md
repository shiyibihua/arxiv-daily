---
layout: default
title: From Liability to Asset: A Three-Mode Grid-Forming Control Framework for Centralized Data Center UPS Systems
---

# From Liability to Asset: A Three-Mode Grid-Forming Control Framework for Centralized Data Center UPS Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16497" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16497v1</a>
  <a href="https://arxiv.org/pdf/2512.16497.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16497v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16497v1', 'From Liability to Asset: A Three-Mode Grid-Forming Control Framework for Centralized Data Center UPS Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohamed Shamseldein

**分类**: eess.SY

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**针对数据中心UPS系统，提出三模式并网控制框架，提升弱电网适应性。**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `数据中心` `不间断电源` `并网控制` `弱电网` `电压暂降` `频率响应` `储能系统`

## 📋 核心要点

1. 数据中心UPS系统面临弱电网连接下的故障和负载波动挑战，传统方法难以保证供电质量和电网稳定性。
2. 提出一种三模式并网控制框架，通过调节直流母线、故障模式P-Q优先级控制和快速频率响应，实现稳定供电和电网支撑。
3. 仿真结果表明，该方法在故障期间显著降低了未服务IT能量，改善了PCC电压，并有效抑制了负载波动对电网的影响。

## 📝 摘要（中文）

人工智能负载正将大型数据中心转变为高度动态的电力电子负载；故障期间的行为和负载脉冲可能会给互联的弱电网带来压力。本文提出了一种集中式中压（MV）不间断电源（UPS）控制架构，该架构实现为三种运行模式：模式1调节直流母线并塑造正常运行时的电网吸取；模式2通过UPS电池储能系统（UPS-BESS）缓冲和速率限制的故障后“软返回”来执行限流故障模式下的P-Q优先级；模式3可选地通过电网吸取调制提供基于下垂的快速频率响应。基频平均dq仿真（50 MW模块，短路比（SCR）= 1.5，0.5 p.u.三相骤降150毫秒）显示零未服务信息技术（IT）能量（0.00000 MWh vs. 0.00208 MWh用于瞬时中断基准），0.57 p.u.峰值逆变器电流（vs. 1.02 p.u.用于同步参考系锁相环（SRF-PLL）低电压穿越（LVRT）基线），0.20 p.u.的非零平均故障窗口电网吸取（vs.瞬时中断的近似0），以及在1个周期后改善的稳定公共连接点（PCC）电压最小值0.79 p.u.（vs. 0.66 p.u.）。强制振荡案例研究应用1 Hz脉冲负载（+/- 0.25 p.u.），并表明正常运行整形滤波器过滤了电网看到的振荡，而UPS-BESS缓冲了脉冲分量。

## 🔬 方法详解

**问题定义**：论文旨在解决大型数据中心UPS系统在连接到弱电网时面临的供电稳定性和电网交互问题。传统UPS系统在应对电网故障（如电压骤降）和负载波动时，可能导致IT设备断电，并对电网造成冲击。现有方法，如基于SRF-PLL的LVRT控制，在故障期间可能导致过大的逆变器电流和较低的PCC电压。

**核心思路**：论文的核心思路是将UPS系统视为一个可控的电网支撑单元，通过分模式控制，在正常运行、故障和频率响应三种状态下优化其行为。正常运行时，塑造电网吸取，减少谐波和波动；故障时，优先保证有功和无功功率输出，并限制电流；频率异常时，提供快速频率响应，稳定电网。

**技术框架**：该框架包含三个主要模式：
1. **模式1（正常运行）**：调节直流母线电压，并对电网吸取的电流进行整形，优化电能质量。
2. **模式2（故障模式）**：在电网故障期间，执行限流的P-Q优先级控制，利用UPS-BESS缓冲，并实现速率限制的故障后“软返回”，避免对电网造成冲击。
3. **模式3（频率响应）**：可选地提供基于下垂控制的快速频率响应，通过调制电网吸取来稳定电网频率。

**关键创新**：该方法的主要创新在于其集中式三模式控制架构，能够根据电网状态动态调整UPS系统的行为，从而在保证数据中心供电可靠性的同时，为电网提供支撑。与传统的瞬时中断或简单的LVRT策略相比，该方法能够更好地平衡供电可靠性和电网稳定性。

**关键设计**：论文采用基频平均dq仿真进行验证。关键设计包括：短路比（SCR）设置为1.5的弱电网环境；0.5 p.u.的三相电压骤降，持续150ms；P-Q优先级控制的参数设置，以及速率限制的“软返回”策略。此外，还设计了1Hz的脉冲负载，以评估系统对负载波动的抑制能力。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16497v1/simulation_results_pulse_ramp.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16497v1/simulation_results_pulse.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16497v1/simulation_results_stage1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

仿真结果表明，与瞬时中断基准相比，该方法实现了零未服务IT能量（0.00000 MWh vs. 0.00208 MWh）。在故障期间，峰值逆变器电流降低至0.57 p.u.（相比于SRF-PLL LVRT基线的1.02 p.u.），PCC电压最小值提升至0.79 p.u.（相比于基线的0.66 p.u.）。此外，正常运行模式下的整形滤波器有效抑制了1Hz脉冲负载对电网的影响。

## 🎯 应用场景

该研究成果可应用于大型数据中心的中压UPS系统，尤其是在连接到弱电网或可再生能源比例较高的电网时。通过提高数据中心供电的可靠性和电网的稳定性，可以降低数据中心运营风险，并促进可再生能源的消纳。该技术还可推广到其他需要高可靠性供电的场景，如关键基础设施和工业园区。

## 📄 摘要（原文）

> AI workloads are turning large data centers into highly dynamic power-electronic loads; fault-time behavior and workload pulsing can stress weak-grid points of interconnection. This paper proposes a centralized medium-voltage (MV) uninterruptible power supply (UPS) control architecture implemented as three operating modes: Mode 1 regulates a DC stiff bus and shapes normal-operation grid draw, Mode 2 enforces current-limited fault-mode P--Q priority with UPS battery energy storage system (UPS-BESS) buffering and a rate-limited post-fault "soft return," and Mode 3 optionally provides droop-based fast frequency response via grid-draw modulation. Fundamental-frequency averaged dq simulations (50 MW block, short-circuit ratio (SCR) = 1.5, 0.5 p.u. three-phase dip for 150~ms) show zero unserved information-technology (IT) energy (0.00000 MWh vs.0.00208 MWh for a momentary-cessation benchmark), a 0.57 p.u. peak inverter current (vs. 1.02 p.u. for a synchronous-reference-frame phase-locked loop (SRF-PLL) low-voltage ride-through (LVRT) baseline), a nonzero mean fault-window grid draw of 0.20~p.u. (vs.approx 0 for momentary cessation), and an improved settled point-of-common-coupling (PCC) voltage minimum of 0.79 p.u. after one cycle (vs. 0.66 p.u.). A forced-oscillation case study applies a 1 Hz pulsed load (+/- 0.25 p.u.) and shows that the normal-operation shaping filters the oscillation seen by the grid while the UPS-BESS buffers the pulsing component.

