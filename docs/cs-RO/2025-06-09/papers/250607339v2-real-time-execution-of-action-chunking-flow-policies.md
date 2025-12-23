---
layout: default
title: Real-Time Execution of Action Chunking Flow Policies
---

# Real-Time Execution of Action Chunking Flow Policies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.07339" class="toolbar-btn" target="_blank">📄 arXiv: 2506.07339v2</a>
  <a href="https://arxiv.org/pdf/2506.07339.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.07339v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.07339v2', 'Real-Time Execution of Action Chunking Flow Policies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kevin Black, Manuel Y. Galliker, Sergey Levine

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-06-09 (更新: 2025-12-05)

**备注**: published in NeurIPS 2025

---

## 💡 一句话要点

**提出实时动作分块流策略以解决延迟问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `实时控制` `动作分块` `异步执行` `机器人操作` `高频任务`

## 📋 核心要点

1. 核心问题：现有的通用模型在执行高频控制任务时存在显著延迟，导致动作分块边界处的不稳定性和暂停。
2. 方法要点：提出实时分块（RTC）算法，在执行当前动作的同时生成下一个动作分块，确保动作的平滑过渡。
3. 实验或效果：在Kinetix模拟器和实际双手操作任务中，RTC显著提高了任务的吞吐量和成功率，尤其在高延迟情况下表现优异。

## 📝 摘要（中文）

现代人工智能系统，尤其是与物理世界交互的系统，越来越需要实时性能。然而，当前通用模型的高延迟，特别是最近的视觉-语言动作模型（VLA），带来了显著挑战。尽管动作分块在高频控制任务中实现了时间一致性，但仍未完全解决延迟问题，导致在分块边界处出现暂停或不稳定的运动。本文提出了一种新颖的推理时间算法，能够实现动作分块策略的平滑异步执行。我们的实时分块（RTC）方法适用于任何扩散或流基VLA，无需重新训练。它在执行当前动作的同时生成下一个动作分块，确保执行的动作“冻结”，其余部分进行“填充”。通过在Kinetix模拟器中引入12个高度动态任务的新基准，并评估6个具有挑战性的双手操作任务，结果表明RTC快速、高效，并对推理延迟具有独特的鲁棒性，显著提高了任务吞吐量，并在精确任务中实现了高成功率。

## 🔬 方法详解

**问题定义**：本论文旨在解决现代AI系统在执行高频控制任务时的延迟问题。现有方法在动作分块边界处常常导致暂停或不稳定的运动，影响任务的流畅性和成功率。

**核心思路**：论文提出的实时分块（RTC）算法通过在执行当前动作的同时生成下一个动作分块，确保动作的平滑过渡，从而有效降低延迟对系统性能的影响。

**技术框架**：RTC的整体架构包括两个主要模块：当前动作的执行模块和下一个动作分块的生成模块。当前模块负责实时执行动作，而生成模块则在此过程中计算下一个动作分块。

**关键创新**：RTC的核心创新在于其异步执行机制，能够在不需要重新训练的情况下，直接应用于现有的扩散或流基VLA，显著提高了系统的实时性和鲁棒性。

**关键设计**：在设计RTC时，关键参数包括动作生成的时间窗口和填充策略，确保在高延迟情况下仍能保持动作的连贯性和一致性。

## 📊 实验亮点

实验结果表明，RTC在12个动态任务和6个实际双手操作任务中表现出色，显著提高了任务的吞吐量和成功率。在高延迟情况下，RTC仍能保持高效的动作执行，展示了其在复杂任务中的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动驾驶、虚拟现实等需要实时反应的系统。通过提高动作执行的流畅性和准确性，RTC能够在复杂环境中实现更高效的任务执行，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Modern AI systems, especially those interacting with the physical world, increasingly require real-time performance. However, the high latency of state-of-the-art generalist models, including recent vision-language action models (VLAs), poses a significant challenge. While action chunking has enabled temporal consistency in high-frequency control tasks, it does not fully address the latency problem, leading to pauses or out-of-distribution jerky movements at chunk boundaries. This paper presents a novel inference-time algorithm that enables smooth asynchronous execution of action chunking policies. Our method, real-time chunking (RTC), is applicable to any diffusion- or flow-based VLA out of the box with no re-training. It generates the next action chunk while executing the current one, "freezing" actions guaranteed to execute and "inpainting" the rest. To test RTC, we introduce a new benchmark of 12 highly dynamic tasks in the Kinetix simulator, as well as evaluate 6 challenging real-world bimanual manipulation tasks. Results demonstrate that RTC is fast, performant, and uniquely robust to inference delay, significantly improving task throughput and enabling high success rates in precise tasks $\unicode{x2013}$ such as lighting a match $\unicode{x2013}$ even in the presence of significant latency. See https://pi.website/research/real_time_chunking for videos.

