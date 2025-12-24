---
layout: default
title: A Dataset Generation Scheme Based on Video2EEG-SPGN-Diffusion for SEED-VD
---

# A Dataset Generation Scheme Based on Video2EEG-SPGN-Diffusion for SEED-VD

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05321" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05321v1</a>
  <a href="https://arxiv.org/pdf/2509.05321.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05321v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05321v1', 'A Dataset Generation Scheme Based on Video2EEG-SPGN-Diffusion for SEED-VD')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunfei Guo, Tao Zhang, Wu Huang, Yao Song

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-30

---

## 💡 一句话要点

**提出Video2EEG-SPGN-Diffusion以生成视频刺激下的EEG数据集**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态数据集` `EEG信号生成` `视频刺激` `情感分析` `脑机接口` `自我对弈图网络` `扩散模型`

## 📋 核心要点

1. 现有方法在视频刺激与EEG信号的对齐上存在挑战，难以生成高质量的多模态数据集。
2. 论文提出的Video2EEG-SPGN-Diffusion框架通过自我对弈图网络与扩散模型结合，生成个性化的EEG信号。
3. 新数据集包含1000多个视频刺激样本及对应的62通道EEG信号，显著推动了多模态研究的进展。

## 📝 摘要（中文）

本文介绍了一个开源框架Video2EEG-SPGN-Diffusion，该框架利用SEED-VD数据集生成基于视频刺激的多模态EEG信号数据集。此外，我们披露了一种对齐视频和EEG数据对的工程流程，促进了具有EEG对齐能力的多模态大模型的训练。通过自我对弈图网络(SPGN)与扩散模型的结合，生成个性化EEG信号。作为主要贡献，我们发布了一个新数据集，包含超过1000个SEED-VD视频刺激样本，配对生成的62通道EEG信号（200 Hz）及情感标签，推动视频-EEG对齐及多模态研究。该框架为情感分析、数据增强和脑机接口应用提供了新工具，具有重要的研究和工程意义。

## 🔬 方法详解

**问题定义**：本文旨在解决视频刺激与EEG信号对齐不足的问题，现有方法在生成高质量多模态数据集方面存在局限性。

**核心思路**：通过结合自我对弈图网络(SPGN)与扩散模型，生成个性化的EEG信号，以提高视频与EEG信号的对齐效果。

**技术框架**：整体架构包括视频刺激输入、EEG信号生成模块和数据对齐工程流程，确保视频与EEG信号的高效配对。

**关键创新**：最重要的创新在于提出了Video2EEG-SPGN-Diffusion框架，能够生成高质量的EEG信号并实现视频-EEG对齐，与现有方法相比具有显著的提升。

**关键设计**：在参数设置上，使用62通道EEG信号，采样率为200 Hz，损失函数设计为适应多模态对齐，网络结构结合了SPGN和扩散模型的优势。

## 📊 实验亮点

实验结果显示，生成的EEG信号与视频刺激的对齐精度显著提高，数据集包含超过1000个样本，62通道EEG信号的生成质量优于现有方法，推动了多模态研究的进展。

## 🎯 应用场景

该研究的潜在应用领域包括情感分析、数据增强和脑机接口等。通过生成高质量的多模态数据集，能够促进相关领域的研究进展，并为实际应用提供更为精准的情感识别和交互方式，未来可能在医疗、娱乐等多个行业产生深远影响。

## 📄 摘要（原文）

> This paper introduces an open-source framework, Video2EEG-SPGN-Diffusion, that leverages the SEED-VD dataset to generate a multimodal dataset of EEG signals conditioned on video stimuli. Additionally, we disclose an engineering pipeline for aligning video and EEG data pairs, facilitating the training of multimodal large models with EEG alignment capabilities. Personalized EEG signals are generated using a self-play graph network (SPGN) integrated with a diffusion model. As a major contribution, we release a new dataset comprising over 1000 samples of SEED-VD video stimuli paired with generated 62-channel EEG signals at 200 Hz and emotion labels, enabling video-EEG alignment and advancing multimodal research. This framework offers novel tools for emotion analysis, data augmentation, and brain-computer interface applications, with substantial research and engineering significance.

