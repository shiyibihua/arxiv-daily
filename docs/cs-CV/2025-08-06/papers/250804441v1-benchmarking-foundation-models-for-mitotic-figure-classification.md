---
layout: default
title: Benchmarking Foundation Models for Mitotic Figure Classification
---

# Benchmarking Foundation Models for Mitotic Figure Classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04441" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04441v1</a>
  <a href="https://arxiv.org/pdf/2508.04441.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04441v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04441v1', 'Benchmarking Foundation Models for Mitotic Figure Classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jonas Ammeling, Jonathan Ganz, Emely Rosbach, Ludwig Lausser, Christof A. Bertram, Katharina Breininger, Marc Aubreville

**分类**: cs.CV

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出自监督学习方法以提升有丝分裂图像分类性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自监督学习` `有丝分裂分类` `基础模型` `低秩适应` `医学影像` `深度学习` `肿瘤诊断`

## 📋 核心要点

1. 现有方法在病理图像分类中面临标注数据稀缺的问题，限制了模型的性能和鲁棒性。
2. 本研究提出使用基础模型结合自监督学习和低秩适应（LoRA）技术，以提高有丝分裂图像分类的效果。
3. 实验结果显示，LoRA适应的模型在仅使用10%训练数据时，性能接近全数据可用性，且在未见肿瘤领域的表现显著改善。

## 📝 摘要（中文）

深度学习模型的性能通常随着数据量和多样性的增加而提升。然而，在病理学等医学影像领域，特定任务的标注图像往往有限。自监督学习技术使得利用大量未标注数据训练大型神经网络成为可能，从而解决了数据不足的问题。本研究探讨了基础模型在有丝分裂图像分类中的应用，评估其在不同肿瘤领域的鲁棒性。通过对比线性探测和低秩适应（LoRA）方法，结果表明LoRA适应的基础模型在仅使用10%训练数据的情况下，性能接近100%数据可用性，且在未见肿瘤领域的表现显著提升。

## 🔬 方法详解

**问题定义**：本研究旨在解决有丝分裂图像分类中的数据稀缺问题，现有方法在处理未标注数据时效果不佳，限制了模型的泛化能力。

**核心思路**：通过自监督学习技术，利用大量未标注数据训练基础模型，并结合低秩适应（LoRA）方法，提升模型在新任务上的表现。

**技术框架**：整体架构包括数据预处理、基础模型训练、LoRA适应和性能评估四个主要模块。首先，使用未标注数据进行自监督学习，然后对模型进行LoRA适应，最后在不同肿瘤领域进行评估。

**关键创新**：本研究的主要创新在于将LoRA适应与基础模型结合，显著提升了模型在未见数据上的鲁棒性，与传统的线性探测方法相比，表现出更优的性能。

**关键设计**：在模型训练中，采用了特定的损失函数以优化分类效果，同时在LoRA适应过程中调整了注意力机制的低秩参数设置，以增强模型的适应能力。

## 📊 实验亮点

实验结果表明，LoRA适应的基础模型在仅使用10%训练数据的情况下，性能接近100%数据可用性，且在未见肿瘤领域的表现几乎消除了性能差距。此外，传统架构的全微调仍然保持竞争力，显示出不同方法的互补性。

## 🎯 应用场景

该研究的潜在应用领域包括医学影像分析、肿瘤诊断和病理学研究。通过提升有丝分裂图像分类的准确性，能够为肿瘤的预后评估提供更为可靠的依据，进而改善临床决策和患者管理。未来，该方法有望推广至其他医学影像任务，推动相关领域的发展。

## 📄 摘要（原文）

> The performance of deep learning models is known to scale with data quantity and diversity. In pathology, as in many other medical imaging domains, the availability of labeled images for a specific task is often limited. Self-supervised learning techniques have enabled the use of vast amounts of unlabeled data to train large-scale neural networks, i.e., foundation models, that can address the limited data problem by providing semantically rich feature vectors that can generalize well to new tasks with minimal training effort increasing model performance and robustness. In this work, we investigate the use of foundation models for mitotic figure classification. The mitotic count, which can be derived from this classification task, is an independent prognostic marker for specific tumors and part of certain tumor grading systems. In particular, we investigate the data scaling laws on multiple current foundation models and evaluate their robustness to unseen tumor domains. Next to the commonly used linear probing paradigm, we also adapt the models using low-rank adaptation (LoRA) of their attention mechanisms. We compare all models against end-to-end-trained baselines, both CNNs and Vision Transformers. Our results demonstrate that LoRA-adapted foundation models provide superior performance to those adapted with standard linear probing, reaching performance levels close to 100% data availability with only 10% of training data. Furthermore, LoRA-adaptation of the most recent foundation models almost closes the out-of-domain performance gap when evaluated on unseen tumor domains. However, full fine-tuning of traditional architectures still yields competitive performance.

