---
layout: default
title: Closed-Loop Consistent, Causal Data-Driven Predictive Control via SSARX
---

# Closed-Loop Consistent, Causal Data-Driven Predictive Control via SSARX

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14510" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14510v1</a>
  <a href="https://arxiv.org/pdf/2512.14510.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14510v1" onclick="toggleFavorite(this, '2512.14510v1', 'Closed-Loop Consistent, Causal Data-Driven Predictive Control via SSARX')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aihui Liu, Magnus Jansson

**分类**: eess.SY, eess.SP

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于SSARX的闭环一致因果数据驱动预测控制方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `数据驱动控制` `预测控制` `SSARX模型` `闭环控制` `系统辨识`

## 📋 核心要点

1. 传统DeePC方法依赖于Willems基本引理和Hankel矩阵，计算复杂度高，且对噪声敏感。
2. 该文提出基于SSARX的DDPC方案，避免了Hankel矩阵和DeePC决策变量，降低了计算复杂度。
3. 实验结果表明，在受噪声影响的闭环数据上，SSARX方法与其他方法相比具有竞争力。

## 📝 摘要（中文）

本文提出了一种无需基本引理的数据驱动预测控制(DDPC)方案，用于直接从输入输出数据中合成类似模型预测控制(MPC)的策略。与依赖Willems基本引理的DeePC方法和其他DDPC方法不同，我们的方法避免了堆叠的Hankel矩阵表示和DeePC决策变量g。相反，我们开发了一种基于多步预测器Subspace-ARX (SSARX)的闭环一致、因果DDPC方案。该方法首先(i)通过高阶ARX模型估计预测器/观测器Markov参数以解耦噪声，然后(ii)通过回归学习多步过去到未来的映射，可以选择使用降秩约束。SSARX预测器是严格因果的，这使得它可以自然地集成到MPC公式中。实验结果表明，当应用于受测量和过程噪声影响的闭环数据时，SSARX的性能与其他方法相比具有竞争力。

## 🔬 方法详解

**问题定义**：传统的数据驱动预测控制方法，如DeePC，依赖于Willems基本引理和Hankel矩阵，这导致了较高的计算复杂度，并且对噪声较为敏感。此外，DeePC的决策变量g也增加了计算负担。因此，需要一种更高效、更鲁棒的数据驱动预测控制方法。

**核心思路**：本文的核心思路是利用Subspace-ARX (SSARX)模型来构建一个闭环一致、因果的数据驱动预测控制器。SSARX模型通过高阶ARX模型估计预测器/观测器Markov参数，从而解耦噪声。然后，通过回归学习多步过去到未来的映射，从而实现预测控制。

**技术框架**：该方法主要包含两个阶段：(1) SSARX模型参数估计阶段：利用高阶ARX模型从输入输出数据中估计预测器/观测器Markov参数，以解耦噪声。(2) 多步预测控制阶段：通过回归学习多步过去到未来的映射，并将其集成到MPC框架中，实现预测控制。可以选择使用降秩约束来提高模型的泛化能力。

**关键创新**：该方法最重要的创新点在于，它避免了使用Willems基本引理和Hankel矩阵，而是直接利用SSARX模型进行预测控制。SSARX模型是严格因果的，这使得它可以自然地集成到MPC公式中。此外，该方法通过高阶ARX模型解耦噪声，提高了模型的鲁棒性。

**关键设计**：SSARX模型中的ARX模型的阶数是一个关键参数，需要根据实际数据进行调整。回归学习多步过去到未来的映射时，可以选择使用不同的回归方法，如最小二乘法或岭回归。降秩约束可以用来提高模型的泛化能力，但需要仔细选择秩的大小。

## 📊 实验亮点

实验结果表明，当应用于受测量和过程噪声影响的闭环数据时，基于SSARX的DDPC方法与其他方法相比具有竞争力。具体性能数据未知，但强调了其在噪声环境下的鲁棒性。

## 🎯 应用场景

该研究成果可应用于各种需要精确控制的工业领域，例如机器人控制、过程控制、电力系统控制等。通过直接从数据中学习控制策略，可以避免复杂的系统建模过程，降低开发成本，提高控制性能。该方法尤其适用于难以建立精确模型的复杂系统。

## 📄 摘要（原文）

> We propose a fundamental-lemma-free data-driven predictive control (DDPC) scheme for synthesizing model predictive control (MPC)-like policies directly from input-output data. Unlike the well-known DeePC approach and other DDPC methods that rely on Willems' fundamental lemma, our method avoids stacked Hankel representations and the DeePC decision variable g. Instead, we develop a closed-loop consistent, causal DDPC scheme based on the multi-step predictor Subspace-ARX (SSARX). The method first (i) estimates predictor/observer Markov parameters via a high-order ARX model to decouple the noise, then (ii) learns a multi-step past-to-future map by regression, optionally with a reduced-rank constraint. The SSARX predictor is strictly causal, which allows it to be integrated naturally into an MPC formulation. Our experimental results show that SSARX performs competitively with other methods when applied to closed-loop data affected by measurement and process noise.

