---
layout: default
title: Inpainting-Guided Policy Optimization for Diffusion Large Language Models
---

# Inpainting-Guided Policy Optimization for Diffusion Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10396" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10396v1</a>
  <a href="https://arxiv.org/pdf/2509.10396.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10396v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10396v1', 'Inpainting-Guided Policy Optimization for Diffusion Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siyan Zhao, Mengchen Liu, Jing Huang, Miao Liu, Chenyu Wang, Bo Liu, Yuandong Tian, Guan Pang, Sean Bell, Aditya Grover, Feiyu Chen

**分类**: cs.LG

**发布日期**: 2025-09-12

**备注**: preprint; 21 pages

---

## 💡 一句话要点

**提出IGPO：利用Inpainting引导扩散LLM的强化学习策略优化**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散模型` `强化学习` `策略优化` `图像修复` `大语言模型` `数学问题求解` `样本效率` `探索引导`

## 📋 核心要点

1. 现有强化学习对齐LLM方法面临探索挑战，奖励稀疏且样本效率低，尤其是在模型难以找到正确解时。
2. IGPO利用dLLM的图像修复能力，在在线采样中策略性地插入部分ground-truth推理轨迹，引导探索并保留自我生成推理。
3. 通过IGPO及其他技术，在GSM8K、Math500和AMC等数学基准测试中，全注意力掩码dLLM取得了新的state-of-the-art结果。

## 📝 摘要（中文）

本文提出了一种针对掩码扩散大语言模型(dLLMs)的强化学习算法，该模型作为自回归LLMs的有前景的替代方案，在提供有竞争力的性能的同时，支持独特的生成能力，例如图像修复。我们探索了图像修复如何为dLLMs的RL算法设计提供信息。将LLMs与强化学习对齐面临着探索挑战：稀疏的奖励信号和模型未能发现正确解决方案时的样本浪费。虽然这种低效率广泛影响LLMs，但dLLMs提供了一个独特的机会——它们的图像修复能力可以指导探索。我们引入了IGPO（Inpainting Guided Policy Optimization），这是一个RL框架，它在在线采样期间策略性地插入部分ground-truth推理轨迹。与提供完整解决方案不同，图像修复将探索引导到有希望的轨迹空间，同时保留自我生成的推理，从而弥合了监督微调和强化学习之间的差距。我们将IGPO应用于基于组的优化方法，例如GRPO，其中探索失败会导致零优势和梯度。IGPO恢复了有意义的梯度，同时提高了样本效率。我们还提出了对合成重写的简洁轨迹进行监督微调，这些轨迹更好地与dLLM生成模式对齐。通过包括基于熵的过滤在内的其他技术，我们的训练方法在三个数学基准（GSM8K、Math500 和 AMC）上产生了显着收益，为全注意力掩码dLLM实现了新的最先进的结果。

## 🔬 方法详解

**问题定义**：现有基于强化学习的LLM对齐方法，在面对复杂任务和稀疏奖励时，存在探索效率低下的问题。模型难以找到正确的推理路径，导致大量的样本浪费和无效的梯度更新。尤其是在基于组的优化方法中，探索失败会导致零优势和梯度，严重影响学习效果。

**核心思路**：论文的核心思路是利用dLLM的图像修复能力来引导强化学习的探索过程。通过在采样过程中策略性地插入部分ground-truth推理轨迹，可以有效地将模型引导到更有希望的轨迹空间，从而提高探索效率和样本利用率。这种方法既能利用监督学习的先验知识，又能保留强化学习的自我生成推理能力。

**技术框架**：IGPO框架主要包含以下几个阶段：1) 使用dLLM生成推理轨迹；2) 策略性地选择部分推理步骤，用ground-truth进行修复（inpainting）；3) 使用修复后的轨迹进行策略优化，例如使用GRPO等方法；4) 结合其他技术，如基于熵的过滤，进一步提升性能。整体流程是在线采样和策略更新的循环迭代。

**关键创新**：IGPO的关键创新在于将dLLM的图像修复能力与强化学习的探索过程相结合。与传统的强化学习方法相比，IGPO能够更有效地引导模型探索，避免陷入局部最优解。与完全依赖监督学习的方法相比，IGPO能够保留模型的自我生成推理能力，使其能够适应更复杂和未知的环境。

**关键设计**：IGPO的关键设计包括：1) 如何选择需要修复的推理步骤，例如可以根据模型的不确定性或奖励信号来选择；2) 如何平衡修复的程度，避免过度依赖ground-truth，从而限制模型的探索能力；3) 如何设计奖励函数，鼓励模型生成更符合逻辑和更有效的推理轨迹；4) 结合监督微调，利用合成重写的简洁轨迹来更好地对齐dLLM的生成模式。

## 📊 实验亮点

IGPO在GSM8K、Math500和AMC三个数学基准测试中取得了显著的性能提升，为全注意力掩码dLLM实现了新的state-of-the-art结果。具体的数据提升幅度未知，但摘要中强调了“substantial gains”，表明性能提升是显著的。此外，论文还强调了IGPO能够恢复有意义的梯度，同时提高样本效率。

## 🎯 应用场景

该研究成果可应用于各种需要复杂推理和决策的自然语言处理任务，例如数学问题求解、代码生成、知识图谱推理等。通过提高LLM的探索效率和样本利用率，可以降低训练成本，并提升模型在实际应用中的性能和鲁棒性。该方法还可能促进更通用和智能的AI系统的发展。

## 📄 摘要（原文）

> Masked diffusion large language models (dLLMs) are emerging as promising alternatives to autoregressive LLMs, offering competitive performance while supporting unique generation capabilities such as inpainting. We explore how inpainting can inform RL algorithm design for dLLMs. Aligning LLMs with reinforcement learning faces an exploration challenge: sparse reward signals and sample waste when models fail to discover correct solutions. While this inefficiency affects LLMs broadly, dLLMs offer a distinctive opportunity--their inpainting ability can guide exploration. We introduce IGPO (Inpainting Guided Policy Optimization), an RL framework that strategically inserts partial ground-truth reasoning traces during online sampling. Unlike providing full solutions, inpainting steers exploration toward promising trajectory spaces while preserving self-generated reasoning, bridging supervised fine-tuning and reinforcement learning. We apply IGPO to group-based optimization methods such as GRPO, where exploration failures cause zero advantages and gradients. IGPO restores meaningful gradients while improving sample efficiency. We also propose supervised fine-tuning on synthetically rewritten concise traces that better align with dLLM generation patterns. With additional techniques including entropy-based filtering, our training recipe yields substantial gains across three mathematical benchmarks--GSM8K, Math500, and AMC--achieving new state-of-the-art results for full-attention masked dLLMs.

