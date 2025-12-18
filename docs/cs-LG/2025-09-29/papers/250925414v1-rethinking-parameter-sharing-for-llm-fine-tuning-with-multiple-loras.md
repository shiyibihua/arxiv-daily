---
layout: default
title: Rethinking Parameter Sharing for LLM Fine-Tuning with Multiple LoRAs
---

# Rethinking Parameter Sharing for LLM Fine-Tuning with Multiple LoRAs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25414" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25414v1</a>
  <a href="https://arxiv.org/pdf/2509.25414.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25414v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25414v1', 'Rethinking Parameter Sharing for LLM Fine-Tuning with Multiple LoRAs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Ban, Kaiyi Ji

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-09-29

**🔗 代码/项目**: [GITHUB](https://github.com/OptMN-Lab/ALoRA)

---

## 💡 一句话要点

**提出ALoRA：一种非对称多LoRA微调方法，提升LLM多任务和联邦学习性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `参数高效微调` `多LoRA` `多任务学习` `联邦学习` `大型语言模型` `知识迁移` `非对称结构`

## 📋 核心要点

1. 现有方法在多LoRA微调中，对LoRA的A矩阵进行共享，但忽略了B矩阵的作用，导致知识编码和迁移效率降低。
2. ALoRA的核心思想是共享LoRA的B矩阵，并为每个任务保留独立的A矩阵，从而实现更有效的知识编码和任务特定适配。
3. 实验结果表明，ALoRA在多任务和联邦学习场景下，相比现有方法，实现了更平衡的任务性能和更高的平均准确率。

## 📝 摘要（中文）

大型语言模型通常使用低秩适应(LoRA)等参数高效技术进行适配，其公式为$y = W_0x + BAx$，其中$W_0$是预训练参数，$x$是适配层的输入。多适配器扩展通常采用多个LoRA，但先前的研究表明，内部矩阵$A$在训练过程中高度相似，因此适合共享。我们重新审视了这种现象，发现这种相似性主要归因于相同的初始化，而不是共享知识，$B$在知识编码和转移中起着更关键的作用。受这些见解的启发，我们提出	extbf{ALoRA}，一种非对称多LoRA设计，在多任务微调中具有多个$A$矩阵和一个共享的$B$，以及	extbf{Fed-ALoRA}，它通过一种新颖的矩阵分解策略，在同构和异构设置下的联邦微调中跨客户端共享$B$，以适应跨客户端的异构秩。在常识推理、数学推理、多任务NLP数据集和联邦NLP数据集上的实验表明，相对于现有的多LoRA方法，我们的方法在任务之间实现了更平衡的性能，并具有可比或更高的平均准确率。代码可在https://github.com/OptMN-Lab/ALoRA获取。

## 🔬 方法详解

**问题定义**：现有基于多LoRA的参数高效微调方法，在多任务或联邦学习场景下，通常假设LoRA的A矩阵包含任务特定的信息，而B矩阵可以共享。然而，论文指出A矩阵的相似性更多源于初始化，而忽略了B矩阵在知识编码和迁移中的重要作用。这导致模型在不同任务上的性能不平衡，且整体性能提升有限。

**核心思路**：论文的核心思路是重新审视LoRA中A和B矩阵的作用，并提出一种非对称的多LoRA结构ALoRA。ALoRA的关键在于共享B矩阵，并为每个任务维护独立的A矩阵。这种设计允许B矩阵捕获通用的知识表示，而A矩阵则负责任务特定的适配。

**技术框架**：ALoRA的整体框架基于LoRA，但修改了参数共享策略。在多任务微调中，每个任务都有一个独立的A矩阵，但共享同一个B矩阵。在联邦学习场景下，提出了Fed-ALoRA，通过矩阵分解策略，允许客户端拥有不同秩的LoRA，并共享分解后的B矩阵。

**关键创新**：ALoRA的关键创新在于非对称的LoRA结构，即共享B矩阵并保持A矩阵的独立性。这种设计更符合LoRA中A和B矩阵的实际作用，能够更有效地进行知识编码和任务特定适配。Fed-ALoRA通过矩阵分解，实现了在异构联邦学习场景下共享B矩阵，进一步提升了模型的泛化能力。

**关键设计**：ALoRA的关键设计包括：1) 共享的B矩阵，用于捕获通用知识；2) 独立的A矩阵，用于任务特定适配；3) 在Fed-ALoRA中，使用矩阵分解技术来适应不同客户端的LoRA秩，并共享分解后的B矩阵。损失函数与标准LoRA微调相同，通常使用交叉熵损失。

## 📊 实验亮点

实验结果表明，ALoRA在常识推理、数学推理、多任务NLP数据集和联邦NLP数据集上均取得了显著的性能提升。例如，在多任务NLP数据集上，ALoRA相比现有方法，实现了更平衡的任务性能和更高的平均准确率。在联邦学习场景下，Fed-ALoRA在异构数据分布下，依然能够保持较高的模型性能。

## 🎯 应用场景

ALoRA具有广泛的应用前景，包括多任务学习、联邦学习、个性化推荐、自然语言处理等领域。它可以应用于各种需要对大型语言模型进行高效微调的场景，例如，在医疗领域，可以使用ALoRA对不同疾病的诊断模型进行微调，并共享通用的医学知识。

## 📄 摘要（原文）

> Large language models are often adapted using parameter-efficient techniques such as Low-Rank Adaptation (LoRA), formulated as $y = W_0x + BAx$, where $W_0$ is the pre-trained parameters and $x$ is the input to the adapted layer. While multi-adapter extensions often employ multiple LoRAs, prior studies suggest that the inner $A$ matrices are highly similar during training and thus suitable for sharing. We revisit this phenomenon and find that this similarity is largely attributable to the identical initialization rather than shared knowledge, with $B$ playing a more critical role in knowledge encoding and transfer. Motivated by these insights, we propose \textbf{ALoRA}, an asymmetric multi-LoRA design with multiple $A$ matrices and a single shared $B$ in multi-task fine-tuning, and \textbf{Fed-ALoRA}, which shares $B$ across clients in federated fine-tuning under both homogeneous and heterogeneous settings, through a novel matrix decomposition strategy to accommodate heterogeneous ranks across clients. Experiments on commonsense reasoning, math reasoning, multi-task NLP dataset, and federated NLP dataset demonstrate that our methods achieve more balanced performance across tasks with comparable or superior average accuracy relative to existing multi-LoRA approaches. Codes are available at https://github.com/OptMN-Lab/ALoRA.

