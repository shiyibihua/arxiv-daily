---
layout: default
title: Learning to Wait: Synchronizing Agents with the Physical World
---

# Learning to Wait: Synchronizing Agents with the Physical World

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16262" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16262v1</a>
  <a href="https://arxiv.org/pdf/2512.16262.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16262v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16262v1', 'Learning to Wait: Synchronizing Agents with the Physical World')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifei She, Ping Zhang, He Liu, Yanmin Jia, Yang Jing, Zijun Liu, Peng Sun, Xiangbin Li, Xiaohe Hu

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出Agent端时间同步方法，解决LLM在异步环境中与物理世界交互的时延问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Agent时间同步` `大型语言模型` `上下文学习` `异步环境` `代码即动作`

## 📋 核心要点

1. 现实Agent任务中，动作完成存在时延，导致Agent与环境交互出现时间间隔，现有环境侧解决方案存在可扩展性或上下文稀释问题。
2. 论文提出Agent端方法，通过让LLM预测等待时长（`time.sleep(t)`），主动将其认知时间线与物理世界对齐，实现时间同步。
3. 实验表明，Agent能够精确校准内部时钟，最小化查询开销和执行延迟，验证了时间感知能力对于开放环境自主进化的重要性。

## 📝 摘要（中文）

与同步马尔可夫决策过程（MDP）不同，现实世界的Agent任务通常涉及具有可变延迟的非阻塞动作，从而在动作发起和完成之间产生根本性的“时间间隔”。现有的环境侧解决方案，如阻塞包装器或频繁轮询，要么限制了可扩展性，要么用冗余的观察稀释了Agent的上下文窗口。本文提出了一种Agent端方法，使大型语言模型（LLM）能够主动将其“认知时间线”与物理世界对齐。通过将代码即动作范式扩展到时间域，Agent利用语义先验和上下文学习（ICL）来预测精确的等待时长（`time.sleep(t)`），从而有效地与异步环境同步，而无需详尽的检查。在模拟的Kubernetes集群中的实验表明，Agent可以精确地校准其内部时钟，以最大限度地减少查询开销和执行延迟，从而验证了时间感知是在开放环境中自主进化必不可少的、可学习的能力。

## 🔬 方法详解

**问题定义**：论文旨在解决现实世界Agent任务中，由于动作执行存在时延，导致Agent与环境交互异步的问题。现有方法，如阻塞包装器和频繁轮询，要么限制了系统的可扩展性，要么引入了大量的冗余观察，稀释了Agent的上下文信息，影响决策效率。

**核心思路**：论文的核心思路是赋予Agent时间感知能力，使其能够主动预测并等待动作完成所需的时间，从而实现与异步环境的同步。通过让Agent学习何时以及等待多久，避免了不必要的轮询和阻塞，提高了交互效率和决策质量。

**技术框架**：论文将代码即动作范式扩展到时间域，Agent通过生成包含`time.sleep(t)`指令的代码来控制等待时间。整体流程包括：1) Agent接收环境观测；2) Agent利用LLM生成包含`time.sleep(t)`的动作代码；3) 执行动作代码，Agent进入休眠状态；4) 休眠结束后，Agent再次接收环境观测，进入下一轮交互。论文利用上下文学习（ICL）来引导LLM学习时间感知能力。

**关键创新**：最重要的创新点在于将时间同步问题从环境侧转移到Agent侧，赋予Agent主动控制等待时间的能力。与传统的被动等待或频繁轮询方法相比，该方法能够更有效地利用Agent的计算资源，并减少不必要的环境交互。

**关键设计**：论文的关键设计包括：1) 使用LLM作为Agent的决策核心，利用其强大的语义理解和生成能力；2) 通过上下文学习（ICL）提供时间相关的示例，引导LLM学习预测合适的等待时间；3) 使用`time.sleep(t)`作为控制等待时间的指令，简单而有效；4) 在Kubernetes集群模拟环境中进行实验，验证方法的有效性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16262v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16262v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16262v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，所提出的Agent端时间同步方法能够显著减少查询开销和执行延迟。在模拟的Kubernetes集群环境中，Agent能够精确校准其内部时钟，实现与异步环境的高效同步。具体性能数据未知，但论文强调了该方法在最小化查询开销和执行延迟方面的有效性。

## 🎯 应用场景

该研究成果可应用于各种需要与异步环境交互的Agent系统，例如机器人控制、自动化运维、智能家居等。通过赋予Agent时间感知能力，可以提高其在复杂、动态环境中的自主性和效率，降低人工干预的需求，并为构建更智能、更可靠的自动化系统奠定基础。

## 📄 摘要（原文）

> Real-world agentic tasks, unlike synchronous Markov Decision Processes (MDPs), often involve non-blocking actions with variable latencies, creating a fundamental \textit{Temporal Gap} between action initiation and completion. Existing environment-side solutions, such as blocking wrappers or frequent polling, either limit scalability or dilute the agent's context window with redundant observations. In this work, we propose an \textbf{Agent-side Approach} that empowers Large Language Models (LLMs) to actively align their \textit{Cognitive Timeline} with the physical world. By extending the Code-as-Action paradigm to the temporal domain, agents utilize semantic priors and In-Context Learning (ICL) to predict precise waiting durations (\texttt{time.sleep(t)}), effectively synchronizing with asynchronous environment without exhaustive checking. Experiments in a simulated Kubernetes cluster demonstrate that agents can precisely calibrate their internal clocks to minimize both query overhead and execution latency, validating that temporal awareness is a learnable capability essential for autonomous evolution in open-ended environments.

