---
layout: default
title: Finite Scalar Quantization Enables Redundant and Transmission-Robust Neural Audio Compression at Low Bit-rates
---

# Finite Scalar Quantization Enables Redundant and Transmission-Robust Neural Audio Compression at Low Bit-rates

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09550" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09550v2</a>
  <a href="https://arxiv.org/pdf/2509.09550.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09550v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09550v2', 'Finite Scalar Quantization Enables Redundant and Transmission-Robust Neural Audio Compression at Low Bit-rates')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Harry Julian, Rachel Beeson, Lohith Konathala, Johanna Ulin, Jiameng Gao

**分类**: cs.SD, cs.LG

**发布日期**: 2025-09-11 (更新: 2025-09-12)

---

## 💡 一句话要点

**NeuCodec：基于有限标量量化的鲁棒性神经音频压缩编码**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `神经音频编码` `有限标量量化` `鲁棒性` `编码器蒸馏` `低比特率压缩`

## 📋 核心要点

1. 现有神经音频编解码器多依赖残差矢量量化，训练复杂且码本单一，限制了其在噪声环境下的性能。
2. NeuCodec采用有限标量量化，简化训练流程，并利用其天然的冗余性，增强编码在噪声信道中的鲁棒性。
3. 实验表明，NeuCodec在噪声信道中传输时，比特级扰动鲁棒性远优于RVQ编解码器，且编码器蒸馏实验验证了其冗余性。

## 📝 摘要（中文）

神经音频编解码器(NACs)因其卓越的率失真性能以及与大型语言模型(LLMs)的兼容性（作为音频生成的离散特征表示）而在语音处理任务中得到越来越多的应用。虽然大多数现有编解码器依赖于残差矢量量化(RVQ)，但有限标量量化(FSQ)最近作为一种引人注目的替代方案出现，它简化了训练并原生支持单个码本。我们介绍NeuCodec，一种基于FSQ的NAC，并表明FSQ编码具有内置冗余，从而产生一种在噪声信道中传输时具有鲁棒性的编码。首先，通过编码器蒸馏实验，我们表明两个不同的编码器可以学习将相同的音频编码成截然不同的代码序列，同时使用相同的量化器和解码器保持相当的重建质量。其次，我们通过模拟代码序列通过噪声信道的传输，比较RVQ和FSQ编解码器的性能，证明FSQ具有明显优越的比特级扰动鲁棒性。

## 🔬 方法详解

**问题定义**：现有神经音频编解码器（NACs）主要依赖残差矢量量化（RVQ），存在训练复杂、码本单一等问题，导致在噪声信道中传输时鲁棒性较差。因此，需要一种更简单、更鲁棒的音频压缩方法，以适应实际应用场景。

**核心思路**：论文的核心思路是利用有限标量量化（FSQ）替代RVQ。FSQ简化了训练过程，并且其固有的冗余性可以提高编码对噪声的抵抗能力。通过设计基于FSQ的神经音频编解码器NeuCodec，并结合编码器蒸馏，进一步增强了编码的鲁棒性。

**技术框架**：NeuCodec的整体框架包括编码器、有限标量量化器和解码器三个主要模块。编码器将输入音频转换为潜在表示，然后通过FSQ进行量化，得到离散的代码序列。解码器则将代码序列转换回音频信号。此外，论文还采用了编码器蒸馏技术，训练多个编码器将相同的音频编码成不同的代码序列，进一步增加冗余性。

**关键创新**：论文的关键创新在于将有限标量量化（FSQ）应用于神经音频压缩，并利用其内在的冗余性来提高编码的鲁棒性。与传统的RVQ方法相比，FSQ简化了训练过程，并且通过编码器蒸馏，可以生成具有更高冗余度的编码，从而在噪声信道中表现更好。

**关键设计**：论文的关键设计包括：1) 使用有限标量量化器进行音频特征的离散化；2) 设计基于FSQ的神经音频编解码器NeuCodec；3) 采用编码器蒸馏技术，训练多个编码器生成不同的代码序列，增加冗余性；4) 通过模拟噪声信道传输，评估不同编解码器的鲁棒性。

## 📊 实验亮点

实验结果表明，基于FSQ的NeuCodec在噪声信道中传输时，比特级扰动鲁棒性远优于RVQ编解码器。编码器蒸馏实验也验证了FSQ编码的冗余性，即不同的编码器可以将相同的音频编码成差异很大的代码序列，同时保持相当的重建质量。这些结果表明NeuCodec在低比特率下具有更好的性能和鲁棒性。

## 🎯 应用场景

该研究成果可应用于语音通信、音频存储、流媒体传输等领域，尤其是在信道条件较差的环境下，例如移动通信、卫星通信等。通过提高音频编码的鲁棒性，可以改善用户体验，并降低数据传输的错误率。此外，该方法还可以应用于音频生成任务，为大型语言模型提供更可靠的离散特征表示。

## 📄 摘要（原文）

> Neural Audio Codecs (NACs) have become increasingly adopted in speech processing tasks due to their excellent rate-distortion performance and compatibility with Large Language Models (LLMs) as discrete feature representations for audio generation. While most existing codecs rely on Residual Vector Quantization (RVQ), Finite Scalar Quantization (FSQ) has recently emerged as a compelling alternative that simplifies training and natively supports single codebooks. We introduce NeuCodec, an FSQ-based NAC, and show that FSQ encodes baked-in redundancy which produces an encoding which is robust when transmitted through noisy channels. First, through an encoder distillation experiment, we show that two different encoders can learn to encode identical audio into vastly different code sequences whilst maintaining comparable reconstruction quality with the same quantizer and decoder. Second, we demonstrate that FSQ has vastly superior bit-level perturbation robustness by comparing the performance of RVQ and FSQ codecs when simulating the transmission of code sequences through a noisy channel.

