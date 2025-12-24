---
layout: default
title: Imperfect Competition in Markets for Short-Circuit Current Services
---

# Imperfect Competition in Markets for Short-Circuit Current Services

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09425" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09425v2</a>
  <a href="https://arxiv.org/pdf/2508.09425.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09425v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09425v2', 'Imperfect Competition in Markets for Short-Circuit Current Services')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peng Wang, Luis Badesa

**分类**: eess.SY

**发布日期**: 2025-08-13 (更新: 2025-11-01)

**备注**: Ancillary services, short-circuit current, market power, bilevel optimization, primal-dual formulation. A paper submitted to <Sustainable Energy, Grids and Networks>

---

## 💡 一句话要点

**提出SCC约束双层模型以解决短路电流服务市场竞争问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `短路电流` `逆变器基础资源` `市场力量` `电力系统` `经济机制` `双层模型` `同步发电机`

## 📋 核心要点

1. 核心问题：逆变器基础资源在短路电流贡献方面的不足，导致电力系统安全性降低。
2. 方法要点：采用SCC约束双层模型，研究同步发电机的战略行为及市场力量问题。
3. 实验或效果：分析结果表明，市场力量代理商的收益可达三倍，凸显市场设计的重要性。

## 📝 摘要（中文）

本论文探讨了逆变器基础资源（IBR）在短路电流（SCC）贡献方面的不足，尤其是在同步发电机（SG）占主导地位的电力系统中。随着IBR渗透率的增加，SCC的减少对系统安全运行构成挑战，可能导致线路保护未能及时跳闸。为了解决这一问题，论文提出通过经济机制采购SCC辅助服务。然而，现有市场对SCC服务的适用性尚不明确，可能存在市场力量问题。为此，本文采用SCC约束双层模型研究SG的战略行为，并通过原始-对偶形式重构模型，分析不同位置SG的市场行为，结果显示，具有市场力量的代理商可能从SCC提供中获得高达三倍的收益，强调了市场设计的必要性。

## 🔬 方法详解

**问题定义**：本论文旨在解决逆变器基础资源（IBR）在短路电流（SCC）贡献不足的问题，尤其是在同步发电机（SG）占主导的电力系统中。现有方法未能有效应对市场力量问题，导致SCC服务市场的适用性不明确。

**核心思路**：论文提出通过SCC约束双层模型来研究SG的战略行为，重点分析电网拓扑对SCC贡献的影响。通过这种方式，能够识别在有利电气位置的SG是否会施加市场力量，并探讨相应的缓解措施。

**技术框架**：整体架构包括SCC约束双层模型的构建、原始-对偶形式的重构以及基于修改后的IEEE 30节点系统的案例分析。主要模块包括市场行为分析、收益计算和策略评估。

**关键创新**：最重要的技术创新在于采用双层模型来分析市场力量问题，这一方法能够揭示SG在不同电气位置的市场行为与收益之间的关系，区别于传统的单层模型分析。

**关键设计**：模型中关键参数包括电网拓扑、SG的短路电流贡献等，损失函数设计为考虑市场力量的收益最大化，网络结构则基于电力系统的实际运行情况进行调整。通过这些设计，能够更准确地模拟市场行为。

## 📊 实验亮点

实验结果显示，具有市场力量的代理商在SCC提供中可实现收益高达三倍，表明市场设计的必要性。通过对不同位置SG的分析，揭示了电网拓扑对市场行为的影响，为未来市场机制的优化提供了重要依据。

## 🎯 应用场景

该研究的潜在应用领域包括电力市场设计、短路电流服务的经济机制以及电力系统的安全运行。通过优化SCC服务市场，可以提高电力系统的可靠性和经济性，确保在IBR渗透率增加的情况下，系统依然能够安全稳定运行。

## 📄 摘要（原文）

> An important limitation of Inverter-Based Resources (IBR) is their reduced contribution to Short-Circuit Current (SCC), as compared to that of Synchronous Generators (SGs). With increasing penetration of IBR in most power systems, the reducing SCC poses challenges to a secure system operation, as line protections may not trip when required. In order to address this issue, the SCC ancillary service could be procured via an economic mechanism, aiming at securing adequate SCC on all buses. However, the suitability of markets for SCC services is not well understood, given that these could be prone to market-power issues: since the SCC contributions from various SGs to a certain bus are determined by the electrical topology of the grid, this is a highly local service. It is necessary to understand if SGs at advantageous electrical locations could exert market power and, if so, how it could be mitigated. In order to fill this gap, this paper adopts an SCC-constrained bilevel model to investigate strategic behaviors of SGs. To address the non-convexity due to unit commitment variables, the model is restructured through a primal-dual formulation. Based on a modified IEEE 30-bus system, cases with strategic SGs placed at different buses are analyzed. These studies demonstrate that agents exerting market power could achieve up to triple revenues from SCC provision, highlighting the need to carefully design these markets.

