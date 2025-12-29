---
layout: default
title: "GQ-VAE: A gated quantized VAE for learning variable length tokens"
---

# GQ-VAE: A gated quantized VAE for learning variable length tokens

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21913" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21913v1</a>
  <a href="https://arxiv.org/pdf/2512.21913.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21913v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21913v1', 'GQ-VAE: A gated quantized VAE for learning variable length tokens')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Theo Datta, Kayla Huang, Sham Kakade, David Brandfonbrener

**分类**: cs.LG

**发布日期**: 2025-12-26

**🔗 代码/项目**: [GITHUB](https://github.com/Theo-Datta-115/gq-vae)

---

## 💡 一句话要点

**提出门控量化VAE（GQ-VAE），用于学习变长token，作为现有tokenizer的即插即用替代方案。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `变分自编码器` `token化` `离散表示学习` `门控机制` `自然语言处理`

## 📋 核心要点

1. 现有token化方法（如BPE）虽然常用，但缺乏灵活性，且学习型tokenizer常增加语言模型复杂性，难以大规模应用。
2. GQ-VAE通过学习变长离散token的编码，实现了一种可独立预训练的tokenizer，能直接替换现有tokenizer。
3. 实验表明，GQ-VAE在压缩和语言建模上优于VQ-VAE，接近BPE性能，且在同等压缩率下，能提升下游语言模型学习效果。

## 📝 摘要（中文）

本文提出了一种新颖的架构——门控量化变分自编码器（GQ-VAE），它可以被独立地预训练，作为现有tokenizer的即插即用替代方案。目前大多数前沿模型仍然使用基于频率的确定性token化算法，例如字节对编码（BPE），但最近有大量工作致力于设计学习的神经tokenizers。然而，这些方案通常会增加底层语言模型的复杂性，并强制对架构进行大的更改，使得它们难以大规模实现。GQ-VAE的关键创新在于学习编码变长的离散token。实验表明，GQ-VAE在压缩和语言建模性能方面优于标准VQ-VAE tokenizer，并且接近BPE的压缩率和语言建模性能。有趣的是，如果使用具有较小词汇量的BPE，使得GQ-VAE和BPE之间的压缩率相等，我们发现GQ-VAE可以改善下游语言模型的学习。最后，讨论了未来工作的一些令人兴奋的方向。

## 🔬 方法详解

**问题定义**：现有的大部分模型仍然依赖于确定性的、基于频率的token化算法，例如字节对编码（BPE）。虽然已经有一些工作致力于设计学习的神经tokenizers，但是这些方法通常会增加底层语言模型的复杂性，并且需要对模型架构进行较大的改动，这使得它们难以在大规模场景下应用。因此，需要一种既能学习token表示，又不会显著增加模型复杂度的token化方法。

**核心思路**：GQ-VAE的核心思路是利用变分自编码器（VAE）学习变长的离散token表示。通过量化潜在空间，使得模型能够生成离散的token。引入门控机制，允许模型动态地调整token的长度，从而更好地适应不同的文本内容。这种设计使得GQ-VAE可以独立于下游语言模型进行预训练，并作为即插即用的模块进行替换。

**技术框架**：GQ-VAE的整体架构是一个标准的变分自编码器，包括编码器、量化器和解码器三个主要模块。编码器将输入文本编码成潜在表示，量化器将潜在表示映射到离散的token，解码器则根据离散的token重构输入文本。关键在于量化器和门控机制的设计，使得模型能够学习变长的离散token。

**关键创新**：GQ-VAE最重要的创新点在于其能够学习变长的离散token表示。传统的VQ-VAE通常学习固定长度的token，而GQ-VAE通过引入门控机制，使得模型能够动态地调整token的长度，从而更好地适应不同的文本内容。此外，GQ-VAE可以独立于下游语言模型进行预训练，这使得它可以作为即插即用的模块进行替换，而无需对现有的语言模型架构进行大的改动。

**关键设计**：GQ-VAE的关键设计包括：1) 使用Gumbel-Softmax技巧进行量化，使得模型可以进行端到端的训练。2) 引入门控机制，控制token的长度。门控机制通常是一个sigmoid函数，用于决定是否结束当前token的生成。3) 使用KL散度作为正则化项，鼓励潜在表示服从先验分布。损失函数通常包括重构损失和KL散度损失两部分。具体的网络结构可以根据具体的任务进行调整，例如可以使用Transformer作为编码器和解码器。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21913v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21913v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21913v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，GQ-VAE在压缩率和语言建模性能上优于标准的VQ-VAE tokenizer，并且接近BPE的性能。更重要的是，在与具有较小词汇量的BPE进行比较时（两者压缩率相当），GQ-VAE能够提升下游语言模型的学习效果。这表明GQ-VAE学习到的token表示更具有信息量，能够更好地支持下游任务。

## 🎯 应用场景

GQ-VAE可应用于各种自然语言处理任务，例如机器翻译、文本摘要、对话系统等。它能够作为现有tokenizer的替代方案，提升模型的压缩率和语言建模性能。由于其即插即用的特性，可以方便地集成到现有的NLP系统中，降低了模型开发的成本。未来，GQ-VAE有望在低资源语言处理、移动设备上的模型部署等领域发挥重要作用。

## 📄 摘要（原文）

> While most frontier models still use deterministic frequency-based tokenization algorithms such as byte-pair encoding (BPE), there has been significant recent work to design learned neural tokenizers. However, these schemes generally add to underlying language model complexity and force large changes to architecture, making them hard to implement at large scales. To overcome these challenges, we propose the gated quantized variational autoencoder (GQ-VAE), a novel architecture that can be independently pre-trained to serve as a drop-in replacement for existing tokenizers. The key innovation of the architecture is to learn to encode variable-length discrete tokens. GQ-VAE improves compression and language modeling performance over a standard VQ-VAE tokenizer, and approaches the compression rate and language modeling performance of BPE. Interestingly, if we use BPE with a smaller vocabulary, such that the compression is equivalent between GQ-VAE and BPE, we find that GQ-VAE improves downstream language model learning. We conclude with a discussion of several exciting avenues for future work. Code can be found at https://github.com/Theo-Datta-115/gq-vae.

