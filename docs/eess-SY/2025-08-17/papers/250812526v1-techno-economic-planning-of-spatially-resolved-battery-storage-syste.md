---
layout: default
title: Techno-Economic Planning of Spatially-Resolved Battery Storage Systems in Renewable-Dominant Grids Under Weather Variability
---

# Techno-Economic Planning of Spatially-Resolved Battery Storage Systems in Renewable-Dominant Grids Under Weather Variability

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12526" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12526v1</a>
  <a href="https://arxiv.org/pdf/2508.12526.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12526v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12526v1', 'Techno-Economic Planning of Spatially-Resolved Battery Storage Systems in Renewable-Dominant Grids Under Weather Variability')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seyed Ehsan Ahmadi, Elnaz Kabir, Mohammad Fattahi, Mousa Marzband, Dongjun Li

**分类**: eess.SY

**发布日期**: 2025-08-17

---

## 💡 一句话要点

**提出电池储能系统规划以应对可再生能源波动问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `电池储能系统` `可再生能源` `随机规划` `电力系统` `负荷削减` `经济性分析` `技术优化`

## 📋 核心要点

1. 可再生能源的间歇性和波动性导致电力系统面临负荷削减和系统拥堵等重大挑战，现有方法未能有效解决这些问题。
2. 本研究提出了一种基于两阶段随机规划的方法，优化电池储能系统的选址、规模和类型，以平衡电力供需并降低可再生能源的削减。
3. 研究结果显示，电池储能系统能够显著减少可再生能源的削减和负荷削减，提升电力系统的韧性，助力实现2030年能源目标。

## 📝 摘要（中文）

随着能源转型的推进，可再生能源在电力系统中的占比显著增加，但其间歇性和波动性带来了负荷削减和系统拥堵等挑战。本研究探讨了电池储能系统（BSS）在平衡电力供需中的作用，采用两阶段随机规划优化电池的选址、规模和类型。以纽约州电力系统为案例，结合1980-2019年的负荷和天气数据，考虑了负荷和可再生能源发电的不确定性。研究结果表明，BSS可减少可再生能源的削减34%和负荷削减21%，为实现纽约州2030年能源目标提供了更具韧性的电力系统。此外，BSS的成本与可再生能源渗透率之间的关系并非线性，揭示了成本与容量之间的复杂关系。

## 🔬 方法详解

**问题定义**：本研究旨在解决可再生能源在电力系统中引发的负荷削减和系统拥堵问题。现有方法未能充分考虑电池技术的综合技术和经济特性，导致优化效果不佳。

**核心思路**：论文提出通过两阶段随机规划优化电池储能系统的选址、规模和类型，第一阶段确定电池的总体配置，第二阶段则进行基于小时的操作决策，以应对负荷和可再生能源发电的不确定性。

**技术框架**：整体架构包括数据收集、模型建立和优化求解三个主要模块。首先收集1980-2019年的负荷和天气数据，然后建立包含技术和经济特性的优化模型，最后通过随机规划方法进行求解。

**关键创新**：本研究的创新点在于综合考虑电池技术的全面特性，采用样本平均近似方法处理负荷和可再生能源发电的不确定性，显著提高了优化结果的可靠性。

**关键设计**：在模型设计中，关键参数包括电池的容量、类型和选址，损失函数则考虑了负荷削减和可再生能源削减的成本，确保优化方案的经济性和可行性。

## 📊 实验亮点

实验结果表明，电池储能系统能够将可再生能源削减减少34%，负荷削减降低21%。此外，BSS的成本与容量之间的关系并非线性，揭示了在可再生能源渗透率增加时，成本控制的复杂性。

## 🎯 应用场景

该研究的成果可广泛应用于电力系统的规划与管理，尤其是在可再生能源占比逐渐增加的地区。通过优化电池储能系统的配置，能够有效提升电力系统的稳定性和经济性，为实现可持续能源目标提供支持。

## 📄 摘要（原文）

> The ongoing energy transition is significantly increasing the share of renewable energy sources (RES) in power systems; however, their intermittency and variability pose substantial challenges, including load shedding and system congestion. This study examines the role of the battery storage system (BSS) in mitigating these challenges by balancing power supply and demand. We optimize the location, size, and type of batteries using a two-stage stochastic program, with the second stage involving hourly operational decisions over an entire year. Unlike previous research, we incorporate the comprehensive technical and economic characteristics of battery technologies. The New York State (NYS) power system, currently undergoing a significant shift towards increased RES generation, serves as our case study. Using available load and weather data from 1980-2019, we account for the uncertainty of both load and RES generation through a sample average approximation approach. Our findings indicate that BSS can reduce renewable curtailment by 34% and load shedding by 21%, contributing to a more resilient power system in achieving NYS 2030 energy targets. Furthermore, the cost of employing BSS for the reduction of load shedding and RES curtailment does not increase linearly with additional capacity, revealing a complex relationship between costs and renewable penetration. This study provides valuable insights for the strategic BSS deployment to achieve a cost-effective and reliable power system in the energy transition as well as the feasibility of the NYS 2030 energy targets.

