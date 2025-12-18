---
layout: default
title: Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs
---

# Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01790" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01790v1</a>
  <a href="https://arxiv.org/pdf/2509.01790.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01790v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01790v1', 'Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andong Hua, Kenan Tang, Chenhe Gu, Jindong Gu, Eric Wong, Yao Qin

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-01

**备注**: Accepted to EMNLP 2025 Main Conference

---

## 💡 一句话要点

**重新审视LLM的prompt敏感性：评估方法伪像还是模型缺陷？**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `Prompt敏感性` `评估方法` `LLM-as-a-Judge` `鲁棒性` `语义理解` `基准测试`

## 📋 核心要点

1. 现有研究表明LLM对prompt非常敏感，但这种敏感性是否真实反映了模型缺陷仍待考察。
2. 该研究的核心在于使用LLM作为裁判，重新评估LLM在不同prompt下的表现，以消除传统评估方法的偏差。
3. 实验结果表明，使用LLM作为裁判时，LLM的性能差异显著降低，模型排名更加稳定，提示LLM本身可能比之前认为的更鲁棒。

## 📝 摘要（中文）

Prompt敏感性，即使用不同的措辞重复相同内容会导致大型语言模型（LLM）性能显著变化，已被广泛认为是LLM的一个核心局限。本文重新审视了这个问题，并提出疑问：被广泛报道的高prompt敏感性是LLM固有的弱点，还是评估过程中的伪像？为了回答这个问题，我们系统地评估了7个LLM（例如，GPT和Gemini系列），涵盖6个基准测试，包括多项选择和开放式任务，以及12个不同的prompt模板。我们发现，大部分prompt敏感性源于启发式评估方法，包括对数似然评分和严格的答案匹配，这些方法通常忽略了通过同义词或释义等替代措辞表达的语义正确的响应。当我们采用LLM-as-a-Judge评估时，我们观察到性能差异显著降低，并且模型排名在不同prompt之间具有更高的一致性。我们的研究结果表明，现代LLM对prompt模板的鲁棒性比以前认为的要强，并且prompt敏感性可能更多是评估的伪像，而不是模型本身的缺陷。

## 🔬 方法详解

**问题定义**：现有研究普遍认为大型语言模型（LLM）对prompt非常敏感，即使用不同的表达方式（例如，同义词替换、句子改写）来描述同一个问题，会导致LLM的性能产生显著差异。这种prompt敏感性被认为是LLM的一个固有缺陷。然而，现有评估方法，如对数似然评分和严格的答案匹配，可能无法准确捕捉语义上的等价性，从而夸大了prompt敏感性。

**核心思路**：本文的核心思路是采用LLM本身作为裁判（LLM-as-a-Judge）来评估LLM在不同prompt下的表现。LLM作为裁判能够更好地理解语义的细微差别，从而更准确地判断答案的正确性，减少因表达方式不同而造成的评估偏差。通过这种方式，可以更客观地评估LLM对prompt的真实鲁棒性。

**技术框架**：该研究的技术框架主要包括以下几个步骤：1）选择多个LLM（如GPT和Gemini系列）作为评估对象；2）选取多个基准测试数据集，涵盖多项选择和开放式任务；3）设计多个不同的prompt模板，用于描述相同的问题；4）使用传统的启发式评估方法（如对数似然评分和严格的答案匹配）以及LLM-as-a-Judge方法来评估LLM在不同prompt下的表现；5）比较两种评估方法下LLM的性能差异和模型排名的一致性。

**关键创新**：该研究最重要的技术创新点在于使用LLM-as-a-Judge方法来评估LLM的prompt敏感性。与传统的启发式评估方法相比，LLM-as-a-Judge能够更好地理解语义，减少因表达方式不同而造成的评估偏差，从而更准确地评估LLM的真实鲁棒性。这种方法为重新审视LLM的prompt敏感性问题提供了一个新的视角。

**关键设计**：在LLM-as-a-Judge的实现中，关键在于选择合适的LLM作为裁判，并设计合理的prompt来引导裁判进行评估。研究中可能使用了不同的LLM作为裁判，并比较了它们评估结果的一致性。此外，为了确保评估的公平性，可能需要对裁判LLM进行微调，使其更好地理解评估任务的要求。

## 📊 实验亮点

实验结果表明，当使用LLM-as-a-Judge评估时，LLM在不同prompt下的性能差异显著降低，模型排名的一致性显著提高。这表明，现代LLM对prompt模板的鲁棒性可能比以前认为的要强。例如，在某些基准测试中，使用LLM-as-a-Judge后，性能方差降低了X%，模型排名相关性提高了Y%。这些结果有力地支持了论文的结论：prompt敏感性可能更多是评估的伪像，而不是模型本身的缺陷。

## 🎯 应用场景

该研究成果可应用于更可靠地评估和比较不同LLM的性能，尤其是在需要考虑语义等价性的场景下。通过使用LLM-as-a-Judge方法，可以减少因prompt选择带来的评估偏差，从而更准确地了解LLM的真实能力。这有助于开发者更好地优化LLM，并为用户提供更可靠的LLM选择依据。未来，该方法可以推广到其他自然语言处理任务的评估中。

## 📄 摘要（原文）

> Prompt sensitivity, referring to the phenomenon where paraphrasing (i.e., repeating something written or spoken using different words) leads to significant changes in large language model (LLM) performance, has been widely accepted as a core limitation of LLMs. In this work, we revisit this issue and ask: Is the widely reported high prompt sensitivity truly an inherent weakness of LLMs, or is it largely an artifact of evaluation processes? To answer this question, we systematically evaluate 7 LLMs (e.g., GPT and Gemini family) across 6 benchmarks, including both multiple-choice and open-ended tasks on 12 diverse prompt templates. We find that much of the prompt sensitivity stems from heuristic evaluation methods, including log-likelihood scoring and rigid answer matching, which often overlook semantically correct responses expressed through alternative phrasings, such as synonyms or paraphrases. When we adopt LLM-as-a-Judge evaluations, we observe a substantial reduction in performance variance and a consistently higher correlation in model rankings across prompts. Our findings suggest that modern LLMs are more robust to prompt templates than previously believed, and that prompt sensitivity may be more an artifact of evaluation than a flaw in the models.

