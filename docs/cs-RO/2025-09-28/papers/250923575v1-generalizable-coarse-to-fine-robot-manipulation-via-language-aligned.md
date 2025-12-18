---
layout: default
title: Generalizable Coarse-to-Fine Robot Manipulation via Language-Aligned 3D Keypoints
---

# Generalizable Coarse-to-Fine Robot Manipulation via Language-Aligned 3D Keypoints

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23575" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23575v1</a>
  <a href="https://arxiv.org/pdf/2509.23575.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23575v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23575v1', 'Generalizable Coarse-to-Fine Robot Manipulation via Language-Aligned 3D Keypoints')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianshu Hu, Lidi Wang, Shujia Li, Yunpeng Jiang, Xiao Li, Paul Weng, Yutong Ban

**分类**: cs.RO

**发布日期**: 2025-09-28

---

## 💡 一句话要点

**提出CLAP框架，通过语言对齐的3D关键点实现机器人操作的泛化**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人操作` `泛化能力` `视觉语言模型` `3D关键点` `粗细策略`

## 📋 核心要点

1. 分层粗细策略在机器人操作中具有潜力，但泛化性不足，难以应对新指令和环境。
2. CLAP框架通过任务分解、VLM微调和3D感知表示，提升策略对新指令和环境的泛化能力。
3. 实验表明，CLAP在泛化性能上优于现有方法，且训练样本需求更少，真实机器人实验验证了有效性。

## 📝 摘要（中文）

本文提出了一种名为Coarse-to-fine Language-Aligned manipulation Policy (CLAP) 的框架，旨在增强机器人3D操作任务中分层粗细策略的泛化能力。该框架集成了三个关键组件：任务分解、用于3D关键点预测的VLM微调和3D感知表示。通过在模拟和真实机器人上的综合实验，证明了其卓越的泛化能力。在GemBench基准测试中，CLAP的平均成功率比SOTA方法高出12％，同时仅使用1/5的训练轨迹。在真实世界的实验中，仅用10个演示训练的策略成功地泛化到新的指令和环境中。

## 🔬 方法详解

**问题定义**：现有分层粗细策略在机器人3D操作任务中，即使借助预训练模型，仍然面临泛化性问题。具体来说，模型难以适应新的操作指令和变化的环境，导致在实际应用中表现不佳。现有方法通常需要大量的训练数据才能达到较好的性能，这限制了其在资源受限场景下的应用。

**核心思路**：CLAP的核心思路是将语言信息与3D空间信息对齐，从而提升策略的泛化能力。通过微调视觉语言模型（VLM）来预测3D关键点，使得策略能够理解指令的语义，并将其映射到3D空间中的具体操作位置。同时，利用3D感知表示来增强策略对环境变化的鲁棒性。

**技术框架**：CLAP框架包含三个主要模块：1) 任务分解模块，将复杂的任务分解为一系列简单的子任务；2) VLM微调模块，利用视觉语言模型预测3D关键点，实现语言和3D空间的对齐；3) 3D感知表示模块，利用3D信息增强策略对环境变化的鲁棒性。整体流程是，首先利用任务分解模块将任务分解为子任务，然后利用VLM微调模块预测子任务对应的3D关键点，最后利用3D感知表示模块生成操作指令。

**关键创新**：CLAP最重要的技术创新点在于将视觉语言模型（VLM）引入到机器人操作任务中，并对其进行微调，使其能够预测3D关键点。这使得策略能够理解指令的语义，并将其映射到3D空间中的具体操作位置，从而显著提升了策略的泛化能力。与现有方法相比，CLAP不需要大量的训练数据，即可达到较好的性能。

**关键设计**：VLM微调模块的关键设计在于选择合适的VLM模型和微调策略。论文中具体使用的VLM模型和微调策略未知。3D感知表示模块的关键设计在于选择合适的3D表示方法和融合策略。论文中具体使用的3D表示方法和融合策略未知。损失函数的设计也至关重要，需要平衡关键点预测的准确性和操作指令的合理性。论文中损失函数的具体形式未知。

## 📊 实验亮点

CLAP在GemBench基准测试中，平均成功率比SOTA方法高出12％，同时仅使用1/5的训练轨迹。在真实世界的实验中，仅用10个演示训练的策略成功地泛化到新的指令和环境中。这些结果表明，CLAP在泛化性能和样本效率方面具有显著优势。

## 🎯 应用场景

该研究成果可应用于各种机器人操作任务，例如家庭服务机器人、工业机器人和医疗机器人。通过提升机器人操作的泛化能力，可以使其更好地适应不同的环境和任务需求，从而提高工作效率和降低成本。未来，该技术有望在自动化生产、智能家居和医疗辅助等领域发挥重要作用。

## 📄 摘要（原文）

> Hierarchical coarse-to-fine policy, where a coarse branch predicts a region of interest to guide a fine-grained action predictor, has demonstrated significant potential in robotic 3D manipulation tasks by especially enhancing sample efficiency and enabling more precise manipulation. However, even augmented with pre-trained models, these hierarchical policies still suffer from generalization issues. To enhance generalization to novel instructions and environment variations, we propose Coarse-to-fine Language-Aligned manipulation Policy (CLAP), a framework that integrates three key components: 1) task decomposition, 2) VLM fine-tuning for 3D keypoint prediction, and 3) 3D-aware representation. Through comprehensive experiments in simulation and on a real robot, we demonstrate its superior generalization capability. Specifically, on GemBench, a benchmark designed for evaluating generalization, our approach achieves a 12\% higher average success rate than the SOTA method while using only 1/5 of the training trajectories. In real-world experiments, our policy, trained on only 10 demonstrations, successfully generalizes to novel instructions and environments.

