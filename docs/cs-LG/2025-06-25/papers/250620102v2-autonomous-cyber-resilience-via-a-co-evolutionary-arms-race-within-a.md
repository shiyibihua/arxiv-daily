---
layout: default
title: Autonomous Cyber Resilience via a Co-Evolutionary Arms Race within a Fortified Digital Twin Sandbox
---

# Autonomous Cyber Resilience via a Co-Evolutionary Arms Race within a Fortified Digital Twin Sandbox

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20102" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20102v2</a>
  <a href="https://arxiv.org/pdf/2506.20102.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20102v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20102v2', 'Autonomous Cyber Resilience via a Co-Evolutionary Arms Race within a Fortified Digital Twin Sandbox')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Malikussaid, Sutiyo

**分类**: cs.CR, cs.LG, eess.SY

**发布日期**: 2025-06-25 (更新: 2025-10-16)

**备注**: 6 pages, 2 figures, 4 equations, 1 algorithm, 3 tables, to be published in ISPACS 2025, unabridged version exists as arXiv:2506.20102v1

---

## 💡 一句话要点

**提出对抗性韧性共演框架以解决工业控制系统安全问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `对抗性韧性` `数字双胞胎` `深度强化学习` `工业控制系统` `安全防御` `动态自我改进` `可解释人工智能` `联邦学习`

## 📋 核心要点

1. 现有工业控制系统面临智能对手的威胁，静态防御措施已无法有效应对新型攻击。
2. 提出对抗性韧性共演框架（ARC），通过红方和蓝方代理的共演机制提升系统的安全性和韧性。
3. 在田纳西东曼过程和安全水处理测试床上，F1分数提升至0.89，检测延迟减少至210秒，表现出显著的性能改进。

## 📝 摘要（中文）

信息技术与操作技术的融合使工业控制系统面临智能对手的威胁，传统静态防御已不再有效。本文提出了对抗性韧性共演（ARC）框架，旨在解决模型可信度、数据完整性和分析韧性三者之间的信任问题。ARC在强化安全的数字双胞胎环境中建立了共演的军备竞赛，其中深度强化学习的“红方代理”自主发现攻击路径，而基于集成的“蓝方代理”则不断增强防御能力。通过在田纳西东曼过程和安全水处理测试床上的实验验证，检测新型攻击的性能显著提升，F1分数从0.65提高至0.89，检测延迟从1200秒以上减少至210秒。综合消融研究表明，共演过程本身贡献了27%的性能提升。通过整合可解释人工智能并提出联邦ARC架构，本文为关键基础设施的动态自我改进安全提供了必要的范式转变。

## 🔬 方法详解

**问题定义**：本文旨在解决工业控制系统在面对智能对手时的安全性问题，现有方法多依赖静态防御，无法适应快速变化的攻击策略。

**核心思路**：通过建立对抗性韧性共演框架（ARC），实现红方代理与蓝方代理的动态共演，增强系统的自适应能力和防御能力。

**技术框架**：ARC框架包含两个主要模块：红方代理使用深度强化学习自主发现攻击路径，蓝方代理则通过集成方法不断强化防御，形成共演的军备竞赛。

**关键创新**：最重要的创新在于引入了共演机制，使得攻击与防御在动态环境中相互促进，显著提升了系统的韧性和响应速度。

**关键设计**：在红方代理中，采用深度强化学习算法进行路径发现；蓝方代理则使用集成学习方法增强防御能力，实验中通过消融研究验证了共演过程对性能的贡献。

## 📊 实验亮点

实验结果显示，ARC框架在检测新型攻击方面表现优异，F1分数从0.65提升至0.89，检测延迟显著减少至210秒，较之前的1200秒大幅提升，证明了该方法的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括工业控制系统、智能制造和基础设施安全等。通过动态自我改进的安全机制，ARC框架能够有效提升关键基础设施的防御能力，降低潜在的安全风险，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The convergence of Information Technology and Operational Technology has exposed Industrial Control Systems to adaptive, intelligent adversaries that render static defenses obsolete. This paper introduces the Adversarial Resilience Co-evolution (ARC) framework, addressing the "Trinity of Trust" comprising model fidelity, data integrity, and analytical resilience. ARC establishes a co-evolutionary arms race within a Fortified Secure Digital Twin (F-SCDT), where a Deep Reinforcement Learning "Red Agent" autonomously discovers attack paths while an ensemble-based "Blue Agent" is continuously hardened against these threats. Experimental validation on the Tennessee Eastman Process (TEP) and Secure Water Treatment (SWaT) testbeds demonstrates superior performance in detecting novel attacks, with F1-scores improving from 0.65 to 0.89 and detection latency reduced from over 1200 seconds to 210 seconds. A comprehensive ablation study reveals that the co-evolutionary process itself contributes a 27% performance improvement. By integrating Explainable AI and proposing a Federated ARC architecture, this work presents a necessary paradigm shift toward dynamic, self-improving security for critical infrastructure.

