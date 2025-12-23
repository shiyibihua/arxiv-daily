---
layout: default
title: Benchmarking Deep Learning and Vision Foundation Models for Atypical vs. Normal Mitosis Classification with Cross-Dataset Evaluation
---

# Benchmarking Deep Learning and Vision Foundation Models for Atypical vs. Normal Mitosis Classification with Cross-Dataset Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21444" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21444v2</a>
  <a href="https://arxiv.org/pdf/2506.21444.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21444v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21444v2', 'Benchmarking Deep Learning and Vision Foundation Models for Atypical vs. Normal Mitosis Classification with Cross-Dataset Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sweta Banerjee, Viktoria Weiss, Taryn A. Donovan, Rutger H. J. Fick, Thomas Conrad, Jonas Ammeling, Nils Porsche, Robert Klopfleisch, Christopher Kaltenecker, Katharina Breininger, Marc Aubreville, Christof A. Bertram

**分类**: cs.CV

**发布日期**: 2025-06-26 (更新: 2025-07-16)

**🔗 代码/项目**: [GITHUB](https://github.com/DeepMicroscopy/AMi-Br_Benchmark)

---

## 💡 一句话要点

**基于深度学习的非典型有丝分裂分类基准研究**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `非典型有丝分裂` `深度学习` `转移学习` `模型微调` `肿瘤病理学` `数据集评估` `图像分类`

## 📋 核心要点

1. 非典型有丝分裂分类面临低发生率、微妙形态差异和类别不平衡等挑战，现有方法效果不佳。
2. 本研究提出了基于深度学习的多种方法，包括端到端训练模型和微调的基础模型，以提高分类准确性。
3. 在AMi-Br、AtNorM-Br和AtNorM-MD数据集上，平均平衡准确率分别达到0.8135、0.7788和0.7723，显示出显著的性能提升。

## 📝 摘要（中文）

非典型有丝分裂标志着细胞分裂过程的偏差，已被证明是肿瘤恶性程度的独立预后标志。然而，由于其低发生率、与正常有丝分裂形态的微妙差异、病理学家之间的低一致性以及数据集中的类别不平衡，非典型有丝分裂分类仍然具有挑战性。本研究基于乳腺癌非典型有丝分裂数据集（AMi-Br），全面比较了多种深度学习方法在自动化非典型有丝分裂图像分类中的表现。我们引入了两个新的数据集进行严格评估，并在各个数据集上取得了平均平衡准确率的显著提升。我们的研究表明，尽管非典型有丝分裂分类是一个具有挑战性的问题，但通过转移学习和模型微调技术的最新进展，可以有效解决。

## 🔬 方法详解

**问题定义**：本研究旨在解决非典型有丝分裂分类中的低发生率和类别不平衡等问题。现有方法在处理微妙的形态差异和病理学家之间的一致性方面存在不足。

**核心思路**：论文通过比较多种深度学习方法，特别是端到端训练和微调基础模型，来提高非典型有丝分裂图像的分类性能。这样的设计旨在利用最新的转移学习技术，提升模型在不同数据集上的泛化能力。

**技术框架**：整体架构包括数据预处理、模型训练和评估三个主要阶段。首先，使用AMi-Br数据集进行模型训练，然后在AtNorM-Br和AtNorM-MD数据集上进行验证和测试。

**关键创新**：本研究的主要创新在于引入了新的数据集和评估标准，并比较了多种深度学习方法的有效性，尤其是低秩适应（LoRA）技术的应用。与现有方法相比，能够更好地处理类别不平衡和微妙的形态差异。

**关键设计**：在模型训练中，采用了特定的损失函数和网络结构，确保模型能够有效学习到非典型有丝分裂的特征。同时，使用了线性探测和微调策略，以优化模型在不同数据集上的表现。

## 📊 实验亮点

在本研究中，模型在AMi-Br、AtNorM-Br和AtNorM-MD数据集上的平均平衡准确率分别达到了0.8135、0.7788和0.7723，显示出显著的性能提升。这些结果表明，采用深度学习方法能够有效解决非典型有丝分裂分类中的挑战。

## 🎯 应用场景

该研究的潜在应用领域包括肿瘤病理学和临床诊断，能够帮助病理学家更准确地识别非典型有丝分裂，从而提高肿瘤恶性程度的评估和治疗决策的准确性。未来，该方法有望推广到其他类型的细胞分类任务中，进一步推动医学影像分析的发展。

## 📄 摘要（原文）

> Atypical mitosis marks a deviation in the cell division process that has been shown be an independent prognostic marker for tumor malignancy. However, atypical mitosis classification remains challenging due to low prevalence, at times subtle morphological differences from normal mitotic figures, low inter-rater agreement among pathologists, and class imbalance in datasets. Building on the Atypical Mitosis dataset for Breast Cancer (AMi-Br), this study presents a comprehensive benchmark comparing deep learning approaches for automated atypical mitotic figure (AMF) classification, including end-to-end trained deep learning models, foundation models with linear probing, and foundation models fine-tuned with low-rank adaptation (LoRA). For rigorous evaluation, we further introduce two new held-out AMF datasets - AtNorM-Br, a dataset of mitotic figures from the TCGA breast cancer cohort, and AtNorM-MD, a multi-domain dataset of mitotic figures from a subset of the MIDOG++ training set. We found average balanced accuracy values of up to 0.8135, 0.7788, and 0.7723 on the in-domain AMi-Br and the out-of-domain AtNorm-Br and AtNorM-MD datasets, respectively. Our work shows that atypical mitotic figure classification, while being a challenging problem, can be effectively addressed through the use of recent advances in transfer learning and model fine-tuning techniques. We make all code and data used in this paper available in this github repository: https://github.com/DeepMicroscopy/AMi-Br_Benchmark.

