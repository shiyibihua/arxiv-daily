---
layout: default
title: Energy Management and Wake-up for IoT Networks Powered by Energy Harvesting
---

# Energy Management and Wake-up for IoT Networks Powered by Energy Harvesting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13825" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13825v1</a>
  <a href="https://arxiv.org/pdf/2508.13825.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13825v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13825v1', 'Energy Management and Wake-up for IoT Networks Powered by Energy Harvesting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: David Ernesto Ruiz-Guirola, Samuel Montejo-Sanchez, Israel Leyva-Mayorga, Zhu Han, Petar Popovski, Onel L. A. Lopez

**分类**: eess.SY

**发布日期**: 2025-08-19

**备注**: This work has been partially supported by the Research Council of Finland (Grant 369116 (6G Flagship Programme), Grant 362782), the Finnish Foundation for Technology Promotion, the European Commission through the Horizon Europe/JU SNS project AMBIENT-6G (Grant 101192113), and in Chile, by ANID FONDECYT Regular No.1241977

---

## 💡 一句话要点

**提出基于KNN的能量管理方案以优化IoT网络的能量采集与唤醒**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `物联网` `能量管理` `能量采集` `K近邻` `强化学习` `决策变换器` `数据传输` `可持续性`

## 📋 核心要点

1. 现有IoT设备在能量管理上面临挑战，尤其是在依赖能量采集的情况下，如何延长电池寿命和提高数据传输效率。
2. 论文提出了一种基于KNN的工作周期管理方法，结合空间相关性优化能量效率，并引入RL和DT等机器学习方法以提升信息捕获能力。
3. 实验结果表明，KNN、RL和DT三种方法在能量节省方面均显著优于现有技术，尤其是RL方法在IoT设备数量增加时接近理想基准性能。

## 📝 摘要（中文）

随着物联网（IoT）的快速发展，面临着可持续性挑战，如维护需求增加和整体能耗上升。为此，本文探讨了依赖能量采集（EH）的自给自足IoT生态系统。研究重点在于有效管理IoT设备的工作周期，以延长电池寿命并最大化传输至基站的数据量。基站可在初步检测后唤醒特定IoT设备以获取更多信息。我们提出了一种基于K近邻（KNN）的工作周期管理方法，考虑了IoT设备活动与能量采集过程的空间相关性，从而优化能量效率和检测准确性。通过评估强化学习（RL）和决策变换器（DT）等机器学习方法，显著提高了能量节省效果。

## 🔬 方法详解

**问题定义**：本文旨在解决依赖能量采集的IoT设备在能量管理和数据传输中的效率问题。现有方法在延长电池寿命和提高数据传输量方面存在不足。

**核心思路**：通过基于KNN的工作周期管理方法，结合空间相关性，优化IoT设备的能量使用和数据传输效率。同时，利用机器学习方法（如RL和DT）进一步提升信息捕获能力。

**技术框架**：整体架构包括IoT设备的能量采集模块、数据传输模块和基站的唤醒机制。KNN用于管理设备的工作周期，RL和DT用于优化信息捕获。

**关键创新**：最重要的创新在于将KNN与空间相关性结合，优化了能量管理策略，显著提高了能量效率和检测准确性，区别于传统的单一能量管理方法。

**关键设计**：在参数设置上，KNN的邻居数量、RL的奖励机制和DT的决策策略均经过精细调整，以确保最佳性能。

## 📊 实验亮点

实验结果显示，KNN、RL和DT方法在能量节省方面均显著优于现有技术，尤其是RL方法在IoT设备数量增加时，其性能接近理想基准，表明该方法在实际应用中的有效性和潜力。

## 🎯 应用场景

该研究的潜在应用领域包括智能城市、环境监测和工业自动化等IoT场景。通过优化能量管理和数据传输效率，可以实现更长的设备使用寿命和更高的数据可靠性，推动可持续IoT生态系统的发展。

## 📄 摘要（原文）

> The rapid growth of the Internet of Things (IoT) presents sustainability challenges such as increased maintenance requirements and overall higher energy consumption. This motivates self-sustainable IoT ecosystems based on Energy Harvesting (EH). This paper treats IoT deployments in which IoT devices (IoTDs) rely solely on EH to sense and transmit information about events/alarms to a base station (BS). The objective is to effectively manage the duty cycling of the IoTDs to prolong battery life and maximize the relevant data sent to the BS. The BS can also wake up specific IoTDs if extra information about an event is needed upon initial detection. We propose a K-nearest neighbors (KNN)-based duty cycling management to optimize energy efficiency and detection accuracy by considering spatial correlations among IoTDs' activity and their EH process. We evaluate machine learning approaches, including reinforcement learning (RL) and decision transformers (DT), to maximize information captured from events while managing energy consumption. Significant improvements over the state-ofthe-art approaches are obtained in terms of energy saving by all three proposals, KNN, RL, and DT. Moreover, the RL-based solution approaches the performance of a genie-aided benchmark as the number of IoTDs increases.

