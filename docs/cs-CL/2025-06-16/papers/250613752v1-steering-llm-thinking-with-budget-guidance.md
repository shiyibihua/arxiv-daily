---
layout: default
title: Steering LLM Thinking with Budget Guidance
---

# Steering LLM Thinking with Budget Guidance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13752" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13752v1</a>
  <a href="https://arxiv.org/pdf/2506.13752.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13752v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13752v1', 'Steering LLM Thinking with Budget Guidance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junyan Li, Wenshuo Zhao, Yang Zhang, Chuang Gan

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-16

**🔗 代码/项目**: [GITHUB](https://github.com/UMass-Embodied-AGI/BudgetGuidance)

---

## 💡 一句话要点

**提出预算引导方法以优化大语言模型的推理效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `推理控制` `预算引导` `Gamma分布` `性能优化` `数学基准` `高效推理`

## 📋 核心要点

1. 现有的大语言模型在推理过程中常常产生冗长的推理链，导致推理成本过高且性能提升不成比例。
2. 本文提出的预算引导方法通过引入轻量级预测器，控制推理长度而不需要对模型进行微调，从而实现高效推理。
3. 实验结果表明，预算引导在MATH-500基准上实现了最高26%的准确率提升，同时在推理标记使用上显著高效。

## 📝 摘要（中文）

近年来，深度思考的大语言模型（LLM）通过广泛推理来提升性能，但这种冗长的推理并不总是可取，因为它会导致过高的推理成本与不成比例的性能提升。因此，在不牺牲性能的情况下控制推理长度变得尤为重要。本文提出了一种简单而有效的预算引导方法，旨在引导LLM的推理过程朝向目标预算，而无需对LLM进行微调。该方法引入了一个轻量级预测器，在下一个标记生成过程中对剩余思考长度建模Gamma分布，并以软性、标记级的方式引导生成，确保整体推理轨迹符合指定的思考预算。预算引导在挑战性数学基准上显著提高了标记效率，例如在MATH-500基准上，在紧张预算下相比基线方法实现了最高26%的准确率提升，同时仅使用全思考模型63%的思考标记。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在推理过程中推理长度过长的问题，现有方法在控制推理长度时往往无法兼顾性能与效率。

**核心思路**：提出预算引导方法，通过建模剩余思考长度的Gamma分布，软性引导模型生成过程，确保推理过程符合预设的预算。

**技术框架**：整体架构包括一个轻量级的预测器和生成模块，预测器负责计算剩余思考长度的分布，而生成模块则根据该分布引导下一个标记的生成。

**关键创新**：最重要的创新在于引入了预算引导机制，使得推理过程能够在不进行模型微调的情况下，灵活控制推理长度。

**关键设计**：在参数设置上，Gamma分布的参数通过历史推理数据进行训练，损失函数设计为平衡推理长度与生成质量，确保在预算内实现最佳性能。

## 📊 实验亮点

实验结果显示，预算引导方法在MATH-500基准上实现了最高26%的准确率提升，同时在推理标记使用上仅为全思考模型的63%。这一显著的性能提升表明该方法在控制推理长度方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、金融和科学计算等需要高效推理的场景。通过优化推理过程，预算引导方法能够在资源有限的情况下，提升模型的实际应用价值，未来可能推动更多领域的智能化进程。

## 📄 摘要（原文）

> Recent deep-thinking large language models often reason extensively to improve performance, but such lengthy reasoning is not always desirable, as it incurs excessive inference costs with disproportionate performance gains. Controlling reasoning length without sacrificing performance is therefore important, but remains challenging, especially under tight thinking budgets. We propose budget guidance, a simple yet effective method for steering the reasoning process of LLMs toward a target budget without requiring any LLM fine-tuning. Our approach introduces a lightweight predictor that models a Gamma distribution over the remaining thinking length during next-token generation. This signal is then used to guide generation in a soft, token-level manner, ensuring that the overall reasoning trace adheres to the specified thinking budget. Budget guidance enables natural control of the thinking length, along with significant token efficiency improvements over baseline methods on challenging math benchmarks. For instance, it achieves up to a 26% accuracy gain on the MATH-500 benchmark under tight budgets compared to baseline methods, while maintaining competitive accuracy with only 63% of the thinking tokens used by the full-thinking model. Budget guidance also generalizes to broader task domains and exhibits emergent capabilities, such as estimating question difficulty. The source code is available at: https://github.com/UMass-Embodied-AGI/BudgetGuidance.

