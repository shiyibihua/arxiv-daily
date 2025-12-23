---
layout: default
title: Collapsing Sequence-Level Data-Policy Coverage via Poisoning Attack in Offline Reinforcement Learning
---

# Collapsing Sequence-Level Data-Policy Coverage via Poisoning Attack in Offline Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11172" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11172v1</a>
  <a href="https://arxiv.org/pdf/2506.11172.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11172v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11172v1', 'Collapsing Sequence-Level Data-Policy Coverage via Poisoning Attack in Offline Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xue Zhou, Dapeng Man, Chen Xu, Fanyi Zeng, Tao Liu, Huan Wang, Shucheng He, Chaoyang Gao, Wu Yang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**提出序列级数据-策略覆盖崩溃攻击以解决离线强化学习安全问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `离线强化学习` `数据覆盖` `毒化攻击` `安全性分析` `决策模式`

## 📋 核心要点

1. 现有离线强化学习方法在数据-策略覆盖方面存在不足，未能有效应对安全风险。
2. 本文提出序列级集中系数来量化覆盖，并设计CSDPC毒化攻击以降低覆盖率。
3. 实验结果显示，毒化1%的数据集可导致代理性能下降90%，揭示了安全隐患。

## 📝 摘要（中文）

离线强化学习（RL）严重依赖于预先收集的数据覆盖目标策略的分布。现有研究旨在改善数据-策略覆盖以减轻分布偏移，但忽视了由于覆盖不足带来的安全风险，且单步分析与离线RL的多步决策特性不一致。为此，本文引入序列级集中系数来量化覆盖，并通过理论分析揭示其对估计误差上界的指数放大效应。在此基础上，提出了崩溃序列级数据-策略覆盖（CSDPC）毒化攻击。考虑到离线RL数据的连续性，我们将状态-动作对转换为决策单元，提取捕捉多步行为的代表性决策模式，识别可能导致覆盖不足的稀有模式，并对其进行毒化以减少覆盖并加剧分布偏移。实验表明，仅毒化1%的数据集即可使代理性能下降90%。这一发现为分析和保护离线RL的安全性提供了新视角。

## 🔬 方法详解

**问题定义**：本文旨在解决离线强化学习中由于数据-策略覆盖不足而导致的安全风险。现有方法未能充分考虑覆盖不足的潜在影响，且单步分析无法反映多步决策的复杂性。

**核心思路**：论文引入序列级集中系数来量化数据-策略覆盖，并通过理论分析揭示其对估计误差的影响。基于此，提出CSDPC毒化攻击，通过识别稀有决策模式来降低覆盖率。

**技术框架**：整体流程包括数据收集、决策模式提取、稀有模式识别和毒化攻击实施。首先将状态-动作对转换为决策单元，然后提取代表性模式，最后对识别出的稀有模式进行毒化。

**关键创新**：最重要的创新在于引入序列级集中系数和CSDPC毒化攻击，前者量化了覆盖程度，后者通过针对稀有模式的攻击显著降低了覆盖率，与现有方法相比具有更高的安全性分析能力。

**关键设计**：在技术细节上，论文设计了特定的损失函数来优化毒化效果，并采用了深度学习模型来提取决策模式，确保能够捕捉到多步决策的复杂性。实验中还对毒化比例进行了细致的调节，以评估其对性能的影响。

## 📊 实验亮点

实验结果表明，仅需毒化1%的数据集即可使代理性能下降90%，这一显著的性能下降揭示了离线强化学习在数据覆盖不足情况下的脆弱性。与基线方法相比，CSDPC毒化攻击展现出更强的攻击效果，为离线RL的安全性分析提供了新的视角。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人控制和金融决策等需要依赖历史数据进行决策的场景。通过提高离线强化学习的安全性，能够有效降低系统在实际应用中的风险，提升决策的可靠性和安全性。未来，该方法有望推动离线强化学习在更多高风险领域的应用。

## 📄 摘要（原文）

> Offline reinforcement learning (RL) heavily relies on the coverage of pre-collected data over the target policy's distribution. Existing studies aim to improve data-policy coverage to mitigate distributional shifts, but overlook security risks from insufficient coverage, and the single-step analysis is not consistent with the multi-step decision-making nature of offline RL. To address this, we introduce the sequence-level concentrability coefficient to quantify coverage, and reveal its exponential amplification on the upper bound of estimation errors through theoretical analysis. Building on this, we propose the Collapsing Sequence-Level Data-Policy Coverage (CSDPC) poisoning attack. Considering the continuous nature of offline RL data, we convert state-action pairs into decision units, and extract representative decision patterns that capture multi-step behavior. We identify rare patterns likely to cause insufficient coverage, and poison them to reduce coverage and exacerbate distributional shifts. Experiments show that poisoning just 1% of the dataset can degrade agent performance by 90%. This finding provides new perspectives for analyzing and safeguarding the security of offline RL.

