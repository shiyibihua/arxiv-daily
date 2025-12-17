---
layout: default
title: Reperio-rPPG: Relational Temporal Graph Neural Networks for Periodicity Learning in Remote Physiological Measurement
---

# Reperio-rPPG: Relational Temporal Graph Neural Networks for Periodicity Learning in Remote Physiological Measurement

**arXiv**: [2511.05946v1](https://arxiv.org/abs/2511.05946) | [PDF](https://arxiv.org/pdf/2511.05946.pdf)

**作者**: Ba-Thinh Nguyen, Thach-Ha Ngoc Pham, Hoang-Long Duc Nguyen, Thi-Duyen Ngo, Thanh-Ha Le

**分类**: cs.CV

**发布日期**: 2025-11-08

**🔗 代码/项目**: [GITHUB](https://github.com/deconasser/Reperio-rPPG)

---

## 💡 一句话要点

**提出Reperio-rPPG，利用关系时序图神经网络学习远程生理信号的周期性，实现更鲁棒的心率估计。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `远程光电容积脉搏波` `rPPG` `生理信号处理` `关系卷积网络` `图神经网络` `周期性学习` `心率估计`

## 📋 核心要点

1. 现有rPPG方法未能充分利用生理信号的内在周期性，导致在复杂场景下性能受限。
2. Reperio-rPPG通过关系卷积网络和图Transformer，有效建模生理信号的周期性结构。
3. 实验表明，Reperio-rPPG在多个数据集上达到SOTA，并在不同运动和光照条件下表现出鲁棒性。

## 📝 摘要（中文）

远程光电容积脉搏波(rPPG)是一种新兴的非接触式生理传感技术，它利用面部视频中细微的颜色变化来估计心率和呼吸频率等生命体征。由于其可扩展性和便利性，这种非侵入性方法在远程医疗、情感计算、驾驶员疲劳检测和健康监测等不同领域获得了广泛关注。尽管在远程生理信号测量方面取得了显著进展，但先前的方法通常未充分探索或建模一个关键特征——内在周期性，从而限制了它们在真实条件下捕获细粒度时间动态的能力。为了弥合这一差距，我们提出了Reperio-rPPG，这是一个新颖的框架，它策略性地将关系卷积网络与图Transformer相结合，以有效地捕获生理信号中固有的周期性结构。此外，考虑到现有rPPG数据集的多样性有限，我们进一步引入了一种定制的CutMix增强方法，以提高模型的泛化能力。在三个广泛使用的基准数据集PURE、UBFC-rPPG和MMPD上进行的大量实验表明，Reperio-rPPG不仅实现了最先进的性能，而且在各种运动（例如，静止、旋转、说话、行走）和光照条件（例如，自然光、低LED、高LED）下表现出显著的鲁棒性。

## 🔬 方法详解

**问题定义**：论文旨在解决远程光电容积脉搏波(rPPG)信号分析中，现有方法对生理信号内在周期性建模不足的问题。现有方法在处理真实场景下的复杂运动和光照变化时，由于未能充分利用信号的周期性特征，导致性能下降。

**核心思路**：论文的核心思路是利用关系卷积网络(Relational Convolutional Networks, RCN)和图Transformer相结合，显式地建模rPPG信号的时序关系和周期性。通过构建时序图，并利用RCN学习节点之间的关系，再通过图Transformer进行全局信息整合，从而更有效地提取和利用信号的周期性特征。

**技术框架**：Reperio-rPPG框架主要包含以下几个模块：1) **人脸检测与对齐**：从视频帧中检测并对齐人脸区域。2) **区域提取**：提取人脸区域的感兴趣区域(Region of Interest, ROI)，例如额头、脸颊等。3) **颜色通道提取**：提取ROI区域的RGB颜色通道信息。4) **时序图构建**：将提取的颜色通道信息构建成时序图，其中每个节点代表一个时间步的颜色信息，边代表节点之间的时序关系。5) **关系卷积网络(RCN)**：利用RCN学习时序图中节点之间的关系，提取局部时序特征。6) **图Transformer**：利用图Transformer进行全局信息整合，学习全局周期性特征。7) **心率估计**：利用学习到的特征进行心率估计。

**关键创新**：论文的关键创新在于将关系卷积网络和图Transformer相结合，用于显式地建模rPPG信号的周期性。与传统方法相比，Reperio-rPPG能够更有效地捕获信号的时序依赖关系和周期性特征，从而提高心率估计的准确性和鲁棒性。此外，论文还提出了一个定制的CutMix数据增强方法，以提高模型的泛化能力。

**关键设计**：在时序图构建中，每个节点代表一个时间步的颜色信息，边代表节点之间的时序关系。RCN采用多层卷积结构，学习节点之间的关系。图Transformer采用自注意力机制，进行全局信息整合。损失函数采用均方误差(Mean Squared Error, MSE)，用于衡量估计心率与真实心率之间的差异。CutMix数据增强方法通过随机混合不同样本的ROI区域，增加数据的多样性。

## 📊 实验亮点

实验结果表明，Reperio-rPPG在PURE、UBFC-rPPG和MMPD三个数据集上均取得了state-of-the-art的性能。例如，在UBFC-rPPG数据集上，Reperio-rPPG的MAE（平均绝对误差）显著低于现有方法，并且在不同运动和光照条件下表现出更强的鲁棒性。CutMix数据增强方法也有效提高了模型的泛化能力。

## 🎯 应用场景

Reperio-rPPG技术可广泛应用于远程医疗、健康监测、驾驶员疲劳检测、情感计算等领域。该技术无需接触即可实现心率等生理指标的监测，具有便捷性和非侵入性等优点，在疫情期间的远程健康监测和居家健康管理方面具有重要的应用价值。未来，该技术有望集成到智能手机、平板电脑等移动设备中，实现随时随地的健康监测。

## 📄 摘要（原文）

> Remote photoplethysmography (rPPG) is an emerging contactless physiological sensing technique that leverages subtle color variations in facial videos to estimate vital signs such as heart rate and respiratory rate. This non-invasive method has gained traction across diverse domains, including telemedicine, affective computing, driver fatigue detection, and health monitoring, owing to its scalability and convenience. Despite significant progress in remote physiological signal measurement, a crucial characteristic - the intrinsic periodicity - has often been underexplored or insufficiently modeled in previous approaches, limiting their ability to capture fine-grained temporal dynamics under real-world conditions. To bridge this gap, we propose Reperio-rPPG, a novel framework that strategically integrates Relational Convolutional Networks with a Graph Transformer to effectively capture the periodic structure inherent in physiological signals. Additionally, recognizing the limited diversity of existing rPPG datasets, we further introduce a tailored CutMix augmentation to enhance the model's generalizability. Extensive experiments conducted on three widely used benchmark datasets - PURE, UBFC-rPPG, and MMPD - demonstrate that Reperio-rPPG not only achieves state-of-the-art performance but also exhibits remarkable robustness under various motion (e.g., stationary, rotation, talking, walking) and illumination conditions (e.g., nature, low LED, high LED). The code is publicly available at https://github.com/deconasser/Reperio-rPPG.

