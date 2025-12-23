---
layout: default
title: Hierarchical Text Classification Using Contrastive Learning Informed Path Guided Hierarchy
---

# Hierarchical Text Classification Using Contrastive Learning Informed Path Guided Hierarchy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04381" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04381v1</a>
  <a href="https://arxiv.org/pdf/2506.04381.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04381v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04381v1', 'Hierarchical Text Classification Using Contrastive Learning Informed Path Guided Hierarchy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Neeraj Agrawal, Saurabh Kumar, Priyanka Bhatt, Tanishka Agarwal

**分类**: cs.CL, cs.LG

**发布日期**: 2025-06-04

**备注**: arXiv admin note: text overlap with arXiv:2203.03825 by other authors

**期刊**: ECAI 2023, pp. 19-26. IOS Press, 2023

**DOI**: [10.3233/FAIA230249](https://doi.org/10.3233/FAIA230249)

---

## 💡 一句话要点

**提出基于对比学习的路径引导层次文本分类方法以提升性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `层次文本分类` `对比学习` `路径引导` `文本表示` `机器学习`

## 📋 核心要点

1. 现有的层次文本分类方法在处理复杂标签层次时存在不足，难以充分利用标签之间的关系。
2. 本文提出的HTC-CLIP方法结合了对比学习和路径引导的层次结构，旨在学习更有效的文本表示。
3. 实验结果显示，HTC-CLIP在两个基准数据集上相较于现有模型提升了0.99%至2.37%的Macro F1分数，验证了其有效性。

## 📝 摘要（中文）

层次文本分类（HTC）近年来受到关注，因其能够处理复杂的标签层次结构，广泛应用于电子商务、客户服务和医疗等领域。现有的HTC模型通常分别编码标签层次或在文本编码中引导标签层次结构，二者各有优缺点。本文提出了一种基于对比学习的路径引导层次文本分类方法（HTC-CLIP），通过对比学习学习层次感知的文本表示和文本引导的层次表示。在HTC-CLIP的训练过程中，我们学习了两组不同的类别概率分布，并在推理时结合这两种表示的输出，以获得最佳效果。实验结果表明，HTC-CLIP在两个公共基准数据集上的Macro F1分数比现有的最先进模型提高了0.99%至2.37%。

## 🔬 方法详解

**问题定义**：本文旨在解决层次文本分类中现有方法对标签层次关系利用不足的问题。现有模型通常分别处理文本和标签层次，未能有效结合二者的信息。

**核心思路**：HTC-CLIP通过对比学习的方式，学习层次感知的文本表示和文本引导的层次表示，旨在将两种表示的优势结合起来，从而提升分类性能。

**技术框架**：HTC-CLIP的整体架构包括文本编码模块和层次引导模块。在训练过程中，模型同时学习两组类别概率分布，推理时结合这两组输出以获得更优结果。

**关键创新**：HTC-CLIP的主要创新在于将对比学习与层次引导相结合，形成了一种新的层次文本分类框架，能够更全面地捕捉标签层次结构的信息。

**关键设计**：在模型设计中，采用了特定的损失函数以优化对比学习过程，并在网络结构中引入了路径引导机制，以增强模型对层次信息的理解。具体参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

HTC-CLIP在两个公共基准数据集上的实验结果显示，相较于现有最先进的模型，Macro F1分数提升了0.99%至2.37%。这一提升表明，结合对比学习和路径引导的层次结构能够显著增强模型的分类性能，验证了方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括电子商务中的商品分类、客户服务中的问题分类以及医疗领域的疾病分类等。通过提升层次文本分类的准确性，HTC-CLIP能够帮助企业和机构更有效地处理和分析大量文本数据，提升服务质量和决策效率。未来，该方法还可以扩展到其他需要处理复杂标签层次的领域，如社交媒体分析和内容推荐系统。

## 📄 摘要（原文）

> Hierarchical Text Classification (HTC) has recently gained traction given the ability to handle complex label hierarchy. This has found applications in domains like E- commerce, customer care and medicine industry among other real-world applications. Existing HTC models either encode label hierarchy separately and mix it with text encoding or guide the label hierarchy structure in the text encoder. Both approaches capture different characteristics of label hierarchy and are complementary to each other. In this paper, we propose a Hierarchical Text Classification using Contrastive Learning Informed Path guided hierarchy (HTC-CLIP), which learns hierarchy-aware text representation and text informed path guided hierarchy representation using contrastive learning. During the training of HTC-CLIP, we learn two different sets of class probabilities distributions and during inference, we use the pooled output of both probabilities for each class to get the best of both representations. Our results show that the two previous approaches can be effectively combined into one architecture to achieve improved performance. Tests on two public benchmark datasets showed an improvement of 0.99 - 2.37% in Macro F1 score using HTC-CLIP over the existing state-of-the-art models.

