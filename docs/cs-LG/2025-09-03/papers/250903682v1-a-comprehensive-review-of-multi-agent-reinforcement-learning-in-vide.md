---
layout: default
title: A Comprehensive Review of Multi-Agent Reinforcement Learning in Video Games
---

# A Comprehensive Review of Multi-Agent Reinforcement Learning in Video Games

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03682" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03682v1</a>
  <a href="https://arxiv.org/pdf/2509.03682.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03682v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03682v1', 'A Comprehensive Review of Multi-Agent Reinforcement Learning in Video Games')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhengyang Li, Qijin Ji, Xinghong Ling, Quan Liu

**分类**: cs.LG

**发布日期**: 2025-09-03

**备注**: IEEE Transactions on Games, 2025

**DOI**: [10.1109/TG.2025.3588809](https://doi.org/10.1109/TG.2025.3588809)

---

## 💡 一句话要点

**综述多智能体强化学习在视频游戏中的应用与挑战**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多智能体强化学习` `视频游戏AI` `深度强化学习` `自博弈` `团队协作` `非平稳环境` `部分可观测性`

## 📋 核心要点

1. 现有MARL方法在视频游戏中面临非平稳环境、部分可观测、稀疏奖励等挑战，限制了其应用效果。
2. 该综述旨在全面分析MARL在不同类型视频游戏中的应用，并探讨解决上述挑战的策略。
3. 论文分析了MARL在各类游戏中的成功案例，并提出了一种新的游戏复杂度评估方法，为未来研究提供方向。

## 📝 摘要（中文）

多智能体强化学习(MARL)的最新进展表明其在现代游戏中具有应用潜力。从基础工作到里程碑式的成就，如星际争霸II中的AlphaStar和Dota 2中的OpenAI Five，MARL已经证明了通过自博弈、监督学习和深度强化学习等技术，能够在不同的游戏环境中实现超人的性能。随着其影响力的增长，全面的综述变得越来越重要。本文旨在全面考察MARL在视频游戏中的应用，从回合制双智能体游戏到实时多智能体视频游戏，包括体育游戏、第一人称射击(FPS)游戏、实时战略(RTS)游戏和多人在线战斗竞技场(MOBA)游戏等流行类型。我们进一步分析了MARL在视频游戏中面临的关键挑战，包括非平稳性、部分可观察性、稀疏奖励、团队协调和可扩展性，并重点介绍了在火箭联盟、我的世界、雷神之锤III竞技场、星际争霸II、Dota 2、王者荣耀等游戏中的成功应用。本文深入了解了MARL在视频游戏AI系统中的应用，提出了一种估计游戏复杂性的新方法，并提出了未来的研究方向，以推进MARL及其在游戏开发中的应用，从而激发这个快速发展领域的进一步创新。

## 🔬 方法详解

**问题定义**：多智能体强化学习在视频游戏中面临诸多挑战，例如环境的非平稳性（non-stationarity），由于其他智能体的策略也在不断变化；部分可观测性（partial observability），每个智能体只能观察到环境的一部分信息；稀疏奖励（sparse rewards），智能体很难获得有效的奖励信号；团队协调（team coordination），智能体之间需要协同合作才能完成任务；以及可扩展性（scalability），当智能体数量增加时，算法的计算复杂度会急剧上升。这些问题使得训练出能够在复杂游戏中表现良好的MARL智能体变得非常困难。

**核心思路**：该综述的核心思路是系统性地梳理MARL在不同类型视频游戏中的应用现状，分析现有方法在解决上述挑战时所采用的策略，并总结成功案例的经验。通过对不同游戏类型和MARL算法的对比分析，为研究人员提供一个全面的视角，从而更好地理解MARL在视频游戏中的应用潜力和局限性。

**技术框架**：该综述的技术框架主要包括以下几个部分：首先，介绍MARL的基础知识和常用算法；其次，按照游戏类型（如体育游戏、FPS游戏、RTS游戏、MOBA游戏等）分类，分别介绍MARL在这些游戏中的应用案例；然后，分析MARL在视频游戏中面临的关键挑战，并讨论现有方法如何应对这些挑战；最后，提出一种新的游戏复杂度评估方法，并展望未来的研究方向。

**关键创新**：该综述的创新之处在于其全面性和系统性。它不仅涵盖了MARL在各种类型视频游戏中的应用，还深入分析了MARL面临的挑战和现有方法的局限性。此外，该综述还提出了一种新的游戏复杂度评估方法，为研究人员提供了一个新的工具来评估不同游戏的难度。

**关键设计**：该综述的关键设计在于其结构化的组织方式。通过按照游戏类型和挑战类型进行分类，使得读者可以快速找到自己感兴趣的内容。此外，该综述还包含了大量的参考文献，方便读者进一步深入研究。

## 📊 实验亮点

该综述总结了MARL在《火箭联盟》、《我的世界》、《雷神之锤III竞技场》、《星际争霸II》、《Dota 2》、《王者荣耀》等游戏中的成功应用案例，展示了MARL在不同游戏类型中取得的性能提升。此外，论文还提出了一种新的游戏复杂度评估方法，为MARL算法的设计和选择提供了参考。

## 🎯 应用场景

该研究成果可应用于游戏AI开发，提升游戏智能体的决策能力和协作水平，创造更具挑战性和趣味性的游戏体验。此外，MARL技术在游戏中的应用经验，可以推广到其他多智能体协作场景，如自动驾驶、机器人协同、交通调度等。

## 📄 摘要（原文）

> Recent advancements in multi-agent reinforcement learning (MARL) have demonstrated its application potential in modern games. Beginning with foundational work and progressing to landmark achievements such as AlphaStar in StarCraft II and OpenAI Five in Dota 2, MARL has proven capable of achieving superhuman performance across diverse game environments through techniques like self-play, supervised learning, and deep reinforcement learning. With its growing impact, a comprehensive review has become increasingly important in this field. This paper aims to provide a thorough examination of MARL's application from turn-based two-agent games to real-time multi-agent video games including popular genres such as Sports games, First-Person Shooter (FPS) games, Real-Time Strategy (RTS) games and Multiplayer Online Battle Arena (MOBA) games. We further analyze critical challenges posed by MARL in video games, including nonstationary, partial observability, sparse rewards, team coordination, and scalability, and highlight successful implementations in games like Rocket League, Minecraft, Quake III Arena, StarCraft II, Dota 2, Honor of Kings, etc. This paper offers insights into MARL in video game AI systems, proposes a novel method to estimate game complexity, and suggests future research directions to advance MARL and its applications in game development, inspiring further innovation in this rapidly evolving field.

