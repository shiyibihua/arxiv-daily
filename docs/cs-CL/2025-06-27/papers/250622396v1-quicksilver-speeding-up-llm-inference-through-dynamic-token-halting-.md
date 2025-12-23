---
layout: default
title: QuickSilver -- Speeding up LLM Inference through Dynamic Token Halting, KV Skipping, Contextual Token Fusion, and Adaptive Matryoshka Quantization
---

# QuickSilver -- Speeding up LLM Inference through Dynamic Token Halting, KV Skipping, Contextual Token Fusion, and Adaptive Matryoshka Quantization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22396" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22396v1</a>
  <a href="https://arxiv.org/pdf/2506.22396.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22396v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22396v1', 'QuickSilver -- Speeding up LLM Inference through Dynamic Token Halting, KV Skipping, Contextual Token Fusion, and Adaptive Matryoshka Quantization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Danush Khanna, Aditya Kumar Guru, Srivarshinee Sridhar, Zidan Ahmed, Rubhav Bahirwani, Meetu Malhotra, Vinija Jain, Aman Chadha, Amitava Das, Kripabandhu Ghosh

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-27

**备注**: Preprint. Under submission

---

## 💡 一句话要点

**提出QuickSilver以加速大型语言模型推理过程**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理优化` `动态令牌停止` `KV缓存跳过` `上下文令牌融合` `自适应量化` `自然语言处理`

## 📋 核心要点

1. 现有方法在大型语言模型推理中存在效率低下的问题，尤其是在自回归解码时，导致延迟和能耗高。
2. QuickSilver提出了一种模块化的令牌级框架，通过动态令牌停止、KV缓存跳过和上下文令牌融合等机制，实现推理时的语义适应性。
3. 在实验中，QuickSilver在多个基准数据集上应用于GPT-2和Llama-2，取得了高达39.6%的FLOP减少，且困惑度几乎没有下降。

## 📝 摘要（中文）

推理在大型语言模型（LLM）部署中占据了大部分延迟和能耗，通常超过90%的总成本。尽管训练效率已有显著进展，但运行时优化仍是关键瓶颈，尤其是在自回归解码下。现有方法如剪枝、量化、早期退出和推测解码，往往需要重新训练、架构更改或破坏解码兼容性。我们提出了QuickSilver，一个模块化的、基于令牌的框架，能够在推理时实现语义适应性，而无需改变模型权重或结构。QuickSilver集成了四个协同机制：动态令牌停止、KV缓存跳过、上下文令牌融合和自适应Matryoshka量化。与推测解码或MoE路由不同，QuickSilver完全在冻结的密集模型上运行，并且不需要辅助网络。在WikiText-103和C4上应用于GPT-2和Llama-2，QuickSilver实现了高达39.6%的FLOP减少，且困惑度降幅微乎其微（<=0.2）。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型推理过程中的延迟和能耗问题。现有方法如剪枝和量化等，往往需要重新训练或改变模型架构，影响解码兼容性。

**核心思路**：QuickSilver的核心思路是通过不改变模型权重或结构的方式，实现推理时的语义适应性。该方法通过动态令牌停止等机制，优化计算过程，减少不必要的计算。

**技术框架**：QuickSilver的整体架构包括四个主要模块：动态令牌停止、KV缓存跳过、上下文令牌融合和自适应Matryoshka量化。这些模块协同工作，以提高推理效率。

**关键创新**：QuickSilver的最大创新在于其模块化设计，能够在不依赖辅助网络的情况下，完全在冻结的密集模型上运行。这与现有的推测解码和MoE路由方法有本质区别。

**关键设计**：在设计中，QuickSilver通过动态令牌停止机制来中断计算，KV缓存跳过机制来减少内存写入，上下文令牌融合机制来合并冗余令牌，从而有效缩短序列长度。

## 📊 实验亮点

在实验中，QuickSilver在WikiText-103和C4数据集上应用于GPT-2和Llama-2，成功实现了高达39.6%的FLOP减少，同时保持了困惑度的微小降幅（<=0.2），显示出其在推理效率上的显著提升。

## 🎯 应用场景

QuickSilver的研究成果在多个领域具有潜在应用价值，尤其是在需要高效推理的自然语言处理任务中，如对话系统、文本生成和机器翻译等。其高效的推理机制能够显著降低计算资源消耗，提高实时响应能力，推动智能应用的发展。

## 📄 摘要（原文）

> Inference accounts for the majority of latency and energy consumption in large language model (LLM) deployments, often exceeding 90% of total cost. While training-time efficiency has seen extensive progress, runtime optimization remains a key bottleneck, particularly under autoregressive decoding. Existing approaches -- such as pruning, quantization, early exits, and speculative decoding -- often require retraining, architectural changes, or disrupt decoding compatibility. We introduce QuickSilver, a modular, token-level framework that enables semantic adaptivity at inference time without altering model weights or structure. QuickSilver integrates four synergistic mechanisms:
>   (i) Dynamic Token Halting, which halts computation for tokens with converged representations; (ii) KV Cache Skipping, which selectively suppresses memory writes to reduce attention overhead; and (iii) Contextual Token Fusion, which collapses redundant tokens into shared paths to shrink sequence length.
>   Unlike speculative decoding or MoE routing, QuickSilver operates entirely on frozen, dense models and requires no auxiliary networks. Applied to GPT-2 and Llama-2 across WikiText-103 and C4, QuickSilver achieves up to 39.6% FLOP reduction with negligible perplexity degradation (<=0.2).

