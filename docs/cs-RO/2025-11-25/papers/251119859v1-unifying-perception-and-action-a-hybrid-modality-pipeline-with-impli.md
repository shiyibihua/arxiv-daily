---
layout: default
title: Unifying Perception and Action: A Hybrid-Modality Pipeline with Implicit Visual Chain-of-Thought for Robotic Action Generation
---

# Unifying Perception and Action: A Hybrid-Modality Pipeline with Implicit Visual Chain-of-Thought for Robotic Action Generation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.19859" target="_blank" class="toolbar-btn">arXiv: 2511.19859v1</a>
    <a href="https://arxiv.org/pdf/2511.19859.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.19859v1" 
            onclick="toggleFavorite(this, '2511.19859v1', 'Unifying Perception and Action: A Hybrid-Modality Pipeline with Implicit Visual Chain-of-Thought for Robotic Action Generation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Xiangkai Ma, Lekai Xing, Han Zhang, Wenzhong Li, Sanglu Lu

**分类**: cs.RO

**发布日期**: 2025-11-25

---

## 💡 一句话要点

**提出VITA框架，通过隐式视觉CoT统一感知与动作，提升机器人动作生成能力。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人操作` `视觉语言动作模型` `链式思考` `隐式视觉推理` `轨迹对齐`

## 📋 核心要点

1. 现有VLA模型在复杂空间环境中难以充分捕捉场景细节，文本CoT存在局限性，视觉先验利用不足。
2. VITA框架通过学习视觉和动作的共享离散潜在空间，并引入隐式视觉CoT，实现感知和动作的统一建模。
3. 实验结果表明，VITA在多个benchmark上超越现有方法，并在真实世界任务中表现出良好的泛化能力。

## 📝 摘要（中文）

本文提出了一种视觉集成轨迹对齐（VITA）框架，旨在解决视觉-语言-动作（VLA）模型中视觉信息利用不足和训练不稳定的问题。VITA通过学习视觉和动作的共享离散潜在空间，实现感知和运动控制的联合建模。该框架引入隐式视觉CoT，自回归地生成token，并同时解码为未来帧预测和机器人动作，从而将视觉动态作为运动规划的归纳偏置。在模拟和真实环境中的大量实验表明，VITA取得了最先进的性能，在CALVIN、LIBERO和SimplerEnv上分别比现有基线提高了14.5%、9.6%和12.1%。此外，VITA在六个真实世界任务中实现了平均80.5%的成功率，展示了其作为通用机器人操作模型的潜力。

## 🔬 方法详解

**问题定义**：现有基于视觉-语言-动作（VLA）模型的机器人操作方法，特别是那些依赖于Chain-of-Thought (CoT) 的方法，在复杂环境中难以充分利用视觉信息。文本CoT难以捕捉细致的场景信息，而直接将视觉信息融入动作生成又面临模态差异和训练不稳定的问题，即视觉预测和动作生成的目标相互竞争。

**核心思路**：VITA的核心思路是学习一个视觉和动作的共享离散潜在空间，从而将视觉信息有效地融入到动作生成过程中。通过隐式视觉CoT，模型能够自回归地生成token，这些token既用于预测未来的视觉帧，又用于生成机器人动作。这种设计将视觉动态作为运动规划的归纳偏置，从而提高了动作生成的稳定性和准确性。

**技术框架**：VITA框架包含以下主要模块：1) 视觉编码器，用于提取视觉特征；2) 动作编码器，用于编码动作序列；3) 共享离散潜在空间，用于对视觉和动作信息进行统一表示；4) 自回归解码器，用于生成隐式视觉CoT token，并将其解码为未来帧预测和机器人动作。整个流程是端到端可训练的。

**关键创新**：VITA最重要的技术创新点在于隐式视觉CoT的引入。与显式地生成文本形式的CoT不同，VITA通过自回归地生成token，并将这些token同时用于视觉预测和动作生成，从而实现了视觉信息和动作生成的紧密耦合。这种隐式的方式避免了文本CoT可能带来的信息损失和歧义，并提高了模型的效率和鲁棒性。

**关键设计**：VITA的关键设计包括：1) 使用Transformer架构作为视觉和动作编码器和解码器；2) 采用离散变分自编码器（VAE）学习共享离散潜在空间；3) 使用交叉熵损失函数训练自回归解码器，同时优化未来帧预测和动作生成的准确性；4) 通过调整视觉预测和动作生成损失的权重，平衡两个目标之间的竞争关系。

## 📊 实验亮点

VITA在CALVIN、LIBERO和SimplerEnv等模拟环境benchmark上取得了显著的性能提升，分别比现有基线提高了14.5%、9.6%和12.1%。更重要的是，VITA在六个真实世界机器人操作任务中实现了平均80.5%的成功率，证明了其在真实环境中的泛化能力和实用价值。这些实验结果表明，VITA是目前最先进的通用机器人操作模型之一。

## 🎯 应用场景

VITA框架具有广泛的应用前景，可应用于各种机器人操作任务，如家庭服务机器人、工业自动化机器人、医疗机器人等。该研究有助于提升机器人在复杂环境中的感知和决策能力，实现更智能、更自主的机器人操作。未来，VITA可以进一步扩展到多模态输入（如语音、触觉）和更复杂的任务场景。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models built upon Chain-of-Thought (CoT) have achieved remarkable success in advancing general-purpose robotic agents, owing to its significant perceptual comprehension. Recently, since text-only CoT struggles to adequately capture scene details in complex spatial environments, a highly promising strategy involves leveraging visual priors to guide robotic action generation. Nevertheless, these strategies face two inherent challenges: (i) a modality gap between visual observations and low-level actions, and (ii) unstable training due to competing objectives between visual prediction and action generation. To address these challenges, we propose a Vision-Integrated Trajectory Alignment (VITA) framework that learns a shared discrete latent space for vision and action, enabling joint modeling of perception and motor control. VITA introduces a implicit visual CoT: autoregressively generated tokens is simultaneously decoded into future frames predictions and robot actions, thereby internalizing visual dynamics as an inductive bias for motion planning. Extensive experiments on simulated and real-world environments demonstrate state-of-the-art performance. VITA improves 14.5\%, 9.6\% and 12.1\% over existing baselines on CALVIN, LIBERO and SimplerEnv. Furthermore, VITA attains an average success rate of 80.5\% across six real-world tasks, demonstrating its potential as a generalist robotic manipulation model.

