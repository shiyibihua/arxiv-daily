---
layout: default
title: From Essence to Defense: Adaptive Semantic-aware Watermarking for Embedding-as-a-Service Copyright Protection
---

# From Essence to Defense: Adaptive Semantic-aware Watermarking for Embedding-as-a-Service Copyright Protection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16439" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16439v1</a>
  <a href="https://arxiv.org/pdf/2512.16439.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16439v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16439v1', 'From Essence to Defense: Adaptive Semantic-aware Watermarking for Embedding-as-a-Service Copyright Protection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Li, Yubing Ren, Yanan Cao, Yingjie Li, Fang Fang, Xuebin Wang

**分类**: cs.CR, cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出SemMark：一种自适应语义感知水印方法，用于保护Embedding-as-a-Service的版权**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语义水印` `版权保护` `Embedding-as-a-Service` `局部敏感哈希` `自适应权重`

## 📋 核心要点

1. 现有EaaS水印方法忽略了嵌入的语义信息，导致水印的隐蔽性和无害性不足，容易被攻击。
2. SemMark通过局部敏感哈希划分语义空间，并注入语义感知水印，保证水印的不可察觉性和多样性。
3. 实验证明，SemMark在可验证性、多样性、隐蔽性和无害性方面优于现有方法，有效保护EaaS版权。

## 📝 摘要（中文）

Embedding-as-a-Service (EaaS) 凭借大型语言模型在自然语言理解和生成方面的卓越能力，已成为一种成功的商业模式。然而，以往的研究表明，EaaS容易受到模仿攻击。现有的EaaS知识产权保护方法主要基于水印技术，但它们都忽略了嵌入最重要的属性：语义，导致其无害性和隐蔽性有限。为此，我们提出了一种新颖的基于语义的水印范式SemMark，用于EaaS版权保护。SemMark采用局部敏感哈希来划分语义空间，并将语义感知水印注入到特定区域，确保水印信号保持难以察觉和多样性。此外，我们引入了基于局部离群因子的自适应水印权重机制，以保持原始嵌入分布。我们还提出了Detect-Sampling和Dimensionality-Reduction攻击，并构建了四种场景来评估水印方法。在四个流行的NLP数据集上进行的大量实验表明，SemMark在可验证性、多样性、隐蔽性和无害性方面表现出色。

## 🔬 方法详解

**问题定义**：论文旨在解决Embedding-as-a-Service (EaaS) 的版权保护问题。现有的水印方法忽略了嵌入的语义信息，导致水印的隐蔽性不足，容易被攻击者发现和移除，同时可能对嵌入的原始语义造成较大影响，降低EaaS的服务质量。因此，如何设计一种既能有效保护EaaS版权，又能保证水印的隐蔽性和无害性的水印方法是本文要解决的核心问题。

**核心思路**：SemMark的核心思路是利用嵌入的语义信息来设计水印。通过将语义空间划分为多个区域，并在特定区域内注入语义感知水印，可以保证水印的隐蔽性和多样性。同时，采用自适应水印权重机制，根据局部离群因子调整水印强度，以保持原始嵌入分布，减少水印对嵌入语义的影响。

**技术框架**：SemMark主要包含以下几个模块：1) 语义空间划分：使用局部敏感哈希 (LSH) 将嵌入的语义空间划分为多个区域。2) 水印注入：在选定的语义区域内，根据预先设定的规则注入语义感知水印。3) 自适应权重调整：根据局部离群因子 (LOF) 调整水印的权重，以保持原始嵌入分布。4) 水印检测：通过检测嵌入中是否存在特定的水印信号来验证版权。

**关键创新**：SemMark的关键创新在于：1) 提出了语义感知水印的概念，将水印与嵌入的语义信息相结合，提高了水印的隐蔽性和鲁棒性。2) 引入了自适应水印权重机制，根据局部离群因子动态调整水印强度，有效降低了水印对嵌入语义的影响。3) 提出了Detect-Sampling和Dimensionality-Reduction两种新的攻击方式，并验证了SemMark在这些攻击下的鲁棒性。

**关键设计**：在语义空间划分方面，LSH的哈希桶大小是一个关键参数，它决定了语义区域的粒度。在自适应权重调整方面，局部离群因子LOF的计算半径是一个关键参数，它决定了局部邻域的大小。此外，水印注入的强度也需要仔细调整，以在隐蔽性和鲁棒性之间取得平衡。论文中具体参数设置未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16439v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16439v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16439v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SemMark在四个流行的NLP数据集上进行了广泛的实验，结果表明，SemMark在可验证性、多样性、隐蔽性和无害性方面均优于现有方法。具体性能提升数据未知。此外，SemMark还能够有效抵抗Detect-Sampling和Dimensionality-Reduction等新型攻击。

## 🎯 应用场景

SemMark可应用于各种基于Embedding-as-a-Service的商业平台，例如文本相似度计算、信息检索、推荐系统等。通过有效保护EaaS的版权，可以促进相关技术的发展和应用，维护公平竞争的市场环境。未来，该技术可以扩展到其他类型的嵌入，例如图像嵌入、音频嵌入等。

## 📄 摘要（原文）

> Benefiting from the superior capabilities of large language models in natural language understanding and generation, Embeddings-as-a-Service (EaaS) has emerged as a successful commercial paradigm on the web platform. However, prior studies have revealed that EaaS is vulnerable to imitation attacks. Existing methods protect the intellectual property of EaaS through watermarking techniques, but they all ignore the most important properties of embedding: semantics, resulting in limited harmlessness and stealthiness. To this end, we propose SemMark, a novel semantic-based watermarking paradigm for EaaS copyright protection. SemMark employs locality-sensitive hashing to partition the semantic space and inject semantic-aware watermarks into specific regions, ensuring that the watermark signals remain imperceptible and diverse. In addition, we introduce the adaptive watermark weight mechanism based on the local outlier factor to preserve the original embedding distribution. Furthermore, we propose Detect-Sampling and Dimensionality-Reduction attacks and construct four scenarios to evaluate the watermarking method. Extensive experiments are conducted on four popular NLP datasets, and SemMark achieves superior verifiability, diversity, stealthiness, and harmlessness.

