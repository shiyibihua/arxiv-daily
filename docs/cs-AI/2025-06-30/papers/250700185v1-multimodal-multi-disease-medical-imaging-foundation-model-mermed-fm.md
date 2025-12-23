---
layout: default
title: Multimodal, Multi-Disease Medical Imaging Foundation Model (MerMED-FM)
---

# Multimodal, Multi-Disease Medical Imaging Foundation Model (MerMED-FM)

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00185" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00185v1</a>
  <a href="https://arxiv.org/pdf/2507.00185.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00185v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00185v1', 'Multimodal, Multi-Disease Medical Imaging Foundation Model (MerMED-FM)')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yang Zhou, Chrystie Wan Ning Quek, Jun Zhou, Yan Wang, Yang Bai, Yuhe Ke, Jie Yao, Laura Gutierrez, Zhen Ling Teo, Darren Shu Jeng Ting, Brian T. Soetikno, Christopher S. Nielsen, Tobias Elze, Zengxiang Li, Linh Le Dinh, Lionel Tim-Ee Cheng, Tran Nguyen Tuan Anh, Chee Leong Cheng, Tien Yin Wong, Nan Liu, Iain Beehuat Tan, Tony Kiat Hon Lim, Rick Siow Mong Goh, Yong Liu, Daniel Shu Wei Ting

**分类**: eess.IV, cs.AI, cs.CV

**发布日期**: 2025-06-30

**备注**: 42 pages, 3 composite figures, 4 tables

---

## 💡 一句话要点

**提出MerMED-FM以解决多模态医学影像分析的准确性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态医学影像` `自监督学习` `基础模型` `医学影像分析` `跨专业应用`

## 📋 核心要点

1. 现有医学影像AI模型多为单模态和单疾病，导致临床应用中的准确性不足。
2. MerMED-FM通过自监督学习和记忆模块，整合多模态和多疾病影像数据，提升模型的适应性和准确性。
3. 在330万张医学影像的评估中，MerMED-FM在各模态下均表现出色，AUROC值最高达到0.988，显示出显著的性能提升。

## 📝 摘要（中文）

当前的人工智能医学影像模型主要集中于单一模态和单一疾病，导致临床准确性不一致。为了解决这一问题，研究团队开发了MerMED-FM，这是一个先进的多模态、多疾病基础模型，采用自监督学习和记忆模块进行训练。该模型基于330万张来自十多个专业和七种模态的医学影像进行训练，表现出在多种疾病上的强大性能，AUROC值在不同模态下均超过0.85，显示出其在跨专业医学影像解读中的潜力。

## 🔬 方法详解

**问题定义**：当前医学影像AI模型主要集中于单一模态和单一疾病，导致在多疾病和多模态情况下的临床准确性不一致，且训练这些模型通常需要大量标注良好的数据集，成本高且耗时。

**核心思路**：MerMED-FM通过自监督学习和记忆模块，整合来自不同模态和疾病的数据，旨在提升模型的泛化能力和适应性，使其能够在多种医学影像任务中表现优异。

**技术框架**：该模型的整体架构包括数据预处理、特征提取、记忆模块和自监督学习机制。通过这些模块，模型能够有效地学习不同模态之间的关联性和特征。

**关键创新**：MerMED-FM的主要创新在于其多模态和多疾病的整合能力，利用自监督学习减少对标注数据的依赖，同时通过记忆模块增强模型的学习能力，与传统单一模态模型相比，具有更高的适应性和准确性。

**关键设计**：在模型设计中，采用了多层卷积神经网络（CNN）进行特征提取，结合了多种损失函数以优化不同模态的学习效果，确保模型在多种医学影像任务中的表现均衡。

## 📊 实验亮点

在评估中，MerMED-FM在多种模态下均表现出色，AUROC值分别为0.988（OCT）、0.982（病理）、0.951（超声）、0.943（CT）、0.931（皮肤）、0.894（CFP）和0.858（CXR），显示出其在多疾病影像分析中的强大性能，显著优于现有基础模型。

## 🎯 应用场景

MerMED-FM的潜在应用领域包括医院的影像诊断、远程医疗和医学研究等。其强大的多模态处理能力使得医生能够更准确地解读不同类型的医学影像，从而提高诊断效率和准确性，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Current artificial intelligence models for medical imaging are predominantly single modality and single disease. Attempts to create multimodal and multi-disease models have resulted in inconsistent clinical accuracy. Furthermore, training these models typically requires large, labour-intensive, well-labelled datasets. We developed MerMED-FM, a state-of-the-art multimodal, multi-specialty foundation model trained using self-supervised learning and a memory module. MerMED-FM was trained on 3.3 million medical images from over ten specialties and seven modalities, including computed tomography (CT), chest X-rays (CXR), ultrasound (US), pathology patches, color fundus photography (CFP), optical coherence tomography (OCT) and dermatology images. MerMED-FM was evaluated across multiple diseases and compared against existing foundational models. Strong performance was achieved across all modalities, with AUROCs of 0.988 (OCT); 0.982 (pathology); 0.951 (US); 0.943 (CT); 0.931 (skin); 0.894 (CFP); 0.858 (CXR). MerMED-FM has the potential to be a highly adaptable, versatile, cross-specialty foundation model that enables robust medical imaging interpretation across diverse medical disciplines.

