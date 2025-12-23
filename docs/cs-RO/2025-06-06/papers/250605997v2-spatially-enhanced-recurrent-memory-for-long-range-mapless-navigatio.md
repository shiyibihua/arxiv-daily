---
layout: default
title: Spatially-Enhanced Recurrent Memory for Long-Range Mapless Navigation via End-to-End Reinforcement Learning
---

# Spatially-Enhanced Recurrent Memory for Long-Range Mapless Navigation via End-to-End Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05997" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05997v2</a>
  <a href="https://arxiv.org/pdf/2506.05997.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05997v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05997v2', 'Spatially-Enhanced Recurrent Memory for Long-Range Mapless Navigation via End-to-End Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fan Yang, Per Frivik, David Hoeller, Chen Wang, Cesar Cadena, Marco Hutter

**分类**: cs.RO

**发布日期**: 2025-06-06 (更新: 2025-09-04)

**备注**: 22 pages

---

## 💡 一句话要点

**提出空间增强递归记忆以解决长距离无地图导航问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长距离导航` `无地图导航` `空间记忆` `递归神经网络` `强化学习` `机器人导航` `注意力机制`

## 📋 核心要点

1. 现有的导航方法在空间记忆能力上存在不足，无法有效整合来自不同视角的序列观察。
2. 本文提出空间增强递归单元（SRUs），通过改进RNN结构来增强空间记忆能力，并结合注意力机制实现长距离无地图导航。
3. 实验结果显示，使用SRU记忆的方法在长距离导航上比依赖显式映射和堆叠历史观察的基线分别提升29.6%和105.0%。

## 📝 摘要（中文）

近年来，机器人导航领域特别是端到端学习方法如强化学习（RL）的进展显示出强大的性能。然而，成功导航仍依赖于两个关键能力：映射和规划。传统方法依赖显式映射管道将自我中心观察注册到一致的地图中，而端到端学习则通过递归神经网络（RNN）隐式实现。现有架构如LSTM和GRU能够捕捉时间依赖性，但在空间记忆方面存在关键限制。为此，本文提出空间增强递归单元（SRUs），对现有RNN进行有效改进，增强空间记忆能力。实验结果表明，与现有RNN相比，长距离导航整体提升23.5%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有递归神经网络在长距离导航中空间记忆不足的问题。现有方法依赖显式映射，无法有效整合不同视角的观察数据。

**核心思路**：提出空间增强递归单元（SRUs），通过对RNN的简单有效修改，增强其空间记忆能力，以支持更好的规划和导航。

**技术框架**：整体架构包括SRUs和基于注意力的网络结构，利用单个前向立体相机进行长距离导航。通过正则化技术促进端到端的递归训练。

**关键创新**：SRUs是本文的核心创新点，显著提升了空间记忆能力，与传统的LSTM和GRU方法相比，能够更好地处理空间信息。

**关键设计**：在网络结构中，SRUs通过调整记忆单元的设计，结合注意力机制，优化了参数设置和损失函数，以实现更高效的训练和导航性能。

## 📊 实验亮点

实验结果显示，使用SRU记忆的导航方法在长距离导航任务中整体提升23.5%。与依赖显式映射和堆叠历史观察的基线相比，分别提升了29.6%和105.0%，展现了显著的性能优势。

## 🎯 应用场景

该研究的潜在应用领域包括自主机器人导航、无人驾驶汽车以及智能家居等场景。通过增强空间记忆能力，机器人能够在复杂环境中更有效地进行导航和决策，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advancements in robot navigation, particularly with end-to-end learning approaches such as reinforcement learning (RL), have demonstrated strong performance. However, successful navigation still depends on two key capabilities: mapping and planning (explicitly or implicitly). Classical approaches rely on explicit mapping pipelines to register egocentric observations into a coherent map. In contrast, end-to-end learning often achieves this implicitly -- through recurrent neural networks (RNNs) that fuse current and historical observations into a latent space for planning. While existing architectures, such as LSTM and GRU, can capture temporal dependencies, our findings reveal a critical limitation: their inability to effectively perform spatial memorization. This capability is essential for integrating sequential observations from varying perspectives to build spatial representations that support planning. To address this, we propose Spatially-Enhanced Recurrent Units (SRUs) -- a simple yet effective modification to existing RNNs -- that enhance spatial memorization. We further introduce an attention-based network architecture integrated with SRUs, enabling long-range mapless navigation using a single forward-facing stereo camera. We also employ regularization techniques to facilitate robust end-to-end recurrent training via RL. Experimental results show 23.5% overall improvement in long-range navigation compared to existing RNNs. With SRU memory, our method outperforms RL baselines -- one relying on explicit mapping and the other on stacked historical observations -- by 29.6% and 105.0%, respectively, across diverse environments requiring long-horizon mapping and memorization. Finally, we address the sim-to-real gap by leveraging large-scale pretraining on synthetic depth data, enabling zero-shot transfer for deployment across diverse and complex real-world environments.

