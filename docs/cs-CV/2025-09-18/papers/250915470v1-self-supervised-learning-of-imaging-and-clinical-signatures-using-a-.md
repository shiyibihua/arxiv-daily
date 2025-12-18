---
layout: default
title: Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture
---

# Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15470" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15470v1</a>
  <a href="https://arxiv.org/pdf/2509.15470.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15470v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15470v1', 'Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Thomas Z. Li, Aravind R. Krishnan, Lianrui Zuo, John M. Still, Kim L. Sandler, Fabien Maldonado, Thomas A. Lasko, Bennett A. Landman

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-18

---

## 💡 一句话要点

**利用多模态联合嵌入预测架构的自监督学习提升肺结节诊断**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自监督学习` `多模态学习` `联合嵌入` `肺结节诊断` `医学影像` `电子健康记录` `预测模型`

## 📋 核心要点

1. 肺结节诊断的多模态模型受限于标注数据的匮乏，容易在训练集上过拟合。
2. 提出一种基于多模态联合嵌入预测架构（JEPA）的自监督学习方法，利用无标注的CT扫描和电子健康记录进行预训练。
3. 实验表明，该方法在内部数据集上优于其他模型，但在外部数据集上表现不佳，并分析了JEPA的局限性。

## 📝 摘要（中文）

针对肺结节诊断多模态模型面临的标注数据稀缺和过拟合问题，本文提出了一种利用纵向和多模态数据进行自监督学习的方法。该方法使用机构内部的CT扫描和电子健康记录构建无标注数据集，用于联合嵌入预测架构（JEPA）的预训练。在监督微调后，该方法在内部队列中优于未正则化的多模态模型和仅使用影像的模型（AUC分别为0.91、0.88和0.73），但在外部队列中表现较差（AUC分别为0.72和0.75）。本文还构建了一个合成环境，用于分析JEPA可能表现不佳的情况。该研究创新性地利用无标注多模态医学数据来改进预测模型，并展示了其在肺结节诊断中的优势和局限性。

## 🔬 方法详解

**问题定义**：肺结节诊断的多模态模型面临两个主要问题：一是标注数据稀缺，获取成本高昂；二是模型容易在训练数据上过拟合，泛化能力不足。现有方法难以充分利用大规模的无标注多模态数据，导致模型性能受限。

**核心思路**：本文的核心思路是利用自监督学习，从未标注的CT扫描和电子健康记录中学习通用的影像和临床特征表示。通过预训练一个联合嵌入预测架构（JEPA），使模型能够捕捉多模态数据之间的关联性，从而提高模型的泛化能力和对标注数据稀缺的鲁棒性。

**技术框架**：整体框架包含两个主要阶段：预训练阶段和微调阶段。在预训练阶段，使用无标注的CT扫描和电子健康记录训练JEPA模型，学习多模态数据的联合嵌入表示。在微调阶段，使用少量标注数据对预训练的JEPA模型进行微调，使其适应肺结节诊断任务。

**关键创新**：该方法的主要创新在于利用联合嵌入预测架构（JEPA）进行多模态自监督学习。JEPA能够同时学习影像和临床数据的嵌入表示，并预测它们之间的关系，从而捕捉多模态数据之间的互补信息。此外，本文还构建了一个合成环境，用于分析JEPA在不同数据分布下的性能表现。

**关键设计**：JEPA模型包含影像编码器和临床数据编码器，分别用于提取CT扫描和电子健康记录的特征。模型使用对比学习损失函数，鼓励相似样本的嵌入表示靠近，不相似样本的嵌入表示远离。在微调阶段，使用交叉熵损失函数对模型进行优化，使其能够准确预测肺结节的诊断结果。

## 📊 实验亮点

实验结果表明，在内部队列中，经过JEPA预训练和微调的模型AUC达到0.91，优于未正则化的多模态模型（AUC=0.88）和仅使用影像的模型（AUC=0.73）。然而，在外部队列中，JEPA模型的性能略低于仅使用影像的模型（AUC分别为0.72和0.75），表明该方法在跨数据集泛化方面仍有提升空间。

## 🎯 应用场景

该研究成果可应用于肺结节的早期诊断和风险评估，有助于医生更准确地判断结节的良恶性，并制定个性化的治疗方案。此外，该方法还可以推广到其他医学影像和临床数据的多模态分析任务中，例如疾病预测、预后评估等，具有广泛的应用前景和临床价值。

## 📄 摘要（原文）

> The development of multimodal models for pulmonary nodule diagnosis is limited by the scarcity of labeled data and the tendency for these models to overfit on the training distribution. In this work, we leverage self-supervised learning from longitudinal and multimodal archives to address these challenges. We curate an unlabeled set of patients with CT scans and linked electronic health records from our home institution to power joint embedding predictive architecture (JEPA) pretraining. After supervised finetuning, we show that our approach outperforms an unregularized multimodal model and imaging-only model in an internal cohort (ours: 0.91, multimodal: 0.88, imaging-only: 0.73 AUC), but underperforms in an external cohort (ours: 0.72, imaging-only: 0.75 AUC). We develop a synthetic environment that characterizes the context in which JEPA may underperform. This work innovates an approach that leverages unlabeled multimodal medical archives to improve predictive models and demonstrates its advantages and limitations in pulmonary nodule diagnosis.

