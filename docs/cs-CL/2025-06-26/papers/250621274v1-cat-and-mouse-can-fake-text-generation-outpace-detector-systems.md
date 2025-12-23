---
layout: default
title: Cat and Mouse -- Can Fake Text Generation Outpace Detector Systems?
---

# Cat and Mouse -- Can Fake Text Generation Outpace Detector Systems?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21274" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21274v1</a>
  <a href="https://arxiv.org/pdf/2506.21274.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21274v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21274v1', 'Cat and Mouse -- Can Fake Text Generation Outpace Detector Systems?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andrea McGlinchey, Peter J Barclay

**分类**: cs.CL

**发布日期**: 2025-06-26

**备注**: (Submitted for publication)

---

## 💡 一句话要点

**探讨假文本生成与检测系统的博弈关系**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `假文本检测` `大型语言模型` `统计分类器` `文本生成` `信息真实性`

## 📋 核心要点

1. 当前的假文本检测方法在面对不断增强的生成模型时，可能会面临能力的瓶颈。
2. 本文通过统计分类器分析经典侦探小说风格的假文本，探讨其检测能力与生成模型的关系。
3. 实验结果显示，Gemini在生成欺骗性文本方面表现优于GPT，表明检测的可行性依然存在。

## 📝 摘要（中文）

大型语言模型能够在学术写作、产品评论和政治新闻等领域生成令人信服的“假文本”。尽管已有多种方法用于检测人工生成的文本，但新一代大型语言模型（LLMs）在参数、训练数据和能耗上不断增加，而相对简单的分类器在资源有限的情况下仍能实现良好的检测准确率。本文研究了统计分类器在经典侦探小说风格的“假文本”识别能力。结果表明，Gemini在生成欺骗性文本方面表现出更强的能力，而GPT则未见显著提升。这表明，即使面对越来越大的模型，可靠的假文本检测仍然是可行的，尽管新的模型架构可能会提高其欺骗性。

## 🔬 方法详解

**问题定义**：本文旨在探讨假文本生成模型与检测系统之间的博弈关系，尤其是现有检测方法在面对新一代大型语言模型时的有效性和局限性。

**核心思路**：通过对经典侦探小说风格的假文本进行分析，评估统计分类器在识别这些文本方面的能力，探讨生成模型的提升是否会影响检测的准确性。

**技术框架**：研究采用了统计分类器对生成的假文本进行评估，比较不同版本的生成模型（如Gemini与GPT）在文本生成能力上的差异。

**关键创新**：本研究的创新在于通过具体的文本风格（侦探小说）来评估假文本的生成与检测能力，揭示了即使在模型参数不断增加的情况下，检测的可靠性依然存在。

**关键设计**：实验中对比了Gemini与GPT在生成文本的欺骗性方面的表现，发现Gemini在生成能力上有显著提升，而GPT则未见明显变化。

## 📊 实验亮点

实验结果显示，Gemini在生成欺骗性文本方面的能力显著增强，而GPT则未表现出相应的提升。这表明，尽管生成模型在不断进化，统计分类器仍能有效识别假文本，保持检测的可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括学术诚信、在线评论的真实性验证以及新闻报道的可信度评估。随着假文本生成技术的不断进步，开发有效的检测工具将对维护信息的真实性和可靠性产生重要影响。

## 📄 摘要（原文）

> Large language models can produce convincing "fake text" in domains such as academic writing, product reviews, and political news. Many approaches have been investigated for the detection of artificially generated text. While this may seem to presage an endless "arms race", we note that newer LLMs use ever more parameters, training data, and energy, while relatively simple classifiers demonstrate a good level of detection accuracy with modest resources. To approach the question of whether the models' ability to beat the detectors may therefore reach a plateau, we examine the ability of statistical classifiers to identify "fake text" in the style of classical detective fiction. Over a 0.5 version increase, we found that Gemini showed an increased ability to generate deceptive text, while GPT did not. This suggests that reliable detection of fake text may remain feasible even for ever-larger models, though new model architectures may improve their deceptiveness

