---
layout: default
title: Autoregressive Universal Video Segmentation Model
---

# Autoregressive Universal Video Segmentation Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19242" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19242v1</a>
  <a href="https://arxiv.org/pdf/2508.19242.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19242v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19242v1', 'Autoregressive Universal Video Segmentation Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Miran Heo, Sukjun Hwang, Min-Hung Chen, Yu-Chiang Frank Wang, Albert Gu, Seon Joo Kim, Ryo Hachiuma

**分类**: cs.CV

**发布日期**: 2025-08-26

---

## 💡 一句话要点

**提出自回归通用视频分割模型以解决无提示分割问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频分割` `自回归模型` `状态空间模型` `无提示分割` `并行训练`

## 📋 核心要点

1. 现有视频分割方法多依赖于提示，无法满足无提示分割的实际需求，导致任务特定模型和流程的碎片化。
2. 本文提出自回归通用分割模型（AUSM），将流视频分割视为序列掩码预测，统一了提示和无提示分割的处理方式。
3. 在多个标准基准测试上，AUSM的性能超越了现有方法，并在16帧序列上实现了高达2.5倍的训练速度提升。

## 📝 摘要（中文）

近年来，视频基础模型如SAM2在提示视频分割方面表现出色，但许多实际场景需要无提示分割，即在没有外部提示的情况下检测和跟踪视频中的所有对象。本文将流视频分割重新定义为序列掩码预测，提出自回归通用分割模型（AUSM），该模型统一了提示和无提示视频分割。AUSM基于最新的状态空间模型，能够处理任意长度的视频流，并且所有组件均设计为跨帧并行训练，从而显著加快训练速度。在标准基准测试上，AUSM超越了之前的通用流视频分割方法，并在16帧序列上实现了最高2.5倍的训练加速。

## 🔬 方法详解

**问题定义**：本文旨在解决当前视频分割方法在无提示分割场景中的不足，现有方法往往依赖于外部提示，导致在实际应用中无法有效检测和跟踪所有对象。

**核心思路**：论文提出的自回归通用分割模型（AUSM）通过将视频分割视为序列掩码预测，借鉴语言建模的思想，能够在无提示的情况下进行有效的对象检测和跟踪。

**技术框架**：AUSM基于状态空间模型，维护固定大小的空间状态，能够处理任意长度的视频流。模型的所有组件均设计为支持跨帧并行训练，从而提高训练效率。

**关键创新**：AUSM的主要创新在于其统一了提示和无提示视频分割的处理方式，采用自回归的方式进行序列掩码预测，显著提升了模型的通用性和灵活性。

**关键设计**：在模型设计中，AUSM采用了固定大小的空间状态，结合并行训练策略，优化了训练速度和效率。损失函数和网络结构的设计也经过精心调整，以适应视频分割任务的需求。

## 📊 实验亮点

在标准基准测试（如DAVIS17、YouTube-VOS 2018 & 2019等）中，AUSM的性能超越了以往的通用流视频分割方法，并在16帧序列上实现了高达2.5倍的训练速度提升，显示出显著的效率优势。

## 🎯 应用场景

该研究在视频监控、自动驾驶、虚拟现实等领域具有广泛的应用潜力。通过实现高效的无提示视频分割，AUSM能够提升对象检测和跟踪的准确性，为实时视频分析提供支持，进而推动智能系统的发展。

## 📄 摘要（原文）

> Recent video foundation models such as SAM2 excel at prompted video segmentation by treating masks as a general-purpose primitive. However, many real-world settings require unprompted segmentation that aims to detect and track all objects in a video without external cues, leaving today's landscape fragmented across task-specific models and pipelines. We recast streaming video segmentation as sequential mask prediction, analogous to language modeling, and introduce the Autoregressive Universal Segmentation Model (AUSM), a single architecture that unifies both prompted and unprompted video segmentation. Built on recent state-space models, AUSM maintains a fixed-size spatial state and scales to video streams of arbitrary length. Furthermore, all components of AUSM are designed for parallel training across frames, yielding substantial speedups over iterative training. On standard benchmarks (DAVIS17, YouTube-VOS 2018 & 2019, MOSE, YouTube-VIS 2019 & 2021, and OVIS) AUSM outperforms prior universal streaming video segmentation methods and achieves up to 2.5x faster training on 16-frame sequences.

