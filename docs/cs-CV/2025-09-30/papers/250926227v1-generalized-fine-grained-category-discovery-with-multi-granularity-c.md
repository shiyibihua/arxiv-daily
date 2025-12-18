---
layout: default
title: Generalized Fine-Grained Category Discovery with Multi-Granularity Conceptual Experts
---

# Generalized Fine-Grained Category Discovery with Multi-Granularity Conceptual Experts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26227" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26227v1</a>
  <a href="https://arxiv.org/pdf/2509.26227.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26227v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26227v1', 'Generalized Fine-Grained Category Discovery with Multi-Granularity Conceptual Experts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haiyang Zheng, Nan Pu, Wenjing Li, Nicu Sebe, Zhun Zhong

**分类**: cs.CV

**发布日期**: 2025-09-30

**🔗 代码/项目**: [GITHUB](https://github.com/HaiyangZheng/MGCE)

---

## 💡 一句话要点

**提出多粒度概念专家网络MGCE，解决广义细粒度类别发现问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `广义类别发现` `细粒度识别` `多粒度学习` `对比学习` `概念挖掘`

## 📋 核心要点

1. 现有广义类别发现方法难以有效利用视觉数据的多粒度概念信息，限制了表征学习的质量。
2. MGCE框架通过动态概念对比学习和多粒度专家协同学习，自适应地挖掘视觉概念并整合多粒度知识。
3. 实验表明，MGCE在多个细粒度数据集上取得了SOTA结果，尤其是在新类别识别方面，无需预知类别数量。

## 📝 摘要（中文）

广义类别发现(GCD)是一个开放世界问题，它利用部分标记类别中的知识来聚类未标记数据。一个关键挑战是未标记数据可能包含已知和新类别。现有方法存在两个主要限制。首先，它们未能利用视觉数据中的多粒度概念信息，这限制了表征质量。其次，大多数方法假设在训练期间已知未标记类别的数量，这在实际场景中是不切实际的。为了解决这些问题，我们提出了一种多粒度概念专家(MGCE)框架，该框架自适应地挖掘视觉概念并整合多粒度知识，以实现准确的类别发现。MGCE由两个模块组成：(1)动态概念对比学习(DCCL)，它在概念挖掘和双层表示学习之间交替，以联合优化特征学习和类别发现；(2)多粒度专家协同学习(MECL)，它通过引入不同粒度的额外专家，并采用概念对齐矩阵进行有效的跨专家协作，从而扩展了单专家范式。重要的是，MGCE可以自动估计未标记数据中的类别数量，使其适用于实际的开放世界设置。在九个细粒度视觉识别基准上的大量实验表明，MGCE取得了最先进的结果，尤其是在新类别的准确性方面。值得注意的是，即使在没有类别数量的先验知识的情况下，MGCE的性能也优于需要知道确切类别数量的参数化方法，平均提高了3.6%。代码可在https://github.com/HaiyangZheng/MGCE获得。

## 🔬 方法详解

**问题定义**：论文旨在解决广义细粒度类别发现（Generalized Fine-Grained Category Discovery, GCD）问题。该问题的主要挑战在于，如何利用部分标记的数据，对包含已知类别和未知类别的数据进行聚类。现有方法的痛点在于无法充分利用多粒度概念信息，并且通常需要预先知道未知类别的数量，这在实际应用中是不现实的。

**核心思路**：论文的核心思路是构建一个多粒度概念专家网络（Multi-Granularity Conceptual Experts, MGCE），通过自适应地挖掘视觉概念，并整合多粒度知识，从而实现更准确的类别发现。这种设计允许模型在不同抽象层次上理解图像，并更好地处理细粒度类别之间的差异。

**技术框架**：MGCE框架主要包含两个模块：动态概念对比学习（Dynamic Conceptual Contrastive Learning, DCCL）和多粒度专家协同学习（Multi-Granularity Experts Collaborative Learning, MECL）。DCCL模块通过交替进行概念挖掘和双层表示学习，联合优化特征学习和类别发现。MECL模块则引入了多个不同粒度的专家，并通过概念对齐矩阵实现跨专家协作。整个框架能够自动估计未标记数据中的类别数量。

**关键创新**：MGCE的关键创新在于：1) 提出了动态概念对比学习，能够自适应地挖掘视觉概念，并将其融入到特征学习中；2) 引入了多粒度专家协同学习，通过不同粒度的专家共同决策，提高了类别发现的准确性；3) 能够自动估计未标记数据中的类别数量，无需预先指定。

**关键设计**：DCCL模块使用对比学习损失来学习概念表示，并使用动态更新机制来调整概念的权重。MECL模块使用概念对齐矩阵来衡量不同专家之间的概念相似度，并使用加权融合策略来整合不同专家的预测结果。损失函数包括对比损失、聚类损失和对齐损失，以共同优化特征表示、类别划分和专家协作。

## 📊 实验亮点

MGCE在九个细粒度视觉识别基准上取得了SOTA结果，尤其是在新类别准确率方面。即使在没有类别数量先验知识的情况下，MGCE的性能也优于需要知道确切类别数量的参数化方法，平均提高了3.6%。这些结果表明，MGCE在广义细粒度类别发现任务中具有显著的优势。

## 🎯 应用场景

该研究成果可应用于智能相册管理、细粒度图像搜索、生物多样性监测、商品识别等领域。通过自动发现和识别图像中的细粒度类别，可以提升用户体验和工作效率，具有重要的实际应用价值和商业潜力。未来，该方法可以扩展到视频分析、医学图像诊断等更广泛的应用场景。

## 📄 摘要（原文）

> Generalized Category Discovery (GCD) is an open-world problem that clusters unlabeled data by leveraging knowledge from partially labeled categories. A key challenge is that unlabeled data may contain both known and novel categories. Existing approaches suffer from two main limitations. First, they fail to exploit multi-granularity conceptual information in visual data, which limits representation quality. Second, most assume that the number of unlabeled categories is known during training, which is impractical in real-world scenarios. To address these issues, we propose a Multi-Granularity Conceptual Experts (MGCE) framework that adaptively mines visual concepts and integrates multi-granularity knowledge for accurate category discovery. MGCE consists of two modules: (1) Dynamic Conceptual Contrastive Learning (DCCL), which alternates between concept mining and dual-level representation learning to jointly optimize feature learning and category discovery; and (2) Multi-Granularity Experts Collaborative Learning (MECL), which extends the single-expert paradigm by introducing additional experts at different granularities and by employing a concept alignment matrix for effective cross-expert collaboration. Importantly, MGCE can automatically estimate the number of categories in unlabeled data, making it suitable for practical open-world settings. Extensive experiments on nine fine-grained visual recognition benchmarks demonstrate that MGCE achieves state-of-the-art results, particularly in novel-class accuracy. Notably, even without prior knowledge of category numbers, MGCE outperforms parametric approaches that require knowing the exact number of categories, with an average improvement of 3.6\%. Code is available at https://github.com/HaiyangZheng/MGCE.

