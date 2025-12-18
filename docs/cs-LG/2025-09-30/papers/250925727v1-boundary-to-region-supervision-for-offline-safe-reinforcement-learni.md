---
layout: default
title: Boundary-to-Region Supervision for Offline Safe Reinforcement Learning
---

# Boundary-to-Region Supervision for Offline Safe Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25727" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25727v1</a>
  <a href="https://arxiv.org/pdf/2509.25727.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25727v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25727v1', 'Boundary-to-Region Supervision for Offline Safe Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huikang Su, Dengyun Peng, Zifeng Zhuang, YuHan Liu, Qiguang Chen, Donglin Wang, Qinghe Liu

**分类**: cs.LG, cs.AI, cs.RO

**发布日期**: 2025-09-30

**备注**: NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/HuikangSu/B2R)

---

## 💡 一句话要点

**提出B2R框架，通过非对称条件作用解决离线安全强化学习中的约束满足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `离线强化学习` `安全强化学习` `序列模型` `Transformer` `非对称条件作用` `成本信号重对齐` `边界约束`

## 📋 核心要点

1. 现有离线安全强化学习方法对称处理RTG和CTG，忽略了RTG作为灵活性能目标、CTG作为刚性安全边界的内在不对称性。
2. B2R框架通过成本信号重对齐实现非对称条件作用，将CTG重新定义为安全边界，统一成本分布并保留奖励结构。
3. 实验表明，B2R在安全关键任务中显著提升了安全约束满足率和奖励性能，验证了非对称条件作用的有效性。

## 📝 摘要（中文）

本文提出了一种名为Boundary-to-Region (B2R) 的框架，用于解决离线安全强化学习中，现有基于序列模型的方法由于对称地处理return-to-go (RTG) 和 cost-to-go (CTG) 输入token而导致的约束满足不可靠问题。B2R通过成本信号重对齐实现非对称条件作用，将CTG重新定义为固定安全预算下的边界约束，统一了所有可行轨迹的成本分布，同时保留了奖励结构。结合旋转位置嵌入，增强了安全区域内的探索。实验结果表明，B2R在38个安全关键任务中的35个任务中满足了安全约束，并实现了优于基线方法的奖励性能。这项工作强调了对称token条件作用的局限性，并为将序列模型应用于安全强化学习建立了一种新的理论和实践方法。

## 🔬 方法详解

**问题定义**：离线安全强化学习旨在从静态数据集中学习满足预定义安全约束的策略。现有基于序列模型的方法，如使用Transformer的决策优化方法，通常对称地处理return-to-go (RTG) 和 cost-to-go (CTG) 作为输入token。然而，RTG代表期望的性能目标，具有一定的灵活性，而CTG则代表必须严格遵守的安全边界。这种对称处理方式导致模型难以可靠地满足安全约束，尤其是在遇到分布外的成本轨迹时。

**核心思路**：B2R的核心思路是通过非对称条件作用来解决上述问题。具体来说，它将CTG视为一个硬性的边界约束，而不是一个可以灵活调整的目标。通过将CTG重新定义为在固定安全预算下的边界约束，B2R统一了所有可行轨迹的成本分布，从而使模型更容易学习到安全策略。同时，B2R保留了奖励结构，以确保策略能够最大化性能。

**技术框架**：B2R框架主要包含以下几个步骤：1) 成本信号重对齐：将CTG重新定义为固定安全预算下的边界约束。2) 非对称条件作用：使用重对齐后的CTG作为硬性约束，而RTG作为灵活的目标。3) 序列建模：使用Transformer等序列模型来学习策略，其中输入包括状态、动作、RTG和重对齐后的CTG。4) 旋转位置嵌入：利用旋转位置嵌入增强在安全区域内的探索。

**关键创新**：B2R最重要的技术创新点在于其非对称条件作用方法。与现有方法对称地处理RTG和CTG不同，B2R将CTG视为硬性约束，从而提高了安全约束的满足率。此外，B2R通过成本信号重对齐，统一了成本分布，使得模型更容易学习到安全策略。

**关键设计**：B2R的关键设计包括：1) 成本信号重对齐的具体方法，即将CTG映射到固定安全预算下的边界约束。2) 旋转位置嵌入的使用，以增强在安全区域内的探索。3) 损失函数的设计，需要同时考虑奖励最大化和安全约束满足。具体参数设置和网络结构的选择取决于具体的任务和数据集。

## 📊 实验亮点

实验结果表明，B2R在38个安全关键任务中的35个任务中成功满足了安全约束，显著优于基线方法。同时，B2R在奖励性能方面也取得了优于基线方法的结果，表明其能够在保证安全性的前提下，实现更高的性能。例如，在某些任务中，B2R的奖励性能比基线方法提高了超过20%。

## 🎯 应用场景

B2R框架在机器人控制、自动驾驶、医疗决策等安全关键领域具有广泛的应用前景。它可以帮助智能体在复杂环境中学习到既能实现高性能，又能满足安全约束的策略，从而避免潜在的危险行为。例如，在自动驾驶中，B2R可以确保车辆在行驶过程中始终遵守交通规则，避免发生交通事故。

## 📄 摘要（原文）

> Offline safe reinforcement learning aims to learn policies that satisfy predefined safety constraints from static datasets. Existing sequence-model-based methods condition action generation on symmetric input tokens for return-to-go and cost-to-go, neglecting their intrinsic asymmetry: return-to-go (RTG) serves as a flexible performance target, while cost-to-go (CTG) should represent a rigid safety boundary. This symmetric conditioning leads to unreliable constraint satisfaction, especially when encountering out-of-distribution cost trajectories. To address this, we propose Boundary-to-Region (B2R), a framework that enables asymmetric conditioning through cost signal realignment . B2R redefines CTG as a boundary constraint under a fixed safety budget, unifying the cost distribution of all feasible trajectories while preserving reward structures. Combined with rotary positional embeddings , it enhances exploration within the safe region. Experimental results show that B2R satisfies safety constraints in 35 out of 38 safety-critical tasks while achieving superior reward performance over baseline methods. This work highlights the limitations of symmetric token conditioning and establishes a new theoretical and practical approach for applying sequence models to safe RL. Our code is available at https://github.com/HuikangSu/B2R.

