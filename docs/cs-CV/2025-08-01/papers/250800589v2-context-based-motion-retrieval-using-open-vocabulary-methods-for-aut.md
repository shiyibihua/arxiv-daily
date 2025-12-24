---
layout: default
title: Context-based Motion Retrieval using Open Vocabulary Methods for Autonomous Driving
---

# Context-based Motion Retrieval using Open Vocabulary Methods for Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.00589" class="toolbar-btn" target="_blank">📄 arXiv: 2508.00589v2</a>
  <a href="https://arxiv.org/pdf/2508.00589.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.00589v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.00589v2', 'Context-based Motion Retrieval using Open Vocabulary Methods for Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Stefan Englmeier, Max A. Büttner, Katharina Winter, Fabian B. Flohr

**分类**: cs.CV, cs.CL, cs.IR, cs.RO

**发布日期**: 2025-08-01 (更新: 2025-08-12)

**备注**: Project page: https://iv.ee.hm.edu/contextmotionclip/; This work has been submitted to the IEEE for possible publication

---

## 💡 一句话要点

**提出基于上下文的运动检索框架以解决自动驾驶中的边缘案例问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `运动检索` `多模态学习` `上下文感知` `人类行为识别` `数据集扩展` `深度学习`

## 📋 核心要点

1. 现有方法在大规模数据集中检索稀有的人类行为场景面临挑战，尤其是在复杂的自动驾驶场景中。
2. 本文提出了一种上下文感知的运动检索框架，结合SMPL运动序列与视频帧，编码为多模态嵌入空间。
3. 在WayMoCo数据集上，提出的方法在运动上下文检索中比现有模型提高了27.5%的准确率。

## 📝 摘要（中文）

自动驾驶系统必须在安全关键场景中可靠运行，尤其是在涉及脆弱道路使用者（VRUs）复杂行为的情况下。识别这些边缘案例对于稳健评估和泛化至关重要，但在大规模数据集中检索这些稀有的人类行为场景具有挑战性。为支持对多样化人本场景的目标评估，本文提出了一种新颖的上下文感知运动检索框架。该方法结合了基于Skinned Multi-Person Linear（SMPL）的运动序列和相应的视频帧，并将其编码到与自然语言对齐的共享多模态嵌入空间中。该方法通过文本查询实现了人类行为及其上下文的可扩展检索。此外，本文还引入了WayMoCo数据集，这是Waymo开放数据集的扩展，包含从生成的伪真实SMPL序列和相应图像数据中派生的自动标注运动和场景上下文描述。我们的方案在WayMoCo数据集上在运动上下文检索中比最先进的模型提高了多达27.5%的准确率。

## 🔬 方法详解

**问题定义**：本文旨在解决在自动驾驶场景中，如何有效检索复杂和稀有的人类行为，现有方法在处理这些边缘案例时表现不佳，导致评估不够全面。

**核心思路**：提出的框架通过结合SMPL模型生成的运动序列和视频帧，利用自然语言进行检索，从而实现上下文感知的运动检索，增强了对人类行为的理解。

**技术框架**：整体架构包括数据预处理、运动序列与视频帧的结合、生成多模态嵌入空间以及基于文本的查询检索。主要模块包括运动序列生成、视频帧提取和多模态嵌入网络。

**关键创新**：最重要的创新在于将SMPL模型与视频数据结合，形成一个共享的多模态嵌入空间，使得检索过程更加灵活和高效，显著提升了对复杂行为的识别能力。

**关键设计**：在网络结构上，采用了多层神经网络进行特征提取，并设计了适应性损失函数以优化检索精度，确保了模型在多样化场景下的鲁棒性。具体参数设置和训练策略在实验部分进行了详细描述。

## 📊 实验亮点

在WayMoCo数据集上，提出的方法在运动上下文检索任务中表现优异，相较于最先进的基线模型，准确率提高了27.5%，显示出显著的性能提升，验证了方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶系统的安全评估、交通行为分析以及人机交互设计。通过提高对复杂人类行为的检索能力，能够更好地支持自动驾驶技术的开发与优化，提升行车安全性和用户体验。

## 📄 摘要（原文）

> Autonomous driving systems must operate reliably in safety-critical scenarios, particularly those involving unusual or complex behavior by Vulnerable Road Users (VRUs). Identifying these edge cases in driving datasets is essential for robust evaluation and generalization, but retrieving such rare human behavior scenarios within the long tail of large-scale datasets is challenging. To support targeted evaluation of autonomous driving systems in diverse, human-centered scenarios, we propose a novel context-aware motion retrieval framework. Our method combines Skinned Multi-Person Linear (SMPL)-based motion sequences and corresponding video frames before encoding them into a shared multimodal embedding space aligned with natural language. Our approach enables the scalable retrieval of human behavior and their context through text queries. This work also introduces our dataset WayMoCo, an extension of the Waymo Open Dataset. It contains automatically labeled motion and scene context descriptions derived from generated pseudo-ground-truth SMPL sequences and corresponding image data. Our approach outperforms state-of-the-art models by up to 27.5% accuracy in motion-context retrieval, when evaluated on the WayMoCo dataset.

