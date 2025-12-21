---
layout: default
title: Sigma-Moe-Tiny Technical Report
---

# Sigma-Moe-Tiny Technical Report

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16248" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16248v1</a>
  <a href="https://arxiv.org/pdf/2512.16248.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16248v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16248v1', 'Sigma-Moe-Tiny Technical Report')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qingguo Hu, Zhenghao Lin, Ziyue Yang, Yucheng Ding, Xiao Liu, Yuting Jiang, Ruizhe Wang, Tianyu Chen, Zhongxin Guo, Yifan Xiong, Rui Gao, Lei Qu, Jinsong Su, Peng Cheng, Yeyun Gong

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-18

**🔗 代码/项目**: [GITHUB](https://github.com/microsoft/ltp-megatron-lm) | [PROJECT_PAGE](https://qghuxmu.github.io/Sigma-MoE-Tiny)

---

## 💡 一句话要点

**Sigma-MoE-Tiny：提出一种高稀疏MoE语言模型，解决专家负载均衡问题，实现高效扩展。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家模型` `MoE` `稀疏模型` `负载均衡` `渐进式稀疏化`

## 📋 核心要点

1. 现有MoE模型在极端稀疏性下，专家负载均衡面临挑战，传统负载均衡损失在底层失效。
2. 提出渐进式稀疏化策略，平衡专家利用率和训练稳定性，解决高稀疏性下的负载均衡问题。
3. Sigma-MoE-Tiny仅激活0.5B参数，但在同等或更大规模模型中表现出色，训练过程稳定。

## 📝 摘要（中文）

本文介绍了Sigma-MoE-Tiny，一种混合专家（MoE）语言模型，它实现了现有开源模型中最高的稀疏性。Sigma-MoE-Tiny采用细粒度的专家分割，每层最多有96个专家，但每个token只激活一个专家，从而在总参数量为200亿的情况下，仅激活0.5B参数。这种极端稀疏性带来的主要挑战是专家负载均衡。研究发现，在这种设置下，广泛使用的负载均衡损失在较低层往往失效。为了解决这个问题，提出了一种渐进式稀疏化策略，旨在平衡专家利用率和训练稳定性。Sigma-MoE-Tiny在一个多样化和高质量的语料库上进行预训练，然后进行后训练以进一步释放其能力。整个训练过程保持了显著的稳定性，没有出现不可恢复的损失峰值。综合评估表明，尽管只激活了0.5B参数，Sigma-MoE-Tiny在同等或更大规模的同类模型中实现了顶级的性能。此外，还深入讨论了高稀疏MoE模型中的负载均衡问题，为未来MoE架构中提高稀疏性提供了见解。

## 🔬 方法详解

**问题定义**：论文旨在解决MoE模型中，在极高稀疏度下专家负载不均衡的问题。现有的负载均衡损失函数在高稀疏度下，尤其是在模型的底层，效果显著下降，导致部分专家过度使用，而另一些专家则利用不足，影响模型整体性能和训练稳定性。

**核心思路**：论文的核心思路是通过渐进式稀疏化策略来解决专家负载均衡问题。该策略并非一开始就采用最高的稀疏度，而是逐步增加稀疏度，从而在训练初期保证所有专家都能得到充分利用，避免早期训练阶段出现专家利用率严重不均衡的情况。这种逐步稀疏化的方式有助于稳定训练过程，并最终达到期望的高稀疏度。

**技术框架**：Sigma-MoE-Tiny的整体框架基于Transformer架构，并引入了MoE层。每个MoE层包含多个专家（最多96个），但每个token只激活一个专家。模型首先在大量数据上进行预训练，然后进行后训练以提升性能。关键在于训练过程中使用的渐进式稀疏化策略，该策略控制着每层激活的专家数量，并随着训练的进行逐步增加稀疏度。

**关键创新**：论文的关键创新在于提出了渐进式稀疏化策略。与传统的MoE训练方法不同，该策略不是一开始就设定固定的高稀疏度，而是通过一个schedule逐步增加稀疏度。这种方法能够更好地平衡专家利用率和训练稳定性，避免了因早期专家利用率不均衡而导致的训练崩溃。

**关键设计**：渐进式稀疏化策略的具体实现涉及到一个稀疏度schedule，该schedule定义了在训练的不同阶段激活的专家数量。例如，在训练初期，可能激活更多的专家，以确保所有专家都能得到训练。随着训练的进行，逐渐减少激活的专家数量，最终达到目标稀疏度。此外，论文还可能涉及到对负载均衡损失函数的调整，以适应高稀疏度下的训练。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16248v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16248v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16248v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Sigma-MoE-Tiny在激活仅0.5B参数的情况下，实现了与参数量更大模型相当甚至更优的性能。实验结果表明，该模型在多个NLP任务上取得了具有竞争力的结果，证明了其在高稀疏度下的有效性。此外，训练过程表现出极高的稳定性，没有出现不可恢复的损失峰值，验证了渐进式稀疏化策略的有效性。

## 🎯 应用场景

Sigma-MoE-Tiny的研究成果可应用于各种需要高效和可扩展语言模型的场景，例如自然语言处理、机器翻译、文本生成、对话系统等。其高稀疏性使得模型能够在资源受限的环境中部署，降低计算成本和能源消耗。此外，该研究为未来MoE架构的设计提供了新的思路，有助于开发更大规模、更高性能的语言模型。

## 📄 摘要（原文）

> Mixture-of-Experts (MoE) has emerged as a promising paradigm for foundation models due to its efficient and powerful scalability. In this work, we present Sigma-MoE-Tiny, an MoE language model that achieves the highest sparsity compared to existing open-source models. Sigma-MoE-Tiny employs fine-grained expert segmentation with up to 96 experts per layer, while activating only one expert for each token, resulting in 20B total parameters with just 0.5B activated. The major challenge introduced by such extreme sparsity lies in expert load balancing. We find that the widely-used load balancing loss tends to become ineffective in the lower layers under this setting. To address this issue, we propose a progressive sparsification schedule aiming to balance expert utilization and training stability. Sigma-MoE-Tiny is pre-trained on a diverse and high-quality corpus, followed by post-training to further unlock its capabilities. The entire training process remains remarkably stable, with no occurrence of irrecoverable loss spikes. Comprehensive evaluations reveal that, despite activating only 0.5B parameters, Sigma-MoE-Tiny achieves top-tier performance among counterparts of comparable or significantly larger scale. In addition, we provide an in-depth discussion of load balancing in highly sparse MoE models, offering insights for advancing sparsity in future MoE architectures.
>   Project page: https://qghuxmu.github.io/Sigma-MoE-Tiny
>   Code: https://github.com/microsoft/ltp-megatron-lm

