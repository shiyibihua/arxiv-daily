---
layout: default
title: Large Language Models Are Zero-Shot Text Classifiers
---

# Large Language Models Are Zero-Shot Text Classifiers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.01044" class="toolbar-btn" target="_blank">📄 arXiv: 2312.01044v1</a>
  <a href="https://arxiv.org/pdf/2312.01044.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.01044v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.01044v1', 'Large Language Models Are Zero-Shot Text Classifiers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiqiang Wang, Yiran Pang, Yanbin Lin

**分类**: cs.CL

**发布日期**: 2023-12-02

**备注**: 9 pages, 3 figures, 6 tables

---

## 💡 一句话要点

**验证大型语言模型在零样本文本分类中的有效性，尤其适用于资源受限场景。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `零样本学习` `文本分类` `思维链提示` `GPT模型`

## 📋 核心要点

1. 文本分类面临计算成本高、耗时以及对未见类别泛化能力弱等挑战。
2. 利用思维链提示（CoT）和零样本学习，直接使用预训练LLMs进行文本分类。
3. 实验表明，LLMs在多个数据集上作为零样本文本分类器表现出色，尤其适合资源有限的场景。

## 📝 摘要（中文）

经过重新训练的大型语言模型（LLMs）已广泛应用于自然语言处理（NLP）的各个子领域。在NLP中，文本分类问题受到了相当大的关注，但仍然面临着计算成本高昂、耗时以及对未见类别的鲁棒性不足等限制。随着思维链提示（CoT）的提出，LLMs可以使用零样本学习（ZSL）以及逐步推理提示来实现，而不是传统的问答形式。零样本LLMs在文本分类问题中可以通过直接利用预训练模型来预测已见和未见类别，从而缓解这些限制。我们的研究主要验证了GPT模型在文本分类中的能力。我们专注于有效地利用提示策略来适应各种文本分类场景。此外，我们将零样本LLMs的性能与其他最先进的文本分类方法（包括传统机器学习方法、深度学习方法和ZSL方法）进行了比较。实验结果表明，在分析的四个数据集中，LLMs的性能突显了它们作为零样本文本分类器的有效性。这种能力对于可能没有广泛文本分类知识的小企业或团队尤其有利。

## 🔬 方法详解

**问题定义**：论文旨在解决文本分类任务中，传统方法计算成本高昂、耗时，且对未见类别泛化能力不足的问题。现有方法需要大量的标注数据进行训练，对于小企业或团队而言，获取和处理这些数据的成本很高。

**核心思路**：论文的核心思路是利用大型语言模型（LLMs）的强大zero-shot能力，通过思维链提示（CoT）引导模型进行推理，从而实现无需额外训练数据的文本分类。这种方法旨在降低计算成本和时间消耗，并提高对未见类别的泛化能力。

**技术框架**：该方法主要依赖于预训练的GPT模型。首先，设计合适的思维链提示（CoT），引导模型逐步推理文本的类别。然后，将文本和提示输入到GPT模型中，模型生成推理过程和最终的类别预测。最后，评估模型在不同数据集上的分类性能。

**关键创新**：关键创新在于将思维链提示（CoT）与零样本LLMs相结合，用于文本分类。与传统的直接问答形式不同，CoT提示允许模型逐步推理，从而提高分类的准确性和可解释性。此外，该方法无需针对特定数据集进行训练，降低了数据标注和模型训练的成本。

**关键设计**：论文的关键设计在于提示策略的设计。不同的提示策略会显著影响模型的性能。论文探索了多种提示策略，并比较了它们在不同数据集上的表现。此外，论文还研究了不同规模的GPT模型对分类性能的影响。具体的参数设置和网络结构沿用了GPT模型的默认设置，没有进行特别的修改。

## 📊 实验亮点

实验结果表明，LLMs在四个数据集中的三个上表现出作为零样本文本分类器的有效性。该方法在某些数据集上甚至可以与经过专门训练的传统机器学习和深度学习方法相媲美，尤其是在数据量较小的情况下，优势更加明显。这表明LLMs具有强大的zero-shot学习能力，可以有效地应用于文本分类任务。

## 🎯 应用场景

该研究成果可广泛应用于各种文本分类场景，如情感分析、主题分类、垃圾邮件检测等。尤其适用于资源有限的小企业或团队，他们可以利用预训练的LLMs快速构建文本分类系统，而无需投入大量资金和时间进行数据标注和模型训练。未来，该方法可以进一步扩展到其他自然语言处理任务，如文本摘要、机器翻译等。

## 📄 摘要（原文）

> Retrained large language models (LLMs) have become extensively used across various sub-disciplines of natural language processing (NLP). In NLP, text classification problems have garnered considerable focus, but still faced with some limitations related to expensive computational cost, time consumption, and robust performance to unseen classes. With the proposal of chain of thought prompting (CoT), LLMs can be implemented using zero-shot learning (ZSL) with the step by step reasoning prompts, instead of conventional question and answer formats. The zero-shot LLMs in the text classification problems can alleviate these limitations by directly utilizing pretrained models to predict both seen and unseen classes. Our research primarily validates the capability of GPT models in text classification. We focus on effectively utilizing prompt strategies to various text classification scenarios. Besides, we compare the performance of zero shot LLMs with other state of the art text classification methods, including traditional machine learning methods, deep learning methods, and ZSL methods. Experimental results demonstrate that the performance of LLMs underscores their effectiveness as zero-shot text classifiers in three of the four datasets analyzed. The proficiency is especially advantageous for small businesses or teams that may not have extensive knowledge in text classification.

