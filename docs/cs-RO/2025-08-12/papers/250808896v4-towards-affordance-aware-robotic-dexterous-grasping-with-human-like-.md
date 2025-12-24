---
layout: default
title: Towards Affordance-Aware Robotic Dexterous Grasping with Human-like Priors
---

# Towards Affordance-Aware Robotic Dexterous Grasping with Human-like Priors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08896" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08896v4</a>
  <a href="https://arxiv.org/pdf/2508.08896.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08896v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08896v4', 'Towards Affordance-Aware Robotic Dexterous Grasping with Human-like Priors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyu Zhao, Linghao Zhuang, Xingyue Zhao, Cheng Zeng, Haoran Xu, Yuming Jiang, Jun Cen, Kexiang Wang, Jiayan Guo, Siteng Huang, Xin Li, Deli Zhao, Hua Zou

**分类**: cs.RO

**发布日期**: 2025-08-12 (更新: 2025-11-11)

**备注**: AAAI 2026

---

## 💡 一句话要点

**提出AffordDex以解决机器人灵巧抓取中的人类姿态与功能适应性问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱五：交互与反应 (Interaction & Reaction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `灵巧抓取` `功能感知` `人类姿态` `机器人学习` `蒸馏训练` `运动先验` `残差学习`

## 📋 核心要点

1. 现有方法主要集中在低级抓取稳定性指标，忽视了物体功能感知和人类姿态的适应性，限制了灵巧抓取的有效性。
2. AffordDex框架通过两阶段训练，首先在大量人类手部动作上进行预训练，然后通过残差模块适应特定物体实例，提升抓取策略的自然性和适应性。
3. 实验结果显示，AffordDex在已见物体、未见实例和全新类别上均显著超越了现有最先进基线，展示了其优越的抓取能力和人类特征。

## 📝 摘要（中文）

灵巧手能够对物体进行通用抓取是通用嵌入式人工智能发展的基础。然而，现有方法过于关注低级抓取稳定性指标，忽视了对物体功能的理解和人类姿态的重要性。为了解决这些局限性，我们提出了AffordDex，一个新颖的框架，通过两阶段训练学习具有运动先验和物体功能理解的通用抓取策略。第一阶段，轨迹模仿器在大量人类手部动作上进行预训练，以建立自然运动的强先验。第二阶段，残差模块被训练以将这些通用的人类动作适应于特定物体实例。该过程由负向功能感知分割模块和特权教师-学生蒸馏过程指导，确保最终的视觉基础策略成功。大量实验表明，AffordDex不仅实现了通用灵巧抓取，还在姿态上保持了人类特征，并在接触位置上功能适当。

## 🔬 方法详解

**问题定义**：本论文旨在解决机器人灵巧抓取中对物体功能感知和人类姿态适应性的不足。现有方法过于关注抓取的稳定性，未能有效考虑抓取动作的自然性和适用性。

**核心思路**：论文提出的AffordDex框架通过两阶段训练，首先利用人类手部动作的先验知识进行预训练，然后通过残差模块将这些动作适应于特定物体实例，从而提升抓取的灵活性和适应性。

**技术框架**：整体架构包括两个主要阶段：第一阶段是轨迹模仿器的预训练，第二阶段是残差模块的训练。关键模块包括负向功能感知分割模块和教师-学生蒸馏过程，确保抓取策略的成功。

**关键创新**：AffordDex的核心创新在于结合了人类动作的先验知识和物体功能感知，通过负向功能感知分割模块识别不适合的接触区域，显著提升了抓取的自然性和有效性。

**关键设计**：在设计中，使用了大量人类手部动作数据进行预训练，损失函数结合了抓取成功率和接触区域的适当性，网络结构采用了残差学习以增强模型的适应能力。

## 📊 实验亮点

实验结果表明，AffordDex在灵巧抓取任务中表现优异，尤其在处理未见实例和全新类别时，抓取成功率显著提高，超越了现有最先进的基线，展示了其在通用性和适应性方面的优势。

## 🎯 应用场景

该研究在机器人抓取、自动化制造和人机交互等领域具有广泛的应用潜力。通过提升机器人对物体功能的理解和自然抓取能力，AffordDex能够推动智能机器人在复杂环境中的应用，提升其操作的灵活性和效率。

## 📄 摘要（原文）

> A dexterous hand capable of generalizable grasping objects is fundamental for the development of general-purpose embodied AI. However, previous methods focus narrowly on low-level grasp stability metrics, neglecting affordance-aware positioning and human-like poses which are crucial for downstream manipulation. To address these limitations, we propose AffordDex, a novel framework with two-stage training that learns a universal grasping policy with an inherent understanding of both motion priors and object affordances. In the first stage, a trajectory imitator is pre-trained on a large corpus of human hand motions to instill a strong prior for natural movement. In the second stage, a residual module is trained to adapt these general human-like motions to specific object instances. This refinement is critically guided by two components: our Negative Affordance-aware Segmentation (NAA) module, which identifies functionally inappropriate contact regions, and a privileged teacher-student distillation process that ensures the final vision-based policy is highly successful. Extensive experiments demonstrate that AffordDex not only achieves universal dexterous grasping but also remains remarkably human-like in posture and functionally appropriate in contact location. As a result, AffordDex significantly outperforms state-of-the-art baselines across seen objects, unseen instances, and even entirely novel categories.

