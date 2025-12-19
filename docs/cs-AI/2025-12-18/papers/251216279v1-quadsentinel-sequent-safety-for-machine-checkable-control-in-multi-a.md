---
layout: default
title: QuadSentinel: Sequent Safety for Machine-Checkable Control in Multi-agent Systems
---

# QuadSentinel: Sequent Safety for Machine-Checkable Control in Multi-agent Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16279" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16279v1</a>
  <a href="https://arxiv.org/pdf/2512.16279.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16279v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16279v1', 'QuadSentinel: Sequent Safety for Machine-Checkable Control in Multi-agent Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiliu Yang, Yilei Jiang, Qunzhong Wang, Yingshui Tan, Xiaoyong Zhu, Sherman S. M. Chow, Bo Zheng, Xiangyu Yue

**分类**: cs.AI, cs.CL

**发布日期**: 2025-12-18

**备注**: Preprint

**🔗 代码/项目**: [GITHUB](https://github.com/yyiliu/QuadSentinel)

---

## 💡 一句话要点

**QuadSentinel：多智能体系统中基于时序推理和可机检规则的安全控制**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `安全控制` `可机检规则` `时序逻辑` `智能体架构`

## 📋 核心要点

1. 现有基于自然语言的安全策略难以转化为可机检规则，导致多智能体系统运行时安全控制不可靠。
2. 提出QuadSentinel，采用四智能体架构，将安全策略编译为基于可观察状态谓词的可机检规则，并在线执行。
3. 实验表明，QuadSentinel提高了护栏精度和规则召回率，减少了误报，并优于单智能体基线。

## 📝 摘要（中文）

基于大型语言模型的智能体在解决复杂任务时，涉及工具使用、多步计划和智能体间消息传递，由此产生安全风险。然而，部署者编写的自然语言策略具有模糊性和上下文依赖性，难以映射到可机检规则，且运行时强制执行不可靠。本文提出	extsc{QuadSentinel}，一种四智能体守卫（状态跟踪器、策略验证器、威胁观察器和裁判）系统，将安全策略表示为时序逻辑，并将其编译为基于可观察状态谓词的可机检规则，并在线执行。裁判逻辑和高效的top-$k$谓词更新器通过优先检查和分层解决冲突来降低成本。在ST-WebAgentBench和AgentHarm上的实验表明，	extsc{QuadSentinel}提高了护栏精度和规则召回率，同时减少了误报。与ShieldAgent等单智能体基线相比，它产生了更好的整体安全控制。无需修改核心智能体，通过保持策略分离和可机检性，近期部署即可采用此模式。代码将在https://github.com/yyiliu/QuadSentinel公开。

## 🔬 方法详解

**问题定义**：多智能体系统在执行复杂任务时，由于智能体间的交互和工具的使用，容易出现安全风险。现有的安全策略通常以自然语言形式表达，存在模糊性和上下文依赖性，难以转化为机器可执行的规则，导致运行时安全控制效果不佳。此外，单智能体安全控制方法难以有效应对多智能体环境下的复杂交互。

**核心思路**：将安全策略表示为时序逻辑（sequents），并将其编译为基于可观察状态谓词的可机检规则。通过引入四智能体守卫架构，实现对多智能体系统运行时的安全监控和控制。核心在于将模糊的自然语言策略转化为精确的、可验证的机器规则，并利用多智能体协同来增强安全控制的鲁棒性和准确性。

**技术框架**：QuadSentinel采用四智能体架构，包括：1) 状态跟踪器（State Tracker）：负责跟踪和记录多智能体系统的状态信息。2) 策略验证器（Policy Verifier）：将安全策略编译为可机检规则，并验证当前状态是否违反策略。3) 威胁观察器（Threat Watcher）：监控潜在的威胁行为，并发出警报。4) 裁判（Referee）：根据策略验证器和威胁观察器的结果，做出最终的安全决策，并采取相应的控制措施。整体流程是状态跟踪器提供状态信息，策略验证器和威胁观察器进行评估，裁判根据评估结果执行安全策略。

**关键创新**：主要创新点在于将自然语言安全策略转化为可机检的时序逻辑规则，并利用四智能体架构实现对多智能体系统的在线安全控制。与传统的单智能体安全控制方法相比，QuadSentinel能够更好地应对多智能体环境下的复杂交互和潜在威胁。此外，裁判逻辑和高效的top-$k$谓词更新器能够有效降低计算成本，提高系统的实时性。

**关键设计**：裁判逻辑采用分层冲突解决机制，优先处理高优先级规则，避免冲突决策。Top-$k$谓词更新器用于选择最相关的状态谓词进行验证，降低计算复杂度。具体的参数设置和损失函数信息未知，论文可能未详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16279v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16279v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16279v1/imgs/harmful_by_category.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，QuadSentinel在ST-WebAgentBench和AgentHarm数据集上，提高了护栏精度和规则召回率，同时减少了误报。与ShieldAgent等单智能体基线相比，QuadSentinel在整体安全控制方面表现更优，证明了其在多智能体安全控制方面的有效性。

## 🎯 应用场景

QuadSentinel可应用于各种多智能体系统，例如：自动驾驶、机器人协作、智能家居、金融交易等。通过提供可信赖的安全保障，能够促进多智能体技术在实际场景中的应用，并降低潜在的安全风险。该研究有助于构建更安全、可靠的人工智能系统。

## 📄 摘要（原文）

> Safety risks arise as large language model-based agents solve complex tasks with tools, multi-step plans, and inter-agent messages. However, deployer-written policies in natural language are ambiguous and context dependent, so they map poorly to machine-checkable rules, and runtime enforcement is unreliable. Expressing safety policies as sequents, we propose \textsc{QuadSentinel}, a four-agent guard (state tracker, policy verifier, threat watcher, and referee) that compiles these policies into machine-checkable rules built from predicates over observable state and enforces them online. Referee logic plus an efficient top-$k$ predicate updater keeps costs low by prioritizing checks and resolving conflicts hierarchically. Measured on ST-WebAgentBench (ICML CUA~'25) and AgentHarm (ICLR~'25), \textsc{QuadSentinel} improves guardrail accuracy and rule recall while reducing false positives. Against single-agent baselines such as ShieldAgent (ICML~'25), it yields better overall safety control. Near-term deployments can adopt this pattern without modifying core agents by keeping policies separate and machine-checkable. Our code will be made publicly available at https://github.com/yyiliu/QuadSentinel.

