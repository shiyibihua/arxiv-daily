---
layout: default
title: Distilling On-device Language Models for Robot Planning with Minimal Human Intervention
---

# Distilling On-device Language Models for Robot Planning with Minimal Human Intervention

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17486" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17486v2</a>
  <a href="https://arxiv.org/pdf/2506.17486.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17486v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17486v2', 'Distilling On-device Language Models for Robot Planning with Minimal Human Intervention')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zachary Ravichandran, Ignacio Hounie, Fernando Cladera, Alejandro Ribeiro, George J. Pappas, Vijay Kumar

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-06-20 (更新: 2025-10-06)

**备注**: Accepted to the Conference on Robot Learning (CoRL) 2025

**🔗 代码/项目**: [PROJECT_PAGE](https://zacravichandran.github.io/PRISM)

---

## 💡 一句话要点

**提出PRISM框架以实现机器人规划的本地语言模型蒸馏**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `机器人规划` `模型蒸馏` `自主系统` `合成数据`

## 📋 核心要点

1. 现有的LLM驱动机器人依赖云端模型，限制了在不可靠通信环境中的应用。
2. PRISM框架通过合成任务和环境，自动从LLM中提取规划，蒸馏出小型语言模型。
3. 实验表明，PRISM显著提升了Llama-3.2-3B的性能，从10-20%提升至93%以上，且具有良好的跨平台泛化能力。

## 📝 摘要（中文）

大型语言模型（LLMs）为机器人提供了强大的上下文推理能力和自然的人机接口。然而，当前的LLM驱动机器人通常依赖于云端模型，这限制了它们在通信基础设施不可靠的环境中的可用性，如户外或工业场景。本文提出了PRISM框架，旨在通过最小的人类监督，蒸馏出能够在设备上运行的小型语言模型（SLM）以进行机器人规划。PRISM从现有的LLM驱动规划器出发，自动合成多样的任务和环境，从LLM中引出规划，并利用合成数据集蒸馏出紧凑的SLM，作为源模型的替代品。我们将PRISM应用于三种LLM驱动的规划器，并展示其在性能上的显著提升。所有软件、训练模型和数据集已在https://zacravichandran.github.io/PRISM发布。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLM驱动机器人在不可靠环境中无法独立运行的问题。当前方法依赖于云端模型，导致在户外或工业环境中应用受限。

**核心思路**：PRISM框架通过自动合成多样的任务和环境，利用合成数据集从大型语言模型中提取规划，从而蒸馏出小型语言模型，使其能够在设备上独立运行。

**技术框架**：PRISM的整体架构包括任务合成模块、环境合成模块、规划提取模块和模型蒸馏模块。首先合成多样化的任务和环境，然后从LLM中提取规划，最后利用这些数据进行模型蒸馏。

**关键创新**：PRISM的主要创新在于其能够在没有人类干预的情况下，自动生成合成数据并进行模型蒸馏，这与传统的依赖人工标注数据的方法有本质区别。

**关键设计**：在模型蒸馏过程中，PRISM采用了特定的损失函数和网络结构，以确保蒸馏后的模型在性能上接近源模型，同时保持计算效率。

## 📊 实验亮点

实验结果显示，PRISM显著提升了Llama-3.2-3B的性能，从10-20%提升至93%以上，且在不同的机器人平台和环境中均表现出良好的泛化能力。这一成果表明，PRISM能够有效地将大型语言模型的能力转移到小型模型上。

## 🎯 应用场景

该研究的潜在应用领域包括自主机器人、工业自动化和家庭助理等场景。通过实现本地语言模型，机器人能够在没有网络连接的情况下执行复杂任务，提升了其在各种环境中的适用性和可靠性。未来，PRISM框架可能推动更多智能设备的独立运行，减少对云计算资源的依赖。

## 📄 摘要（原文）

> Large language models (LLMs) provide robots with powerful contextual reasoning abilities and a natural human interface. Yet, current LLM-enabled robots typically depend on cloud-hosted models, limiting their usability in environments with unreliable communication infrastructure, such as outdoor or industrial settings. We present PRISM, a framework for distilling small language model (SLM)-enabled robot planners that run on-device with minimal human supervision. Starting from an existing LLM-enabled planner, PRISM automatically synthesizes diverse tasks and environments, elicits plans from the LLM, and uses this synthetic dataset to distill a compact SLM as a drop-in replacement of the source model. We apply PRISM to three LLM-enabled planners for mapping and exploration, manipulation, and household assistance, and we demonstrate that PRISM improves the performance of Llama-3.2-3B from 10-20% of GPT-4o's performance to over 93% - using only synthetic data. We further demonstrate that the distilled planners generalize across heterogeneous robotic platforms (ground and aerial) and diverse environments (indoor and outdoor). We release all software, trained models, and datasets at https://zacravichandran.github.io/PRISM.

