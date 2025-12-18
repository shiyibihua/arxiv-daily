---
layout: default
title: High-Fidelity Digital Twins for Bridging the Sim2Real Gap in LiDAR-Based ITS Perception
---

# High-Fidelity Digital Twins for Bridging the Sim2Real Gap in LiDAR-Based ITS Perception

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02904" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02904v1</a>
  <a href="https://arxiv.org/pdf/2509.02904.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02904v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02904v1', 'High-Fidelity Digital Twins for Bridging the Sim2Real Gap in LiDAR-Based ITS Perception')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muhammad Shahbaz, Shaurya Agarwal

**分类**: cs.CV

**发布日期**: 2025-09-03

---

## 💡 一句话要点

**提出高保真数字孪生框架，解决LiDAR感知中Sim2Real迁移问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `数字孪生` `Sim2Real` `LiDAR感知` `领域自适应` `智能交通系统`

## 📋 核心要点

1. 现有Sim2Real方法在LiDAR感知中存在领域差异，导致模型在真实数据上表现不佳。
2. 构建高保真数字孪生环境，模拟真实世界的几何、拓扑和传感器特性，生成同域合成数据。
3. 实验表明，使用数字孪生数据训练的模型在真实数据上性能提升4.8%，并有效减少领域偏移。

## 📝 摘要（中文）

本文提出了一种高保真数字孪生(HiFi DT)框架，旨在解决智能交通系统(ITS)中基于LiDAR的感知任务(如目标检测、跟踪、分割)的Sim2Real迁移问题。该框架通过整合真实世界的背景几何、车道级道路拓扑以及传感器特定规格和位置，构建更真实的仿真环境。论文形式化了Sim2Real学习中的领域自适应挑战，并提出了一种系统性的方法来构建生成同域合成数据的仿真环境。使用HiFi DT生成的合成数据训练了一个现成的3D目标检测器，并在真实数据上进行了评估。实验结果表明，DT训练的模型比在真实数据上训练的同等模型性能提高了4.8%。通过Chamfer距离(CD)、最大均值差异(MMD)、Earth Mover距离(EMD)和Fréchet距离(FD)等多种指标，在原始输入和潜在特征层面量化了合成数据和真实数据之间的分布对齐程度。结果表明，HiFi DT显著减少了领域偏移，并提高了在不同评估场景中的泛化能力。这些发现强调了数字孪生在实现可靠的、基于仿真的LiDAR感知在真实世界ITS应用中的重要作用。

## 🔬 方法详解

**问题定义**：论文旨在解决基于LiDAR的智能交通系统感知任务中，由于仿真环境与真实环境存在差异，导致模型从仿真环境迁移到真实环境时性能显著下降的问题。现有方法难以充分模拟真实世界的复杂性和传感器特性，造成较大的领域偏移。

**核心思路**：论文的核心思路是构建一个高保真数字孪生(HiFi DT)环境，尽可能逼真地模拟真实世界的场景，从而生成与真实数据分布更接近的合成数据。通过在HiFi DT上训练模型，可以有效减少Sim2Real的领域偏移，提高模型在真实环境中的泛化能力。

**技术框架**：整体框架包括以下几个主要步骤：1)构建HiFi DT环境，包括真实世界的背景几何、车道级道路拓扑以及传感器特定规格和位置；2)在HiFi DT环境中生成合成LiDAR数据；3)使用合成数据训练3D目标检测器；4)在真实数据上评估模型性能；5)使用多种指标(CD, MMD, EMD, FD)量化合成数据和真实数据之间的分布差异。

**关键创新**：最重要的技术创新点在于HiFi DT的构建方法，它不仅仅是简单地复制真实场景，而是系统性地考虑了影响LiDAR数据分布的关键因素，包括几何、拓扑和传感器特性。这种精细化的建模方法能够更有效地减少领域偏移，提高模型在真实环境中的性能。

**关键设计**：论文的关键设计包括：1)使用真实世界的背景几何数据来构建仿真环境；2)精确模拟车道级道路拓扑结构；3)考虑传感器特定的参数和位置，例如LiDAR的扫描模式、分辨率和噪声模型；4)使用多种分布距离度量来量化领域偏移，并指导HiFi DT的优化。

## 📊 实验亮点

实验结果表明，使用HiFi DT生成的合成数据训练的3D目标检测器，在真实数据上的性能比在真实数据上训练的同等模型提高了4.8%。此外，通过多种分布距离度量(CD, MMD, EMD, FD)的量化分析，证明HiFi DT能够显著减少合成数据和真实数据之间的领域偏移，从而提高模型的泛化能力。

## 🎯 应用场景

该研究成果可广泛应用于智能交通系统，例如自动驾驶、高级驾驶辅助系统(ADAS)、交通监控和管理等。通过使用高保真数字孪生技术，可以降低开发和测试成本，加速LiDAR感知算法的部署，并提高系统的安全性和可靠性。未来，该技术还可以扩展到其他传感器和应用领域，例如视觉感知、毫米波雷达感知等。

## 📄 摘要（原文）

> Sim2Real domain transfer offers a cost-effective and scalable approach for developing LiDAR-based perception (e.g., object detection, tracking, segmentation) in Intelligent Transportation Systems (ITS). However, perception models trained in simulation often under perform on real-world data due to distributional shifts. To address this Sim2Real gap, this paper proposes a high-fidelity digital twin (HiFi DT) framework that incorporates real-world background geometry, lane-level road topology, and sensor-specific specifications and placement. We formalize the domain adaptation challenge underlying Sim2Real learning and present a systematic method for constructing simulation environments that yield in-domain synthetic data. An off-the-shelf 3D object detector is trained on HiFi DT-generated synthetic data and evaluated on real data. Our experiments show that the DT-trained model outperforms the equivalent model trained on real data by 4.8%. To understand this gain, we quantify distributional alignment between synthetic and real data using multiple metrics, including Chamfer Distance (CD), Maximum Mean Discrepancy (MMD), Earth Mover's Distance (EMD), and Fr'echet Distance (FD), at both raw-input and latent-feature levels. Results demonstrate that HiFi DTs substantially reduce domain shift and improve generalization across diverse evaluation scenarios. These findings underscore the significant role of digital twins in enabling reliable, simulation-based LiDAR perception for real-world ITS applications.

