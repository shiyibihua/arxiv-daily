---
layout: default
title: Any-Order Flexible Length Masked Diffusion
---

# Any-Order Flexible Length Masked Diffusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01025" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01025v2</a>
  <a href="https://arxiv.org/pdf/2509.01025.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01025v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01025v2', 'Any-Order Flexible Length Masked Diffusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jaeyeon Kim, Lee Cheuk-Kit, Carles Domingo-Enrich, Yilun Du, Sham Kakade, Timothy Ngotiaoco, Sitan Chen, Michael Albergo

**分类**: cs.LG

**发布日期**: 2025-08-31 (更新: 2025-09-07)

**备注**: Preprint

---

## 💡 一句话要点

**提出灵活的掩码扩散模型以解决固定长度生成问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `掩码扩散模型` `灵活生成` `序列建模` `自然语言处理` `代码生成`

## 📋 核心要点

1. 现有的掩码扩散模型（MDMs）无法支持令牌插入，限制了生成长度的灵活性。
2. 本文提出的灵活掩码扩散模型（FlexMDMs）通过插入和解掩码令牌，实现了灵活长度序列的生成。
3. 在合成迷宫规划任务中，FlexMDMs的成功率比MDM基线高出约60%，并在数学和代码填充任务上表现优异。

## 📝 摘要（中文）

掩码扩散模型（MDMs）作为自回归模型在离散领域的替代方案，能够以任意顺序并行生成序列，适用于非因果任务。然而，MDMs的一个重要局限是无法支持令牌插入，导致生成长度固定。为此，本文提出了灵活掩码扩散模型（FlexMDMs），该模型能够同时建模灵活长度的序列，同时保持MDMs的任意顺序推理能力。基于随机插值框架的扩展，FlexMDMs通过插入掩码令牌并解掩码来生成序列。实验证明，FlexMDMs在困惑度上与MDMs相当，同时在长度统计建模上具有更高的保真度。在合成迷宫规划任务中，FlexMDMs的成功率比MDM基线高出约60%。最后，我们展示了预训练的MDMs可以轻松改装为FlexMDMs：在16个H100上，仅需三天即可将LLaDA-8B微调为FlexMDM，在数学（GSM8K，58%提升至67%）和代码填充性能（52%提升至65%）上取得了优越的表现。

## 🔬 方法详解

**问题定义**：本文旨在解决掩码扩散模型（MDMs）在生成过程中无法支持令牌插入的问题，导致生成长度固定，限制了模型的灵活性和应用场景。

**核心思路**：提出灵活掩码扩散模型（FlexMDMs），通过插入掩码令牌并解掩码的方式，允许模型生成可变长度的序列，同时保持任意顺序推理的能力。

**技术框架**：FlexMDMs的整体架构基于随机插值框架的扩展，主要包括掩码令牌的插入模块和解掩码模块，确保生成过程的灵活性与高效性。

**关键创新**：FlexMDMs的核心创新在于其能够在保持MDMs灵活性的同时，实现可变长度序列的生成，这一特性在现有模型中尚未实现。

**关键设计**：在模型设计中，FlexMDMs采用了特定的损失函数以优化生成质量，并在网络结构上进行了调整，以适应掩码令牌的插入与解掩码过程。

## 📊 实验亮点

FlexMDMs在合成迷宫规划任务中成功率比MDM基线高出约60%。此外，FlexMDMs在数学（GSM8K）和代码填充任务上表现优异，分别将准确率从58%提升至67%和从52%提升至65%。

## 🎯 应用场景

灵活掩码扩散模型（FlexMDMs）在自然语言处理、代码生成和其他序列生成任务中具有广泛的应用潜力。其灵活的生成长度和高效的推理能力使其能够适应多种实际场景，提升生成质量和效率，未来可能推动相关领域的进一步发展。

## 📄 摘要（原文）

> Masked diffusion models (MDMs) have recently emerged as a promising alternative to autoregressive models over discrete domains. MDMs generate sequences in an any-order, parallel fashion, enabling fast inference and strong performance on non-causal tasks. However, a crucial limitation is that they do not support token insertions and are thus limited to fixed-length generations. To this end, we introduce Flexible Masked Diffusion Models (FlexMDMs), a discrete diffusion paradigm that simultaneously can model sequences of flexible length while provably retaining MDMs' flexibility of any-order inference. Grounded in an extension of the stochastic interpolant framework, FlexMDMs generate sequences by inserting mask tokens and unmasking them. Empirically, we show that FlexMDMs match MDMs in perplexity while modeling length statistics with much higher fidelity. On a synthetic maze planning task, they achieve $\approx 60 \%$ higher success rate than MDM baselines. Finally, we show pretrained MDMs can easily be retrofitted into FlexMDMs: on 16 H100s, it takes only three days to fine-tune LLaDA-8B into a FlexMDM, achieving superior performance on math (GSM8K, $58\% \to 67\%$) and code infilling performance ($52\% \to 65\%$).

