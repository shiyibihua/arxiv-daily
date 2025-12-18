---
layout: default
title: Multiplayer Nash Preference Optimization
---

# Multiplayer Nash Preference Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23102" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23102v1</a>
  <a href="https://arxiv.org/pdf/2509.23102.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23102v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23102v1', 'Multiplayer Nash Preference Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fang Wu, Xu Huang, Weihao Xuan, Zhiwei Zhang, Yijia Xiao, Guancheng Wan, Xiaomin Li, Bing Hu, Peng Xia, Jure Leskovec, Yejin Choi

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-27

**🔗 代码/项目**: [GITHUB](https://github.com/smiles724/MNPO)

---

## 💡 一句话要点

**提出多玩家纳什偏好优化（MNPO），提升LLM在复杂偏好下的对齐效果。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型对齐` `人类反馈强化学习` `纳什均衡` `多玩家博弈` `偏好优化`

## 📋 核心要点

1. 现有基于奖励的RLHF方法难以捕捉人类偏好的非传递性和异质性，导致对齐效果不佳。
2. MNPO将对齐问题建模为n人博弈，每个策略与多个对手竞争，并正则化到参考模型，从而捕捉更丰富的偏好结构。
3. 实验表明，MNPO在指令跟随任务上优于现有NLHF方法，尤其在异构标注和混合策略评估中表现更佳。

## 📝 摘要（中文）

从人类反馈中进行强化学习（RLHF）已成为使大型语言模型（LLM）与人类偏好对齐的标准范式。然而，基于Bradley-Terry假设的基于奖励的方法难以捕捉真实世界偏好的非传递性和异质性。为了解决这个问题，最近的研究将对齐重新定义为一个双人纳什博弈，从而产生了基于人类反馈的纳什学习（NLHF）。虽然这种视角激发了诸如INPO、ONPO和EGPO等具有强大理论和经验保证的算法，但它们仍然从根本上局限于双人交互，产生了一种单一对手偏差，无法捕捉现实偏好结构的全部复杂性。在这项工作中，我们引入了多玩家纳什偏好优化（MNPO），这是一个将NLHF推广到多玩家机制的新框架。它将对齐形式化为一个n人博弈，其中每个策略与一个对手群体竞争，同时被正则化到一个参考模型。我们的框架在多玩家环境中建立了明确定义的纳什均衡，并将对偶间隙的概念扩展到量化近似质量。我们证明MNPO继承了双人方法的均衡保证，同时实现了更丰富的竞争动态和对多样化偏好结构的更好覆盖。通过全面的经验评估，我们表明MNPO在指令跟随基准测试中始终优于现有的NLHF基线，在异构标注者条件和混合策略评估场景下实现了卓越的对齐质量。总之，这些结果确立了MNPO作为一个原则性和可扩展的框架，用于使LLM与复杂的、非传递的人类偏好对齐。

## 🔬 方法详解

**问题定义**：现有基于人类反馈的强化学习（RLHF）方法，特别是基于Bradley-Terry模型的奖励学习方法，在处理复杂的、非传递性的人类偏好时表现不足。这些方法通常假设偏好是传递的，并且忽略了不同标注者之间的异质性，导致学习到的奖励模型无法准确反映真实的人类偏好。此外，现有的纳什学习方法（NLHF）主要局限于双人博弈，无法捕捉多方交互的复杂性，产生单一对手偏差。

**核心思路**：MNPO的核心思路是将LLM的对齐问题建模为一个多玩家纳什博弈。在这个博弈中，每个策略（例如，LLM的不同版本或策略）都与其他策略群体进行竞争。通过引入多个对手，MNPO能够更好地捕捉人类偏好的多样性和非传递性。同时，MNPO通过将每个策略正则化到一个参考模型，保证了训练的稳定性，避免了策略崩溃。

**技术框架**：MNPO的整体框架包括以下几个主要组成部分：1）**策略网络**：用于生成LLM的输出。2）**参考模型**：用于提供策略正则化，防止策略偏离过远。3）**偏好数据**：由人类标注者提供的偏好比较数据。4）**纳什均衡求解器**：用于找到多玩家博弈的纳什均衡策略。MNPO的训练流程如下：首先，从策略网络和参考模型中采样生成多个输出。然后，将这些输出呈现给人类标注者，收集偏好数据。接下来，使用偏好数据训练策略网络，使其能够生成更符合人类偏好的输出。同时，使用参考模型对策略网络进行正则化。最后，使用纳什均衡求解器找到多玩家博弈的纳什均衡策略。

**关键创新**：MNPO的关键创新在于将NLHF扩展到多玩家博弈。与传统的双人博弈方法相比，MNPO能够更好地捕捉人类偏好的多样性和非传递性。此外，MNPO还引入了对偶间隙的概念，用于量化多玩家博弈的近似质量，为算法的收敛性提供了理论保证。

**关键设计**：MNPO的关键设计包括：1）**多玩家博弈的建模**：MNPO将LLM的对齐问题建模为一个n人博弈，其中每个策略与其他策略群体进行竞争。2）**策略正则化**：MNPO使用参考模型对策略网络进行正则化，防止策略偏离过远。3）**对偶间隙的量化**：MNPO引入了对偶间隙的概念，用于量化多玩家博弈的近似质量。4）**损失函数**：MNPO使用基于偏好数据的损失函数来训练策略网络，使其能够生成更符合人类偏好的输出。具体的损失函数形式可能根据具体的偏好模型（例如，Bradley-Terry模型或Hinge Loss）而有所不同。

## 📊 实验亮点

实验结果表明，MNPO在指令跟随基准测试中始终优于现有的NLHF基线。在异构标注者条件下，MNPO能够更好地适应不同标注者的偏好差异，实现更高的对齐质量。在混合策略评估场景下，MNPO能够更好地应对来自不同策略的挑战，表现出更强的鲁棒性。具体性能提升数据在论文中给出，证明了MNPO在复杂偏好环境下的优越性。

## 🎯 应用场景

MNPO可应用于各种需要与人类偏好对齐的LLM应用场景，例如对话系统、文本生成、代码生成等。通过更好地捕捉复杂的人类偏好，MNPO可以提高LLM的实用性和用户满意度。此外，MNPO还可以用于个性化推荐系统，根据用户的个人偏好提供更精准的推荐结果。未来，MNPO有望成为LLM对齐的标准框架，推动LLM在各个领域的广泛应用。

## 📄 摘要（原文）

> Reinforcement learning from human feedback (RLHF) has emerged as the standard paradigm for aligning large language models (LLMs) with human preferences. However, reward-based methods built on the Bradley-Terry assumption struggle to capture the non-transitive and heterogeneous nature of real-world preferences. To address this, recent studies have reframed alignment as a two-player Nash game, giving rise to Nash learning from human feedback (NLHF). While this perspective has inspired algorithms such as INPO, ONPO, and EGPO with strong theoretical and empirical guarantees, they remain fundamentally restricted to two-player interactions, creating a single-opponent bias that fails to capture the full complexity of realistic preference structures. In this work, we introduce Multiplayer Nash Preference Optimization (MNPO), a novel framework that generalizes NLHF to the multiplayer regime. It formulates alignment as an $n$-player game, where each policy competes against a population of opponents while being regularized toward a reference model. Our framework establishes well-defined Nash equilibria in multiplayer settings and extends the concept of duality gap to quantify approximation quality. We demonstrate that MNPO inherits the equilibrium guarantees of two-player methods while enabling richer competitive dynamics and improved coverage of diverse preference structures. Through comprehensive empirical evaluation, we show that MNPO consistently outperforms existing NLHF baselines on instruction-following benchmarks, achieving superior alignment quality under heterogeneous annotator conditions and mixed-policy evaluation scenarios. Together, these results establish MNPO as a principled and scalable framework for aligning LLMs with complex, non-transitive human preferences. Code is available at https://github.com/smiles724/MNPO.

