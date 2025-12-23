---
layout: default
title: Robustness Evaluation of OCR-based Visual Document Understanding under Multi-Modal Adversarial Attacks
---

# Robustness Evaluation of OCR-based Visual Document Understanding under Multi-Modal Adversarial Attacks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16407" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16407v1</a>
  <a href="https://arxiv.org/pdf/2506.16407.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16407v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16407v1', 'Robustness Evaluation of OCR-based Visual Document Understanding under Multi-Modal Adversarial Attacks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dong Nguyen Tien, Dung D. Le

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-19

**备注**: 8 pages, 1 figure, under review at EMNLP 2025

---

## 💡 一句话要点

**提出统一框架以评估OCR基础视觉文档理解的鲁棒性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `视觉文档理解` `对抗攻击` `OCR技术` `多模态融合` `鲁棒性评估`

## 📋 核心要点

1. 现有的视觉文档理解系统在面对现实世界中的对抗扰动时，鲁棒性不足，影响信息提取的准确性。
2. 本文提出了一个统一框架，能够生成和评估多模态对抗攻击，涵盖多种布局攻击场景，确保扰动的合理性。
3. 实验结果显示，行级攻击和复合扰动对模型性能的影响最为显著，PGD方法在所有模型中表现优越。

## 📝 摘要（中文）

视觉文档理解（VDU）系统通过整合文本、布局和视觉信号在信息提取方面取得了显著的性能。然而，它们在现实对抗扰动下的鲁棒性仍然不足。本文首次提出了一个统一框架，用于生成和评估针对OCR基础VDU模型的多模态对抗攻击。该方法涵盖六种基于梯度的布局攻击场景，涉及OCR边界框、像素和文本的操控，并在布局扰动预算（如IoU >= 0.6）下保持合理性。实验结果表明，行级攻击和复合扰动（边界框 + 像素 + 文本）导致性能显著下降。基于投影梯度下降（PGD）的边界框扰动在所有模型中均优于随机偏移基线。消融研究进一步验证了布局预算、文本修改和对抗可转移性的影响。

## 🔬 方法详解

**问题定义**：本文旨在解决OCR基础视觉文档理解模型在面对多模态对抗攻击时的鲁棒性不足问题。现有方法未能充分考虑对抗扰动对信息提取的影响，导致性能下降。

**核心思路**：论文提出的统一框架通过生成多种对抗攻击，评估其对VDU模型的影响，确保攻击的合理性和有效性。通过对布局、文本和像素的综合操控，增强模型的鲁棒性评估。

**技术框架**：该框架包括攻击生成模块和评估模块。攻击生成模块负责创建不同类型的对抗扰动，而评估模块则通过实验验证模型在这些扰动下的性能表现。

**关键创新**：最重要的创新在于首次系统性地将多模态对抗攻击应用于OCR基础VDU模型，并通过布局预算约束确保扰动的合理性，区别于以往的单一攻击方法。

**关键设计**：在设计中，设置了布局扰动预算（如IoU >= 0.6），并采用了基于PGD的边界框扰动方法，确保了攻击的有效性和可转移性。

## 📊 实验亮点

实验结果显示，行级攻击和复合扰动（边界框 + 像素 + 文本）导致性能显著下降，尤其是PGD方法在所有模型中均优于随机偏移基线，验证了布局预算和文本修改的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括文档自动化处理、信息提取和智能文档分析等。通过提高VDU系统在对抗攻击下的鲁棒性，可以增强其在实际应用中的可靠性和安全性，推动智能文档处理技术的发展。

## 📄 摘要（原文）

> Visual Document Understanding (VDU) systems have achieved strong performance in information extraction by integrating textual, layout, and visual signals. However, their robustness under realistic adversarial perturbations remains insufficiently explored. We introduce the first unified framework for generating and evaluating multi-modal adversarial attacks on OCR-based VDU models. Our method covers six gradient-based layout attack scenarios, incorporating manipulations of OCR bounding boxes, pixels, and texts across both word and line granularities, with constraints on layout perturbation budget (e.g., IoU >= 0.6) to preserve plausibility.
>   Experimental results across four datasets (FUNSD, CORD, SROIE, DocVQA) and six model families demonstrate that line-level attacks and compound perturbations (BBox + Pixel + Text) yield the most severe performance degradation. Projected Gradient Descent (PGD)-based BBox perturbations outperform random-shift baselines in all investigated models. Ablation studies further validate the impact of layout budget, text modification, and adversarial transferability.

