---
layout: default
title: Optimizing Product Deduplication in E-Commerce with Multimodal Embeddings
---

# Optimizing Product Deduplication in E-Commerce with Multimodal Embeddings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15858" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15858v2</a>
  <a href="https://arxiv.org/pdf/2509.15858.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15858v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15858v2', 'Optimizing Product Deduplication in E-Commerce with Multimodal Embeddings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aysenur Kulunk, Berk Taskin, M. Furkan Eseoglu, H. Bahadir Sahin

**分类**: cs.IR, cs.LG

**发布日期**: 2025-09-19 (更新: 2025-12-01)

**备注**: 8 pages, accepted to 2025 IEEE International Conference on Big Data, Industrial and Goverment Track

---

## 💡 一句话要点

**提出一种基于多模态嵌入的电商商品去重方法，提升大规模商品目录下的去重精度。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `商品去重` `多模态嵌入` `BERT` `Masked Autoencoders` `向量数据库` `电商平台` `相似性搜索`

## 📋 核心要点

1. 传统关键词搜索方法依赖精确文本匹配，难以识别语义相似的重复商品，导致去重效果不佳。
2. 利用BERT和Masked Autoencoders提取文本和图像特征，结合降维技术和新型决策模型，实现高效去重。
3. 实验表明，该方法在超过2亿件商品的目录中实现了0.90的宏平均F1分数，优于现有方案。

## 📝 摘要（中文）

本文提出了一种专为电商领域设计、可扩展的多模态商品去重方法，旨在解决大规模电商平台中重复商品列表导致的用户困惑和运营效率低下问题。该方法结合了基于BERT架构的领域特定文本模型和用于图像表示的Masked Autoencoders，并通过降维技术生成紧凑的128维嵌入向量，同时开发了一种利用文本和图像向量的新型决策模型。通过将这些特征提取机制与优化的向量数据库Milvus集成，该系统能够高效且高精度地在超过2亿件商品的庞大商品目录中进行相似性搜索，且仅消耗100GB的系统RAM。实验结果表明，该匹配系统实现了0.90的宏平均F1分数，优于第三方解决方案的0.83。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模电商平台中商品重复 listing 的问题。现有方法，特别是基于关键词的搜索，无法有效识别语义相似但文本描述不同的重复商品，导致用户体验下降和运营成本增加。现有方法的痛点在于对商品标题的语义理解不足，以及在大规模数据集上的计算效率问题。

**核心思路**：论文的核心思路是利用多模态信息（文本和图像）来更准确地识别重复商品。通过深度学习模型学习商品标题和图像的嵌入表示，并结合向量数据库实现高效的相似性搜索。这种方法能够捕捉商品之间的语义相似性，克服了传统关键词匹配的局限性。

**技术框架**：整体框架包含以下几个主要模块：1) 文本特征提取：使用基于BERT架构的领域特定文本模型提取商品标题的嵌入向量。2) 图像特征提取：使用Masked Autoencoders提取商品图像的嵌入向量。3) 降维：使用降维技术将文本和图像嵌入向量压缩到128维，以减少计算量和存储空间。4) 决策模型：开发一种新型决策模型，结合文本和图像向量来判断商品是否重复。5) 向量数据库：使用Milvus向量数据库存储商品嵌入向量，并实现高效的相似性搜索。

**关键创新**：论文的关键创新点在于：1) 结合文本和图像信息进行商品去重，充分利用了商品的多模态特征。2) 针对电商领域定制了BERT模型，使其更适合处理商品标题等文本数据。3) 开发了一种新型决策模型，能够有效融合文本和图像向量。4) 将深度学习模型与向量数据库相结合，实现了大规模商品目录下的高效去重。

**关键设计**：文本模型采用BERT架构，并在电商商品标题数据集上进行预训练和微调。图像模型采用Masked Autoencoders，通过重建被遮盖的图像区域来学习图像特征。降维技术采用PCA或其他线性/非线性降维方法，目标是保留尽可能多的信息，同时降低向量维度。决策模型可以采用多种分类器，如逻辑回归、支持向量机或神经网络，输入为文本和图像嵌入向量，输出为商品是否重复的概率。

## 📊 实验亮点

实验结果表明，该方法在商品去重任务中取得了显著的性能提升，宏平均F1分数达到0.90，优于第三方解决方案的0.83。该系统能够在超过2亿件商品的庞大商品目录中进行高效的相似性搜索，且仅消耗100GB的系统RAM，证明了其在大规模电商环境中的实用性。

## 🎯 应用场景

该研究成果可广泛应用于各类电商平台，用于自动检测和删除重复商品列表，提升用户体验，降低运营成本。此外，该方法也可扩展到其他领域，如社交媒体内容去重、图像检索等，具有重要的实际应用价值和商业潜力。未来，可以进一步研究如何利用用户行为数据来提升去重精度。

## 📄 摘要（原文）

> In large scale e-commerce marketplaces, duplicate product listings frequently cause consumer confusion and operational inefficiencies, degrading trust on the platform and increasing costs. Traditional keyword-based search methodologies falter in accurately identifying duplicates due to their reliance on exact textual matches, neglecting semantic similarities inherent in product titles. To address these challenges, we introduce a scalable, multimodal product deduplication designed specifically for the e-commerce domain. Our approach employs a domain-specific text model grounded in BERT architecture in conjunction with MaskedAutoEncoders for image representations. Both of these architectures are augmented with dimensionality reduction techniques to produce compact 128-dimensional embeddings without significant information loss. Complementing this, we also developed a novel decider model that leverages both text and image vectors. By integrating these feature extraction mechanisms with Milvus, an optimized vector database, our system can facilitate efficient and high-precision similarity searches across extensive product catalogs exceeding 200 million items with just 100GB of system RAM consumption. Empirical evaluations demonstrate that our matching system achieves a macro-average F1 score of 0.90, outperforming third-party solutions which attain an F1 score of 0.83. Our findings show the potential of combining domain-specific adaptations with state-of-the-art machine learning techniques to mitigate duplicate listings in large-scale e-commerce environments.

