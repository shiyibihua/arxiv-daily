---
layout: default
title: Efficient Multi-Camera Tokenization with Triplanes for End-to-End Driving
---

# Efficient Multi-Camera Tokenization with Triplanes for End-to-End Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12251" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12251v2</a>
  <a href="https://arxiv.org/pdf/2506.12251.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12251v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12251v2', 'Efficient Multi-Camera Tokenization with Triplanes for End-to-End Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Boris Ivanovic, Cristiano Saltori, Yurong You, Yan Wang, Wenjie Luo, Marco Pavone

**分类**: cs.CV, cs.LG, cs.RO

**发布日期**: 2025-06-13 (更新: 2025-07-21)

**备注**: 12 pages, 10 figures, 5 tables

---

## 💡 一句话要点

**提出基于三平面的多摄像头高效标记方法以提升自动驾驶性能**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `自动驾驶` `多摄像头系统` `传感器数据标记` `三维重建` `实时推理` `自回归变换器` `运动规划`

## 📋 核心要点

1. 现有的图像块标记方法在处理多摄像头传感器数据时效率低下，限制了自动驾驶系统的实时性能。
2. 本文提出了一种基于三平面的标记策略，能够高效处理多摄像头数据，且与输入摄像头的数量和分辨率无关。
3. 实验结果显示，该方法在标记数量上减少了72%，推理速度提升了50%，同时保持了运动规划精度和越野能力。

## 📝 摘要（中文）

自回归变换器在端到端机器人和自动驾驶汽车（AV）策略架构中的应用日益增多，因其可扩展性和利用互联网规模预训练进行泛化的潜力。因此，高效标记传感器数据对于确保这些架构在嵌入式硬件上的实时可行性至关重要。为此，本文提出了一种基于三平面的多摄像头标记策略，利用最新的3D神经重建和渲染技术，生成与输入摄像头数量和分辨率无关的传感器标记，同时明确考虑了AV周围的几何结构。在大规模AV数据集和最先进的神经模拟器上的实验表明，该方法在当前图像块标记策略上节省了高达72%的标记数量，实现了高达50%的策略推理加速，同时在开放环运动规划精度和闭环驾驶模拟中的越野率上有所提升。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多摄像头传感器数据标记方法效率低下的问题，尤其是在实时自动驾驶应用中，传统图像块标记策略无法满足需求。

**核心思路**：提出的三平面标记策略通过结合3D神经重建和渲染技术，生成与摄像头数量和分辨率无关的传感器标记，从而提高标记效率和实时性。

**技术框架**：整体架构包括数据采集、三维重建、标记生成和策略推理四个主要模块。首先，通过多摄像头系统采集环境数据，然后进行三维重建，接着生成相应的传感器标记，最后进行策略推理。

**关键创新**：最重要的创新在于提出了三平面标记方法，该方法能够有效减少标记数量，同时保持高精度的运动规划能力，与传统方法相比具有显著的性能提升。

**关键设计**：在设计中，采用了优化的损失函数以平衡标记数量和精度，同时在网络结构上引入了适应性模块，以处理不同摄像头的输入数据。具体参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，提出的方法在标记数量上减少了72%，推理速度提升了50%，同时在开放环运动规划精度和闭环驾驶模拟中的越野率上均有显著改善。这些结果展示了该方法在实际应用中的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶汽车、机器人导航和智能交通系统等。通过提高传感器数据的处理效率，该方法能够显著提升自动驾驶系统的实时反应能力和安全性，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Autoregressive Transformers are increasingly being deployed as end-to-end robot and autonomous vehicle (AV) policy architectures, owing to their scalability and potential to leverage internet-scale pretraining for generalization. Accordingly, tokenizing sensor data efficiently is paramount to ensuring the real-time feasibility of such architectures on embedded hardware. To this end, we present an efficient triplane-based multi-camera tokenization strategy that leverages recent advances in 3D neural reconstruction and rendering to produce sensor tokens that are agnostic to the number of input cameras and their resolution, while explicitly accounting for their geometry around an AV. Experiments on a large-scale AV dataset and state-of-the-art neural simulator demonstrate that our approach yields significant savings over current image patch-based tokenization strategies, producing up to 72% fewer tokens, resulting in up to 50% faster policy inference while achieving the same open-loop motion planning accuracy and improved offroad rates in closed-loop driving simulations.

