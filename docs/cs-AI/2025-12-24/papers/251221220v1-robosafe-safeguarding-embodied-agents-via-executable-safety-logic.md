---
layout: default
title: "RoboSafe: Safeguarding Embodied Agents via Executable Safety Logic"
---

# RoboSafe: Safeguarding Embodied Agents via Executable Safety Logic

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21220" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21220v1</a>
  <a href="https://arxiv.org/pdf/2512.21220.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21220v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21220v1', 'RoboSafe: Safeguarding Embodied Agents via Executable Safety Logic')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Le Wang, Zonghao Ying, Xiao Yang, Quanchen Zou, Zhenfei Yin, Tianlin Li, Jian Yang, Yaodong Yang, Aishan Liu, Xianglong Liu

**分类**: cs.AI, cs.CV, cs.RO

**发布日期**: 2025-12-24

**备注**: 11 pages, 6 figures

---

## 💡 一句话要点

**RoboSafe：通过可执行安全逻辑保障具身智能体的安全**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能体` `安全保障` `运行时安全` `混合推理` `可执行逻辑` `安全谓词` `风险预测`

## 📋 核心要点

1. 现有具身智能体的安全防护依赖静态规则或提示控制，难以应对动态环境中隐式风险。
2. RoboSafe提出混合推理运行时安全保障，通过可执行的谓词安全逻辑，实现自适应安全。
3. 实验表明，RoboSafe显著降低了危险行为发生率，同时保持了任务性能，并在真实机械臂上验证了实用性。

## 📝 摘要（中文）

具身智能体在视觉-语言模型（VLM）驱动下，执行复杂现实世界任务的能力日益增强，但它们仍然容易受到可能触发不安全行为的危险指令的影响。运行时安全防护栏因其灵活性而提供了一种有前景的解决方案，可以在任务执行期间拦截危险动作。然而，现有的防御措施通常依赖于静态规则过滤器或提示级别的控制，难以解决动态、时间依赖和上下文丰富的环境中出现的隐式风险。为了解决这个问题，我们提出了RoboSafe，一种混合推理运行时安全保障，通过可执行的基于谓词的安全逻辑来保护具身智能体。RoboSafe在混合长短期安全记忆上集成了两种互补的推理过程。我们首先提出了一个后向反射推理模块，该模块不断回顾短期记忆中的近期轨迹，以推断时间安全谓词，并在检测到违规时主动触发重新规划。然后，我们提出了一个前向预测推理模块，该模块通过从长期安全记忆和智能体的多模态观察中生成上下文感知的安全谓词来预测即将到来的风险。这些组件共同构成了一种自适应的、可验证的安全逻辑，既可解释又可作为代码执行。跨多个智能体的大量实验表明，与领先的基线相比，RoboSafe显著减少了危险行为（风险发生率降低36.8%），同时保持了接近原始的任务性能。在物理机械臂上的真实世界评估进一步证实了它的实用性。代码将在接收后发布。

## 🔬 方法详解

**问题定义**：论文旨在解决具身智能体在执行任务时，由于环境的动态性和指令的复杂性，容易出现不安全行为的问题。现有方法，如静态规则过滤和提示级别控制，无法有效应对时间依赖和上下文相关的隐式风险，导致智能体可能做出危险动作。

**核心思路**：RoboSafe的核心思路是构建一个混合推理的运行时安全保障系统，通过结合后向反射推理和前向预测推理，对智能体的行为进行动态的安全评估和干预。这种混合推理方式能够同时考虑历史轨迹和未来风险，从而更全面地保障智能体的安全。

**技术框架**：RoboSafe的整体架构包含以下几个主要模块：1) 混合长短期安全记忆：用于存储智能体的历史轨迹和安全知识。2) 后向反射推理模块：回顾短期记忆中的近期轨迹，推断时间安全谓词，并在检测到违规时触发重新规划。3) 前向预测推理模块：从长期安全记忆和智能体的多模态观察中生成上下文感知的安全谓词，预测即将到来的风险。4) 可执行安全逻辑：将安全谓词转化为可执行的代码，用于实时监控和干预智能体的行为。

**关键创新**：RoboSafe的关键创新在于其混合推理机制和可执行安全逻辑。传统的安全保障方法通常依赖于静态规则或提示工程，而RoboSafe能够根据环境和任务的动态变化，自适应地调整安全策略。可执行安全逻辑使得安全规则更加透明和可验证，方便开发者进行调试和优化。

**关键设计**：RoboSafe的关键设计包括：1) 混合长短期安全记忆的结构和更新策略，用于有效存储和检索相关信息。2) 后向反射推理模块中，时间安全谓词的定义和推理方法，用于检测历史轨迹中的安全违规。3) 前向预测推理模块中，上下文感知安全谓词的生成方法，以及如何利用多模态观察进行风险预测。4) 可执行安全逻辑的实现方式，以及如何将其与智能体的控制系统进行集成。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21220v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21220v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21220v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，RoboSafe在多个智能体上显著降低了危险行为的发生率，风险发生率降低了36.8%，优于现有的基线方法。同时，RoboSafe保持了接近原始的任务性能，表明其安全保障措施不会对智能体的效率产生显著影响。在真实机械臂上的实验进一步验证了RoboSafe的实用性和有效性。

## 🎯 应用场景

RoboSafe可应用于各种需要安全保障的具身智能体场景，如家庭服务机器人、工业机器人、自动驾驶车辆等。通过减少危险行为的发生，RoboSafe能够提高智能体的可靠性和安全性，降低事故风险，从而促进具身智能体在现实世界中的广泛应用。

## 📄 摘要（原文）

> Embodied agents powered by vision-language models (VLMs) are increasingly capable of executing complex real-world tasks, yet they remain vulnerable to hazardous instructions that may trigger unsafe behaviors. Runtime safety guardrails, which intercept hazardous actions during task execution, offer a promising solution due to their flexibility. However, existing defenses often rely on static rule filters or prompt-level control, which struggle to address implicit risks arising in dynamic, temporally dependent, and context-rich environments. To address this, we propose RoboSafe, a hybrid reasoning runtime safeguard for embodied agents through executable predicate-based safety logic. RoboSafe integrates two complementary reasoning processes on a Hybrid Long-Short Safety Memory. We first propose a Backward Reflective Reasoning module that continuously revisits recent trajectories in short-term memory to infer temporal safety predicates and proactively triggers replanning when violations are detected. We then propose a Forward Predictive Reasoning module that anticipates upcoming risks by generating context-aware safety predicates from the long-term safety memory and the agent's multimodal observations. Together, these components form an adaptive, verifiable safety logic that is both interpretable and executable as code. Extensive experiments across multiple agents demonstrate that RoboSafe substantially reduces hazardous actions (-36.8% risk occurrence) compared with leading baselines, while maintaining near-original task performance. Real-world evaluations on physical robotic arms further confirm its practicality. Code will be released upon acceptance.

