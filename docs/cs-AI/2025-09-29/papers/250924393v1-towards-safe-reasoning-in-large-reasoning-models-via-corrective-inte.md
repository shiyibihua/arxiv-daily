---
layout: default
title: Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention
---

# Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24393" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24393v1</a>
  <a href="https://arxiv.org/pdf/2509.24393.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24393v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24393v1', 'Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yichi Zhang, Yue Ding, Jingwen Yang, Tianwei Luo, Dongbai Li, Ranjie Duan, Qiang Liu, Hang Su, Yinpeng Dong, Jun Zhu

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**提出Intervened Preference Optimization以提升大型推理模型安全性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型推理模型` `安全性` `思维链` `过程监督` `偏好优化`

## 📋 核心要点

1. 现有大型推理模型在复杂推理过程中可能产生有害内容，即使最终结果看似安全，这带来了安全风险。
2. 论文提出Intervened Preference Optimization (IPO)方法，通过干预不安全推理步骤，引导模型生成更安全的推理过程。
3. 实验表明，IPO在jailbreak和对抗性安全基准测试中，显著降低了有害性，优于现有SFT和RL方法。

## 📝 摘要（中文）

大型推理模型(LRMs)在解决复杂问题方面取得了进展，但其思维链(CoT)推理常包含有害内容，即使最终回复看起来安全也可能持续存在。现有方法忽略了安全推理的独特重要性，损害了其可信度，并在恶意用户利用不安全推理时构成潜在风险。本文将重点转移到对齐推理本身的安全性，并探索过程监督作为解决方案。然而，简单地奖励安全推理是不够的，因为其rollout多样性低且训练信号有限。为此，我们深入研究了安全推理的特征，并揭示了几个关键见解：1)安全推理通常由几个关键的安全触发步骤巩固；2)合规线索与不安全的延续密切相关；3)纠正性干预可靠地引导不安全轨迹走向更安全的轨迹。受此启发，我们提出Intervened Preference Optimization (IPO)，一种通过用安全触发器替换合规步骤并构建具有强信号的偏好学习对来强制执行安全推理的对齐方法。在jailbreak和对抗性安全基准上的实验表明，IPO显著提高了推理和响应的整体安全性，优于基于SFT和基于RL的基线，有害性相对降低了30%以上，同时保持了在各种推理任务中的出色性能。结果突出了显式对齐推理的重要性，并为更安全的LRM提供了一条实用途径。

## 🔬 方法详解

**问题定义**：大型推理模型虽然在解决复杂问题上表现出色，但其推理过程（chain-of-thought, CoT）可能包含有害信息，即使最终输出是安全的。现有方法往往忽略了推理过程本身的安全，导致模型容易受到恶意攻击，产生不安全或有害的推理路径。因此，如何保证推理过程的安全性是一个亟待解决的问题。

**核心思路**：论文的核心思路是通过对不安全的推理过程进行干预，引导模型生成更安全的推理轨迹。具体来说，通过识别不安全推理步骤中的“合规线索”，并将其替换为“安全触发器”，从而改变推理方向，避免产生有害内容。这种干预策略旨在从根本上提升推理过程的安全性，而不仅仅是关注最终输出。

**技术框架**：Intervened Preference Optimization (IPO) 方法主要包含以下几个阶段：1) 分析安全推理的特征，识别安全触发器和合规线索；2) 在推理过程中，检测到合规线索时，用安全触发器进行替换，生成干预后的推理轨迹；3) 使用干预前后的推理轨迹构建偏好学习对，并利用偏好优化算法训练模型，使其倾向于生成更安全的推理过程。

**关键创新**：IPO 的关键创新在于其对推理过程的显式干预。与以往只关注最终输出安全性的方法不同，IPO 深入到推理的中间步骤，通过替换不安全线索来改变推理轨迹。这种方法能够更有效地控制推理过程，从而提高整体安全性。此外，IPO 还利用偏好学习，使得模型能够学习到安全推理的模式，并将其泛化到新的场景中。

**关键设计**：在 IPO 中，关键的设计包括：1) 安全触发器和合规线索的定义和识别方法；2) 干预策略的选择，例如如何选择合适的安全触发器来替换合规线索；3) 偏好学习对的构建方式，如何确保偏好信号的强度和准确性；4) 偏好优化算法的选择，例如使用 PPO 或其他合适的算法来训练模型。

## 📊 实验亮点

实验结果表明，IPO 方法在 jailbreak 和对抗性安全基准测试中，相对于基于 SFT 和基于 RL 的基线方法，有害性相对降低了 30% 以上。同时，IPO 还能保持模型在各种推理任务中的出色性能，表明该方法在提升安全性的同时，不会显著降低模型的通用能力。这些结果充分证明了 IPO 方法的有效性和实用性。

## 🎯 应用场景

该研究成果可应用于各种需要安全推理的大型语言模型应用场景，例如智能客服、内容生成、代码生成等。通过提升推理过程的安全性，可以有效防止模型生成有害、不准确或具有偏见的内容，从而提高用户体验和降低潜在风险。未来，该方法有望推广到更广泛的AI系统中，构建更安全、可靠的人工智能服务。

## 📄 摘要（原文）

> Although Large Reasoning Models (LRMs) have progressed in solving complex problems, their chain-of-thought (CoT) reasoning often contains harmful content that can persist even when the final responses appear safe. We show that this issue still remains in existing methods which overlook the unique significance of safe reasoning, undermining their trustworthiness and posing potential risks in applications if unsafe reasoning is accessible for and exploited by malicious users. We therefore shift our focus to aligning the safety of reasoning itself in this paper and explore process supervision as the solution. However, simply rewarding safe reasoning proves inadequate due to low rollout diversity and limited training signals. To tackle this challenge, we first delve into the characteristics of safe reasoning and uncover several critical insights that 1) safe reasoning is often consolidated by a few critical steps of safety triggers; 2) compliance cues strongly correlate with unsafe continuations; and 3) corrective interventions reliably steer unsafe trajectories towards safer traces. Motivated by these, we propose Intervened Preference Optimization (IPO), an alignment method that enforces safe reasoning by substituting compliance steps with safety triggers and constructing pairs for preference learning with strong signals. Experiments on jailbreak and adversarial safety benchmarks demonstrate that IPO remarkably improves overall safety regarding both reasoning and responses, outperforming SFT-based and RL-based baselines with a relative reduction of over 30% in harmfulness, while preserving excellent performance across diverse reasoning tasks. The results highlight the importance of explicit alignment for reasoning and provide a practical path to safer LRMs.

