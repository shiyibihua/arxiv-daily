---
layout: default
title: Intention Chain-of-Thought Prompting with Dynamic Routing for Code Generation
---

# Intention Chain-of-Thought Prompting with Dynamic Routing for Code Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14048" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14048v1</a>
  <a href="https://arxiv.org/pdf/2512.14048.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14048v1" onclick="toggleFavorite(this, '2512.14048v1', 'Intention Chain-of-Thought Prompting with Dynamic Routing for Code Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shen Li, Li Huang, Shaoxiong Zhan, Weifeng Sun, Tao Yin, Zhongxin Liu, Meng Yan

**分类**: cs.AI

**发布日期**: 2025-12-16

**备注**: Accepted at AAAI-2026

---

## 💡 一句话要点

**提出RoutingGen以解决代码生成中的推理效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码生成` `链式思维` `动态路由` `意图建模` `推理效率` `大型语言模型` `机器学习`

## 📋 核心要点

1. 现有的链式思维提示方法在简单任务上容易导致过度思考，同时缺乏对代码生成中核心意图的建模。
2. 本文提出RoutingGen框架，动态调整提示策略，简单任务使用少量示例，复杂任务采用意图链式思维（ICoT）策略。
3. 实验结果显示RoutingGen在六个标准代码生成基准上表现优异，平均减少46.37%的令牌使用量，并超越六个现有提示基线。

## 📝 摘要（中文）

大型语言模型（LLMs）在代码生成中展现出强大的生成能力。现有的链式思维（CoT）提示方法通过引导中间步骤来增强模型推理，但存在两个主要局限：一是统一应用导致简单任务的过度思考，二是缺乏代码生成中的意图抽象，未能有效建模核心算法设计和效率。为此，本文提出了一种新颖的难度感知路由框架RoutingGen，动态调整代码生成的提示策略。对于简单任务，采用少量示例提示；对于复杂任务，引入意图链式思维（ICoT）策略，引导模型捕捉任务意图。实验表明，RoutingGen在大多数设置中实现了最先进的性能，同时平均减少了46.37%的总令牌使用量。

## 🔬 方法详解

**问题定义**：本文旨在解决现有链式思维提示方法在代码生成中的效率问题，尤其是在简单任务上导致的过度思考及缺乏意图建模的不足。

**核心思路**：RoutingGen框架通过动态调整提示策略，针对不同复杂度的任务采用不同的推理方式，以提高推理效率和准确性。对于简单任务，使用少量示例提示；而对于复杂任务，则引入意图链式思维（ICoT）来捕捉核心算法逻辑和时间复杂度。

**技术框架**：RoutingGen的整体架构包括两个主要模块：一是难度感知模块，根据任务复杂度选择提示策略；二是意图链式思维模块，提供结构化推理以捕捉任务意图。

**关键创新**：RoutingGen的核心创新在于其动态路由机制，能够根据任务的复杂性灵活调整提示策略，与现有方法的固定提示方式形成鲜明对比。

**关键设计**：在设计上，RoutingGen采用了少量示例提示和意图链式思维的结合，确保在简单任务中高效推理，同时在复杂任务中深入理解任务意图。

## 📊 实验亮点

实验结果表明，RoutingGen在大多数设置中实现了最先进的性能，特别是在复杂任务上，ICoT策略超越了六个现有的提示基线，且平均减少了46.37%的令牌使用量，显示出显著的效率提升。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发、自动化编程和教育等。通过提高代码生成的效率和准确性，RoutingGen能够帮助开发者更快速地实现功能，同时为教育领域提供更智能的编程学习工具，未来可能对编程教育和软件开发流程产生深远影响。

## 📄 摘要（原文）

> Large language models (LLMs) exhibit strong generative capabilities and have shown great potential in code generation. Existing chain-of-thought (CoT) prompting methods enhance model reasoning by eliciting intermediate steps, but suffer from two major limitations: First, their uniform application tends to induce overthinking on simple tasks. Second, they lack intention abstraction in code generation, such as explicitly modeling core algorithmic design and efficiency, leading models to focus on surface-level structures while neglecting the global problem objective. Inspired by the cognitive economy principle of engaging structured reasoning only when necessary to conserve cognitive resources, we propose RoutingGen, a novel difficulty-aware routing framework that dynamically adapts prompting strategies for code generation. For simple tasks, it adopts few-shot prompting; for more complex ones, it invokes a structured reasoning strategy, termed Intention Chain-of-Thought (ICoT), which we introduce to guide the model in capturing task intention, such as the core algorithmic logic and its time complexity. Experiments across three models and six standard code generation benchmarks show that RoutingGen achieves state-of-the-art performance in most settings, while reducing total token usage by 46.37% on average across settings. Furthermore, ICoT outperforms six existing prompting baselines on challenging benchmarks.

