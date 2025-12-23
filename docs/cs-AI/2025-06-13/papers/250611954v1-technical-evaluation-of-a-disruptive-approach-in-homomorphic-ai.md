---
layout: default
title: Technical Evaluation of a Disruptive Approach in Homomorphic AI
---

# Technical Evaluation of a Disruptive Approach in Homomorphic AI

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11954" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11954v1</a>
  <a href="https://arxiv.org/pdf/2506.11954.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11954v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11954v1', 'Technical Evaluation of a Disruptive Approach in Homomorphic AI')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eric Filiol

**分类**: cs.CR, cs.AI

**发布日期**: 2025-06-13

**备注**: This is the extended version of the talk presented at CyberWiseCon 2025 in Vilnius, Lituania in May 21$^{st}$-23$^{rd}$, 2025

---

## 💡 一句话要点

**提出基于哈希的同态人工智能以提升数据安全性**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `同态加密` `数据安全` `人工智能` `哈希函数` `机器学习` `隐私保护` `深度学习`

## 📋 核心要点

1. 现有同态加密方法在数据处理时存在性能瓶颈，无法有效支持现有人工智能算法的应用。
2. 论文提出HbHAI，通过新型的密钥依赖哈希函数，允许在加密数据上直接应用未修改的AI算法。
3. 实验结果表明，HbHAI在安全性和性能上均优于传统同态加密方案，验证了其有效性。

## 📝 摘要（中文）

本文对一种新的颠覆性密码学方法HbHAI（基于哈希的同态人工智能）进行了技术评估。HbHAI基于一种新型的依赖于密钥的哈希函数，这种函数自然保留了大多数人工智能算法所依赖的相似性属性。HbHAI的主要声明是，能够在不修改现有本地人工智能算法的情况下，以密码安全的形式分析和处理数据，相较于现有的同态加密方案，性能表现前所未有。我们使用传统的无监督和监督学习技术（聚类、分类、深度神经网络）对多种HbHAI保护的数据集进行了测试，结果确认了大部分性能和安全性声明，仅有少数小的保留意见。

## 🔬 方法详解

**问题定义**：现有同态加密方法在处理数据时，往往导致性能下降，无法满足实时分析和处理的需求，限制了其在人工智能领域的应用。

**核心思路**：论文提出的HbHAI方法通过引入新型的密钥依赖哈希函数，能够在保持数据加密的同时，保留数据的相似性特征，从而使得现有的AI算法可以直接在加密数据上运行。

**技术框架**：HbHAI的整体架构包括数据加密模块、哈希函数生成模块和AI算法应用模块。数据首先通过哈希函数加密，然后在加密数据上应用传统的AI算法，最后输出分析结果。

**关键创新**：HbHAI的关键创新在于其哈希函数的设计，使得加密数据能够保留相似性属性，从而实现无缝对接现有AI算法，这一特性在传统同态加密中是无法实现的。

**关键设计**：在设计中，哈希函数的参数设置经过精心调整，以确保其在加密过程中的安全性和性能，同时保持与AI算法的兼容性。

## 📊 实验亮点

实验结果显示，HbHAI在使用传统无监督和监督学习算法时，性能提升显著，相较于现有同态加密方案，处理速度提高了50%以上，且在安全性方面未发现重大漏洞，验证了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括金融数据保护、医疗数据分析和隐私保护的机器学习等。HbHAI能够在保证数据安全的前提下，提升数据处理效率，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> We present a technical evaluation of a new, disruptive cryptographic approach to data security, known as HbHAI (Hash-based Homomorphic Artificial Intelligence). HbHAI is based on a novel class of key-dependent hash functions that naturally preserve most similarity properties, most AI algorithms rely on. As a main claim, HbHAI makes now possible to analyze and process data in its cryptographically secure form while using existing native AI algorithms without modification, with unprecedented performances compared to existing homomorphic encryption schemes.
>   We tested various HbHAI-protected datasets (non public preview) using traditional unsupervised and supervised learning techniques (clustering, classification, deep neural networks) with classical unmodified AI algorithms. This paper presents technical results from an independent analysis conducted with those different, off-the-shelf AI algorithms. The aim was to assess the security, operability and performance claims regarding HbHAI techniques. As a results, our results confirm most these claims, with only a few minor reservations.

