---
layout: default
title: Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding
---

# Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15178" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15178v1</a>
  <a href="https://arxiv.org/pdf/2509.15178.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15178v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15178v1', 'Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zaiquan Yang, Yuhao Liu, Gerhard Hancke, Rynson W. H. Lau

**分类**: cs.CV

**发布日期**: 2025-09-18

**期刊**: NeurIPS2025

**🔗 代码/项目**: [GITHUB](https://github.com/zaiquanyang/LLaVA_Next_STVG)

---

## 💡 一句话要点

**利用多模态LLM进行零样本时空视频定位，提出DSTH和TAS策略。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时空视频定位` `多模态LLM` `零样本学习` `视觉语言模型` `注意力机制`

## 📋 核心要点

1. 现有STVG方法难以有效利用文本查询中的属性和动作信息，导致定位精度受限。
2. 提出分解时空高亮（DSTH）和时间增强组装（TAS）策略，提升MLLM在STVG任务中的推理能力。
3. 实验结果表明，该方法在多个STVG基准测试中超越了现有最优方法，验证了其有效性。

## 📝 摘要（中文）

本文旨在利用多模态大型语言模型（MLLM）探索零样本时空视频定位（STVG）方法，即根据文本查询定位视频中的时空区域。研究揭示了MLLM的两个关键特性：一是MLLM倾向于动态分配特殊token（称为“grounding token”）来定位文本查询；二是MLLM由于无法充分整合文本查询中的线索（例如属性、动作）进行推理，常常导致次优的定位效果。基于此，本文提出了一个基于MLLM的零样本STVG框架，包含新颖的分解时空高亮（DSTH）和时间增强组装（TAS）策略，以释放MLLM的推理能力。DSTH策略首先将原始查询分解为属性和动作子查询，从而在空间和时间上查询目标的存在性。然后，它使用一种新颖的logit引导的重注意力（LRA）模块，通过正则化每个子查询的token预测来学习潜在变量作为空间和时间提示。这些提示分别突出显示属性和动作线索，引导模型关注可靠的空间和时间相关视觉区域。此外，由于属性子查询的空间定位应在时间上保持一致，因此我们引入了TAS策略，使用原始视频帧和时间增强帧作为输入来组装预测，以帮助提高时间一致性。我们在各种MLLM上评估了我们的方法，结果表明它在三个常见的STVG基准测试中优于SOTA方法。

## 🔬 方法详解

**问题定义**：时空视频定位（STVG）旨在根据给定的文本查询，在视频中定位对应的时空区域。现有方法通常难以充分利用文本查询中的所有信息，例如属性和动作，导致定位精度不高，尤其是在零样本场景下表现较差。

**核心思路**：本文的核心思路是利用多模态大型语言模型（MLLM）的强大推理能力，并针对MLLM在STVG任务中的不足进行改进。通过分解查询、引入注意力机制和时间增强，引导MLLM更准确地理解文本查询并定位视频中的目标。

**技术框架**：整体框架包括以下几个主要模块：1) 查询分解：将原始文本查询分解为属性和动作两个子查询。2) 分解时空高亮（DSTH）：利用logit引导的重注意力（LRA）模块，学习空间和时间提示，突出显示属性和动作线索。3) 时间增强组装（TAS）：使用原始视频帧和时间增强帧作为输入，组装预测结果，提高时间一致性。

**关键创新**：本文的关键创新在于DSTH策略和TAS策略。DSTH策略通过分解查询和引入LRA模块，能够更有效地利用文本查询中的属性和动作信息，引导模型关注相关的视觉区域。TAS策略通过时间增强，提高了定位结果的时间一致性。

**关键设计**：LRA模块通过正则化每个子查询的token预测来学习潜在变量作为空间和时间提示。TAS策略中，时间增强的具体方法（例如，帧采样策略、时间窗口大小）以及如何融合原始帧和增强帧的预测结果是关键设计细节。损失函数的设计也至关重要，需要考虑空间定位的准确性和时间一致性。

## 📊 实验亮点

实验结果表明，该方法在三个常见的STVG基准测试中均取得了显著的性能提升，超越了现有最优方法。具体性能数据（例如，IoU指标）和提升幅度需要在论文中查找。

## 🎯 应用场景

该研究成果可应用于视频监控、智能安防、自动驾驶、人机交互等领域。例如，在视频监控中，可以通过文本查询快速定位特定事件或人物；在自动驾驶中，可以帮助车辆理解周围环境，提高安全性。

## 📄 摘要（原文）

> Spatio-temporal video grounding (STVG) aims at localizing the spatio-temporal tube of a video, as specified by the input text query. In this paper, we utilize multimodal large language models (MLLMs) to explore a zero-shot solution in STVG. We reveal two key insights about MLLMs: (1) MLLMs tend to dynamically assign special tokens, referred to as \textit{grounding tokens}, for grounding the text query; and (2) MLLMs often suffer from suboptimal grounding due to the inability to fully integrate the cues in the text query (\textit{e.g.}, attributes, actions) for inference. Based on these insights, we propose a MLLM-based zero-shot framework for STVG, which includes novel decomposed spatio-temporal highlighting (DSTH) and temporal-augmented assembling (TAS) strategies to unleash the reasoning ability of MLLMs. The DSTH strategy first decouples the original query into attribute and action sub-queries for inquiring the existence of the target both spatially and temporally. It then uses a novel logit-guided re-attention (LRA) module to learn latent variables as spatial and temporal prompts, by regularizing token predictions for each sub-query. These prompts highlight attribute and action cues, respectively, directing the model's attention to reliable spatial and temporal related visual regions. In addition, as the spatial grounding by the attribute sub-query should be temporally consistent, we introduce the TAS strategy to assemble the predictions using the original video frames and the temporal-augmented frames as inputs to help improve temporal consistency. We evaluate our method on various MLLMs, and show that it outperforms SOTA methods on three common STVG benchmarks.
>   The code will be available at https://github.com/zaiquanyang/LLaVA_Next_STVG.

