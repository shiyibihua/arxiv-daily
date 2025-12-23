---
layout: default
title: Brain-Grounded Axes for Reading and Steering LLM States
---

# Brain-Grounded Axes for Reading and Steering LLM States

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19399" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19399v1</a>
  <a href="https://arxiv.org/pdf/2512.19399.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19399v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19399v1', 'Brain-Grounded Axes for Reading and Steering LLM States')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sandro Andric

**分类**: cs.LG

**发布日期**: 2025-12-22

**备注**: 10 pages, 4 figures. Code: https://github.com/sandroandric/Brain-Grounded-Axes-for-Reading-and-Steering-LLM-States

---

## 💡 一句话要点

**提出基于人脑活动的LLM状态解读与操控方法，实现神经生理学层面可控性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型可解释性` `脑机接口` `神经生理学` `脑磁图` `独立成分分析` `模型操控` `认知神经科学`

## 📋 核心要点

1. 现有LLM可解释性方法依赖文本监督，缺乏外部依据，难以保证结果的可靠性和泛化性。
2. 利用人脑活动作为LLM状态的坐标系，通过MEG数据构建脑活动图谱，提取潜在轴，实现神经生理学层面的解读与操控。
3. 实验表明，该方法在多个LLM中发现了鲁棒的词汇轴和功能/内容轴，并验证了其有效性和一致性。

## 📝 摘要（中文）

本文提出了一种新的LLM可解释性方法，该方法不依赖于文本监督，而是利用人脑活动作为坐标系来读取和操控LLM的状态。具体而言，研究者使用SMN4Lang MEG数据集构建了一个词级别的脑活动图谱（基于相位锁定值PLV），并通过ICA提取潜在轴。通过独立的词汇表和NER标签验证这些轴（使用POS/log-frequency作为健全性检查），然后训练轻量级适配器，将LLM的隐藏状态映射到这些脑轴，而无需微调LLM。沿着这些脑源方向进行操控，在TinyLlama的中间层产生了一个鲁棒的词汇（频率相关）轴。脑轴与文本探针的对比显示，脑轴具有更大的log-frequency偏移和更低的困惑度。一个功能/内容轴（轴13）在TinyLlama、Qwen2-0.5B和GPT-2中表现出一致的操控效果。探索性的fMRI锚定表明嵌入变化和log frequency可能存在潜在的对齐，但效果对血流动力学建模假设敏感。这些结果支持一种新的接口：神经生理学基础的轴为LLM行为提供了可解释和可控的句柄。

## 🔬 方法详解

**问题定义**：现有的大语言模型（LLM）可解释性方法主要依赖于文本监督信号，例如词汇表、NER标签等。这种方法的局限性在于，文本本身可能存在偏差或噪声，导致解释结果缺乏外部的客观依据。此外，基于文本的解释难以直接与人类认知过程建立联系，限制了对LLM内部机制的深入理解。因此，需要一种更具外部依据且与人类认知相关的LLM可解释性方法。

**核心思路**：本文的核心思路是将人脑活动作为LLM状态的坐标系，通过分析LLM隐藏层状态与人脑活动之间的关系，来理解和操控LLM的行为。具体而言，作者利用脑磁图（MEG）数据构建词级别的脑活动图谱，并提取潜在的脑活动轴。然后，将LLM的隐藏状态映射到这些脑轴上，从而实现对LLM行为的神经生理学层面的解读和操控。这种方法的优势在于，它将LLM的内部状态与人类的认知过程联系起来，提供了一种更具客观性和可解释性的视角。

**技术框架**：该方法主要包含以下几个阶段：
1. **构建脑活动图谱**：使用SMN4Lang MEG数据集，计算词级别的相位锁定值（PLV），构建脑活动图谱。
2. **提取脑活动轴**：使用独立成分分析（ICA）从脑活动图谱中提取潜在的脑活动轴。
3. **验证脑活动轴**：使用独立的词汇表和NER标签验证脑活动轴的有效性，并使用POS/log-frequency作为健全性检查。
4. **训练适配器**：训练轻量级适配器，将LLM的隐藏状态映射到脑活动轴，无需微调LLM。
5. **操控LLM状态**：沿着脑活动轴的方向操控LLM的状态，观察LLM行为的变化。
6. **fMRI锚定（探索性）**：使用fMRI数据探索嵌入变化和log frequency与脑活动之间的潜在对齐关系。

**关键创新**：该方法最重要的技术创新点在于，它将人脑活动作为LLM状态的坐标系，提供了一种全新的LLM可解释性视角。与传统的基于文本监督的方法相比，该方法具有以下优势：
1. **外部依据**：利用人脑活动作为外部依据，避免了文本偏差或噪声的影响。
2. **认知相关**：将LLM的内部状态与人类的认知过程联系起来，有助于深入理解LLM的内部机制。
3. **可操控性**：通过操控脑活动轴，可以实现对LLM行为的神经生理学层面的操控。

**关键设计**：
1. **MEG数据处理**：使用SMN4Lang MEG数据集，计算词级别的相位锁定值（PLV），以表征脑活动。
2. **ICA参数设置**：使用独立成分分析（ICA）从脑活动图谱中提取潜在的脑活动轴，需要选择合适的ICA算法和参数。
3. **适配器网络结构**：训练轻量级适配器，将LLM的隐藏状态映射到脑活动轴，需要设计合适的网络结构和损失函数。
4. **操控策略**：沿着脑活动轴的方向操控LLM的状态，需要选择合适的操控策略和幅度。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19399v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19399v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19399v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在TinyLlama、Qwen2-0.5B和GPT-2等多个LLM中发现了鲁棒的词汇轴和功能/内容轴。脑轴与文本探针的对比显示，脑轴具有更大的log-frequency偏移和更低的困惑度。重建脑活动图谱时，即使移除GPT嵌入变化特征或使用word2vec嵌入，轴结构依然稳定（\|r\|=0.64-0.95）。

## 🎯 应用场景

该研究成果可应用于提升LLM的可解释性和可控性，例如，通过操控LLM的脑活动轴，可以控制LLM生成特定情感或风格的文本。此外，该方法还可以用于诊断LLM的潜在问题，例如，通过分析LLM的脑活动轴，可以发现LLM是否存在认知偏差或逻辑错误。未来，该研究有望促进人机协作，实现更自然、更智能的人机交互。

## 📄 摘要（原文）

> Interpretability methods for large language models (LLMs) typically derive directions from textual supervision, which can lack external grounding. We propose using human brain activity not as a training signal but as a coordinate system for reading and steering LLM states. Using the SMN4Lang MEG dataset, we construct a word-level brain atlas of phase-locking value (PLV) patterns and extract latent axes via ICA. We validate axes with independent lexica and NER-based labels (POS/log-frequency used as sanity checks), then train lightweight adapters that map LLM hidden states to these brain axes without fine-tuning the LLM. Steering along the resulting brain-derived directions yields a robust lexical (frequency-linked) axis in a mid TinyLlama layer, surviving perplexity-matched controls, and a brain-vs-text probe comparison shows larger log-frequency shifts (relative to the text probe) with lower perplexity for the brain axis. A function/content axis (axis 13) shows consistent steering in TinyLlama, Qwen2-0.5B, and GPT-2, with PPL-matched text-level corroboration. Layer-4 effects in TinyLlama are large but inconsistent, so we treat them as secondary (Appendix). Axis structure is stable when the atlas is rebuilt without GPT embedding-change features or with word2vec embeddings (\|r\|=0.64-0.95 across matched axes), reducing circularity concerns. Exploratory fMRI anchoring suggests potential alignment for embedding change and log frequency, but effects are sensitive to hemodynamic modeling assumptions and are treated as population-level evidence only. These results support a new interface: neurophysiology-grounded axes provide interpretable and controllable handles for LLM behavior.

