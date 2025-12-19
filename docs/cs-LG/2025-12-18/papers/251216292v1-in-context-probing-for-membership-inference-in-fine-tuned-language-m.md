---
layout: default
title: In-Context Probing for Membership Inference in Fine-Tuned Language Models
---

# In-Context Probing for Membership Inference in Fine-Tuned Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16292" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16292v1</a>
  <a href="https://arxiv.org/pdf/2512.16292.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16292v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16292v1', 'In-Context Probing for Membership Inference in Fine-Tuned Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhexi Lu, Hongliang Chi, Nathalie Baracaldo, Swanand Ravindra Kadhe, Yuseok Jeon, Lei Yu

**分类**: cs.CR, cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出ICP-MIA框架，通过上下文探查解决微调语言模型的成员推断攻击问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `成员推断攻击` `大型语言模型` `隐私安全` `上下文学习` `优化差距`

## 📋 核心要点

1. 现有黑盒成员推断攻击依赖置信度等信号，易受样本固有属性干扰，泛化性差。
2. 提出ICP-MIA框架，利用优化差距作为成员信号，通过上下文探查模拟微调行为。
3. 实验表明，ICP-MIA显著优于现有黑盒MIA，尤其在低假阳性率下，验证了有效性。

## 📝 摘要（中文）

成员推断攻击(MIAs)对微调的大型语言模型(LLMs)构成严重的隐私威胁，尤其是在模型使用敏感数据进行特定领域任务适配时。现有的黑盒MIA技术依赖于置信度分数或token似然，但这些信号通常与样本的固有属性（如内容难度或稀有性）纠缠在一起，导致泛化能力差和信噪比低。本文提出了ICP-MIA，一个基于训练动态理论（特别是优化过程中的收益递减现象）的新型MIA框架。我们将优化差距作为成员的基本信号：在收敛时，成员样本表现出最小的剩余损失减少潜力，而非成员样本保留了进一步优化的显著潜力。为了在黑盒设置中估计这个差距，我们提出了上下文探查(ICP)，一种通过策略性构建的输入上下文来模拟微调行为的免训练方法。我们提出了两种探查策略：基于参考数据的探查（使用语义相似的公共样本）和自扰动（通过掩码或生成）。在三个任务和多个LLM上的实验表明，ICP-MIA显著优于先前的黑盒MIA，尤其是在低假阳性率下。我们进一步分析了参考数据对齐、模型类型、PEFT配置和训练计划如何影响攻击效果。我们的发现将ICP-MIA确立为一个实用且理论上合理的框架，用于审计已部署LLM中的隐私风险。

## 🔬 方法详解

**问题定义**：论文旨在解决微调语言模型中，现有成员推断攻击（MIA）方法效果不佳的问题。现有方法依赖于模型输出的置信度或token似然等信号，但这些信号容易受到样本自身属性（如难度、稀有度）的干扰，导致攻击的泛化能力较差，信噪比低。因此，如何更准确地判断一个样本是否为训练集成员，是本研究要解决的核心问题。

**核心思路**：论文的核心思路是利用训练动态中的“收益递减”现象。作者认为，在模型训练收敛后，训练集中的样本（成员）已经得到了充分学习，其损失减少的潜力很小；而未见过的样本（非成员）则仍有较大的优化空间。因此，可以通过估计样本的“优化差距”（Optimization Gap）来判断其是否为成员。为了在黑盒场景下估计这个差距，论文提出了“上下文探查”（In-Context Probing, ICP）方法，通过构造特定的输入上下文来模拟微调过程，从而评估样本的优化潜力。

**技术框架**：ICP-MIA框架主要包含以下几个步骤：1) **选择目标样本**：选择需要进行成员推断的样本。2) **构建上下文**：使用ICP方法构建输入上下文，模拟微调过程。论文提出了两种上下文构建策略：基于参考数据的探查和自扰动。3) **损失计算**：计算在原始模型和经过上下文探查后的模型上的损失，得到优化差距。4) **成员推断**：根据优化差距的大小，判断样本是否为训练集成员。优化差距小的样本被认为是成员，优化差距大的样本被认为是非成员。

**关键创新**：该论文最重要的创新点在于提出了基于“优化差距”的成员推断信号，并设计了“上下文探查”方法来在黑盒场景下估计这个差距。与以往依赖置信度等信号的方法不同，该方法直接从训练动态的角度出发，更准确地反映了样本与模型之间的关系。此外，ICP方法无需训练，降低了攻击的成本和复杂性。

**关键设计**：在上下文探查方面，论文提出了两种关键的设计：1) **基于参考数据的探查**：利用与目标样本语义相似的公共数据作为参考，构建上下文。关键在于如何选择合适的参考数据，论文可能使用了语义相似度计算等方法。2) **自扰动**：通过对目标样本进行掩码或生成等操作，生成扰动后的样本，并将其作为上下文。关键在于如何设计扰动策略，以保证扰动后的样本仍然具有一定的语义信息，并且能够反映样本的优化潜力。论文可能使用了特定的掩码策略或生成模型。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16292v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16292v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16292v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，ICP-MIA在三个任务和多个LLM上显著优于先前的黑盒MIA方法，尤其是在低假阳性率下。这意味着在保证较低误报率的前提下，ICP-MIA能够更准确地识别出训练集成员。具体的性能提升数据（例如AUC、准确率等）以及对比的基线方法需要在论文中查找。

## 🎯 应用场景

该研究成果可应用于评估和增强已部署大型语言模型的隐私安全性。通过ICP-MIA框架，可以审计模型是否存在过度记忆训练数据的风险，从而指导模型开发者采取相应的隐私保护措施，例如差分隐私训练、数据增强等，以降低模型泄露敏感信息的可能性。该研究对于保护用户隐私、促进LLM安全应用具有重要意义。

## 📄 摘要（原文）

> Membership inference attacks (MIAs) pose a critical privacy threat to fine-tuned large language models (LLMs), especially when models are adapted to domain-specific tasks using sensitive data. While prior black-box MIA techniques rely on confidence scores or token likelihoods, these signals are often entangled with a sample's intrinsic properties - such as content difficulty or rarity - leading to poor generalization and low signal-to-noise ratios. In this paper, we propose ICP-MIA, a novel MIA framework grounded in the theory of training dynamics, particularly the phenomenon of diminishing returns during optimization. We introduce the Optimization Gap as a fundamental signal of membership: at convergence, member samples exhibit minimal remaining loss-reduction potential, while non-members retain significant potential for further optimization. To estimate this gap in a black-box setting, we propose In-Context Probing (ICP), a training-free method that simulates fine-tuning-like behavior via strategically constructed input contexts. We propose two probing strategies: reference-data-based (using semantically similar public samples) and self-perturbation (via masking or generation). Experiments on three tasks and multiple LLMs show that ICP-MIA significantly outperforms prior black-box MIAs, particularly at low false positive rates. We further analyze how reference data alignment, model type, PEFT configurations, and training schedules affect attack effectiveness. Our findings establish ICP-MIA as a practical and theoretically grounded framework for auditing privacy risks in deployed LLMs.

