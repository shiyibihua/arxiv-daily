---
layout: default
title: Human-Alignment and Calibration of Inference-Time Uncertainty in Large Language Models
---

# Human-Alignment and Calibration of Inference-Time Uncertainty in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08204" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08204v1</a>
  <a href="https://arxiv.org/pdf/2508.08204.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08204v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08204v1', 'Human-Alignment and Calibration of Inference-Time Uncertainty in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kyle Moore, Jesse Roberts, Daryl Watson

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-11

**备注**: preprint, under review

---

## 💡 一句话要点

**提出人类对齐与推理时不确定性校准方法以提升LLM用户体验**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `不确定性校准` `大型语言模型` `人类对齐` `推理时不确定性` `模型校准` `用户体验` `智能助手`

## 📋 核心要点

1. 现有研究对大型语言模型的不确定性校准关注较多，但对模型不确定性与人类不确定性的对齐评估较少。
2. 本研究通过评估多种推理时不确定性度量，探索其与人类不确定性及模型校准的对齐程度，提出了新的度量变体。
3. 实验结果显示，多个度量与人类不确定性高度对齐，并在正确性相关性和分布分析中展现出中到强的模型校准证据。

## 📝 摘要（中文）

近年来，评估大型语言模型的不确定性校准引起了广泛关注，以便于模型控制和调节用户信任。推理时的不确定性为模型或外部控制模块提供实时信号，尤其重要。本研究评估了一系列推理时不确定性度量，使用既有指标和新变体，探讨其与人类群体不确定性及传统模型校准的对齐程度。结果表明，多个度量与人类不确定性高度对齐，尽管与人类答案偏好不一致。对于这些成功的度量，我们发现其在正确性相关性和分布分析方面表现出中到强的模型校准证据。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型推理时不确定性与人类不确定性之间的对齐问题。现有方法主要集中在模型校准上，缺乏对人类不确定性的直接评估。

**核心思路**：论文通过评估一系列推理时不确定性度量，结合传统指标和新变体，探讨其与人类不确定性之间的关系，以提高模型的实用性和用户体验。

**技术框架**：研究首先定义了不确定性度量的标准，然后通过实验比较这些度量与人类群体不确定性之间的对齐程度，最后分析模型校准的表现。

**关键创新**：本研究的创新在于提出了新的不确定性度量变体，并通过实证分析验证了这些度量与人类不确定性之间的强对齐性，填补了现有研究的空白。

**关键设计**：在实验中，采用了多种标准度量和新提出的变体，设计了相应的损失函数和评估指标，以确保对齐性和校准性的全面评估。具体参数设置和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果显示，多个推理时不确定性度量与人类不确定性高度对齐，尤其在正确性相关性和分布分析中表现出中到强的模型校准证据。这表明所提出的方法在实际应用中具有显著的潜力和价值。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动问答系统和人机交互等场景。通过提高大型语言模型的不确定性校准，能够增强用户对模型的信任，从而提升用户体验和满意度。未来，该研究可能推动更智能的交互系统的发展，促进人机协作的效率。

## 📄 摘要（原文）

> There has been much recent interest in evaluating large language models for uncertainty calibration to facilitate model control and modulate user trust. Inference time uncertainty, which may provide a real-time signal to the model or external control modules, is particularly important for applying these concepts to improve LLM-user experience in practice. While many of the existing papers consider model calibration, comparatively little work has sought to evaluate how closely model uncertainty aligns to human uncertainty. In this work, we evaluate a collection of inference-time uncertainty measures, using both established metrics and novel variations, to determine how closely they align with both human group-level uncertainty and traditional notions of model calibration. We find that numerous measures show evidence of strong alignment to human uncertainty, even despite the lack of alignment to human answer preference. For those successful metrics, we find moderate to strong evidence of model calibration in terms of both correctness correlation and distributional analysis.

