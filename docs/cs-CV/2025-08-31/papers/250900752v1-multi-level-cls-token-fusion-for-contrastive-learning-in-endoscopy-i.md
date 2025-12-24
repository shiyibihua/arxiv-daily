---
layout: default
title: Multi-Level CLS Token Fusion for Contrastive Learning in Endoscopy Image Classification
---

# Multi-Level CLS Token Fusion for Contrastive Learning in Endoscopy Image Classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00752" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00752v1</a>
  <a href="https://arxiv.org/pdf/2509.00752.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00752v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00752v1', 'Multi-Level CLS Token Fusion for Contrastive Learning in Endoscopy Image Classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Y Hop Nguyen, Doan Anh Phan Huu, Trung Thai Tran, Nhat Nam Mai, Van Toi Giap, Thao Thi Phuong Dao, Trung-Nghia Le

**分类**: cs.CV

**发布日期**: 2025-08-31

**备注**: ACM Multimedia 2025

**DOI**: [10.1145/3746027.3762093](https://doi.org/10.1145/3746027.3762093)

---

## 💡 一句话要点

**提出多层CLS Token融合以解决内窥镜图像分类问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `内窥镜图像分析` `多模态学习` `对比学习` `自然语言处理` `医学图像分类` `视觉-语言框架`

## 📋 核心要点

1. 现有的基于CNN的方法在捕捉跨模态语义方面存在困难，限制了内窥镜图像分析的效果。
2. 本文提出了一种基于CLIP ViT-B/16的框架，通过低秩适应和多层CLS token聚合来增强模型的表现力。
3. 在ACM MM'25 ENTRep Grand Challenge中，我们的框架在分类和检索任务中均取得了优异的性能，验证了其有效性。

## 📝 摘要（中文）

本文提出了一种统一的视觉-语言框架，专为耳鼻喉科内窥镜图像分析而设计，同时解决图像分类、图像到图像检索和文本到图像检索三项临床相关任务。与传统的基于CNN的方法相比，我们的方法利用CLIP ViT-B/16骨干网络，并通过低秩适应、多层CLS token聚合和球面特征插值进行增强。这些组件共同实现了在有限医学数据上的高效微调，同时改善了跨模态的表示多样性和语义对齐。为缩小视觉输入与文本诊断上下文之间的差距，我们引入了类特定的自然语言提示，通过结合监督分类与对比学习的联合训练目标来引导图像编码器。我们在ACM MM'25 ENTRep Grand Challenge中验证了该框架，分类准确率和F1-score达到95%，图像到图像和文本到图像检索的Recall@1分别为0.93和0.92，MRR分数为0.97和0.96。消融研究证明了每个架构组件的增益，验证了我们设计在低资源临床环境中实现稳健多模态医学理解的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决内窥镜图像分类及相关检索任务中的跨模态语义捕捉不足的问题。现有方法多依赖于CNN，难以有效整合视觉和文本信息。

**核心思路**：我们提出的框架利用CLIP ViT-B/16骨干网络，通过低秩适应和多层CLS token聚合来提升模型在有限医学数据上的表现，同时引入类特定的自然语言提示以增强语义对齐。

**技术框架**：整体架构包括图像编码器和文本编码器，采用联合训练目标，结合监督分类与对比学习。图像编码器通过自然语言提示引导，增强了对图像内容的理解。

**关键创新**：最重要的创新在于多层CLS token的聚合和球面特征插值，这些设计使得模型在多模态数据上实现了更好的表示多样性和语义对齐，区别于传统的单一特征提取方法。

**关键设计**：我们在模型中设置了低秩适应的参数，采用了特定的损失函数来平衡分类与对比学习的目标，同时优化了网络结构以适应医学图像的特性。通过消融实验验证了各个组件的有效性。

## 📊 实验亮点

在ACM MM'25 ENTRep Grand Challenge中，我们的框架在分类任务中达到了95%的准确率和F1-score，图像到图像检索和文本到图像检索的Recall@1分别为0.93和0.92，MRR分数为0.97和0.96，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括医疗影像分析、智能诊断系统和临床决策支持。通过提高内窥镜图像的分析能力，能够帮助医生更准确地进行诊断和治疗，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We present a unified vision-language framework tailored for ENT endoscopy image analysis that simultaneously tackles three clinically-relevant tasks: image classification, image-to-image retrieval, and text-to-image retrieval. Unlike conventional CNN-based pipelines that struggle to capture cross-modal semantics, our approach leverages the CLIP ViT-B/16 backbone and enhances it through Low-Rank Adaptation, multi-level CLS token aggregation, and spherical feature interpolation. These components collectively enable efficient fine-tuning on limited medical data while improving representation diversity and semantic alignment across modalities. To bridge the gap between visual inputs and textual diagnostic context, we introduce class-specific natural language prompts that guide the image encoder through a joint training objective combining supervised classification with contrastive learning. We validated our framework through participation in the ACM MM'25 ENTRep Grand Challenge, achieving 95% accuracy and F1-score in classification, Recall@1 of 0.93 and 0.92 for image-to-image and text-to-image retrieval respectively, and MRR scores of 0.97 and 0.96. Ablation studies demonstrated the incremental benefits of each architectural component, validating the effectiveness of our design for robust multimodal medical understanding in low-resource clinical settings.

