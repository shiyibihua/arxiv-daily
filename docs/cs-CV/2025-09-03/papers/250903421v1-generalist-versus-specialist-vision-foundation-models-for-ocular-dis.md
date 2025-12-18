---
layout: default
title: Generalist versus Specialist Vision Foundation Models for Ocular Disease and Oculomics
---

# Generalist versus Specialist Vision Foundation Models for Ocular Disease and Oculomics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03421" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03421v1</a>
  <a href="https://arxiv.org/pdf/2509.03421.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03421v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03421v1', 'Generalist versus Specialist Vision Foundation Models for Ocular Disease and Oculomics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yukun Zhou, Paul Nderitu, Jocelyn Hui Lin Goh, Justin Engelmann, Siegfried K. Wagner, Anran Ran, Hongyang Jiang, Lie Ju, Ke Zou, Sahana Srinivasan, Hyunmin Kim, Takahiro Ninomiya, Zheyuan Wang, Gabriel Dawei Yang, Eden Ruffell, Dominic Williamson, Rui Santos, Gabor Mark Somfai, Carol Y. Cheung, Tien Yin Wong, Daniel C. Alexander, Yih Chung Tham, Pearse A. Keane

**分类**: eess.IV, cs.CV

**发布日期**: 2025-09-03

**备注**: 39 pages, 8 Figures

---

## 💡 一句话要点

**领域专精的RETFound在眼科疾病和眼基因组学任务中优于通用视觉基础模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视网膜图像分析` `眼科疾病检测` `通用视觉模型` `领域专精模型` `迁移学习` `数据效率` `眼基因组学`

## 📋 核心要点

1. 现有方法依赖于通用视觉基础模型，但在眼科特定任务中表现不足，缺乏领域针对性。
2. 论文提出比较通用模型（DINOv2/v3）与领域专精模型（RETFound）在视网膜图像分析任务中的性能。
3. 实验结果表明，尽管通用模型具有良好的适应性，但专精的RETFound模型在眼科疾病检测和眼基因组学任务中表现更优。

## 📝 摘要（中文）

医学基础模型通过大规模临床数据预训练，在各种临床相关应用中表现出强大的性能。RETFound是在近百万张视网膜图像上训练的模型，是该方法在视网膜图像应用中的典范。然而，DINOv2和DINOv3等日益强大且规模更大的通用基础模型的出现，引发了领域特定预训练是否仍然必要的疑问，以及如果必要，差距在哪里。为了研究这一点，我们系统地评估了DINOv2和DINOv3在视网膜图像应用中的适应性，并将其与两个专精的RETFound模型RETFound-MAE和RETFound-DINOv2进行了比较。我们使用微调和线性探测两种适应策略评估了眼科疾病检测和全身疾病预测的性能。进一步分析了数据效率和适应效率，以表征预测性能和计算成本之间的权衡。结果表明，尽管扩展通用模型可以在各种任务中产生强大的适应性，但RETFound-DINOv2在眼科疾病检测和眼基因组学任务中始终优于这些通用基础模型，表现出更强的泛化性和数据效率。这些发现表明，专精的视网膜基础模型仍然是临床应用中最有效的选择，而与通用基础模型之间差距的缩小表明，持续的数据和模型扩展可以带来领域相关的收益，并使它们成为未来医学基础模型的强大基础。

## 🔬 方法详解

**问题定义**：论文旨在解决通用视觉基础模型在眼科疾病检测和眼基因组学任务中表现不如领域专精模型的问题。现有通用模型虽然规模庞大，但在处理特定领域的医学图像时，由于缺乏针对性的预训练，性能受到限制。

**核心思路**：论文的核心思路是通过对比通用视觉基础模型（DINOv2, DINOv3）和领域专精的视网膜图像基础模型（RETFound），来评估领域特定预训练的必要性以及存在的差距。通过在下游任务上的性能比较，揭示领域专精模型在数据效率和泛化能力上的优势。

**技术框架**：论文采用的整体框架包括：1) 使用通用视觉基础模型（DINOv2, DINOv3）和领域专精模型（RETFound-MAE, RETFound-DINOv2）作为特征提取器；2) 使用微调（Fine-tuning）和线性探测（Linear Probing）两种适应策略，将预训练模型应用于下游的眼科疾病检测和全身疾病预测任务；3) 评估模型在不同任务上的性能，并分析数据效率和适应效率。

**关键创新**：论文的关键创新在于系统性地比较了通用视觉基础模型和领域专精模型在眼科图像分析任务中的性能。通过实验证明，尽管通用模型可以通过大规模数据获得良好的泛化能力，但在特定领域，领域专精模型仍然具有优势，尤其是在数据效率和泛化能力方面。

**关键设计**：论文的关键设计包括：1) 选择DINOv2和DINOv3作为通用视觉基础模型，因为它们在通用视觉任务中表现出色；2) 选择RETFound作为领域专精模型，因为它是在大规模视网膜图像数据集上预训练的；3) 使用微调和线性探测两种适应策略，以评估模型在不同适应程度下的性能；4) 评估数据效率和适应效率，以量化模型在预测性能和计算成本之间的权衡。

## 📊 实验亮点

实验结果表明，RETFound-DINOv2在眼科疾病检测和眼基因组学任务中始终优于通用基础模型DINOv2和DINOv3，表现出更强的泛化性和数据效率。这表明，在眼科领域，领域专精的模型仍然具有显著优势，尤其是在数据有限的情况下。

## 🎯 应用场景

该研究成果可应用于眼科疾病的早期诊断、个性化治疗方案的制定以及全身性疾病的预测。通过利用领域专精的视网膜基础模型，可以提高诊断的准确性和效率，从而改善患者的治疗效果。未来的影响在于推动医学影像分析领域的发展，并为构建更有效的医学人工智能系统提供指导。

## 📄 摘要（原文）

> Medical foundation models, pre-trained with large-scale clinical data, demonstrate strong performance in diverse clinically relevant applications. RETFound, trained on nearly one million retinal images, exemplifies this approach in applications with retinal images. However, the emergence of increasingly powerful and multifold larger generalist foundation models such as DINOv2 and DINOv3 raises the question of whether domain-specific pre-training remains essential, and if so, what gap persists. To investigate this, we systematically evaluated the adaptability of DINOv2 and DINOv3 in retinal image applications, compared to two specialist RETFound models, RETFound-MAE and RETFound-DINOv2. We assessed performance on ocular disease detection and systemic disease prediction using two adaptation strategies: fine-tuning and linear probing. Data efficiency and adaptation efficiency were further analysed to characterise trade-offs between predictive performance and computational cost. Our results show that although scaling generalist models yields strong adaptability across diverse tasks, RETFound-DINOv2 consistently outperforms these generalist foundation models in ocular-disease detection and oculomics tasks, demonstrating stronger generalisability and data efficiency. These findings suggest that specialist retinal foundation models remain the most effective choice for clinical applications, while the narrowing gap with generalist foundation models suggests that continued data and model scaling can deliver domain-relevant gains and position them as strong foundations for future medical foundation models.

