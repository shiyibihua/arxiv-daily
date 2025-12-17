---
layout: default
title: GeoToken: Hierarchical Geolocalization of Images via Next Token Prediction
---

# GeoToken: Hierarchical Geolocalization of Images via Next Token Prediction

**arXiv**: [2511.01082v1](https://arxiv.org/abs/2511.01082) | [PDF](https://arxiv.org/pdf/2511.01082.pdf)

**作者**: Narges Ghasemi, Amir Ziashahabi, Salman Avestimehr, Cyrus Shahabi

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-11-02

**备注**: Accepted to IEEE International Conference on Data Mining (ICDM) 2025

**🔗 代码/项目**: [GITHUB](https://github.com/NNargesNN/GeoToken)

---

## 💡 一句话要点

**GeoToken：通过预测地理位置Token序列实现图像的层级地理定位**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `图像地理定位` `层级预测` `序列预测` `自回归模型` `S2单元格`

## 📋 核心要点

1. 图像地理定位面临跨区域视觉相似性和大搜索空间的挑战，现有方法难以有效应对。
2. GeoToken通过层级预测地理Token序列，模拟人类由粗到精的定位方式，利用S2单元格进行多分辨率划分。
3. 实验表明，GeoToken在Im2GPS3k和YFCC4k数据集上显著优于现有方法，无需MLLM时准确率提升高达13.9%。

## 📝 摘要（中文）

图像地理定位，即确定图像的地理来源，面临着巨大的挑战，这主要是由于不同位置之间存在视觉相似性以及搜索空间巨大。为了解决这些问题，我们提出了一种层级序列预测方法，其灵感来源于人类从广阔区域缩小到特定地址的定位方式。类似地，我们的模型以层级方式预测地理Token，首先识别一个大致区域，然后依次细化预测到越来越精确的位置。我们的方法没有依赖显式的语义划分，而是使用S2单元格（一种嵌套的多分辨率全局网格），并根据视觉输入和先前的预测，依次预测更精细级别的单元格。这个过程类似于大型语言模型中的自回归文本生成。与语言建模类似，最终性能不仅取决于训练，还取决于推理时的策略。我们研究了多种自顶向下的遍历方法来进行自回归采样，结合了语言模型中使用的测试时计算缩放技术。具体来说，我们集成了束搜索和多样本推理，同时探索了各种选择策略来确定最终输出。这使得模型能够通过探索层次结构中的多个合理路径来管理不确定性。我们在Im2GPS3k和YFCC4k数据集上评估了我们的方法，并针对两组不同的基线进行了评估：一组是不使用多模态大型语言模型（MLLM）的基线，另一组是利用MLLM的基线。在没有MLLM的情况下，我们的模型在几乎所有指标上都超过了其他可比基线，实现了最先进的性能，准确率提高了高达13.9%。当使用MLLM增强时，我们的模型优于所有基线，并在所有指标上都创造了新的最先进水平。源代码可在https://github.com/NNargesNN/GeoToken 获得。

## 🔬 方法详解

**问题定义**：图像地理定位旨在确定图像的地理位置。现有方法的痛点在于，不同地理位置可能存在视觉相似性，导致模型难以区分。此外，地理位置的搜索空间非常大，使得精确定位变得困难。

**核心思路**：GeoToken的核心思路是模仿人类由粗到精的定位过程，通过层级化的方式预测地理位置。模型首先预测一个大的地理区域，然后逐步细化预测，最终确定精确的位置。这种方法将地理定位问题转化为一个序列预测问题，类似于自然语言处理中的文本生成。

**技术框架**：GeoToken的整体框架包括以下几个主要阶段：1) 图像特征提取：使用卷积神经网络（CNN）提取图像的视觉特征。2) 层级地理编码：使用S2单元格对地球进行层级划分，每个单元格代表一个地理区域。3) 自回归预测：模型根据图像特征和之前预测的地理Token，自回归地预测下一个更精细的地理Token。4) 推理策略：采用束搜索和多样本推理等策略，探索多个可能的地理位置序列，以提高定位的准确性。

**关键创新**：GeoToken最重要的技术创新点在于其层级化的地理Token预测方法。与传统的直接预测经纬度坐标的方法不同，GeoToken将地理定位问题分解为一系列的序列预测任务，从而降低了问题的复杂度。此外，GeoToken还借鉴了自然语言处理中的自回归模型和推理策略，进一步提高了定位的准确性。

**关键设计**：GeoToken的关键设计包括：1) S2单元格的使用：S2单元格提供了一种有效的层级地理编码方式，可以方便地进行多分辨率的地理位置表示。2) 自回归模型的选择：可以选择Transformer等自回归模型进行地理Token的预测。3) 推理策略的优化：束搜索的宽度、多样本推理的样本数量等参数需要根据具体数据集进行调整。4) 损失函数的设计：可以使用交叉熵损失函数来训练模型，目标是最大化正确地理Token序列的概率。

## 📊 实验亮点

GeoToken在Im2GPS3k和YFCC4k数据集上取得了显著的性能提升。在不使用MLLM的情况下，GeoToken在几乎所有指标上都超过了其他可比基线，准确率提升高达13.9%。当使用MLLM增强时，GeoToken优于所有基线，并在所有指标上都创造了新的state-of-the-art。

## 🎯 应用场景

GeoToken在自动驾驶、增强现实、地理信息系统等领域具有广泛的应用前景。它可以帮助自动驾驶车辆进行精确定位，为AR应用提供地理位置信息，并提高地理信息系统的准确性和效率。未来，GeoToken有望应用于更广泛的场景，例如旅游推荐、社交媒体内容定位等。

## 📄 摘要（原文）

> Image geolocalization, the task of determining an image's geographic origin, poses significant challenges, largely due to visual similarities across disparate locations and the large search space. To address these issues, we propose a hierarchical sequence prediction approach inspired by how humans narrow down locations from broad regions to specific addresses. Analogously, our model predicts geographic tokens hierarchically, first identifying a general region and then sequentially refining predictions to increasingly precise locations. Rather than relying on explicit semantic partitions, our method uses S2 cells, a nested, multiresolution global grid, and sequentially predicts finer-level cells conditioned on visual inputs and previous predictions. This procedure mirrors autoregressive text generation in large language models. Much like in language modeling, final performance depends not only on training but also on inference-time strategy. We investigate multiple top-down traversal methods for autoregressive sampling, incorporating techniques from test-time compute scaling used in language models. Specifically, we integrate beam search and multi-sample inference while exploring various selection strategies to determine the final output. This enables the model to manage uncertainty by exploring multiple plausible paths through the hierarchy. We evaluate our method on the Im2GPS3k and YFCC4k datasets against two distinct sets of baselines: those that operate without a Multimodal Large Language Model (MLLM) and those that leverage one. In the MLLM-free setting, our model surpasses other comparable baselines on nearly all metrics, achieving state-of-the-art performance with accuracy gains of up to 13.9%. When augmented with an MLLM, our model outperforms all baselines, setting a new state-of-the-art across all metrics. The source code is available at https://github.com/NNargesNN/GeoToken.

