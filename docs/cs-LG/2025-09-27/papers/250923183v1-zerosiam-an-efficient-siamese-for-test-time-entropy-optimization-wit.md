---
layout: default
title: ZeroSiam: An Efficient Siamese for Test-Time Entropy Optimization without Collapse
---

# ZeroSiam: An Efficient Siamese for Test-Time Entropy Optimization without Collapse

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23183" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23183v1</a>
  <a href="https://arxiv.org/pdf/2509.23183.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23183v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23183v1', 'ZeroSiam: An Efficient Siamese for Test-Time Entropy Optimization without Collapse')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guohao Chen, Shuaicheng Niu, Deyu Chen, Jiahao Yang, Zitian Zhang, Mingkui Tan, Pengcheng Wu, Zhiqi Shen

**分类**: cs.LG, cs.NI

**发布日期**: 2025-09-27

---

## 💡 一句话要点

**提出ZeroSiam，通过Siamese架构和熵优化解决测试时模型坍塌问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `测试时自适应` `熵最小化` `Siamese网络` `模型坍塌` `非对称学习`

## 📋 核心要点

1. 测试时熵最小化能使模型适应新环境，提升推理能力，但易导致模型坍塌。
2. ZeroSiam通过非对称Siamese架构和散度对齐，有效防止模型坍塌，并正则化学习信号。
3. 实验表明，ZeroSiam在视觉和语言任务上，对多种模型均表现出稳定且优越的性能。

## 📝 摘要（中文）

本文提出ZeroSiam，一种高效的非对称Siamese架构，专为测试时熵最小化设计。纯粹的熵最小化可能倾向于非泛化的捷径，例如膨胀logit范数并将所有预测驱动到主导类别以减少熵，从而导致模型坍塌。ZeroSiam通过非对称散度对齐来防止坍塌，这通过可学习的预测器和分类器前的停止梯度算子有效实现。经验和理论证据表明，ZeroSiam不仅可以防止坍塌，还可以吸收和正则化有偏的学习信号，从而提高性能，即使没有发生坍塌。大量结果表明，ZeroSiam在使用可忽略的开销的情况下，比先前的方法表现更稳定，证明了其在具有挑战性的测试场景和各种模型（包括特别容易发生坍塌的小型模型）上的视觉适应和大型语言模型推理任务中的有效性。

## 🔬 方法详解

**问题定义**：测试时自适应旨在利用模型自身的预测在推理阶段持续改进，但直接最小化预测熵容易导致模型坍塌，即输出恒定的one-hot向量，从而获得极低的熵值，但丧失了泛化能力。现有方法难以有效防止这种坍塌现象，尤其是在小型模型上更为明显。

**核心思路**：ZeroSiam的核心思路是引入非对称的Siamese网络结构，通过一个可学习的预测器和一个停止梯度操作，实现非对称的散度对齐。这种设计能够有效地防止模型坍塌，同时还能吸收和正则化有偏的学习信号，从而提升模型的泛化能力。

**技术框架**：ZeroSiam包含两个分支，一个分支是原始模型，另一个分支是带有可学习预测器的模型。原始模型的输出经过分类器得到预测结果，而另一个分支的输出经过预测器后，与原始模型的输出进行散度对齐。在预测器之前，使用停止梯度操作，阻止梯度从原始模型流向预测器，从而实现非对称性。整体流程是在测试时，利用预测结果的熵和散度对齐损失来更新模型参数。

**关键创新**：ZeroSiam的关键创新在于其非对称的Siamese架构和非对称散度对齐方式。传统的Siamese网络通常是对称的，而ZeroSiam通过引入可学习的预测器和停止梯度操作，打破了这种对称性，从而更好地防止了模型坍塌。此外，非对称的散度对齐能够更有效地吸收和正则化有偏的学习信号。

**关键设计**：ZeroSiam的关键设计包括：1) 可学习的预测器，用于将一个分支的输出映射到另一个分支的输出空间；2) 停止梯度操作，阻止梯度从原始模型流向预测器，实现非对称性；3) 散度对齐损失，用于衡量两个分支输出之间的差异，并促使模型学习到更加鲁棒的特征表示。损失函数通常包含熵损失和散度对齐损失两部分，通过调整两者的权重来平衡熵最小化和防止坍塌。

## 📊 实验亮点

实验结果表明，ZeroSiam在视觉适应和大型语言模型推理任务上均表现出色。在多个数据集上，ZeroSiam相比于现有方法，在防止模型坍塌的同时，取得了更高的准确率。尤其是在小型模型上，ZeroSiam的优势更加明显，证明了其在资源受限环境下的有效性。

## 🎯 应用场景

ZeroSiam可应用于各种需要测试时自适应的场景，例如图像识别、目标检测、自然语言处理等。尤其适用于资源受限的边缘设备或小型模型，能够提升模型在未知环境下的鲁棒性和泛化能力。该方法在医疗诊断、自动驾驶等领域具有潜在的应用价值，可以提高模型在复杂和动态环境中的可靠性。

## 📄 摘要（原文）

> Test-time entropy minimization helps adapt a model to novel environments and incentivize its reasoning capability, unleashing the model's potential during inference by allowing it to evolve and improve in real-time using its own predictions, achieving promising performance. However, pure entropy minimization can favor non-generalizable shortcuts, such as inflating the logit norm and driving all predictions to a dominant class to reduce entropy, risking collapsed solutions (e.g., constant one-hot outputs) that trivially minimize the objective without meaningful learning. In this paper, we introduce ZeroSiam, an efficient asymmetric Siamese architecture tailored for test-time entropy minimization. ZeroSiam prevents collapse through asymmetric divergence alignment, which is efficiently achieved by a learnable predictor and a stop-gradient operator before the classifier. We provide empirical and theoretical evidence that ZeroSiam not only prevents collapse solutions, but also absorbs and regularizes biased learning signals, enhancing performance even when no collapse occurs. Despite its simplicity, extensive results show that ZeroSiam performs more stably over prior methods using negligible overhead, demonstrating efficacy on both vision adaptation and large language model reasoning tasks across challenging test scenarios and diverse models, including tiny models that are particularly collapse-prone.

