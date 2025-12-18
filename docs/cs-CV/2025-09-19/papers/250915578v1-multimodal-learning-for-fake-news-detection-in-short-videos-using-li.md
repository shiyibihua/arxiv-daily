---
layout: default
title: Multimodal Learning for Fake News Detection in Short Videos Using Linguistically Verified Data and Heterogeneous Modality Fusion
---

# Multimodal Learning for Fake News Detection in Short Videos Using Linguistically Verified Data and Heterogeneous Modality Fusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15578" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15578v1</a>
  <a href="https://arxiv.org/pdf/2509.15578.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15578v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15578v1', 'Multimodal Learning for Fake News Detection in Short Videos Using Linguistically Verified Data and Heterogeneous Modality Fusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shanghong Li, Chiam Wen Qi Ruth, Hong Xu, Fang Liu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**提出异构融合网络HFN，用于短视频假新闻检测，提升多模态信息利用率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `短视频假新闻检测` `多模态融合` `异构信息融合` `决策网络` `加权特征融合`

## 📋 核心要点

1. 现有短视频假新闻检测方法难以有效处理视频内容动态性和多模态异构性。
2. HFN通过决策网络动态调整模态权重，并使用加权融合模块处理不完整数据。
3. 在FakeTT和VESV数据集上，HFN的Marco F1指标分别提升了2.71%和4.14%。

## 📝 摘要（中文）

短视频平台的快速发展催生了对先进的假新闻检测方法的需求。由于错误信息传播广泛且易于分享，可能导致严重的社会危害，因此需要此类方法。现有方法通常难以应对短视频内容的动态和多模态特性。本文提出了HFN（异构融合网络），这是一个新颖的多模态框架，集成了视频、音频和文本数据，以评估短视频内容的真实性。HFN引入了一个决策网络，该网络在推理过程中动态调整模态权重，以及一个加权多模态特征融合模块，以确保即使在数据不完整的情况下也能实现稳健的性能。此外，我们贡献了一个全面的数据集VESV（短视频真实性），专门为短视频假新闻检测而设计。在FakeTT和新收集的VESV数据集上进行的实验表明，与最先进的方法相比，Marco F1指标分别提高了2.71%和4.14%。这项工作建立了一个强大的解决方案，能够有效地识别短视频平台复杂环境中的假新闻，为打击错误信息提供更可靠和全面的方法。

## 🔬 方法详解

**问题定义**：该论文旨在解决短视频平台中假新闻检测的问题。现有方法在处理短视频的多模态特性（视频、音频、文本）以及模态数据不完整的情况时表现不佳，无法有效利用异构信息进行准确判断。

**核心思路**：论文的核心思路是设计一个能够动态调整不同模态信息权重的异构融合网络，从而更有效地利用多模态信息进行假新闻检测。通过决策网络学习不同模态的重要性，并使用加权融合模块处理数据缺失的情况，提升模型的鲁棒性和准确性。

**技术框架**：HFN（Heterogeneous Fusion Net）框架主要包含以下几个模块：1) 视频特征提取模块：用于提取视频帧的视觉特征。2) 音频特征提取模块：用于提取音频信号的声学特征。3) 文本特征提取模块：用于提取文本信息的语义特征。4) 决策网络：根据输入数据的特征动态调整不同模态的权重。5) 加权多模态特征融合模块：将不同模态的特征进行加权融合，得到最终的表示。6) 分类器：根据融合后的特征进行真假新闻的分类。

**关键创新**：HFN的关键创新在于引入了决策网络来动态调整模态权重。与传统的多模态融合方法不同，HFN能够根据输入数据的具体情况自适应地调整不同模态的重要性，从而更有效地利用多模态信息。此外，加权多模态特征融合模块能够有效处理数据不完整的情况，提升模型的鲁棒性。

**关键设计**：决策网络的设计是关键。具体来说，决策网络接收来自不同模态的特征作为输入，并输出每个模态的权重。这些权重用于加权融合不同模态的特征。损失函数的设计也至关重要，需要同时考虑分类的准确性和模态权重的合理性。具体的网络结构和参数设置在论文中进行了详细描述，例如，可以使用Transformer结构来建模不同模态之间的关系，并使用交叉熵损失函数来优化分类结果。

## 📊 实验亮点

实验结果表明，HFN在FakeTT和VESV数据集上均取得了显著的性能提升。在FakeTT数据集上，HFN的Marco F1指标比最先进的方法提高了2.71%；在VESV数据集上，HFN的Marco F1指标提高了4.14%。这些结果验证了HFN在短视频假新闻检测方面的有效性和优越性。

## 🎯 应用场景

该研究成果可应用于短视频平台的内容审核，自动识别和过滤虚假新闻，减少错误信息的传播，维护网络空间的健康。此外，该技术还可以扩展到其他多媒体内容的真实性验证，例如在线广告、社交媒体帖子等，具有广泛的应用前景和社会价值。

## 📄 摘要（原文）

> The rapid proliferation of short video platforms has necessitated advanced methods for detecting fake news. This need arises from the widespread influence and ease of sharing misinformation, which can lead to significant societal harm. Current methods often struggle with the dynamic and multimodal nature of short video content. This paper presents HFN, Heterogeneous Fusion Net, a novel multimodal framework that integrates video, audio, and text data to evaluate the authenticity of short video content. HFN introduces a Decision Network that dynamically adjusts modality weights during inference and a Weighted Multi-Modal Feature Fusion module to ensure robust performance even with incomplete data. Additionally, we contribute a comprehensive dataset VESV (VEracity on Short Videos) specifically designed for short video fake news detection. Experiments conducted on the FakeTT and newly collected VESV datasets demonstrate improvements of 2.71% and 4.14% in Marco F1 over state-of-the-art methods. This work establishes a robust solution capable of effectively identifying fake news in the complex landscape of short video platforms, paving the way for more reliable and comprehensive approaches in combating misinformation.

