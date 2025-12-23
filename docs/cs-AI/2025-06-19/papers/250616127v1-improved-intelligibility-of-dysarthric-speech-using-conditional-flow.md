---
layout: default
title: Improved Intelligibility of Dysarthric Speech using Conditional Flow Matching
---

# Improved Intelligibility of Dysarthric Speech using Conditional Flow Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16127" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16127v1</a>
  <a href="https://arxiv.org/pdf/2506.16127.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16127v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16127v1', 'Improved Intelligibility of Dysarthric Speech using Conditional Flow Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shoutrik Das, Nishant Singh, Arjun Gangwar, S Umesh

**分类**: cs.SD, cs.AI, eess.AS

**发布日期**: 2025-06-19

**备注**: Accepted at Interspeech 2025

---

## 💡 一句话要点

**提出条件流匹配以改善构音障碍语音的可懂性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `构音障碍` `语音转换` `条件流匹配` `自监督学习` `扩散变换器` `离散声学单元` `语音可懂性`

## 📋 核心要点

1. 构音障碍患者的语音可懂性显著降低，现有的转换技术在处理这种语音时存在局限性。
2. 本研究提出了一种基于条件流匹配的非自回归方法，旨在直接将构音障碍语音转换为清晰语音。
3. 实验结果显示，使用离散声学单元可以有效提高语音可懂性，并且收敛速度优于传统方法。

## 📝 摘要（中文）

构音障碍是一种显著影响语音可懂性的神经系统疾病，常导致患者无法有效沟通。因此，开发稳健的构音障碍到正常语音的转换技术显得尤为重要。本研究探讨了自监督学习（SSL）特征及其量化表示作为语音生成的替代方案，并提出了一种完全非自回归的方法，利用条件流匹配（CFM）与扩散变换器直接映射构音障碍语音到清晰语音。研究结果表明，离散声学单元在提高可懂性方面表现出色，同时与传统的梅尔频谱法相比，收敛速度更快。

## 🔬 方法详解

**问题定义**：本论文旨在解决构音障碍语音的可懂性问题，现有的语音转换方法在处理此类语音时常常效果不佳，难以满足实际沟通需求。

**核心思路**：论文提出了一种基于条件流匹配（CFM）的完全非自回归方法，通过直接映射构音障碍语音到清晰语音，克服了传统方法的局限性。

**技术框架**：整体架构包括特征提取、条件流匹配模块和扩散变换器。特征提取使用WavLM提取单一说话者的干净语音特征，随后通过CFM进行映射，最后生成清晰语音。

**关键创新**：最重要的创新在于引入了条件流匹配与扩散变换器的结合，利用离散声学单元来提升语音的可懂性，显著提高了转换的效率与效果。

**关键设计**：在参数设置上，采用了特定的损失函数以优化语音生成质量，同时网络结构设计上注重了对离散声学单元的有效利用，以加速收敛过程。

## 📊 实验亮点

实验结果表明，使用条件流匹配方法的模型在语音可懂性上较传统梅尔频谱方法有显著提升，具体性能数据未提供，但收敛速度明显加快，展示了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括辅助沟通设备、语音治疗工具以及智能语音助手等。通过改善构音障碍患者的语音可懂性，能够极大提升他们的沟通能力和生活质量，具有重要的社会价值和实际意义。

## 📄 摘要（原文）

> Dysarthria is a neurological disorder that significantly impairs speech intelligibility, often rendering affected individuals unable to communicate effectively. This necessitates the development of robust dysarthric-to-regular speech conversion techniques. In this work, we investigate the utility and limitations of self-supervised learning (SSL) features and their quantized representations as an alternative to mel-spectrograms for speech generation. Additionally, we explore methods to mitigate speaker variability by generating clean speech in a single-speaker voice using features extracted from WavLM. To this end, we propose a fully non-autoregressive approach that leverages Conditional Flow Matching (CFM) with Diffusion Transformers to learn a direct mapping from dysarthric to clean speech. Our findings highlight the effectiveness of discrete acoustic units in improving intelligibility while achieving faster convergence compared to traditional mel-spectrogram-based approaches.

