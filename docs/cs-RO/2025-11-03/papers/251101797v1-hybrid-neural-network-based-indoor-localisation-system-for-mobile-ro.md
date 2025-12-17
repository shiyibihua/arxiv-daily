---
layout: default
title: Hybrid Neural Network-Based Indoor Localisation System for Mobile Robots Using CSI Data in a Robotics Simulator
---

# Hybrid Neural Network-Based Indoor Localisation System for Mobile Robots Using CSI Data in a Robotics Simulator

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.01797" target="_blank" class="toolbar-btn">arXiv: 2511.01797v1</a>
    <a href="https://arxiv.org/pdf/2511.01797.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.01797v1" 
            onclick="toggleFavorite(this, '2511.01797v1', 'Hybrid Neural Network-Based Indoor Localisation System for Mobile Robots Using CSI Data in a Robotics Simulator')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Javier Ballesteros-Jerez, Jesus Martínez-Gómez, Ismael García-Varea, Luis Orozco-Barbosa, Manuel Castillo-Cara

**分类**: cs.RO, cs.LG

**发布日期**: 2025-11-03

**备注**: 13 pages, 7 figures. Conference paper (ROBOVIS 2025)

**期刊**: Robotics, Computer Vision and Intelligent Systems. ROBOVIS 2025. Communications in Computer and Information Science, vol 2629 (2025) 148-163

**DOI**: [10.1007/978-3-032-00986-9_11](https://doi.org/10.1007/978-3-032-00986-9_11)

---

## 💡 一句话要点

**提出一种基于混合神经网络的室内定位系统，利用CSI数据为移动机器人实现精准定位。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `室内定位` `移动机器人` `信道状态信息` `混合神经网络` `卷积神经网络`

## 📋 核心要点

1. 现有室内定位方法在复杂环境中精度不足，且难以充分利用CSI数据中的空间信息。
2. 提出一种混合神经网络（HyNN），结合CNN提取CSI图像特征和MLP进行位置回归，充分利用CSI数据。
3. 将HyNN定位方案集成到机器人仿真器和ROS中，通过异构测试用例验证了其在复杂环境中的定位精度。

## 📝 摘要（中文）

本文提出了一种混合神经网络模型，用于推断移动机器人在室内环境中的位置，该模型利用来自大规模MIMO系统的信道状态信息（CSI）数据。该方法利用现有的CSI数据集，集成卷积神经网络（CNN）和多层感知器（MLP），形成混合神经网络（HyNN），以估计2D机器人位置。CSI读数使用TINTO工具转换为合成图像。该定位解决方案与机器人仿真器和机器人操作系统（ROS）集成，从而可以通过异构测试用例进行评估，并采用卡尔曼滤波器等状态估计器。研究结果表明，HyNN模型在复杂环境中为移动机器人实现精确的室内定位和导航方面具有潜力，并提出了一种适用于不同场景和数据集的通用程序。

## 🔬 方法详解

**问题定义**：论文旨在解决移动机器人在室内环境中的精确定位问题。现有方法，如基于RSSI或WiFi指纹的定位，在复杂环境中精度受限。CSI数据包含更丰富的信道信息，但如何有效利用CSI数据进行定位是一个挑战。现有方法难以充分利用CSI数据中的空间相关性。

**核心思路**：论文的核心思路是将CSI数据转换为合成图像，然后利用卷积神经网络（CNN）提取图像特征，再结合多层感知器（MLP）进行位置回归。这种混合神经网络（HyNN）能够同时利用CSI数据的空间信息和非线性关系，从而提高定位精度。

**技术框架**：整体框架包括以下几个主要阶段：1) CSI数据采集：利用大规模MIMO系统获取CSI数据。2) 数据预处理：使用TINTO工具将CSI数据转换为合成图像。3) 特征提取：使用CNN从CSI图像中提取特征。4) 位置回归：使用MLP将提取的特征映射到2D机器人位置。5) 系统集成：将定位解决方案集成到机器人仿真器和ROS中。

**关键创新**：论文的最重要的技术创新点是提出了HyNN模型，将CNN和MLP相结合，充分利用CSI数据的空间信息和非线性关系。与传统的基于CSI的定位方法相比，HyNN能够更有效地提取CSI数据中的特征，从而提高定位精度。

**关键设计**：CSI数据通过TINTO工具转换为合成图像，图像大小和通道数需要根据具体CSI数据进行调整。CNN的网络结构包括卷积层、池化层和全连接层，具体参数需要根据数据集进行调整。MLP的网络结构包括多个全连接层，层数和神经元数量需要根据数据集进行调整。损失函数通常选择均方误差（MSE）或交叉熵损失函数。

## 📊 实验亮点

论文通过在机器人仿真器中进行实验，验证了HyNN模型的有效性。实验结果表明，HyNN模型能够实现精确的室内定位，并能够与ROS和卡尔曼滤波器等工具集成。虽然论文中没有给出具体的性能数据和对比基线，但强调了该方法在复杂环境中的潜力。

## 🎯 应用场景

该研究成果可应用于室内导航、仓储物流、智能家居、医疗健康等领域。通过精确的室内定位，移动机器人可以更好地完成导航、搬运、巡检等任务。该技术还可以应用于人员定位，例如在大型商场、医院等场所为用户提供导航服务。未来，该技术有望与SLAM等技术结合，实现更鲁棒的室内定位和导航。

## 📄 摘要（原文）

> We present a hybrid neural network model for inferring the position of mobile robots using Channel State Information (CSI) data from a Massive MIMO system. By leveraging an existing CSI dataset, our approach integrates a Convolutional Neural Network (CNN) with a Multilayer Perceptron (MLP) to form a Hybrid Neural Network (HyNN) that estimates 2D robot positions. CSI readings are converted into synthetic images using the TINTO tool. The localisation solution is integrated with a robotics simulator, and the Robot Operating System (ROS), which facilitates its evaluation through heterogeneous test cases, and the adoption of state estimators like Kalman filters. Our contributions illustrate the potential of our HyNN model in achieving precise indoor localisation and navigation for mobile robots in complex environments. The study follows, and proposes, a generalisable procedure applicable beyond the specific use case studied, making it adaptable to different scenarios and datasets.

