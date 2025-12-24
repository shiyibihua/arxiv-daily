---
layout: default
title: System Synchronization Based on Complex Frequency
---

# System Synchronization Based on Complex Frequency

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11381" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11381v2</a>
  <a href="https://arxiv.org/pdf/2508.11381.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11381v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11381v2', 'System Synchronization Based on Complex Frequency')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yusen Wei, Lan Tang, Peidong Li

**分类**: eess.SY

**发布日期**: 2025-08-15 (更新: 2025-11-21)

**备注**: 13 pages,11 figures

---

## 💡 一句话要点

**基于复频率的系统同步方法解决低惯量电力系统问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `复频率` `低惯量电力系统` `同步稳定性` `动态标准` `电压支持` `频率惯量` `IEEE 9节点系统`

## 📋 核心要点

1. 现有的同步标准主要基于频率一致性，无法有效应对低惯量电力系统中的频率和电压耦合动态问题。
2. 本文提出了复频率的概念，构建了一个综合的分析框架，以评估低惯量电力系统的同步稳定性。
3. 通过对修改后的IEEE 9节点系统进行仿真，验证了所提方法的有效性，能够清晰揭示系统的同步关系。

## 📝 摘要（中文）

随着可再生能源的不断渗透，系统惯量持续降低，传统基于频率一致性的同步标准无法准确捕捉频率和电压在瞬态过程中的耦合动态。为此，本文采用复频率的概念，开发了一个分析框架，整合理论、指标和仿真，以评估低惯量电力系统中的同步稳定性。首先介绍了复频率及复频率同步的基本概念和数学表述。然后建立了局部和全局复同步的动态标准，并提出了复惯量指标，统一了传统频率惯量和电压惯量的支持作用，能够定量评估区域内协调频率-电压支持和扰动拒绝的强度。最后，通过对修改后的IEEE 9节点系统进行瞬态仿真验证了该方法。结果表明，该方法能够清晰揭示子网络与整体系统之间的同步关系，为低惯量电力系统的稳定性分析和控制策略设计提供了有益的理论参考。

## 🔬 方法详解

**问题定义**：本文旨在解决低惯量电力系统中频率和电压耦合动态的同步问题，现有方法无法准确捕捉这些动态特性。

**核心思路**：通过引入复频率的概念，建立一个新的分析框架，整合理论、指标和仿真，提供更全面的同步稳定性评估。

**技术框架**：整体架构包括复频率的基本概念介绍、动态同步标准的建立、复惯量指标的提出以及仿真验证四个主要模块。

**关键创新**：提出的复惯量指标统一了频率惯量和电压惯量的支持作用，能够定量评估频率-电压协调支持的强度，这是与现有方法的本质区别。

**关键设计**：在指标设计中，考虑了频率和电压的耦合效应，采用了适当的数学模型和仿真工具，以确保结果的准确性和可靠性。

## 📊 实验亮点

实验结果表明，所提方法能够有效揭示子网络与整体系统之间的同步关系，提供了比传统方法更清晰的动态分析，验证了在低惯量条件下的有效性，具有显著的理论和实践意义。

## 🎯 应用场景

该研究可广泛应用于低惯量电力系统的稳定性分析与控制策略设计，尤其是在可再生能源比例逐渐增加的背景下，具有重要的实际价值和未来影响。通过提供新的分析工具，能够帮助电力系统运营商更好地应对瞬态扰动，提高系统的稳定性和可靠性。

## 📄 摘要（原文）

> The increasing penetration of renewable energy leads to a continuous reduction in system inertia, for which conventional synchronization criteria based solely on frequency consistency can no longer accurately capture the coupled dynamics of frequency and voltage during transients. To address this issue, this paper employs the concept of complex frequency and develops an analysis framework that integrates theory, indices, and simulation for assessing synchronization stability in low-inertia power systems. First, the basic concepts and mathematical formulation of complex frequency and complex-frequency synchronization are introduced. Then, dynamic criteria for local and global complex synchronization are established, upon which a complex inertia index is proposed. This index unifies the supporting role of traditional frequency inertia and the voltage support capability associated with voltage inertia, enabling quantitative evaluation of the strength of coordinated frequency-voltage support and disturbance rejection within a region. Finally, transient simulations on a modified IEEE 9-bus system are carried out to validate the proposed method. The results show that the method can clearly reveal the synchronization relationships between subnetworks and the overall system, providing a useful theoretical reference for stability analysis and control strategy design in low-inertia power systems.

