---
layout: default
title: Identifying Reliable Evaluation Metrics for Scientific Text Revision
---

# Identifying Reliable Evaluation Metrics for Scientific Text Revision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04772" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04772v3</a>
  <a href="https://arxiv.org/pdf/2506.04772.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04772v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04772v3', 'Identifying Reliable Evaluation Metrics for Scientific Text Revision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Léane Jourdan, Florian Boudin, Richard Dufour, Nicolas Hernandez

**分类**: cs.CL

**发布日期**: 2025-06-05 (更新: 2025-06-12)

**备注**: V3 contains only the English version, accepted to ACL 2025 main (26 pages). V2 contains both English (ACL 2025) and French (TALN 2025) versions (58 pages)

---

## 💡 一句话要点

**提出混合评估方法以解决科学文本修订评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本修订` `评估指标` `自然语言处理` `大型语言模型` `科学写作` `混合方法`

## 📋 核心要点

1. 核心问题：现有的评估指标如ROUGE和BERTScore未能有效捕捉文本修订的实际改进，导致评估结果的可靠性不足。
2. 方法要点：本文提出了一种混合评估方法，结合了LLM作为评估者的能力与领域特定的评估指标，以提高评估的准确性。
3. 实验或效果：实验结果显示，混合评估方法在修订质量评估上表现优越，尤其在指令遵循方面效果显著。

## 📝 摘要（中文）

科学写作中的文本修订评估仍然面临挑战，传统的评估指标如ROUGE和BERTScore主要关注相似性，而未能捕捉到有意义的改进。本文分析并识别了这些指标的局限性，探索了更符合人类判断的替代评估方法。我们首先进行了一项手动标注研究，以评估不同修订的质量。然后，我们调查了来自相关NLP领域的无参考评估指标。此外，我们还考察了LLM作为评估者的方法，分析其在有无金标准情况下评估修订的能力。结果表明，LLM在遵循指令方面有效，但在正确性评估上存在困难，而领域特定的指标提供了互补的见解。我们发现，结合LLM评估和任务特定指标的混合方法提供了最可靠的修订质量评估。

## 🔬 方法详解

**问题定义**：本文旨在解决科学文本修订评估中的可靠性问题，现有方法主要关注文本相似性，未能有效反映修订的质量和改进。

**核心思路**：论文提出了一种混合评估方法，结合了大型语言模型（LLM）和领域特定的评估指标，以更全面地评估文本修订的质量。这样的设计旨在克服传统指标的局限性，提供更符合人类判断的评估结果。

**技术框架**：整体架构包括三个主要模块：首先进行手动标注研究以评估修订质量；其次调查无参考评估指标；最后分析LLM作为评估者的能力。

**关键创新**：最重要的技术创新在于提出了LLM与领域特定指标的结合使用，这种混合方法能够提供更可靠的评估结果，与传统方法相比，能够更好地反映文本修订的实际改进。

**关键设计**：在设计中，LLM的选择和训练过程至关重要，此外，任务特定指标的选择也影响评估的准确性，论文中对这些参数进行了详细讨论。

## 📊 实验亮点

实验结果表明，混合评估方法在修订质量评估中表现优越，尤其在指令遵循方面，LLM的评估能力显著提升。与传统方法相比，混合方法提供了更全面的评估视角，能够更好地捕捉文本修订的实际改进。

## 🎯 应用场景

该研究的潜在应用领域包括学术写作、文本编辑和自然语言处理等。通过提供更可靠的文本修订评估方法，能够帮助研究人员和编辑更有效地改进科学论文的质量，提升学术交流的效率。未来，该方法还可能扩展到其他文本生成和修改任务中，具有广泛的实际价值。

## 📄 摘要（原文）

> Evaluating text revision in scientific writing remains a challenge, as traditional metrics such as ROUGE and BERTScore primarily focus on similarity rather than capturing meaningful improvements. In this work, we analyse and identify the limitations of these metrics and explore alternative evaluation methods that better align with human judgments. We first conduct a manual annotation study to assess the quality of different revisions. Then, we investigate reference-free evaluation metrics from related NLP domains. Additionally, we examine LLM-as-a-judge approaches, analysing their ability to assess revisions with and without a gold reference. Our results show that LLMs effectively assess instruction-following but struggle with correctness, while domain-specific metrics provide complementary insights. We find that a hybrid approach combining LLM-as-a-judge evaluation and task-specific metrics offers the most reliable assessment of revision quality.

