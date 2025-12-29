---
layout: default
title: "See Less, See Right: Bi-directional Perceptual Shaping For Multimodal Reasoning"
---

# See Less, See Right: Bi-directional Perceptual Shaping For Multimodal Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.22120" class="toolbar-btn" target="_blank">📄 arXiv: 2512.22120v1</a>
  <a href="https://arxiv.org/pdf/2512.22120.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.22120v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.22120v1', 'See Less, See Right: Bi-directional Perceptual Shaping For Multimodal Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuoshuo Zhang, Yizhen Zhang, Jingjing Fu, Lei Song, Jiang Bian, Yujiu Yang, Rui Wang

**分类**: cs.CV

**发布日期**: 2025-12-26

---

## 💡 一句话要点

**提出双向感知塑形方法以提升多模态推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `多模态推理` `双向感知塑形` `KL一致性` `细粒度视觉证据` `跨领域泛化` `智能问答` `图像理解`

## 📋 核心要点

1. 现有的视觉-语言模型在推理过程中未能充分利用细粒度的视觉证据，导致泛化能力不足和推理时间成本高。
2. 本文提出双向感知塑形（BiPS），通过引入KL一致性和KL分离约束，增强模型对视觉信息的依赖，改善推理效果。
3. 在八个基准测试中，BiPS平均提升了Qwen2.5-VL-7B模型8.2%的性能，且在未见数据集上表现出色，显示出良好的泛化能力。

## 📝 摘要（中文）

大型视觉-语言模型（VLMs）通常依赖中间视觉线索，但现有方法忽视了细粒度的视觉证据，且在不同领域的泛化能力较差，推理时间成本高。本文提出了双向感知塑形（BiPS），通过将问题条件下的遮蔽视图转化为双向的关注信号，来塑造训练过程中的感知。BiPS首先在原始图像与保留证据的视图之间施加KL一致性约束，以鼓励对支持像素的粗略但完整覆盖。然后，它在原始图像与证据消融视图之间施加KL分离约束，以防止仅依赖文本的快捷回答，并强化对细粒度视觉信息的依赖。实验表明，BiPS在八个基准测试中平均提升了Qwen2.5-VL-7B模型8.2%的性能，并在未见数据集和图像类型上展现出强大的跨领域泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉-语言模型在推理过程中对细粒度视觉证据的忽视，导致的泛化能力不足和高推理时间成本的问题。

**核心思路**：论文提出的双向感知塑形（BiPS）方法，通过对问题条件下的遮蔽视图进行双向信号塑形，鼓励模型在训练中更好地依赖视觉信息。

**技术框架**：BiPS的整体架构包括两个主要阶段：首先施加KL一致性约束以保持问题相关区域的完整覆盖，其次施加KL分离约束以消除关键像素，防止文本快捷回答。

**关键创新**：BiPS的核心创新在于引入了双向的关注信号塑形机制，通过KL一致性和KL分离约束，显著提升了模型对视觉信息的依赖程度，与传统方法相比，能够更好地处理细粒度视觉证据。

**关键设计**：在设计中，采用了KL一致性和KL分离作为损失函数，确保模型在训练过程中既能覆盖支持像素，又能避免仅依赖文本信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22120v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22120v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22120v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果显示，BiPS在八个基准测试中平均提升了Qwen2.5-VL-7B模型8.2%的性能，尤其在未见数据集和不同图像类型上展现出强大的跨领域泛化能力，显著优于传统方法。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、图像理解和多模态交互等。通过提升模型对细粒度视觉信息的依赖，BiPS可以在更复杂的多模态任务中表现出更高的准确性和鲁棒性，未来可能推动相关领域的技术进步。

## 📄 摘要（原文）

> Large vision-language models (VLMs) often benefit from intermediate visual cues, either injected via external tools or generated as latent visual tokens during reasoning, but these mechanisms still overlook fine-grained visual evidence (e.g., polylines in charts), generalize poorly across domains, and incur high inference-time cost. In this paper, we propose Bi-directional Perceptual Shaping (BiPS), which transforms question-conditioned masked views into bidirectional where-to-look signals that shape perception during training. BiPS first applies a KL-consistency constraint between the original image and an evidence-preserving view that keeps only question-relevant regions, encouraging coarse but complete coverage of supporting pixels. It then applies a KL-separation constraint between the original and an evidence-ablated view where critical pixels are masked so the image no longer supports the original answer, discouraging text-only shortcuts (i.e., answering from text alone) and enforcing fine-grained visual reliance. Across eight benchmarks, BiPS boosts Qwen2.5-VL-7B by 8.2% on average and shows strong out-of-domain generalization to unseen datasets and image types.

