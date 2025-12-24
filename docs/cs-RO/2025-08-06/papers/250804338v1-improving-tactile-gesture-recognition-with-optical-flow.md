---
layout: default
title: Improving Tactile Gesture Recognition with Optical Flow
---

# Improving Tactile Gesture Recognition with Optical Flow

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04338" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04338v1</a>
  <a href="https://arxiv.org/pdf/2508.04338.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04338v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04338v1', 'Improving Tactile Gesture Recognition with Optical Flow')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaohong Zhong, Alessandro Albini, Giammarco Caroleo, Giorgio Cannata, Perla Maiolino

**分类**: cs.RO

**发布日期**: 2025-08-06

**备注**: 7 pages, 7 figures, paper accepted by the 2025 34th IEEE International Conference on Robot and Human Interactive Communication (ROMAN)

---

## 💡 一句话要点

**通过光流增强触觉手势识别的准确性**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `触觉手势识别` `光流` `人机交互` `机器学习` `卷积神经网络` `动态特征提取` `机器人技术`

## 📋 核心要点

1. 现有的触觉手势识别方法主要依赖于触觉图像，难以区分某些相似的手势，导致识别准确率不足。
2. 本文提出通过计算触觉图像的密集光流，显著突出接触动态，从而改善手势识别的准确性。
3. 实验结果显示，使用光流信息增强的触觉图像训练的分类器，手势分类准确率提高了9%。

## 📝 摘要（中文）

触觉手势识别系统在人与机器人交互中至关重要，能够实现直观的沟通。现有文献主要通过机器学习技术对触觉图像序列进行分类，但仅依靠触觉图像的信息，某些手势难以区分。本文提出了一种简单有效的方法，通过计算密集光流来突出触觉图像中的接触动态，从而提高手势识别分类器的准确性。实验结果表明，使用光流信息增强的触觉图像训练的分类器相比于标准触觉图像训练的分类器，手势分类准确率提高了9%。

## 🔬 方法详解

**问题定义**：本文旨在解决触觉手势识别中，依赖触觉图像导致的手势区分困难的问题。现有方法在处理相似手势时，准确率不足，无法有效捕捉接触动态信息。

**核心思路**：论文的核心思路是通过计算触觉图像的密集光流，来增强输入数据的动态信息。这种设计使得分类器能够更好地区分在触觉图像上相似但接触动态不同的手势。

**技术框架**：整体架构包括数据预处理、光流计算、特征提取和分类器训练四个主要模块。首先对触觉图像进行预处理，然后计算其光流，接着提取特征，最后使用增强后的数据训练分类器。

**关键创新**：最重要的技术创新点在于引入光流信息作为触觉图像的补充特征，这与传统方法仅依赖静态触觉图像的方式有本质区别。

**关键设计**：在参数设置上，光流计算采用了密集光流算法，损失函数使用交叉熵损失，网络结构则基于卷积神经网络（CNN）进行设计，以适应增强后的输入特征。

## 📊 实验亮点

实验结果表明，使用光流信息增强的触觉图像训练的分类器相比于标准触觉图像训练的分类器，手势分类准确率提高了9%。这一显著提升展示了光流在触觉手势识别中的重要性，为未来的研究提供了新的方向。

## 🎯 应用场景

该研究的潜在应用领域包括人机交互、机器人控制和智能家居等。通过提高触觉手势识别的准确性，可以实现更自然的交互方式，提升用户体验。此外，未来可能在医疗、辅助技术等领域发挥重要作用，帮助残障人士更好地与环境互动。

## 📄 摘要（原文）

> Tactile gesture recognition systems play a crucial role in Human-Robot Interaction (HRI) by enabling intuitive communication between humans and robots. The literature mainly addresses this problem by applying machine learning techniques to classify sequences of tactile images encoding the pressure distribution generated when executing the gestures. However, some gestures can be hard to differentiate based on the information provided by tactile images alone. In this paper, we present a simple yet effective way to improve the accuracy of a gesture recognition classifier. Our approach focuses solely on processing the tactile images used as input by the classifier. In particular, we propose to explicitly highlight the dynamics of the contact in the tactile image by computing the dense optical flow. This additional information makes it easier to distinguish between gestures that produce similar tactile images but exhibit different contact dynamics. We validate the proposed approach in a tactile gesture recognition task, showing that a classifier trained on tactile images augmented with optical flow information achieved a 9% improvement in gesture classification accuracy compared to one trained on standard tactile images.

