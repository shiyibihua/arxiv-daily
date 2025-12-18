---
layout: default
title: Revolutionizing Reinforcement Learning Framework for Diffusion Large Language Models
---

# Revolutionizing Reinforcement Learning Framework for Diffusion Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06949" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06949v1</a>
  <a href="https://arxiv.org/pdf/2509.06949.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06949v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06949v1', 'Revolutionizing Reinforcement Learning Framework for Diffusion Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yinjie Wang, Ling Yang, Bowen Li, Ye Tian, Ke Shen, Mengdi Wang

**分类**: cs.CL

**发布日期**: 2025-09-08

**备注**: Code and Models: https://github.com/Gen-Verse/dLLM-RL

**🔗 代码/项目**: [GITHUB](https://github.com/Gen-Verse/dLLM-RL)

---

## 💡 一句话要点

**TraceRL：面向扩散语言模型的轨迹感知强化学习框架，提升推理性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散语言模型` `强化学习` `轨迹感知` `数学推理` `代码生成`

## 📋 核心要点

1. 现有语言模型在复杂推理任务中面临挑战，尤其是在数学和编码等领域，需要更有效的训练方法。
2. TraceRL通过将偏好的推理轨迹融入扩散语言模型的后训练中，并结合扩散值模型，提升训练稳定性和推理性能。
3. 实验结果表明，TraDo模型在数学推理任务上显著优于同等规模的自回归模型，并在长文本CoT任务上取得突破。

## 📝 摘要（中文）

本文提出TraceRL，一种轨迹感知的扩散语言模型（DLM）强化学习框架，它将偏好的推理轨迹融入到后训练中，并且适用于不同的架构。该框架配备了基于扩散的值模型，增强了训练的稳定性。实验表明，TraceRL改进了复杂数学和编码任务的推理性能。此外，它还可以应用于将特定块的模型适配到更大的块，从而提高采样灵活性。使用TraceRL，我们得到了一系列最先进的扩散语言模型，即TraDo。TraDo-4B-Instruct虽然小于7B规模的AR模型，但在复杂的数学推理任务中仍然始终优于它们。TraDo-8B-Instruct在数学推理基准测试中，相对于Qwen2.5-7B-Instruct和Llama3.1-8B-Instruct，分别实现了6.1%和51.3%的相对准确率提升。通过课程学习，我们还得到了第一个长CoT DLM，在MATH500上优于Qwen2.5-7B-Instruct，相对准确率提升了18.1%。为了方便可复现的研究和实际应用，我们发布了一个全面的开源框架，用于构建、训练和部署各种架构的扩散LLM。该框架集成了加速KV-cache技术和推理引擎，用于推理和强化学习，并包括各种监督微调和RL方法的实现，适用于数学、编码和通用任务。

## 🔬 方法详解

**问题定义**：现有语言模型，特别是自回归模型，在处理复杂的推理任务，如数学问题和代码生成时，往往需要大量的参数和计算资源才能达到较好的性能。此外，如何有效地利用强化学习来优化扩散语言模型，使其更好地遵循期望的推理路径，是一个挑战。

**核心思路**：TraceRL的核心思路是将强化学习与扩散语言模型相结合，通过学习“轨迹”来引导模型的生成过程。具体来说，它通过一个扩散值模型来评估生成轨迹的质量，并使用强化学习算法来优化模型，使其更倾向于生成高质量的轨迹。这种方法能够有效地利用数据中的信息，提高模型的推理能力。

**技术框架**：TraceRL框架主要包含以下几个模块：1) 扩散语言模型：作为生成模型，负责生成文本序列。2) 扩散值模型：用于评估生成轨迹的质量，输出一个奖励信号。3) 强化学习算法：利用奖励信号来优化扩散语言模型，使其更倾向于生成高质量的轨迹。整个训练过程是一个迭代的过程，扩散语言模型生成轨迹，扩散值模型评估轨迹，强化学习算法利用评估结果更新模型。

**关键创新**：TraceRL的关键创新在于将轨迹信息融入到扩散语言模型的强化学习训练中。传统的强化学习方法通常只关注最终的输出结果，而忽略了生成过程中的中间步骤。TraceRL通过学习轨迹，能够更有效地利用数据中的信息，提高模型的推理能力。此外，扩散值模型的使用也增强了训练的稳定性。

**关键设计**：TraceRL的关键设计包括：1) 扩散值模型的构建：扩散值模型需要能够准确地评估生成轨迹的质量。论文中可能使用了特定的网络结构和损失函数来实现这一目标。2) 强化学习算法的选择：论文中可能使用了特定的强化学习算法，如PPO或SAC，来优化扩散语言模型。3) 奖励函数的设计：奖励函数需要能够有效地引导模型生成高质量的轨迹。论文中可能使用了多种奖励信号，如正确率、流畅度等。

## 📊 实验亮点

TraDo-4B-Instruct在数学推理任务上优于7B规模的自回归模型。TraDo-8B-Instruct在数学推理基准测试中，相对于Qwen2.5-7B-Instruct和Llama3.1-8B-Instruct，分别实现了6.1%和51.3%的相对准确率提升。在MATH500上，相对于Qwen2.5-7B-Instruct，相对准确率提升了18.1%。

## 🎯 应用场景

TraceRL具有广泛的应用前景，包括但不限于：数学问题求解、代码生成、自然语言推理、对话系统等。通过优化扩散语言模型的推理能力，可以提升这些应用在复杂任务上的性能。此外，该框架还可以用于构建更高效、更灵活的语言模型，推动人工智能技术的发展。

## 📄 摘要（原文）

> We propose TraceRL, a trajectory-aware reinforcement learning framework for diffusion language models (DLMs) that incorporates preferred inference trajectory into post-training, and is applicable across different architectures. Equipped with a diffusion-based value model that enhances training stability, we demonstrate improved reasoning performance on complex math and coding tasks. Besides, it can also be applied to adapt block-specific models to larger blocks, which improves sampling flexibility. Employing TraceRL, we derive a series of state-of-the-art diffusion language models, namely TraDo. Although smaller than 7B-scale AR models, TraDo-4B-Instruct still consistently outperforms them across complex math reasoning tasks. TraDo-8B-Instruct achieves relative accuracy improvements of 6.1% over Qwen2.5-7B-Instruct and 51.3% over Llama3.1-8B-Instruct on mathematical reasoning benchmarks. Through curriculum learning, we also derive the first long-CoT DLM, outperforming Qwen2.5-7B-Instruct on MATH500 with an 18.1% relative accuracy gain. To facilitate reproducible research and practical applications, we release a comprehensive open-source framework for building, training, and deploying diffusion LLMs across diverse architectures. The framework integrates accelerated KV-cache techniques and inference engines for both inference and reinforcement learning, and includes implementations of various supervised fine-tuning and RL methods for mathematics, coding, and general tasks. Code and Models: https://github.com/Gen-Verse/dLLM-RL

