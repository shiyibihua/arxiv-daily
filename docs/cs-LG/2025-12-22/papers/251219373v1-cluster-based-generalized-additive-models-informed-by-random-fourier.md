---
layout: default
title: Cluster-Based Generalized Additive Models Informed by Random Fourier Features
---

# Cluster-Based Generalized Additive Models Informed by Random Fourier Features

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19373" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19373v1</a>
  <a href="https://arxiv.org/pdf/2512.19373.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19373v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19373v1', 'Cluster-Based Generalized Additive Models Informed by Random Fourier Features')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xin Huang, Jia Li, Jun Yu

**分类**: stat.ML, cs.LG

**发布日期**: 2025-12-22

**备注**: 25 pages, 13 figures, 4 tables

---

## 💡 一句话要点

**提出基于随机傅里叶特征的聚类广义加性模型，提升可解释回归任务的预测性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `可解释机器学习` `广义加性模型` `随机傅里叶特征` `聚类分析` `回归分析`

## 📋 核心要点

1. 深度神经网络等黑盒模型预测能力强但缺乏可解释性，如何在预测精度和模型透明度之间取得平衡是一个挑战。
2. 论文提出一种混合广义加性模型，利用随机傅里叶特征学习数据局部结构，并通过软聚类构建局部GAMs。
3. 实验表明，在真实回归数据集上，该方法相对于经典可解释模型，预测性能有所提升，实现了表示学习与透明统计建模的结合。

## 📝 摘要（中文）

本文提出了一种混合广义加性模型（GAMs），该模型利用随机傅里叶特征（RFF）表示来揭示数据中局部自适应结构。该方法首先学习基于RFF的嵌入，然后通过主成分分析进行压缩。得到的低维表示用于通过高斯混合模型对数据进行软聚类。这些聚类分配随后被应用于构建混合GAMs框架，其中每个局部GAM通过可解释的单变量平滑函数捕获非线性效应。在包括加州住房、NASA翼型自噪声和自行车共享数据集在内的真实回归基准上的数值实验表明，相对于经典的可解释模型，预测性能有所提高。总而言之，这种构建为将表示学习与透明统计建模相结合提供了一种原则性方法。

## 🔬 方法详解

**问题定义**：现有黑盒模型，如深度神经网络，虽然预测精度高，但缺乏可解释性。传统可解释模型，如线性回归，表达能力有限，难以捕捉复杂非线性关系。因此，如何在保证预测精度的同时，提高模型的可解释性是一个关键问题。

**核心思路**：论文的核心思路是将数据进行聚类，然后在每个簇内使用广义加性模型（GAM）进行建模。通过聚类，可以将复杂的数据分布分解为多个局部简单的分布，从而可以使用GAM在每个局部进行更精确的建模。同时，GAM本身具有良好的可解释性，可以清晰地展示每个特征对预测结果的影响。

**技术框架**：该方法主要包含以下几个阶段：1. **RFF嵌入学习**：使用随机傅里叶特征（RFF）将原始数据映射到高维空间，以便更好地捕捉非线性关系。2. **降维**：通过主成分分析（PCA）对RFF嵌入进行降维，减少计算复杂度。3. **软聚类**：使用高斯混合模型（GMM）对降维后的数据进行软聚类，得到每个数据点属于每个簇的概率。4. **混合GAM建模**：在每个簇内，使用GAM进行建模，其中每个GAM使用可解释的单变量平滑函数来捕捉非线性效应。最终的预测结果是所有GAM的加权平均，权重为数据点属于每个簇的概率。

**关键创新**：该方法最重要的创新点在于将表示学习（RFF嵌入）与可解释的统计建模（GAM）相结合。通过RFF嵌入，可以有效地捕捉非线性关系，而GAM则保证了模型的可解释性。此外，使用软聚类可以更好地处理数据分布的复杂性，避免硬聚类可能导致的误差。

**关键设计**：RFF的参数（如傅里叶基的数量）需要根据数据集的复杂程度进行调整。GMM的簇的数量也需要根据数据的分布进行选择。GAM中使用的平滑函数的类型（如样条函数）和参数也需要进行调整，以获得最佳的预测性能。损失函数通常是均方误差或对数似然函数，具体取决于回归任务的类型。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19373v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19373v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19373v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在加州住房、NASA翼型自噪声和自行车共享数据集上的实验结果表明，该方法相对于经典的可解释模型，如线性回归和GAM，预测性能有所提高。具体提升幅度取决于数据集的复杂程度和参数的调整情况。实验结果验证了该方法在可解释回归任务中的有效性。

## 🎯 应用场景

该研究成果可应用于需要高预测精度和可解释性的回归任务，例如金融风险评估、医疗诊断、环境监测等领域。通过该方法，可以更好地理解模型预测的原因，从而提高决策的可靠性和透明度。未来，该方法可以扩展到分类任务和其他类型的可解释模型。

## 📄 摘要（原文）

> Explainable machine learning aims to strike a balance between prediction accuracy and model transparency, particularly in settings where black-box predictive models, such as deep neural networks or kernel-based methods, achieve strong empirical performance but remain difficult to interpret. This work introduces a mixture of generalized additive models (GAMs) in which random Fourier feature (RFF) representations are leveraged to uncover locally adaptive structure in the data. In the proposed method, an RFF-based embedding is first learned and then compressed via principal component analysis. The resulting low-dimensional representations are used to perform soft clustering of the data through a Gaussian mixture model. These cluster assignments are then applied to construct a mixture-of-GAMs framework, where each local GAM captures nonlinear effects through interpretable univariate smooth functions. Numerical experiments on real-world regression benchmarks, including the California Housing, NASA Airfoil Self-Noise, and Bike Sharing datasets, demonstrate improved predictive performance relative to classical interpretable models. Overall, this construction provides a principled approach for integrating representation learning with transparent statistical modeling.

