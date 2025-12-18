---
layout: default
title: How Good are Foundation Models in Step-by-Step Embodied Reasoning?
---

# How Good are Foundation Models in Step-by-Step Embodied Reasoning?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15293" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15293v2</a>
  <a href="https://arxiv.org/pdf/2509.15293.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15293v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15293v2', 'How Good are Foundation Models in Step-by-Step Embodied Reasoning?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dinura Dissanayake, Ahmed Heakl, Omkar Thawakar, Noor Ahsan, Ritesh Thawkar, Ketan More, Jean Lahoud, Rao Anwer, Hisham Cholakkal, Ivan Laptev, Fahad Shahbaz Khan, Salman Khan

**分类**: cs.CV, cs.RO

**发布日期**: 2025-09-18 (更新: 2025-09-22)

**备注**: Project page: https://mbzuai-oryx.github.io/FoMER-Bench/

---

## 💡 一句话要点

**提出FoMER基准，评估具身环境中基础模型逐步推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能` `大型多模态模型` `推理能力评估` `机器人` `基准测试` `物理约束` `安全推理`

## 📋 核心要点

1. 现有LMMs在具身任务中进行结构化推理的能力有待探索，尤其是在安全性和空间连贯性方面。
2. 提出FoMER基准，包含多种具身任务，旨在评估LMMs在复杂环境下的逐步推理能力。
3. 通过实验分析了多个LMMs在FoMER基准上的表现，揭示了它们的潜力和局限性，为未来研究指明方向。

## 📝 摘要（中文）

具身智能体在物理世界中操作时，必须做出有效、安全、空间连贯且基于上下文的决策。尽管大型多模态模型(LMMs)在视觉理解和语言生成方面取得了显著进展，但它们在现实世界具身任务中执行结构化推理的能力仍未得到充分探索。本文旨在了解基础模型在具身环境中执行逐步推理的能力。为此，我们提出了基础模型具身推理(FoMER)基准，旨在评估LMMs在复杂具身决策场景中的推理能力。我们的基准涵盖了一系列不同的任务，这些任务要求智能体解释多模态观察，推理物理约束和安全性，并以自然语言生成有效的下一步动作。我们提出了(i)一个大规模、精心策划的具身推理任务套件，(ii)一种新颖的评估框架，将感知基础与动作推理分离，以及(iii)在这种设置下对几种领先LMMs的实证分析。我们的基准包括超过1.1k个样本，涵盖10个任务和8个具身，涉及三种不同的机器人类型。我们的结果突出了LMMs在具身推理中的潜力和当前局限性，指出了机器人智能未来研究的关键挑战和机遇。我们的数据和代码将公开提供。

## 🔬 方法详解

**问题定义**：论文旨在解决大型多模态模型（LMMs）在具身环境中进行逐步推理能力评估的问题。现有方法难以有效评估LMMs在物理约束、安全性和空间连贯性等方面的推理能力，缺乏一个全面且细粒度的评估基准。

**核心思路**：论文的核心思路是构建一个专门用于评估LMMs在具身环境中推理能力的基准测试集FoMER。通过设计一系列需要智能体理解多模态信息、推理物理规则并生成合理动作的任务，来考察LMMs的推理能力。这种方法能够更全面地评估LMMs在实际应用中的潜力。

**技术框架**：FoMER基准包含以下几个关键组成部分：1) 大规模的具身推理任务套件，涵盖10个任务和8个具身，涉及三种不同的机器人类型；2) 新颖的评估框架，将感知基础与动作推理分离，以便更精确地评估LMMs的推理能力；3) 详细的步骤级推理数据，包含超过1.1k个样本。整体流程是，LMMs接收多模态输入（例如图像、文本），然后生成下一步动作的自然语言描述，最后通过评估框架判断动作的合理性。

**关键创新**：该论文的关键创新在于提出了FoMER基准，这是一个专门为评估LMMs在具身环境中推理能力而设计的基准。与现有方法相比，FoMER更加关注物理约束、安全性和空间连贯性等因素，能够更全面地评估LMMs在实际应用中的潜力。此外，评估框架将感知基础与动作推理分离，从而可以更精确地评估LMMs的推理能力。

**关键设计**：FoMER基准中的任务设计涵盖了多种不同的场景和挑战，例如导航、操作、规划等。每个任务都包含详细的步骤级推理数据，可以用于训练和评估LMMs。评估框架采用多种指标来衡量LMMs的性能，包括动作的正确性、安全性、空间连贯性等。具体参数设置和网络结构的选择取决于所使用的LMMs。

## 📊 实验亮点

实验结果表明，现有的LMMs在FoMER基准上表现出一定的推理能力，但仍存在局限性，尤其是在处理复杂的物理约束和安全问题时。该研究揭示了LMMs在具身推理方面的潜力，并指出了未来研究的关键方向，例如如何提高LMMs对物理世界的理解和推理能力。

## 🎯 应用场景

该研究成果可应用于机器人导航、智能家居、自动驾驶等领域。通过提升LMMs在具身环境中的推理能力，可以使机器人更好地理解环境、做出合理的决策，从而实现更安全、更高效的人机协作。未来，该研究有望推动机器人智能的发展，使其在更多实际场景中发挥作用。

## 📄 摘要（原文）

> Embodied agents operating in the physical world must make decisions that are not only effective but also safe, spatially coherent, and grounded in context. While recent advances in large multimodal models (LMMs) have shown promising capabilities in visual understanding and language generation, their ability to perform structured reasoning for real-world embodied tasks remains underexplored. In this work, we aim to understand how well foundation models can perform step-by-step reasoning in embodied environments. To this end, we propose the Foundation Model Embodied Reasoning (FoMER) benchmark, designed to evaluate the reasoning capabilities of LMMs in complex embodied decision-making scenarios. Our benchmark spans a diverse set of tasks that require agents to interpret multimodal observations, reason about physical constraints and safety, and generate valid next actions in natural language. We present (i) a large-scale, curated suite of embodied reasoning tasks, (ii) a novel evaluation framework that disentangles perceptual grounding from action reasoning, and (iii) empirical analysis of several leading LMMs under this setting. Our benchmark includes over 1.1k samples with detailed step-by-step reasoning across 10 tasks and 8 embodiments, covering three different robot types. Our results highlight both the potential and current limitations of LMMs in embodied reasoning, pointing towards key challenges and opportunities for future research in robot intelligence. Our data and code will be made publicly available.

