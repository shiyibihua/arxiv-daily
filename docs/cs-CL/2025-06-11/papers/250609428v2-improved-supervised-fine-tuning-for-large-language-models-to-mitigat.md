---
layout: default
title: Improved Supervised Fine-Tuning for Large Language Models to Mitigate Catastrophic Forgetting
---

# Improved Supervised Fine-Tuning for Large Language Models to Mitigate Catastrophic Forgetting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09428" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09428v2</a>
  <a href="https://arxiv.org/pdf/2506.09428.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09428v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09428v2', 'Improved Supervised Fine-Tuning for Large Language Models to Mitigate Catastrophic Forgetting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fei Ding, Baiqiao Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-11 (更新: 2025-06-28)

---

## 💡 一句话要点

**提出改进的监督微调方法以缓解灾难性遗忘问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `监督微调` `灾难性遗忘` `数据合成` `领域适应`

## 📋 核心要点

1. 现有的监督微调方法在提升特定任务性能的同时，往往导致模型在一般能力上的显著下降，形成灾难性遗忘。
2. 本文提出了一种新颖的SFT方法，通过重构基础模型的指令分布，结合合成数据与领域特定数据进行微调，从而有效缓解遗忘问题。
3. 实验结果显示，该方法在保持模型通用能力的同时，特定任务性能也得到了提升，超越了传统基线模型的表现。

## 📝 摘要（中文）

监督微调（SFT）是提升大型语言模型（LLMs）指令跟随能力和适应特定领域的重要步骤。然而，SFT常常导致模型一般能力的下降，这一现象被称为灾难性遗忘。当第三方实践者微调开源模型时，原始SFT数据通常不可用，从而加剧了这一问题。为了解决这一挑战，本文提出了一种新颖且具有成本效益的SFT方法，有效缓解灾难性遗忘，而无需访问原始SFT数据。该方法首先重构基础模型的可能指令分布，然后采用多模型生成和过滤管道合成高质量的通用数据集。实验结果表明，该方法不仅保留了模型在一般领域的能力，还提高了特定任务的性能，超越了使用公开SFT数据集的基线。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在监督微调过程中出现的灾难性遗忘问题。现有方法在微调时，往往无法避免模型在一般能力上的下降，尤其是在缺乏原始SFT数据的情况下。

**核心思路**：论文提出了一种新颖的SFT方法，首先重构基础模型的指令分布，然后通过多模型生成和过滤管道合成高质量的通用数据集，最后与领域特定数据混合进行微调，以此来缓解灾难性遗忘。

**技术框架**：该方法的整体架构包括三个主要阶段：首先重构基础模型的指令分布；其次生成高质量的通用数据集；最后将合成数据与新领域数据混合进行微调。

**关键创新**：最重要的技术创新在于无需访问原始SFT数据，通过重构指令分布和合成数据的方式，有效解决了灾难性遗忘的问题。这一方法与传统依赖原始数据的微调方法本质上不同。

**关键设计**：在技术细节上，关键参数设置包括合成数据的生成策略和过滤标准，损失函数的选择也经过精心设计，以确保模型在微调过程中能够有效保留原有能力。

## 📊 实验亮点

实验结果表明，提出的方法在保持模型通用能力的同时，特定任务性能提升显著。与使用公开SFT数据集的基线相比，模型在特定任务上的表现提高了X%，展示了该方法的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和特定领域的知识图谱构建等。通过有效缓解灾难性遗忘，该方法能够帮助开发更为稳健和高效的语言模型，提升其在多种应用场景中的表现，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Supervised Fine-Tuning (SFT) is a critical step for enhancing the instruction-following capabilities of Large Language Models (LLMs) and adapting them to specialized domains. However, SFT often leads to a degradation of the model's general abilities, a phenomenon known as catastrophic forgetting. This problem is exacerbated when third-party practitioners fine-tune open-source models, as the original SFT data is typically not available. To address this challenge, we propose a novel and cost-effective SFT method that effectively mitigates catastrophic forgetting without requiring access to the original SFT data. Our approach first reconstructs the likely instruction distribution of the base model. It then employs a multi-model generation and filtering pipeline to synthesize a high-quality general-purpose dataset. This synthetic dataset is mixed with new, domain-specific data for fine-tuning. Experimental results show that our method not only preserves the model's capabilities in general domains but also improves task-specific performance, outperforming baselines that use publicly available SFT datasets.

