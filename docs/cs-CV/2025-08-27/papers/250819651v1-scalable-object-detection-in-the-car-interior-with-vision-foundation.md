---
layout: default
title: Scalable Object Detection in the Car Interior With Vision Foundation Models
---

# Scalable Object Detection in the Car Interior With Vision Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19651" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19651v1</a>
  <a href="https://arxiv.org/pdf/2508.19651.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19651v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19651v1', 'Scalable Object Detection in the Car Interior With Vision Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bálint Mészáros, Ahmet Firintepe, Sebastian Schmidt, Stephan Günnemann

**分类**: cs.CV

**发布日期**: 2025-08-27

---

## 💡 一句话要点

**提出ODAL框架以解决车内物体检测与定位问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `车内物体检测` `分布式计算` `场景理解` `基础模型` `微调技术` `智能汽车` `AI助手`

## 📋 核心要点

1. 现有方法在车载系统中受限于计算资源，难以实现高效的物体检测与定位。
2. 本文提出的ODAL框架通过分布式架构，结合车载与云端计算，提升了车内场景理解能力。
3. 经过微调的ODAL-LLaVA模型在ODAL_score上达到89%，较基线提升71%，并超越GPT-4o近20%。

## 📝 摘要（中文）

车内的AI任务，如识别和定位外部引入的物体，对于个人助手的响应质量至关重要。然而，车载系统的计算资源受限，限制了此类解决方案的直接部署。为了解决这一限制，本文提出了新颖的物体检测与定位（ODAL）框架，利用分布式架构将计算任务分配到车载系统和云端，从而克服了直接在车内运行基础模型的资源限制。我们还引入了ODALbench作为新的评估指标，全面评估检测和定位性能。实验结果表明，该框架在该领域建立了新的标准。

## 🔬 方法详解

**问题定义**：本文旨在解决车内物体检测与定位的计算资源限制问题。现有方法在车载系统中难以高效运行，影响了AI助手的响应质量。

**核心思路**：ODAL框架通过分布式架构，将计算任务分配到车载系统和云端，从而有效利用资源，提升检测与定位的准确性和效率。

**技术框架**：ODAL框架包括数据采集、模型推理和结果融合三个主要模块。数据采集通过车载摄像头获取场景信息，模型推理在云端和车载系统之间分配，最后进行结果融合以输出最终检测结果。

**关键创新**：ODAL框架的创新在于其分布式计算设计，使得基础模型可以在资源受限的环境中高效运行，显著提升了检测性能。

**关键设计**：在模型选择上，本文比较了GPT-4o与轻量级的LLaVA 1.5 7B模型，并通过微调提升了轻量模型的性能，最终实现了高达89%的ODAL_score。

## 📊 实验亮点

实验结果显示，微调后的ODAL-LLaVA模型在ODAL_score上达到89%，较基线提升71%，并且在检测准确性上显著降低了幻觉现象，其ODAL_SNR是GPT-4o的三倍，展示了该框架的强大性能。

## 🎯 应用场景

该研究的潜在应用领域包括智能汽车、自动驾驶和车载个人助手等。通过提高车内物体检测与定位的准确性，能够显著提升用户体验和安全性，推动智能交通系统的发展。未来，该框架还可扩展到其他需要实时场景理解的领域。

## 📄 摘要（原文）

> AI tasks in the car interior like identifying and localizing externally introduced objects is crucial for response quality of personal assistants. However, computational resources of on-board systems remain highly constrained, restricting the deployment of such solutions directly within the vehicle. To address this limitation, we propose the novel Object Detection and Localization (ODAL) framework for interior scene understanding. Our approach leverages vision foundation models through a distributed architecture, splitting computational tasks between on-board and cloud. This design overcomes the resource constraints of running foundation models directly in the car. To benchmark model performance, we introduce ODALbench, a new metric for comprehensive assessment of detection and localization.Our analysis demonstrates the framework's potential to establish new standards in this domain. We compare the state-of-the-art GPT-4o vision foundation model with the lightweight LLaVA 1.5 7B model and explore how fine-tuning enhances the lightweight models performance. Remarkably, our fine-tuned ODAL-LLaVA model achieves an ODAL$_{score}$ of 89%, representing a 71% improvement over its baseline performance and outperforming GPT-4o by nearly 20%. Furthermore, the fine-tuned model maintains high detection accuracy while significantly reducing hallucinations, achieving an ODAL$_{SNR}$ three times higher than GPT-4o.

