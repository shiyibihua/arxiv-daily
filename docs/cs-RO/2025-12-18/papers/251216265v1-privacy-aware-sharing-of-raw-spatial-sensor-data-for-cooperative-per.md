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

**关键词**: `协同感知` `隐私保护` `数据共享` `自动驾驶` `传感器数据`

## 📋 核心要点

1. 现有车辆协同感知系统依赖原始传感器数据共享，但直接共享引发了严重的隐私泄露风险，阻碍了实际应用。
2. SHARP框架旨在通过隐私保护机制，最小化原始数据共享过程中的隐私泄露，从而鼓励利益相关者共享数据。
3. 论文提出了SHARP框架，并讨论了实现该框架在网络系统、移动计算和感知研究等领域面临的挑战和开放性问题。

## 📝 摘要（中文）

车辆间的协同感知有望提供更强大和可靠的场景理解能力。最近，我们看到实验性系统研究正在构建测试平台，用于共享原始空间传感器数据以实现协同感知。虽然精度有了显著提高，并且这是自然的发展方向，但我们在此停下来思考这种方法在最终被汽车制造商采用时可能存在的问题。在本文中，我们首先指出，新的隐私问题正在出现，这会阻碍利益相关者共享原始传感器数据。接下来，我们提出了SHARP，一个研究框架，旨在最小化隐私泄露，并推动利益相关者朝着基于原始数据的协同感知的宏伟目标前进。最后，我们讨论了网络系统、移动计算、感知研究人员、行业和政府在实现我们提出的框架时面临的开放性问题。

## 🔬 方法详解

**问题定义**：论文旨在解决车辆协同感知中，直接共享原始空间传感器数据所带来的隐私泄露问题。现有方法虽然提高了感知精度，但忽略了用户隐私，导致利益相关者不愿共享数据，阻碍了协同感知技术的推广应用。

**核心思路**：SHARP框架的核心思路是在保证协同感知性能的前提下，通过隐私保护机制，降低原始数据共享过程中的隐私泄露风险。具体而言，框架可能采用差分隐私、同态加密等技术，对原始数据进行处理，使其在满足协同感知需求的同时，尽可能地减少敏感信息的暴露。

**技术框架**：由于论文摘要中没有详细描述SHARP框架的具体架构，因此无法给出确切的模块和流程。但可以推测，该框架可能包含以下几个主要模块：1) 数据预处理模块：对原始传感器数据进行清洗、校准等操作。2) 隐私保护模块：应用差分隐私、同态加密等技术，对数据进行脱敏处理。3) 数据共享模块：将处理后的数据安全地共享给其他车辆或云平台。4) 感知融合模块：接收来自其他车辆的数据，并进行融合，以提高感知精度。

**关键创新**：论文的关键创新在于提出了SHARP框架，将隐私保护机制融入到车辆协同感知的数据共享过程中。与现有方法相比，SHARP框架更加关注用户隐私，有望解决数据共享的瓶颈问题，促进协同感知技术的实际应用。

**关键设计**：由于论文摘要中没有提供关于关键设计的具体细节，因此无法给出确切的参数设置、损失函数、网络结构等信息。这些细节可能在论文的后续章节中进行详细描述。例如，差分隐私的参数ε和δ的选择，同态加密方案的选择，以及感知融合算法的设计等。

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

由于摘要中没有提供具体的实验结果，因此无法总结实验亮点。需要阅读论文全文才能了解SHARP框架在实际应用中的性能表现，以及与现有方法的对比结果。

## 🎯 应用场景

该研究成果可应用于自动驾驶、智能交通等领域。通过SHARP框架，车辆可以安全地共享传感器数据，提高协同感知能力，从而提升自动驾驶的安全性和可靠性。此外，该框架还可以应用于其他需要数据共享的场景，例如智慧城市、环境监测等，具有广泛的应用前景。

## 📄 摘要（原文）

> Cooperative perception between vehicles is poised to offer robust and reliable scene understanding. Recently, we are witnessing experimental systems research building testbeds that share raw spatial sensor data for cooperative perception. While there has been a marked improvement in accuracies and is the natural way forward, we take a moment to consider the problems with such an approach for eventual adoption by automakers. In this paper, we first argue that new forms of privacy concerns arise and discourage stakeholders to share raw sensor data. Next, we present SHARP, a research framework to minimize privacy leakage and drive stakeholders towards the ambitious goal of raw data based cooperative perception. Finally, we discuss open questions for networked systems, mobile computing, perception researchers, industry and government in realizing our proposed framework.

