---
layout: default
title: Plug-and-Play Prompt Refinement via Latent Feedback for Diffusion Model Alignment
---

# Plug-and-Play Prompt Refinement via Latent Feedback for Diffusion Model Alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00430" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00430v1</a>
  <a href="https://arxiv.org/pdf/2510.00430.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00430v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00430v1', 'Plug-and-Play Prompt Refinement via Latent Feedback for Diffusion Model Alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Suhyeon Lee, Jong Chul Ye

**分类**: cs.LG, cs.AI, cs.CV

**发布日期**: 2025-10-01

**备注**: 23 pages, 15 figures

---

## 💡 一句话要点

**提出PromptLoop：一种基于隐空间反馈的即插即用提示优化扩散模型对齐框架**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散模型` `提示优化` `强化学习` `多模态学习` `模型对齐`

## 📋 核心要点

1. 现有基于强化学习的扩散模型微调方法泛化性差，易受奖励操纵，且组合性不足。
2. PromptLoop通过强化学习训练多模态大语言模型，根据扩散模型的中间隐状态迭代优化提示词。
3. 实验表明PromptLoop能有效优化奖励，泛化性好，可与现有对齐方法组合，并减轻过度优化。

## 📝 摘要（中文）

尽管最近取得了进展，但基于强化学习（RL）的扩散模型微调通常难以泛化、组合，并且对奖励黑客攻击的鲁棒性较差。最近的研究探索了提示优化作为一种模块化替代方案，但大多数采用前馈方法，在整个采样轨迹中应用单个优化的提示，从而未能充分利用强化学习的顺序特性。为了解决这个问题，我们提出PromptLoop，一个即插即用的RL框架，它将隐空间反馈融入到逐步提示优化中。与修改扩散模型权重不同，使用RL训练多模态大型语言模型（MLLM），以基于扩散模型的中间隐状态迭代更新提示。这种设计实现了与扩散RL方法的结构类比，同时保留了基于提示对齐的灵活性和通用性。在不同的奖励函数和扩散骨干网络上的大量实验表明，PromptLoop（i）实现了有效的奖励优化，（ii）无缝泛化到未见过的模型，（iii）与现有的对齐方法正交组合，以及（iv）减轻了过度优化和奖励黑客攻击。

## 🔬 方法详解

**问题定义**：论文旨在解决扩散模型对齐过程中，基于强化学习的微调方法存在的泛化性差、组合性不足以及容易受到奖励黑客攻击的问题。现有的提示优化方法通常采用前馈方式，无法充分利用扩散模型的顺序采样特性，导致优化效果受限。

**核心思路**：论文的核心思路是利用强化学习训练一个多模态大语言模型（MLLM），使其能够根据扩散模型的中间隐状态，迭代地优化提示词。通过在扩散模型的采样过程中，逐步调整提示词，从而更有效地引导扩散模型的生成过程，实现更好的对齐效果。

**技术框架**：PromptLoop框架主要包含以下几个模块：1) 扩散模型：作为生成图像的基础模型。2) 多模态大语言模型（MLLM）：作为提示词优化器，接收扩散模型的中间隐状态和奖励信号，输出优化的提示词。3) 强化学习模块：用于训练MLLM，使其能够根据奖励信号优化提示词。整个流程是：扩散模型生成中间隐状态，MLLM根据隐状态生成优化后的提示词，扩散模型使用优化后的提示词继续生成，直到生成最终图像，根据最终图像计算奖励，并用奖励信号更新MLLM。

**关键创新**：PromptLoop的关键创新在于将隐空间反馈融入到提示词优化过程中。与传统的前馈提示优化方法不同，PromptLoop能够根据扩散模型的中间状态，动态地调整提示词，从而更有效地利用扩散模型的顺序采样特性。此外，PromptLoop采用即插即用的设计，无需修改扩散模型的权重，即可实现对齐。

**关键设计**：MLLM的具体选择未知，但需要具备理解图像信息和生成文本的能力。强化学习算法的选择未知，但需要能够处理连续动作空间。奖励函数的设计至关重要，需要能够准确地反映对齐目标。具体的参数设置和网络结构等技术细节在论文中可能有所描述，但此处无法得知。

## 📊 实验亮点

实验结果表明，PromptLoop在多个奖励函数和扩散模型上都取得了显著的性能提升。与现有的提示优化方法相比，PromptLoop能够更好地优化奖励，并具有更好的泛化性和鲁棒性。此外，PromptLoop还可以与现有的对齐方法正交组合，进一步提高对齐效果。具体性能数据未知。

## 🎯 应用场景

PromptLoop可应用于各种需要对齐扩散模型的场景，例如文本到图像生成、图像编辑、风格迁移等。该方法能够提高生成图像的质量和与目标任务的相关性，并降低模型被恶意利用的风险。未来，PromptLoop有望成为扩散模型对齐的标准方法之一。

## 📄 摘要（原文）

> Despite the recent progress, reinforcement learning (RL)-based fine-tuning of diffusion models often struggles with generalization, composability, and robustness against reward hacking. Recent studies have explored prompt refinement as a modular alternative, but most adopt a feed-forward approach that applies a single refined prompt throughout the entire sampling trajectory, thereby failing to fully leverage the sequential nature of reinforcement learning. To address this, here we introduce PromptLoop, a plug-and-play RL framework that incorporates latent feedback into step-wise prompt refinement. Rather than modifying diffusion model weights, a multimodal large language model (MLLM) is trained with RL to iteratively update prompts based on intermediate latent states of diffusion models. This design achieves a structural analogy to the Diffusion RL approach, while retaining the flexibility and generality of prompt-based alignment. Extensive experiments across diverse reward functions and diffusion backbones demonstrate that PromptLoop (i) achieves effective reward optimization, (ii) generalizes seamlessly to unseen models, (iii) composes orthogonally with existing alignment methods, and (iv) mitigates over-optimization and reward hacking.

