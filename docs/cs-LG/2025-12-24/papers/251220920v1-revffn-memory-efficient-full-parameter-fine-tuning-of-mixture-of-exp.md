---
layout: default
title: "RevFFN: Memory-Efficient Full-Parameter Fine-Tuning of Mixture-of-Experts LLMs with Reversible Blocks"
---

# RevFFN: Memory-Efficient Full-Parameter Fine-Tuning of Mixture-of-Experts LLMs with Reversible Blocks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20920" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20920v1</a>
  <a href="https://arxiv.org/pdf/2512.20920.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20920v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20920v1', 'RevFFN: Memory-Efficient Full-Parameter Fine-Tuning of Mixture-of-Experts LLMs with Reversible Blocks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ningyuan Liu, Jing Yang, Kaitong Cai, Keze Wang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-24

**备注**: Under submission

---

## 💡 一句话要点

**RevFFN：利用可逆块实现MoE LLM全参数高效微调**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `全参数微调` `混合专家模型` `内存优化` `可逆神经网络`

## 📋 核心要点

1. 现有全参数微调方法因需缓存大量中间激活值，导致内存开销巨大，限制了大规模LLM的微调。
2. RevFFN通过可逆Transformer块，在反向传播时从输出重建输入激活，避免存储大量中间激活值，降低内存消耗。
3. RevFFN能够在单个GPU上实现高效的全参数微调，同时保持MoE架构的表达能力。

## 📝 摘要（中文）

全参数微调是使大型语言模型（LLM）适应下游任务的关键技术，但由于需要缓存大量的中间激活值以进行反向传播，因此会产生巨大的内存开销。这一瓶颈使得对当前大规模LLM进行全参数微调在实践中具有挑战性。现有的分布式训练框架（如DeepSpeed）使用ZeRO和FSDP等技术来缓解这个问题，这些技术依赖于多GPU内存或CPU卸载，但通常需要额外的硬件资源并降低训练速度。我们引入了RevFFN，这是一种用于混合专家（MoE）LLM的内存高效微调范例。RevFFN采用精心设计的可逆Transformer块，允许在反向传播期间从输出重建层输入激活，从而无需在内存中存储大多数中间激活。在保留MoE架构的表达能力的同时，这种方法显著降低了全参数微调的峰值内存消耗。因此，RevFFN能够在单个消费级或服务器级GPU上实现高效的全参数微调。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）全参数微调过程中内存消耗过大的问题。现有方法，如直接反向传播，需要存储所有中间层的激活值，这对于参数量巨大的LLM来说是不可接受的。即使使用分布式训练框架，也需要额外的硬件资源或牺牲训练速度。

**核心思路**：论文的核心思路是利用可逆Transformer块，使得每一层的输入激活可以从输出激活中恢复出来。这样，在反向传播时，只需要存储少量激活值，就可以通过计算重建其他层的激活值，从而显著降低内存占用。

**技术框架**：RevFFN的核心是可逆Transformer块的设计。标准的Transformer块被替换为可逆块，这些块的设计允许从输出计算输入。整体训练流程与标准的全参数微调流程类似，但在反向传播阶段，会动态地重新计算所需的激活值，而不是从内存中读取。

**关键创新**：最关键的创新在于可逆Transformer块的设计，它允许在不显著增加计算量的前提下，避免存储大量的中间激活值。与传统的Transformer块相比，可逆块在结构上进行了调整，使得输入和输出之间存在可逆的映射关系。

**关键设计**：可逆Transformer块的具体设计包括对前馈网络（FFN）的修改，使其具有可逆性。论文可能采用了特定的激活函数或网络结构，以保证可逆性。此外，损失函数和优化器的选择可能也需要进行调整，以适应可逆块的特性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20920v1/x1.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文提出的RevFFN方法显著降低了MoE LLM全参数微调的内存消耗，使得在单个消费级或服务器级GPU上进行高效微调成为可能。具体的性能数据（例如，内存占用降低的百分比、训练速度的提升等）需要在论文中查找。

## 🎯 应用场景

RevFFN技术可广泛应用于各种需要对大型语言模型进行微调的场景，例如自然语言处理、机器翻译、文本生成等。它降低了微调LLM的硬件门槛，使得研究人员和开发者能够在资源有限的环境下进行模型定制和优化，加速LLM在各领域的应用。

## 📄 摘要（原文）

> Full parameter fine tuning is a key technique for adapting large language models (LLMs) to downstream tasks, but it incurs substantial memory overhead due to the need to cache extensive intermediate activations for backpropagation. This bottleneck makes full fine tuning of contemporary large scale LLMs challenging in practice. Existing distributed training frameworks such as DeepSpeed alleviate this issue using techniques like ZeRO and FSDP, which rely on multi GPU memory or CPU offloading, but often require additional hardware resources and reduce training speed. We introduce RevFFN, a memory efficient fine tuning paradigm for mixture of experts (MoE) LLMs. RevFFN employs carefully designed reversible Transformer blocks that allow reconstruction of layer input activations from outputs during backpropagation, eliminating the need to store most intermediate activations in memory. While preserving the expressive capacity of MoE architectures, this approach significantly reduces peak memory consumption for full parameter fine tuning. As a result, RevFFN enables efficient full fine tuning on a single consumer grade or server grade GPU.

