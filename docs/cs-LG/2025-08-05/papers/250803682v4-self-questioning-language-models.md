---
layout: default
title: Self-Questioning Language Models
---

# Self-Questioning Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03682" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03682v4</a>
  <a href="https://arxiv.org/pdf/2508.03682.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03682v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03682v4', 'Self-Questioning Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lili Chen, Mihir Prabhudesai, Katerina Fragkiadaki, Hao Liu, Deepak Pathak

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-05 (更新: 2025-09-09)

---

## 💡 一句话要点

**提出自问自答语言模型以提升推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自问自答` `语言模型` `推理能力` `强化学习` `无监督学习`

## 📋 核心要点

1. 现有方法在推理能力提升方面依赖于外部数据，限制了模型的自我学习能力。
2. 论文提出了一种自问自答的框架，通过提问者和解答者的互动来生成和解决问题，提升模型的推理能力。
3. 实验结果显示，该方法在三位数乘法、代数问题和编程问题上均取得了显著的性能提升。

## 📝 摘要（中文）

本研究探讨大型语言模型是否可以通过生成自身问题和答案而无需外部数据来提升推理能力。我们假设，预训练的语言模型在给定主题提示的情况下，可以生成自己的问题，从而改善其推理能力。为此，我们提出了自问自答语言模型（SQLM），这是一种不对称自我对弈框架，其中提问者生成问题，解答者尝试回答。提问者和解答者均通过强化学习进行训练，提问者在问题难度适中时获得奖励，解答者则基于多数投票获得奖励。我们在三个基准上研究了这一框架，结果表明，语言模型能够在没有任何策划训练数据集的情况下，通过不断生成和解决更有趣的问题来提升下游基准的表现。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在推理能力提升过程中对外部数据的依赖问题。现有方法往往需要大量标注数据，限制了模型的自我学习和适应能力。

**核心思路**：论文的核心思路是通过自问自答的方式，利用预训练语言模型生成问题并尝试解答，从而在没有外部数据的情况下提升推理能力。提问者生成问题，解答者尝试回答，二者通过强化学习相互促进。

**技术框架**：整体架构包括提问者和解答者两个主要模块。提问者在给定主题下生成问题，解答者尝试回答这些问题。二者通过强化学习进行训练，提问者和解答者的奖励机制分别基于问题难度和回答的正确性。

**关键创新**：最重要的技术创新在于引入了不对称自我对弈的框架，使得语言模型能够在没有外部数据的情况下，通过生成和解决问题来提升自身能力。这种方法与传统依赖大量标注数据的训练方式本质上不同。

**关键设计**：在设计中，提问者的奖励机制考虑了问题的难度，确保生成的问题既不太简单也不太困难；解答者的奖励则基于多数投票，作为正确性的代理。此外，对于编程任务，提问者可以生成单元测试用于验证解答的正确性。

## 📊 实验亮点

实验结果表明，SQLM在三个基准测试中均表现出色，尤其是在代数问题和编程问题上，模型的性能显著提升，展示了在没有策划训练数据集的情况下，语言模型的自我学习能力和推理能力的增强。

## 🎯 应用场景

该研究的潜在应用领域包括教育、编程辅助和智能问答系统等。通过自问自答的方式，模型能够在没有外部数据的情况下不断提升自身的推理能力，具有重要的实际价值和广泛的应用前景。未来，这一方法可能会推动更高效的自我学习系统的发展，减少对人工标注数据的依赖。

## 📄 摘要（原文）

> Can large language models improve without external data -- by generating their own questions and answers? We hypothesize that a pre-trained language model can improve its reasoning skills given only a single prompt specifying the topic (e.g., algebra word problems) and asking the model to generate its own questions. To do this, we propose Self-Questioning Language Models (SQLM): an asymmetric self-play framework where a proposer is given the topic and generates a question for a solver, who tries to answer it. Both the proposer and solver are trained via reinforcement learning. The proposer receives a reward if the problem is not too easy or too difficult, and the solver receives a reward based on majority voting, a proxy for correctness in the absence of ground-truth answers. For coding, the proposer can instead generate unit tests which are used for verification. We study this asymmetric self-play framework on three benchmarks: three-digit multiplication, algebra problems from the OMEGA benchmark, and programming problems from Codeforces. By continually generating more interesting problems and attempting to solve them, language models can improve on downstream benchmarks without access to any curated training datasets.

