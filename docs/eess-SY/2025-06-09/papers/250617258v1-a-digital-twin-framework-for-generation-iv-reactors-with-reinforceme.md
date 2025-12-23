---
layout: default
title: A Digital Twin Framework for Generation-IV Reactors with Reinforcement Learning-Enabled Health-Aware Supervisory Control
---

# A Digital Twin Framework for Generation-IV Reactors with Reinforcement Learning-Enabled Health-Aware Supervisory Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17258" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17258v1</a>
  <a href="https://arxiv.org/pdf/2506.17258.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17258v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17258v1', 'A Digital Twin Framework for Generation-IV Reactors with Reinforcement Learning-Enabled Health-Aware Supervisory Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jasmin Y. Lim, Dimitrios Pylorof, Humberto E. Garcia, Karthik Duraisamy

**分类**: eess.SY, cs.AI

**发布日期**: 2025-06-09

**备注**: 39 pages, 22 figures

**DOI**: [10.1016/j.pnucene.2025.106105](https://doi.org/10.1016/j.pnucene.2025.106105)

---

## 💡 一句话要点

**提出数字双胞胎框架以优化第四代核反应堆的健康监控与控制**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `数字双胞胎` `第四代核反应堆` `强化学习` `健康监控` `贝叶斯推断` `闭环控制` `运营优化`

## 📋 核心要点

1. 现有的核反应堆运营方法在成本、决策效率和健康监控方面存在不足，限制了第四代反应堆的应用。
2. 本文提出的数字双胞胎框架结合强化学习和贝叶斯推断，优化了反应堆的运营和维护策略。
3. 通过长达一年的运营案例研究，展示了该框架在维护规划、短期精度提升和实时重校准方面的有效性。

## 📝 摘要（中文）

第四代（Gen-IV）核电站旨在取代现有反应堆，提高性能、安全性、可靠性和可持续性。然而，巨大的投资成本限制了这些先进反应堆概念的部署。数字双胞胎技术将现实系统与数字工具相结合，以降低成本、增强决策能力并提高运营效率。本文设计了一个数字双胞胎框架，用于操作氟盐冷却高温反应堆，利用数据增强方法优化运营和维护策略，同时遵循系统约束。该闭环框架整合了代理建模、强化学习和贝叶斯推断，以简化在线调节和自我调整的端到端通信。强化学习考虑了组件健康和退化，以驱动目标功率生成，并通过参考调节器控制算法确保泵流量和温度限制的合规性。通过三个案例研究验证了该框架的鲁棒性，展示了健康监控和约束信息驱动的核电站运营的广泛适用性。

## 🔬 方法详解

**问题定义**：本文旨在解决第四代核反应堆在运营中面临的高成本和健康监控不足的问题。现有方法缺乏有效的在线决策支持，导致运营效率低下。

**核心思路**：通过构建数字双胞胎框架，结合强化学习和贝叶斯推断，实时优化反应堆的运营和维护策略，确保在系统约束下的高效运行。

**技术框架**：该框架包括代理建模、强化学习模块和贝叶斯推断模块，形成闭环控制系统，实现在线调节和自我调整。数据通过贝叶斯滤波与测量数据相结合，提升决策的准确性。

**关键创新**：最重要的创新在于将强化学习与健康监控相结合，利用参考调节器控制算法确保系统在约束条件下的合规性，这在现有方法中尚未实现。

**关键设计**：在设计中，强化学习模型考虑了组件的健康状态和退化情况，损失函数设计为平衡目标功率生成与系统约束，网络结构采用深度学习方法以提高学习效率和准确性。

## 📊 实验亮点

实验结果表明，数字双胞胎框架在维护规划和短期精度提升方面表现出色，能够在高频测量下实现实时重校准，确保系统在变化边界条件下的稳定性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括第四代核反应堆的运营管理、维护规划以及其他复杂工程系统的健康监控。通过数字双胞胎技术，可以显著提高系统的决策效率和安全性，推动先进核能技术的实际应用。

## 📄 摘要（原文）

> Generation IV (Gen-IV) nuclear power plants are envisioned to replace the current reactor fleet, bringing improvements in performance, safety, reliability, and sustainability. However, large cost investments currently inhibit the deployment of these advanced reactor concepts. Digital twins bridge real-world systems with digital tools to reduce costs, enhance decision-making, and boost operational efficiency. In this work, a digital twin framework is designed to operate the Gen-IV Fluoride-salt-cooled High-temperature Reactor, utilizing data-enhanced methods to optimize operational and maintenance policies while adhering to system constraints. The closed-loop framework integrates surrogate modeling, reinforcement learning, and Bayesian inference to streamline end-to-end communication for online regulation and self-adjustment. Reinforcement learning is used to consider component health and degradation to drive the target power generations, with constraints enforced through a Reference Governor control algorithm that ensures compliance with pump flow rate and temperature limits. These input driving modules benefit from detailed online simulations that are assimilated to measurement data with Bayesian filtering. The digital twin is demonstrated in three case studies: a one-year long-term operational period showcasing maintenance planning capabilities, short-term accuracy refinement with high-frequency measurements, and system shock capturing that demonstrates real-time recalibration capabilities when change in boundary conditions. These demonstrations validate robustness for health-aware and constraint-informed nuclear plant operation, with general applicability to other advanced reactor concepts and complex engineering systems.

