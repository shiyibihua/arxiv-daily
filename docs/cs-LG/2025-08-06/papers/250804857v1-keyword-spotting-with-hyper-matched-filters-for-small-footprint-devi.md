---
layout: default
title: Keyword Spotting with Hyper-Matched Filters for Small Footprint Devices
---

# Keyword Spotting with Hyper-Matched Filters for Small Footprint Devices

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04857" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04857v1</a>
  <a href="https://arxiv.org/pdf/2508.04857.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04857v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04857v1', 'Keyword Spotting with Hyper-Matched Filters for Small Footprint Devices')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yael Segal-Feldman, Ann R. Bradlow, Matthew Goldrick, Joseph Keshet

**分类**: eess.AS, cs.LG, cs.SD

**发布日期**: 2025-08-06

**备注**: pre-print

---

## 💡 一句话要点

**提出一种开放词汇的关键词检测模型以解决小型设备的检测精度问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `关键词检测` `开放词汇` `小型设备` `超网络` `卷积滤波器` `语音识别` `模型优化`

## 📋 核心要点

1. 现有的关键词检测方法在小型设备上面临检测精度不足和资源消耗高的挑战。
2. 本文提出的模型通过超网络生成关键词特定的卷积滤波器，优化了关键词检测过程。
3. 实验结果显示，该模型在多种条件下表现优异，尤其是在小型设备上实现了高效的关键词检测。

## 📝 摘要（中文）

开放词汇关键词检测（KWS）是指在语音录音中检测单词或术语的任务，无论这些单词是否包含在训练数据中。本文提出了一种具有最先进检测精度的开放词汇关键词检测模型，适用于小型设备。该模型由语音编码器、目标关键词编码器和检测网络组成。语音编码器可以是小型Whisper或小型Conformer。目标关键词编码器作为超网络实现，将所需关键词作为字符字符串输入，生成卷积层的独特权重集，视为关键词特定的匹配滤波器。检测网络利用匹配滤波器权重进行关键词特定卷积，指导Perceiver模块的交叉注意机制判断目标术语是否出现在录音中。结果表明，该系统在检测性能上达到最先进水平，并有效泛化到域外条件，包括第二语言（L2）语音。值得注意的是，我们最小的模型仅有420万参数，性能与几倍更大的模型相当或更优，展示了其效率和鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决小型设备上开放词汇关键词检测的精度和效率问题。现有方法通常需要大量计算资源，难以在资源受限的设备上实现高效检测。

**核心思路**：论文的核心思路是使用超网络生成关键词特定的卷积滤波器，从而实现高效的关键词检测。通过这种方式，模型能够在不依赖于大量训练数据的情况下，灵活地识别各种关键词。

**技术框架**：整体架构包括三个主要模块：语音编码器（如小型Whisper或小型Conformer）、目标关键词编码器（超网络）和检测网络。语音编码器负责提取语音特征，目标关键词编码器生成特定于关键词的卷积权重，检测网络则执行关键词检测。

**关键创新**：最重要的技术创新在于引入超网络作为关键词编码器，能够动态生成匹配滤波器权重。这一设计使得模型在小型设备上实现了高效的关键词检测，显著提高了检测精度。

**关键设计**：模型的关键设计包括使用小型的语音编码器以减少计算负担，以及通过超网络生成的卷积层权重来实现关键词特定的匹配滤波。损失函数的设计也经过优化，以确保模型在多种语言和口音下的鲁棒性。

## 📊 实验亮点

实验结果表明，提出的模型在关键词检测性能上达到了最先进水平，尤其是在小型设备上表现突出。最小模型仅有420万参数，却与几倍更大的模型相当或更优，展示了其在效率和鲁棒性方面的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居设备、移动设备和语音助手等小型设备中，能够实现高效的关键词检测。其实际价值在于提升用户体验，使设备能够更准确地响应用户指令，未来可能推动更多基于语音的交互技术的发展。

## 📄 摘要（原文）

> Open-vocabulary keyword spotting (KWS) refers to the task of detecting words or terms within speech recordings, regardless of whether they were included in the training data. This paper introduces an open-vocabulary keyword spotting model with state-of-the-art detection accuracy for small-footprint devices. The model is composed of a speech encoder, a target keyword encoder, and a detection network. The speech encoder is either a tiny Whisper or a tiny Conformer. The target keyword encoder is implemented as a hyper-network that takes the desired keyword as a character string and generates a unique set of weights for a convolutional layer, which can be considered as a keyword-specific matched filter. The detection network uses the matched-filter weights to perform a keyword-specific convolution, which guides the cross-attention mechanism of a Perceiver module in determining whether the target term appears in the recording. The results indicate that our system achieves state-of-the-art detection performance and generalizes effectively to out-of-domain conditions, including second-language (L2) speech. Notably, our smallest model, with just 4.2 million parameters, matches or outperforms models that are several times larger, demonstrating both efficiency and robustness.

