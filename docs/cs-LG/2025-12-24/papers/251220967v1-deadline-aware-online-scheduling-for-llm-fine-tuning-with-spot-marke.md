---
layout: default
title: Deadline-Aware Online Scheduling for LLM Fine-Tuning with Spot Market Predictions
---

# Deadline-Aware Online Scheduling for LLM Fine-Tuning with Spot Market Predictions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20967" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20967v1</a>
  <a href="https://arxiv.org/pdf/2512.20967.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20967v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20967v1', 'Deadline-Aware Online Scheduling for LLM Fine-Tuning with Spot Market Predictions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Linggao Kong, Yuedong Xu, Lei Jiao, Chuan Xu

**分类**: cs.DC, cs.LG

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**提出基于预测的在线调度方法以优化LLM微调成本**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `在线调度` `现货市场` `LLM微调` `成本优化` `预测算法` `资源分配` `机器学习`

## 📋 核心要点

1. 现有方法在处理GPU现货实例的价格波动和可用性时面临挑战，导致微调成本高昂。
2. 论文提出了一种混合使用现货和按需实例的在线调度算法，利用价格和可用性预测来优化资源分配。
3. 实验结果显示，所提框架在不同市场动态下能够自适应选择最佳策略，性能提升显著，最高可达54.8%。

## 📝 摘要（中文）

随着基础模型规模的不断扩大，微调这些模型的成本也在增加。虽然GPU的现货实例提供了低成本的替代方案，但其价格和可用性的波动使得基于截止日期的调度变得尤为困难。本文通过混合使用现货和按需实例来解决这一问题。我们展示了现货市场中价格和可用性的可预测性，以及预测在实现成本高效调度中的重要性和对估计误差的敏感性。我们提出了一种基于承诺水平控制的方法的在线分配算法，并在预测不准确时提供了无预测的补充算法。实验结果表明，我们的在线框架能够在变化的现货市场动态和预测质量下自适应选择最佳策略，性能提升可达54.8%。

## 🔬 方法详解

**问题定义**：本文旨在解决在GPU现货市场中进行LLM微调时，由于价格波动和可用性不确定性导致的调度问题。现有方法未能有效利用现货实例的成本优势，导致资源利用率低下。

**核心思路**：论文提出了一种结合现货和按需实例的在线调度算法，利用对市场价格和可用性的预测来实现成本效益最大化。通过承诺水平控制的方法，算法能够在动态环境中做出更优决策。

**技术框架**：整体框架包括预测模块、在线分配算法和策略选择算法。预测模块负责估计价格和可用性，在线分配算法基于预测结果进行资源分配，而策略选择算法则从多种策略中学习最佳选择。

**关键创新**：最重要的创新在于提出了基于承诺水平的在线调度算法，能够在预测准确时提供更紧的性能界限，并在预测失误时切换到无预测的补充算法。这种灵活性是现有方法所不具备的。

**关键设计**：算法设计中包含了对承诺水平的设置，损失函数的选择，以及如何构建策略池以便进行在线学习。这些设计确保了算法在不同市场条件下的适应性和鲁棒性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20967v1/figure/throughput_vs_gpu_glm3.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20967v1/figure/throughput_vs_gpu_llama2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20967v1/figure/a100_avail.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，所提出的在线调度框架在不同的现货市场动态和预测质量下，能够自适应选择最佳策略，性能提升可达54.8%。与基线相比，算法在成本效益和资源利用率上表现出显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括大规模机器学习模型的训练和微调，尤其是在资源有限或成本敏感的环境中。通过优化调度策略，可以显著降低训练成本，提高资源利用率，推动AI技术的普及与应用。

## 📄 摘要（原文）

> As foundation models grow in size, fine-tuning them becomes increasingly expensive. While GPU spot instances offer a low-cost alternative to on-demand resources, their volatile prices and availability make deadline-aware scheduling particularly challenging. We tackle this difficulty by using a mix of spot and on-demand instances. Distinctively, we show the predictability of prices and availability in a spot instance market, the power of prediction in enabling cost-efficient scheduling and its sensitivity to estimation errors. An integer programming problem is formulated to capture the use of mixed instances under both the price and availability dynamics. We propose an online allocation algorithm with prediction based on the committed horizon control approach that leverages a \emph{commitment level} to enforce the partial sequence of decisions. When this prediction becomes inaccurate, we further present a complementary online algorithm without predictions. An online policy selection algorithm is developed that learns the best policy from a pool constructed by varying the parameters of both algorithms. We prove that the prediction-based algorithm achieves tighter performance bounds as prediction error decreases, while the policy selection algorithm possesses a regret bound of $\mathcal{O}(\sqrt{T})$. Experimental results demonstrate that our online framework can adaptively select the best policy under varying spot market dynamics and prediction quality, consistently outperforming baselines and improving utility by up to 54.8\%.

