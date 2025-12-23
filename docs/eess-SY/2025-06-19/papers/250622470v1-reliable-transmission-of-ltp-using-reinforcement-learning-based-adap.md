---
layout: default
title: Reliable Transmission of LTP Using Reinforcement Learning-Based Adaptive FEC
---

# Reliable Transmission of LTP Using Reinforcement Learning-Based Adaptive FEC

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22470" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22470v1</a>
  <a href="https://arxiv.org/pdf/2506.22470.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22470v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22470v1', 'Reliable Transmission of LTP Using Reinforcement Learning-Based Adaptive FEC')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liang Chen, Yu Song, Kanglian Zhao, Juan A. Fraire, Wenfeng Li

**分类**: cs.NI, eess.SY

**发布日期**: 2025-06-19

**备注**: 15 pages, 30 figures, Liang Chen and Yu Song are co-first authors

---

## 💡 一句话要点

**提出基于强化学习的自适应FEC以解决深空网络数据传输问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深空网络` `自适应FEC` `强化学习` `数据传输` `信道预测` `编码效率` `矩阵解码` `LTP`

## 📋 核心要点

1. 现有的静态和动态编码方法在深空网络中面对高度可变的信道条件时，无法有效降低重传时间成本。
2. 本文提出了一种基于强化学习的自适应FEC算法，通过历史反馈预测信道条件并调整编码速率，旨在提高数据传输的可靠性。
3. 实验结果表明，该算法在地月和地火链路场景中显著减少了矩阵解码失败，提升幅度超过2/3。

## 📝 摘要（中文）

延迟/中断容忍网络（DTN）采用Licklider传输协议（LTP）和自动重传请求（ARQ）来实现可靠的数据传输。然而，现有的静态和基于延迟反馈的动态编码方法在深空信道条件高度可变和不可预测的情况下表现不佳。本文提出了一种基于强化学习的自适应前向纠错（FEC）算法，利用历史反馈和系统状态预测未来信道条件，并主动调整编码速率，从而提高编码效率，减少重传次数。通过在模拟的地月和地火链路场景中进行的性能评估，验证了该算法在优化深空网络数据传输方面的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决在深空网络中，现有静态和动态编码方法无法适应高度可变信道条件的问题，导致重传时间成本高和解码失败率高。

**核心思路**：提出的自适应FEC算法基于强化学习，通过历史反馈和系统状态预测未来信道质量，主动调整编码速率，以应对信道质量的变化。

**技术框架**：该算法的整体架构包括数据采集模块、信道状态预测模块和编码速率调整模块。数据采集模块负责收集历史反馈，预测模块利用强化学习算法进行信道状态预测，调整模块根据预测结果动态调整编码速率。

**关键创新**：最重要的技术创新在于引入强化学习来实现自适应编码速率调整，这与现有静态和基于延迟反馈的动态方法形成了鲜明对比，能够更有效地应对信道条件的变化。

**关键设计**：算法中采用了特定的损失函数来优化预测精度，并设计了适合深空网络的网络结构，以提高模型的学习效率和适应性。

## 📊 实验亮点

实验结果显示，基于强化学习的自适应FEC算法在地月和地火链路场景中，矩阵解码失败率减少了至少2/3，相较于现有方法显著提升了数据传输的可靠性和效率。

## 🎯 应用场景

该研究的潜在应用领域包括深空探测任务、卫星通信和其他需要在不稳定信道条件下进行可靠数据传输的场景。通过提高数据传输的可靠性和效率，能够为未来的深空探索和通信提供重要支持，推动相关技术的发展。

## 📄 摘要（原文）

> Delay/Disruption Tolerant Networking (DTN) employs the Licklider Transmission Protocol (LTP) with Automatic Repeat reQuest (ARQ) for reliable data delivery in challenging interplanetary networks. While previous studies have integrated packet-level Forward Erasure Correction (FEC) into LTP to reduce retransmission time costs, existing static and delay-feedback-based dynamic coding methods struggle with highly variable and unpredictable deep space channel conditions. This paper proposes a reinforcement learning (RL)-based adaptive FEC algorithm to address these limitations. The algorithm utilizes historical feedback and system state to predict future channel conditions and proactively adjust the code rate. This approach aims to anticipate channel quality degradation, thereby preventing decoding failures and subsequent LTP retransmissions and improving coding efficiency by minimizing redundancy during favorable channel conditions. Performance evaluations conducted in simulated Earth-Moon and Earth-Mars link scenarios demonstrate this algorithm's effectiveness in optimizing data transmission for interplanetary networks. Compared to existing methods, this approach demonstrates significant improvement, with matrix decoding failures reduced by at least 2/3.

