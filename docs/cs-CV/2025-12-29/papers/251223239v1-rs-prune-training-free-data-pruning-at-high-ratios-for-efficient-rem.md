---
layout: default
title: "RS-Prune: Training-Free Data Pruning at High Ratios for Efficient Remote Sensing Diffusion Foundation Models"
---

# RS-Prune: Training-Free Data Pruning at High Ratios for Efficient Remote Sensing Diffusion Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23239" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23239v1</a>
  <a href="https://arxiv.org/pdf/2512.23239.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23239v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23239v1', 'RS-Prune: Training-Free Data Pruning at High Ratios for Efficient Remote Sensing Diffusion Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fan Wei, Runmin Dong, Yushan Lai, Yixiang Yang, Zhaoyang Luo, Jinxiao Zhang, Miao Yang, Shuai Yuan, Jiyao Zhao, Bin Luo, Haohuan Fu

**分类**: cs.CV

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**RS-Prune：面向遥感扩散模型的高比例免训练数据剪枝**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `遥感图像` `扩散模型` `数据剪枝` `免训练` `场景感知聚类`

## 📋 核心要点

1. 遥感扩散模型训练依赖大量数据，但数据中存在冗余、噪声和类别不平衡问题，影响训练效率和模型收敛。
2. 提出一种免训练的两阶段数据剪枝方法，通过熵值筛选低信息样本，并结合场景感知聚类和分层抽样，选择高质量数据子集。
3. 实验表明，即使剪枝85%的数据，该方法仍能显著提升模型收敛速度和生成质量，并在下游任务中取得SOTA性能。

## 📝 摘要（中文）

基于扩散的遥感（RS）生成式基础模型对于下游任务至关重要。然而，这些模型依赖于大量的全局代表性数据，这些数据通常包含冗余、噪声和类别不平衡，从而降低了训练效率并阻碍了收敛。现有的RS扩散基础模型通常聚合多个分类数据集或应用简单的去重，忽略了生成建模的分布需求和RS图像的异质性。为了解决这些限制，我们提出了一种免训练的两阶段数据剪枝方法，该方法能够快速选择高质量的子集，即使在高剪枝率下也能实现初步基础模型的快速收敛，并作为生成、下游微调和其他应用的多功能骨干网络。我们的方法联合考虑了局部信息内容与全局场景级别的多样性和代表性。首先，基于熵的标准有效地移除低信息量的样本。接下来，利用RS场景分类数据集作为参考基准，我们执行场景感知的聚类和分层抽样，以提高聚类效果，同时降低大规模无标签数据的计算成本。最后，通过平衡聚类级别的均匀性和样本代表性，该方法能够在高剪枝率下进行细粒度选择，同时保持整体的多样性和代表性。实验表明，即使在剪枝85%的训练数据后，我们的方法也能显著提高收敛性和生成质量。此外，使用我们的方法训练的扩散基础模型在包括超分辨率和语义图像合成在内的下游任务中始终取得最先进的性能。这种数据剪枝范式为开发RS生成式基础模型提供了实践指导。

## 🔬 方法详解

**问题定义**：遥感扩散模型训练需要大量数据，但现有数据集存在冗余、噪声和类别不平衡等问题，导致训练效率低下，模型难以收敛。现有方法通常采用简单的数据去重或直接聚合多个数据集，忽略了遥感图像的异质性和生成模型的分布需求。

**核心思路**：通过两阶段的数据剪枝策略，在不进行模型训练的前提下，从原始数据集中选择一个高质量、具有代表性的子集。第一阶段基于熵值去除低信息量样本，第二阶段利用场景分类信息进行聚类和分层抽样，保证数据子集的多样性和代表性。

**技术框架**：该方法包含两个主要阶段：1) 基于熵值的信息量筛选：计算每个样本的信息熵，去除熵值较低的样本，从而过滤掉冗余和无信息的图像。2) 场景感知的聚类和分层抽样：利用遥感场景分类数据集作为参考，对剩余样本进行聚类，并根据场景类别进行分层抽样，保证每个场景类别都有足够的样本被保留。

**关键创新**：该方法的核心创新在于结合了局部信息内容（熵值）和全局场景级别的多样性和代表性。传统的剪枝方法通常只关注单个样本的信息量，而忽略了数据集的整体分布。该方法通过场景感知的聚类和分层抽样，保证了剪枝后的数据集仍然能够覆盖原始数据集的各种场景，从而提高了模型的泛化能力。

**关键设计**：在信息量筛选阶段，使用图像的像素值计算熵值。在场景感知聚类阶段，使用预训练的场景分类模型提取图像的特征，然后使用K-means算法进行聚类。在分层抽样阶段，根据每个聚类的样本数量，按照比例进行抽样，保证每个场景类别都有足够的样本被保留。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23239v1/Pictures/head.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23239v1/Pictures/0ef27c9b830072a346925b518d7876ee.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23239v1/x1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，即使剪枝85%的训练数据，使用RS-Prune方法训练的扩散模型在收敛速度和生成质量上均有显著提升。此外，该模型在超分辨率和语义图像合成等下游任务中取得了state-of-the-art的性能，验证了该数据剪枝方法的有效性和泛化能力。

## 🎯 应用场景

该研究成果可应用于遥感图像生成、超分辨率重建、语义图像合成等领域。通过高效的数据剪枝，可以降低遥感扩散模型训练的计算成本和时间成本，加速遥感基础模型的发展，并为下游应用提供更高质量的数据支持，具有重要的实际应用价值和广阔的应用前景。

## 📄 摘要（原文）

> Diffusion-based remote sensing (RS) generative foundation models are cruial for downstream tasks. However, these models rely on large amounts of globally representative data, which often contain redundancy, noise, and class imbalance, reducing training efficiency and preventing convergence. Existing RS diffusion foundation models typically aggregate multiple classification datasets or apply simplistic deduplication, overlooking the distributional requirements of generation modeling and the heterogeneity of RS imagery. To address these limitations, we propose a training-free, two-stage data pruning approach that quickly select a high-quality subset under high pruning ratios, enabling a preliminary foundation model to converge rapidly and serve as a versatile backbone for generation, downstream fine-tuning, and other applications. Our method jointly considers local information content with global scene-level diversity and representativeness. First, an entropy-based criterion efficiently removes low-information samples. Next, leveraging RS scene classification datasets as reference benchmarks, we perform scene-aware clustering with stratified sampling to improve clustering effectiveness while reducing computational costs on large-scale unlabeled data. Finally, by balancing cluster-level uniformity and sample representativeness, the method enables fine-grained selection under high pruning ratios while preserving overall diversity and representativeness. Experiments show that, even after pruning 85\% of the training data, our method significantly improves convergence and generation quality. Furthermore, diffusion foundation models trained with our method consistently achieve state-of-the-art performance across downstream tasks, including super-resolution and semantic image synthesis. This data pruning paradigm offers practical guidance for developing RS generative foundation models.

