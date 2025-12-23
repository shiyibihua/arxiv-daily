---
layout: default
title: Persona-Assigned Large Language Models Exhibit Human-Like Motivated Reasoning
---

# Persona-Assigned Large Language Models Exhibit Human-Like Motivated Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20020" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20020v1</a>
  <a href="https://arxiv.org/pdf/2506.20020.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20020v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20020v1', 'Persona-Assigned Large Language Models Exhibit Human-Like Motivated Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Saloni Dash, Amélie Reymond, Emma S. Spiro, Aylin Caliskan

**分类**: cs.AI, cs.CL

**发布日期**: 2025-06-24

---

## 💡 一句话要点

**研究表明人格分配的大型语言模型表现出人类般的动机推理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `动机推理` `认知偏见` `人格分配` `科学证据评估` `信息真伪辨别` `去偏见方法`

## 📋 核心要点

1. 现有研究表明，大型语言模型容易受到人类认知偏见的影响，但其在身份一致推理方面的表现尚未深入探讨。
2. 本文通过为LLMs分配8种人格，研究其在信息真伪辨别和科学证据评估中的动机推理现象。
3. 实验结果显示，分配人格的LLMs在真伪辨别上准确率降低9%，而在与其政治身份一致的情况下，评估科学证据的正确率提高90%。

## 📝 摘要（中文）

人类的推理常因身份保护等动机而受到偏见影响，进而削弱理性决策。本文探讨了在大型语言模型（LLMs）中分配8种人格是否会引发动机推理。研究发现，分配人格的LLMs在信息真伪辨别上比未分配人格的模型降低了9%的准确性，尤其在与其政治身份一致的情况下，政治人格模型在评估科学证据时的正确率提高了90%。常规的去偏见方法对这些影响效果不佳，提示了LLMs和人类在身份一致推理方面的潜在风险。

## 🔬 方法详解

**问题定义**：本文旨在探讨大型语言模型在分配人格后是否会表现出动机推理，现有方法未能充分揭示这一现象的影响。

**核心思路**：通过为LLMs分配不同的政治和社会人口属性的人格，研究其在推理任务中的表现，以揭示动机推理的存在及其影响。

**技术框架**：研究涉及8种LLMs（包括开源和专有模型），在两个推理任务上进行测试：信息真伪辨别和科学证据评估。

**关键创新**：首次系统性地展示了人格分配对LLMs推理过程的影响，尤其是在与其身份一致的情况下，表现出明显的动机推理特征。

**关键设计**：实验中使用了多种人格设置，评估其在不同任务中的表现，且常规的去偏见方法未能有效缓解这些影响。

## 📊 实验亮点

实验结果显示，分配人格的LLMs在信息真伪辨别上准确率降低了9%，而在与其政治身份一致的情况下，评估科学证据的正确率提高了90%。常规的去偏见方法未能有效减轻这些影响，提示了潜在的风险。

## 🎯 应用场景

该研究的发现对社会科学、心理学和人工智能领域具有重要意义，尤其是在理解和设计更具人性化的AI系统时。未来，研究结果可用于改善AI在敏感话题上的表现，减少偏见影响，从而促进更理性的公共讨论。

## 📄 摘要（原文）

> Reasoning in humans is prone to biases due to underlying motivations like identity protection, that undermine rational decision-making and judgment. This motivated reasoning at a collective level can be detrimental to society when debating critical issues such as human-driven climate change or vaccine safety, and can further aggravate political polarization. Prior studies have reported that large language models (LLMs) are also susceptible to human-like cognitive biases, however, the extent to which LLMs selectively reason toward identity-congruent conclusions remains largely unexplored. Here, we investigate whether assigning 8 personas across 4 political and socio-demographic attributes induces motivated reasoning in LLMs. Testing 8 LLMs (open source and proprietary) across two reasoning tasks from human-subject studies -- veracity discernment of misinformation headlines and evaluation of numeric scientific evidence -- we find that persona-assigned LLMs have up to 9% reduced veracity discernment relative to models without personas. Political personas specifically, are up to 90% more likely to correctly evaluate scientific evidence on gun control when the ground truth is congruent with their induced political identity. Prompt-based debiasing methods are largely ineffective at mitigating these effects. Taken together, our empirical findings are the first to suggest that persona-assigned LLMs exhibit human-like motivated reasoning that is hard to mitigate through conventional debiasing prompts -- raising concerns of exacerbating identity-congruent reasoning in both LLMs and humans.

