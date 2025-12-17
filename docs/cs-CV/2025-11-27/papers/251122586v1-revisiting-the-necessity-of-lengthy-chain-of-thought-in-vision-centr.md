---
layout: default
title: Revisiting the Necessity of Lengthy Chain-of-Thought in Vision-centric Reasoning Generalization
---

# Revisiting the Necessity of Lengthy Chain-of-Thought in Vision-centric Reasoning Generalization

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.22586" target="_blank" class="toolbar-btn">arXiv: 2511.22586v1</a>
    <a href="https://arxiv.org/pdf/2511.22586.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.22586v1" 
            onclick="toggleFavorite(this, '2511.22586v1', 'Revisiting the Necessity of Lengthy Chain-of-Thought in Vision-centric Reasoning Generalization')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yifan Du, Kun Zhou, Yingqian Min, Yue Ling, Wayne Xin Zhao, Youbin Wu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-27

---

## 💡 一句话要点

**研究表明，在视觉推理泛化中，简洁的思维链（CoT）优于冗长的CoT。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `视觉推理` `思维链` `视觉语言模型` `泛化能力` `迷宫求解`

## 📋 核心要点

1. 现有视觉语言模型依赖冗长的思维链进行视觉推理，但其必要性和泛化能力有待考察。
2. 论文提出通过对比不同CoT格式（语言、接地、视觉）在迷宫求解任务中的表现，探究CoT设计对泛化能力的影响。
3. 实验表明，简洁的、仅包含必要接地步骤的CoT，在不同迷宫尺寸上表现出最佳的泛化能力。

## 📝 摘要（中文）

本文研究了不同的思维链（CoT）设计如何影响视觉语言模型（VLMs）中可泛化的视觉推理能力的获取。尽管CoT数据，特别是长CoT或视觉CoT（如“think with image”）已被广泛用于监督中间推理过程，但尚不清楚为什么特定的CoT设计有效，以及哪些设计真正支持可泛化的推理。为了系统地评估这一点，我们专注于一个受控的迷宫求解基准，其中推理规则完全是视觉的，难度可以通过网格大小进行调整，并且所有中间步骤都可以自动生成。使用Qwen2.5-VL-7B在标准的SFT-then-RL流程下，我们比较了三种具有代表性的CoT格式：语言CoT、带有空间坐标轨迹的接地CoT和带有图像操作的视觉CoT。实验表明，视觉和较长的CoT主要加速收敛，但不会提高最终性能上限；包含基本接地步骤的简洁CoT优于较长的轨迹；并且，令人惊讶的是，仅保留最小接地结果的CoT在不同的迷宫尺寸上泛化效果最好。我们进一步在其他以视觉为中心的任务上验证了这些见解。这些发现强调了一种“短即是长”的效应，并为构建更具泛化性的视觉推理SFT数据集提供了实践指导。

## 🔬 方法详解

**问题定义**：现有视觉语言模型在视觉推理任务中，通常采用冗长的思维链（Chain-of-Thought, CoT）数据进行训练，以期获得更好的推理能力。然而，这些冗长的CoT是否真正必要，以及哪种CoT设计能够更好地支持泛化能力，仍然是一个开放问题。现有方法缺乏对不同CoT设计进行系统性的评估，难以指导更有效的视觉推理模型训练。

**核心思路**：论文的核心思路是通过对比不同类型的CoT数据在视觉推理任务中的表现，来揭示CoT设计对泛化能力的影响。具体来说，论文设计了一个受控的迷宫求解环境，并比较了语言CoT、接地CoT（包含空间坐标轨迹）和视觉CoT（包含图像操作）三种CoT格式。通过分析不同CoT格式对模型性能的影响，从而找到更有效的CoT设计方案。

**技术框架**：论文采用标准的SFT-then-RL（Supervised Fine-Tuning followed by Reinforcement Learning）流程。首先，使用不同类型的CoT数据对Qwen2.5-VL-7B模型进行监督微调（SFT）。然后，使用强化学习（RL）进一步优化模型的推理能力。在迷宫求解环境中，模型需要根据视觉输入，逐步推理出到达目标位置的路径。

**关键创新**：论文的关键创新在于发现“短即是长”的效应，即简洁的、仅包含必要接地步骤的CoT，在视觉推理任务中能够获得更好的泛化能力。这与以往认为更长、更复杂的CoT能够提升推理能力的观点不同。

**关键设计**：论文的关键设计包括：1) 设计了一个可控的迷宫求解环境，可以自动生成不同难度的迷宫和对应的CoT数据；2) 比较了三种具有代表性的CoT格式：语言CoT、接地CoT和视觉CoT；3) 使用Qwen2.5-VL-7B模型和标准的SFT-then-RL流程进行实验。

## 📊 实验亮点

实验结果表明，在迷宫求解任务中，简洁的接地CoT优于冗长的视觉CoT和语言CoT。具体来说，仅保留最小接地结果的CoT在不同迷宫尺寸上表现出最佳的泛化能力。这一发现挑战了以往认为更长CoT更有效的观点，并为构建更具泛化性的视觉推理SFT数据集提供了实践指导。

## 🎯 应用场景

该研究成果可应用于提升视觉语言模型在各种视觉推理任务中的泛化能力，例如机器人导航、图像理解、视觉问答等。通过采用更简洁有效的CoT数据进行训练，可以降低模型对训练数据的依赖，提高模型在实际应用中的鲁棒性和适应性。该研究为构建更通用的视觉推理系统提供了新的思路。

## 📄 摘要（原文）

> We study how different Chain-of-Thought (CoT) designs affect the acquisition of the generalizable visual reasoning ability in vision-language models (VLMs). While CoT data, especially long or visual CoT such as "think with image", has been widely used to supervise intermediate reasoning, it remains unclear why specific CoT designs help and which ones truly support generalizable reasoning. To systematically evaluate this, we focus on a controlled maze-solving benchmark where reasoning rules are fully visual, difficulty can be tuned by grid size, and all the intermediate steps can be automatically generated. Using Qwen2.5-VL-7B under a standard SFT-then-RL pipeline, we compare three representative CoT formats: Language CoT, Grounding CoT (with spatial coordinate trajectories), and Visual CoT (with image manipulations). Our experiments reveal that visual and longer CoT mainly accelerate convergence but do not lift the final performance ceiling; concise CoT containing only essential grounding steps outperforms longer traces; and, strikingly, CoT retaining only the minimal grounding results generalizes best across different maze sizes. We further validate these insights on other vision-centric tasks. These findings highlight a "short is long" effect and provide practical guidance for constructing more generalizable SFT datasets for visual reasoning.

