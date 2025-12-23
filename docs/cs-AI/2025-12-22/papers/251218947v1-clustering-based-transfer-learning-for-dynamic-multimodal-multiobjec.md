---
layout: default
title: Clustering-based Transfer Learning for Dynamic Multimodal MultiObjective Evolutionary Algorithm
---

# Clustering-based Transfer Learning for Dynamic Multimodal MultiObjective Evolutionary Algorithm

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.18947" class="toolbar-btn" target="_blank">📄 arXiv: 2512.18947v1</a>
  <a href="https://arxiv.org/pdf/2512.18947.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.18947v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.18947v1', 'Clustering-based Transfer Learning for Dynamic Multimodal MultiObjective Evolutionary Algorithm')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Li Yan, Bolun Liu, Chao Li, Jing Liang, Kunjie Yu, Caitong Yue, Xuzhao Chai, Boyang Qu

**分类**: cs.AI, cs.NE

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**提出基于聚类迁移学习的动态多模态多目标进化算法，解决动态环境下的多模态优化问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `动态多目标优化` `多模态优化` `进化算法` `迁移学习` `聚类` `自编码器` `动态环境`

## 📋 核心要点

1. 现有动态多目标进化算法忽略解的模态，静态多模态算法缺乏对动态环境的适应性，难以同时跟踪多个最优解并保持种群多样性。
2. 提出基于聚类的自编码器预测动态响应机制，利用自编码器处理聚类生成多样化初始种群，并结合自适应小生境策略平衡收敛性和多样性。
3. 在12个动态多模态测试函数上的实验表明，该算法在决策空间和目标空间均优于现有算法，能有效保持种群多样性并实现更好的收敛性。

## 📝 摘要（中文）

本文针对动态多模态多目标优化问题，该问题需要在时变环境中同时跟踪多个等价的帕累托最优集并保持种群多样性。现有动态多目标进化算法通常忽略解的模态，而静态多模态多目标进化算法缺乏对动态变化的适应性。为了解决上述挑战，本文做出了两个主要贡献。首先，我们构建了一个新的动态多模态多目标测试函数基准套件，该套件融合了动态和多模态优化的特性，以建立一个严格的评估平台。其次，我们提出了一种以基于聚类的自编码器预测动态响应机制为中心的新算法，该算法利用自编码器模型处理匹配的聚类以生成高度多样化的初始种群。此外，为了平衡算法的收敛性和多样性，我们将自适应小生境策略集成到静态优化器中。在12个动态多模态多目标测试函数实例上的经验分析表明，与几种最先进的动态多目标进化算法和多模态多目标进化算法相比，我们的算法不仅在决策空间中更有效地保持了种群多样性，而且在目标空间中实现了卓越的收敛性。

## 🔬 方法详解

**问题定义**：动态多模态多目标优化问题（DMMOP）旨在解决环境随时间变化时，同时优化多个目标并找到多个等价的帕累托最优解集的问题。现有方法的痛点在于，动态多目标进化算法（DMOEAs）通常忽略解的模态信息，导致难以维持种群多样性；而静态多模态多目标进化算法（MMOEAs）则缺乏对动态环境的适应性，无法有效跟踪最优解的变化。

**核心思路**：本文的核心思路是利用聚类和迁移学习的思想，通过自编码器学习历史环境中的解分布信息，并在新环境中生成具有多样性的初始种群。具体来说，首先对历史种群进行聚类，然后训练自编码器学习每个簇的特征表示，最后在新环境中，利用自编码器生成新的种群，并结合自适应小生境策略来平衡算法的收敛性和多样性。这样设计的目的是为了充分利用历史信息，加速算法的收敛速度，并维持种群的多样性，从而更好地适应动态环境的变化。

**技术框架**：该算法主要包含以下几个阶段：1) **环境变化检测**：检测环境是否发生变化。2) **聚类与自编码器训练**：对历史种群进行聚类，并训练自编码器学习每个簇的特征表示。3) **种群初始化**：在新环境中，利用训练好的自编码器生成新的种群。4) **自适应小生境优化**：利用自适应小生境策略对种群进行优化，平衡算法的收敛性和多样性。5) **种群更新**：根据环境变化情况，更新种群和自编码器模型。

**关键创新**：该算法的关键创新在于：1) 提出了基于聚类的自编码器预测动态响应机制，能够有效地利用历史信息生成具有多样性的初始种群。2) 将自适应小生境策略集成到静态优化器中，从而更好地平衡算法的收敛性和多样性。3) 构建了一个新的动态多模态多目标测试函数基准套件，为该领域的研究提供了一个严格的评估平台。

**关键设计**：在聚类方面，可以使用K-means等算法。自编码器的网络结构可以根据具体问题进行调整，损失函数可以使用均方误差等。自适应小生境策略的关键在于如何动态调整小生境半径，以平衡算法的收敛性和多样性。具体的参数设置需要根据实验结果进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18947v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18947v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18947v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该算法在12个动态多模态多目标测试函数实例上，与几种最先进的DMOEAs和MMOEAs相比，不仅在决策空间中更有效地保持了种群多样性，而且在目标空间中实现了卓越的收敛性。具体性能提升数据在论文中给出，证明了该算法在解决DMMOP问题上的有效性。

## 🎯 应用场景

该研究成果可应用于需要动态优化和维持多个最优解的实际问题，例如：动态资源调度、机器人路径规划、电力系统优化、金融投资组合优化等。通过快速适应环境变化并保持解的多样性，可以提高决策效率和鲁棒性，从而在动态环境中获得更好的性能。

## 📄 摘要（原文）

> Dynamic multimodal multiobjective optimization presents the dual challenge of simultaneously tracking multiple equivalent pareto optimal sets and maintaining population diversity in time-varying environments. However, existing dynamic multiobjective evolutionary algorithms often neglect solution modality, whereas static multimodal multiobjective evolutionary algorithms lack adaptability to dynamic changes. To address above challenge, this paper makes two primary contributions. First, we introduce a new benchmark suite of dynamic multimodal multiobjective test functions constructed by fusing the properties of both dynamic and multimodal optimization to establish a rigorous evaluation platform. Second, we propose a novel algorithm centered on a Clustering-based Autoencoder prediction dynamic response mechanism, which utilizes an autoencoder model to process matched clusters to generate a highly diverse initial population. Furthermore, to balance the algorithm's convergence and diversity, we integrate an adaptive niching strategy into the static optimizer. Empirical analysis on 12 instances of dynamic multimodal multiobjective test functions reveals that, compared with several state-of-the-art dynamic multiobjective evolutionary algorithms and multimodal multiobjective evolutionary algorithms, our algorithm not only preserves population diversity more effectively in the decision space but also achieves superior convergence in the objective space.

