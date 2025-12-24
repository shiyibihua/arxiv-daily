---
layout: default
title: Majority Bit-Aware Watermarking For Large Language Models
---

# Majority Bit-Aware Watermarking For Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03829" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03829v1</a>
  <a href="https://arxiv.org/pdf/2508.03829.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03829v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03829v1', 'Majority Bit-Aware Watermarking For Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahao Xu, Rui Hu, Zikai Zhang

**分类**: cs.CL, cs.CR

**发布日期**: 2025-08-05

**备注**: Preprint

---

## 💡 一句话要点

**提出MajorMark以解决大语言模型水印质量与解码准确性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `水印技术` `文本生成` `解码准确性` `内容验证` `聚类分析`

## 📋 核心要点

1. 现有多比特水印方案在文本质量与解码准确性之间存在权衡，限制了优先标记集合的大小，影响生成内容的质量。
2. 本文提出的MajorMark方法通过基于多数比特的编码策略，选择优先标记集合，提升了标记的灵活性和采样范围。
3. 实验结果显示，MajorMark在解码准确性和文本生成质量上显著优于现有的多比特水印方案，验证了其有效性。

## 📝 摘要（中文）

随着大语言模型（LLMs）在实际应用中的广泛部署，如何防止其生成有害或误导性内容成为一个重要问题。水印技术作为一种有效的解决方案，通过将可识别的二进制信息嵌入生成文本中，实现来源验证和滥用追踪。尽管现有的多比特水印方案能够嵌入丰富的信息，但通常面临文本质量与解码准确性之间的权衡。本文提出的MajorMark方法通过基于多数比特的编码策略，选择优先的标记集合，从而实现更大且灵活的标记采样。与依赖标记频率分析的解码方法不同，MajorMark采用基于聚类的解码策略，确保在优先标记集合较大时仍能保持高解码准确性。我们还引入了MajorMark$^+$，将消息分为多个块独立编码和解码，进一步提升水印文本的质量和解码准确性。实验结果表明，我们的方法在解码准确性和文本生成质量上显著优于现有的多比特水印基线。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多比特水印方案在文本生成质量与解码准确性之间的权衡问题。现有方法通常需要限制优先标记集合的大小，以确保可靠的消息解码，这导致生成内容质量下降。

**核心思路**：论文提出的MajorMark方法通过基于多数比特的编码策略，选择优先标记集合，允许更大且灵活的标记采样，从而在保持文本质量的同时提高解码准确性。

**技术框架**：MajorMark的整体架构包括两个主要模块：首先是基于多数比特的编码模块，其次是聚类解码模块。编码模块根据消息的多数比特选择标记，而解码模块则通过聚类分析实现高准确性的解码。

**关键创新**：MajorMark的核心创新在于其基于多数比特的编码策略和聚类解码方法，这与传统依赖标记频率分析的解码方式有本质区别，能够在优先标记集合较大时仍保持高解码准确性。

**关键设计**：在参数设置上，MajorMark通过动态调整优先标记集合的大小来优化编码过程，同时在解码时采用聚类算法来提高准确性。MajorMark$^+$进一步将消息分块编码，确保每个块的独立性和可解码性，提升整体水印文本的质量。

## 📊 实验亮点

实验结果表明，MajorMark在解码准确性上提升了XX%，文本生成质量提高了YY%，显著优于现有的多比特水印基线，验证了其在实际应用中的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括内容生成、社交媒体、在线教育等，能够有效防止大语言模型生成的内容被滥用或误用。通过水印技术，用户可以追踪内容来源，确保信息的真实性和可靠性，未来可能对内容审核和版权保护产生深远影响。

## 📄 摘要（原文）

> The growing deployment of Large Language Models (LLMs) in real-world applications has raised concerns about their potential misuse in generating harmful or deceptive content. To address this issue, watermarking techniques have emerged as a promising solution by embedding identifiable binary messages into generated text for origin verification and misuse tracing. While recent efforts have explored multi-bit watermarking schemes capable of embedding rich information such as user identifiers, they typically suffer from the fundamental trade-off between text quality and decoding accuracy: to ensure reliable message decoding, they have to restrict the size of preferred token sets during encoding, yet such restrictions reduce the quality of the generated content. In this work, we propose MajorMark, a novel watermarking method that improves this trade-off through majority bit-aware encoding. MajorMark selects preferred token sets based on the majority bit of the message, enabling a larger and more flexible sampling of tokens. In contrast to prior methods that rely on token frequency analysis for decoding, MajorMark employs a clustering-based decoding strategy, which maintains high decoding accuracy even when the preferred token set is large, thus preserving both content quality and decoding accuracy. We further introduce MajorMark$^+$, which partitions the message into multiple blocks to independently encode and deterministically decode each block, thereby further enhancing the quality of watermarked text and improving decoding accuracy. Extensive experiments on state-of-the-art LLMs demonstrate that our methods significantly enhance both decoding accuracy and text generation quality, outperforming prior multi-bit watermarking baselines.

