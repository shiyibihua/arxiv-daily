---
layout: default
title: dots.llm1 Technical Report
---

# dots.llm1 Technical Report

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05767" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05767v1</a>
  <a href="https://arxiv.org/pdf/2506.05767.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05767v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05767v1', 'dots.llm1 Technical Report')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bi Huo, Bin Tu, Cheng Qin, Da Zheng, Debing Zhang, Dongjie Zhang, En Li, Fu Guo, Jian Yao, Jie Lou, Junfeng Tian, Li Hu, Ran Zhu, Shengdong Chen, Shuo Liu, Su Guang, Te Wo, Weijun Zhang, Xiaoming Shi, Xinxin Peng, Xing Wu, Yawen Liu, Yuqiu Ji, Ze Wen, Zhenhai Liu, Zichao Li, Zilong Liao

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-06

---

## 💡 一句话要点

**提出dots.llm1以高效激活语言模型参数**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家` `语言模型` `高效训练` `参数激活` `自然语言处理` `模型开源` `深度学习`

## 📋 核心要点

1. 现有的语言模型在参数激活效率和训练成本上存在挑战，难以在保持性能的同时扩展规模。
2. dots.llm1通过混合专家机制，仅激活部分参数，显著降低了计算资源消耗，同时保持了与最先进模型相当的性能。
3. 经过11.2T高质量标记的预训练，dots.llm1在性能上与Qwen2.5-72B相当，且提供了中间训练检查点以供研究使用。

## 📝 摘要（中文）

混合专家（MoE）模型作为一种有效扩展语言模型的范式，通过为每个输入标记激活部分参数而实现高效计算。在本报告中，我们介绍了dots.llm1，一个大规模的MoE模型，能够在总计142B参数中激活14B参数，性能与最先进的模型相当，同时降低了训练和推理成本。通过精心设计的数据处理流程，dots.llm1在预训练11.2T高质量标记后，性能可与Qwen2.5-72B相媲美，且在预训练过程中未使用任何合成数据。为促进进一步研究，我们开源了每一万亿标记的中间训练检查点，提供了对大型语言模型学习动态的宝贵见解。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有语言模型在参数激活效率和训练成本上的不足，尤其是在大规模模型的训练和推理过程中，如何有效利用计算资源。

**核心思路**：dots.llm1采用混合专家（MoE）架构，仅在每次输入时激活部分参数，从而在保持模型性能的同时，显著降低计算开销。

**技术框架**：该模型的整体架构包括多个专家模块，输入数据经过高效的数据处理管道，激活特定的专家进行计算，最终输出结果。

**关键创新**：最重要的创新在于通过精确的参数激活策略，dots.llm1能够在总参数量达到142B的情况下，仅激活14B参数，达到与更大模型相当的性能。

**关键设计**：在模型设计中，采用了高效的损失函数和网络结构，确保在激活参数的同时，能够快速收敛并提升模型的学习能力。

## 📊 实验亮点

dots.llm1在经过11.2T高质量标记的预训练后，性能与Qwen2.5-72B相当，且在参数激活方面仅使用了14B参数，显著降低了训练和推理成本。该模型的开源中间检查点为研究者提供了深入理解大型语言模型学习动态的机会。

## 🎯 应用场景

dots.llm1的研究成果具有广泛的应用潜力，尤其是在自然语言处理、对话系统和智能助手等领域。通过高效的参数激活机制，该模型能够在资源有限的情况下，提供高质量的语言理解和生成能力，推动相关技术的商业化应用。

## 📄 摘要（原文）

> Mixture of Experts (MoE) models have emerged as a promising paradigm for scaling language models efficiently by activating only a subset of parameters for each input token. In this report, we present dots.llm1, a large-scale MoE model that activates 14B parameters out of a total of 142B parameters, delivering performance on par with state-of-the-art models while reducing training and inference costs. Leveraging our meticulously crafted and efficient data processing pipeline, dots.llm1 achieves performance comparable to Qwen2.5-72B after pretraining on 11.2T high-quality tokens and post-training to fully unlock its capabilities. Notably, no synthetic data is used during pretraining. To foster further research, we open-source intermediate training checkpoints at every one trillion tokens, providing valuable insights into the learning dynamics of large language models.

