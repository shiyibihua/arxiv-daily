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

**提出ICP-MIA框架，通过上下文探查解决微调语言模型的成员推理攻击问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `成员推理攻击` `大型语言模型` `隐私保护` `上下文学习` `优化差距`

## 📋 核心要点

1. 现有黑盒成员推理攻击依赖置信度等信号，易受样本固有属性干扰，泛化性差。
2. 提出ICP-MIA框架，利用优化差距作为成员信号，通过上下文探查模拟微调行为。
3. 实验表明，ICP-MIA显著优于现有黑盒MIA方法，尤其在低假阳性率下表现突出。

## 📝 摘要（中文）

成员推理攻击(MIAs)对微调的大型语言模型(LLMs)构成严重的隐私威胁，尤其是在模型使用敏感数据进行领域特定任务适配时。现有的黑盒MIA技术依赖于置信度分数或token似然，但这些信号通常与样本的内在属性（如内容难度或稀有度）纠缠在一起，导致泛化能力差和信噪比低。本文提出了ICP-MIA，一个基于训练动态理论（特别是优化过程中的收益递减现象）的新型MIA框架。我们将优化差距作为成员身份的基本信号：在收敛时，成员样本表现出最小的剩余损失减少潜力，而非成员样本保留了进一步优化的显著潜力。为了在黑盒设置中估计这个差距，我们提出了一种无需训练的方法——上下文探查(ICP)，它通过策略性构建的输入上下文来模拟微调行为。我们提出了两种探查策略：基于参考数据的探查（使用语义相似的公共样本）和自扰动（通过掩码或生成）。在三个任务和多个LLM上的实验表明，ICP-MIA显著优于先前的黑盒MIA，尤其是在低假阳性率下。我们进一步分析了参考数据对齐、模型类型、PEFT配置和训练计划如何影响攻击效果。我们的发现确立了ICP-MIA作为一个实用且理论上合理的框架，用于审计已部署LLM中的隐私风险。

## 🔬 方法详解

**问题定义**：论文旨在解决微调语言模型中，现有成员推理攻击方法效果不佳的问题。现有方法依赖于模型输出的置信度或token似然等信号，但这些信号与样本本身的难度、稀有度等属性高度相关，导致攻击者难以区分模型“记住”了训练数据，还是仅仅因为样本本身就容易预测。因此，现有方法泛化能力差，信噪比低，难以有效识别成员样本。

**核心思路**：论文的核心思路是利用训练动态中的“收益递减”现象。成员样本在训练过程中已经被模型“记住”，因此在模型收敛后，对这些样本进行进一步优化带来的收益（损失减少）会很小。而非成员样本则还有很大的优化空间。因此，可以通过估计样本的“优化差距”（Optimization Gap）来判断其是否为成员样本。

**技术框架**：ICP-MIA框架主要包含两个阶段：首先，通过“上下文探查”（In-Context Probing, ICP）来估计样本的优化差距。然后，利用估计的优化差距来判断样本是否为成员。ICP阶段又包含两种探查策略：基于参考数据的探查和自扰动探查。基于参考数据的探查使用与目标样本语义相似的公共数据作为上下文，引导模型对目标样本进行预测。自扰动探查则通过掩码或生成等方式对目标样本进行扰动，然后观察模型在扰动后的预测变化。

**关键创新**：论文最重要的创新点在于提出了利用“优化差距”作为成员推理攻击的信号。与以往方法直接利用模型输出的置信度等信号不同，优化差距更能反映模型对样本的“记忆”程度，从而提高了攻击的准确性和泛化能力。此外，提出的“上下文探查”方法无需训练，可以直接在黑盒模型上进行，具有很强的实用性。

**关键设计**：在基于参考数据的探查中，关键在于选择与目标样本语义相似的参考数据。论文可能使用了某种语义相似度度量方法（具体方法未知）来选择参考数据。在自扰动探查中，关键在于选择合适的扰动方式和扰动强度。论文可能尝试了不同的掩码策略和生成模型（具体细节未知）。此外，如何将估计的优化差距转化为成员概率，可能也涉及一些阈值设置或概率模型（具体细节未知）。

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

实验结果表明，ICP-MIA在多个任务和模型上显著优于现有的黑盒MIA方法。尤其是在低假阳性率下，ICP-MIA的性能提升更为明显，表明其能够更准确地识别成员样本，降低误报率。论文还分析了参考数据对齐、模型类型、PEFT配置和训练计划等因素对攻击效果的影响，为实际应用提供了指导。

## 🎯 应用场景

该研究成果可应用于评估和提升已部署大型语言模型的隐私安全性。通过ICP-MIA框架，可以有效识别模型存在的隐私泄露风险，并指导模型开发者采取相应的防御措施，例如差分隐私训练、对抗训练等，从而保护用户敏感数据。

## 📄 摘要（原文）

> Membership inference attacks (MIAs) pose a critical privacy threat to fine-tuned large language models (LLMs), especially when models are adapted to domain-specific tasks using sensitive data. While prior black-box MIA techniques rely on confidence scores or token likelihoods, these signals are often entangled with a sample's intrinsic properties - such as content difficulty or rarity - leading to poor generalization and low signal-to-noise ratios. In this paper, we propose ICP-MIA, a novel MIA framework grounded in the theory of training dynamics, particularly the phenomenon of diminishing returns during optimization. We introduce the Optimization Gap as a fundamental signal of membership: at convergence, member samples exhibit minimal remaining loss-reduction potential, while non-members retain significant potential for further optimization. To estimate this gap in a black-box setting, we propose In-Context Probing (ICP), a training-free method that simulates fine-tuning-like behavior via strategically constructed input contexts. We propose two probing strategies: reference-data-based (using semantically similar public samples) and self-perturbation (via masking or generation). Experiments on three tasks and multiple LLMs show that ICP-MIA significantly outperforms prior black-box MIAs, particularly at low false positive rates. We further analyze how reference data alignment, model type, PEFT configurations, and training schedules affect attack effectiveness. Our findings establish ICP-MIA as a practical and theoretically grounded framework for auditing privacy risks in deployed LLMs.

