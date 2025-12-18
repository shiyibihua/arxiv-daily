---
layout: default
title: Data distribution impacts the performance and generalisability of contrastive learning-based foundation models of electrocardiograms
---

# Data distribution impacts the performance and generalisability of contrastive learning-based foundation models of electrocardiograms

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10369" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10369v1</a>
  <a href="https://arxiv.org/pdf/2509.10369.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10369v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10369v1', 'Data distribution impacts the performance and generalisability of contrastive learning-based foundation models of electrocardiograms')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gul Rukh Khattak, Konstantinos Patlatzoglou, Joseph Barker, Libor Pastika, Boroumand Zeidaabadi, Ahmed El-Medany, Hesham Aggour, Yixiu Liang, Antonio H. Ribeiro, Jeffrey Annis, Antonio Luiz Pinho Ribeiro, Junbo Ge, Daniel B. Kramer, Jonathan W. Waks, Evan Brittain, Nicholas Peters, Fu Siong Ng, Arunashis Sau

**分类**: cs.LG, cs.AI, eess.SP, q-bio.TO

**发布日期**: 2025-09-12

**备注**: Currently under review at npj Digital Medicine

---

## 💡 一句话要点

**提出CAPE心电图基础模型，解决对比学习在心电图数据分布偏移下的泛化性问题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对比学习` `心电图` `基础模型` `分布外泛化` `自监督学习`

## 📋 核心要点

1. 对比学习在心电图分析中应用广泛，但其性能受预训练数据分布影响，尤其是在跨人群泛化时面临挑战。
2. 论文提出CAPE模型，通过对比学习在多中心心电图数据上预训练，并引入IDB策略增强模型在不同分布下的鲁棒性。
3. 实验表明，多中心预训练虽提升了分布内精度，但降低了分布外泛化性；IDB策略有效缓解了这一问题，提升了OOD性能。

## 📝 摘要（中文）

对比学习是一种广泛采用的自监督预训练策略，但其对队列组成部分的依赖性仍未被充分探索。本文提出了对比患者增强心电图（CAPE）基础模型，并在来自三大洲（北美洲、南美洲、亚洲）的不同人群的四个队列（n = 5,203,352）上进行预训练。系统地评估了队列的人口统计学、健康状况和人群多样性如何影响下游预测任务的性能，包括来自另一个大洲（欧洲）的两个额外队列。研究发现，下游性能取决于预训练队列的分布属性，包括人口统计学和健康状况。此外，虽然使用多中心、人口统计学上多样化的队列进行预训练可以提高分布内准确性，但它会通过编码队列特定的伪像来降低对比方法的分布外（OOD）泛化能力。为了解决这个问题，本文提出了分布内批次（IDB）策略，该策略在预训练期间保持队列内一致性并增强OOD鲁棒性。这项工作为开发临床上公平且可泛化的基础模型提供了重要的见解。

## 🔬 方法详解

**问题定义**：现有基于对比学习的心电图分析方法，在面对不同来源、不同人群的心电图数据时，泛化能力不足。主要痛点在于，预训练数据分布的偏差会导致模型学习到特定队列的伪影，从而影响其在其他数据集上的表现。

**核心思路**：论文的核心思路是，通过精心设计的预训练策略，使模型能够更好地学习到心电图数据的本质特征，同时减少对特定队列伪影的依赖。具体而言，通过引入In-Distribution Batch (IDB)策略，在预训练过程中保持队列内数据的一致性，从而提高模型的分布外泛化能力。

**技术框架**：整体框架包括数据预处理、对比学习预训练和下游任务微调三个阶段。首先，对来自不同中心的心电图数据进行预处理。然后，利用对比学习方法，在预训练数据集上训练CAPE模型。在预训练过程中，使用IDB策略来增强模型的泛化能力。最后，将预训练好的CAPE模型应用于下游的心电图分类或诊断任务，并进行微调。

**关键创新**：论文的关键创新在于提出了In-Distribution Batch (IDB)策略。该策略的核心思想是，在构建对比学习的batch时，尽量保证batch内的数据来自同一个队列。这样可以使模型更好地学习到队列内数据的一致性，从而减少对队列特定伪影的依赖，提高模型的分布外泛化能力。

**关键设计**：IDB策略的关键设计在于batch的构建方式。传统的对比学习方法通常随机构建batch，而IDB策略则首先将数据按照队列进行分组，然后在每个队列内随机抽取数据，构建batch。此外，论文还采用了标准的对比学习损失函数，如InfoNCE loss。网络结构方面，采用了ResNet等常用的卷积神经网络结构。

## 📊 实验亮点

实验结果表明，使用多中心数据预训练的CAPE模型在分布内数据集上取得了较高的准确率，但分布外泛化能力较差。引入IDB策略后，CAPE模型在分布外数据集上的性能得到了显著提升，表明IDB策略能够有效提高模型的鲁棒性和泛化能力。具体性能提升数据未知。

## 🎯 应用场景

该研究成果可应用于开发更可靠、更公平的心电图分析AI系统。通过提升模型在不同人群和数据分布下的泛化能力，可以减少因数据偏差导致的误诊或漏诊，从而改善医疗服务的公平性和可及性。未来，该方法有望推广到其他医疗影像和生理信号分析领域。

## 📄 摘要（原文）

> Contrastive learning is a widely adopted self-supervised pretraining strategy, yet its dependence on cohort composition remains underexplored. We present Contrasting by Patient Augmented Electrocardiograms (CAPE) foundation model and pretrain on four cohorts (n = 5,203,352), from diverse populations across three continents (North America, South America, Asia). We systematically assess how cohort demographics, health status, and population diversity influence the downstream performance for prediction tasks also including two additional cohorts from another continent (Europe). We find that downstream performance depends on the distributional properties of the pretraining cohort, including demographics and health status. Moreover, while pretraining with a multi-centre, demographically diverse cohort improves in-distribution accuracy, it reduces out-of-distribution (OOD) generalisation of our contrastive approach by encoding cohort-specific artifacts. To address this, we propose the In-Distribution Batch (IDB) strategy, which preserves intra-cohort consistency during pretraining and enhances OOD robustness. This work provides important insights for developing clinically fair and generalisable foundation models.

