---
layout: default
title: Large Language Model probabilities cannot distinguish between possible and impossible language
---

# Large Language Model probabilities cannot distinguish between possible and impossible language

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15114" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15114v1</a>
  <a href="https://arxiv.org/pdf/2509.15114.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15114v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15114v1', 'Large Language Model probabilities cannot distinguish between possible and impossible language')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Evelina Leivada, Raquel Montero, Paolo Morosi, Natalia Moskvina, Tamara Serrano, Marcel Aguilar, Fritz Guenther

**分类**: cs.CL

**发布日期**: 2025-09-18

---

## 💡 一句话要点

**大型语言模型概率无法区分语言的可能性与不可能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `语法知识` `Surprisal` `语言可能性` `模型评估`

## 📋 核心要点

1. 现有研究对LLM区分语法与非语法语言的能力存在争议，测试材料的可靠性是关键挑战。
2. 该研究通过分析模型内部表示和概率，探究LLM如何区分语法和非语法结构。
3. 实验结果表明，LLM的概率不能可靠地反映其内部语法知识，语义和语用异常的影响更大。

## 📝 摘要（中文）

本文研究大型语言模型（LLM）区分可能语言和不可能语言的能力。尽管有证据表明模型对语法不可能的语言边界具有敏感性，但这些证据因测试材料的可靠性而受到质疑。本文使用模型内部表示来直接探究LLM如何表示“语法-非语法”的区别。通过一项新的基准测试，从4个模型中提取概率，并计算最小对的surprisal差异，将语法句子的概率与（i）较低频率的语法句子，（ii）非语法句子，（iii）语义上奇怪的句子和（iv）语用上奇怪的句子进行对比。预测是，如果字符串概率可以作为语法限制的代理，那么非语法条件将在涉及语言违规的条件中脱颖而出，显示出surprisal率的峰值。结果表明，非语法提示没有独特的surprisal特征，因为语义和语用上奇怪的条件始终显示出更高的surprisal。因此，证明概率不能作为模型内部语法知识表示的可靠代理。因此，关于模型能够区分可能语言和不可能语言的说法需要通过不同的方法进行验证。

## 🔬 方法详解

**问题定义**：现有方法难以准确评估大型语言模型（LLM）区分语法上可能和不可能的语言的能力。以往研究依赖的测试材料可能存在偏差，导致结论的可靠性受到质疑。因此，需要一种更直接、更可靠的方法来探究LLM的内部语法知识表示。

**核心思路**：该研究的核心思路是绕过外部测试材料的潜在偏差，直接分析LLM内部的概率分布，特别是通过计算不同类型语言结构的surprisal值。通过比较语法正确、语法错误、语义异常和语用异常的句子，观察LLM在概率上的差异，从而推断其内部语法知识的表示方式。

**技术框架**：该研究的技术框架主要包括以下几个步骤：1) 从预训练的LLM中提取不同类型句子的概率；2) 计算最小对的surprisal差异，即比较相似句子在概率上的差异；3) 将语法正确的句子与四种类型的违规句子（低频语法、非语法、语义异常、语用异常）进行对比；4) 分析surprisal值的分布，寻找非语法句子是否具有独特的特征。

**关键创新**：该研究的关键创新在于使用模型内部的概率分布作为探究LLM语法知识的手段，避免了外部测试材料可能引入的偏差。通过比较不同类型语言结构的surprisal值，可以更直接地了解LLM如何区分语法和非语法结构。

**关键设计**：研究中使用了最小对（minimal pairs）设计，确保对比的句子在其他方面尽可能相似，从而突出语法差异的影响。Surprisal值被用作衡量模型对句子意外程度的指标，计算公式通常基于句子概率的负对数。研究选择了4个不同的LLM进行实验，以验证结果的普遍性。

## 📊 实验亮点

实验结果表明，LLM的概率分布并不能可靠地区分语法正确和语法错误的句子。相反，语义和语用异常的句子往往具有更高的surprisal值，表明LLM对这些类型的违规更为敏感。这一发现挑战了以往关于LLM能够区分可能语言和不可能语言的观点，并强调了使用更可靠的方法评估LLM语法能力的重要性。

## 🎯 应用场景

该研究成果有助于更深入地理解大型语言模型的内部工作机制，特别是在语法知识表示方面。这对于改进LLM的语言生成能力、提高其在自然语言处理任务中的表现具有重要意义。此外，该研究的方法也可以应用于评估其他类型语言模型的语法能力，并为模型的设计和训练提供指导。

## 📄 摘要（原文）

> A controversial test for Large Language Models concerns the ability to discern possible from impossible language. While some evidence attests to the models' sensitivity to what crosses the limits of grammatically impossible language, this evidence has been contested on the grounds of the soundness of the testing material. We use model-internal representations to tap directly into the way Large Language Models represent the 'grammatical-ungrammatical' distinction. In a novel benchmark, we elicit probabilities from 4 models and compute minimal-pair surprisal differences, juxtaposing probabilities assigned to grammatical sentences to probabilities assigned to (i) lower frequency grammatical sentences, (ii) ungrammatical sentences, (iii) semantically odd sentences, and (iv) pragmatically odd sentences. The prediction is that if string-probabilities can function as proxies for the limits of grammar, the ungrammatical condition will stand out among the conditions that involve linguistic violations, showing a spike in the surprisal rates. Our results do not reveal a unique surprisal signature for ungrammatical prompts, as the semantically and pragmatically odd conditions consistently show higher surprisal. We thus demonstrate that probabilities do not constitute reliable proxies for model-internal representations of syntactic knowledge. Consequently, claims about models being able to distinguish possible from impossible language need verification through a different methodology.

