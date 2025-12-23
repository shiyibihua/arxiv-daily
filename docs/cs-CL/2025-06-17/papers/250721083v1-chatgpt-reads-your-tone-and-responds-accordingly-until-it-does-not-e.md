---
layout: default
title: ChatGPT Reads Your Tone and Responds Accordingly -- Until It Does Not -- Emotional Framing Induces Bias in LLM Outputs
---

# ChatGPT Reads Your Tone and Responds Accordingly -- Until It Does Not -- Emotional Framing Induces Bias in LLM Outputs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.21083" class="toolbar-btn" target="_blank">📄 arXiv: 2507.21083v1</a>
  <a href="https://arxiv.org/pdf/2507.21083.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.21083v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.21083v1', 'ChatGPT Reads Your Tone and Responds Accordingly -- Until It Does Not -- Emotional Framing Induces Bias in LLM Outputs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Franck Bardol

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-17

**🔗 代码/项目**: [GITHUB](https://github.com/bardolfranck/llm-responses-viewer)

---

## 💡 一句话要点

**探讨情感框架对大型语言模型输出的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感分析` `大型语言模型` `模型偏差` `AI对齐` `用户信任`

## 📋 核心要点

1. 现有大型语言模型在情感框架下的响应偏差尚未得到充分研究，可能影响模型的可靠性和信任度。
2. 本文通过系统变化提示的情感基调，探讨其对GPT-4响应的影响，提出了新的量化方法。
3. 实验结果表明，GPT-4对负面问题的响应显著减少，尤其在敏感话题上，模型的情感响应被抑制。

## 📝 摘要（中文）

大型语言模型（如GPT-4）不仅根据提问内容调整响应，还会受到情感措辞的影响。本文系统地变化了156个提示的情感基调，分析其对模型响应的影响。研究发现，GPT-4对负面框架问题的负面响应概率是中性问题的三分之一，表明模型存在“反弹”偏差，常常向中性或积极倾斜。在敏感话题上，这种效应更为明显，提示的基调变化被抑制，暗示对齐覆盖现象。我们引入了“基调下限”等概念，并使用基调-效价转移矩阵量化行为，1536维嵌入的可视化结果确认了基于基调的语义漂移。我们的研究揭示了情感框架驱动的偏差这一未被充分探讨的类别，对AI对齐和信任具有重要影响。

## 🔬 方法详解

**问题定义**：本文旨在探讨大型语言模型在情感框架下的响应偏差，现有方法未能充分考虑情感措辞对模型输出的影响，导致模型在敏感话题上的表现不一致。

**核心思路**：通过系统性地变化提示的情感基调，分析其对模型响应的影响，提出“基调下限”等新概念，以量化模型的情感响应特征。

**技术框架**：研究采用156个不同情感基调的提示，结合1536维嵌入进行可视化分析，使用基调-效价转移矩阵量化模型的响应变化。

**关键创新**：引入了“反弹”偏差和“基调下限”概念，揭示了情感框架对模型输出的深远影响，填补了现有研究的空白。

**关键设计**：在实验中，使用了多种情感基调的提示，并通过量化分析和可视化手段，深入探讨了模型在不同情感框架下的响应特征。具体参数设置和损失函数未在摘要中详细说明。

## 📊 实验亮点

实验结果显示，GPT-4对负面框架问题的负面响应概率是中性问题的三分之一，表明模型存在显著的“反弹”偏差。在敏感话题上，这种偏差更加明显，提示的情感基调变化被抑制，强调了情感框架对模型输出的深远影响。

## 🎯 应用场景

该研究的潜在应用领域包括情感分析、用户交互设计和AI对话系统的优化。通过理解情感框架对模型输出的影响，可以提升AI系统在敏感话题上的响应质量，增强用户信任，推动更安全和可靠的AI应用。未来，研究结果可能引导更好的AI对齐策略，确保模型在多样化情感表达下的稳定性。

## 📄 摘要（原文）

> Large Language Models like GPT-4 adjust their responses not only based on the question asked, but also on how it is emotionally phrased. We systematically vary the emotional tone of 156 prompts - spanning controversial and everyday topics - and analyze how it affects model responses. Our findings show that GPT-4 is three times less likely to respond negatively to a negatively framed question than to a neutral one. This suggests a "rebound" bias where the model overcorrects, often shifting toward neutrality or positivity. On sensitive topics (e.g., justice or politics), this effect is even more pronounced: tone-based variation is suppressed, suggesting an alignment override. We introduce concepts like the "tone floor" - a lower bound in response negativity - and use tone-valence transition matrices to quantify behavior. Visualizations based on 1536-dimensional embeddings confirm semantic drift based on tone. Our work highlights an underexplored class of biases driven by emotional framing in prompts, with implications for AI alignment and trust. Code and data are available at: https://github.com/bardolfranck/llm-responses-viewer

