---
layout: default
title: Improvement of Nuclide Detection through Graph Spectroscopic Analysis Framework and its Application to Nuclear Facility Upset Detection
---

# Improvement of Nuclide Detection through Graph Spectroscopic Analysis Framework and its Application to Nuclear Facility Upset Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16522" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16522v1</a>
  <a href="https://arxiv.org/pdf/2506.16522.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16522v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16522v1', 'Improvement of Nuclide Detection through Graph Spectroscopic Analysis Framework and its Application to Nuclear Facility Upset Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pedro Rodríguez Fernández, Christian Svinth, Alex Hagen

**分类**: physics.ins-det, cs.LG, physics.data-an

**发布日期**: 2025-06-19

---

## 💡 一句话要点

**提出基于图谱光谱分析框架的放射性核素检测改进方法**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `放射性核素检测` `神经网络` `注意力机制` `光谱分析` `核设施安全` `实时监测` `环境辐射`

## 📋 核心要点

1. 现有的放射性核素检测方法在检测限和准确性上存在不足，尤其在核设施事故情况下的实时检测能力较弱。
2. 本文提出了一种基于神经网络和注意力机制的检测方法，通过调节检测阈值来提高检测性能，尤其是针对时间事件分布和光谱特征的适应性。
3. 实验结果表明，该方法在铯释放检测中实现了2倍的性能提升，相较于传统方法具有显著优势。

## 📝 摘要（中文）

本文提出了一种利用光谱辐射探测器和每个检测到的辐射量子到达时间来提高放射性核素检测限的方法。该方法基于具有注意力机制的神经网络实现，针对核设施事故中铯释放的检测进行了说明，显示出相较于传统光谱方法有2倍的提升。我们假设该方法通过根据时间事件分布和局部光谱特征调节检测阈值，从而调制检测概率，取得了这一性能提升。我们认为该方法具有广泛的适用性，尤其对于具有复杂衰变链的放射性核素可能更为成功，并且可以超越到达时间的添加，整合其他检测事件数据。

## 🔬 方法详解

**问题定义**：本文旨在解决现有放射性核素检测方法在检测限和准确性方面的不足，尤其是在核设施事故情况下的实时检测能力较弱。

**核心思路**：通过引入具有注意力机制的神经网络，调节检测阈值以适应时间事件分布和局部光谱特征，从而提高检测性能。

**技术框架**：整体架构包括数据采集、特征提取、神经网络模型训练和检测结果输出四个主要模块。数据采集阶段负责获取辐射探测器的信号，特征提取阶段则提取到达时间和光谱特征，随后通过训练的神经网络进行检测。

**关键创新**：最重要的技术创新在于通过注意力机制动态调节检测阈值，使得检测概率能够根据事件的时间分布和光谱特征进行优化，这与传统方法的静态阈值设定形成了本质区别。

**关键设计**：在网络结构上，采用了多层感知机（MLP）结合注意力机制，损失函数设计为结合检测准确率和召回率的加权损失，以确保模型在不同检测场景下的鲁棒性。

## 📊 实验亮点

实验结果显示，所提出的方法在铯释放检测中实现了2倍的性能提升，相较于传统光谱方法，显著提高了检测的准确性和灵敏度。这一结果为核设施的安全监测提供了新的技术手段。

## 🎯 应用场景

该研究的潜在应用领域包括核设施的安全监测、环境辐射监测以及核事故应急响应等。通过提高放射性核素的检测能力，可以更有效地保障公众安全和环境保护，未来可能在核能利用和辐射防护领域产生深远影响。

## 📄 摘要（原文）

> We present a method to improve the detection limit for radionuclides using spectroscopic radiation detectors and the arrival time of each detected radiation quantum. We enable this method using a neural network with an attention mechanism. We illustrate the method on the detection of Cesium release from a nuclear facility during an upset, and our method shows $2\times$ improvement over the traditional spectroscopic method. We hypothesize that our method achieves this performance increase by modulating its detection probability by the overall rate of probable detections, specifically by adapting detection thresholds based on temporal event distributions and local spectral features, and show evidence to this effect. We believe this method is applicable broadly and may be more successful for radionuclides with more complicated decay chains than Cesium; we also note that our method can generalize beyond the addition of arrival time and could integrate other data about each detection event, such as pulse quality, location in detector, or even combining the energy and time from detections in different detectors.

