---
layout: default
title: Weights-Rotated Preference Optimization for Large Language Models
---

# Weights-Rotated Preference Optimization for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17637" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17637v1</a>
  <a href="https://arxiv.org/pdf/2508.17637.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17637v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17637v1', 'Weights-Rotated Preference Optimization for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenxu Yang, Ruipeng Jia, Mingyu Zheng, Naibin Gu, Zheng Lin, Siyuan Chen, Weichong Yin, Hua Wu, Weiping Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-25

**备注**: EMNLP 2025

---

## 💡 一句话要点

**提出权重旋转偏好优化以解决大语言模型的奖励黑客问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `直接偏好优化` `奖励黑客` `权重旋转优化` `自然语言处理` `知识保留` `生成模型`

## 📋 核心要点

1. 现有的直接偏好优化方法在对齐大语言模型时面临奖励黑客问题，导致生成内容缺乏多样性和知识遗忘。
2. 本文提出的权重旋转偏好优化算法通过约束输出层和中间隐藏状态，防止模型偏离参考模型，保留知识。
3. 实验结果表明，RoPO在AlpacaEval 2上提升3.27分，在MT-Bench上超越基线6.2至7.5分，且仅使用0.015%可训练参数。

## 📝 摘要（中文）

尽管直接偏好优化（DPO）在对齐大语言模型（LLMs）方面有效，但奖励黑客仍然是一个关键挑战。该问题出现在LLMs过度降低拒绝完成的概率以获得高奖励，而未真正实现其预期目标，导致生成内容过于冗长且缺乏多样性，同时造成知识的灾难性遗忘。我们探讨了这一问题的根本原因，即参数空间中的神经元崩溃导致的表示冗余。因此，我们提出了一种新颖的权重旋转偏好优化（RoPO）算法，该算法通过KL散度隐式约束输出层logits，并通过在多粒度正交矩阵上进行微调显式约束中间隐藏状态。这一设计防止了策略模型过度偏离参考模型，从而保留了在预训练和SFT阶段获得的知识和表达能力。我们的RoPO在AlpacaEval 2上实现了最高3.27分的提升，并在MT-Bench上超越最佳基线6.2至7.5分，仅使用0.015%的可训练参数，展示了其在缓解DPO奖励黑客问题方面的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在直接偏好优化中出现的奖励黑客问题。现有方法导致模型生成内容冗长且缺乏多样性，同时造成知识的灾难性遗忘。

**核心思路**：提出权重旋转偏好优化（RoPO）算法，通过隐式和显式约束，保持模型的知识和表达能力，防止其偏离参考模型。

**技术框架**：RoPO算法包括两个主要模块：一是通过KL散度约束输出层logits，二是通过多粒度正交矩阵微调中间隐藏状态。

**关键创新**：RoPO的创新在于同时对输出层和隐藏状态进行约束，解决了现有方法中的表示冗余问题，显著提升了模型的生成质量。

**关键设计**：RoPO使用的损失函数结合了KL散度和正交约束，确保模型在训练过程中保持对知识的有效利用，同时减少可训练参数的数量。

## 📊 实验亮点

RoPO算法在AlpacaEval 2上实现了最高3.27分的提升，并在MT-Bench上超越最佳基线6.2至7.5分，显示出其在解决奖励黑客问题方面的显著效果。此外，该算法仅使用0.015%的可训练参数，展现了其高效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和文本生成等。通过优化大语言模型的生成质量，RoPO能够提升用户体验，并在多种实际场景中实现更高效的知识传递和信息生成。未来，该方法可能对大规模语言模型的训练和应用产生深远影响。

## 📄 摘要（原文）

> Despite the efficacy of Direct Preference Optimization (DPO) in aligning Large Language Models (LLMs), reward hacking remains a pivotal challenge. This issue emerges when LLMs excessively reduce the probability of rejected completions to achieve high rewards, without genuinely meeting their intended goals. As a result, this leads to overly lengthy generation lacking diversity, as well as catastrophic forgetting of knowledge. We investigate the underlying reason behind this issue, which is representation redundancy caused by neuron collapse in the parameter space. Hence, we propose a novel Weights-Rotated Preference Optimization (RoPO) algorithm, which implicitly constrains the output layer logits with the KL divergence inherited from DPO and explicitly constrains the intermediate hidden states by fine-tuning on a multi-granularity orthogonal matrix. This design prevents the policy model from deviating too far from the reference model, thereby retaining the knowledge and expressive capabilities acquired during pre-training and SFT stages. Our RoPO achieves up to a 3.27-point improvement on AlpacaEval 2, and surpasses the best baseline by 6.2 to 7.5 points on MT-Bench with merely 0.015% of the trainable parameters, demonstrating its effectiveness in alleviating the reward hacking problem of DPO.

