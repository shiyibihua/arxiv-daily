---
layout: default
title: MOON2.0: Dynamic Modality-balanced Multimodal Representation Learning for E-commerce Product Understanding
---

# MOON2.0: Dynamic Modality-balanced Multimodal Representation Learning for E-commerce Product Understanding

**arXiv**: [2511.12449v1](https://arxiv.org/abs/2511.12449) | [PDF](https://arxiv.org/pdf/2511.12449.pdf)

**作者**: Zhanheng Nie, Chenghan Fu, Daoze Zhang, Junxian Wu, Wanxian Guan, Pengjie Wang, Jian Xu, Bo Zheng

**分类**: cs.CV, cs.AI, cs.IR, cs.LG

**发布日期**: 2025-11-16

**备注**: 11 pages, 7 figures

---

## 💡 一句话要点

**提出MOON2.0以解决电商产品理解中的多模态不平衡问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多模态表示学习` `电商产品理解` `模态平衡` `图文协同增强` `语义对齐` `动态样本过滤` `专家混合模型`

## 📋 核心要点

1. 现有多模态大语言模型在电商产品理解中存在模态不平衡、内在对齐关系利用不足和噪声处理能力有限等挑战。
2. MOON2.0通过模态驱动的专家混合模块、双层对齐方法和图文协同增强策略，动态平衡模态并提升表示学习效果。
3. 实验结果显示，MOON2.0在MBE2.0和多个公共数据集上实现了最先进的零-shot性能，且可视化结果支持了多模态对齐的改善。

## 📝 摘要（中文）

随着电子商务的快速发展，需求日益增长的多模态模型需要理解丰富的视觉和文本产品信息。尽管近期的多模态大语言模型在产品理解方面展现出强大的表示学习能力，但仍面临三大挑战：模态混合训练导致的模态不平衡、未充分利用视觉与文本信息之间的内在对齐关系，以及对电商多模态数据噪声的处理能力有限。为此，我们提出了MOON2.0，一个动态模态平衡的多模态表示学习框架。MOON2.0包括模态驱动的专家混合模块、双层对齐方法以及基于MLLM的图文协同增强策略。实验表明，MOON2.0在多个公共数据集上实现了最先进的零-shot性能。

## 🔬 方法详解

**问题定义**：本论文旨在解决电商产品理解中的多模态不平衡问题，现有方法在模态混合训练中导致模态信息利用不均，且未能有效处理视觉与文本信息的内在对齐关系，此外，对噪声的处理能力也较弱。

**核心思路**：MOON2.0的核心思路是通过动态模态平衡的框架来提升多模态表示学习的效果。通过模态驱动的专家混合模块，适应性地处理输入样本，缓解模态不平衡问题，并通过双层对齐方法更好地利用产品内部的语义对齐特性。

**技术框架**：MOON2.0的整体架构包括三个主要模块：模态驱动的专家混合模块、双层对齐方法和基于MLLM的图文协同增强策略。该框架通过动态样本过滤提升训练数据质量，形成一个闭环的学习过程。

**关键创新**：MOON2.0的关键创新在于模态驱动的专家混合模块和双层对齐方法，这些设计使得模型能够更有效地处理多模态数据的内在关系，显著提升了表示学习的效果。

**关键设计**：在技术细节上，MOON2.0采用了动态样本过滤机制，以提高训练数据的质量，并结合了多模态的协同增强策略，确保视觉和文本信息的有效整合。

## 📊 实验亮点

实验结果表明，MOON2.0在MBE2.0基准上实现了最先进的零-shot性能，相较于现有基线模型，性能提升幅度达到XX%。此外，基于注意力的热图可视化结果进一步验证了MOON2.0在多模态对齐方面的显著改善。

## 🎯 应用场景

该研究的潜在应用领域包括电商产品推荐、智能搜索引擎和用户行为分析等。通过提升多模态理解能力，MOON2.0能够为电商平台提供更精准的产品匹配和推荐服务，进而提升用户体验和转化率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The rapid growth of e-commerce calls for multimodal models that comprehend rich visual and textual product information. Although recent multimodal large language models (MLLMs) for product understanding exhibit strong capability in representation learning for e-commerce, they still face three challenges: (i) the modality imbalance induced by modality mixed training; (ii) underutilization of the intrinsic alignment relationships among visual and textual information within a product; and (iii) limited handling of noise in e-commerce multimodal data. To address these, we propose MOON2.0, a dynamic modality-balanced multimodal representation learning framework for e-commerce product understanding. MOON2.0 comprises: (1) a Modality-driven Mixture-of-Experts (MoE) module that adaptively processes input samples by their modality composition, enabling Multimodal Joint Learning to mitigate the modality imbalance; (2) a Dual-level Alignment method to better leverage semantic alignment properties inside individual products; and (3) an MLLM-based Image-text Co-augmentation strategy that integrates textual enrichment with visual expansion, coupled with Dynamic Sample Filtering to improve training data quality. We further introduce MBE2.0, a co-augmented multimodal representation benchmark for e-commerce representation learning and evaluation. Experiments show that MOON2.0 delivers state-of-the-art zero-shot performance on MBE2.0 and multiple public datasets. Furthermore, attention-based heatmap visualization provides qualitative evidence of improved multimodal alignment of MOON2.0.

