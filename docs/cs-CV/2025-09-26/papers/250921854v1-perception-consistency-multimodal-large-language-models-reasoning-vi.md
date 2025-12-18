---
layout: default
title: Perception-Consistency Multimodal Large Language Models Reasoning via Caption-Regularized Policy Optimization
---

# Perception-Consistency Multimodal Large Language Models Reasoning via Caption-Regularized Policy Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21854" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21854v1</a>
  <a href="https://arxiv.org/pdf/2509.21854.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21854v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21854v1', 'Perception-Consistency Multimodal Large Language Models Reasoning via Caption-Regularized Policy Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Songjun Tu, Qichao Zhang, Jingbo Sun, Yuqian Fu, Linjing Li, Xiangyuan Lan, Dongmei Jiang, Yaowei Wang, Dongbin Zhao

**分类**: cs.MM, cs.CV

**发布日期**: 2025-09-26

**备注**: 12pages, 11 figures

---

## 💡 一句话要点

**提出CapPO，通过Caption正则化策略优化提升多模态大语言模型感知一致性推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `强化学习` `策略优化` `感知一致性` `Caption正则化`

## 📋 核心要点

1. 多模态大语言模型易受感知误差影响，导致推理链错误，现有强化学习方法难以解决视觉与推理的错位问题。
2. 提出Caption正则化策略优化（CapPO），通过Caption一致性正则化和KL加权优势估计，显式地提升感知一致性。
3. 实验表明，CapPO在数学和通用推理任务上均有显著提升，分别达到+6.0%和+2.4%，并有效减少感知相关错误。

## 📝 摘要（中文）

多模态大语言模型在整合视觉感知和符号推理的任务中表现出色，但其性能常因感知引起的错误在推理链中传播而受损。现有的强化学习微调方法虽然增强了推理能力，但未能解决视觉基础与后续推理过程之间的根本错位问题。为了应对这一挑战，我们提出了一种新的强化学习框架——Caption正则化策略优化（CapPO），该框架在策略优化过程中显式地强制执行感知一致性。CapPO集成了两个关键机制：(1) 基于Caption的一致性正则化，它最小化了以原始图像为条件的响应与以Caption为条件的响应之间的差异，从而将推理锚定到语义上忠实的视觉内容；(2) KL加权优势估计方案，它自适应地缩放强化信号，以加强感知一致的轨迹，同时抑制虚假相关性。在五个数学相关和五个通用推理基准上的大量实验表明，CapPO取得了有竞争力的性能，在数学相关任务上比Qwen2.5-VL-7B模型提高了+6.0%的准确率，在通用推理任务上提高了+2.4%。此外，消融研究进一步证实了每个组件的有效性，而错误分析表明，与基线相比，CapPO显著减少了与感知相关的错误。总的来说，CapPO为提高多模态推理提供了一个简单而有效的框架。

## 🔬 方法详解

**问题定义**：多模态大语言模型在处理视觉信息进行推理时，容易受到视觉感知误差的影响，这些误差会沿着推理链传播，导致最终结果错误。现有的强化学习微调方法虽然可以提升模型的推理能力，但往往忽略了视觉感知与后续推理过程之间的一致性，无法有效解决感知误差带来的问题。

**核心思路**：CapPO的核心思路是通过显式地强制执行感知一致性来提高多模态大语言模型的推理能力。具体来说，它利用图像的Caption信息作为语义锚点，使模型在推理过程中更加依赖于语义上忠实的视觉内容，从而减少感知误差的传播。同时，通过KL散度加权优势估计，强化感知一致的轨迹，抑制虚假相关性。

**技术框架**：CapPO的整体框架基于强化学习，主要包含以下几个模块：1) 多模态大语言模型（如Qwen2.5-VL-7B），作为策略网络；2) Caption生成模块，用于生成图像的Caption；3) Caption一致性正则化模块，用于计算基于原始图像和基于Caption的响应之间的差异；4) KL加权优势估计模块，用于自适应地调整强化信号。训练过程中，模型通过与环境交互生成轨迹，并利用Caption一致性正则化和KL加权优势估计来更新策略网络。

**关键创新**：CapPO的关键创新在于：1) 提出了Caption一致性正则化，通过最小化基于原始图像和基于Caption的响应之间的差异，显式地强制执行感知一致性；2) 提出了KL加权优势估计，通过自适应地调整强化信号，强化感知一致的轨迹，抑制虚假相关性。与现有方法相比，CapPO更加关注视觉感知与推理过程之间的一致性，能够更有效地减少感知误差。

**关键设计**：Caption一致性正则化采用交叉熵损失函数来衡量基于原始图像和基于Caption的响应之间的差异。KL加权优势估计使用KL散度来衡量当前策略与先前策略之间的差异，并将其作为权重来调整优势函数。优势函数的计算采用标准的优势函数估计方法。具体参数设置（如KL散度的系数、优势函数的折扣因子等）需要根据具体任务进行调整。

## 📊 实验亮点

实验结果表明，CapPO在五个数学相关和五个通用推理基准上均取得了显著提升。在数学相关任务上，CapPO比基线模型Qwen2.5-VL-7B提高了+6.0%的准确率，在通用推理任务上提高了+2.4%。消融实验验证了Caption一致性正则化和KL加权优势估计的有效性。错误分析表明，CapPO能够显著减少与感知相关的错误。

## 🎯 应用场景

该研究成果可应用于需要视觉感知和复杂推理的各种场景，例如智能问答、视觉导航、机器人操作等。通过提高多模态大语言模型的感知一致性，可以提升其在这些场景中的可靠性和准确性，从而实现更智能、更安全的应用。

## 📄 摘要（原文）

> While multimodal large language models excel at tasks that integrate visual perception with symbolic reasoning, their performance is often undermined by a critical vulnerability: perception-induced errors that propagate through the reasoning chain. Current reinforcement learning (RL) fine-tuning methods, while enhancing reasoning abilities, largely fail to address the underlying misalignment between visual grounding and the subsequent reasoning process. To address this challenge, we propose \textbf{Caption-Regularized Policy Optimization (CapPO)}, a novel RL framework that explicitly enforces perceptual consistency during policy optimization. CapPO integrates two key mechanisms: (1) a caption-based consistency regularization, which minimizes the divergence between responses conditioned on raw images and those conditioned on captions, thereby anchoring reasoning to semantically faithful visual content; and (2) a KL-weighted advantage estimation scheme, which adaptively scales reinforcement signals to strengthen perceptually consistent trajectories while suppressing spurious correlations. Extensive experiments on five math-focused and five general reasoning benchmarks demonstrate that CapPO achieves competitive performance, yielding gains of +6.0% accuracy on math-related tasks and +2.4% on general reasoning tasks over the base Qwen2.5-VL-7B model. Moreover, ablation studies further confirm the effectiveness of each component, while error analysis reveals that CapPO significantly reduces perception-related mistakes compared with baselines. Overall, CapPO provides a simple yet effective framework for improving multimodal reasoning.

