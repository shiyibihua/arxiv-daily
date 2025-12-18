---
layout: default
title: Symbolic Graphics Programming with Large Language Models
---

# Symbolic Graphics Programming with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05208" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05208v1</a>
  <a href="https://arxiv.org/pdf/2509.05208.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05208v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05208v1', 'Symbolic Graphics Programming with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yamei Chen, Haoquan Zhang, Yangyi Huang, Zeju Qiu, Kaipeng Zhang, Yandong Wen, Weiyang Liu

**分类**: cs.CV, cs.LG

**发布日期**: 2025-09-05

**备注**: Technical report (32 pages, 12 figures, project page: https://spherelab.ai/SGP-Gen/)

---

## 💡 一句话要点

**提出基于强化学习的框架，提升大语言模型生成精确可控SVG图像的能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `符号图形编程` `大语言模型` `强化学习` `SVG生成` `跨模态学习`

## 📋 核心要点

1. 现有大语言模型在程序合成方面表现出色，但在生成可渲染为精确视觉内容的符号图形程序（SGP）方面的能力仍有待探索。
2. 论文提出一种基于强化学习（RL）和可验证奖励的方法，利用格式有效性门和跨模态奖励来提升LLM生成SGP的能力。
3. 实验表明，该方法应用于Qwen-2.5-7B后，显著提高了SVG生成质量和语义，达到了与前沿系统相当的性能。

## 📝 摘要（中文）

本文研究了符号图形编程，旨在从自然语言描述生成可渲染为精确视觉内容的符号图形程序（SGP）。该任务通过提示大语言模型（LLM）生成由SGP渲染的图像，从而考察LLM对视觉世界的理解。本文专注于可缩放矢量图形（SVG）。首先，评估了LLM生成SGP的能力，为此引入了SGP-GenBench，一个涵盖对象保真度、场景保真度和组合性（属性绑定、空间关系、数值能力）的综合基准。实验表明，前沿专有模型显著优于开源模型，且性能与通用编码能力密切相关。针对这一差距，本文提出了一种基于强化学习（RL）和可验证奖励的方法，其中格式有效性门确保SVG可渲染，跨模态奖励通过强大的视觉编码器（例如，SigLIP用于文本-图像，DINO用于图像-图像）对齐文本和渲染图像。应用于Qwen-2.5-7B后，该方法显著提高了SVG生成质量和语义，达到了与前沿系统相当的性能。进一步分析了训练动态，表明RL诱导了（i）将对象更精细地分解为可控的基元，以及（ii）改善场景连贯性的上下文细节。结果表明，符号图形编程为跨模态基础提供了精确且可解释的视角。

## 🔬 方法详解

**问题定义**：论文旨在解决大语言模型（LLM）在生成符号图形程序（SGP）方面的不足，特别是生成可渲染为精确视觉内容的SVG图像。现有方法难以保证生成SVG的质量和语义准确性，尤其是在对象保真度、场景保真度和组合性方面存在挑战。

**核心思路**：论文的核心思路是利用强化学习（RL）来训练LLM，使其能够生成更准确、更符合语义的SVG代码。通过引入可验证奖励机制，确保生成的SVG格式有效且内容与给定的文本描述一致。这种方法旨在弥合LLM的文本生成能力与视觉内容生成之间的差距。

**技术框架**：整体框架包括以下几个主要模块：1) LLM（例如Qwen-2.5-7B）作为SVG代码生成器；2) 格式有效性门，用于验证生成的SVG代码是否可渲染；3) 跨模态奖励模块，利用视觉编码器（SigLIP和DINO）计算文本描述与渲染图像之间的相似度，作为RL的奖励信号；4) 强化学习算法（具体算法未知），用于优化LLM的生成策略。

**关键创新**：最重要的技术创新点在于将强化学习与可验证奖励相结合，用于训练LLM生成SVG代码。这种方法不仅保证了生成SVG的格式有效性，还通过跨模态奖励确保了生成内容与文本描述的语义一致性。与传统的监督学习方法相比，RL能够更好地探索SVG代码的生成空间，从而生成更复杂、更准确的图像。

**关键设计**：关键设计包括：1) 使用SigLIP作为文本-图像编码器，用于计算文本描述与渲染图像之间的相似度；2) 使用DINO作为图像-图像编码器，用于评估生成图像的质量和一致性；3) 设计合适的奖励函数，平衡格式有效性和语义一致性；4) 强化学习算法的具体选择和参数调整（未知）。

## 📊 实验亮点

实验结果表明，将该方法应用于Qwen-2.5-7B后，SVG生成质量和语义显著提高，达到了与前沿专有模型相当的性能水平。通过分析训练动态，发现强化学习能够促使LLM将对象分解为更精细的可控基元，并生成改善场景连贯性的上下文细节。具体性能提升数据未知。

## 🎯 应用场景

该研究成果可应用于图像生成、计算机辅助设计、视觉内容创作等领域。通过自然语言描述生成高质量的矢量图形，可以降低设计门槛，提高创作效率。未来，该技术有望应用于自动化内容生成、虚拟现实、增强现实等领域，实现更智能、更便捷的视觉内容交互。

## 📄 摘要（原文）

> Large language models (LLMs) excel at program synthesis, yet their ability to produce symbolic graphics programs (SGPs) that render into precise visual content remains underexplored. We study symbolic graphics programming, where the goal is to generate an SGP from a natural-language description. This task also serves as a lens into how LLMs understand the visual world by prompting them to generate images rendered from SGPs. Among various SGPs, our paper sticks to scalable vector graphics (SVGs). We begin by examining the extent to which LLMs can generate SGPs. To this end, we introduce SGP-GenBench, a comprehensive benchmark covering object fidelity, scene fidelity, and compositionality (attribute binding, spatial relations, numeracy). On SGP-GenBench, we discover that frontier proprietary models substantially outperform open-source models, and performance correlates well with general coding capabilities. Motivated by this gap, we aim to improve LLMs' ability to generate SGPs. We propose a reinforcement learning (RL) with verifiable rewards approach, where a format-validity gate ensures renderable SVG, and a cross-modal reward aligns text and the rendered image via strong vision encoders (e.g., SigLIP for text-image and DINO for image-image). Applied to Qwen-2.5-7B, our method substantially improves SVG generation quality and semantics, achieving performance on par with frontier systems. We further analyze training dynamics, showing that RL induces (i) finer decomposition of objects into controllable primitives and (ii) contextual details that improve scene coherence. Our results demonstrate that symbolic graphics programming offers a precise and interpretable lens on cross-modal grounding.

