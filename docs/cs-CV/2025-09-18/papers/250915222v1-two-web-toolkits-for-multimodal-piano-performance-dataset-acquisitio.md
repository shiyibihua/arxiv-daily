---
layout: default
title: Two Web Toolkits for Multimodal Piano Performance Dataset Acquisition and Fingering Annotation
---

# Two Web Toolkits for Multimodal Piano Performance Dataset Acquisition and Fingering Annotation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15222" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15222v1</a>
  <a href="https://arxiv.org/pdf/2509.15222.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15222v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15222v1', 'Two Web Toolkits for Multimodal Piano Performance Dataset Acquisition and Fingering Annotation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junhyung Park, Yonghyun Kim, Joonhyung Bae, Kirak Kim, Taegyun Kwon, Alexander Lerch, Juhan Nam

**分类**: cs.SD, cs.CV, cs.MM, eess.AS, eess.IV

**发布日期**: 2025-09-18

**备注**: Accepted to the Late-Breaking Demo Session of the 26th International Society for Music Information Retrieval (ISMIR) Conference, 2025

---

## 💡 一句话要点

**提出用于多模态钢琴演奏数据集采集与指法标注的Web工具包**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态数据采集` `钢琴演奏` `指法标注` `Web工具包` `图形用户界面`

## 📋 核心要点

1. 大规模多模态钢琴演奏数据集的获取困难，是制约相关研究发展的瓶颈。
2. 论文提出一个集成的Web工具包，包含数据采集和指法标注两个图形界面，简化数据获取流程。
3. 该工具包能够同步采集音频、视频、MIDI和元数据，并支持从视觉数据中高效标注指法。

## 📝 摘要（中文）

钢琴演奏是一种多模态活动，它将物理动作与声音表现内在结合。尽管人们对分析钢琴演奏的多模态特性越来越感兴趣，但获取大规模多模态数据的繁琐过程仍然是一个重要的瓶颈，阻碍了该领域的进一步发展。为了克服这一障碍，我们提出了一个集成的Web工具包，包含两个图形用户界面（GUI）：（i）PiaRec，支持音频、视频、MIDI和演奏元数据的同步采集；（ii）ASDF，能够从视觉数据中高效地标注演奏者的指法。总而言之，该系统可以简化多模态钢琴演奏数据集的采集。

## 🔬 方法详解

**问题定义**：现有钢琴演奏分析研究对多模态数据的需求日益增长，然而，手动采集和标注大规模多模态数据集（包括音频、视频、MIDI、指法等）非常耗时耗力，严重阻碍了该领域的发展。现有的数据采集和标注方法效率低下，缺乏统一的工具和流程。

**核心思路**：论文的核心思路是开发一个集成的Web工具包，通过图形用户界面（GUI）简化多模态钢琴演奏数据的采集和指法标注过程。该工具包旨在提供一个用户友好的平台，使研究人员能够更轻松地创建和管理大规模数据集。

**技术框架**：该Web工具包包含两个主要模块：PiaRec和ASDF。PiaRec负责同步采集音频、视频、MIDI和演奏元数据。ASDF则用于从视频数据中高效地标注演奏者的指法。这两个模块通过Web界面集成，用户可以在浏览器中直接使用。

**关键创新**：该工具包的关键创新在于其集成性和易用性。它将数据采集和指法标注两个关键步骤整合到一个统一的平台中，并提供了直观的图形用户界面，降低了数据采集和标注的门槛。此外，该工具包支持多种数据格式，方便数据的后续处理和分析。

**关键设计**：PiaRec使用WebRTC技术实现音视频数据的实时采集和传输，并使用MIDI库处理MIDI数据。ASDF则采用基于视频帧的指法标注方法，用户可以通过点击视频帧来标注指法信息。工具包使用JSON格式存储数据和标注信息，方便数据的导入导出。

## 📊 实验亮点

论文重点在于工具包的设计与实现，并未提供具体的实验数据。其亮点在于提供了一个易于使用且功能全面的多模态钢琴演奏数据集采集与标注平台，有望加速相关领域的研究进展。该工具包的开源或公开使用将极大地促进数据集的构建和共享。

## 🎯 应用场景

该研究成果可广泛应用于音乐信息检索、音乐教育、人机交互等领域。例如，可以利用该工具包创建大规模钢琴演奏数据集，用于训练钢琴演奏风格识别、自动指法推荐等模型。此外，该工具包还可以用于钢琴教学，帮助学生更好地理解和学习钢琴演奏技巧。

## 📄 摘要（原文）

> Piano performance is a multimodal activity that intrinsically combines physical actions with the acoustic rendition. Despite growing research interest in analyzing the multimodal nature of piano performance, the laborious process of acquiring large-scale multimodal data remains a significant bottleneck, hindering further progress in this field. To overcome this barrier, we present an integrated web toolkit comprising two graphical user interfaces (GUIs): (i) PiaRec, which supports the synchronized acquisition of audio, video, MIDI, and performance metadata. (ii) ASDF, which enables the efficient annotation of performer fingering from the visual data. Collectively, this system can streamline the acquisition of multimodal piano performance datasets.

