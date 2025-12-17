---
layout: default
title: Native Intelligence Emerges from Large-Scale Clinical Practice: A Retinal Foundation Model with Deployment Efficiency
---

# Native Intelligence Emerges from Large-Scale Clinical Practice: A Retinal Foundation Model with Deployment Efficiency

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14499" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14499v1</a>
  <a href="https://arxiv.org/pdf/2512.14499.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14499v1" onclick="toggleFavorite(this, '2512.14499v1', 'Native Intelligence Emerges from Large-Scale Clinical Practice: A Retinal Foundation Model with Deployment Efficiency')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jia Guo, Jiawei Du, Shengzhu Yang, Shuai Lu, Wenquan Cheng, Kaiwen Zhang, Yihua Sun, Chuhong Yang, Weihang Zhang, Fang Chen, Yilan Wu, Lie Ju, Guochen Ning, Longfei Ma, Huiping Yao, Jinyuan Wang, Peilun Shi, Yukun Zhou, Jie Xu, Pearse A. Keane, Hanruo Liu, Hongen Liao, Ningli Wang, Huiqi Li

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**ReVision：基于大规模临床实践的视网膜原生智能模型，提升部署效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视网膜疾病诊断` `眼底图像分析` `远程医疗` `深度学习` `迁移学习`

## 📋 核心要点

1. 现有视网膜基础模型依赖人工数据集，缺乏真实临床环境，且需大量任务优化，限制了低资源环境下的部署。
2. ReVision利用大规模远程医疗项目积累的眼底照片和诊断报告，学习临床图像解读，构建临床原生智能。
3. ReVision在多个眼科基准测试中表现出色，无需特定训练即可实现高精度疾病检测，并能有效迁移到新场景。

## 📝 摘要（中文）

现有的视网膜基础模型受限于缺乏真实临床背景的人工数据集，并且需要针对每个应用进行大量的任务特定优化，限制了其在低资源环境中的部署效率。本文提出ReVision，一个从真实医疗实践中学习临床原生智能的视网膜基础模型。核心思想是，大规模远程医疗项目是学习临床图像解读的天然资源库。ReVision从中国162家医疗机构十年远程医疗项目中积累的485,980张彩色眼底照片及其诊断报告的自然对齐关系中学习。在27个眼科基准测试中，ReVision在极少本地资源下实现了高效部署。无需任何任务特定训练，ReVision在12个公共基准测试中实现了0.946的平均AUROC，在3个独立临床队列中实现了0.952的平均AUROC。当进行少量适配时，ReVision匹配了经过大量微调的替代方案，同时需要的可训练参数和标记样本数量级更少。学习到的表征有效地迁移到新的临床站点、成像领域、成像模式和全身健康预测任务。在对33名眼科医生的前瞻性读者研究中，ReVision的零样本辅助将诊断准确率提高了14.8%。这些结果表明，可以直接从临床档案中提取临床原生智能，而无需任何进一步的注释，从而构建适用于各种低资源环境的医疗AI系统。

## 🔬 方法详解

**问题定义**：现有视网膜基础模型依赖于经过人工标注和筛选的数据集，这些数据集往往无法充分代表真实临床环境的多样性和复杂性。此外，针对不同的眼科疾病诊断任务，这些模型通常需要进行大量的任务特定微调，导致部署成本高昂，尤其是在资源有限的医疗机构中，难以实现高效部署。

**核心思路**：本文的核心思路是利用大规模远程医疗项目中积累的眼底照片和诊断报告之间的自然对齐关系，直接从真实临床实践中学习临床原生智能。这种方法避免了人工标注的成本和偏差，能够更好地捕捉临床数据的真实分布，从而提高模型的泛化能力和鲁棒性。

**技术框架**：ReVision的整体框架包括数据收集与预处理、模型训练和评估三个主要阶段。首先，从大规模远程医疗项目中收集眼底照片和对应的诊断报告，并进行数据清洗和预处理。然后，利用对比学习等技术，训练一个能够从眼底照片中提取有效特征的深度学习模型。最后，在多个眼科疾病诊断基准测试中评估模型的性能，并进行迁移学习实验，验证模型的泛化能力。

**关键创新**：ReVision最重要的技术创新点在于其“临床原生智能”的学习方式。与传统的依赖人工标注数据的训练方法不同，ReVision直接从真实临床实践中学习，能够更好地捕捉临床数据的真实分布，从而提高模型的泛化能力和鲁棒性。此外，ReVision还采用了高效的迁移学习策略，能够快速适应新的临床场景和任务，降低部署成本。

**关键设计**：ReVision采用了Transformer作为主干网络，利用自注意力机制捕捉眼底图像中的全局信息。在损失函数方面，采用了对比学习损失，鼓励模型学习到具有区分性的特征表示。此外，为了提高模型的泛化能力，还采用了数据增强、正则化等技术。

## 📊 实验亮点

ReVision在12个公共基准测试中实现了0.946的平均AUROC，在3个独立临床队列中实现了0.952的平均AUROC，无需任何任务特定训练。在对33名眼科医生的前瞻性读者研究中，ReVision的零样本辅助将诊断准确率提高了14.8%。ReVision在少量适配时，匹配了经过大量微调的替代方案，同时需要的可训练参数和标记样本数量级更少。

## 🎯 应用场景

ReVision具有广泛的应用前景，可用于眼科疾病的早期筛查、诊断和治疗方案制定。尤其是在医疗资源匮乏的地区，ReVision可以作为一种低成本、高效的辅助诊断工具，帮助医生提高诊断准确率，改善患者的就医体验。未来，ReVision还可以扩展到其他医学影像领域，为构建智能医疗系统提供有力支持。

## 📄 摘要（原文）

> Current retinal foundation models remain constrained by curated research datasets that lack authentic clinical context, and require extensive task-specific optimization for each application, limiting their deployment efficiency in low-resource settings. Here, we show that these barriers can be overcome by building clinical native intelligence directly from real-world medical practice. Our key insight is that large-scale telemedicine programs, where expert centers provide remote consultations across distributed facilities, represent a natural reservoir for learning clinical image interpretation. We present ReVision, a retinal foundation model that learns from the natural alignment between 485,980 color fundus photographs and their corresponding diagnostic reports, accumulated through a decade-long telemedicine program spanning 162 medical institutions across China. Through extensive evaluation across 27 ophthalmic benchmarks, we demonstrate that ReVison enables deployment efficiency with minimal local resources. Without any task-specific training, ReVision achieves zero-shot disease detection with an average AUROC of 0.946 across 12 public benchmarks and 0.952 on 3 independent clinical cohorts. When minimal adaptation is feasible, ReVision matches extensively fine-tuned alternatives while requiring orders of magnitude fewer trainable parameters and labeled examples. The learned representations also transfer effectively to new clinical sites, imaging domains, imaging modalities, and systemic health prediction tasks. In a prospective reader study with 33 ophthalmologists, ReVision's zero-shot assistance improved diagnostic accuracy by 14.8% across all experience levels. These results demonstrate that clinical native intelligence can be directly extracted from clinical archives without any further annotation to build medical AI systems suited to various low-resource settings.

