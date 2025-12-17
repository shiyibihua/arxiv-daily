---
layout: default
title: Adaptable Segmentation Pipeline for Diverse Brain Tumors with Radiomic-guided Subtyping and Lesion-Wise Model Ensemble
---

# Adaptable Segmentation Pipeline for Diverse Brain Tumors with Radiomic-guided Subtyping and Lesion-Wise Model Ensemble

**arXiv**: [2512.14648v1](https://arxiv.org/abs/2512.14648) | [PDF](https://arxiv.org/pdf/2512.14648.pdf)

**作者**: Daniel Capellán-Martín, Abhijeet Parida, Zhifan Jiang, Nishad Kulkarni, Krithika Iyer, Austin Tapp, Syed Muhammad Anwar, María J. Ledesma-Carbayo, Marius George Linguraru

**分类**: cs.CV, eess.IV

**发布日期**: 2025-12-16

**备注**: 12 pages, 5 figures, 3 tables. Algorithm presented at MICCAI BraTS 2025

---

## 💡 一句话要点

**提出一种基于放射组学引导和病灶级模型集成的脑肿瘤自适应分割流程**

🎯 **匹配领域**: **物理动画 (Physics-based Animation)**

**关键词**: `脑肿瘤分割` `放射组学` `模型集成` `自适应分割` `深度学习`

## 📋 核心要点

1. 脑肿瘤类型多样，多参数MRI图像分割面临鲁棒性和泛化性挑战。
2. 利用放射组学特征指导肿瘤亚型检测，实现更平衡的训练，并结合病灶级性能指标优化模型集成。
3. 在BraTS挑战赛数据集上，该流程取得了与顶尖算法相当的性能，验证了其有效性。

## 📝 摘要（中文）

在多参数磁共振成像（MRI）上对脑肿瘤进行鲁棒且泛化的分割仍然很困难，因为肿瘤类型差异很大。BraTS 2025 Lighthouse Challenge 在成人和儿童肿瘤的多样化高质量数据集上对分割方法进行基准测试，包括：多联盟国际儿科脑肿瘤分割（PED）、术前脑膜瘤肿瘤分割（MEN）、脑膜瘤放射治疗分割（MEN-RT）以及治疗前和治疗后脑转移瘤分割（MET）。我们提出了一种灵活、模块化和自适应的流程，通过选择和组合最先进的模型，并在训练前后应用肿瘤和病灶特定的处理来提高分割性能。从 MRI 中提取的放射组学特征有助于检测肿瘤亚型，确保更平衡的训练。自定义病灶级别性能指标确定每个模型在集成中的影响，并优化进一步细化预测的后处理，使工作流程能够针对每个病例定制每个步骤。在 BraTS 测试集上，我们的流程实现了与多个挑战中排名靠前的算法相当的性能。这些发现证实，自定义病灶感知处理和模型选择可以产生鲁棒的分割，而无需将方法锁定到特定的网络架构。我们的方法具有在临床实践中进行定量肿瘤测量的潜力，支持诊断和预后。

## 🔬 方法详解

**问题定义**：论文旨在解决多参数MRI图像中不同类型脑肿瘤的精确分割问题。现有方法难以在不同肿瘤类型和数据集上保持鲁棒性和泛化性，需要针对特定肿瘤类型进行调整，缺乏通用性。

**核心思路**：论文的核心思路是构建一个灵活、模块化和自适应的分割流程，该流程能够根据肿瘤类型和病灶特征，自动选择和组合合适的分割模型，并进行针对性的预处理和后处理。通过放射组学特征指导肿瘤亚型检测，实现更平衡的训练，并利用病灶级性能指标优化模型集成。

**技术框架**：该流程包含以下主要模块：1) 数据预处理：包括图像配准、标准化等操作；2) 放射组学特征提取：从MRI图像中提取放射组学特征，用于肿瘤亚型检测；3) 肿瘤亚型检测：利用放射组学特征对肿瘤进行亚型分类；4) 模型选择与集成：根据肿瘤亚型选择合适的分割模型，并进行集成；5) 病灶级后处理：根据病灶级性能指标，对分割结果进行优化。

**关键创新**：该方法最重要的创新点在于其自适应性，能够根据肿瘤类型和病灶特征，自动调整分割流程的各个环节，从而提高分割的鲁棒性和泛化性。此外，利用放射组学特征指导肿瘤亚型检测，并利用病灶级性能指标优化模型集成，也是该方法的关键创新。

**关键设计**：论文中，放射组学特征的选择和提取方法、肿瘤亚型分类器的设计、模型集成的策略、病灶级性能指标的定义以及后处理的优化方法等都是关键的设计细节。具体的网络结构和损失函数选择取决于所使用的分割模型。

## 📊 实验亮点

该方法在BraTS 2025 Lighthouse Challenge的多个子任务中取得了与顶尖算法相当的性能，证明了其在不同类型脑肿瘤分割任务中的有效性和泛化能力。该方法无需锁定特定网络架构，具有很强的灵活性和可扩展性。

## 🎯 应用场景

该研究成果可应用于临床脑肿瘤诊断和治疗计划制定。精确的肿瘤分割能够帮助医生更准确地评估肿瘤的大小、位置和形态，从而制定更有效的治疗方案，并对治疗效果进行评估。该方法还可用于药物研发，辅助评估药物对肿瘤的疗效。

## 📄 摘要（原文）

> Robust and generalizable segmentation of brain tumors on multi-parametric magnetic resonance imaging (MRI) remains difficult because tumor types differ widely. The BraTS 2025 Lighthouse Challenge benchmarks segmentation methods on diverse high-quality datasets of adult and pediatric tumors: multi-consortium international pediatric brain tumor segmentation (PED), preoperative meningioma tumor segmentation (MEN), meningioma radiotherapy segmentation (MEN-RT), and segmentation of pre- and post-treatment brain metastases (MET). We present a flexible, modular, and adaptable pipeline that improves segmentation performance by selecting and combining state-of-the-art models and applying tumor- and lesion-specific processing before and after training. Radiomic features extracted from MRI help detect tumor subtype, ensuring a more balanced training. Custom lesion-level performance metrics determine the influence of each model in the ensemble and optimize post-processing that further refines the predictions, enabling the workflow to tailor every step to each case. On the BraTS testing sets, our pipeline achieved performance comparable to top-ranked algorithms across multiple challenges. These findings confirm that custom lesion-aware processing and model selection yield robust segmentations yet without locking the method to a specific network architecture. Our method has the potential for quantitative tumor measurement in clinical practice, supporting diagnosis and prognosis.

