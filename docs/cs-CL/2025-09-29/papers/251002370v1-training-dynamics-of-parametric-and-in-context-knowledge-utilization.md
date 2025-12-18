---
layout: default
title: Training Dynamics of Parametric and In-Context Knowledge Utilization in Language Models
---

# Training Dynamics of Parametric and In-Context Knowledge Utilization in Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02370" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02370v1</a>
  <a href="https://arxiv.org/pdf/2510.02370.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02370v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.02370v1', 'Training Dynamics of Parametric and In-Context Knowledge Utilization in Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Minsung Kim, Dong-Kyum Kim, Jea Kwon, Nakyeong Yang, Kyomin Jung, Meeyoung Cha

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-29

**备注**: 16 pages

---

## 💡 一句话要点

**研究训练条件对语言模型参数化知识和上下文知识利用的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `知识仲裁` `上下文学习` `参数化知识` `检索增强生成`

## 📋 核心要点

1. 现有语言模型在利用上下文知识和参数化知识时存在冲突，缺乏对训练过程中知识仲裁策略的系统理解。
2. 该研究通过控制训练条件，研究了其对模型利用上下文知识和参数化知识的影响，以及模型如何在两者之间进行仲裁。
3. 实验表明，文档内事实重复和包含不一致信息的语料库训练，有助于模型发展更强大的知识仲裁策略。

## 📝 摘要（中文）

大型语言模型在推理时经常遇到上下文检索知识与预训练期间获得的参数化知识之间的冲突。盲目接受外部知识的模型容易受到错误信息的影响，而严格遵守参数化知识的模型则无法从检索中获益。尽管检索增强生成已被广泛采用，但我们仍然缺乏对训练过程中知识仲裁策略形成因素的系统理解。这种差距可能导致预训练模型具有不良的仲裁行为，从而浪费大量的计算资源。为了解决这个问题，我们首次对训练条件如何影响模型对上下文知识和参数化知识的利用以及它们如何在两者之间进行仲裁进行了受控研究。我们在一个合成的传记语料库上训练基于Transformer的语言模型，同时系统地控制各种条件。我们的实验表明，文档内事实的重复促进了参数化和上下文能力的发展。此外，在包含不一致信息或分布偏差的语料库上进行训练，鼓励模型开发利用参数化和上下文知识的强大策略。我们的结果表明，这些非理想属性对于学习鲁棒的仲裁至关重要，而不是将其视为需要消除的伪影。这些见解为预训练模型提供了具体的经验指导，使其能够和谐地整合参数化和上下文知识。

## 🔬 方法详解

**问题定义**：大型语言模型在推理时，如何有效地利用从上下文中检索到的知识，并与预训练过程中获得的参数化知识进行融合和仲裁，是一个关键问题。现有方法往往缺乏对训练过程如何影响这种知识仲裁策略的系统性理解，导致模型可能过度依赖某一种知识来源，从而影响模型的性能和可靠性。

**核心思路**：该论文的核心思路是通过构建一个可控的实验环境，系统性地研究不同的训练条件如何影响模型对上下文知识和参数化知识的利用。通过分析模型在不同训练条件下的行为，揭示影响知识仲裁策略的关键因素，并为预训练模型的优化提供指导。

**技术框架**：该研究采用基于Transformer的语言模型，并在一个合成的传记语料库上进行训练。该语料库包含可控的事实重复、不一致信息和分布偏差等特征，用于模拟不同的训练条件。通过控制这些条件，研究人员可以观察模型在利用上下文知识和参数化知识时的行为变化。

**关键创新**：该研究的创新之处在于，它首次对训练条件如何影响语言模型的知识仲裁策略进行了系统性的研究。通过构建可控的实验环境，揭示了文档内事实重复和包含不一致信息的语料库训练对模型知识仲裁能力的重要作用。

**关键设计**：实验中，研究人员精心设计了合成传记语料库，控制了事实重复的频率、不一致信息的比例以及数据分布的偏差程度。此外，他们还设计了相应的评估指标，用于衡量模型对上下文知识和参数化知识的利用程度，以及模型在两者之间进行仲裁的能力。具体的参数设置和网络结构与标准的Transformer模型保持一致，重点在于训练数据的设计和分析。

## 📊 实验亮点

实验结果表明，文档内事实的重复促进了参数化和上下文能力的发展。此外，在包含不一致信息或分布偏差的语料库上进行训练，鼓励模型开发利用参数化和上下文知识的强大策略。这些结果表明，非理想的训练数据对于学习鲁棒的知识仲裁至关重要。

## 🎯 应用场景

该研究成果可应用于预训练语言模型的优化，使其能够更好地利用上下文知识和参数化知识，提高模型在各种下游任务中的性能和可靠性。例如，可以用于改进检索增强生成模型，使其能够更有效地利用检索到的信息，并避免受到错误信息的影响。此外，该研究还可以为构建更鲁棒、更可信的AI系统提供指导。

## 📄 摘要（原文）

> Large language models often encounter conflicts between in-context knowledge retrieved at inference time and parametric knowledge acquired during pretraining. Models that accept external knowledge uncritically are vulnerable to misinformation, whereas models that adhere rigidly to parametric knowledge fail to benefit from retrieval. Despite the widespread adoption of retrieval-augmented generation, we still lack a systematic understanding of what shapes knowledge-arbitration strategies during training. This gap risks producing pretrained models with undesirable arbitration behaviors and, consequently, wasting substantial computational resources after the pretraining budget has already been spent. To address this problem, we present the first controlled study of how training conditions influence models' use of in-context and parametric knowledge, and how they arbitrate between them. We train transformer-based language models on a synthetic biographies corpus while systematically controlling various conditions. Our experiments reveal that intra-document repetition of facts fosters the development of both parametric and in-context capabilities. Moreover, training on a corpus that contains inconsistent information or distributional skew encourages models to develop robust strategies for leveraging parametric and in-context knowledge. Rather than viewing these non-ideal properties as artifacts to remove, our results indicate that they are important for learning robust arbitration. These insights offer concrete, empirical guidance for pretraining models that harmoniously integrate parametric and in-context knowledge.

