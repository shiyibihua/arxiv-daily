---
layout: default
title: Estimating problem difficulty without ground truth using Large Language Model comparisons
---

# Estimating problem difficulty without ground truth using Large Language Model comparisons

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14220" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14220v1</a>
  <a href="https://arxiv.org/pdf/2512.14220.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14220v1" onclick="toggleFavorite(this, '2512.14220v1', 'Estimating problem difficulty without ground truth using Large Language Model comparisons')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marthe Ballon, Andres Algaba, Brecht Verbeken, Vincent Ginis

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-16

**备注**: 19 pages, 10 figures

---

## 💡 一句话要点

**提出LLM compare，一种无需ground truth的大语言模型问题难度评估方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `问题难度评估` `大语言模型` `无监督学习` `Bradley-Terry模型` `合成数据生成`

## 📋 核心要点

1. 现有问题难度评估方法依赖人工标注或模型性能，难以泛化到超出分布的、对人类和LLM都困难的问题。
2. LLM compare通过让LLM进行成对难度比较，并计算Bradley-Terry分数，实现无需ground truth的难度评估。
3. 实验表明，LLM compare与人类标注高度一致（Pearson r ≥ 0.80），且对噪声具有较强的鲁棒性。

## 📝 摘要（中文）

本文提出了一种新的问题难度评估方法，名为LLM compare，旨在解决现有方法在外推问题上的局限性。现有方法如人工校准或基于性能的评分，无法推广到超出分布的问题，因为它们不具备可扩展性、耗时且依赖于ground truth。LLM compare通过让大语言模型执行成对难度比较，然后基于比较结果计算Bradley-Terry分数来克服这些限制。为了验证该方法，首先提出了一个概念框架，将现有方法定位在三个正交平面上——构造、规模和依赖性。LLM compare自然地占据了所有理想象限，是第一个连续动态、模型无关且独立于ground truth信息的度量。其次，实验表明LLM compare与人类标注具有很强的一致性（Pearson r ≥ 0.80，n=1876）。第三，LLM compare对幻觉具有鲁棒性，注入10%的噪声后，Pearson相关性仅下降不到6%。这项工作代表着在替代耗时的人工标注和合成数据生成方面迈出了重要一步，并将成为课程设计、模型评估和AI辅助研究构思的重要驱动力。

## 🔬 方法详解

**问题定义**：论文旨在解决现有问题难度评估方法无法有效评估超出分布（out-of-distribution）问题难度的难题。现有方法，如人工校准和基于性能的评分，依赖于人工标注或模型在已知问题上的表现，因此无法推广到那些人类和LLM都难以解决的新问题。这些方法通常耗时、成本高昂，并且需要ground truth信息，限制了它们在快速迭代和探索未知领域的应用。

**核心思路**：论文的核心思路是利用大语言模型（LLM）自身的理解能力来评估问题的相对难度，而无需依赖外部的ground truth。通过让LLM对问题进行成对比较，判断哪个问题更难，然后基于这些比较结果，使用Bradley-Terry模型计算每个问题的难度得分。这种方法的核心在于利用LLM作为一种“内部评估器”，从而避免了对外部标注的依赖。

**技术框架**：LLM compare方法主要包含以下几个阶段：
1. **问题对生成**：从问题集中随机抽取问题对。
2. **LLM比较**：使用LLM对每个问题对进行难度比较，判断哪个问题更难。
3. **Bradley-Terry评分**：基于LLM的比较结果，使用Bradley-Terry模型计算每个问题的难度得分。Bradley-Terry模型是一种用于成对比较数据的统计模型，可以根据比较结果估计每个对象的相对强度或难度。
4. **难度排序**：根据Bradley-Terry得分对问题进行难度排序。

**关键创新**：LLM compare最重要的创新在于它是一种无需ground truth的难度评估方法。与现有方法相比，它具有以下优势：
* **连续动态**：可以对新问题进行评估，无需重新训练或标注。
* **模型无关**：可以使用不同的LLM进行比较，具有较强的通用性。
* **独立于ground truth**：无需人工标注或已知问题的性能数据。

**关键设计**：
* **LLM选择**：论文中使用了特定的大语言模型进行实验，但该方法理论上可以与任何具有足够理解能力的LLM一起使用。LLM的选择可能会影响评估结果的准确性。
* **比较提示词设计**：用于引导LLM进行难度比较的提示词的设计至关重要。提示词需要清晰明确，避免引入偏差。
* **Bradley-Terry模型参数**：Bradley-Terry模型的参数设置可能会影响难度得分的计算结果。论文中可能使用了默认参数或经过调整的参数。

## 📊 实验亮点

实验结果表明，LLM compare与人类标注具有高度一致性，Pearson相关系数达到0.80以上（n=1876）。此外，该方法对LLM的幻觉具有较强的鲁棒性，即使在注入10%的噪声后，Pearson相关系数的下降也小于6%。这些结果验证了LLM compare的有效性和可靠性。

## 🎯 应用场景

LLM compare可应用于合成数据生成、课程学习设计、模型评估和AI辅助研究构思等领域。它可以帮助自动生成更具挑战性的训练数据，设计更有效的学习课程，评估模型的泛化能力，并辅助研究人员探索新的研究方向。该方法尤其适用于那些缺乏ground truth或难以进行人工标注的领域。

## 📄 摘要（原文）

> Recent advances in the finetuning of large language models (LLMs) have significantly improved their performance on established benchmarks, emphasizing the need for increasingly difficult, synthetic data. A key step in this data generation pipeline is a method for estimating problem difficulty. Current approaches, such as human calibration or performance-based scoring, fail to generalize to out-of-distribution problems, i.e. problems currently unsolvable by humans and LLMs, because they are not scalable, time-consuming, and ground truth dependent. Therefore, we propose a new method for estimating problem difficulty, LLM compare, that addresses these limitations. An LLM performs pairwise difficulty comparisons, and then Bradley-Terry scores are computed based on the outcomes. To validate our method, we first propose a conceptual framework that positions existing approaches on three orthogonal planes--construction, scale and dependence--identifying which quadrants a measure needs to occupy to score out-of-distribution problems. LLM compare naturally occupies all desirable quadrants as the first measure that is continuous and dynamic, model-agnostic and independent of ground truth information. As a second validation, we show that LLM compare demonstrates strong alignment with human annotations: Pearson $r \geq 0.80$ for $n=1876$. Thirdly, we show that LLM compare is robust to hallucinations, with less than $6\%$ degradation in Pearson correlation for $10\%$ noise injection. Our work represents a significant step towards replacing time-consuming human annotations and synthetic data generation, and will be an important driver for curriculum design, model evaluation, and AI-assisted research ideation.

