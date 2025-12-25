---
layout: default
title: Optimizing Decoding Paths in Masked Diffusion Models by Quantifying Uncertainty
---

# Optimizing Decoding Paths in Masked Diffusion Models by Quantifying Uncertainty

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21336" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21336v1</a>
  <a href="https://arxiv.org/pdf/2512.21336.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21336v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21336v1', 'Optimizing Decoding Paths in Masked Diffusion Models by Quantifying Uncertainty')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyu Chen, Xinbei Jiang, Peng Sun, Tao Lin

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**提出基于不确定性量化的掩码扩散模型解码路径优化方法**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `掩码扩散模型` `解码路径优化` `不确定性量化` `去噪熵` `非自回归生成`

## 📋 核心要点

1. 掩码扩散模型解码顺序对生成质量影响大，现有方法缺乏有效控制。
2. 提出基于去噪熵的解码路径优化方法，量化生成过程中的不确定性。
3. 实验证明，该方法显著提升了推理、规划和代码生成等任务的准确性。

## 📝 摘要（中文）

掩码扩散模型(MDMs)提供了一种灵活的、非自回归的生成方式，但这种自由也带来了一个挑战：最终输出质量对解码顺序高度敏感。我们首次将这个问题形式化，并将输出质量的变化归因于生成路径上的累积预测不确定性。为了量化这种不确定性，我们引入了去噪熵(Denoising Entropy)，这是一种可计算的指标，可以作为评估生成过程的内部信号。利用这个指标，我们提出了两种旨在优化解码路径的算法：一种事后选择方法和一种实时指导策略。实验表明，我们的熵引导方法显著提高了生成质量，持续提升了在具有挑战性的推理、规划和代码基准测试中的准确性。我们的工作将去噪熵确立为理解和控制生成过程的有效工具，有效地将MDM中的不确定性从一种负担转变为发现高质量解决方案的关键优势。

## 🔬 方法详解

**问题定义**：掩码扩散模型（MDMs）在生成过程中，由于其非自回归的特性，解码顺序的选择对最终生成结果的质量有显著影响。不同的解码路径会导致输出质量的巨大差异。现有的方法缺乏对这种解码路径选择的有效控制机制，导致生成结果不稳定，难以保证高质量的输出。

**核心思路**：论文的核心思路是通过量化生成过程中的不确定性来指导解码路径的选择。具体来说，论文提出了一种名为“去噪熵”（Denoising Entropy）的指标，用于衡量每一步去噪过程中的预测不确定性。通过选择不确定性较低的解码路径，可以降低累积误差，从而提高生成质量。

**技术框架**：整体框架包含以下几个主要步骤：1) 使用掩码扩散模型进行初始生成；2) 计算每一步去噪过程的去噪熵，作为衡量不确定性的指标；3) 基于去噪熵，采用两种策略优化解码路径：事后选择（选择熵值最低的路径）和实时指导（在生成过程中动态调整解码顺序）；4) 输出最终生成结果。

**关键创新**：论文的关键创新在于提出了“去噪熵”这一概念，并将其作为量化掩码扩散模型生成过程中不确定性的有效指标。这是首次将不确定性量化引入到MDM的解码路径优化中，为控制生成过程提供了一种新的视角和工具。与现有方法相比，该方法能够更准确地评估解码路径的质量，从而实现更有效的优化。

**关键设计**：去噪熵的计算基于模型预测的概率分布。具体来说，对于每一步去噪过程，模型会预测一个概率分布，去噪熵就是该概率分布的熵值。熵值越高，表示模型的不确定性越大。在事后选择策略中，选择具有最低平均去噪熵的完整解码路径。在实时指导策略中，每一步都选择能够最小化未来去噪熵的解码方向。具体的参数设置和网络结构与所使用的掩码扩散模型相关，论文中没有明确指出。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21336v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21336v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21336v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，基于去噪熵的解码路径优化方法在多个具有挑战性的任务上取得了显著的性能提升。例如，在推理、规划和代码生成等基准测试中，该方法能够持续提高生成准确率。具体的数据提升幅度在论文中有所体现，证明了该方法的有效性和优越性。

## 🎯 应用场景

该研究成果可应用于各种需要高质量、可控生成的场景，例如图像修复、文本生成、代码生成、药物发现等。通过优化解码路径，可以显著提高生成结果的质量和稳定性，从而提升相关应用的性能和用户体验。未来，该方法有望进一步扩展到其他类型的生成模型中，为人工智能的创造性应用提供更强大的支持。

## 📄 摘要（原文）

> Masked Diffusion Models (MDMs) offer flexible, non-autoregressive generation, but this freedom introduces a challenge: final output quality is highly sensitive to the decoding order. We are the first to formalize this issue, attributing the variability in output quality to the cumulative predictive uncertainty along a generative path. To quantify this uncertainty, we introduce Denoising Entropy, a computable metric that serves as an internal signal for evaluating generative process. Leveraging this metric, we propose two algorithms designed to optimize the decoding path: a post-hoc selection method and a real-time guidance strategy. Experiments demonstrate that our entropy-guided methods significantly improve generation quality, consistently boosting accuracy on challenging reasoning, planning, and code benchmarks. Our work establishes Denoising Entropy as a principled tool for understanding and controlling generation, effectively turning the uncertainty in MDMs from a liability into a key advantage for discovering high-quality solutions.

