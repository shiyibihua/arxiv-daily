---
layout: default
title: World Model for AI Autonomous Navigation in Mechanical Thrombectomy
---

# World Model for AI Autonomous Navigation in Mechanical Thrombectomy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25518" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25518v2</a>
  <a href="https://arxiv.org/pdf/2509.25518.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25518v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25518v2', 'World Model for AI Autonomous Navigation in Mechanical Thrombectomy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Harry Robertshaw, Han-Ru Wu, Alejandro Granados, Thomas C Booth

**分类**: cs.LG, cs.RO, eess.IV

**发布日期**: 2025-09-29 (更新: 2025-10-02)

**备注**: Published in Medical Image Computing and Computer Assisted Intervention - MICCAI 2025, Lecture Notes in Computer Science, vol 15968

**期刊**: MICCAI 2025. Lecture Notes in Computer Science, vol 15968 (2026)

**DOI**: [10.1007/978-3-032-05114-1_65](https://doi.org/10.1007/978-3-032-05114-1_65)

---

## 💡 一句话要点

**提出基于世界模型的TD-MPC2算法，提升机械取栓术中AI自主导航性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机械取栓术` `自主导航` `强化学习` `世界模型` `TD-MPC2` `机器人辅助` `血管内导航`

## 📋 核心要点

1. 现有基于强化学习的血管内导航方法难以在不同患者血管结构和长时程任务中泛化。
2. 论文提出使用基于世界模型的TD-MPC2算法，通过学习环境模型来提升导航策略的泛化能力。
3. 实验结果表明，TD-MPC2在多任务学习中显著优于SAC，成功率从37%提升到65%。

## 📝 摘要（中文）

机械取栓术（MT）的自主导航面临血管解剖复杂和实时决策精度要求高的挑战。基于强化学习（RL）的方法在自动化血管内导航方面显示出潜力，但现有方法在跨患者血管的泛化和长时程任务中表现不佳。本文提出了一种基于世界模型的自主血管内导航方法，使用TD-MPC2（一种基于模型的RL算法）。在十个真实患者血管的多个血管内导航任务中训练单个RL智能体，并与最先进的Soft Actor-Critic（SAC）方法进行比较。结果表明，TD-MPC2在多任务学习中显著优于SAC，平均成功率达到65%，而SAC为37%，路径比率也有显著提高。TD-MPC2的程序时间有所增加，表明成功率和执行速度之间存在权衡。这些发现突出了世界模型在改善自主血管内导航方面的潜力，并为未来AI驱动的机器人干预的泛化研究奠定了基础。

## 🔬 方法详解

**问题定义**：机械取栓术中的自主导航需要精确控制导管在复杂血管结构中移动，现有强化学习方法难以泛化到不同患者的血管结构，并且在长时程任务中容易出现误差累积，导致导航失败。因此，需要一种能够学习血管环境模型，并在此基础上进行规划的导航方法。

**核心思路**：论文的核心思路是利用世界模型来学习血管环境的动态特性，并使用TD-MPC2算法在学习到的世界模型中进行规划，从而提高导航策略的泛化能力和鲁棒性。世界模型能够预测未来状态，使得智能体能够提前评估不同动作序列的潜在结果，从而做出更明智的决策。

**技术框架**：整体框架包括三个主要模块：环境交互模块、世界模型学习模块和策略优化模块。环境交互模块负责与血管环境进行交互，收集数据。世界模型学习模块利用收集到的数据学习血管环境的动态模型。策略优化模块使用TD-MPC2算法，在学习到的世界模型中进行规划，优化导航策略。TD-MPC2算法是一种基于模型的强化学习算法，它结合了时序差分学习和模型预测控制的优点。

**关键创新**：最重要的技术创新点在于将世界模型引入到机械取栓术的自主导航中，并使用TD-MPC2算法进行策略优化。与传统的基于模型的强化学习方法相比，TD-MPC2算法能够更有效地利用学习到的世界模型进行规划，从而提高导航策略的性能。此外，该方法在多个真实患者血管数据上进行了训练和测试，验证了其泛化能力。

**关键设计**：世界模型采用循环神经网络（RNN）结构，用于预测血管环境的未来状态。TD-MPC2算法使用交叉熵方法进行规划，选择最优的动作序列。损失函数包括状态预测误差和奖励函数。实验中，对TD-MPC2和SAC算法的关键参数进行了调整，以获得最佳性能。

## 📊 实验亮点

实验结果表明，TD-MPC2在多任务学习中显著优于SAC，平均成功率达到65%，而SAC为37%。TD-MPC2在路径比率方面也有显著提升，表明其导航路径更加高效。虽然TD-MPC2的程序时间有所增加，但成功率的显著提升表明其在复杂血管环境中的导航能力更强。

## 🎯 应用场景

该研究成果可应用于机械取栓术等微创手术的机器人辅助导航，提高手术的精准性和效率，降低手术风险。未来，该技术有望推广到其他需要精确导航的医疗场景，例如药物递送、活检等，实现更智能化的医疗干预。

## 📄 摘要（原文）

> Autonomous navigation for mechanical thrombectomy (MT) remains a critical challenge due to the complexity of vascular anatomy and the need for precise, real-time decision-making. Reinforcement learning (RL)-based approaches have demonstrated potential in automating endovascular navigation, but current methods often struggle with generalization across multiple patient vasculatures and long-horizon tasks. We propose a world model for autonomous endovascular navigation using TD-MPC2, a model-based RL algorithm. We trained a single RL agent across multiple endovascular navigation tasks in ten real patient vasculatures, comparing performance against the state-of-the-art Soft Actor-Critic (SAC) method. Results indicate that TD-MPC2 significantly outperforms SAC in multi-task learning, achieving a 65% mean success rate compared to SAC's 37%, with notable improvements in path ratio. TD-MPC2 exhibited increased procedure times, suggesting a trade-off between success rate and execution speed. These findings highlight the potential of world models for improving autonomous endovascular navigation and lay the foundation for future research in generalizable AI-driven robotic interventions.

