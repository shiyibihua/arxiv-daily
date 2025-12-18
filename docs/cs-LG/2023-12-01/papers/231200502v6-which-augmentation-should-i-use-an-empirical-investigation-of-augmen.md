---
layout: default
title: Which Augmentation Should I Use? An Empirical Investigation of Augmentations for Self-Supervised Phonocardiogram Representation Learning
---

# Which Augmentation Should I Use? An Empirical Investigation of Augmentations for Self-Supervised Phonocardiogram Representation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.00502" class="toolbar-btn" target="_blank">📄 arXiv: 2312.00502v6</a>
  <a href="https://arxiv.org/pdf/2312.00502.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.00502v6" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.00502v6', 'Which Augmentation Should I Use? An Empirical Investigation of Augmentations for Self-Supervised Phonocardiogram Representation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aristotelis Ballas, Vasileios Papapanagiotou, Christos Diou

**分类**: cs.LG, cs.SD, eess.AS, q-bio.QM

**发布日期**: 2023-12-01 (更新: 2025-01-04)

**备注**: Accepted in IEEE ACCESS: https://doi.org/10.1109/ACCESS.2024.3519297

**DOI**: [10.1109/ACCESS.2024.3519297](https://doi.org/10.1109/ACCESS.2024.3519297)

---

## 💡 一句话要点

**探索音频增强策略以提升自监督心音图分类模型的鲁棒性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自监督学习` `心音图分类` `数据增强` `模型鲁棒性` `对比学习` `音频处理` `医疗应用`

## 📋 核心要点

1. 现有方法在心音图分类中面临数据稀缺和标注不足的挑战，导致模型的泛化能力不足。
2. 本研究通过探索多种音频增强策略，评估其对自监督学习模型在PCG分类中的影响，旨在提升模型的鲁棒性。
3. 实验结果表明，选择合适的增强策略可以显著提高模型性能，SSL模型在未见数据上的性能下降仅为10%，而全监督模型则下降高达32%。

## 📝 摘要（中文）

尽管深度学习在多个领域取得了进展，但在医学应用中，如心音图（PCG）分类的应用仍然有限，主要由于缺乏高质量的标注数据。自监督学习（SSL）对抗学习在缓解数据稀缺问题上显示出潜力，但在PCG分类中，数据增强的影响尚未得到充分研究。本文通过对多种音频增强策略的评估，揭示了增强选择对模型鲁棒性的显著影响，并为PCG信号处理提供了有价值的指导。

## 🔬 方法详解

**问题定义**：本文旨在解决在心音图分类中，数据增强策略选择不当导致模型性能下降的问题。现有方法在这一领域的研究相对较少，缺乏系统的比较分析。

**核心思路**：通过对多种音频增强策略的系统评估，探索哪些增强组合能够有效提升自监督学习模型的性能，特别是在处理未见数据时的鲁棒性。

**技术框架**：研究采用了对比学习的自监督学习框架，结合多种音频增强技术，进行全面的实验评估。主要模块包括数据预处理、增强策略应用、模型训练和性能评估。

**关键创新**：本研究的创新在于系统性地评估了多种音频增强策略对PCG分类模型的影响，揭示了增强选择对模型鲁棒性的关键作用，填补了该领域的研究空白。

**关键设计**：在实验中，设置了多种增强参数，并使用了适应性损失函数来优化模型训练，确保模型在不同数据分布下的有效性。

## 📊 实验亮点

实验结果显示，选择合适的音频增强策略对模型性能有显著影响。全监督模型在未见数据上的性能下降高达32%，而自监督模型在相同条件下仅下降10%，甚至在某些情况下表现出性能提升，证明了SSL模型的鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗诊断、心脏病监测和远程医疗等。通过提升心音图分类模型的鲁棒性，能够更好地应对临床环境中的数据稀缺问题，进而推动智能医疗的发展，提升患者的健康管理水平。

## 📄 摘要（原文）

> Despite recent advancements in deep learning, its application in real-world medical settings, such as phonocardiogram (PCG) classification, remains limited. A significant barrier is the lack of high-quality annotated datasets, which hampers the development of robust, generalizable models that can perform well on newly collected, out-of-distribution (OOD) data. Self-Supervised Learning (SSL) contrastive learning, has shown promise in mitigating the issue of data scarcity by using unlabeled data to enhance model robustness. Even though SSL methods have been proposed and researched in other domains, works focusing on the impact of data augmentations on model robustness for PCG classification are limited. In particular, while augmentations are a key component in SSL, selecting the most suitable policy during training is highly challenging. Improper augmentations can lead to substantial performance degradation and even hinder a network's ability to learn meaningful representations. Addressing this gap, our research aims to explore and evaluate a wide range of audio-based augmentations and uncover combinations that enhance SSL model performance in PCG classification. We conduct a comprehensive comparative analysis across multiple datasets, assessing the impact of various augmentations on model performance. Our findings reveal that depending on the training distribution, augmentation choice significantly influences model robustness, with fully-supervised models experiencing up to a 32\% drop in effectiveness when evaluated on unseen data, while SSL models demonstrate greater resilience, losing only 10\% or even improving in some cases. This study also highlights the most promising and appropriate augmentations for PCG signal processing, by calculating their effect size on training. These insights equip researchers with valuable guidelines for developing reliable models in PCG signal processing.

