---
layout: default
title: Feature-Selective Representation Misdirection for Machine Unlearning
---

# Feature-Selective Representation Misdirection for Machine Unlearning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16297" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16297v1</a>
  <a href="https://arxiv.org/pdf/2512.16297.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16297v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16297v1', 'Feature-Selective Representation Misdirection for Machine Unlearning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Taozhao Chen, Linghan Huang, Kim-Kwang Raymond Choo, Huaming Chen

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出选择性表征误导(SRMU)框架，解决LLM中知识遗忘难题，兼顾安全与效用。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器遗忘` `大型语言模型` `知识移除` `表征学习` `激活编辑`

## 📋 核心要点

1. 现有机器遗忘方法在遗忘和保留数据集高度纠缠时表现不佳，容易导致模型效用下降或无法保证安全性。
2. SRMU通过激活编辑，有选择性地施加特征感知和方向控制的扰动，抑制有害表征，同时保留良性表征的效用。
3. 实验表明，SRMU在低、高纠缠配置下均表现出色，即使在20-30%的数据重叠下，仍优于现有方法，且效用损失最小。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在安全关键和受监管领域日益普及，模型中保留的敏感或禁止知识带来了不断升级的风险，包括隐私泄露、违反法规以及潜在的滥用等。近期的研究表明，机器遗忘技术有助于确保已部署的模型符合不断变化的法律、安全和治理要求。然而，现有的遗忘技术假设遗忘数据集和保留数据集之间存在清晰的分离，这在具有高度纠缠分布的实际操作环境中是具有挑战性的。在这种情况下，基于扰动的方法通常会降低模型的通用效用或无法确保安全性。为了解决这个问题，我们提出了一种用于遗忘的选择性表征误导（SRMU）方法，这是一种新颖的、有原则的激活编辑框架，它强制执行特征感知和方向控制的扰动。与不加区分的模型权重扰动不同，SRMU采用带有激活重要性图的结构化误导向量。目标是允许SRMU选择性地抑制有害表征，同时保持对良性表征的效用。在广泛使用的WMDP基准上，针对低纠缠和高纠缠配置进行了实验。实验结果表明，SRMU提供了最先进的遗忘性能，同时效用损失最小，并且在现有基线崩溃的20-30%重叠下仍然有效。SRMU为新兴的基于LLM的应用中的安全驱动模型治理、隐私合规性和受控知识移除提供了强大的基础。我们在https://figshare.com/s/d5931192a8824de26aff发布了复制包。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）中知识遗忘的问题，尤其是在遗忘数据和保留数据高度纠缠的情况下。现有基于扰动的遗忘方法，如直接修改模型权重，容易导致模型通用性能下降，或者无法有效移除有害知识，难以满足安全性和合规性要求。

**核心思路**：论文的核心思路是通过选择性地修改模型内部的激活表征，从而达到遗忘特定知识的目的。这种方法不是直接修改模型权重，而是通过在激活层引入有针对性的扰动，来“误导”模型的判断，使其不再输出与遗忘知识相关的内容。通过控制扰动的方向和强度，可以最大限度地减少对模型通用性能的影响。

**技术框架**：SRMU框架主要包含以下几个阶段：1) **激活重要性评估**：确定哪些激活对于模型输出特定知识最为重要。这可以通过梯度信息或其他方法来实现。2) **误导向量生成**：基于激活重要性，生成一个结构化的误导向量，该向量包含方向和强度信息，用于指导扰动的施加。3) **激活编辑**：将误导向量施加到模型的激活层，从而改变模型的内部表征。4) **模型微调（可选）**：在激活编辑后，可以对模型进行微调，以进一步提高其通用性能。

**关键创新**：SRMU的关键创新在于其选择性和方向控制的扰动机制。与传统的权重扰动方法不同，SRMU不是盲目地修改模型参数，而是有针对性地修改激活表征，并且可以控制扰动的方向，从而最大限度地减少对模型通用性能的影响。此外，SRMU还引入了激活重要性图，用于指导扰动的施加，从而进一步提高了遗忘的效率和准确性。

**关键设计**：SRMU的关键设计包括：1) **激活重要性评估方法**：可以使用梯度信息、注意力权重或其他方法来评估激活的重要性。2) **误导向量的生成方式**：误导向量的方向可以设置为与目标知识相关的激活方向相反，强度可以根据激活的重要性进行调整。3) **激活编辑的策略**：可以将误导向量直接加到激活值上，或者使用更复杂的编辑策略，如基于注意力机制的编辑。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16297v1/img/overviewSRMU.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16297v1/img/combinationablation.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SRMU在WMDP基准测试中取得了最先进的遗忘性能，同时保持了最小的效用损失。在高纠缠配置下，即使在20-30%的数据重叠情况下，SRMU仍然有效，而现有的基线方法已经失效。这表明SRMU具有更强的鲁棒性和实用性，能够应对更复杂的实际应用场景。

## 🎯 应用场景

SRMU技术可应用于各种需要知识遗忘的场景，例如：1) 大型语言模型中的隐私数据移除，确保模型不泄露用户个人信息；2) 模型合规性治理，移除模型中违反法律法规或伦理道德的内容；3) 模型知识产权保护，防止模型被用于非法复制或传播受版权保护的内容。该技术有助于提升LLM在安全敏感领域的应用价值。

## 📄 摘要（原文）

> As large language models (LLMs) are increasingly adopted in safety-critical and regulated sectors, the retention of sensitive or prohibited knowledge introduces escalating risks, ranging from privacy leakage to regulatory non-compliance to to potential misuse, and so on. Recent studies suggest that machine unlearning can help ensure deployed models comply with evolving legal, safety, and governance requirements. However, current unlearning techniques assume clean separation between forget and retain datasets, which is challenging in operational settings characterized by highly entangled distributions. In such scenarios, perturbation-based methods often degrade general model utility or fail to ensure safety. To address this, we propose Selective Representation Misdirection for Unlearning (SRMU), a novel principled activation-editing framework that enforces feature-aware and directionally controlled perturbations. Unlike indiscriminate model weights perturbations, SRMU employs a structured misdirection vector with an activation importance map. The goal is to allow SRMU selectively suppresses harmful representations while preserving the utility on benign ones. Experiments are conducted on the widely used WMDP benchmark across low- and high-entanglement configurations. Empirical results reveal that SRMU delivers state-of-the-art unlearning performance with minimal utility losses, and remains effective under 20-30\% overlap where existing baselines collapse. SRMU provides a robust foundation for safety-driven model governance, privacy compliance, and controlled knowledge removal in the emerging LLM-based applications. We release the replication package at https://figshare.com/s/d5931192a8824de26aff.

