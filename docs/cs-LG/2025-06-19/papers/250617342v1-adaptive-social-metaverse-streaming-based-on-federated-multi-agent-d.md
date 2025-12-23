---
layout: default
title: Adaptive Social Metaverse Streaming based on Federated Multi-Agent Deep Reinforcement Learning
---

# Adaptive Social Metaverse Streaming based on Federated Multi-Agent Deep Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17342" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17342v1</a>
  <a href="https://arxiv.org/pdf/2506.17342.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17342v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17342v1', 'Adaptive Social Metaverse Streaming based on Federated Multi-Agent Deep Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zijian Long, Haopeng Wang, Haiwei Dong, Abdulmotaleb El Saddik

**分类**: cs.LG, cs.AI, cs.MM, cs.NI

**发布日期**: 2025-06-19

**备注**: Accepted by IEEE Transactions on Computational Social Systems

**DOI**: [10.1109/TCSS.2025.3555419](https://doi.org/10.1109/TCSS.2025.3555419)

---

## 💡 一句话要点

**提出ASMS以解决社交元宇宙流媒体隐私与延迟问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `社交元宇宙` `流媒体传输` `隐私保护` `深度强化学习` `联邦学习` `动态调整` `用户体验`

## 📋 核心要点

1. 现有流媒体方法在社交元宇宙中面临隐私保护和低延迟传输的双重挑战，难以满足用户需求。
2. 本文提出的ASMS系统通过F-MAPPO结合联邦学习和深度强化学习，动态调整流媒体比特率，确保用户隐私。
3. 实验结果显示，ASMS在不同网络条件下相比传统方法提升了至少14%的用户体验，显著改善了流媒体质量。

## 📝 摘要（中文）

社交元宇宙是一个融合虚拟与现实世界的数字生态系统，用户可以在其中进行社交互动、工作、购物和娱乐。然而，隐私问题依然是一个重大挑战，因为沉浸式互动需要持续收集生物特征和行为数据。同时，由于实时互动、沉浸式渲染和带宽优化的需求，确保高质量、低延迟的流媒体传输变得困难。为了解决这些问题，本文提出了ASMS（自适应社交元宇宙流媒体），这是一种基于联邦多智能体近端策略优化（F-MAPPO）的新型流媒体系统。ASMS利用F-MAPPO，结合联邦学习和深度强化学习，动态调整流媒体比特率，同时保护用户隐私。实验结果表明，ASMS在各种网络条件下相比现有流媒体方法提升了至少14%的用户体验。

## 🔬 方法详解

**问题定义**：本文旨在解决社交元宇宙中流媒体传输的隐私保护与低延迟问题。现有方法在实时互动和数据隐私方面存在显著不足，无法有效满足用户需求。

**核心思路**：ASMS通过引入F-MAPPO，将联邦学习与深度强化学习相结合，动态调整流媒体的比特率，从而在保证用户隐私的前提下提升流媒体质量。

**技术框架**：ASMS的整体架构包括数据收集模块、F-MAPPO训练模块和流媒体传输模块。数据收集模块负责获取用户的行为数据，F-MAPPO训练模块则根据实时反馈调整流媒体比特率，流媒体传输模块负责将数据传输到用户设备。

**关键创新**：ASMS的核心创新在于将联邦学习与深度强化学习结合，形成F-MAPPO，能够在保护用户隐私的同时，实现流媒体传输的动态优化。这一设计与现有方法的根本区别在于其对用户数据的本地处理能力。

**关键设计**：在ASMS中，关键参数包括流媒体比特率的动态调整范围、F-MAPPO的训练周期和损失函数的设计，确保系统在不同网络条件下的适应性和稳定性。

## 📊 实验亮点

实验结果表明，ASMS在各种网络条件下相比现有流媒体方法提升了至少14%的用户体验，显示出其在流媒体质量和用户隐私保护方面的显著优势。这一成果为社交元宇宙的可持续发展提供了有力支持。

## 🎯 应用场景

该研究的潜在应用场景包括社交元宇宙平台、在线游戏、虚拟会议等领域，能够为用户提供更流畅的互动体验，同时保护用户的隐私数据。随着社交元宇宙的不断发展，ASMS的技术方案将对未来的数字生态系统产生深远影响。

## 📄 摘要（原文）

> The social metaverse is a growing digital ecosystem that blends virtual and physical worlds. It allows users to interact socially, work, shop, and enjoy entertainment. However, privacy remains a major challenge, as immersive interactions require continuous collection of biometric and behavioral data. At the same time, ensuring high-quality, low-latency streaming is difficult due to the demands of real-time interaction, immersive rendering, and bandwidth optimization. To address these issues, we propose ASMS (Adaptive Social Metaverse Streaming), a novel streaming system based on Federated Multi-Agent Proximal Policy Optimization (F-MAPPO). ASMS leverages F-MAPPO, which integrates federated learning (FL) and deep reinforcement learning (DRL) to dynamically adjust streaming bit rates while preserving user privacy. Experimental results show that ASMS improves user experience by at least 14% compared to existing streaming methods across various network conditions. Therefore, ASMS enhances the social metaverse experience by providing seamless and immersive streaming, even in dynamic and resource-constrained networks, while ensuring that sensitive user data remains on local devices.

