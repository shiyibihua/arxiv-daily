---
layout: default
title: Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents
---

# Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14480" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14480v1</a>
  <a href="https://arxiv.org/pdf/2509.14480.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14480v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14480v1', 'Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weiting Tan, Xinghua Qu, Ming Tu, Meng Ge, Andy T. Liu, Philipp Koehn, Lu Lu

**分类**: cs.CL, cs.AI, cs.MA

**发布日期**: 2025-09-17

---

## 💡 一句话要点

**提出Turn-level Adjudicated RL，解决交互式多模态工具使用Agent的训练难题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `多模态学习` `工具使用` `人机交互` `大型语言模型` `信用分配` `交互式Agent`

## 📋 核心要点

1. 现有交互式工具使用Agent在多轮规划和长上下文对话管理方面面临挑战，尤其是在多模态环境中。
2. 提出Turn-level Adjudicated Reinforcement Learning (TARL)，利用LLM进行turn-level评估，解决长时程任务中的信用分配问题。
3. 通过混合任务训练课程，在文本基准测试中任务通过率提升超过6%，并验证了框架在多模态Agent微调中的有效性。

## 📝 摘要（中文）

本文提出了一种用于训练交互式多模态工具使用Agent的强化学习框架。该框架专注于工具集成推理(TIR)，这是一个涉及多轮规划和长上下文对话管理的复杂过程。为了训练Agent处理这种动态过程，特别是在多模态环境中，我们引入了一个支持交错语音-文本rollout的强化学习sandbox环境。我们的核心策略，Turn-level Adjudicated Reinforcement Learning (TARL)，通过使用大型语言模型(LLM)作为裁判来提供turn-level评估，从而解决了长时程任务中的信用分配问题。为了增强探索，我们整合了一个混合任务训练课程，其中包含数学推理问题。这种统一的方法使基于文本的$τ$-bench上的任务通过率比强大的RL基线提高了6%以上。至关重要的是，我们证明了我们的框架适用于微调多模态基础模型以用于Agent任务。通过在交错的语音-文本rollout上训练基础多模态LLM，我们使其具备了工具使用能力，为更自然的、语音驱动的交互式Agent铺平了道路。

## 🔬 方法详解

**问题定义**：现有交互式工具使用Agent在处理复杂任务时，面临工具集成推理(TIR)的挑战，具体表现为多轮规划和长上下文对话管理的困难。尤其是在多模态环境下，Agent需要同时理解和处理语音和文本信息，这进一步加剧了训练的复杂性。传统的强化学习方法在长时程任务中存在信用分配问题，难以有效指导Agent的学习。

**核心思路**：本文的核心思路是利用大型语言模型(LLM)的强大推理能力，将其作为裁判，对Agent在每个turn的行为进行评估，从而实现更精确的信用分配。这种Turn-level Adjudicated Reinforcement Learning (TARL)方法能够更有效地指导Agent在长时程任务中的学习，并提高其工具使用能力。同时，通过混合任务训练课程，增强Agent的探索能力，使其能够更好地适应不同的任务场景。

**技术框架**：整体框架包含一个强化学习sandbox环境，支持交错的语音-文本rollout。Agent与环境进行交互，生成语音和文本序列。LLM裁判对Agent在每个turn的行为进行评估，生成奖励信号。强化学习算法利用这些奖励信号更新Agent的策略。此外，还引入了混合任务训练课程，包含数学推理等任务，以增强Agent的探索能力。

**关键创新**：最重要的技术创新点在于Turn-level Adjudicated Reinforcement Learning (TARL)方法。与传统的强化学习方法相比，TARL能够更精确地进行信用分配，从而更有效地指导Agent的学习。此外，利用LLM作为裁判，避免了人工设计奖励函数的困难，并能够更好地适应不同的任务场景。

**关键设计**：LLM裁判的设计是关键。需要选择合适的LLM，并设计合适的prompt，使其能够准确评估Agent的行为。混合任务训练课程的设计也需要仔细考虑，需要选择与目标任务相关的任务，并合理安排训练顺序。具体的参数设置和网络结构等技术细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，提出的TARL方法在基于文本的$τ$-bench上，任务通过率比强大的RL基线提高了6%以上。此外，通过在交错的语音-文本rollout上训练基础多模态LLM，使其具备了工具使用能力，验证了该框架适用于微调多模态基础模型以用于Agent任务。

## 🎯 应用场景

该研究成果可应用于开发更智能、更自然的交互式Agent，例如智能助手、客服机器人等。这些Agent能够理解用户的语音和文本指令，并利用各种工具完成复杂的任务。尤其是在需要多轮交互和长上下文理解的场景下，该方法具有显著优势。未来，该技术有望推动人机交互方式的变革，使人们能够更方便地使用各种工具和服务。

## 📄 摘要（原文）

> Effective interactive tool use requires agents to master Tool Integrated Reasoning (TIR): a complex process involving multi-turn planning and long-context dialogue management. To train agents for this dynamic process, particularly in multi-modal contexts, we introduce a sandbox environment for reinforcement learning (RL) that supports interleaved speech-text rollouts. Our core strategy, Turn-level Adjudicated Reinforcement Learning (TARL), addresses the challenge of credit assignment in long-horizon tasks by employing a Large Language Model (LLM) as a judge to provide turn-level evaluation. To enhance exploration, we integrate a mixed-task training curriculum with mathematical reasoning problems. This unified approach boosts the task pass rate on the text-based $τ$-bench by over 6% compared to strong RL baselines. Crucially, we demonstrate our framework's suitability for fine-tuning a multi-modal foundation model for agentic tasks. By training a base multi-modal LLM on interleaved speech-text rollouts, we equip it with tool-use abilities, paving the way for more natural, voice-driven interactive agents.

