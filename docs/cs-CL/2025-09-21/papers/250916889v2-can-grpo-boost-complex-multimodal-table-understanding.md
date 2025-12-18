---
layout: default
title: Can GRPO Boost Complex Multimodal Table Understanding?
---

# Can GRPO Boost Complex Multimodal Table Understanding?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16889" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16889v2</a>
  <a href="https://arxiv.org/pdf/2509.16889.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16889v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16889v2', 'Can GRPO Boost Complex Multimodal Table Understanding?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoqiang Kang, Shengen Wu, Zimu Wang, Yilin Liu, Xiaobo Jin, Kaizhu Huang, Wei Wang, Yutao Yue, Xiaowei Huang, Qiufeng Wang

**分类**: cs.CL

**发布日期**: 2025-09-21 (更新: 2025-09-23)

**备注**: EMNLP 2025

**期刊**: EMNLP 2025

---

## 💡 一句话要点

**Table-R1：通过三阶段强化学习提升复杂多模态表格理解能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `表格理解` `强化学习` `多模态学习` `视觉语言模型` `奖励函数设计`

## 📋 核心要点

1. 现有表格理解方法在处理复杂结构和逻辑推理时面临挑战，监督微调虽主流，但强化学习方法受限于初始策略精度和粗糙奖励。
2. Table-R1框架通过预热、感知对齐GRPO和提示补全GRPO三个阶段，克服初始化瓶颈和奖励稀疏性，提升表格理解能力。
3. 实验表明Table-R1显著提升模型在表格推理上的表现，甚至超越了更大的特定表格理解模型，接近闭源模型GPT-4o的性能。

## 📝 摘要（中文）

现有的表格理解方法面临着复杂表格结构和复杂逻辑推理的挑战。虽然监督微调(SFT)在现有研究中占据主导地位，但强化学习(RL)，如Group Relative Policy Optimization (GRPO)，已经显示出潜力，但在表格上下文中，它也面临着初始策略准确率低和粗糙奖励的问题。本文提出了Table-R1，一个三阶段的RL框架，通过以下方式增强多模态表格理解：(1)预热阶段，激发初始感知和推理能力；(2)感知对齐GRPO (PA-GRPO)，它采用连续的树编辑距离相似度(TEDS)奖励来识别表格结构和内容；(3)提示补全GRPO (HC-GRPO)，它利用基于提示引导问题的剩余步骤的细粒度奖励。大量的实验表明，Table-R1可以显著提高模型在内部和外部数据集上的表格推理性能，大大优于SFT和GRPO。值得注意的是，使用Table-R1的Qwen2-VL-7B超过了更大的特定表格理解模型(例如，Table-LLaVA 13B)，甚至在内部数据集上实现了与闭源模型GPT-4o相当的性能，证明了Table-R1的每个阶段在克服初始化瓶颈和奖励稀疏性方面的有效性，从而推进了鲁棒的多模态表格理解。

## 🔬 方法详解

**问题定义**：论文旨在解决复杂多模态表格理解问题。现有方法，特别是基于监督微调(SFT)的方法，在处理复杂表格结构和需要复杂逻辑推理的场景时表现不足。强化学习方法虽然有潜力，但受限于初始策略准确率低和奖励信号稀疏的问题，难以有效训练。

**核心思路**：论文的核心思路是通过一个三阶段的强化学习框架Table-R1，逐步提升模型在表格理解任务中的表现。首先通过预热阶段提升模型的初始感知和推理能力，然后利用感知对齐GRPO和提示补全GRPO两个阶段，分别解决表格结构和内容的识别以及复杂推理问题。这种分阶段的方法旨在克服强化学习中的初始化瓶颈和奖励稀疏性问题。

**技术框架**：Table-R1框架包含三个主要阶段：
1. **Warm-up (预热)**：利用监督学习方法，使模型具备初步的表格感知和推理能力，为后续的强化学习提供一个较好的初始策略。
2. **Perception Alignment GRPO (PA-GRPO)**：使用连续的树编辑距离相似度(TEDS)作为奖励信号，引导模型学习识别表格的结构和内容。TEDS奖励能够更准确地反映模型对表格结构的理解程度。
3. **Hint-Completion GRPO (HC-GRPO)**：利用基于提示引导问题的剩余步骤的细粒度奖励，鼓励模型进行更深入的推理。通过提示信息，模型可以逐步完成复杂的推理任务，并获得相应的奖励。

**关键创新**：Table-R1的关键创新在于其三阶段的强化学习框架，以及针对表格理解任务设计的特定奖励函数。PA-GRPO阶段使用TEDS奖励，能够更准确地评估模型对表格结构的理解。HC-GRPO阶段使用细粒度的剩余步骤奖励，能够有效引导模型进行复杂推理。与传统的单阶段强化学习方法相比，Table-R1能够更好地克服初始化瓶颈和奖励稀疏性问题。

**关键设计**：
* **TEDS奖励**：使用树编辑距离相似度作为PA-GRPO阶段的奖励信号，用于衡量模型预测的表格结构与真实结构之间的相似度。TEDS奖励是连续的，能够提供更丰富的反馈信息。
* **剩余步骤奖励**：在HC-GRPO阶段，根据模型完成提示引导问题的剩余步骤数来设计奖励。剩余步骤越少，奖励越高，鼓励模型更有效地完成推理任务。
* **Qwen2-VL-7B**：选择Qwen2-VL-7B作为基础模型，并在此基础上进行Table-R1的训练。

## 📊 实验亮点

实验结果表明，Table-R1在内部和外部数据集上均显著优于SFT和GRPO方法。特别地，使用Table-R1的Qwen2-VL-7B模型超越了Table-LLaVA 13B等更大的特定表格理解模型，并在内部数据集上取得了与闭源模型GPT-4o相当的性能，验证了Table-R1框架的有效性。

## 🎯 应用场景

该研究成果可应用于智能文档处理、数据分析、问答系统等领域。通过提升表格理解能力，可以更有效地从表格数据中提取信息，支持决策制定和知识发现。未来，该方法有望应用于更复杂的表格场景，例如包含嵌套结构或跨页表格的文档。

## 📄 摘要（原文）

> Existing table understanding methods face challenges due to complex table structures and intricate logical reasoning. While supervised finetuning (SFT) dominates existing research, reinforcement learning (RL), such as Group Relative Policy Optimization (GRPO), has shown promise but struggled with low initial policy accuracy and coarse rewards in tabular contexts. In this paper, we introduce Table-R1, a three-stage RL framework that enhances multimodal table understanding through: (1) Warm-up that prompts initial perception and reasoning capabilities, (2) Perception Alignment GRPO (PA-GRPO), which employs continuous Tree-Edit-Distance Similarity (TEDS) rewards for recognizing table structures and contents, and (3) Hint-Completion GRPO (HC-GRPO), which utilizes fine-grained rewards of residual steps based on the hint-guided question. Extensive experiments demonstrate that Table-R1 can boost the model's table reasoning performance obviously on both held-in and held-out datasets, outperforming SFT and GRPO largely. Notably, Qwen2-VL-7B with Table-R1 surpasses larger specific table understanding models (e.g., Table-LLaVA 13B), even achieving comparable performance to the closed-source model GPT-4o on held-in datasets, demonstrating the efficacy of each stage of Table-R1 in overcoming initialization bottlenecks and reward sparsity, thereby advancing robust multimodal table understanding.

