---
layout: default
title: Enhancing Fault-Tolerant Space Computing: Guidance Navigation and Control (GNC) and Landing Vision System (LVS) Implementations on Next-Gen Multi-Core Processors
---

# Enhancing Fault-Tolerant Space Computing: Guidance Navigation and Control (GNC) and Landing Vision System (LVS) Implementations on Next-Gen Multi-Core Processors

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.04052" target="_blank" class="toolbar-btn">arXiv: 2511.04052v1</a>
    <a href="https://arxiv.org/pdf/2511.04052.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.04052v1" 
            onclick="toggleFavorite(this, '2511.04052v1', 'Enhancing Fault-Tolerant Space Computing: Guidance Navigation and Control (GNC) and Landing Vision System (LVS) Implementations on Next-Gen Multi-Core Processors')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Kyongsik Yun, David Bayard, Gerik Kubiak, Austin Owens, Andrew Johnson, Ryan Johnson, Dan Scharf, Thomas Lu

**分类**: cs.RO

**发布日期**: 2025-11-06

---

## 💡 一句话要点

**针对深空探测，论文提出基于多核处理器的容错GNC/LVS系统，加速并保障计算可靠性。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `深空探测` `容错计算` `多核处理器` `GNC` `LVS` `ARBITER` `故障注入` `自主导航`

## 📋 核心要点

1. 深空探测任务对自主GNC/LVS系统提出更高要求，传统航天硬件算力不足，难以满足实时性和复杂算法的需求。
2. 论文提出在多核处理器上部署GNC/LVS算法，并设计ARBITER容错机制，通过多核冗余和投票实现实时故障检测和纠正。
3. 实验表明，LVS图像处理速度提升高达15倍，GFOLD轨迹优化速度提升超过250倍，验证了ARBITER在静态和动态控制中的有效性。

## 📝 摘要（中文）

未来的行星探测任务需要在进入、下降和着陆（EDL）期间实现自主制导、导航和控制（GNC）以及着陆视觉系统（LVS）操作，这需要高性能、容错计算。本文评估了GNC和LVS算法在新一代多核处理器（HPSC、Snapdragon VOXL2和AMD Xilinx Versal）上的部署，LVS图像处理速度提升高达15倍，燃料最优大偏差（GFOLD）轨迹优化速度提升超过250倍（相比传统航天硬件）。为了确保计算可靠性，我们提出了一种多核投票（MV）机制ARBITER（用于可信执行和恢复的异步冗余行为检查），该机制可在冗余内核之间执行实时故障检测和纠正。ARBITER在静态优化任务（GFOLD）和动态闭环控制（姿态控制系统）中都得到了验证。故障注入研究进一步确定了GFOLD中的梯度计算阶段对位级错误最敏感，从而推动了选择性保护策略和基于向量的输出仲裁。这项工作为未来的任务（包括火星样本返回、土卫二Orbilander和谷神星样本返回）建立了一个可扩展且节能的架构，在这些任务中，车载自主性、低延迟和容错能力至关重要。

## 🔬 方法详解

**问题定义**：论文旨在解决深空探测任务中，传统航天计算硬件无法满足自主GNC/LVS系统对高性能和高可靠性计算的需求的问题。现有航天硬件算力有限，难以支持复杂的GNC/LVS算法，且缺乏有效的容错机制，容易受到太空环境中的辐射等因素影响，导致计算错误。

**核心思路**：论文的核心思路是利用新一代多核处理器的强大算力加速GNC/LVS算法的执行，并通过多核冗余和投票机制（ARBITER）实现实时故障检测和纠正，从而提高计算的可靠性。这种设计旨在兼顾性能和可靠性，满足深空探测任务的需求。

**技术框架**：整体架构包含GNC和LVS算法的部署以及ARBITER容错机制。GNC算法包括燃料最优大偏差（GFOLD）轨迹优化和姿态控制系统。LVS算法用于图像处理。ARBITER作为多核投票机制，在多个核心上并行运行相同的计算任务，并对结果进行投票，以检测和纠正错误。

**关键创新**：论文的关键创新在于将高性能多核处理器与多核投票容错机制相结合，为深空探测任务提供了一种可扩展且节能的计算架构。ARBITER机制能够实时检测和纠正错误，提高了计算的可靠性，而多核处理器则提供了足够的算力来支持复杂的GNC/LVS算法。

**关键设计**：ARBITER机制的关键设计包括异步冗余执行、行为检查和投票仲裁。异步冗余执行允许在多个核心上并行运行相同的计算任务，而无需同步。行为检查用于检测核心的异常行为。投票仲裁则根据多个核心的输出结果进行投票，以确定最终的输出结果。此外，论文还通过故障注入研究确定了GFOLD算法中对位级错误最敏感的梯度计算阶段，并针对性地提出了选择性保护策略和基于向量的输出仲裁方法。

## 📊 实验亮点

实验结果表明，在新一代多核处理器上部署GNC和LVS算法，LVS图像处理速度提升高达15倍，GFOLD轨迹优化速度提升超过250倍（相比传统航天硬件）。ARBITER容错机制在静态优化任务（GFOLD）和动态闭环控制（姿态控制系统）中都得到了验证，能够有效检测和纠正错误。故障注入研究表明，GFOLD中的梯度计算阶段对位级错误最敏感，为选择性保护策略提供了依据。

## 🎯 应用场景

该研究成果可应用于未来的深空探测任务，如火星样本返回、土卫二Orbilander和谷神星样本返回等。通过提高车载自主性和计算可靠性，可以降低对地面站的依赖，提高任务的灵活性和效率。此外，该架构也可应用于其他需要高性能和高可靠性计算的领域，如自动驾驶、机器人等。

## 📄 摘要（原文）

> Future planetary exploration missions demand high-performance, fault-tolerant computing to enable autonomous Guidance, Navigation, and Control (GNC) and Lander Vision System (LVS) operations during Entry, Descent, and Landing (EDL). This paper evaluates the deployment of GNC and LVS algorithms on next-generation multi-core processors--HPSC, Snapdragon VOXL2, and AMD Xilinx Versal--demonstrating up to 15x speedup for LVS image processing and over 250x speedup for Guidance for Fuel-Optimal Large Divert (GFOLD) trajectory optimization compared to legacy spaceflight hardware. To ensure computational reliability, we present ARBITER (Asynchronous Redundant Behavior Inspection for Trusted Execution and Recovery), a Multi-Core Voting (MV) mechanism that performs real-time fault detection and correction across redundant cores. ARBITER is validated in both static optimization tasks (GFOLD) and dynamic closed-loop control (Attitude Control System). A fault injection study further identifies the gradient computation stage in GFOLD as the most sensitive to bit-level errors, motivating selective protection strategies and vector-based output arbitration. This work establishes a scalable and energy-efficient architecture for future missions, including Mars Sample Return, Enceladus Orbilander, and Ceres Sample Return, where onboard autonomy, low latency, and fault resilience are critical.

