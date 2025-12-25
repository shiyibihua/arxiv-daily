---
layout: default
title: Model Merging via Multi-Teacher Knowledge Distillation
---

# Model Merging via Multi-Teacher Knowledge Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21288" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21288v1</a>
  <a href="https://arxiv.org/pdf/2512.21288.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21288v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21288v1', 'Model Merging via Multi-Teacher Knowledge Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seyed Arshan Dalili, Mehrdad Mahdavi

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-24

**🔗 代码/项目**: [GITHUB](https://github.com/arshandalili/SAMerging)

---

## 💡 一句话要点

**提出SAMerging，通过多教师知识蒸馏实现模型合并，提升泛化性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `模型合并` `知识蒸馏` `多任务学习` `泛化能力` `PAC-Bayes` `Sharpness-Aware Minimization` `深度学习` `模型优化`

## 📋 核心要点

1. 现有模型合并方法依赖启发式参数组合，缺乏理论指导，导致性能不稳定且对初始化敏感。
2. 论文将模型合并视为多教师知识蒸馏，通过最小化KL散度来优化合并模型，并推导出泛化误差上界。
3. 提出的SAMerging方法利用Sharpness-Aware Minimization寻找平坦最小值，在视觉和NLP任务上取得SOTA性能。

## 📝 摘要（中文）

模型合并是联合多任务学习的一种轻量级替代方案，但合并模型的泛化特性在很大程度上仍未被探索。建立此类理论保证并非易事，因为合并过程通常禁止访问原始训练数据，并且涉及组合在根本上异构的数据分布上微调的模型。由于缺乏对这些动态的原则性理解，当前的方法通常依赖于启发式方法来近似参数的最佳组合。这种依赖在系数缩放中最为关键，系数缩放调节每个微调模型对共享参数的贡献程度。然而，在没有原则性目标来指导其选择的情况下，这些方法会导致脆弱的性能，并且对缩放初始化高度敏感。我们通过以下方式解决这一差距：(i) 专门为模型合并设置建立一种新颖的、感知平坦度的PAC-Bayes泛化界限。该分析引入了一个“跨任务异质性”项，该项正式捕获了各种微调模型先验与目标多任务分布之间的不匹配。(ii) 在此理论见解的指导下，我们将模型合并定义为在稀缺的未标记数据上的多教师知识蒸馏。我们正式证明，最小化学生-教师Kullback-Leibler散度可以直接收紧合并模型超额风险的上限。在导出的感知平坦度的界限的指导下，(iii) 我们通过SAMerging来实现这一目标，SAMerging采用Sharpness-Aware Minimization (SAM) 来寻找平坦最小值。在经验上，SAMerging在视觉和NLP基准测试中建立了新的最先进水平，取得了显著的性能。代码可在https://github.com/arshandalili/SAMerging获得。

## 🔬 方法详解

**问题定义**：模型合并旨在将多个在不同任务上微调的模型合并为一个模型，以实现多任务学习的目的。现有方法通常依赖于启发式方法来确定每个模型的权重，缺乏理论指导，导致合并后的模型性能不稳定，并且对权重初始化非常敏感。尤其是在无法访问原始训练数据的情况下，如何有效地合并模型是一个挑战。

**核心思路**：论文的核心思路是将模型合并问题转化为多教师知识蒸馏问题。通过将多个微调后的模型视为教师模型，利用少量未标记数据进行知识蒸馏，训练出一个学生模型作为合并后的模型。这种方法能够利用教师模型的知识，同时避免了直接操作模型参数的复杂性。

**技术框架**：SAMerging的整体框架包括以下几个步骤：1) 对多个模型在各自的任务上进行微调。2) 利用少量未标记数据，将微调后的模型作为教师模型，训练一个学生模型。3) 在训练过程中，最小化学生模型和教师模型之间的Kullback-Leibler (KL) 散度，以保证学生模型能够学习到教师模型的知识。4) 使用Sharpness-Aware Minimization (SAM) 优化学生模型，寻找平坦最小值，提高模型的泛化能力。

**关键创新**：论文的关键创新在于：1) 将模型合并问题转化为多教师知识蒸馏问题，为模型合并提供了一种新的视角。2) 提出了一个专门针对模型合并场景的、感知平坦度的PAC-Bayes泛化界限，为模型合并的理论分析提供了基础。3) 将Sharpness-Aware Minimization (SAM) 应用于模型合并，通过寻找平坦最小值来提高模型的泛化能力。

**关键设计**：SAMerging的关键设计包括：1) 使用KL散度作为学生模型和教师模型之间的损失函数，以保证学生模型能够学习到教师模型的知识。2) 使用Sharpness-Aware Minimization (SAM) 优化学生模型，SAM通过寻找参数空间中loss值变化不敏感的区域，来提高模型的泛化能力。具体来说，SAM首先在当前参数附近寻找一个扰动，使得loss值增加最多，然后沿着loss增加的反方向更新参数。3) 论文中提出的“跨任务异质性”项，用于衡量不同任务之间的差异，并在PAC-Bayes泛化界限中发挥作用。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21288v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21288v1/arxiv/plots_to_use/eurosat_vs_sun397__samerging_vs_adamerging_8.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21288v1/arxiv/plots_to_use/eurosat_vs_sun397_comparison.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SAMerging在多个视觉和NLP基准测试中取得了显著的性能提升，建立了新的SOTA。具体性能数据在论文中给出，相较于之前的模型合并方法，SAMerging在多个任务上都取得了明显的性能提升，验证了该方法的有效性。实验结果表明，SAMerging能够有效地利用多个模型的知识，并提高模型的泛化能力。

## 🎯 应用场景

该研究成果可应用于各种需要模型合并的场景，例如多任务学习、联邦学习和持续学习。通过SAMerging，可以有效地将多个在不同任务上训练的模型合并为一个高性能模型，从而降低模型部署和维护的成本，并提高模型的泛化能力。该方法在计算机视觉、自然语言处理等领域具有广泛的应用前景。

## 📄 摘要（原文）

> Model merging has emerged as a lightweight alternative to joint multi-task learning (MTL), yet the generalization properties of merged models remain largely unexplored. Establishing such theoretical guarantees is non-trivial, as the merging process typically forbids access to the original training data and involves combining fine-tuned models trained on fundamentally heterogeneous data distributions. Without a principled understanding of these dynamics, current methods often rely on heuristics to approximate the optimal combination of parameters. This dependence is most critical in coefficient scaling, the weighting factors that modulate the magnitude of each fine-tuned model's contribution to the shared parameter. However, without a principled objective to guide their selection, these methods lead to brittle performance and are highly sensitive to scaling initialization. We address this gap by (i) establishing a novel flatness-aware PAC-Bayes generalization bound specifically for the model merging setting. This analysis introduces a "cross-task heterogeneity" term that formally captures the mismatch between diverse fine-tuned model priors and the target multi-task distributions. Guided by this theoretical insight, (ii) we frame model merging as multi-teacher knowledge distillation on scarce, unlabeled data. We formally demonstrate that minimizing the student-teacher Kullback-Leibler divergence directly tightens the upper bound on the merged model's excess risk. Guided by the flatness-aware bound derived, (iii) we operationalize this objective via SAMerging, a method that employs Sharpness-Aware Minimization (SAM) to find flat minima. Empirically, SAMerging establishes a new state of the art across vision and NLP benchmarks, achieving remarkable performance. The code is available at https://github.com/arshandalili/SAMerging.

