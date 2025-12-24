---
layout: default
title: High-Power Wide-Bandwidth High-Quality Modular Pulse Synthesizer with Adaptive Voltage Asymmetry in Medical Power Electronics
---

# High-Power Wide-Bandwidth High-Quality Modular Pulse Synthesizer with Adaptive Voltage Asymmetry in Medical Power Electronics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00291" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00291v1</a>
  <a href="https://arxiv.org/pdf/2509.00291.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00291v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00291v1', 'High-Power Wide-Bandwidth High-Quality Modular Pulse Synthesizer with Adaptive Voltage Asymmetry in Medical Power Electronics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinshui Zhang, Stefan M. Goetz

**分类**: eess.SY

**发布日期**: 2025-08-30

---

## 💡 一句话要点

**提出高功率宽带高质量模块化脉冲合成器以解决脑刺激信号合成问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `非侵入性脑刺激` `电源电子` `脉冲合成` `模块化设计` `高功率` `宽带` `电压不对称` `神经科学`

## 📋 核心要点

1. 现有的电源电子设备在非侵入性脑刺激中面临功率和带宽的限制，难以实现高质量的脉冲合成。
2. 论文提出通过高功率宽带电压不对称和模块间不同电压分配，减少模块数量同时提高脉冲成形分辨率。
3. 实验结果表明，三模块原型在电压失真方面相比于现有技术有显著减少，验证了设计的有效性。

## 📝 摘要（中文）

非侵入性脑刺激能够将信号写入神经元，但需要具备极高功率（兆伏安级）和千赫兹可用带宽的电源电子设备。传统的振荡器电路仅提供少量脉冲形状，而模块化级联电源电子首次解决了这一长期问题，实现了刺激时间形状的任意软件合成。本文提出了一种通过高功率宽带电压不对称实现高分辨率脉冲成形的替代方案，显著减少所需模块数量。我们设计的系统通过不同电压分配给各模块，近似指数提高了分辨率，并引入了开关电容充电机制，使模块能够通过单一直流电源充电至不同电压。实验验证显示，三模块原型相比于现有技术减少了13.4%的电压失真。

## 🔬 方法详解

**问题定义**：本文旨在解决非侵入性脑刺激中对高功率和高带宽电源电子设备的需求，现有方法在脉冲形状合成上存在模块数量多、输出质量差等痛点。

**核心思路**：通过实现高功率宽带电压不对称，论文提出了一种新的脉冲合成方法，能够在较少模块的情况下实现高分辨率的脉冲成形。

**技术框架**：整体架构包括多个模块，每个模块通过不同电压进行配置，采用开关电容充电机制，使得各模块能够从单一直流电源充电至不同电压。

**关键创新**：本文首次提出不对称多级电路作为高精度高功率合成器，并且首次在模块化电源电子中自适应优化不对称电压序列，显著提高了输出质量。

**关键设计**：设计中采用了不同电压分配策略而非简单的二进制模式，确保了输出的高分辨率和低失真，同时通过实验验证了设计的有效性。

## 📊 实验亮点

实验结果显示，三模块原型相比于现有三模块技术减少了13.4%的电压失真，相比于六模块技术减少了4.5%的失真，验证了该设计在提高输出质量方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括神经科学、医疗设备和脑机接口等，能够推动非侵入性脑刺激技术的发展，提高治疗效果和精确度。未来，该技术可能会在精神疾病治疗和神经调控等方面发挥重要作用。

## 📄 摘要（原文）

> Noninvasive brain stimulation can write signals into neurons but requires power electronics with exceptionally high power in the mega-volt-ampere range and kilohertz usable bandwidth. Whereas oscillator circuits offered only one or very few pulse shapes, modular cascaded power electronics solved a long-standing problem for the first time and enabled arbitrary software-based synthesis of the temporal shape of stimuli. However, synthesizing arbitrary stimuli with a high output quality requires a large number of modules. We propose an alternative solution that achieves high-resolution pulse shaping with fewer modules by implementing high-power wide-bandwidth voltage asymmetry. Rather than equal voltage steps, our system strategically assigns different voltages to each module to achieve a near-exponential improvement in resolution. The module voltage sequence does also not use just a simple binary pattern other work might suggest but adapts it to the output. Additionally, we introduce a switched-capacitor charging mechanism that allows the modules to charge to different voltages through a single dc power supply. We validated our design in a head-to-head comparison with the state of the art on experimental prototypes. Our three-module prototype reduces total voltage distortion by 13.4% compared to prior art with three modules, and by 4.5% compared to prior art with six -- twice as many -- modules. This paper is the first asymmetric multilevel circuit as a high-precision high-power synthesizer, as well as the first to adaptively optimize asymmetric voltage sequence in modular power electronics.

