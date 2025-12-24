---
layout: default
title: Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning
---

# Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03501" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03501v2</a>
  <a href="https://arxiv.org/pdf/2508.03501.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03501v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03501v2', 'Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alexander Golubev, Maria Trofimova, Sergei Polezhaev, Ibragim Badertdinov, Maksim Nekrashevich, Anton Shevtsov, Simon Karasik, Sergey Abramov, Andrei Andriushchenko, Filipp Fisin, Sergei Skvortsov, Boris Yangel

**分类**: cs.LG, cs.CL, cs.SE

**发布日期**: 2025-08-05 (更新: 2025-10-10)

---

## 💡 一句话要点

**提出强化学习方法以解决软件工程中的多轮交互问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `多轮交互` `软件工程` `拒绝微调` `执行反馈` `动态策略优化` `大型语言模型`

## 📋 核心要点

1. 现有的强化学习方法多集中于单轮交互，缺乏对多轮状态反馈的处理，导致在软件工程等复杂领域的应用效果不佳。
2. 本文提出了一种新的方法，通过拒绝微调和同步强化学习管道，利用执行反馈来训练能够有效处理多轮交互的代理。
3. 实验结果表明，所提出的方法在多个基准测试中显著提升了模型的性能，尤其是在SWE-bench和SWE-rebench上达到了竞争水平。

## 📝 摘要（中文）

在强化学习（RL）应用于大型语言模型的研究中，主要集中于单轮问题，如数学推理或单次代码生成。然而，这些问题可以视为多轮马尔可夫决策过程的简化情况，与软件工程等真实世界领域的多轮交互需求相悖。为此，本文展示了RL在这一广泛场景中的成功应用。我们的方法首先通过执行反馈进行拒绝微调（RFT），训练策略有效地遵循指令和格式，随后采用同步RL管道进行迭代改进。将该管道应用于Qwen2.5-72B-Instruct，我们在SWE-bench Verified基准上的Pass@1从11%提升至39%，显著优于20%的RFT基线。最终代理在SWE-rebench的May和June分割上分别达到了35%和31%的Pass@1，表现出色，甚至与更大模型如DeepSeek-V3-0324或Qwen3-235B-A22B相竞争，表明我们的方法为训练多轮交互任务的能力代理提供了实用的解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决现有强化学习方法在软件工程领域多轮交互中的不足，尤其是缺乏有效的状态反馈机制。现有方法多集中于单轮问题，无法适应复杂的多轮交互场景。

**核心思路**：论文提出通过拒绝微调（RFT）结合执行反馈，训练模型遵循指令和格式，随后使用同步强化学习（RL）管道进行迭代改进，以提升模型在多轮交互中的表现。

**技术框架**：整体方法分为两个主要阶段：第一阶段是拒绝微调，利用执行反馈优化策略；第二阶段是同步RL管道，采用DAPO（Dynamic Action Policy Optimization）进行持续改进。

**关键创新**：最重要的创新在于将强化学习有效应用于多轮交互场景，尤其是通过执行反馈的拒绝微调，显著提升了模型的指令遵循能力和格式化效果。

**关键设计**：在参数设置上，采用了特定的损失函数来优化指令遵循的准确性，网络结构则基于大型语言模型进行调整，以适应多轮交互的需求。

## 📊 实验亮点

实验结果显示，所提出的方法在SWE-bench Verified基准上的Pass@1从11%提升至39%，在SWE-rebench的May和June分割上分别达到了35%和31%的Pass@1，表现优于20%的RFT基线，展现出强大的竞争力。

## 🎯 应用场景

该研究的潜在应用领域包括软件工程中的自动化代码生成、调试和优化等任务。通过提升模型在多轮交互中的表现，可以显著提高开发效率，降低人力成本，未来可能在智能编程助手等领域发挥重要作用。

## 📄 摘要（原文）

> Research on applications of reinforcement learning (RL) to large language models has mostly been focused on single-turn problems, such as mathematical reasoning or single-shot code generation. While these problems can be viewed as token-level multi-turn Markov decision processes (MDPs), this view corresponds to a degenerate case of multi-turn interaction where the environment provides no feedback. This contrasts with many real-world domains, such as software engineering (SWE), which require rich multi-turn interactions with a stateful environment that responds to each action with a non-trivial observation. To bridge this gap, we demonstrate the successful application of RL to this general regime. Our methodology begins with rejection fine-tuning (RFT) using execution feedback to train a policy to follow instructions and formatting effectively, followed by a synchronous RL pipeline using DAPO for iterative improvement. Applying this pipeline to Qwen2.5-72B-Instruct, we increase its Pass@1 on the SWE-bench Verified benchmark from 11% to 39%, substantially improving upon the 20% RFT baseline. On the May and June splits of SWE-rebench, the resulting agent achieves Pass@1 of 35% and 31% respectively, competitive with even larger models such as DeepSeek-V3-0324 or Qwen3-235B-A22B, demonstrating that our methodology offers a practical approach for training capable agents for multi-turn interactive tasks using open-weight models.

