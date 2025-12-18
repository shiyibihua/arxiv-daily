---
layout: default
title: Measuring and mitigating overreliance is necessary for building human-compatible AI
---

# Measuring and mitigating overreliance is necessary for building human-compatible AI

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08010" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08010v1</a>
  <a href="https://arxiv.org/pdf/2509.08010.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08010v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08010v1', 'Measuring and mitigating overreliance is necessary for building human-compatible AI')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lujain Ibrahim, Katherine M. Collins, Sunnie S. Y. Kim, Anka Reuel, Max Lamparth, Kevin Feng, Lama Ahmad, Prajna Soni, Alia El Kattan, Merlin Stein, Siddharth Swaroop, Ilia Sucholutsky, Andrew Strait, Q. Vera Liao, Umang Bhatt

**分类**: cs.CY, cs.AI, cs.CL, cs.HC

**发布日期**: 2025-09-08

---

## 💡 一句话要点

**针对大语言模型过度依赖风险，提出测量与缓解策略，保障人机协同。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `过度依赖` `人机协作` `认知偏差` `风险评估`

## 📋 核心要点

1. 现有方法未能充分解决LLM带来的过度依赖风险，可能导致高风险决策失误和认知能力下降。
2. 论文核心在于提出一套测量和缓解LLM过度依赖的框架，强调人机协同而非完全依赖AI。
3. 论文分析了LLM特性、系统设计和用户认知偏差，并提出了改进测量和缓解策略的方向。

## 📝 摘要（中文）

大型语言模型（LLMs）通过更流畅的自然语言交互，作为协作“思考伙伴”脱颖而出。随着LLMs在医疗保健和个人建议等领域对重要决策的影响日益增加，过度依赖——即超出LLMs能力范围的依赖——的风险也在增长。本文认为，测量和缓解过度依赖必须成为LLM研究和部署的核心。首先，我们整合了个人和社会层面的过度依赖风险，包括高风险错误、治理挑战和认知技能退化。然后，我们探讨了LLM的特性、系统设计特征以及用户认知偏差，这些因素共同引发了对实践中过度依赖的严重和独特的担忧。我们还考察了测量过度依赖的历史方法，识别出三个重要差距，并提出了三个有希望的改进测量方向。最后，我们提出了AI研究界可以采取的缓解策略，以确保LLMs增强而非削弱人类能力。

## 🔬 方法详解

**问题定义**：论文旨在解决用户对大型语言模型（LLMs）的过度依赖问题。现有方法的痛点在于缺乏对过度依赖的有效测量和缓解机制，导致用户在高风险场景下可能盲目信任LLM的输出，从而产生错误决策，并可能导致用户认知能力的退化。

**核心思路**：论文的核心解决思路是建立一套全面的框架，用于测量和缓解用户对LLM的过度依赖。该框架强调理解LLM的特性、系统设计以及用户认知偏差在过度依赖形成中的作用，并基于此提出相应的干预措施。核心在于确保LLM作为辅助工具，增强而非取代人类的判断和决策能力。

**技术框架**：论文并未提出一个具体的、可执行的技术框架，而更多的是一个概念性的框架。它包含以下几个主要阶段：1) 识别过度依赖的风险，包括个人和社会层面；2) 分析LLM的特性、系统设计和用户认知偏差，理解其如何导致过度依赖；3) 评估现有测量过度依赖的方法，识别其不足；4) 提出改进测量和缓解过度依赖的策略。

**关键创新**：论文的关键创新在于其对LLM过度依赖问题的系统性分析和框架性思考。它没有提出一个全新的算法或模型，而是从更宏观的角度审视了LLM的应用风险，并强调了人机协同的重要性。与现有方法相比，该论文更注重对问题本质的理解和对潜在风险的预判。

**关键设计**：由于论文主要关注框架性的讨论，因此没有涉及具体的参数设置、损失函数或网络结构等技术细节。论文提出的缓解策略包括改进LLM的透明度和可解释性、设计更友好的用户界面、以及对用户进行相关培训，以提高其对LLM局限性的认识。

## 📊 实验亮点

该论文是一篇立场性文章，没有提供具体的实验结果。其亮点在于系统性地分析了LLM过度依赖的风险，并提出了改进测量和缓解策略的方向。论文强调了在LLM应用中，需要充分考虑用户认知偏差和系统设计因素，以确保人机协同的有效性。

## 🎯 应用场景

该研究成果可应用于各种涉及人机协作的领域，如医疗诊断、金融投资、法律咨询等。通过有效测量和缓解过度依赖，可以提高决策质量，降低风险，并促进人与AI的和谐共处。未来，该研究将有助于构建更安全、可靠和以人为本的AI系统。

## 📄 摘要（原文）

> Large language models (LLMs) distinguish themselves from previous technologies by functioning as collaborative "thought partners," capable of engaging more fluidly in natural language. As LLMs increasingly influence consequential decisions across diverse domains from healthcare to personal advice, the risk of overreliance - relying on LLMs beyond their capabilities - grows. This position paper argues that measuring and mitigating overreliance must become central to LLM research and deployment. First, we consolidate risks from overreliance at both the individual and societal levels, including high-stakes errors, governance challenges, and cognitive deskilling. Then, we explore LLM characteristics, system design features, and user cognitive biases that - together - raise serious and unique concerns about overreliance in practice. We also examine historical approaches for measuring overreliance, identifying three important gaps and proposing three promising directions to improve measurement. Finally, we propose mitigation strategies that the AI research community can pursue to ensure LLMs augment rather than undermine human capabilities.

