---
layout: default
title: Binary Autoencoder for Mechanistic Interpretability of Large Language Models
---

# Binary Autoencoder for Mechanistic Interpretability of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20997" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20997v1</a>
  <a href="https://arxiv.org/pdf/2509.20997.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20997v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20997v1', 'Binary Autoencoder for Mechanistic Interpretability of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hakaze Cho, Haolin Yang, Brian M. Kurkoski, Naoya Inoue

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-09-25

**备注**: 36 pages, 41 figures, 3 tables

---

## 💡 一句话要点

**提出二值自编码器(BAE)，用于大语言模型机制可解释性的特征解耦。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `可解释性` `自编码器` `特征解耦` `二值化` `熵最小化` `原子化特征`

## 📋 核心要点

1. 现有方法依赖隐式正则化，缺乏全局稀疏性保证，导致大量密集特征，影响特征稀疏性和原子化。
2. 提出二值自编码器(BAE)，通过最小化minibatch隐藏激活熵，促进特征独立性和跨实例稀疏性。
3. 实验表明，BAE能有效计算特征集熵，并提取更多可解释的原子化特征，优于现有方法。

## 📝 摘要（中文）

本文提出了一种新颖的自编码器变体，旨在解决现有方法在解耦大语言模型(LLM)隐藏状态中的原子化数值成分（特征）时，依赖于受隐式训练时正则化约束的自编码器，缺乏全局稀疏性保证的问题。该方法通过在隐藏激活的minibatch上强制执行最小熵，从而促进跨实例的特征独立性和稀疏性。为了高效计算熵，我们将隐藏激活通过阶跃函数离散化为1比特，并应用梯度估计以实现反向传播，因此我们将其命名为二值自编码器(BAE)。实验表明，BAE在两个主要应用中表现出色：(1)特征集熵计算，BAE可以可靠地估计二值隐藏激活上的熵，用于表征LLM的推理动态和上下文学习。(2)特征解耦，BAE可以提取LLM隐藏状态中的原子化特征。为了稳健地评估特征提取能力，我们改进了传统的特征解释方法，避免不可靠的数值token处理，结果表明BAE避免了密集特征，同时产生了最多的可解释特征，证实了BAE作为特征提取器的有效性。

## 🔬 方法详解

**问题定义**：现有的大语言模型可解释性研究致力于从隐藏状态中解耦原子化的数值成分（特征）。然而，现有方法依赖于受隐式训练时正则化约束的自编码器，例如L1正则化或top-k函数，这些方法在单个训练实例上进行约束，无法保证跨实例的全局稀疏性。这导致大量特征同时处于非激活状态，降低了特征的稀疏性和原子化程度。

**核心思路**：本文的核心思路是通过在隐藏激活的minibatch上强制执行最小熵，来促进跨实例的特征独立性和稀疏性。最小熵鼓励每个特征在不同的实例中具有不同的激活状态，从而避免出现大量同时非激活的密集特征。通过将隐藏激活二值化，可以更有效地计算熵，并利用梯度估计进行反向传播。

**技术框架**：BAE的整体框架包括一个标准的自编码器结构，由编码器和解码器组成。编码器将LLM的隐藏状态作为输入，将其映射到低维的隐藏表示。关键在于隐藏表示的激活值会被二值化，然后用于计算熵损失。解码器将二值化的隐藏表示重构回原始的隐藏状态。整个训练过程通过最小化重构损失和熵损失来进行优化。

**关键创新**：BAE最重要的创新点在于引入了二值化操作和熵损失，以显式地促进跨实例的特征稀疏性和独立性。与现有方法隐式地依赖正则化不同，BAE通过直接优化熵来控制特征的激活模式。此外，二值化操作使得熵的计算更加高效，并允许使用梯度估计进行反向传播。

**关键设计**：BAE的关键设计包括：1) 使用阶跃函数进行二值化，将隐藏激活离散化为1比特。2) 使用梯度估计技术（例如Straight-Through Estimator）来近似阶跃函数的梯度，从而实现反向传播。3) 使用交叉熵作为熵损失函数，鼓励特征在minibatch中具有不同的激活状态。4) 平衡重构损失和熵损失的权重，以在特征解耦和重构精度之间取得平衡。

## 📊 实验亮点

实验结果表明，BAE能够有效地避免密集特征的产生，并提取出比现有方法更多的可解释特征。通过改进的特征解释方法，BAE在特征解耦方面取得了显著的提升。此外，BAE能够可靠地估计二值隐藏激活上的熵，用于表征LLM的推理动态和上下文学习。

## 🎯 应用场景

该研究成果可应用于大语言模型的机制可解释性分析，帮助研究人员理解模型内部的推理过程和知识表示方式。通过提取原子化的特征，可以更好地诊断模型的行为，发现潜在的偏差或漏洞，并为模型的改进提供指导。此外，该方法还可以用于上下文学习的分析，揭示模型如何利用上下文信息进行预测。

## 📄 摘要（原文）

> Existing works are dedicated to untangling atomized numerical components (features) from the hidden states of Large Language Models (LLMs) for interpreting their mechanism. However, they typically rely on autoencoders constrained by some implicit training-time regularization on single training instances (i.e., $L_1$ normalization, top-k function, etc.), without an explicit guarantee of global sparsity among instances, causing a large amount of dense (simultaneously inactive) features, harming the feature sparsity and atomization. In this paper, we propose a novel autoencoder variant that enforces minimal entropy on minibatches of hidden activations, thereby promoting feature independence and sparsity across instances. For efficient entropy calculation, we discretize the hidden activations to 1-bit via a step function and apply gradient estimation to enable backpropagation, so that we term it as Binary Autoencoder (BAE) and empirically demonstrate two major applications: (1) Feature set entropy calculation. Entropy can be reliably estimated on binary hidden activations, which we empirically evaluate and leverage to characterize the inference dynamics of LLMs and In-context Learning. (2) Feature untangling. Similar to typical methods, BAE can extract atomized features from LLM's hidden states. To robustly evaluate such feature extraction capability, we refine traditional feature-interpretation methods to avoid unreliable handling of numerical tokens, and show that BAE avoids dense features while producing the largest number of interpretable ones among baselines, which confirms the effectiveness of BAE serving as a feature extractor.

