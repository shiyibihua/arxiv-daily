---
layout: default
title: Explicit and Non-asymptotic Query Complexities of Rank-Based Zeroth-order Algorithm on Stochastic Smooth Functions
---

# Explicit and Non-asymptotic Query Complexities of Rank-Based Zeroth-order Algorithm on Stochastic Smooth Functions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19104" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19104v1</a>
  <a href="https://arxiv.org/pdf/2512.19104.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19104v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19104v1', 'Explicit and Non-asymptotic Query Complexities of Rank-Based Zeroth-order Algorithm on Stochastic Smooth Functions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haishan Ye

**分类**: math.OC, cs.LG

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**提出基于排序的零阶算法，解决随机光滑函数优化问题，达到最优查询效率。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `零阶优化` `序数反馈` `随机优化` `查询复杂度` `人机交互`

## 📋 核心要点

1. 现有零阶优化算法在处理序数反馈和随机目标时，理论理解有限，尤其是在标准光滑性假设下。
2. 论文提出一种基于排序的零阶算法，利用序数信息实现优化，关注算法的查询复杂度。
3. 结果表明，该算法在随机环境下，仅使用序数信息即可达到与基于价值的算法相同的最优查询效率。

## 📝 摘要（中文）

本文研究了随机函数的基于排序的零阶优化问题，其中仅能获得随机函数的序数反馈。针对此问题，提出了一种简单且计算高效的基于排序的零阶算法。在包括光滑性、强凸性和随机梯度的有界二阶矩等标准假设下，建立了凸和非凸目标的显式非渐近查询复杂度界限。值得注意的是，我们的结果与基于价值的零阶算法的最佳已知查询复杂度相匹配，表明仅凭序数信息就足以在随机环境中实现最佳查询效率。我们的分析不同于现有的基于漂移和信息几何的技术，为噪声下的基于排序的优化研究提供了新的工具。这些发现缩小了理论与实践之间的差距，并为人类偏好驱动的优化提供了原则性基础。

## 🔬 方法详解

**问题定义**：论文旨在解决随机光滑函数的零阶优化问题，该问题仅能获得函数的序数反馈（例如，排序或偏好）。现有基于价值的零阶优化算法虽然有效，但在序数反馈场景下，理论分析较为复杂，且可能无法充分利用序数信息的优势。此外，在随机环境下，如何保证算法的查询效率也是一个挑战。

**核心思路**：论文的核心思路是设计一种基于排序的零阶算法，该算法直接利用序数信息进行优化，避免了对函数值的直接估计。通过比较不同样本点的函数值排序，算法可以推断出梯度方向，从而进行优化。这种方法可以更好地适应序数反馈的特点，并提高算法的鲁棒性。

**技术框架**：该算法主要包含以下几个阶段：1）样本点生成：在当前解的邻域内随机生成一组样本点。2）序数反馈获取：通过某种方式（例如，人类反馈或模拟器）获取这些样本点的函数值排序。3）梯度估计：基于样本点的排序信息，估计梯度方向。4）解更新：沿着估计的梯度方向更新当前解。5）重复上述步骤，直到满足停止条件。

**关键创新**：论文的关键创新在于提出了一种新的基于排序的梯度估计方法，该方法能够有效地利用序数信息，并具有较好的鲁棒性。此外，论文还对算法的查询复杂度进行了详细的理论分析，证明了该算法在随机环境下可以达到最优的查询效率。

**关键设计**：算法的关键设计包括：1）样本点生成策略：采用合适的采样分布，以保证样本点的多样性。2）梯度估计方法：设计一种能够有效利用序数信息的梯度估计方法，例如，基于排序的平均梯度估计。3）步长选择策略：采用自适应步长选择策略，以保证算法的收敛性。4）停止条件：设置合理的停止条件，以避免过度优化。

## 📊 实验亮点

论文的主要实验结果是建立了凸和非凸目标的显式非渐近查询复杂度界限。结果表明，该算法在随机环境下，仅使用序数信息即可达到与基于价值的零阶算法相同的最优查询复杂度。这表明序数信息在随机优化中具有重要的价值，并且该算法具有较好的实用性。

## 🎯 应用场景

该研究成果可应用于人机交互、强化学习、推荐系统等领域。例如，在强化学习中，可以利用人类反馈的偏好信息来指导智能体的学习，从而提高学习效率和性能。在推荐系统中，可以利用用户的排序信息来优化推荐结果，从而提高用户满意度。此外，该算法还可以应用于进化策略等优化问题中。

## 📄 摘要（原文）

> Zeroth-order (ZO) optimization with ordinal feedback has emerged as a fundamental problem in modern machine learning systems, particularly in human-in-the-loop settings such as reinforcement learning from human feedback, preference learning, and evolutionary strategies. While rank-based ZO algorithms enjoy strong empirical success and robustness properties, their theoretical understanding, especially under stochastic objectives and standard smoothness assumptions, remains limited. In this paper, we study rank-based zeroth-order optimization for stochastic functions where only ordinal feedback of the stochastic function is available. We propose a simple and computationally efficient rank-based ZO algorithm. Under standard assumptions including smoothness, strong convexity, and bounded second moments of stochastic gradients, we establish explicit non-asymptotic query complexity bounds for both convex and nonconvex objectives. Notably, our results match the best-known query complexities of value-based ZO algorithms, demonstrating that ordinal information alone is sufficient for optimal query efficiency in stochastic settings. Our analysis departs from existing drift-based and information-geometric techniques, offering new tools for the study of rank-based optimization under noise. These findings narrow the gap between theory and practice and provide a principled foundation for optimization driven by human preferences.

