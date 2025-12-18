---
layout: default
title: Explaining multimodal LLMs via intra-modal token interactions
---

# Explaining multimodal LLMs via intra-modal token interactions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22415" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22415v2</a>
  <a href="https://arxiv.org/pdf/2509.22415.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22415v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22415v2', 'Explaining multimodal LLMs via intra-modal token interactions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiawei Liang, Ruoyu Chen, Xianghao Jiao, Siyuan Liang, Shiming Liu, Qunli Zhang, Zheng Hu, Xiaochun Cao

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-26 (更新: 2025-10-01)

---

## 💡 一句话要点

**通过模态内token交互增强多模态LLM的可解释性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `可解释性` `大型语言模型` `视觉语言模型` `模态内交互`

## 📋 核心要点

1. 现有MLLM可解释性方法忽略了模态内部token的依赖关系，导致视觉解释分散，文本解释引入虚假激活。
2. 论文提出利用模态内交互增强可解释性，视觉模态采用多尺度解释聚合，文本模态采用激活排序相关性。
3. 实验表明，该方法在多个MLLM和数据集上优于现有方法，提供更忠实和细粒度的模型行为解释。

## 📝 摘要（中文）

多模态大型语言模型(MLLM)在各种视觉-语言任务中取得了显著成功，但其内部决策机制仍未得到充分理解。现有的可解释性研究主要集中于跨模态归因，即识别模型在输出生成过程中关注的图像区域。然而，这些方法通常忽略了模态内的依赖关系。在视觉模态中，由于感受野有限，将重要性归因于孤立的图像块会忽略空间上下文，导致解释分散且嘈杂。在文本模态中，依赖于前面的token会引入虚假的激活。未能有效缓解这些干扰会损害归因的保真度。为了解决这些限制，我们提出通过利用模态内交互来增强可解释性。对于视觉分支，我们引入了多尺度解释聚合(MSEA)，它聚合多尺度输入的归因，以动态调整感受野，从而产生更整体和空间连贯的视觉解释。对于文本分支，我们提出了激活排序相关性(ARC)，它通过对齐上下文token的top-k预测排名来衡量上下文token与当前token的相关性。ARC利用这种相关性来抑制来自不相关上下文的虚假激活，同时保留语义上连贯的激活。在最先进的MLLM和基准数据集上进行的大量实验表明，我们的方法始终优于现有的可解释性方法，从而产生更忠实和细粒度的模型行为解释。

## 🔬 方法详解

**问题定义**：现有MLLM可解释性方法主要关注跨模态的视觉区域定位，忽略了模态内部token之间的依赖关系。在视觉模态中，由于感受野的限制，对孤立图像块的归因忽略了空间上下文，导致解释结果分散且噪声大。在文本模态中，对前序token的依赖会引入虚假激活，影响归因的准确性。

**核心思路**：论文的核心思路是通过挖掘和利用模态内部token之间的交互关系来提升可解释性。具体来说，对于视觉模态，通过聚合多尺度信息来动态调整感受野，从而获得更全面的空间上下文信息。对于文本模态，通过评估上下文token与当前token的相关性来抑制不相关的激活，保留语义连贯的信息。

**技术框架**：整体框架包含两个主要模块：视觉解释增强模块和文本解释增强模块。视觉解释增强模块采用多尺度解释聚合(MSEA)，文本解释增强模块采用激活排序相关性(ARC)。MSEA首先对输入图像进行多尺度处理，然后对每个尺度下的归因图进行聚合，得到最终的视觉解释。ARC首先计算上下文token与当前token的预测排名相关性，然后利用该相关性对上下文token的激活进行加权，从而抑制不相关的激活。

**关键创新**：论文的关键创新在于提出了利用模态内token交互来增强MLLM可解释性的思想。与现有方法相比，该方法能够更有效地利用模态内部的信息，从而产生更准确、更细粒度的解释。MSEA通过多尺度聚合动态调整感受野，克服了传统方法感受野固定的局限性。ARC通过预测排名相关性来评估token相关性，避免了直接依赖前序token带来的虚假激活问题。

**关键设计**：在MSEA中，多尺度的选择和聚合方式是关键。论文中具体使用了哪些尺度，以及如何对不同尺度的归因图进行加权聚合，这些细节决定了最终的解释效果。在ARC中，top-k值的选择以及相关性度量方式的选择是关键。不同的k值和相关性度量方式会影响token相关性的评估结果，从而影响虚假激活的抑制效果。论文中具体使用了什么k值和相关性度量方式，需要进一步研究。

## 📊 实验亮点

论文提出的MSEA和ARC方法在多个MLLM和数据集上取得了显著的性能提升。实验结果表明，该方法能够产生更忠实、更细粒度的模型行为解释，优于现有的可解释性方法。具体的性能数据和对比基线需要在论文中查找。

## 🎯 应用场景

该研究成果可应用于提升多模态大语言模型的可信度和透明度，帮助用户理解模型的决策过程。在医疗诊断、自动驾驶等安全攸关领域，清晰的解释能够增强用户对模型的信任，并促进模型的部署和应用。此外，该方法还可以用于模型调试和优化，发现模型潜在的问题和改进方向。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have achieved remarkable success across diverse vision-language tasks, yet their internal decision-making mechanisms remain insufficiently understood. Existing interpretability research has primarily focused on cross-modal attribution, identifying which image regions the model attends to during output generation. However, these approaches often overlook intra-modal dependencies. In the visual modality, attributing importance to isolated image patches ignores spatial context due to limited receptive fields, resulting in fragmented and noisy explanations. In the textual modality, reliance on preceding tokens introduces spurious activations. Failing to effectively mitigate these interference compromises attribution fidelity. To address these limitations, we propose enhancing interpretability by leveraging intra-modal interaction. For the visual branch, we introduce \textit{Multi-Scale Explanation Aggregation} (MSEA), which aggregates attributions over multi-scale inputs to dynamically adjust receptive fields, producing more holistic and spatially coherent visual explanations. For the textual branch, we propose \textit{Activation Ranking Correlation} (ARC), which measures the relevance of contextual tokens to the current token via alignment of their top-$k$ prediction rankings. ARC leverages this relevance to suppress spurious activations from irrelevant contexts while preserving semantically coherent ones. Extensive experiments across state-of-the-art MLLMs and benchmark datasets demonstrate that our approach consistently outperforms existing interpretability methods, yielding more faithful and fine-grained explanations of model behavior.

