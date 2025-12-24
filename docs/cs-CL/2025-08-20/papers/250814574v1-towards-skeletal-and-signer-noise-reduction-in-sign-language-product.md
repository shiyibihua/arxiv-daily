---
layout: default
title: Towards Skeletal and Signer Noise Reduction in Sign Language Production via Quaternion-Based Pose Encoding and Contrastive Learning
---

# Towards Skeletal and Signer Noise Reduction in Sign Language Production via Quaternion-Based Pose Encoding and Contrastive Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14574" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14574v1</a>
  <a href="https://arxiv.org/pdf/2508.14574.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14574v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14574v1', 'Towards Skeletal and Signer Noise Reduction in Sign Language Production via Quaternion-Based Pose Encoding and Contrastive Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guilhem Fauré, Mostafa Sadeghi, Sam Bigeard, Slim Ouni

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-20

**期刊**: SLTAT 2025: 9th Workshop on Sign Language Translation and Avatar Technologies, Sep 2025, Berlin, Germany

---

## 💡 一句话要点

**提出基于四元数的姿态编码与对比学习以减少手语生成中的噪声**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `手语生成` `四元数编码` `对比学习` `渐进式变换器` `姿态识别` `语义相似性` `深度学习`

## 📋 核心要点

1. 手语生成中的高类内变异性导致模型鲁棒性不足，现有方法难以处理不同签署者的风格差异。
2. 本文提出通过四元数编码姿态和对比损失来增强渐进式变换器架构，提高手语生成的准确性和清晰度。
3. 在Phoenix14T数据集上，结合新方法的模型在关键点概率和骨角误差上均有显著提升，验证了方法的有效性。

## 📝 摘要（中文）

手语生成（SLP）中的主要挑战之一是手势的高类内变异性，这源于签署者的形态特征和训练数据中的风格多样性。为提高对这些变异的鲁棒性，本文对标准的渐进式变换器架构进行了两项增强：首先，使用四元数空间中的骨骼旋转编码姿态，并通过测地损失训练，以提高关节运动的准确性和清晰度；其次，引入对比损失，通过语义相似性结构化解码器嵌入，旨在过滤掉不传达相关语义信息的解剖和风格特征。在Phoenix14T数据集上，仅对比损失就使得正确关键点概率提高了16%。结合四元数姿态编码后，模型的平均骨角误差减少了6%。这些结果表明，将骨骼结构建模和语义引导的对比目标纳入基于变换器的SLP模型训练中具有显著益处。

## 🔬 方法详解

**问题定义**：手语生成（SLP）面临的主要问题是高类内变异性，导致模型在不同签署者的手势表现上缺乏鲁棒性，现有方法未能有效解决这一挑战。

**核心思路**：本文提出通过四元数编码来表示骨骼姿态，并结合对比损失来优化解码器嵌入，从而提高手语生成的准确性和语义一致性。

**技术框架**：整体架构基于渐进式变换器，主要模块包括四元数姿态编码模块和对比损失模块。四元数模块负责将关节旋转信息转化为四元数表示，而对比损失模块则通过语义相似性来优化模型输出。

**关键创新**：最重要的创新在于引入四元数空间的姿态编码和对比损失，这与传统的欧几里得空间表示和简单的损失函数有本质区别，能够更好地捕捉关节运动的细微变化。

**关键设计**：在损失函数设计上，采用测地损失来优化四元数表示的准确性，同时使用基于语义相似性的对比损失来增强解码器的语义结构，确保模型输出的手势在语义上更为一致。

## 📊 实验亮点

实验结果表明，仅对比损失就使得正确关键点概率提高了16%，而结合四元数编码后，模型的平均骨角误差减少了6%。这些结果显著优于基线模型，验证了新方法在手语生成中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括手语翻译、虚拟现实中的手势交互以及辅助沟通工具的开发。通过提高手语生成的准确性和鲁棒性，能够更好地服务于听障人士，促进人机交互的无障碍性。未来，该方法还可能扩展到其他需要姿态识别的领域，如运动分析和人机协作。

## 📄 摘要（原文）

> One of the main challenges in neural sign language production (SLP) lies in the high intra-class variability of signs, arising from signer morphology and stylistic variety in the training data. To improve robustness to such variations, we propose two enhancements to the standard Progressive Transformers (PT) architecture (Saunders et al., 2020). First, we encode poses using bone rotations in quaternion space and train with a geodesic loss to improve the accuracy and clarity of angular joint movements. Second, we introduce a contrastive loss to structure decoder embeddings by semantic similarity, using either gloss overlap or SBERT-based sentence similarity, aiming to filter out anatomical and stylistic features that do not convey relevant semantic information. On the Phoenix14T dataset, the contrastive loss alone yields a 16% improvement in Probability of Correct Keypoint over the PT baseline. When combined with quaternion-based pose encoding, the model achieves a 6% reduction in Mean Bone Angle Error. These results point to the benefit of incorporating skeletal structure modeling and semantically guided contrastive objectives on sign pose representations into the training of Transformer-based SLP models.

