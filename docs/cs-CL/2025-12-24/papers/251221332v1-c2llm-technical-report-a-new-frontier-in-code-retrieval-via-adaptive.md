---
layout: default
title: "C2LLM Technical Report: A New Frontier in Code Retrieval via Adaptive Cross-Attention Pooling"
---

# C2LLM Technical Report: A New Frontier in Code Retrieval via Adaptive Cross-Attention Pooling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21332" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21332v1</a>
  <a href="https://arxiv.org/pdf/2512.21332.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21332v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21332v1', 'C2LLM Technical Report: A New Frontier in Code Retrieval via Adaptive Cross-Attention Pooling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jin Qin, Zihan Liao, Ziyin Zhang, Hang Yu, Peng Di, Rui Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**C2LLM：通过自适应跨注意力池化实现代码检索的新突破**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码检索` `代码embedding` `大语言模型` `多头注意力` `对比学习`

## 📋 核心要点

1. 现有基于EOS token的序列embedding方法存在信息瓶颈，无法有效利用所有token信息。
2. C2LLM采用多头注意力池化（PMA）模块，聚合所有token信息，并利用LLM的因果表示。
3. C2LLM在MTEB-Code上取得了显著提升，C2LLM-7B在同等规模模型中排名第一。

## 📝 摘要（中文）

本文介绍了C2LLM，一个对比代码大语言模型家族，包含0.5B和7B两种规模。C2LLM基于Qwen-2.5-Coder骨干网络，采用多头注意力池化（Pooling by Multihead Attention, PMA）模块，从token embedding生成序列embedding，有效地：1）利用了LLM在预训练期间获得的因果表示；2）能够聚合序列中所有token的信息，打破了基于EOS的序列embedding的信息瓶颈；3）支持embedding维度的灵活调整，作为MRL的替代方案。C2LLM模型在三百万公开数据上进行训练，在同等规模的模型中，于MTEB-Code上创造了新的记录，其中C2LLM-7B在总排行榜上排名第一。

## 🔬 方法详解

**问题定义**：现有的代码embedding模型，特别是基于大语言模型（LLM）的方法，通常依赖于EOS（End-of-Sequence）token的embedding来表示整个代码序列。这种方法的痛点在于，EOS token的embedding可能无法充分捕捉序列中的所有信息，造成信息瓶颈，限制了代码检索的性能。此外，固定维度的embedding也缺乏灵活性，难以适应不同的应用场景。

**核心思路**：C2LLM的核心思路是利用多头注意力池化（PMA）模块，将序列中所有token的embedding进行聚合，从而生成更具代表性的序列embedding。PMA模块通过自适应地学习不同token的重要性，有效地捕捉序列中的关键信息，打破了EOS token的信息瓶颈。同时，C2LLM还利用了LLM在预训练过程中学习到的因果表示，进一步提升了embedding的质量。

**技术框架**：C2LLM的整体框架基于Qwen-2.5-Coder骨干网络，并在其基础上添加了PMA模块。具体流程如下：首先，将代码序列输入到Qwen-2.5-Coder中，得到每个token的embedding。然后，将这些token embedding输入到PMA模块中进行聚合，生成序列embedding。最后，使用对比学习的目标函数，在大量代码数据上对模型进行训练，优化embedding的质量。

**关键创新**：C2LLM最重要的技术创新点在于PMA模块的应用。与传统的基于EOS token的方法相比，PMA模块能够更有效地聚合序列中的所有信息，避免了信息瓶颈。此外，PMA模块还支持embedding维度的灵活调整，可以根据不同的应用场景进行优化。

**关键设计**：PMA模块的关键设计包括：多头注意力的头数、注意力机制的类型、池化操作的方式等。论文中可能使用了标准的多头注意力机制，并采用可学习的query向量进行池化。损失函数方面，可能采用了对比学习中常用的InfoNCE损失函数，通过最大化正样本之间的相似度，最小化负样本之间的相似度，来优化embedding的质量。具体参数设置和网络结构细节需要在论文中进一步查找。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21332v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21332v1/x2.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

C2LLM模型在MTEB-Code基准测试中取得了显著的性能提升。C2LLM-7B在同等规模的模型中排名第一，超越了现有的SOTA模型。实验结果表明，PMA模块能够有效地提升代码embedding的质量，打破EOS token的信息瓶颈。具体的性能数据和对比基线需要在论文中进一步查找。

## 🎯 应用场景

C2LLM在代码检索、代码克隆检测、代码摘要生成等领域具有广泛的应用前景。高质量的代码embedding可以提高代码检索的准确率，帮助开发者快速找到所需的代码片段。此外，C2LLM还可以用于代码相似性分析，检测代码中的潜在漏洞和安全风险。未来，C2LLM有望成为代码智能领域的重要基础设施。

## 📄 摘要（原文）

> We present C2LLM - Contrastive Code Large Language Models, a family of code embedding models in both 0.5B and 7B sizes. Building upon Qwen-2.5-Coder backbones, C2LLM adopts a Pooling by Multihead Attention (PMA) module for generating sequence embedding from token embeddings, effectively 1) utilizing the LLM's causal representations acquired during pretraining, while also 2) being able to aggregate information from all tokens in the sequence, breaking the information bottleneck in EOS-based sequence embeddings, and 3) supporting flexible adaptation of embedding dimension, serving as an alternative to MRL. Trained on three million publicly available data, C2LLM models set new records on MTEB-Code among models of similar sizes, with C2LLM-7B ranking 1st on the overall leaderboard.

