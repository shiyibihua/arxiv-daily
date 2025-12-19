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

**提出选择性表征误导（SRMU）框架，用于解决高数据纠缠场景下的机器遗忘问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器遗忘` `表征学习` `激活编辑` `数据隐私` `大型语言模型`

## 📋 核心要点

1. 现有机器遗忘方法在数据高度纠缠的情况下表现不佳，容易导致模型性能下降或遗忘失败。
2. SRMU通过引入特征感知的、方向可控的扰动，选择性地抑制有害表征，同时保留对良性表征的效用。
3. 实验表明，SRMU在高数据纠缠场景下实现了最先进的遗忘性能，且对模型效用的影响最小。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在安全关键和受监管领域的日益普及，模型中保留的敏感或违禁知识带来了不断升级的风险，包括隐私泄露、违反法规以及潜在的滥用等。近期的研究表明，机器遗忘有助于确保已部署的模型符合不断变化的法律、安全和治理要求。然而，现有的遗忘技术通常假设遗忘数据集和保留数据集之间存在清晰的分离，这在具有高度纠缠分布的实际操作环境中极具挑战性。在这种情况下，基于扰动的方法通常会降低模型的通用性或无法确保安全性。为了解决这个问题，我们提出了一种新颖的、基于原则的激活编辑框架——用于遗忘的选择性表征误导（SRMU），该框架强制执行特征感知和方向控制的扰动。与不加区分的模型权重扰动不同，SRMU采用带有激活重要性图的结构化误导向量。目标是允许SRMU选择性地抑制有害表征，同时保留对良性表征的效用。在广泛使用的WMDP基准上，针对低纠缠和高纠缠配置进行了实验。实验结果表明，SRMU提供了最先进的遗忘性能，同时最大限度地减少了效用损失，并且在现有基线崩溃的20-30%重叠下仍然有效。SRMU为安全驱动的模型治理、隐私合规性和新兴的基于LLM的应用中的受控知识移除提供了强大的基础。我们在https://figshare.com/s/d5931192a8824de26aff发布了复现包。

## 🔬 方法详解

**问题定义**：论文旨在解决机器遗忘领域中，当遗忘数据和保留数据高度纠缠时，现有方法难以有效遗忘敏感信息且容易损害模型通用性的问题。现有方法通常假设数据之间存在清晰的分离，但在实际应用中，这种假设往往不成立，导致基于扰动的方法要么无法有效遗忘，要么过度扰动模型权重，降低模型性能。

**核心思路**：SRMU的核心思路是通过选择性地“误导”模型内部的表征，使其不再包含或弱化与遗忘数据相关的特征，同时尽可能保留与保留数据相关的特征。这种“误导”不是随机的，而是基于特征重要性和方向控制的，从而实现更精确的遗忘效果，并减少对模型整体性能的影响。

**技术框架**：SRMU框架主要包含以下几个阶段：1) **激活重要性图生成**：评估模型每一层激活对遗忘任务的重要性。2) **结构化误导向量构建**：基于激活重要性图，构建一个具有方向性的扰动向量，用于“误导”模型的表征。3) **激活编辑**：将误导向量应用到模型的激活层，从而选择性地抑制有害表征。4) **模型微调**：对模型进行微调，以恢复因激活编辑而损失的性能。

**关键创新**：SRMU的关键创新在于其选择性和方向性的扰动方式。与传统的权重扰动方法不同，SRMU不是直接修改模型权重，而是通过修改激活层来实现遗忘。此外，SRMU还引入了激活重要性图，用于指导扰动的方向和强度，从而实现更精确的遗忘效果。

**关键设计**：SRMU的关键设计包括：1) **激活重要性评估方法**：论文可能采用梯度信息或其他方法来评估激活对遗忘任务的重要性。2) **误导向量的构建方式**：误导向量需要能够有效地抑制有害表征，同时尽可能保留良性表征。3) **激活编辑的具体操作**：如何将误导向量应用到激活层，以及如何控制扰动的强度。4) **微调策略**：如何通过微调来恢复模型性能，同时避免重新学习到遗忘的信息。

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

SRMU在WMDP基准测试中取得了最先进的遗忘性能，尤其是在高数据纠缠的情况下，显著优于现有基线方法。即使在遗忘数据和保留数据存在20-30%的重叠时，SRMU仍然能够有效遗忘，而现有方法已经失效。此外，SRMU在实现有效遗忘的同时，对模型效用的影响也最小。

## 🎯 应用场景

SRMU技术可应用于各种需要进行安全驱动的模型治理、隐私合规性和受控知识移除的场景，例如：大型语言模型在医疗、金融等敏感领域的应用；在线教育平台中对不适宜内容的过滤；以及企业内部知识库中对过期或错误信息的移除。该技术有助于确保AI系统在满足合规性要求的同时，保持良好的性能和可靠性。

## 📄 摘要（原文）

> As large language models (LLMs) are increasingly adopted in safety-critical and regulated sectors, the retention of sensitive or prohibited knowledge introduces escalating risks, ranging from privacy leakage to regulatory non-compliance to to potential misuse, and so on. Recent studies suggest that machine unlearning can help ensure deployed models comply with evolving legal, safety, and governance requirements. However, current unlearning techniques assume clean separation between forget and retain datasets, which is challenging in operational settings characterized by highly entangled distributions. In such scenarios, perturbation-based methods often degrade general model utility or fail to ensure safety. To address this, we propose Selective Representation Misdirection for Unlearning (SRMU), a novel principled activation-editing framework that enforces feature-aware and directionally controlled perturbations. Unlike indiscriminate model weights perturbations, SRMU employs a structured misdirection vector with an activation importance map. The goal is to allow SRMU selectively suppresses harmful representations while preserving the utility on benign ones. Experiments are conducted on the widely used WMDP benchmark across low- and high-entanglement configurations. Empirical results reveal that SRMU delivers state-of-the-art unlearning performance with minimal utility losses, and remains effective under 20-30\% overlap where existing baselines collapse. SRMU provides a robust foundation for safety-driven model governance, privacy compliance, and controlled knowledge removal in the emerging LLM-based applications. We release the replication package at https://figshare.com/s/d5931192a8824de26aff.

