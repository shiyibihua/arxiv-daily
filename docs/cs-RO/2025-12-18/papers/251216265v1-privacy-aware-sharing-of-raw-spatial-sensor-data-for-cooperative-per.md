---
layout: default
title: Privacy-Aware Sharing of Raw Spatial Sensor Data for Cooperative Perception
---

# Privacy-Aware Sharing of Raw Spatial Sensor Data for Cooperative Perception

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16265" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16265v1</a>
  <a href="https://arxiv.org/pdf/2512.16265.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16265v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16265v1', 'Privacy-Aware Sharing of Raw Spatial Sensor Data for Cooperative Perception')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bangya Liu, Chengpo Yan, Chenghao Jiang, Suman Banerjee, Akarsh Prabhakara

**分类**: cs.NI, cs.RO

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出SHARP框架，旨在最小化原始空间传感器数据共享中的隐私泄露，促进车辆协同感知。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `协同感知` `隐私保护` `原始数据共享` `车辆网络` `自动驾驶`

## 📋 核心要点

1. 现有车辆协同感知系统依赖原始传感器数据共享，但直接共享引发了严重的隐私泄露风险，阻碍了实际应用。
2. 论文提出SHARP框架，通过隐私保护机制，在最小化隐私泄露的同时，促进基于原始数据的协同感知。
3. 论文构建了一个研究框架，并讨论了实现该框架在网络系统、移动计算和感知研究中面临的开放性问题。

## 📝 摘要（中文）

车辆间的协同感知有望提供更强大和可靠的场景理解能力。最近，我们看到实验性系统研究正在构建测试平台，以共享原始空间传感器数据用于协同感知。虽然精度有了显著提高，并且这是自然的发展方向，但我们花时间考虑了汽车制造商最终采用这种方法的问题。在本文中，我们首先论证了新的隐私问题出现，并阻碍了利益相关者共享原始传感器数据。接下来，我们提出了SHARP，一个研究框架，旨在最小化隐私泄露，并推动利益相关者朝着基于原始数据的协同感知的宏伟目标前进。最后，我们讨论了网络系统、移动计算、感知研究人员、工业界和政府在实现我们提出的框架时面临的开放性问题。

## 🔬 方法详解

**问题定义**：论文旨在解决车辆协同感知中，直接共享原始空间传感器数据所带来的隐私泄露问题。现有方法在追求感知精度的同时，忽略了用户隐私，导致利益相关者不愿共享数据，阻碍了协同感知技术的实际应用。

**核心思路**：SHARP框架的核心思路是在数据共享过程中引入隐私保护机制，通过对原始数据进行处理，降低隐私泄露的风险，同时尽可能保持数据的可用性，以支持协同感知任务。这样既能促进数据共享，又能保护用户隐私。

**技术框架**：论文提出了一个研究框架SHARP，但摘要中并未详细描述其具体架构和流程。根据上下文推断，该框架可能包含以下模块：1) 隐私评估模块：用于评估原始数据中存在的隐私风险；2) 隐私保护模块：用于对原始数据进行处理，例如差分隐私、同态加密等，以降低隐私泄露风险；3) 数据共享模块：用于安全地共享处理后的数据；4) 感知融合模块：用于将来自不同车辆的数据进行融合，以提高感知精度。

**关键创新**：该论文的关键创新在于提出了一个隐私感知的协同感知框架SHARP，强调在原始数据共享过程中保护用户隐私的重要性。与现有方法相比，SHARP框架更加关注隐私保护，旨在平衡感知精度和隐私保护之间的关系。

**关键设计**：由于摘要中没有提供关于SHARP框架的具体技术细节，因此无法得知关键参数设置、损失函数或网络结构等信息。这些细节需要在论文正文中进一步查找。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16265v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16265v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16265v1/hotnets25-template/newfigures/privacy_metrics.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

由于论文摘要主要关注框架的提出和问题分析，并未提供具体的实验结果。因此，无法从摘要中提取实验亮点。具体的性能数据、对比基线和提升幅度等信息需要在论文正文中查找。

## 🎯 应用场景

该研究成果可应用于自动驾驶、智能交通等领域。通过SHARP框架，车辆可以在保护用户隐私的前提下，共享传感器数据，实现更安全、更高效的协同感知。这有助于提高自动驾驶系统的可靠性，减少交通事故，并优化交通流量。

## 📄 摘要（原文）

> Cooperative perception between vehicles is poised to offer robust and reliable scene understanding. Recently, we are witnessing experimental systems research building testbeds that share raw spatial sensor data for cooperative perception. While there has been a marked improvement in accuracies and is the natural way forward, we take a moment to consider the problems with such an approach for eventual adoption by automakers. In this paper, we first argue that new forms of privacy concerns arise and discourage stakeholders to share raw sensor data. Next, we present SHARP, a research framework to minimize privacy leakage and drive stakeholders towards the ambitious goal of raw data based cooperative perception. Finally, we discuss open questions for networked systems, mobile computing, perception researchers, industry and government in realizing our proposed framework.

