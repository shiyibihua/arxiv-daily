---
layout: default
title: Mitigating Catastrophic Forgetting in Continual Learning through Model Growth
---

# Mitigating Catastrophic Forgetting in Continual Learning through Model Growth

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01213" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01213v1</a>
  <a href="https://arxiv.org/pdf/2509.01213.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01213v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01213v1', 'Mitigating Catastrophic Forgetting in Continual Learning through Model Growth')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ege Süalp, Mina Rezaei

**分类**: cs.CL

**发布日期**: 2025-09-01

---

## 💡 一句话要点

**通过模型增长缓解持续学习中的灾难性遗忘**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `持续学习` `灾难性遗忘` `模型增长` `大型语言模型` `知识保留`

## 📋 核心要点

1. 大型语言模型在持续学习中面临灾难性遗忘问题，即在新任务上微调后，模型会丢失先前学习的知识。
2. 论文提出利用模型增长策略，通过从小模型到大模型的训练方式，期望缓解灾难性遗忘问题，提升模型对先前知识的保留能力。
3. 实验结果表明，基于增长的模型在阅读理解方面表现出更强的知识保留能力，但在处理社会偏见方面存在权衡。

## 📝 摘要（中文）

灾难性遗忘是持续学习中的一个重大挑战，模型在新任务上进行微调时会丢失先前的知识。这个问题对于进行持续学习的大型语言模型（LLM）尤为关键，因为保持跨多个领域的能力对于其通用性至关重要。本文探讨了模型增长，这是一种有前景的策略，它利用较小的模型来加速和构建较大模型的训练，以缓解灾难性遗忘问题。虽然基于增长的预训练，特别是通过Transformer堆叠，已显示出加速收敛的潜力，但其对遗忘的影响仍未得到充分探索。因此，我们评估了基于增长的模型（Stack LLM）和未基于增长的模型（LLM）是否能更有效地保留先前学习的能力，跨越一系列涉及领域知识、推理、阅读理解和偏差的微调任务。我们的研究结果表明，两种模型在领域知识方面都有所提高。然而，推理和阅读理解随着时间的推移而退化，表明存在灾难性遗忘的迹象。Stack LLM始终表现出较小的退化，尤其是在阅读理解方面，表明其具有更强的保留能力。有趣的是，在偏差评估中，基线LLM随着持续微调而逐渐变得更加中性，而Stack LLM将偏差率稳定在60-61％左右。这些结果表明，基于增长的预训练可能在抵抗灾难性遗忘方面带来适度的改进，但在处理社会偏见方面仍然存在权衡。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在持续学习过程中遇到的灾难性遗忘问题。现有方法在应对新任务时，往往会显著降低模型在先前任务上的性能，导致知识的丢失。这种现象严重限制了LLM在需要持续学习和适应新知识的应用场景中的实用性。

**核心思路**：论文的核心思路是利用模型增长（Model Growth）策略。通过从小模型开始训练，逐步扩展到更大的模型，期望能够更好地组织和结构化知识的学习过程，从而提高模型对先前知识的保留能力。这种方法借鉴了Transformer堆叠等已有的增长式预训练方法，并将其应用于持续学习场景。

**技术框架**：论文采用了一种对比实验框架，比较了两种模型的性能：一种是基于增长训练的模型（Stack LLM），另一种是直接训练的大型语言模型（LLM）。两种模型都经过一系列微调任务，这些任务涵盖了领域知识、推理、阅读理解和偏差评估等多个方面。通过比较两种模型在这些任务上的性能变化，评估模型增长策略对缓解灾难性遗忘的影响。

**关键创新**：论文的关键创新在于将模型增长策略应用于持续学习的灾难性遗忘问题，并验证了其在一定程度上缓解该问题的有效性。虽然增长式预训练已被用于加速模型收敛，但其对持续学习中知识保留的影响尚未得到充分研究。该研究填补了这一空白，并为持续学习提供了一种新的思路。

**关键设计**：论文的关键设计包括：1) 选择了涵盖不同方面的微调任务，以全面评估模型的知识保留能力；2) 对比了基于增长训练的模型和直接训练的大型语言模型，以突出模型增长策略的效果；3) 关注了模型在社会偏见方面的表现，揭示了模型增长策略可能带来的潜在问题。

## 📊 实验亮点

实验结果表明，基于增长训练的模型（Stack LLM）在阅读理解任务中表现出更强的知识保留能力，相比于直接训练的大型语言模型（LLM），其性能退化程度更小。此外，研究还发现，Stack LLM在社会偏见方面表现出与LLM不同的行为，维持了相对稳定的偏差率。

## 🎯 应用场景

该研究成果可应用于需要持续学习和适应新知识的各种大型语言模型应用场景，例如智能客服、知识问答系统、机器翻译等。通过缓解灾难性遗忘，可以提高模型在不断变化的环境中的性能和可靠性，使其能够更好地服务于用户。

## 📄 摘要（原文）

> Catastrophic forgetting is a significant challenge in continual learning, in which a model loses prior knowledge when it is fine-tuned on new tasks. This problem is particularly critical for large language models (LLMs) undergoing continual learning, as retaining performance across diverse domains is important for their general utility. In this paper, we explore model growth, a promising strategy that leverages smaller models to expedite and structure the training of larger ones for mitigating the catastrophic forgetting problem. Although growth-based pretraining, particularly via transformer stacking, has shown promise in accelerating convergence, its impact on forgetting remains under-explored. Therefore, we evaluate whether growth-based models can retain previously learned capabilities more effectively across a sequence of fine-tuning tasks involving domain knowledge, reasoning, reading comprehension, and bias. Our findings show that both models -- one trained with growth (Stack LLM) and one without (LLM) -- exhibit improvements in domain knowledge. However, reasoning and reading comprehension degrade over time, indicating signs of catastrophic forgetting. Stack LLM consistently shows less degradation, especially in reading comprehension, suggesting enhanced retention capabilities. Interestingly, in bias evaluation, the baseline LLM becomes progressively more neutral with continued fine-tuning, while Stack LLM maintains a steady bias ratio around 60--61\%. These results indicate that growth-based pretraining may deliver modest improvements in resisting catastrophic forgetting, though trade-offs remain in handling social biases.

