---
layout: default
title: Large Language Models as Nondeterministic Causal Models
---

# Large Language Models as Nondeterministic Causal Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22297" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22297v1</a>
  <a href="https://arxiv.org/pdf/2509.22297.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22297v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22297v1', 'Large Language Models as Nondeterministic Causal Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sander Beckers

**分类**: cs.AI

**发布日期**: 2025-09-26

**备注**: Preprint: under review

---

## 💡 一句话要点

**提出基于非确定性因果模型的大语言模型反事实生成方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `反事实生成` `因果模型` `非确定性` `解释性` `黑盒模型`

## 📋 核心要点

1. 现有LLM反事实生成方法对LLM的解释存在歧义，未能充分体现LLM的非确定性本质。
2. 论文提出一种更简单的反事实生成方法，将LLM视为非确定性因果模型，更符合LLM的预期语义。
3. 新方法可直接应用于任何黑盒LLM，无需修改，且为特定应用的反事实生成奠定理论基础。

## 📝 摘要（中文）

Chatzi等人和Ravfogel等人最近的工作首次开发了一种生成概率大语言模型反事实的方法。这些反事实告诉我们，如果某个实际提示${f x}$变为${f x}^*$，LLM的输出将会是什么或可能是什么。生成此类反事实的能力是解释、评估和比较LLM行为的重要必要步骤。然而，我认为现有方法对LLM的解释存在歧义：它没有从字面上解释LLM，因为它假设可以改变LLM采样过程的实现而不改变LLM本身；它也没有按照预期解释LLM，因为它明确地将非确定性LLM表示为确定性因果模型。我在这里提出了一种更简单的生成反事实的方法，该方法基于LLM的预期解释，将其表示为非确定性因果模型。我的更简单方法的优点是它可以直接应用于任何黑盒LLM而无需修改，因为它与任何实现细节无关。另一方面，现有方法的优点是它直接实现了特定类型反事实的生成，这种反事实对于某些目的有用，但对于其他目的则不然。我通过提供一个基于LLM预期语义的推理反事实的理论基础来阐明这两种方法之间的关系，从而为生成反事实的新型特定应用方法奠定基础。

## 🔬 方法详解

**问题定义**：现有方法在生成LLM的反事实时，要么假设可以改变LLM的实现细节而不改变LLM本身，要么将非确定性的LLM表示为确定性的因果模型，这两种方式都未能准确反映LLM的本质特性，导致反事实生成结果可能存在偏差。现有方法依赖于对LLM内部机制的假设，限制了其通用性和适用性。

**核心思路**：论文的核心思路是将LLM视为一个非确定性的因果模型。这意味着LLM的输出不仅仅由输入决定，还受到内在随机性的影响。通过直接对这种非确定性进行建模，可以更准确地生成反事实，从而更好地理解LLM的行为。这种方法避免了对LLM内部实现的假设，使其更具通用性。

**技术框架**：该方法的核心在于将LLM视为一个黑盒，并通过对其输入和输出进行观察来推断其因果关系。具体流程包括：1) 给定一个输入提示；2) LLM生成一个输出；3) 对输入提示进行反事实修改；4) LLM生成新的输出；5) 分析两个输出之间的差异，从而理解输入修改对输出的影响。整个过程无需访问LLM的内部参数或结构。

**关键创新**：最重要的创新点在于将LLM视为非确定性因果模型，并基于此提出了一种简单且通用的反事实生成方法。与现有方法相比，该方法不需要对LLM的内部实现进行假设，因此可以应用于任何黑盒LLM。此外，该方法为基于LLM预期语义的反事实推理提供了理论基础，为开发特定应用的反事实生成方法奠定了基础。

**关键设计**：由于该方法将LLM视为黑盒，因此不需要特定的参数设置或网络结构。关键在于如何设计反事实修改，以及如何分析修改后的输出与原始输出之间的差异。具体的设计取决于具体的应用场景和需要分析的因果关系。例如，可以采用不同的反事实修改策略，如词语替换、句子删除等，并使用不同的指标来衡量输出的差异，如BLEU score、ROUGE score等。

## 📊 实验亮点

论文提出了一种更简单、更通用的反事实生成方法，无需修改即可应用于任何黑盒LLM。该方法基于LLM的预期语义，将其表示为非确定性因果模型，避免了对LLM内部实现的假设。虽然论文没有提供具体的性能数据，但强调了该方法为特定应用的反事实生成奠定了理论基础，并具有广泛的应用前景。

## 🎯 应用场景

该研究成果可应用于LLM的解释性分析、安全性评估和公平性改进。通过生成反事实，可以理解LLM在不同输入下的行为，发现潜在的偏见和漏洞，并针对性地进行改进。此外，该方法还可以用于比较不同LLM的性能和行为差异，为LLM的选型和优化提供依据。未来，该方法有望应用于更广泛的自然语言处理任务，如文本生成、机器翻译等。

## 📄 摘要（原文）

> Recent work by Chatzi et al. and Ravfogel et al. has developed, for the first time, a method for generating counterfactuals of probabilistic Large Language Models. Such counterfactuals tell us what would - or might - have been the output of an LLM if some factual prompt ${\bf x}$ had been ${\bf x}^*$ instead. The ability to generate such counterfactuals is an important necessary step towards explaining, evaluating, and comparing, the behavior of LLMs. I argue, however, that the existing method rests on an ambiguous interpretation of LLMs: it does not interpret LLMs literally, for the method involves the assumption that one can change the implementation of an LLM's sampling process without changing the LLM itself, nor does it interpret LLMs as intended, for the method involves explicitly representing a nondeterministic LLM as a deterministic causal model. I here present a much simpler method for generating counterfactuals that is based on an LLM's intended interpretation by representing it as a nondeterministic causal model instead. The advantage of my simpler method is that it is directly applicable to any black-box LLM without modification, as it is agnostic to any implementation details. The advantage of the existing method, on the other hand, is that it directly implements the generation of a specific type of counterfactuals that is useful for certain purposes, but not for others. I clarify how both methods relate by offering a theoretical foundation for reasoning about counterfactuals in LLMs based on their intended semantics, thereby laying the groundwork for novel application-specific methods for generating counterfactuals.

