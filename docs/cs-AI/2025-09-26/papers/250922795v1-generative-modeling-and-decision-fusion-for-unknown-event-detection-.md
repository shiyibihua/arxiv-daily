---
layout: default
title: Generative Modeling and Decision Fusion for Unknown Event Detection and Classification Using Synchrophasor Data
---

# Generative Modeling and Decision Fusion for Unknown Event Detection and Classification Using Synchrophasor Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22795" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22795v1</a>
  <a href="https://arxiv.org/pdf/2509.22795.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22795v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22795v1', 'Generative Modeling and Decision Fusion for Unknown Event Detection and Classification Using Synchrophasor Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yi Hu, Zheyuan Cheng

**分类**: eess.SP, cs.AI, eess.SY

**发布日期**: 2025-09-26

**备注**: 10 pages

---

## 💡 一句话要点

**提出基于生成模型和决策融合的电力系统未知事件检测与分类框架**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `电力系统事件检测` `同步相量数据` `生成模型` `变分自编码器` `生成对抗网络` `决策融合` `异常检测` `未知事件分类`

## 📋 核心要点

1. 现有电力系统事件检测方法依赖有限的标注数据，泛化能力受限，难以识别罕见或未知的扰动。
2. 利用变分自编码器-生成对抗网络建模正常工况，提取重建误差和判别器误差作为异常指标，并结合决策融合。
3. 实验结果表明，该方法在准确性上优于机器学习、深度学习等基线方法，并能有效识别未知事件。

## 📝 摘要（中文）

本文提出了一种新颖的框架，该框架集成了生成模型、滑动窗口时序处理和决策融合，以实现使用同步相量数据的鲁棒事件检测和分类。采用变分自编码器-生成对抗网络来模拟正常运行条件，其中重建误差和判别器误差均被提取作为异常指标。开发了两种互补的决策策略：一种基于阈值的规则，用于提高计算效率；一种基于凸包的方法，用于在复杂的误差分布下保持鲁棒性。这些特征通过滑动窗口机制被组织成时空检测和分类矩阵，并且识别和决策融合阶段集成了来自PMU的输出。这种设计使该框架能够识别已知事件，同时系统地将先前未见过的扰动分类为新类别，从而解决了监督分类器的一个关键限制。实验结果表明，该方法具有最先进的准确性，超过了机器学习、深度学习和基于包络的基线。识别未知事件的能力进一步突出了所提出的方法在现代电力系统中进行广域事件分析的适应性和实际价值。

## 🔬 方法详解

**问题定义**：电力系统事件的可靠检测和分类对于维持电网稳定性和态势感知至关重要。然而，现有方法通常依赖于有限的已标注数据集，这限制了它们对罕见或未见过的扰动的泛化能力。因此，如何有效地检测和分类电力系统中已知和未知的事件是一个关键问题。

**核心思路**：本文的核心思路是利用生成模型学习电力系统正常运行状态的分布，然后通过检测与正常状态的偏差来识别异常事件。同时，为了提高鲁棒性，采用了多种决策策略进行融合，并结合时空信息进行综合判断。这种方法能够有效地识别已知事件，并能够将未知的扰动分类到一个新的类别中。

**技术框架**：该框架主要包含以下几个阶段：1) 利用变分自编码器-生成对抗网络（VAE-GAN）对正常运行条件下的同步相量数据进行建模；2) 从VAE-GAN中提取重建误差和判别器误差作为异常指标；3) 采用基于阈值的规则和基于凸包的方法进行决策；4) 通过滑动窗口机制将特征组织成时空检测和分类矩阵；5) 通过识别和决策融合阶段整合来自不同PMU的输出。

**关键创新**：该方法最重要的创新点在于它能够识别未知的事件。传统的监督学习方法只能识别训练集中已有的类别，而该方法通过学习正常状态的分布，可以检测到与正常状态偏差较大的未知事件，并将其归类为新的类别。此外，结合了VAE和GAN的优点，利用两种误差指标进行互补，提升了异常检测的准确性。

**关键设计**：VAE-GAN的网络结构设计需要仔细考虑，以确保能够有效地学习正常运行状态的分布。损失函数的设计也至关重要，需要平衡重建误差和判别器误差，以避免模型过度拟合或欠拟合。滑动窗口的大小和步长需要根据数据的特点进行调整，以捕捉到事件的时序特征。决策融合策略需要根据不同决策方法的特点进行选择，以实现最佳的性能。

## 📊 实验亮点

实验结果表明，该方法在电力系统事件检测和分类任务中取得了最先进的准确性，超过了传统的机器学习、深度学习和基于包络的基线方法。该方法不仅能够准确地识别已知事件，还能够有效地检测和分类未知的扰动，这突出了其在实际应用中的价值和潜力。

## 🎯 应用场景

该研究成果可应用于现代电力系统的广域事件分析，提高电网的稳定性和态势感知能力。通过及时检测和分类电力系统中的异常事件，可以采取相应的措施，避免事故的发生，保障电力系统的安全可靠运行。此外，该方法还可以应用于其他领域的异常检测和故障诊断，例如工业控制系统、交通运输系统等。

## 📄 摘要（原文）

> Reliable detection and classification of power system events are critical for maintaining grid stability and situational awareness. Existing approaches often depend on limited labeled datasets, which restricts their ability to generalize to rare or unseen disturbances. This paper proposes a novel framework that integrates generative modeling, sliding-window temporal processing, and decision fusion to achieve robust event detection and classification using synchrophasor data. A variational autoencoder-generative adversarial network is employed to model normal operating conditions, where both reconstruction error and discriminator error are extracted as anomaly indicators. Two complementary decision strategies are developed: a threshold-based rule for computational efficiency and a convex hull-based method for robustness under complex error distributions. These features are organized into spatiotemporal detection and classification matrices through a sliding-window mechanism, and an identification and decision fusion stage integrates the outputs across PMUs. This design enables the framework to identify known events while systematically classifying previously unseen disturbances into a new category, addressing a key limitation of supervised classifiers. Experimental results demonstrate state-of-the-art accuracy, surpassing machine learning, deep learning, and envelope-based baselines. The ability to recognize unknown events further highlights the adaptability and practical value of the proposed approach for wide-area event analysis in modern power systems.

