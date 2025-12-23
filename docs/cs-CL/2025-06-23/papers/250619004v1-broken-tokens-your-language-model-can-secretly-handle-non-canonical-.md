---
layout: default
title: Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations
---

# Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19004" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19004v1</a>
  <a href="https://arxiv.org/pdf/2506.19004.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19004v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19004v1', 'Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Brian Siyuan Zheng, Alisa Liu, Orevaoghene Ahia, Jonathan Hayase, Yejin Choi, Noah A. Smith

**分类**: cs.CL

**发布日期**: 2025-06-23

**备注**: preprint

---

## 💡 一句话要点

**研究非标准分词对语言模型性能的影响**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `语言模型` `非标准分词` `鲁棒性` `指令调优` `文本处理` `性能提升`

## 📋 核心要点

1. 现有的分词方法通常依赖于确定性算法，导致模型对非标准分词形式的鲁棒性不足。
2. 本研究提出探讨语言模型在未见过的非标准分词下的表现，发现模型在随机和字符级分词下仍能保持较高性能。
3. 实验结果显示，经过指令调优的模型在特定任务中能够显著提升性能，尤其是在字符串操作和大数算术任务中。

## 📝 摘要（中文）

现代分词器采用确定性算法将文本映射为单一的“标准”标记序列，但同一字符串可以使用分词词汇表编码为多种非标准分词形式。本研究探讨了语言模型对未在训练中见过的非标准分词的鲁棒性。令人惊讶的是，在20个基准测试中，经过指令调优的模型在随机采样的分词下仍能保持高达93.4%的原始性能，字符级分词下为90.8%。更强的模型通常表现出更好的鲁棒性，而鲁棒性随着分词偏离标准形式而减弱。此外，我们发现某些非标准分词方案可以提升性能，例如字符级分词在字符串操作和代码理解任务中提高了14%，而右对齐数字分组在大数算术中提升了33%。最后，我们探讨了这种鲁棒性的来源，发现其在指令调优阶段形成。

## 🔬 方法详解

**问题定义**：本论文旨在解决语言模型在面对未见过的非标准分词时的鲁棒性问题。现有方法通常假设模型仅能处理标准分词，导致在实际应用中性能下降。

**核心思路**：论文的核心思路是验证语言模型在非标准分词下的表现，并探索如何利用这些非标准分词形式提升模型性能。通过对比不同分词方式，研究发现某些非标准分词形式能够有效提高模型在特定任务上的表现。

**技术框架**：整体架构包括对语言模型的指令调优阶段，评估模型在不同分词形式下的表现。主要模块包括标准分词与非标准分词的比较、性能评估以及鲁棒性分析。

**关键创新**：本研究的创新点在于揭示了语言模型对分词器的依赖程度低于预期，且在推理阶段对分词的干预能够显著提升性能。这一发现挑战了传统观点，表明模型可以灵活适应不同的分词形式。

**关键设计**：在实验中，采用了多种分词策略，包括随机分词和字符级分词，并通过指令调优来增强模型对非标准分词的理解。模型在训练时未见过的分词形式被视为拼写错误，基于此设计了相应的损失函数和评估指标。

## 📊 实验亮点

实验结果显示，经过指令调优的模型在随机分词下保持93.4%的原始性能，而在字符级分词下为90.8%。此外，字符级分词在字符串操作和代码理解任务中提升了14%，右对齐数字分组在大数算术中提升了33%。这些结果表明，非标准分词形式在特定任务中具有显著的性能提升潜力。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的文本生成、代码理解和字符串操作等任务。通过优化分词策略，模型在实际应用中能够更好地处理多样化的输入，提升用户体验。未来，研究结果可能推动更灵活的分词方法在各类语言模型中的应用，进一步提高模型的适应性和性能。

## 📄 摘要（原文）

> Modern tokenizers employ deterministic algorithms to map text into a single "canonical" token sequence, yet the same string can be encoded as many non-canonical tokenizations using the tokenizer vocabulary. In this work, we investigate the robustness of LMs to text encoded with non-canonical tokenizations entirely unseen during training. Surprisingly, when evaluated across 20 benchmarks, we find that instruction-tuned models retain up to 93.4% of their original performance when given a randomly sampled tokenization, and 90.8% with character-level tokenization. We see that overall stronger models tend to be more robust, and robustness diminishes as the tokenization departs farther from the canonical form. Motivated by these results, we then identify settings where non-canonical tokenization schemes can *improve* performance, finding that character-level segmentation improves string manipulation and code understanding tasks by up to +14%, and right-aligned digit grouping enhances large-number arithmetic by +33%. Finally, we investigate the source of this robustness, finding that it arises in the instruction-tuning phase. We show that while both base and post-trained models grasp the semantics of non-canonical tokenizations (perceiving them as containing misspellings), base models try to mimic the imagined mistakes and degenerate into nonsensical output, while post-trained models are committed to fluent responses. Overall, our findings suggest that models are less tied to their tokenizer than previously believed, and demonstrate the promise of intervening on tokenization at inference time to boost performance.

