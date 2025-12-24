---
layout: default
title: Grid Edge Intelligence-Assisted Model Predictive Framework for Black Start of Distribution Systems with Inverter-Based Resources
---

# Grid Edge Intelligence-Assisted Model Predictive Framework for Black Start of Distribution Systems with Inverter-Based Resources

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12937" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12937v1</a>
  <a href="https://arxiv.org/pdf/2508.12937.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12937v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12937v1', 'Grid Edge Intelligence-Assisted Model Predictive Framework for Black Start of Distribution Systems with Inverter-Based Resources')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junyuan Zheng, Salish Maharjan, Zhaoyu Wang

**分类**: eess.SY

**发布日期**: 2025-08-18

**备注**: This manuscript has been submitted to IEEE Transaction on Smart Grid

---

## 💡 一句话要点

**提出基于网边智能的预测框架以解决配电系统黑启动问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `分布式能源` `黑启动` `网边智能` `频率约束` `配电系统` `灵活性调度` `恢复过程` `电力系统韧性`

## 📋 核心要点

1. 现有的黑启动策略未能充分考虑背负表DERs的灵活性，导致恢复过程中的频率安全问题。
2. 本文提出了一种基于网边智能的预测框架，利用BTM DERs的灵活性进行频率约束的黑启动策略。
3. 通过在修改的IEEE 123-bus测试系统中验证，结果显示该框架在不同GEI渗透场景下均表现出显著的性能提升。

## 📝 摘要（中文）

随着分布式能源资源（DERs）的快速增长，配电系统的韧性和可靠性显著增强。然而，在黑启动（BS）和恢复过程中，许多背负表（BTM）DERs常常被忽视。现有的BS策略通常未能考虑频率安全和同步约束。为了解决这些问题，本文提出了一种基于网边智能（GEI）的预测框架，利用BTM DERs的灵活性进行自下而上的黑启动。该框架开发了GEI的预测模型，以估计多周期的灵活性范围并跟踪公用事业的调度信号。引入了一种频率约束的BS策略，明确纳入频率最低点、频率变化率（RoCoF）和准稳态频率的约束。该框架还包括同步开关，以实现更快速和安全的负载恢复。通过修改的IEEE 123-bus测试系统验证了该框架的有效性，并通过比较不同GEI渗透场景的结果展示了GEI的影响。

## 🔬 方法详解

**问题定义**：本文旨在解决配电系统黑启动过程中对背负表DERs灵活性利用不足的问题。现有方法在频率安全和同步约束方面存在显著不足，影响了恢复效率。

**核心思路**：提出基于网边智能的预测框架，利用BTM DERs的灵活性来优化黑启动过程，特别是在频率约束下进行调度。

**技术框架**：该框架包括GEI的预测模型、频率约束的黑启动策略和同步开关模块。GEI模型用于估计灵活性范围并跟踪调度信号，黑启动策略则确保频率安全。

**关键创新**：最重要的创新在于引入了频率约束的黑启动策略，明确考虑频率最低点、RoCoF和准稳态频率的约束，与现有方法相比，显著提升了恢复的安全性和效率。

**关键设计**：框架中GEI设备仅需通信灵活性范围，公用事业发送调度信号而无需交换详细资产信息，简化了信息交互过程。

## 📊 实验亮点

实验结果表明，所提出的框架在不同GEI渗透场景下均实现了显著的性能提升。与传统方法相比，频率约束的黑启动策略有效降低了频率波动，提升了负载恢复的速度和安全性，验证了GEI的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括配电系统的黑启动和恢复过程，尤其是在分布式能源资源日益普及的背景下。通过提高黑启动的效率和安全性，能够增强电力系统的整体韧性，减少停电时间，提升用户体验，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The growing proliferation of distributed energy resources (DERs) is significantly enhancing the resilience and reliability of distribution systems. However, a substantial portion of behind-the-meter (BTM) DERs is often overlooked during black start (BS) and restoration processes. Existing BS strategies that utilize grid-forming (GFM) battery energy storage systems (BESS) frequently ignore critical frequency security and synchronization constraints. To address these limitations, this paper proposes a predictive framework for bottom-up BS that leverages the flexibility of BTM DERs through Grid Edge Intelligence (GEI). A predictive model is developed for GEI to estimate multi-period flexibility ranges and track dispatch signals from the utility. A frequency-constrained BS strategy is then introduced, explicitly incorporating constraints on frequency nadir, rate-of-change-of-frequency (RoCoF), and quasi-steady-state (QSS) frequency. The framework also includes synchronizing switches to enable faster and more secure load restoration. Notably, it requires GEI devices to communicate only their flexibility ranges and the utility to send dispatch signals without exchanging detailed asset information. The proposed framework is validated using a modified IEEE 123-bus test system, and the impact of GEI is demonstrated by comparing results across various GEI penetration scenarios.

