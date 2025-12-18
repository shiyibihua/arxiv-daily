---
layout: default
title: Momentum-constrained Hybrid Heuristic Trajectory Optimization Framework with Residual-enhanced DRL for Visually Impaired Scenarios
---

# Momentum-constrained Hybrid Heuristic Trajectory Optimization Framework with Residual-enhanced DRL for Visually Impaired Scenarios

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15582" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15582v2</a>
  <a href="https://arxiv.org/pdf/2509.15582.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15582v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15582v2', 'Momentum-constrained Hybrid Heuristic Trajectory Optimization Framework with Residual-enhanced DRL for Visually Impaired Scenarios')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuting Zeng, Zhiwen Zheng, You Zhou, JiaLing Xiao, Yongbin Yu, Manping Fan, Bo Gong, Liyong Ren

**分类**: cs.RO, cs.AI

**发布日期**: 2025-09-19 (更新: 2025-12-05)

**备注**: Upon further internal evaluation, we found that the current version does not adequately represent the clarity and completeness that we intend for this work. To avoid possible misunderstanding caused by this preliminary form, we request withdrawal. A refined version will be prepared privately before any further dissemination

---

## 💡 一句话要点

**针对视障人士，提出动量约束混合启发式轨迹优化框架，结合残差增强DRL。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视障辅助导航` `轨迹优化` `深度强化学习` `启发式算法` `残差网络` `LSTM` `Frenet坐标系`

## 📋 核心要点

1. 现有方法在视障人士辅助导航中，难以兼顾轨迹的平滑性、安全性和实时性，面临复杂环境下的挑战。
2. 提出MHHTOF框架，结合启发式轨迹采样和残差增强DRL，实现轨迹生成、优化和评估的有效集成。
3. 实验表明，该框架显著提升了训练速度和稳定性，降低了成本和风险，验证了其在辅助导航中的有效性。

## 📝 摘要（中文）

本文提出了一种动量约束混合启发式轨迹优化框架(MHHTOF)，专为视障人士的辅助导航设计，集成了轨迹采样生成、优化和评估以及残差增强深度强化学习(DRL)。第一阶段，利用五阶多项式进行三阶插值，在Frenet坐标系中生成启发式轨迹采样簇(HTSC)，并采用动量约束轨迹优化(MTO)约束，以确保平滑性和可行性。在第一阶段的成本评估之后，第二阶段利用基于LSTM的时间特征建模的残差增强actor-critic网络，自适应地细化笛卡尔坐标系中的轨迹选择。具有权重转移的双阶段成本建模机制(DCMM)对齐了跨阶段的语义优先级，支持以人为本的优化。实验结果表明，所提出的LSTM-ResB-PPO实现了显著更快的收敛速度，在大约PPO基线所需训练迭代次数的一半内获得了稳定的策略性能，同时提高了奖励结果和训练稳定性。与基线方法相比，所选模型将平均成本和成本方差降低了30.3%和53.3%，并将自身和障碍物风险降低了77%以上。这些发现验证了该框架在复杂的辅助规划任务中增强鲁棒性、安全性和实时可行性的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决视障人士在复杂环境中进行辅助导航时，传统轨迹规划方法难以兼顾轨迹平滑性、安全性以及实时性的问题。现有方法通常难以在保证安全的前提下，快速生成可行的轨迹，并且难以适应动态变化的环境。

**核心思路**：论文的核心思路是将启发式轨迹采样与深度强化学习相结合，利用启发式方法快速生成候选轨迹，然后通过深度强化学习对轨迹进行优化和选择。通过这种混合方法，可以兼顾轨迹生成的效率和轨迹优化的质量，从而提高辅助导航系统的性能。

**技术框架**：MHHTOF框架包含两个主要阶段：第一阶段是启发式轨迹采样生成，在Frenet坐标系下，利用五阶多项式进行三阶插值，并施加动量约束，生成平滑且可行的轨迹簇。第二阶段是基于残差增强DRL的轨迹优化，利用LSTM-based的actor-critic网络，在笛卡尔坐标系下对轨迹进行精细调整。此外，还设计了双阶段成本建模机制(DCMM)，用于对齐两个阶段的语义优先级。

**关键创新**：论文的关键创新在于将启发式轨迹采样与残差增强深度强化学习相结合，并提出了双阶段成本建模机制。残差增强DRL能够更有效地学习轨迹优化策略，而双阶段成本建模机制则能够保证两个阶段的优化目标一致性。

**关键设计**：在第一阶段，使用五阶多项式进行三阶插值，保证轨迹的平滑性。动量约束用于限制轨迹的曲率变化。在第二阶段，使用LSTM-based的actor-critic网络，利用时间序列信息进行轨迹优化。残差连接用于加速训练过程。双阶段成本建模机制通过权重转移，将第一阶段的成本信息传递到第二阶段。

## 📊 实验亮点

实验结果表明，所提出的LSTM-ResB-PPO算法相比PPO基线，收敛速度提升约50%，在更少的训练迭代次数内达到稳定的策略性能。同时，该算法将平均成本和成本方差分别降低了30.3%和53.3%，并将自身和障碍物风险降低了77%以上，显著提升了轨迹规划的安全性。

## 🎯 应用场景

该研究成果可应用于视障人士辅助导航系统、智能轮椅、自动驾驶等领域。通过提供安全、平滑、实时的轨迹规划，可以显著提高视障人士的出行安全性和便利性，增强其独立生活能力。未来，该技术有望进一步推广到其他需要人机协作的机器人应用场景。

## 📄 摘要（原文）

> This paper proposes a momentum-constrained hybrid heuristic trajectory optimization framework (MHHTOF) tailored for assistive navigation in visually impaired scenarios, integrating trajectory sampling generation, optimization and evaluation with residual-enhanced deep reinforcement learning (DRL). In the first stage, heuristic trajectory sampling cluster (HTSC) is generated in the Frenet coordinate system using third-order interpolation with fifth-order polynomials and momentum-constrained trajectory optimization (MTO) constraints to ensure smoothness and feasibility. After first stage cost evaluation, the second stage leverages a residual-enhanced actor-critic network with LSTM-based temporal feature modeling to adaptively refine trajectory selection in the Cartesian coordinate system. A dual-stage cost modeling mechanism (DCMM) with weight transfer aligns semantic priorities across stages, supporting human-centered optimization. Experimental results demonstrate that the proposed LSTM-ResB-PPO achieves significantly faster convergence, attaining stable policy performance in approximately half the training iterations required by the PPO baseline, while simultaneously enhancing both reward outcomes and training stability. Compared to baseline method, the selected model reduces average cost and cost variance by 30.3% and 53.3%, and lowers ego and obstacle risks by over 77%. These findings validate the framework's effectiveness in enhancing robustness, safety, and real-time feasibility in complex assistive planning tasks.

