---
layout: default
title: Training Large Language Models To Reason In Parallel With Global Forking Tokens
---

# Training Large Language Models To Reason In Parallel With Global Forking Tokens

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.05132" class="toolbar-btn" target="_blank">📄 arXiv: 2510.05132v2</a>
  <a href="https://arxiv.org/pdf/2510.05132.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.05132v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.05132v2', 'Training Large Language Models To Reason In Parallel With Global Forking Tokens')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sheng Jia, Xiao Wang, Shiva Prasad Kasiviswanathan

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-10-01 (更新: 2025-11-06)

---

## 💡 一句话要点

**提出SSFT方法，通过全局Forking Tokens训练LLM进行并行推理，提升复杂问题求解能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `并行推理` `监督微调` `集合预测` `全局Forking Tokens`

## 📋 核心要点

1. 现有方法在鼓励LLM进行多样化推理时，难以兼顾推理的准确性，尤其是在复杂问题中。
2. 论文提出Set Supervised Fine-Tuning (SSFT) 方法，将并行推理视为集合预测问题，并引入全局损失。
3. 实验表明，SSFT方法能够保留独特的推理模式，并产生全局forking tokens，在推理基准测试中优于SFT。

## 📝 摘要（中文）

大型语言模型（LLM）通过扩展并行测试时计算能力来提升性能，但这依赖于生成既多样又准确的推理路径。对于复杂问题，触发多样且正确推理模式的forking tokens通常位于采样树的深处。因此，诸如温度缩放等鼓励多样性的常用策略会加剧多样性和准确性之间的权衡。为了解决这一挑战，我们将并行推理视为一个集合的下一个token预测问题，并使用全局forking tokens和唯一推理轨迹之间的自监督二分匹配，将基于集合的全局损失纳入到监督微调（SFT）中。我们观察到，使用多个推理轨迹进行朴素微调会使这些独特的推理模式崩溃，而我们提出的方法，集合监督微调（SSFT），保留了这些模式并产生了新兴的全局forking tokens。在多个推理基准上的实验表明，我们的SSFT在Pass@1和Cons@k指标下始终优于SFT。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在复杂推理任务中，并行推理时多样性和准确性难以兼顾的问题。现有方法，如温度缩放，虽然可以增加推理路径的多样性，但往往会降低推理的准确性，导致性能下降。这是因为触发多样且正确推理模式的forking tokens通常位于采样树的深处，简单的多样性鼓励策略难以有效捕捉这些关键token。

**核心思路**：论文的核心思路是将并行推理过程视为一个集合预测问题，即预测一组可能的下一个token（forking tokens）。通过引入基于集合的全局损失，鼓励模型学习到能够触发多样且正确的推理路径的forking tokens。这种方法旨在克服传统方法中多样性和准确性之间的权衡，从而提升LLM在复杂推理任务中的性能。

**技术框架**：SSFT方法在标准的监督微调（SFT）框架之上进行改进。主要包含以下几个阶段：1) 使用LLM生成多个推理轨迹；2) 定义全局forking tokens，这些tokens代表了不同推理路径的分叉点；3) 使用自监督二分匹配算法，将全局forking tokens与唯一的推理轨迹进行匹配；4) 将基于集合的全局损失函数加入到SFT的损失函数中，对模型进行微调。

**关键创新**：论文最重要的技术创新点在于引入了基于集合的全局损失函数，并将其应用于LLM的微调过程中。这种方法能够有效地学习到全局forking tokens，从而保留了独特的推理模式，并提升了并行推理的多样性和准确性。与现有方法相比，SSFT方法能够更好地平衡多样性和准确性之间的权衡，从而在复杂推理任务中取得更好的性能。

**关键设计**：SSFT的关键设计包括：1) 全局forking tokens的定义，需要根据具体的推理任务进行选择；2) 自监督二分匹配算法的选择，需要保证匹配的准确性和效率；3) 基于集合的全局损失函数的选择，需要能够有效地衡量预测的forking tokens与真实推理轨迹之间的差异。论文中具体使用的损失函数和匹配算法的具体细节未知。

## 📊 实验亮点

实验结果表明，SSFT方法在多个推理基准测试中始终优于SFT方法，在Pass@1和Cons@k指标上均取得了显著提升。这表明SSFT方法能够有效地保留独特的推理模式，并产生全局forking tokens，从而提升了LLM的并行推理能力。具体的性能提升幅度未知。

## 🎯 应用场景

该研究成果可应用于需要复杂推理能力的各种场景，例如：自动定理证明、代码生成、问题求解、对话系统等。通过提升LLM的并行推理能力，可以显著提高这些应用场景的性能和效率。此外，该方法还可以用于提升LLM的鲁棒性和泛化能力，使其能够更好地适应不同的任务和环境。

## 📄 摘要（原文）

> Although LLMs have demonstrated improved performance by scaling parallel test-time compute, doing so relies on generating reasoning paths that are both diverse and accurate. For challenging problems, the forking tokens that trigger diverse yet correct reasoning modes are typically deep in the sampling tree. Consequently, common strategies to encourage diversity, such as temperature scaling, encounter a worsened trade-off between diversity and accuracy. Motivated by this challenge, we treat parallel reasoning as a set-of-next-token-prediction problem, and incorporate a set-based global loss into Supervised Fine-Tuning (SFT) using self-supervised bipartite matching between our global forking tokens and unique reasoning traces. We observe that, while naive fine-tuning with multiple reasoning traces collapses these unique reasoning modes, our proposed method, Set Supervised Fine-Tuning (SSFT), preserves these modes and produces emergent global forking tokens. Experiments on multiple reasoning benchmarks show that our SSFT consistently outperforms SFT under both Pass@1 and Cons@k metrics.

