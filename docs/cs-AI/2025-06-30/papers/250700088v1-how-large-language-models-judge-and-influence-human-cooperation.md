---
layout: default
title: How large language models judge and influence human cooperation
---

# How large language models judge and influence human cooperation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00088" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00088v1</a>
  <a href="https://arxiv.org/pdf/2507.00088.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00088v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00088v1', 'How large language models judge and influence human cooperation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alexandre S. Pires, Laurens Samson, Sennay Ghebreab, Fernando P. Santos

**分类**: physics.soc-ph, cs.AI, cs.SI

**发布日期**: 2025-06-30

---

## 💡 一句话要点

**评估大型语言模型对人类合作的影响与判断**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `人类合作` `社会决策` `道德判断` `进化博弈` `合作动态` `声誉影响`

## 📋 核心要点

1. 当前对大型语言模型在社会决策中的长期影响尚不明确，尤其是如何影响人类合作行为。
2. 本文通过提供多种社交情境示例，评估LLMs对合作行为的判断，并结合进化博弈理论分析合作动态。
3. 研究发现，LLMs在评估良好对手时表现出一致性，但在声誉不佳的个体上存在显著差异，这可能影响合作的普遍性。

## 📝 摘要（中文）

人类日益依赖大型语言模型（LLMs）在社会情境中支持决策。先前研究表明，这些工具会影响人们的道德和政治判断。然而，基于LLM的社会决策的长期影响仍然未知。本文评估了最先进的LLMs如何判断合作行为，提供了21种不同的LLMs与一系列合作与拒绝合作的社交情境示例，并探讨了这些判断对人类合作的长期影响。研究发现，在评估与良好对手的合作时，模型之间的判断一致性显著，但在与声誉不佳的个体合作时，模型之间存在较大差异。最后，通过目标导向的提示，研究展示了如何引导LLM的判断，以维护人类合作。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型如何影响人类合作判断的问题。现有研究未能充分探讨LLM在社会决策中的长期影响，尤其是对人类合作的潜在影响。

**核心思路**：通过提供多种社交情境下的合作与拒绝合作示例，评估LLMs的判断，并利用进化博弈理论分析这些判断对合作动态的影响。

**技术框架**：研究首先收集了21种不同的LLMs，并为每个模型提供了丰富的社交互动示例。然后，通过分析模型的判断结果，结合进化博弈模型，评估合作的长期影响。

**关键创新**：本研究的创新点在于系统评估LLMs在不同社交情境下的判断一致性与差异，揭示了这些差异如何影响人类合作的普遍性。

**关键设计**：研究中使用了多种社交情境示例，并通过目标导向的提示来引导LLMs的判断，探索如何通过调整提示来影响模型的判断结果。具体的参数设置和损失函数设计未在摘要中详细说明，需参考原文获取更多技术细节。

## 📊 实验亮点

研究发现，LLMs在评估与良好对手的合作时表现出显著的一致性，而在与声誉不佳的个体合作时则存在较大差异。这些差异可能显著影响合作的普遍性，提示我们在设计LLM时需谨慎对待其判断标准。

## 🎯 应用场景

该研究的潜在应用领域包括社会决策支持系统、道德与政治判断辅助工具等。通过理解LLMs对人类合作的影响，可以在设计社交平台和决策支持系统时更好地维护人类的合作行为，促进社会和谐与信任。

## 📄 摘要（原文）

> Humans increasingly rely on large language models (LLMs) to support decisions in social settings. Previous work suggests that such tools shape people's moral and political judgements. However, the long-term implications of LLM-based social decision-making remain unknown. How will human cooperation be affected when the assessment of social interactions relies on language models? This is a pressing question, as human cooperation is often driven by indirect reciprocity, reputations, and the capacity to judge interactions of others. Here, we assess how state-of-the-art LLMs judge cooperative actions. We provide 21 different LLMs with an extensive set of examples where individuals cooperate -- or refuse cooperating -- in a range of social contexts, and ask how these interactions should be judged. Furthermore, through an evolutionary game-theoretical model, we evaluate cooperation dynamics in populations where the extracted LLM-driven judgements prevail, assessing the long-term impact of LLMs on human prosociality. We observe a remarkable agreement in evaluating cooperation against good opponents. On the other hand, we notice within- and between-model variance when judging cooperation with ill-reputed individuals. We show that the differences revealed between models can significantly impact the prevalence of cooperation. Finally, we test prompts to steer LLM norms, showing that such interventions can shape LLM judgements, particularly through goal-oriented prompts. Our research connects LLM-based advices and long-term social dynamics, and highlights the need to carefully align LLM norms in order to preserve human cooperation.

