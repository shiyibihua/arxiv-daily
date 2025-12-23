---
layout: default
title: Multimodal Modeling of CRISPR-Cas12 Activity Using Foundation Models and Chromatin Accessibility Data
---

# Multimodal Modeling of CRISPR-Cas12 Activity Using Foundation Models and Chromatin Accessibility Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11182" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11182v1</a>
  <a href="https://arxiv.org/pdf/2506.11182.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11182v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11182v1', 'Multimodal Modeling of CRISPR-Cas12 Activity Using Foundation Models and Chromatin Accessibility Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Azim Dehghani Amirabad, Yanfei Zhang, Artem Moskalev, Sowmya Rajesh, Tommaso Mansi, Shuwei Li, Mangal Prakash, Rui Liao

**分类**: q-bio.GN, cs.AI

**发布日期**: 2025-06-12

**备注**: This manuscript has been accepted by ICML workshop 2025

---

## 💡 一句话要点

**利用基础模型和染色质可及性数据提升CRISPR-Cas12 gRNA活性预测**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `CRISPR-Cas12` `gRNA活性预测` `基础模型` `染色质可及性` `多模态学习` `生物信息学`

## 📋 核心要点

1. 现有方法在gRNA活性预测中面临数据不足和PAM序列变异等挑战，影响了CRISPR-Cas12基因组编辑的有效性。
2. 本文提出利用预训练的生物基础模型和染色质可及性数据，改善gRNA活性估计，展示了新方法的有效性。
3. 实验结果表明，使用轻量回归器结合RNA基础模型嵌入，性能显著优于传统基线，且整合染色质数据进一步提升了预测效果。

## 📝 摘要（中文）

预测引导RNA（gRNA）活性对于有效的CRISPR-Cas12基因组编辑至关重要，但由于数据有限、PAM序列变异及对大规模训练的依赖，仍然面临挑战。本文研究了是否可以利用预训练的生物基础模型来改善gRNA活性估计，即使没有领域特定的预训练。通过将现有RNA基础模型的嵌入作为轻量回归器的输入，我们展示了相较于传统基线的显著提升。此外，我们还整合了染色质可及性数据，以捕捉调控背景，进一步提高了性能。研究结果突显了预训练基础模型和染色质可及性数据在gRNA活性预测中的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决gRNA活性预测中的数据不足和PAM序列变异带来的挑战。现有方法依赖于大规模训练，难以有效估计gRNA活性。

**核心思路**：论文提出利用预训练的生物基础模型，尤其是RNA基础模型的嵌入，作为输入来构建轻量回归器，从而提高gRNA活性预测的准确性。

**技术框架**：整体架构包括两个主要模块：首先是从RNA基础模型中提取嵌入，然后将这些嵌入输入到轻量回归器中进行gRNA活性预测。同时，整合染色质可及性数据以捕捉调控信息。

**关键创新**：最重要的创新在于利用预训练的基础模型进行gRNA活性预测，而不需要领域特定的预训练。这种方法在数据稀缺的情况下仍能显著提升预测性能。

**关键设计**：在模型设计中，选择了轻量回归器作为主要预测工具，并通过优化损失函数和调整网络结构，确保模型在处理生物数据时的有效性和准确性。具体参数设置和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果显示，利用预训练的RNA基础模型和染色质可及性数据，gRNA活性预测的性能显著提升，较传统基线提高了XX%（具体数据待补充），验证了新方法的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括基因组编辑、基因治疗和合成生物学等。通过提高gRNA活性预测的准确性，能够有效指导CRISPR-Cas12技术的应用，推动基因组编辑技术的进步，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Predicting guide RNA (gRNA) activity is critical for effective CRISPR-Cas12 genome editing but remains challenging due to limited data, variation across protospacer adjacent motifs (PAMs-short sequence requirements for Cas binding), and reliance on large-scale training. We investigate whether pre-trained biological foundation model originally trained on transcriptomic data can improve gRNA activity estimation even without domain-specific pre-training. Using embeddings from existing RNA foundation model as input to lightweight regressor, we show substantial gains over traditional baselines. We also integrate chromatin accessibility data to capture regulatory context, improving performance further. Our results highlight the effectiveness of pre-trained foundation models and chromatin accessibility data for gRNA activity prediction.

