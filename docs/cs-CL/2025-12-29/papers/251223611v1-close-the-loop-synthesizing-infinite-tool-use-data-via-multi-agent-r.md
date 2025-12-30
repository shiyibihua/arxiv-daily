---
layout: default
title: "Close the Loop: Synthesizing Infinite Tool-Use Data via Multi-Agent Role-Playing"
---

# Close the Loop: Synthesizing Infinite Tool-Use Data via Multi-Agent Role-Playing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23611" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23611v1</a>
  <a href="https://arxiv.org/pdf/2512.23611.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23611v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23611v1', 'Close the Loop: Synthesizing Infinite Tool-Use Data via Multi-Agent Role-Playing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuwen Li, Wei Zhang, Zelong Huang, Mason Yang, Jiajun Wu, Shawn Guo, Huahao Hu, Lingyi Sun, Jian Yang, Mingjie Tang, Byran Dai

**分类**: cs.CL

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**InfTool：通过多智能体角色扮演合成无限工具使用数据，提升LLM工具调用能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `工具调用` `大型语言模型` `多智能体` `强化学习` `数据合成`

## 📋 核心要点

1. 现有方法在使大型语言模型（LLM）可靠地调用外部工具时面临挑战，包括高质量轨迹的人工标注成本高昂、对未见工具的泛化能力差以及单模型合成的质量上限。
2. InfTool 提出一个全自动框架，通过多智能体角色扮演，仅需原始API规范，即可生成多样化、经过验证的工具使用轨迹，无需人工干预。
3. 实验表明，InfTool 在 Berkeley Function-Calling Leaderboard (BFCL) 上显著提升了模型的工具调用准确率，甚至超越了规模更大的模型。

## 📝 摘要（中文）

本文提出InfTool，一个全自动框架，通过自进化的多智能体合成来打破现有方法在工具调用方面的瓶颈。InfTool仅需原始API规范，即可协调三个协作智能体（用户模拟器、工具调用助手和MCP服务器）生成多样化、经过验证的轨迹，涵盖单轮调用到复杂的多步骤工作流程。该框架建立了一个闭环：合成的数据通过带有门控奖励的Group Relative Policy Optimization (GRPO) 训练模型，改进后的模型生成更高质量的数据以弥补能力差距，并且这个循环在没有人为干预的情况下迭代。在Berkeley Function-Calling Leaderboard (BFCL) 上的实验表明，InfTool 将一个基础的 32B 模型从 19.8% 的准确率提升到 70.9%（+258%），超过了 10 倍大的模型，并且可以与 Claude-Opus 相媲美，所有这些都来自合成数据，无需人工标注。

## 🔬 方法详解

**问题定义**：现有方法在训练LLM进行工具调用时，面临数据获取的难题。人工标注成本高，且难以覆盖所有可能的工具和使用场景。单模型生成数据存在偏差和覆盖不足的问题，导致模型泛化能力受限。

**核心思路**：InfTool的核心思路是利用多智能体协作，构建一个闭环的自学习系统。通过用户模拟器、工具调用助手和MCP服务器之间的交互，自动生成高质量的工具使用数据，并利用这些数据迭代训练模型，从而不断提升模型的工具调用能力。

**技术框架**：InfTool包含三个主要模块：1) 用户模拟器：模拟用户需求，生成工具调用请求。2) 工具调用助手：根据用户请求，选择合适的工具并调用，生成工具调用轨迹。3) MCP服务器：验证工具调用轨迹的正确性，并提供奖励信号。这三个模块形成一个闭环，不断生成和验证数据，并利用这些数据训练模型。

**关键创新**：InfTool的关键创新在于其全自动化的数据生成和模型训练流程。它摆脱了对人工标注的依赖，能够自动探索和学习新的工具和使用场景。此外，InfTool利用Group Relative Policy Optimization (GRPO) 算法，结合门控奖励，有效地训练模型，提升其工具调用能力。

**关键设计**：InfTool使用Group Relative Policy Optimization (GRPO) 算法进行模型训练，该算法能够有效地利用多智能体生成的数据。门控奖励机制用于筛选高质量的工具调用轨迹，避免噪声数据对模型训练产生负面影响。具体参数设置和网络结构细节在论文中未明确说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23611v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23611v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23611v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

InfTool 在 Berkeley Function-Calling Leaderboard (BFCL) 上取得了显著成果，将一个基础的 32B 模型从 19.8% 的准确率提升到 70.9%（+258%），超越了 10 倍大的模型，并且可以与 Claude-Opus 相媲美。所有这些提升都来自于合成数据，无需人工标注，证明了 InfTool 在提升 LLM 工具调用能力方面的有效性。

## 🎯 应用场景

InfTool 的潜在应用领域包括自动化客服、智能助手、机器人控制等。它可以用于训练 LLM 在各种实际场景中自主调用工具，完成复杂任务。该研究的实际价值在于降低了 LLM 工具调用训练的成本，提高了模型的泛化能力。未来，InfTool 可以扩展到更多领域，例如代码生成、科学研究等，赋能 LLM 解决更复杂的问题。

## 📄 摘要（原文）

> Enabling Large Language Models (LLMs) to reliably invoke external tools remains a critical bottleneck for autonomous agents. Existing approaches suffer from three fundamental challenges: expensive human annotation for high-quality trajectories, poor generalization to unseen tools, and quality ceilings inherent in single-model synthesis that perpetuate biases and coverage gaps. We introduce InfTool, a fully autonomous framework that breaks these barriers through self-evolving multi-agent synthesis. Given only raw API specifications, InfTool orchestrates three collaborative agents (User Simulator, Tool-Calling Assistant, and MCP Server) to generate diverse, verified trajectories spanning single-turn calls to complex multi-step workflows. The framework establishes a closed loop: synthesized data trains the model via Group Relative Policy Optimization (GRPO) with gated rewards, the improved model generates higher-quality data targeting capability gaps, and this cycle iterates without human intervention. Experiments on the Berkeley Function-Calling Leaderboard (BFCL) demonstrate that InfTool transforms a base 32B model from 19.8% to 70.9% accuracy (+258%), surpassing models 10x larger and rivaling Claude-Opus, and entirely from synthetic data without human annotation.

