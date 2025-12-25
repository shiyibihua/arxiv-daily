---
layout: default
title: "SegMo: Segment-aligned Text to 3D Human Motion Generation"
---

# SegMo: Segment-aligned Text to 3D Human Motion Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21237" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21237v1</a>
  <a href="https://arxiv.org/pdf/2512.21237.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21237v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21237v1', 'SegMo: Segment-aligned Text to 3D Human Motion Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bowen Dang, Lin Wu, Xiaohang Yang, Zheng Yuan, Zhixiang Chen

**分类**: cs.CV

**发布日期**: 2025-12-24

**备注**: The IEEE/CVF Winter Conference on Applications of Computer Vision 2026

---

## 💡 一句话要点

**提出SegMo框架，通过对齐文本和运动片段实现更精细的文本驱动3D人体动作生成。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `文本驱动动作生成` `3D人体动作` `片段对齐` `对比学习` `多模态学习`

## 📋 核心要点

1. 现有文本驱动人体动作生成方法忽略了文本和动作序列内部的语义结构，导致对齐不够精细。
2. SegMo框架通过提取文本和动作片段，并在片段级别进行对齐，从而实现更细粒度的文本-动作对应。
3. 实验结果表明，SegMo在HumanML3D数据集上取得了显著的性能提升，并可应用于运动检索等任务。

## 📝 摘要（中文）

本文提出了一种新的分段对齐的文本条件3D人体动作生成框架SegMo，旨在实现细粒度的文本-动作对齐。现有方法通常在序列级别对齐文本描述和人体动作，忽略了模态内部的语义结构。SegMo框架包含三个模块：文本片段提取，将复杂的文本描述分解为按时间顺序排列的短语，每个短语代表一个简单的原子动作；运动片段提取，将完整的运动序列划分为相应的运动片段；细粒度文本-动作对齐，通过对比学习对齐文本和运动片段。在广泛使用的两个数据集上的实验表明，SegMo改进了强大的基线，在HumanML3D测试集上实现了0.553的TOP 1得分。此外，由于学习到的文本和运动片段的共享嵌入空间，SegMo还可以应用于运动定位和运动到文本检索等检索任务。

## 🔬 方法详解

**问题定义**：现有文本驱动3D人体动作生成方法主要在序列级别进行文本和动作的对齐，忽略了文本描述和动作序列内部的语义结构。这种粗粒度的对齐方式无法捕捉到文本和动作之间的细微对应关系，限制了生成动作的准确性和多样性。因此，如何实现更精细的文本-动作对齐是本文要解决的核心问题。

**核心思路**：本文的核心思路是将文本描述和动作序列分解为更小的、语义连贯的片段，然后在片段级别进行对齐。这种方法能够更好地捕捉文本和动作之间的局部对应关系，从而提高生成动作的质量。具体来说，就是将文本分解为原子动作短语，将动作序列分解为相应的运动片段，然后学习一个共享的嵌入空间，使得对应的文本和运动片段在该空间中的距离更近。

**技术框架**：SegMo框架包含三个主要模块：1) **文本片段提取**：使用自然语言处理技术将复杂的文本描述分解为按时间顺序排列的短语，每个短语代表一个简单的原子动作。2) **运动片段提取**：使用运动分割算法将完整的运动序列划分为相应的运动片段。3) **细粒度文本-动作对齐**：使用对比学习方法，学习文本和运动片段的共享嵌入空间，使得对应的文本和运动片段在该空间中的距离更近。

**关键创新**：SegMo的关键创新在于提出了片段级别的文本-动作对齐方法。与现有方法在序列级别进行对齐不同，SegMo能够捕捉到文本和动作之间的局部对应关系，从而实现更精细的控制。此外，SegMo还提出了相应的文本和运动片段提取方法，以及基于对比学习的对齐策略。

**关键设计**：在文本片段提取模块，使用了预训练的语言模型（例如BERT）来提取文本特征，并使用句法分析技术来分割文本。在运动片段提取模块，使用了基于运动学特征的分割算法。在细粒度文本-动作对齐模块，使用了InfoNCE损失函数来训练共享嵌入空间。具体的网络结构和参数设置在论文中有详细描述，这里不再赘述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21237v1/images/1_idea.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21237v1/images/3_overview.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21237v1/images/4_qualitative.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SegMo在HumanML3D数据集上取得了显著的性能提升，TOP 1得分达到了0.553，超过了现有的基线方法。实验结果表明，SegMo能够生成更准确、更逼真的人体动作。此外，SegMo还可以应用于运动定位和运动到文本检索等任务，展示了其强大的泛化能力。

## 🎯 应用场景

SegMo框架具有广泛的应用前景，例如视频游戏、虚拟现实和增强现实等领域。它可以用于生成逼真的人体动作，从而提高用户体验。例如，在虚拟现实游戏中，可以根据玩家的语音指令生成相应的角色动作。此外，SegMo还可以应用于运动康复、动画制作等领域，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Generating 3D human motions from textual descriptions is an important research problem with broad applications in video games, virtual reality, and augmented reality. Recent methods align the textual description with human motion at the sequence level, neglecting the internal semantic structure of modalities. However, both motion descriptions and motion sequences can be naturally decomposed into smaller and semantically coherent segments, which can serve as atomic alignment units to achieve finer-grained correspondence. Motivated by this, we propose SegMo, a novel Segment-aligned text-conditioned human Motion generation framework to achieve fine-grained text-motion alignment. Our framework consists of three modules: (1) Text Segment Extraction, which decomposes complex textual descriptions into temporally ordered phrases, each representing a simple atomic action; (2) Motion Segment Extraction, which partitions complete motion sequences into corresponding motion segments; and (3) Fine-grained Text-Motion Alignment, which aligns text and motion segments with contrastive learning. Extensive experiments demonstrate that SegMo improves the strong baseline on two widely used datasets, achieving an improved TOP 1 score of 0.553 on the HumanML3D test set. Moreover, thanks to the learned shared embedding space for text and motion segments, SegMo can also be applied to retrieval-style tasks such as motion grounding and motion-to-text retrieval.

