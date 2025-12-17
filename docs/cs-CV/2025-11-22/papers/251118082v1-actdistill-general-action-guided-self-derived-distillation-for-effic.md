---
layout: default
title: ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models
---

# ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.18082" target="_blank" class="toolbar-btn">arXiv: 2511.18082v1</a>
    <a href="https://arxiv.org/pdf/2511.18082.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18082v1" 
            onclick="toggleFavorite(this, '2511.18082v1', 'ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Wencheng Ye, Tianshi Wang, Lei Zhu, Fengling Li, Guoli Yang

**分类**: cs.CV, cs.RO

**发布日期**: 2025-11-22

---

## 💡 一句话要点

**ActDistill：面向高效VLA模型的动作引导自蒸馏框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `视觉-语言-动作模型` `模型蒸馏` `知识迁移` `动作引导` `动态路由`

## 📋 核心要点

1. 现有的VLA模型计算开销大、推理延迟高，难以部署于机器人操作等实际场景。
2. ActDistill利用动作先验引导知识迁移和模型压缩，将大型VLA模型的动作预测能力迁移到轻量级模型。
3. 实验表明，ActDistill在显著降低计算量和推理延迟的同时，保持甚至提升了VLA模型的性能。

## 📝 摘要（中文）

本文提出ActDistill，一种通用的动作引导自蒸馏框架，旨在将现有视觉-语言-动作(VLA)模型的动作预测能力迁移到轻量级模型，从而降低计算开销和推理延迟。与以往侧重视觉-语言相关性的效率策略不同，ActDistill利用动作先验来指导知识迁移和模型压缩，实现VLA模型面向动作的效率提升。具体而言，该方法使用训练好的VLA模型作为教师，并引入图结构封装策略来显式建模动作预测的层级演化。从图封装的教师模型派生出的学生模型，配备了动态路由，可以根据动作预测需求自适应地选择计算路径，并在层级图信息的监督下平滑高效地演化。在推理阶段，移除图相关的辅助组件，学生模型仅执行动态路由的层，以最小的计算和延迟预测高精度动作。在具身智能基准测试上的实验表明，ActDistill在计算量减少50%以上，速度提升高达1.67倍的情况下，实现了与全尺寸VLA模型相当甚至更优的性能，从而为高效具身智能建立了一个通用范例。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作(VLA)模型虽然展现出强大的灵活性和泛化能力，但其庞大的计算开销和高推理延迟限制了它们在机器人操作等领域的实际应用。现有的模型压缩方法主要关注视觉和语言模态之间的相关性，忽略了动作预测本身的重要性。

**核心思路**：ActDistill的核心思想是利用动作先验知识来指导模型蒸馏和压缩，从而实现面向动作预测的高效VLA模型。通过将大型VLA模型的知识迁移到轻量级学生模型，并在训练过程中显式地建模动作预测的层级演化过程，使得学生模型能够以更少的计算资源实现与教师模型相当甚至更优的性能。

**技术框架**：ActDistill框架主要包含三个关键组件：教师模型、图结构封装策略和动态路由学生模型。首先，使用一个预训练好的VLA模型作为教师模型。然后，引入图结构封装策略来显式地建模教师模型中动作预测的层级演化过程，将教师模型封装成一个图结构。最后，基于该图结构，构建一个动态路由学生模型，该模型可以根据动作预测的需求自适应地选择计算路径。

**关键创新**：ActDistill的关键创新在于其动作引导的自蒸馏方法和图结构封装策略。传统的模型蒸馏方法通常只关注输入-输出之间的映射关系，而ActDistill则显式地利用了动作先验知识来指导知识迁移。图结构封装策略能够有效地建模动作预测的层级演化过程，从而使得学生模型能够更好地学习教师模型的知识。

**关键设计**：图结构封装策略将教师模型的每一层或几层组合成图中的节点，节点之间的连接表示信息传递关系。动态路由学生模型使用一个动态路由器来决定每一层应该选择哪条计算路径。损失函数包括模仿损失（模仿教师模型的输出）和图信息监督损失（鼓励学生模型学习图结构中的层级关系）。具体参数设置（如学习率、batch size等）和网络结构细节（如图的构建方式、动态路由器的设计等）未知。

## 📊 实验亮点

ActDistill在具身智能基准测试中表现出色，在计算量减少50%以上的情况下，实现了与全尺寸VLA模型相当甚至更优的性能。同时，推理速度提升高达1.67倍，证明了该方法在提高VLA模型效率方面的有效性。这些结果表明ActDistill为高效具身智能提供了一个有前景的解决方案。

## 🎯 应用场景

ActDistill具有广泛的应用前景，尤其是在资源受限的机器人操作、自动驾驶等领域。通过降低VLA模型的计算开销和推理延迟，可以使得这些模型能够更高效地部署在边缘设备上，从而实现更智能、更自主的机器人和自动驾驶系统。此外，该方法还可以应用于其他需要高效多模态理解和决策的任务中。

## 📄 摘要（原文）

> Recent Vision-Language-Action (VLA) models have shown impressive flexibility and generalization, yet their deployment in robotic manipulation remains limited by heavy computational overhead and inference latency. In this work, we present ActDistill, a general action-guided self-derived distillation framework that transfers the action prediction capability of any existing VLA model to a lightweight counterpart. Unlike previous efficiency strategies that primarily emphasize vision-language correlations, ActDistill leverages action priors to guide knowledge transfer and model compression, achieving action-oriented efficiency for VLA models. Specifically, we employ a well-trained VLA model as the teacher and introduce a graph-structured encapsulation strategy to explicitly model the hierarchical evolution of action prediction. The student model, derived from the graph-encapsulated teacher, is further equipped with a dynamic router that adaptively selects computation paths based on action prediction demands, guided by hierarchical graph-informed supervision to ensure smooth and efficient evolution. During inference, graph-related auxiliary components are removed, allowing the student to execute only dynamically routed layers and predict high-precision actions with minimal computation and latency. Experiments on embodied benchmarks demonstrate that ActDistill achieves comparable or superior performance to full-scale VLA models while reducing computation by over 50% with up to 1.67 times speedup, thereby establishing a general paradigm toward efficient embodied intelligence.

