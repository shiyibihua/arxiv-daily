---
layout: default
title: Joint Transcription of Acoustic Guitar Strumming Directions and Chords
---

# Joint Transcription of Acoustic Guitar Strumming Directions and Chords

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07973" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07973v1</a>
  <a href="https://arxiv.org/pdf/2508.07973.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07973v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07973v1', 'Joint Transcription of Acoustic Guitar Strumming Directions and Chords')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sebastian Murgul, Johannes Schimper, Michael Heizmann

**分类**: cs.SD, cs.CL, eess.AS

**发布日期**: 2025-08-11

**备注**: Accepted to the 26th International Society for Music Information Retrieval Conference (ISMIR), 2025

---

## 💡 一句话要点

**提出一种深度学习模型以解决吉他扫弦方向与和弦的自动转录问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `吉他扫弦` `音频转录` `深度学习` `多模态数据` `音乐信息检索`

## 📋 核心要点

1. 现有方法在吉他扫弦转录中面临数据集不足的问题，导致效果不佳。
2. 本文提出了一种基于深度学习的转录模型，并引入了新的真实和合成数据集。
3. 实验结果表明，混合数据方法在扫弦检测和和弦分类上显著提高了准确率。

## 📝 摘要（中文）

自动转录吉他扫弦是音乐信息检索（MIR）中一个较少研究且具有挑战性的任务，尤其是在从音频信号中提取扫弦方向和和弦进程方面。现有方法的有效性常因数据集的限制而受到影响。本文通过引入一个新数据集和基于深度学习的转录模型，扩展了多模态吉他扫弦转录的方法。我们使用ESP32智能手表运动传感器和结构化录音协议收集了90分钟的真实吉他录音，并补充了4小时标记的合成扫弦音频数据集。训练的卷积递归神经网络（CRNN）模型能够检测扫弦事件、分类其方向并识别相应和弦。评估结果显示，与基线起始检测算法相比，混合使用合成和真实数据的方法在扫弦动作检测和和弦分类上均取得了显著提升。这些结果突显了深度学习在稳健的吉他扫弦转录中的潜力，并为自动节奏吉他分析开辟了新途径。

## 🔬 方法详解

**问题定义**：本文旨在解决吉他扫弦方向和和弦的自动转录问题。现有方法由于数据集的限制，往往无法有效提取音频信号中的相关信息。

**核心思路**：论文提出了一种结合真实和合成数据的深度学习模型，通过卷积递归神经网络（CRNN）来检测扫弦事件和和弦分类，旨在提高转录的准确性和鲁棒性。

**技术框架**：整体架构包括数据收集、模型训练和评估三个主要阶段。首先，使用ESP32智能手表收集真实吉他录音，然后结合合成数据进行模型训练，最后通过评估验证模型性能。

**关键创新**：最重要的技术创新在于引入了一个新的多模态数据集，并通过深度学习模型实现了扫弦方向和和弦的联合转录，这在现有研究中尚属首次。

**关键设计**：模型采用卷积递归神经网络结构，设置了适当的损失函数以优化扫弦事件检测和和弦分类的性能，同时结合了合成和真实数据以增强模型的泛化能力。

## 📊 实验亮点

实验结果显示，混合使用合成和真实数据的方法在扫弦动作检测和和弦分类上取得了显著提升，准确率超过了基线起始检测算法，展示了深度学习在音乐信息检索中的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括音乐教育、自动伴奏生成和音乐分析工具的开发。通过实现更准确的吉他扫弦转录，可以帮助音乐创作者和学习者更好地理解和应用吉他演奏技巧，提升音乐创作的效率和质量。

## 📄 摘要（原文）

> Automatic transcription of guitar strumming is an underrepresented and challenging task in Music Information Retrieval (MIR), particularly for extracting both strumming directions and chord progressions from audio signals. While existing methods show promise, their effectiveness is often hindered by limited datasets. In this work, we extend a multimodal approach to guitar strumming transcription by introducing a novel dataset and a deep learning-based transcription model. We collect 90 min of real-world guitar recordings using an ESP32 smartwatch motion sensor and a structured recording protocol, complemented by a synthetic dataset of 4h of labeled strumming audio. A Convolutional Recurrent Neural Network (CRNN) model is trained to detect strumming events, classify their direction, and identify the corresponding chords using only microphone audio. Our evaluation demonstrates significant improvements over baseline onset detection algorithms, with a hybrid method combining synthetic and real-world data achieving the highest accuracy for both strumming action detection and chord classification. These results highlight the potential of deep learning for robust guitar strumming transcription and open new avenues for automatic rhythm guitar analysis.

