---
layout: default
title: Unregularized Linear Convergence in Zero-Sum Game from Preference Feedback
---

# Unregularized Linear Convergence in Zero-Sum Game from Preference Feedback

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24818" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24818v1</a>
  <a href="https://arxiv.org/pdf/2512.24818.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24818v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24818v1', 'Unregularized Linear Convergence in Zero-Sum Game from Preference Feedback')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shulun Chen, Runlong Zhou, Zihan Zhang, Maryam Fazel, Simon S. Du

**分类**: cs.LG

**发布日期**: 2025-12-31

**备注**: 28 pages

---

## 💡 一句话要点

**提出无正则化的OMWU算法，解决偏好反馈零和博弈中的线性收敛问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `偏好学习` `零和博弈` `纳什均衡` `乐观乘性权重更新` `线性收敛` `无正则化` `大型语言模型对齐` `人类反馈`

## 📋 核心要点

1. 现有基于Bradley-Terry模型的偏好学习方法假设传递性，无法有效处理人类偏好的复杂性。
2. 论文提出使用乐观乘性权重更新（OMWU）算法，在无正则化的情况下寻找零和博弈的纳什均衡。
3. 实验结果表明，OMWU算法在表格和神经策略类中均表现出良好的收敛性，并具备应用于LLM的潜力。

## 📝 摘要（中文）

将大型语言模型（LLM）与人类偏好对齐已被证明能有效提升模型能力。然而，使用Bradley-Terry模型的标准偏好建模假设传递性，忽略了人类群体偏好的内在复杂性。从人类反馈中进行纳什学习（NLHF）通过将非传递偏好构建为双人零和博弈来解决这个问题，其中对齐简化为寻找纳什均衡（NE）。然而，现有算法通常依赖于正则化，在计算原始博弈中的对偶间隙时会产生不可避免的偏差。本文为NLHF中的乐观乘性权重更新（OMWU）提供了首个收敛保证，表明只要存在具有完全支持的NE，它就能在burn-in阶段后实现最后一次迭代的线性收敛，并具有实例相关的线性收敛速度到原始NE，通过对偶间隙衡量。与Wei等人（2020）的先前结果相比，我们不需要NE唯一性的假设。我们的分析确定了一种新的边际收敛行为，其中很少采取的行动的概率从指数小的数值呈指数增长，从而实现了比先前结果更好的实例相关常数的指数依赖性。实验证实了OMWU在表格和神经策略类中的理论优势，证明了其在LLM应用中的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决从人类偏好反馈中学习策略的问题，特别是当人类偏好不满足传递性时。现有的方法通常采用正则化技术来保证算法的收敛性，但正则化会引入偏差，影响最终策略的准确性。此外，现有方法通常需要纳什均衡唯一性的假设，限制了其适用范围。

**核心思路**：论文的核心思路是将人类偏好学习问题建模为一个双人零和博弈，并使用乐观乘性权重更新（OMWU）算法来寻找纳什均衡。OMWU算法是一种无正则化的算法，可以避免正则化带来的偏差。此外，论文证明了OMWU算法在纳什均衡不唯一的情况下也能收敛。

**技术框架**：论文的技术框架主要包括以下几个部分：1) 将人类偏好建模为双人零和博弈；2) 使用OMWU算法更新策略；3) 分析OMWU算法的收敛性。具体来说，论文首先定义了一个 payoff 矩阵，用于表示不同策略组合下的收益。然后，使用OMWU算法迭代更新两个玩家的策略，使其逐渐逼近纳什均衡。最后，论文通过理论分析证明了OMWU算法的线性收敛性。

**关键创新**：论文的关键创新在于：1) 提出了无正则化的OMWU算法，避免了正则化带来的偏差；2) 证明了OMWU算法在纳什均衡不唯一的情况下也能收敛；3) 发现了一种新的边际收敛行为，即很少采取的行动的概率从指数小的数值呈指数增长，从而实现了更好的实例相关常数的指数依赖性。

**关键设计**：论文的关键设计包括：1) OMWU算法的学习率参数设置；2) payoff 矩阵的构建方式；3) 收敛性分析中使用的 Lyapunov 函数的设计。具体来说，论文选择合适的学习率参数，以保证算法的收敛速度和稳定性。Payoff 矩阵的构建方式直接影响到博弈的性质和纳什均衡的存在性。Lyapunov 函数的设计是收敛性分析的关键，论文设计了一个合适的 Lyapunov 函数，证明了OMWU算法的线性收敛性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24818v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24818v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24818v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文证明了OMWU算法在NLHF中实现了最后一次迭代的线性收敛，且不需要纳什均衡唯一性的假设。与现有方法相比，OMWU算法避免了正则化带来的偏差，并实现了更好的实例相关常数的指数依赖性。实验结果验证了OMWU算法在表格和神经策略类中的有效性。

## 🎯 应用场景

该研究成果可应用于大型语言模型的对齐，通过人类偏好反馈训练模型，使其更好地符合人类价值观和需求。此外，该方法还可应用于推荐系统、强化学习等领域，解决非传递偏好下的策略学习问题，提升系统的性能和用户体验。未来，该研究有望推动人工智能技术在更广泛领域的应用。

## 📄 摘要（原文）

> Aligning large language models (LLMs) with human preferences has proven effective for enhancing model capabilities, yet standard preference modeling using the Bradley-Terry model assumes transitivity, overlooking the inherent complexity of human population preferences. Nash learning from human feedback (NLHF) addresses this by framing non-transitive preferences as a two-player zero-sum game, where alignment reduces to finding the Nash equilibrium (NE). However, existing algorithms typically rely on regularization, incurring unavoidable bias when computing the duality gap in the original game. In this work, we provide the first convergence guarantee for Optimistic Multiplicative Weights Update ($\mathtt{OMWU}$) in NLHF, showing that it achieves last-iterate linear convergence after a burn-in phase whenever an NE with full support exists, with an instance-dependent linear convergence rate to the original NE, measured by duality gaps. Compared to prior results in Wei et al. (2020), we do not require the assumption of NE uniqueness. Our analysis identifies a novel marginal convergence behavior, where the probability of rarely played actions grows exponentially from exponentially small values, enabling exponentially better dependence on instance-dependent constants than prior results. Experiments corroborate the theoretical strengths of $\mathtt{OMWU}$ in both tabular and neural policy classes, demonstrating its potential for LLM applications.

