---
layout: default
title: Describe What You See with Multimodal Large Language Models to Enhance Video Recommendations
---

# Describe What You See with Multimodal Large Language Models to Enhance Video Recommendations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09789" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09789v1</a>
  <a href="https://arxiv.org/pdf/2508.09789.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09789v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09789v1', 'Describe What You See with Multimodal Large Language Models to Enhance Video Recommendations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marco De Nadai, Andreas Damianou, Mounia Lalmas

**分类**: cs.IR, cs.CV

**发布日期**: 2025-08-13

**DOI**: [10.1145/3705328.3759303](https://doi.org/10.1145/3705328.3759303)

---

## 💡 一句话要点

**提出多模态大语言模型以增强视频推荐系统的语义理解**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频推荐` `多模态大语言模型` `自然语言处理` `个性化推荐` `深层语义理解`

## 📋 核心要点

1. 现有视频推荐系统依赖低级特征，缺乏对内容深层语义的理解，导致个性化推荐效果不佳。
2. 本文提出通过多模态大语言模型生成自然语言描述，增强推荐系统对视频内容的理解。
3. 在MicroLens-100K数据集上，所提框架在五个代表性模型中均优于传统特征，显示出显著提升。

## 📝 摘要（中文）

现有的视频推荐系统主要依赖用户定义的元数据或由专门编码器提取的低级视觉和声学信号。这些低级特征虽然描述了屏幕上出现的内容，但缺乏更深层次的语义信息，如意图、幽默感和世界知识，这些因素使得视频片段能够引起观众的共鸣。本文提出了一种简单的、与推荐系统无关的零微调框架，通过提示现成的多模态大语言模型（MLLM）为每个视频片段生成丰富的自然语言描述，从而将高层语义注入推荐流程。实验结果表明，该框架在MicroLens-100K数据集上超越了传统的视频、音频和元数据特征，展示了MLLM作为即时知识提取器的潜力。

## 🔬 方法详解

**问题定义**：现有视频推荐系统主要依赖低级视觉和声学信号，无法捕捉视频内容的深层语义，如意图和幽默感，导致推荐效果不理想。

**核心思路**：本文提出通过多模态大语言模型（MLLM）生成视频片段的自然语言描述，从而将高层语义信息注入推荐流程，提升个性化推荐的准确性。

**技术框架**：整体架构包括三个主要模块：首先，使用MLLM对视频片段进行描述生成；其次，利用先进的文本编码器处理MLLM输出；最后，将处理后的信息输入到标准的协同过滤、基于内容和生成推荐模型中。

**关键创新**：最重要的创新点在于引入MLLM作为即时知识提取器，能够在不进行微调的情况下，直接为推荐系统提供丰富的语义信息，这与传统方法截然不同。

**关键设计**：在设计中，MLLM的输出被用作文本特征，结合了先进的文本编码器，确保了信息的有效传递和处理。具体参数设置和损失函数未在摘要中详细说明，需参考原文获取更多细节。

## 📊 实验亮点

实验结果表明，所提框架在MicroLens-100K数据集上表现优异，超越了传统视频、音频和元数据特征，提升幅度在多个代表性模型中均显著，展示了MLLM在视频推荐中的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体平台、视频流服务和在线教育等，能够显著提升用户体验和内容推荐的相关性。通过更好地理解用户意图和视频内容，未来的推荐系统将更加智能化和个性化，推动内容消费的变革。

## 📄 摘要（原文）

> Existing video recommender systems rely primarily on user-defined metadata or on low-level visual and acoustic signals extracted by specialised encoders. These low-level features describe what appears on the screen but miss deeper semantics such as intent, humour, and world knowledge that make clips resonate with viewers. For example, is a 30-second clip simply a singer on a rooftop, or an ironic parody filmed amid the fairy chimneys of Cappadocia, Turkey? Such distinctions are critical to personalised recommendations yet remain invisible to traditional encoding pipelines. In this paper, we introduce a simple, recommendation system-agnostic zero-finetuning framework that injects high-level semantics into the recommendation pipeline by prompting an off-the-shelf Multimodal Large Language Model (MLLM) to summarise each clip into a rich natural-language description (e.g. "a superhero parody with slapstick fights and orchestral stabs"), bridging the gap between raw content and user intent. We use MLLM output with a state-of-the-art text encoder and feed it into standard collaborative, content-based, and generative recommenders. On the MicroLens-100K dataset, which emulates user interactions with TikTok-style videos, our framework consistently surpasses conventional video, audio, and metadata features in five representative models. Our findings highlight the promise of leveraging MLLMs as on-the-fly knowledge extractors to build more intent-aware video recommenders.

