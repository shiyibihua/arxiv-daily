---
layout: default
title: "Youtu-Agent: Scaling Agent Productivity with Automated Generation and Hybrid Policy Optimization"
---

# Youtu-Agent: Scaling Agent Productivity with Automated Generation and Hybrid Policy Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24615" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24615v1</a>
  <a href="https://arxiv.org/pdf/2512.24615.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24615v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24615v1', 'Youtu-Agent: Scaling Agent Productivity with Automated Generation and Hybrid Policy Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuchen Shi, Yuzheng Cai, Siqi Cai, Zihan Xu, Lichao Chen, Yulei Qin, Zhijian Zhou, Xiang Fei, Chaofan Qiu, Xiaoyu Tan, Gang Li, Zongyi Li, Haojia Lin, Guocan Cai, Yong Mao, Yunsheng Wu, Ke Li, Xing Sun

**分类**: cs.AI

**发布日期**: 2025-12-31

---

## 💡 一句话要点

**Youtu-Agent：通过自动生成和混合策略优化提升Agent生产力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM Agent` `自动生成` `混合策略优化` `强化学习` `上下文学习` `工具集成` `智能自动化`

## 📋 核心要点

1. 现有LLM Agent框架配置成本高昂，且难以适应动态环境，限制了其应用。
2. Youtu-Agent通过模块化设计、自动生成和混合策略优化，实现Agent的自动构建和持续进化。
3. 实验表明，Youtu-Agent在多个基准测试中取得了领先性能，并显著提升了Agent的工具合成和问题解决能力。

## 📝 摘要（中文）

现有的大语言模型（LLM）Agent框架面临两大挑战：高配置成本和静态能力。构建高质量的Agent通常需要在工具集成和提示工程方面进行大量的人工工作，而部署的Agent在没有昂贵的微调的情况下难以适应动态环境。为了解决这些问题，我们提出了Youtu-Agent，这是一个为LLM Agent的自动生成和持续演进而设计的模块化框架。Youtu-Agent具有结构化的配置系统，可解耦执行环境、工具包和上下文管理，从而实现灵活的重用和自动合成。我们引入了两种生成范式：用于标准任务的Workflow模式和用于复杂、非标准需求的Meta-Agent模式，能够自动生成工具代码、提示和配置。此外，Youtu-Agent建立了一个混合策略优化系统：（1）Agent Practice模块，使Agent能够通过上下文优化积累经验并提高性能，而无需参数更新；（2）Agent RL模块，与分布式训练框架集成，以实现任何Youtu-Agent的端到端、大规模可扩展且稳定的强化学习。实验表明，Youtu-Agent使用开源模型在WebWalkerQA（71.47%）和GAIA（72.8%）上实现了最先进的性能。我们的自动生成管道实现了超过81%的工具合成成功率，而Practice模块将AIME 2024/2025的性能分别提高了+2.7%和+5.4%。此外，我们的Agent RL训练实现了40%的加速，并在7B LLM上实现了稳定的性能提升，在Maths和通用/多跳QA基准测试中，分别将编码/推理和搜索能力提高了高达35%和21%。

## 🔬 方法详解

**问题定义**：现有LLM Agent框架需要大量人工配置，包括工具集成和提示工程，成本高昂。同时，已部署的Agent难以适应动态变化的环境，需要耗费资源的微调才能保持性能。因此，如何降低Agent的配置成本，并使其具备持续学习和适应能力，是本文要解决的核心问题。

**核心思路**：Youtu-Agent的核心思路是实现Agent的自动生成和持续进化。通过模块化的框架设计，解耦执行环境、工具包和上下文管理，实现灵活的组件复用和自动合成。同时，引入混合策略优化系统，包括Agent Practice和Agent RL，使Agent能够通过上下文学习和强化学习不断提升自身能力。

**技术框架**：Youtu-Agent包含以下主要模块：
1. **结构化配置系统**：解耦执行环境、工具包和上下文管理，实现组件的灵活复用。
2. **自动生成模块**：包含Workflow模式和Meta-Agent模式，自动生成工具代码、提示和配置。
3. **混合策略优化系统**：包含Agent Practice模块（上下文优化）和Agent RL模块（强化学习）。

**关键创新**：Youtu-Agent的关键创新在于其自动生成和混合策略优化机制。自动生成模块能够显著降低Agent的配置成本，而混合策略优化系统则使Agent具备了持续学习和适应能力，无需人工干预即可提升性能。与现有方法相比，Youtu-Agent更加灵活、高效和智能化。

**关键设计**：
1. **Workflow模式和Meta-Agent模式**：针对不同复杂度的任务，采用不同的生成策略。
2. **Agent Practice模块**：通过上下文学习，使Agent能够从经验中学习，提升性能。
3. **Agent RL模块**：利用分布式训练框架，实现大规模Agent的强化学习，提升Agent的通用能力。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24615v1/figs/fig2_autogen.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24615v1/figs/fig2_2_tfgrpo.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24615v1/figs/fig_youtu-agent-rl.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Youtu-Agent在WebWalkerQA和GAIA数据集上取得了SOTA结果，分别达到71.47%和72.8%。自动生成管道的工具合成成功率超过81%。Agent Practice模块使AIME 2024/2025的性能分别提高了+2.7%和+5.4%。Agent RL训练实现了40%的加速，并在Maths和通用/多跳QA基准测试中，分别将编码/推理和搜索能力提高了高达35%和21%。

## 🎯 应用场景

Youtu-Agent可广泛应用于智能客服、自动化办公、智能搜索等领域。通过自动生成和持续优化，可以大幅降低Agent的开发和维护成本，提高Agent的智能化水平和服务质量。未来，Youtu-Agent有望成为构建通用人工智能Agent的重要基石。

## 📄 摘要（原文）

> Existing Large Language Model (LLM) agent frameworks face two significant challenges: high configuration costs and static capabilities. Building a high-quality agent often requires extensive manual effort in tool integration and prompt engineering, while deployed agents struggle to adapt to dynamic environments without expensive fine-tuning. To address these issues, we propose \textbf{Youtu-Agent}, a modular framework designed for the automated generation and continuous evolution of LLM agents. Youtu-Agent features a structured configuration system that decouples execution environments, toolkits, and context management, enabling flexible reuse and automated synthesis. We introduce two generation paradigms: a \textbf{Workflow} mode for standard tasks and a \textbf{Meta-Agent} mode for complex, non-standard requirements, capable of automatically generating tool code, prompts, and configurations. Furthermore, Youtu-Agent establishes a hybrid policy optimization system: (1) an \textbf{Agent Practice} module that enables agents to accumulate experience and improve performance through in-context optimization without parameter updates; and (2) an \textbf{Agent RL} module that integrates with distributed training frameworks to enable scalable and stable reinforcement learning of any Youtu-Agents in an end-to-end, large-scale manner. Experiments demonstrate that Youtu-Agent achieves state-of-the-art performance on WebWalkerQA (71.47\%) and GAIA (72.8\%) using open-weight models. Our automated generation pipeline achieves over 81\% tool synthesis success rate, while the Practice module improves performance on AIME 2024/2025 by +2.7\% and +5.4\% respectively. Moreover, our Agent RL training achieves 40\% speedup with steady performance improvement on 7B LLMs, enhancing coding/reasoning and searching capabilities respectively up to 35\% and 21\% on Maths and general/multi-hop QA benchmarks.

