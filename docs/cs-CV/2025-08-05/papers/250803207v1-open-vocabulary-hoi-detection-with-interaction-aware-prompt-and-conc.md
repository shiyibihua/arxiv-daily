---
layout: default
title: Open-Vocabulary HOI Detection with Interaction-aware Prompt and Concept Calibration
---

# Open-Vocabulary HOI Detection with Interaction-aware Prompt and Concept Calibration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03207" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03207v1</a>
  <a href="https://arxiv.org/pdf/2508.03207.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03207v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03207v1', 'Open-Vocabulary HOI Detection with Interaction-aware Prompt and Concept Calibration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ting Lei, Shaofeng Yin, Qingchao Chen, Yuxin Peng, Yang Liu

**分类**: cs.CV

**发布日期**: 2025-08-05

**🔗 代码/项目**: [GITHUB](https://github.com/ltttpku/INP-CC)

---

## 💡 一句话要点

**提出INP-CC以解决开放词汇HOI检测中的交互识别问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `开放词汇` `人-物交互` `视觉与语言模型` `交互感知` `概念校准` `负采样策略` `细粒度检测`

## 📋 核心要点

1. 现有方法在开放词汇HOI检测中面临图像编码器不足和文本描述编码困难的挑战，限制了模型的泛化能力。
2. 本文提出了INP-CC，通过动态生成交互感知提示和语言模型指导的概念校准，增强了HOI检测的准确性。
3. 实验结果显示，INP-CC在SWIG-HOI和HICO-DET数据集上显著提升了检测性能，超越了现有的最先进模型。

## 📝 摘要（中文）

开放词汇人-物交互（HOI）检测旨在识别人与物体之间的交互，并能够推广到训练集之外的新交互类别。目前的方法通常依赖于视觉与语言模型（VLMs），但由于图像编码器的不足，导致图像级预训练与细粒度区域级交互检测之间的对齐不佳。此外，有效编码视觉外观的文本描述仍然困难，限制了模型捕捉详细HOI关系的能力。为了解决这些问题，本文提出了交互感知提示与概念校准（INP-CC），这是一个端到端的开放词汇HOI检测器，集成了交互感知提示和概念校准。实验结果表明，INP-CC在SWIG-HOI和HICO-DET数据集上显著优于现有的最先进模型。

## 🔬 方法详解

**问题定义**：本文旨在解决开放词汇HOI检测中，现有方法在图像编码和文本描述编码方面的不足，导致模型无法有效识别新交互类别。

**核心思路**：提出INP-CC，通过交互感知提示生成器动态生成提示，聚焦于关键交互模式，同时通过语言模型校准概念表示，增强模型对多样HOI概念的区分能力。

**技术框架**：INP-CC的整体架构包括交互感知提示生成模块、概念校准模块和负采样策略，形成一个端到端的检测流程。交互感知提示生成器根据输入场景生成提示，而概念校准模块则通过视觉相似性分析来优化HOI概念表示。

**关键创新**：最重要的创新在于交互感知提示的动态生成和概念校准机制，这使得模型能够更好地捕捉细粒度的交互信息，与传统方法相比，显著提升了检测的准确性和泛化能力。

**关键设计**：在模型设计中，采用了负采样策略来改善跨模态相似性建模，确保模型能够有效区分视觉上相似但语义上不同的动作。

## 📊 实验亮点

实验结果表明，INP-CC在SWIG-HOI和HICO-DET数据集上的性能显著优于现有最先进模型，具体提升幅度达到XX%，展示了其在开放词汇HOI检测中的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能监控、机器人交互和人机协作等场景，能够提升机器对复杂人-物交互的理解能力，推动智能系统的自主决策和交互能力的发展。未来，该技术有望在自动驾驶、智能家居等领域发挥重要作用。

## 📄 摘要（原文）

> Open Vocabulary Human-Object Interaction (HOI) detection aims to detect interactions between humans and objects while generalizing to novel interaction classes beyond the training set. Current methods often rely on Vision and Language Models (VLMs) but face challenges due to suboptimal image encoders, as image-level pre-training does not align well with the fine-grained region-level interaction detection required for HOI. Additionally, effectively encoding textual descriptions of visual appearances remains difficult, limiting the model's ability to capture detailed HOI relationships. To address these issues, we propose INteraction-aware Prompting with Concept Calibration (INP-CC), an end-to-end open-vocabulary HOI detector that integrates interaction-aware prompts and concept calibration. Specifically, we propose an interaction-aware prompt generator that dynamically generates a compact set of prompts based on the input scene, enabling selective sharing among similar interactions. This approach directs the model's attention to key interaction patterns rather than generic image-level semantics, enhancing HOI detection. Furthermore, we refine HOI concept representations through language model-guided calibration, which helps distinguish diverse HOI concepts by investigating visual similarities across categories. A negative sampling strategy is also employed to improve inter-modal similarity modeling, enabling the model to better differentiate visually similar but semantically distinct actions. Extensive experimental results demonstrate that INP-CC significantly outperforms state-of-the-art models on the SWIG-HOI and HICO-DET datasets. Code is available at https://github.com/ltttpku/INP-CC.

