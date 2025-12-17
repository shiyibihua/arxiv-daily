---
layout: default
title: Learning-based Cooperative Robotic Paper Wrapping: A Unified Control Policy with Residual Force Control
---

# Learning-based Cooperative Robotic Paper Wrapping: A Unified Control Policy with Residual Force Control

**arXiv**: [2511.03181v1](https://arxiv.org/abs/2511.03181) | [PDF](https://arxiv.org/pdf/2511.03181.pdf)

**作者**: Rewida Ali, Cristian C. Beltran-Hernandez, Weiwei Wan, Kensuke Harada

**分类**: cs.RO, cs.LG

**发布日期**: 2025-11-05

---

## 💡 一句话要点

**提出基于学习的协作机器人纸张包装方法，结合残差力控制实现高成功率。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人协作` `变形物体操作` `纸张包装` `模仿学习` `强化学习` `Transformer` `力控制`

## 📋 核心要点

1. 人机协作处理纸张等变形物体时，由于其动态特性难以预测，且需要自适应力控制，协调机器人动作面临挑战。
2. 提出一种基于学习的框架，利用大型语言模型进行任务规划，并结合模仿学习和强化学习训练统一策略，实现纸张包装。
3. 实验表明，该框架在真实包装任务中达到97%的成功率，验证了所提方法的有效性，并减少了对专用模型的需求。

## 📝 摘要（中文）

本文提出了一种基于学习的框架，用于解决人机协作完成纸张包装任务的难题。该框架将大型语言模型（LLM）驱动的高级任务规划器与混合模仿学习（IL）和强化学习（RL）的低级策略相结合。核心是一个名为Sub-task Aware Robotic Transformer (START) 的模型，它从人类演示中学习统一策略。该方法通过在单个模型中捕获整个包装序列中的长程时间依赖性来实现创新。与通常应用于短任务的Action Chunking with Transformer (ACT) 不同，该方法引入了子任务ID，提供了显式的时间基础。实验结果表明，该框架在真实世界的包装任务中实现了97%的成功率，并减少了对专用模型的需求，实现了受控的人工监督，并有效地桥接了高级意图与变形物体操作所需的精细力控制。

## 🔬 方法详解

**问题定义**：论文旨在解决人机协作完成复杂变形物体（如纸张）包装任务的难题。现有方法难以处理纸张的不可预测的动态特性，并且缺乏有效的力控制策略，导致包装质量难以保证。此外，现有方法通常针对特定任务设计，泛化能力较差。

**核心思路**：论文的核心思路是将高级任务规划与低级力控制相结合，利用大型语言模型进行任务分解和规划，然后通过模仿学习和强化学习训练一个统一的策略，使机器人能够模仿人类的包装动作，并根据环境反馈进行调整。通过引入子任务ID，模型能够更好地理解任务的上下文信息，从而提高包装的成功率。

**技术框架**：整体框架包含三个主要模块：1) 基于大型语言模型的任务规划器，用于将包装任务分解为一系列子任务；2) Sub-task Aware Robotic Transformer (START) 模型，用于学习统一的控制策略；3) 残差力控制模块，用于实现精细的力控制。首先，任务规划器根据用户指令生成子任务序列。然后，START模型根据当前状态和子任务ID生成动作指令。最后，残差力控制模块根据动作指令和力传感器反馈，调整机器人的力输出。

**关键创新**：论文的关键创新在于提出了Sub-task Aware Robotic Transformer (START) 模型，该模型能够捕获整个包装序列中的长程时间依赖性，并利用子任务ID提供显式的时间基础。与传统的Action Chunking with Transformer (ACT) 方法相比，START模型能够更好地理解任务的上下文信息，从而提高包装的成功率。此外，该方法还结合了模仿学习和强化学习，使机器人能够从人类演示中学习，并根据环境反馈进行调整。

**关键设计**：START模型采用Transformer架构，输入包括当前状态、子任务ID和历史动作序列。模型输出为机器人的动作指令。损失函数包括模仿学习损失和强化学习奖励。模仿学习损失用于使机器人模仿人类的包装动作，强化学习奖励用于鼓励机器人完成包装任务。残差力控制模块采用PID控制器，根据动作指令和力传感器反馈，调整机器人的力输出。子任务ID采用one-hot编码。

## 📊 实验亮点

实验结果表明，所提出的框架在真实世界的包装任务中实现了97%的成功率。与传统的Action Chunking with Transformer (ACT) 方法相比，该方法能够更好地理解任务的上下文信息，从而提高包装的成功率。此外，该方法还能够实现受控的人工监督，并有效地桥接了高级意图与变形物体操作所需的精细力控制。

## 🎯 应用场景

该研究成果可应用于仓储、零售等领域，实现自动化包装，提高效率并降低人工成本。此外，该方法还可扩展到其他变形物体的操作任务，如服装折叠、食品包装等。未来，该技术有望应用于更复杂的机器人协作任务，例如医疗手术、灾难救援等。

## 📄 摘要（原文）

> Human-robot cooperation is essential in environments such as warehouses and retail stores, where workers frequently handle deformable objects like paper, bags, and fabrics. Coordinating robotic actions with human assistance remains difficult due to the unpredictable dynamics of deformable materials and the need for adaptive force control. To explore this challenge, we focus on the task of gift wrapping, which exemplifies a long-horizon manipulation problem involving precise folding, controlled creasing, and secure fixation of paper. Success is achieved when the robot completes the sequence to produce a neatly wrapped package with clean folds and no tears.
>   We propose a learning-based framework that integrates a high-level task planner powered by a large language model (LLM) with a low-level hybrid imitation learning (IL) and reinforcement learning (RL) policy. At its core is a Sub-task Aware Robotic Transformer (START) that learns a unified policy from human demonstrations. The key novelty lies in capturing long-range temporal dependencies across the full wrapping sequence within a single model. Unlike vanilla Action Chunking with Transformer (ACT), typically applied to short tasks, our method introduces sub-task IDs that provide explicit temporal grounding. This enables robust performance across the entire wrapping process and supports flexible execution, as the policy learns sub-goals rather than merely replicating motion sequences.
>   Our framework achieves a 97% success rate on real-world wrapping tasks. We show that the unified transformer-based policy reduces the need for specialized models, allows controlled human supervision, and effectively bridges high-level intent with the fine-grained force control required for deformable object manipulation.

