---
layout: default
title: Explaining Recovery Trajectories of Older Adults Post Lower-Limb Fracture Using Modality-wise Multiview Clustering and Large Language Models
---

# Explaining Recovery Trajectories of Older Adults Post Lower-Limb Fracture Using Modality-wise Multiview Clustering and Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12156" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12156v1</a>
  <a href="https://arxiv.org/pdf/2506.12156.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12156v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12156v1', 'Explaining Recovery Trajectories of Older Adults Post Lower-Limb Fracture Using Modality-wise Multiview Clustering and Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shehroz S. Khan, Ali Abedi, Charlene H. Chu

**分类**: cs.LG, cs.AI, cs.CV

**发布日期**: 2025-06-13

**备注**: 15 pages, 2 figures, 3 tables

---

## 💡 一句话要点

**提出多模态聚类与大语言模型以解释老年人下肢骨折恢复轨迹**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态聚类` `大语言模型` `无监督学习` `健康数据分析` `老年医学` `康复治疗` `传感器数据`

## 📋 核心要点

1. 现有的无监督医疗数据分析方法在解释聚类数据时面临挑战，难以为临床提供有效的健康洞察。
2. 论文提出通过多模态传感器数据的单独聚类和大语言模型的上下文感知提示，生成有意义的聚类标签。
3. 实验结果表明，大语言模型生成的聚类标签与临床评分之间存在显著的统计相关性，验证了方法的有效性。

## 📝 摘要（中文）

理解大量高维无标签数据并使其对人类可理解仍然是各领域的一大挑战。本文针对老年患者下肢骨折恢复过程中收集的传感器数据进行聚类分析，提出了一种无监督的数据分析方法。通过对560天的多模态传感器数据进行单独聚类，并利用大语言模型生成有意义的聚类标签，验证了聚类结果与临床评分的统计显著性。这一方法能够帮助临床医生识别高风险患者，从而及时采取措施改善健康结果。

## 🔬 方法详解

**问题定义**：本文旨在解决如何有效解释老年患者下肢骨折恢复过程中收集的高维无标签传感器数据的问题。现有方法在处理此类数据时，往往缺乏有效的聚类解释，导致临床应用受限。

**核心思路**：论文的核心思路是通过对不同数据模态进行单独聚类，结合大语言模型生成聚类标签，从而为临床提供可解释的健康洞察。这样的设计能够充分利用多模态数据的特性，提升聚类结果的可理解性。

**技术框架**：整体流程包括数据收集、模态单独聚类、上下文感知提示生成聚类标签、以及通过统计测试和可视化验证聚类质量。主要模块包括数据预处理、聚类算法应用和大语言模型的标签生成。

**关键创新**：最重要的创新点在于结合了多模态聚类与大语言模型的能力，实现了无监督数据分析的可解释性。这一方法与传统的聚类分析方法相比，能够提供更具临床意义的聚类标签。

**关键设计**：在聚类过程中，采用了针对每种模态的特征提取方法，并通过上下文感知的提示设计来优化大语言模型的输出。具体的参数设置和损失函数设计尚未详细披露，需进一步研究。

## 📊 实验亮点

实验结果显示，大语言模型生成的聚类标签与临床评分之间存在显著的统计相关性，验证了该方法的有效性。具体而言，大多数模态特定的聚类标签在统计上显著，与临床评分的相关性增强了临床决策的依据。

## 🎯 应用场景

该研究的潜在应用领域包括老年医学、康复治疗和智能健康监测等。通过提供可解释的健康数据分析，临床医生能够更好地识别高风险患者，并制定个性化的治疗方案，从而提高患者的健康结果和生活质量。

## 📄 摘要（原文）

> Interpreting large volumes of high-dimensional, unlabeled data in a manner that is comprehensible to humans remains a significant challenge across various domains. In unsupervised healthcare data analysis, interpreting clustered data can offer meaningful insights into patients' health outcomes, which hold direct implications for healthcare providers. This paper addresses the problem of interpreting clustered sensor data collected from older adult patients recovering from lower-limb fractures in the community. A total of 560 days of multimodal sensor data, including acceleration, step count, ambient motion, GPS location, heart rate, and sleep, alongside clinical scores, were remotely collected from patients at home. Clustering was first carried out separately for each data modality to assess the impact of feature sets extracted from each modality on patients' recovery trajectories. Then, using context-aware prompting, a large language model was employed to infer meaningful cluster labels for the clusters derived from each modality. The quality of these clusters and their corresponding labels was validated through rigorous statistical testing and visualization against clinical scores collected alongside the multimodal sensor data. The results demonstrated the statistical significance of most modality-specific cluster labels generated by the large language model with respect to clinical scores, confirming the efficacy of the proposed method for interpreting sensor data in an unsupervised manner. This unsupervised data analysis approach, relying solely on sensor data, enables clinicians to identify at-risk patients and take timely measures to improve health outcomes.

