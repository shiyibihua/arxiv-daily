---
layout: default
title: Multimodal Appearance based Gaze-Controlled Virtual Keyboard with Synchronous Asynchronous Interaction for Low-Resource Settings
---

# Multimodal Appearance based Gaze-Controlled Virtual Keyboard with Synchronous Asynchronous Interaction for Low-Resource Settings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.16606" class="toolbar-btn" target="_blank">📄 arXiv: 2508.16606v1</a>
  <a href="https://arxiv.org/pdf/2508.16606.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.16606v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.16606v1', 'Multimodal Appearance based Gaze-Controlled Virtual Keyboard with Synchronous Asynchronous Interaction for Low-Resource Settings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yogesh Kumar Meena, Manish Salvi

**分类**: cs.HC, cs.AI, cs.LG

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出多模态外观基础的注视控制虚拟键盘以解决低资源环境下的沟通问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `注视控制` `虚拟键盘` `多模态输入` `深度学习` `无障碍沟通` `低资源环境` `用户体验`

## 📋 核心要点

1. 现有的注视控制接口在准确性和复杂命令集处理上存在显著不足，影响了用户体验。
2. 本文提出的解决方案结合深度学习与标准摄像头，设计了支持同步与异步交互的虚拟键盘。
3. 实验结果表明，使用摄像头的打字速度和信息传输率表现良好，显示出系统的可用性和低工作负载特性。

## 📝 摘要（中文）

在过去十年中，移动和语言障碍人士对沟通设备的需求不断增加。注视追踪作为一种无障碍沟通的解决方案，然而传统的外观基础接口面临准确性、非自愿眼动及复杂命令集的挑战。本文提出了一种多模态外观基础的注视控制虚拟键盘，利用深度学习与标准摄像头硬件结合，支持同步与异步命令选择。该虚拟键盘应用支持九个命令的菜单选择，用户可以拼写和输入最多56个英文字母，包括大小写字母、标点符号及删除功能。通过与20名正常参与者的实验评估，结果显示在不同输入方式下的打字速度和信息传输率表现良好，证明了该系统在低资源环境下作为可访问沟通工具的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决传统注视控制接口在准确性、非自愿眼动及复杂命令集处理上的不足，尤其是在低资源环境下的应用场景。

**核心思路**：通过结合深度学习与标准摄像头，设计出一种多模态的注视控制虚拟键盘，支持用户在不同交互模式下进行命令选择，提升用户的输入效率。

**技术框架**：系统整体架构包括输入模块（鼠标、眼动仪、摄像头）、命令选择模块（同步与异步模式）、以及输出模块（虚拟键盘界面），确保用户能够灵活选择输入方式。

**关键创新**：该研究的核心创新在于实现了多模态输入的结合，尤其是通过未修改的摄像头实现的注视控制，显著提升了系统的可用性和适应性。

**关键设计**：在技术细节上，系统采用了特定的深度学习模型来处理输入数据，设置了适当的损失函数以优化命令选择的准确性，同时设计了用户友好的界面以降低用户的认知负担。

## 📊 实验亮点

实验结果显示，使用鼠标的平均打字速度为18.3字母/分钟，而使用眼动仪和摄像头的同步模式分别为12.60和10.94字母/分钟。信息传输率在摄像头同步模式下达到80.29比特/分钟，显示出该系统在不同输入方式下的良好性能和用户体验。

## 🎯 应用场景

该研究的潜在应用领域包括为行动不便或语言障碍人士提供无障碍沟通工具，尤其是在资源有限的环境中。通过简化输入方式和提升用户体验，未来可能在教育、医疗和家庭护理等多个领域产生积极影响。

## 📄 摘要（原文）

> Over the past decade, the demand for communication devices has increased among individuals with mobility and speech impairments. Eye-gaze tracking has emerged as a promising solution for hands-free communication; however, traditional appearance-based interfaces often face challenges such as accuracy issues, involuntary eye movements, and difficulties with extensive command sets. This work presents a multimodal appearance-based gaze-controlled virtual keyboard that utilises deep learning in conjunction with standard camera hardware, incorporating both synchronous and asynchronous modes for command selection. The virtual keyboard application supports menu-based selection with nine commands, enabling users to spell and type up to 56 English characters, including uppercase and lowercase letters, punctuation, and a delete function for corrections. The proposed system was evaluated with twenty able-bodied participants who completed specially designed typing tasks using three input modalities: (i) a mouse, (ii) an eye-tracker, and (iii) an unmodified webcam. Typing performance was measured in terms of speed and information transfer rate (ITR) at both command and letter levels. Average typing speeds were 18.3+-5.31 letters/min (mouse), 12.60+-2.99letters/min (eye-tracker, synchronous), 10.94 +- 1.89 letters/min (webcam, synchronous), 11.15 +- 2.90 letters/min (eye-tracker, asynchronous), and 7.86 +- 1.69 letters/min (webcam, asynchronous). ITRs were approximately 80.29 +- 15.72 bits/min (command level) and 63.56 +- 11 bits/min (letter level) with webcam in synchronous mode. The system demonstrated good usability and low workload with webcam input, highlighting its user-centred design and promise as an accessible communication tool in low-resource settings.

