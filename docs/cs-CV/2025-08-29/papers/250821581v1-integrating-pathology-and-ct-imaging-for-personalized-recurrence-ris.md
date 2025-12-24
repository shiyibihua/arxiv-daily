---
layout: default
title: Integrating Pathology and CT Imaging for Personalized Recurrence Risk Prediction in Renal Cancer
---

# Integrating Pathology and CT Imaging for Personalized Recurrence Risk Prediction in Renal Cancer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21581" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21581v1</a>
  <a href="https://arxiv.org/pdf/2508.21581.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21581v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21581v1', 'Integrating Pathology and CT Imaging for Personalized Recurrence Risk Prediction in Renal Cancer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daniël Boeke, Cedrik Blommestijn, Rebecca N. Wray, Kalina Chupetlovska, Shangqi Gao, Zeyu Gao, Regina G. H. Beets-Tan, Mireia Crispin-Ortuzar, James O. Jones, Wilson Silva, Ines P. Machado

**分类**: cs.CV

**发布日期**: 2025-08-29

**备注**: 12 pages, 2 figures, 1 table. Accepted at the Multimodal Learning and Fusion Across Scales for Clinical Decision Support (ML-CDS) Workshop, MICCAI 2025. This is the submitted version with authors, affiliations, and acknowledgements included; it has not undergone peer review or revisions. The final version will appear in the Springer Lecture Notes in Computer Science (LNCS) proceedings

---

## 💡 一句话要点

**提出多模态融合方法以提升肾癌复发风险预测精度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态融合` `深度学习` `肾癌` `复发风险预测` `病理学` `计算机断层扫描` `生存建模`

## 📋 核心要点

1. 现有的Leibovich评分在患者级别的分辨率有限，且未考虑影像信息，导致复发风险评估不足。
2. 本研究提出了一种多模态融合方法，通过整合CT影像和病理WSI，利用深度学习框架进行复发风险预测。
3. 实验结果表明，WSI模型在性能上优于CT模型，中期融合方法进一步提升了预测精度，接近临床基线水平。

## 📝 摘要（中文）

在透明细胞肾细胞癌（ccRCC）中，复发风险评估对指导术后监测和治疗至关重要。尽管Leibovich评分广泛用于分层远处复发风险，但其在患者级别的分辨率有限，并且未考虑影像信息。本研究通过整合术前计算机断层扫描（CT）和术后组织病理全切片图像（WSIs），评估多模态复发预测。采用模块化深度学习框架，结合预训练编码器和基于Cox的生存建模，测试了单模态、晚期融合和中期融合设置。在真实的ccRCC队列中，基于WSI的模型始终优于仅使用CT的模型，突显了病理学的预后强度。中期融合进一步提升了性能，最佳模型（TITAN-CONCH与ResNet-18）接近调整后的Leibovich评分。随机平局打破缩小了临床基线与学习模型之间的差距，表明离散化可能夸大个体化性能。通过简单的嵌入连接，放射学主要通过融合增加了价值。这些发现展示了基于基础模型的多模态整合在个性化ccRCC风险预测中的可行性。

## 🔬 方法详解

**问题定义**：本研究旨在解决透明细胞肾细胞癌（ccRCC）复发风险评估中，现有Leibovich评分的局限性，尤其是在患者级别分辨率和影像信息的缺失问题。

**核心思路**：通过整合术前CT影像和术后病理WSI，采用深度学习框架进行多模态复发风险预测，以提高预测的准确性和个性化水平。

**技术框架**：整体架构包括预训练的编码器和Cox生存模型，测试了单模态、晚期融合和中期融合的不同设置，以评估各自的性能。

**关键创新**：本研究的主要创新在于中期融合策略的应用，显著提升了模型的预测能力，且WSI模型的表现优于传统CT模型，展示了病理学在预后评估中的重要性。

**关键设计**：采用ResNet-18作为基础网络结构，结合随机平局打破策略，优化了模型的性能评估，确保了多模态数据的有效融合。

## 📊 实验亮点

实验结果显示，基于WSI的模型在复发风险预测中表现优于CT模型，尤其是在中期融合设置下，最佳模型（TITAN-CONCH与ResNet-18）接近调整后的Leibovich评分，展示了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括肾癌患者的个性化治疗方案制定和术后监测，能够为临床医生提供更为精准的复发风险评估，进而优化患者的治疗策略，提升生存率。未来，研究还可扩展至其他类型癌症的多模态融合风险预测。

## 📄 摘要（原文）

> Recurrence risk estimation in clear cell renal cell carcinoma (ccRCC) is essential for guiding postoperative surveillance and treatment. The Leibovich score remains widely used for stratifying distant recurrence risk but offers limited patient-level resolution and excludes imaging information. This study evaluates multimodal recurrence prediction by integrating preoperative computed tomography (CT) and postoperative histopathology whole-slide images (WSIs). A modular deep learning framework with pretrained encoders and Cox-based survival modeling was tested across unimodal, late fusion, and intermediate fusion setups. In a real-world ccRCC cohort, WSI-based models consistently outperformed CT-only models, underscoring the prognostic strength of pathology. Intermediate fusion further improved performance, with the best model (TITAN-CONCH with ResNet-18) approaching the adjusted Leibovich score. Random tie-breaking narrowed the gap between the clinical baseline and learned models, suggesting discretization may overstate individualized performance. Using simple embedding concatenation, radiology added value primarily through fusion. These findings demonstrate the feasibility of foundation model-based multimodal integration for personalized ccRCC risk prediction. Future work should explore more expressive fusion strategies, larger multimodal datasets, and general-purpose CT encoders to better match pathology modeling capacity.

