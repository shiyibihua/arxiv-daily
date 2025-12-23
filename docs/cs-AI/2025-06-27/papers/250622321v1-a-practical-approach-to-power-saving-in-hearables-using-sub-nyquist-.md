---
layout: default
title: A Practical Approach to Power Saving in Hearables Using Sub-Nyquist Sampling with Bandwidth Extension
---

# A Practical Approach to Power Saving in Hearables Using Sub-Nyquist Sampling with Bandwidth Extension

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22321" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22321v1</a>
  <a href="https://arxiv.org/pdf/2506.22321.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22321v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22321v1', 'A Practical Approach to Power Saving in Hearables Using Sub-Nyquist Sampling with Bandwidth Extension')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tarikul Islam Tamiti, Anomadarshi Barua

**分类**: cs.SD, cs.AI, eess.AS

**发布日期**: 2025-06-27

---

## 💡 一句话要点

**提出SUBARU以解决耳机低功耗处理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `耳机` `低功耗处理` `语音增强` `子奈奎斯特采样` `虚拟鉴别器` `移动平台` `音频质量`

## 📋 核心要点

1. 现有方法未能有效降低耳机的功耗，同时保持语音增强的质量和可懂度。
2. 本文提出SUBARU，通过子奈奎斯特采样和低位深的ADC设计，显著降低功耗并提升音频质量。
3. 实验结果表明，SUBARU在移动平台上实现了1.74毫秒的推理时间和低于13.77MB的内存占用，效果显著。

## 📝 摘要（中文）

耳机是佩戴在耳朵上的可穿戴计算机，使用骨导麦克风（BCM）和空气导麦克风（ACM）进行多模态语音增强。然而，现有研究未考虑在耳机中降低采样频率和位深对低功耗处理和语音质量的影响。本文提出SUBARU（子奈奎斯特音频分辨率上采样），通过子奈奎斯特采样和低位深实现3.31倍的功耗降低，并引入多尺度虚拟鉴别器以达到类似GAN的音频质量，且在移动平台上实现实时处理，推理时间为1.74毫秒，内存占用低于13.77MB。

## 🔬 方法详解

**问题定义**：本文旨在解决耳机在低功耗实现中的不足，特别是采样频率和位深对语音质量的影响。现有方法未能有效处理这些问题，导致功耗高且语音增强效果差。

**核心思路**：论文提出SUBARU，通过采用子奈奎斯特采样和低位深的ADC设计，旨在降低功耗的同时保持语音的可懂度和质量。该方法还引入了虚拟鉴别器，避免了传统GAN训练的复杂性。

**技术框架**：SUBARU的整体架构包括三个主要模块：1) 子奈奎斯特采样模块，负责降低采样频率；2) 虚拟鉴别器模块，进行音频质量提升；3) 实时处理模块，确保在移动平台上的高效运行。

**关键创新**：SUBARU的主要创新在于引入多尺度和多周期的虚拟鉴别器，能够在不使用传统GAN的情况下实现类似的音频质量。这一设计显著简化了模型的训练过程。

**关键设计**：在参数设置上，SUBARU使用了特定的低位深ADC配置，并设计了适应性的损失函数，以优化音频质量和处理速度。网络结构上，采用了多层次的虚拟鉴别器，增强了模型的表现力。

## 📊 实验亮点

实验结果显示，SUBARU在功耗方面实现了3.31倍的降低，同时在移动平台上以1.74毫秒的推理时间和低于13.77MB的内存占用，表现出色。这些结果表明该方法在实际应用中的可行性和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能耳机、助听器及其他可穿戴设备，能够在噪声环境中提供高质量的语音增强。未来，SUBARU的技术可推广至更多低功耗音频处理场景，提升用户体验。

## 📄 摘要（原文）

> Hearables are wearable computers that are worn on the ear. Bone conduction microphones (BCMs) are used with air conduction microphones (ACMs) in hearables as a supporting modality for multimodal speech enhancement (SE) in noisy conditions. However, existing works don't consider the following practical aspects for low-power implementations on hearables: (i) They do not explore how lowering the sampling frequencies and bit resolutions in analog-to-digital converters (ADCs) of hearables jointly impact low-power processing and multimodal SE in terms of speech quality and intelligibility. (ii) They don't discuss how GAN-like audio quality can be achieved without using actual GAN discriminators. And (iii) They don't process signals from ACMs/BCMs at sub-Nyquist sampling rate because, in their frameworks, they lack a wideband reconstruction methodology from their narrowband parts. We propose SUBARU (\textbf{Sub}-Nyquist \textbf{A}udio \textbf{R}esolution \textbf{U}psampling), which achieves the following: SUBARU (i) intentionally uses sub-Nyquist sampling and low bit resolution in ADCs, achieving a 3.31x reduction in power consumption; (ii) introduces novel multi-scale and multi-period virtual discriminators, which achieve GAN-like audio quality without using GANs' adversarial training; and (iii) achieves streaming operations on mobile platforms and SE in in-the-wild noisy conditions with an inference time of 1.74ms and a memory footprint of less than 13.77MB.

