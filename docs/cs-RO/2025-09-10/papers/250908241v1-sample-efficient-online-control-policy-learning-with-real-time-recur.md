---
layout: default
title: Sample-Efficient Online Control Policy Learning with Real-Time Recursive Model Updates
---

# Sample-Efficient Online Control Policy Learning with Real-Time Recursive Model Updates

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08241" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08241v1</a>
  <a href="https://arxiv.org/pdf/2509.08241.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08241v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08241v1', 'Sample-Efficient Online Control Policy Learning with Real-Time Recursive Model Updates')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zixin Zhang, James Avtges, Todd D. Murphey

**分类**: cs.RO, eess.SY

**发布日期**: 2025-09-10

---

## 💡 一句话要点

**提出递归Koopman学习(RKL)，实现高样本效率的在线控制策略学习。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `Koopman理论` `在线学习` `递归学习` `数据驱动控制` `样本效率` `机器人控制` `非线性系统`

## 📋 核心要点

1. 现有数据驱动控制方法样本效率低，难以实时更新模型，限制了其在动态环境中的性能。
2. 利用Koopman理论将非线性系统线性化，提出递归Koopman学习(RKL)方法，实现快速模型更新。
3. 实验表明，RKL显著提高了样本效率和稳定性，所需数据量仅为基准方法的<10%。

## 📝 摘要（中文）

本文提出了一种高样本效率的基于Koopman理论的在线控制策略学习方法：递归Koopman学习(RKL)。针对数据驱动控制方法在数据获取和计算资源受限时，样本效率低和难以实时更新模型的问题，RKL利用Koopman理论将非线性系统表示为可观测空间上的线性模型，并可在优化友好的环境中从数据中确定Koopman表示，从而实现快速的模型更新。论文给出了模型收敛的充分条件，并提供了正式的算法分析，证明RKL是轻量级的且快速的，其复杂度与数据集大小无关。在模拟的平面二连杆机械臂和具有软执行器的混合非线性硬件系统上验证了该方法，结果表明，实时递归Koopman模型更新提高了数据驱动控制器合成的样本效率和稳定性，所需数据量仅为基准方法的<10%。该高性能C++代码库已开源。

## 🔬 方法详解

**问题定义**：现有数据驱动的控制方法，尤其是在硬件上学习时，面临着样本效率低和计算资源有限的挑战。许多方法需要大量的数据集，并且难以实时更新模型，这限制了它们在动态环境中的性能。因此，需要一种能够在少量数据下快速学习并适应环境变化的控制策略学习方法。

**核心思路**：论文的核心思路是利用Koopman理论将非线性系统表示为线性系统，从而简化模型学习和控制策略的设计。Koopman理论提供了一种将非线性动力系统嵌入到高维线性空间中的方法，使得可以使用线性系统理论来分析和控制非线性系统。通过递归地更新Koopman算子，可以实现对系统动态的实时跟踪和适应。

**技术框架**：RKL方法的整体框架包括以下几个主要步骤：1) 从环境中收集数据；2) 使用递归最小二乘法或其他在线学习算法来估计Koopman算子；3) 基于估计的Koopman算子设计控制器；4) 将控制器应用于系统，并重复上述步骤以不断改进模型和控制策略。该框架的关键在于Koopman算子的递归更新，这使得模型能够快速适应环境变化。

**关键创新**：该方法最重要的创新点在于其递归的Koopman算子学习方法，该方法能够以高样本效率和低计算成本实时更新模型。与传统的Koopman算子学习方法相比，RKL不需要存储整个数据集，而是可以增量式地更新模型，这使得它非常适合于在线学习和控制。此外，论文还提供了模型收敛的充分条件和算法分析，为该方法的理论基础提供了支持。

**关键设计**：RKL的关键设计包括：1) 使用递归最小二乘法来估计Koopman算子，该方法具有计算效率高和易于实现的优点；2) 选择合适的观测函数，观测函数的选择会影响Koopman算子的性能；3) 设计合适的控制器，例如线性二次调节器(LQR)，以实现对系统的稳定控制。论文还开源了高性能C++代码库，方便其他研究者使用和扩展该方法。

## 📊 实验亮点

实验结果表明，RKL在平面二连杆机械臂和具有软执行器的混合非线性硬件系统上均表现出优异的性能。与基准方法相比，RKL仅需<10%的数据即可实现相当甚至更好的控制性能，显著提高了样本效率。此外，RKL还表现出良好的稳定性和适应性，能够有效地应对环境变化和系统不确定性。

## 🎯 应用场景

该研究成果可应用于机器人控制、自动化系统、航空航天等领域。特别是在资源受限或环境动态变化的场景下，例如无人机编队、自主导航、以及软体机器人的控制，RKL能够实现快速、高效的在线学习和控制，具有重要的实际应用价值和广阔的应用前景。

## 📄 摘要（原文）

> Data-driven control methods need to be sample-efficient and lightweight, especially when data acquisition and computational resources are limited -- such as during learning on hardware. Most modern data-driven methods require large datasets and struggle with real-time updates of models, limiting their performance in dynamic environments. Koopman theory formally represents nonlinear systems as linear models over observables, and Koopman representations can be determined from data in an optimization-friendly setting with potentially rapid model updates. In this paper, we present a highly sample-efficient, Koopman-based learning pipeline: Recursive Koopman Learning (RKL). We identify sufficient conditions for model convergence and provide formal algorithmic analysis supporting our claim that RKL is lightweight and fast, with complexity independent of dataset size. We validate our method on a simulated planar two-link arm and a hybrid nonlinear hardware system with soft actuators, showing that real-time recursive Koopman model updates improve the sample efficiency and stability of data-driven controller synthesis -- requiring only <10% of the data compared to benchmarks. The high-performance C++ codebase is open-sourced. Website: https://www.zixinatom990.com/home/robotics/corl-2025-recursive-koopman-learning.

