---
layout: default
title: On the Gaussian Limit of the Output of IIR Filters
---

# On the Gaussian Limit of the Output of IIR Filters

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12705" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12705v2</a>
  <a href="https://arxiv.org/pdf/2508.12705.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12705v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12705v2', 'On the Gaussian Limit of the Output of IIR Filters')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yashaswini Murthy, Bassam Bamieh, R. Srikant

**分类**: eess.SY, eess.SP

**发布日期**: 2025-08-18 (更新: 2025-10-01)

**备注**: 8 pages, 1 figure, accepted for publication IEEE Conference on Decision and Control 2025

---

## 💡 一句话要点

**研究稳定LTI系统输出的高斯极限特性**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `高斯极限` `LTI系统` `非高斯输入` `Wasserstein距离` `Stein方法` `渐近分析` `信号处理`

## 📋 核心要点

1. 现有研究对非高斯输入驱动的LTI系统输出的渐近性质缺乏严格的理论支持，导致对输出高斯性的理解不够深入。
2. 论文通过引入Wasserstein-1距离，系统性地分析了在特定条件下输出如何趋近于高斯分布，提供了新的理论框架。
3. 研究表明，当系统主极点接近稳定边缘时，输出以特定速率收敛到标准正态分布，验证了理论的有效性。

## 📝 摘要（中文）

本研究探讨了由非高斯随机输入驱动的稳定线性时不变（LTI）系统输出的渐近分布。我们严格界定了在输入不为高斯时，输出过程何时近似高斯。通过使用Wasserstein-1距离作为非高斯性的量化指标，我们推导了适当缩放的输出与标准正态分布之间距离的上界。这些界限通过Stein方法获得，并明确依赖于系统的脉冲响应和输入过程的依赖结构。我们展示了在系统的主极点接近稳定边缘时，输出以$O(1/	ext{sqrt}{t})$的速率收敛到标准正态分布。我们还提供了收敛失败的反例，从而激励了所述假设的提出。我们的结果为低通LTI系统输出近似高斯的广泛观察提供了严格基础。

## 🔬 方法详解

**问题定义**：本论文旨在解决稳定LTI系统在非高斯随机输入驱动下输出的渐近分布特性，现有方法未能提供足够的理论支持，导致对输出高斯性的理解不足。

**核心思路**：论文通过引入Wasserstein-1距离作为量化非高斯性的指标，严格界定了输出何时近似高斯，并推导了输出与标准正态分布之间的距离上界。

**技术框架**：整体研究框架包括对系统脉冲响应的分析、输入过程的依赖结构的考量，以及通过Stein方法推导的理论结果，形成了一个系统的理论分析流程。

**关键创新**：最重要的技术创新在于通过Wasserstein-1距离提供了一个量化非高斯性的工具，并明确了系统主极点与输入依赖结构对输出高斯性的影响，这与现有方法的定性分析形成了鲜明对比。

**关键设计**：研究中对系统的脉冲响应和输入过程的相关性进行了详细分析，特别是对主极点接近稳定边缘的条件进行了深入探讨，确保了理论推导的严谨性。

## 📊 实验亮点

实验结果表明，当系统主极点接近稳定边缘且输入满足特定条件时，输出以$O(1/	ext{sqrt}{t})$的速率收敛到标准正态分布。这一发现为低通LTI系统输出近似高斯的现象提供了理论支持，验证了理论的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括信号处理、控制系统设计和通信系统等，能够为设计低通滤波器和其他LTI系统提供理论依据，提升系统的性能和可靠性。未来，该理论框架可能会影响更广泛的随机过程分析和系统设计领域。

## 📄 摘要（原文）

> We study the asymptotic distribution of the output of a stable Linear Time-Invariant (LTI) system driven by a non-Gaussian stochastic input. Motivated by longstanding heuristics in the stochastic describing function method, we rigorously characterize when the output process becomes approximately Gaussian, even when the input is not. Using the Wasserstein-1 distance as a quantitative measure of non-Gaussianity, we derive upper bounds on the distance between the appropriately scaled output and a standard normal distribution. These bounds are obtained via Stein's method and depend explicitly on the system's impulse response and the dependence structure of the input process. We show that when the dominant pole of the system approaches the edge of stability and the input satisfies one of the following conditions: (i) independence, (ii) positive correlation with a real and positive dominant pole, or (iii) sufficient correlation decay, the output converges to a standard normal distribution at rate $O(1/\sqrt{t})$. We also present counterexamples where convergence fails, thereby motivating the stated assumptions. Our results provide a rigorous foundation for the widespread observation that outputs of low-pass LTI systems tend to be approximately Gaussian.

