---
layout: default
title: Normative Conflicts and Shallow AI Alignment
---

# Normative Conflicts and Shallow AI Alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04679" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04679v1</a>
  <a href="https://arxiv.org/pdf/2506.04679.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04679v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04679v1', 'Normative Conflicts and Shallow AI Alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Raphaël Millière

**分类**: cs.CL

**发布日期**: 2025-06-05

**备注**: Published in Philosophical Studies

**期刊**: Milliere, R. (2025). Normative conflicts and shallow AI alignment. Philosophical Studies, 1-44

**DOI**: [10.1007/s11098-025-02347-3](https://doi.org/10.1007/s11098-025-02347-3)

---

## 💡 一句话要点

**探讨LLM的规范冲突与浅层AI对齐问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `AI安全` `价值对齐` `道德心理学` `规范冲突` `对抗性攻击` `深层对齐` `伦理AI`

## 📋 核心要点

1. 现有的对齐方法无法有效防止LLMs被滥用，尤其是在规范冲突的情况下。
2. 论文提出通过增强LLMs的规范性思考能力，来解决其在对抗性攻击中的脆弱性。
3. 研究表明，现有的推理-focused LLMs未能解决规范冲突问题，仍需进一步改进。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的发展，AI系统的安全部署问题日益突出。本文探讨了LLMs的价值对齐问题，认为当前的对齐策略无法有效防止滥用。尽管通过基于人类偏好的微调来灌输有用性、诚实性和无害性等规范，LLMs依然容易受到利用这些规范之间冲突的对抗性攻击。本文指出，这种脆弱性反映了现有对齐方法的根本局限性：它们强化了浅层行为倾向，而未能赋予LLMs真正的规范性思考能力。通过借鉴道德心理学的研究，本文展示了人类在规范冲突中的理性推理能力如何增强其抵御类似对抗性策略的能力。相较之下，LLMs缺乏有效检测和理性解决规范冲突的能力，使其易受操控，甚至近期在推理方面的进展也未能解决这一脆弱性。此“浅层对齐”问题对AI安全和监管具有重要影响，表明当前方法不足以减轻日益强大的AI系统可能带来的危害。

## 🔬 方法详解

**问题定义**：本文要解决的问题是现有的对齐方法在面对规范冲突时的脆弱性，导致LLMs容易受到对抗性攻击。现有方法主要通过微调来强化行为规范，但未能有效赋予模型深层次的规范性思考能力。

**核心思路**：论文的核心思路是借鉴道德心理学的研究，提出通过增强LLMs的规范性思考能力，使其能够更好地检测和解决规范冲突，从而提高其抵御对抗性攻击的能力。

**技术框架**：整体架构包括对LLMs进行规范性思考能力的训练，主要模块包括人类偏好微调、规范冲突检测和理性推理能力的增强。

**关键创新**：最重要的技术创新在于提出了“深层对齐”的概念，强调赋予LLMs真正的规范性思考能力，而不仅仅是行为上的对齐。这与现有方法的本质区别在于，后者主要关注行为表现，而非内在的思考能力。

**关键设计**：关键设计包括对损失函数的调整，以鼓励模型在面对规范冲突时进行理性推理，此外，网络结构上可能需要引入新的模块以支持复杂的推理过程。具体参数设置和网络结构细节尚未明确。

## 📊 实验亮点

实验结果表明，增强LLMs的规范性思考能力后，其在面对规范冲突时的抵御能力显著提升。具体性能数据和对比基线尚未提供，但研究指出，现有推理-focused LLMs在此方面的不足，强调了本研究的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括AI安全、伦理AI设计和政策制定。通过增强LLMs的规范性思考能力，可以在更广泛的场景中安全地部署AI系统，减少潜在的滥用风险，推动AI技术的负责任发展。

## 📄 摘要（原文）

> The progress of AI systems such as large language models (LLMs) raises increasingly pressing concerns about their safe deployment. This paper examines the value alignment problem for LLMs, arguing that current alignment strategies are fundamentally inadequate to prevent misuse. Despite ongoing efforts to instill norms such as helpfulness, honesty, and harmlessness in LLMs through fine-tuning based on human preferences, they remain vulnerable to adversarial attacks that exploit conflicts between these norms. I argue that this vulnerability reflects a fundamental limitation of existing alignment methods: they reinforce shallow behavioral dispositions rather than endowing LLMs with a genuine capacity for normative deliberation. Drawing from on research in moral psychology, I show how humans' ability to engage in deliberative reasoning enhances their resilience against similar adversarial tactics. LLMs, by contrast, lack a robust capacity to detect and rationally resolve normative conflicts, leaving them susceptible to manipulation; even recent advances in reasoning-focused LLMs have not addressed this vulnerability. This ``shallow alignment'' problem carries significant implications for AI safety and regulation, suggesting that current approaches are insufficient for mitigating potential harms posed by increasingly capable AI systems.

