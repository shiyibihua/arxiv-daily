---
layout: default
title: Flow Matching for Robust Simulation-Based Inference under Model Misspecification
---

# Flow Matching for Robust Simulation-Based Inference under Model Misspecification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23385" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23385v4</a>
  <a href="https://arxiv.org/pdf/2509.23385.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23385v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23385v4', 'Flow Matching for Robust Simulation-Based Inference under Model Misspecification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pierre-Louis Ruhlmann, Pedro L. C. Rodrigues, Michael Arbel, Florence Forbes

**分类**: stat.ML, cs.LG

**发布日期**: 2025-09-27 (更新: 2025-10-17)

---

## 💡 一句话要点

**提出FMCPE框架，利用Flow Matching提升SBI在模型失配下的鲁棒性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `基于模拟的推断` `模型失配` `Flow Matching` `后验估计` `鲁棒性`

## 📋 核心要点

1. 模型失配是SBI的关键挑战，模拟器与现实的差异导致后验估计偏差。
2. FMCPE利用Flow Matching，通过少量真实数据校正模拟训练的后验估计，无需显式建模失配。
3. 实验表明，FMCPE在合成和真实数据集上均能有效缓解模型失配，提高推断精度和不确定性校准。

## 📝 摘要（中文）

基于模拟的推断(SBI)通过模拟数据实现复杂非线性模型中的参数估计，正在改变实验科学。然而，一个持续存在的挑战是模型失配：模拟器只是对现实的近似，模拟数据和真实数据之间的不匹配会导致有偏差或过度自信的后验。我们通过引入Flow Matching Corrected Posterior Estimation (FMCPE)来解决这个问题，该框架利用flow matching范式，使用少量真实校准样本来细化模拟训练的后验估计器。我们的方法分两个阶段进行：首先，在大量模拟数据上训练后验近似器；其次，flow matching将其预测转移到真实观测支持的真实后验，而无需明确了解失配。这种设计使FMCPE能够将SBI的可扩展性与对分布偏移的鲁棒性相结合。在合成基准和真实世界数据集中，我们表明我们的提议始终减轻了失配的影响，与标准SBI基线相比，提供了改进的推断准确性和不确定性校准，同时保持了计算效率。

## 🔬 方法详解

**问题定义**：论文旨在解决在模型失配情况下，基于模拟的推断(SBI)的后验估计偏差问题。现有的SBI方法依赖于模拟器生成的数据，当模拟器与真实世界存在差异时，会导致推断结果不准确，置信度过高或过低。

**核心思路**：论文的核心思路是利用Flow Matching技术，将通过模拟数据训练得到的后验分布，通过学习一个连续的变换，将其“运输”到真实数据对应的后验分布。这种方法不需要显式地建模模拟器和真实世界之间的差异（即模型失配），而是直接学习分布之间的映射关系。

**技术框架**：FMCPE框架包含两个主要阶段：1) **模拟训练阶段**：使用大量的模拟数据训练一个初始的后验近似器。可以使用任何标准的SBI方法，例如神经网络。2) **Flow Matching校正阶段**：使用少量的真实数据，训练一个Flow Matching模型，该模型学习将模拟训练的后验分布映射到真实后验分布。Flow Matching通过学习一个时间依赖的向量场，定义了两个分布之间的连续轨迹。

**关键创新**：关键创新在于使用Flow Matching来校正模拟训练的后验分布，从而提高SBI在模型失配下的鲁棒性。与传统的领域自适应方法相比，FMCPE不需要显式地建模源域和目标域之间的差异，而是直接学习分布之间的映射关系，更加灵活和高效。此外，FMCPE只需要少量的真实数据即可实现有效的校正。

**关键设计**：Flow Matching模型通常使用神经网络实现，其目标是学习一个时间依赖的向量场，使得从模拟后验到真实后验的轨迹满足一定的条件。损失函数通常基于Flow Matching的目标，例如最小化向量场与真实轨迹之间的差异。具体网络结构和参数设置需要根据具体问题进行调整。论文中可能使用了特定的Flow Matching变体或优化技巧，具体细节未知。

## 📊 实验亮点

论文在合成数据集和真实数据集上验证了FMCPE的有效性。实验结果表明，FMCPE能够显著降低模型失配带来的偏差，提高后验估计的准确性和不确定性校准。与标准的SBI基线方法相比，FMCPE在推断精度上取得了显著提升，并且计算效率高，具有良好的可扩展性。具体提升幅度未知。

## 🎯 应用场景

FMCPE可广泛应用于需要基于模拟进行参数推断的领域，例如计算生物学、流行病学、气候科学和机器人学。在这些领域中，模拟器通常是对现实的简化，存在模型失配问题。FMCPE能够提高推断的准确性和可靠性，从而帮助科学家和工程师更好地理解和控制复杂系统，具有重要的实际价值和潜在的未来影响。

## 📄 摘要（原文）

> Simulation-based inference (SBI) is transforming experimental sciences by enabling parameter estimation in complex non-linear models from simulated data. A persistent challenge, however, is model misspecification: simulators are only approximations of reality, and mismatches between simulated and real data can yield biased or overconfident posteriors. We address this issue by introducing Flow Matching Corrected Posterior Estimation (FMCPE), a framework that leverages the flow matching paradigm to refine simulation-trained posterior estimators using a small set of real calibration samples. Our approach proceeds in two stages: first, a posterior approximator is trained on abundant simulated data; second, flow matching transports its predictions toward the true posterior supported by real observations, without requiring explicit knowledge of the misspecification. This design enables FMCPE to combine the scalability of SBI with robustness to distributional shift. Across synthetic benchmarks and real-world datasets, we show that our proposal consistently mitigates the effects of misspecification, delivering improved inference accuracy and uncertainty calibration compared to standard SBI baselines, while remaining computationally efficient.

