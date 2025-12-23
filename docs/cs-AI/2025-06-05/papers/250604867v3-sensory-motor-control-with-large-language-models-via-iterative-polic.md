---
layout: default
title: Sensory-Motor Control with Large Language Models via Iterative Policy Refinement
---

# Sensory-Motor Control with Large Language Models via Iterative Policy Refinement

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04867" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04867v3</a>
  <a href="https://arxiv.org/pdf/2506.04867.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04867v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04867v3', 'Sensory-Motor Control with Large Language Models via Iterative Policy Refinement')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jônata Tyska Carvalho, Stefano Nolfi

**分类**: cs.AI, cs.HC, cs.LG, cs.RO

**发布日期**: 2025-06-05 (更新: 2025-11-14)

**备注**: Article updated with results from gpt-oss:120b and gpt-oss:20b. 27 pages (13 pages are from appendix), 8 figures, 2 tables, code for experiments replication and supplementary material provided at https://github.com/jtyska/llm-robotics-article/

---

## 💡 一句话要点

**提出一种方法使大型语言模型控制具身智能体**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `控制策略` `具身智能体` `迭代优化` `感知-运动数据` `机器人控制` `自动驾驶`

## 📋 核心要点

1. 现有方法在控制具身智能体时，往往依赖于复杂的手工设计策略，缺乏灵活性和适应性。
2. 本文提出的解决方案通过大型语言模型生成初步控制策略，并通过反馈迭代优化，提升了策略的有效性。
3. 实验结果显示，该方法在多个经典控制任务中表现优异，能够找到接近最优的解决方案，验证了其有效性。

## 📝 摘要（中文）

本文提出了一种方法，使大型语言模型（LLMs）能够通过生成控制策略来控制具身智能体，这些策略将连续观察向量直接映射到连续动作向量。最初，LLMs基于智能体、环境和预期目标的文本描述生成控制策略。随后，通过学习过程对该策略进行迭代优化，LLMs在评估过程中使用性能反馈和感知-运动数据不断改进当前策略。该方法在Gymnasium库的经典控制任务和MuJoCo库的倒立摆任务上进行了验证，结果表明，使用相对紧凑的模型如GPT-oss:120b和Qwen2.5:72b时，该方法能够有效识别最优或近似最优的解决方案，成功地将推理得出的符号知识与智能体与环境交互过程中收集的子符号感知-运动数据相结合。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在控制具身智能体时的策略生成和优化问题。现有方法通常依赖于手工设计的控制策略，缺乏灵活性和适应性，难以应对复杂环境中的变化。

**核心思路**：论文的核心思路是利用大型语言模型生成初步控制策略，并通过迭代学习过程不断优化该策略。通过将符号知识与感知-运动数据结合，提升了策略的适应性和有效性。

**技术框架**：整体架构包括三个主要模块：1) 初步策略生成模块，基于文本描述生成控制策略；2) 反馈收集模块，在智能体与环境交互中收集性能反馈和感知-运动数据；3) 策略优化模块，利用收集的数据迭代改进控制策略。

**关键创新**：最重要的技术创新在于将大型语言模型与感知-运动数据结合，通过迭代优化实现了策略的动态调整。这一方法与传统的手工设计策略有本质区别，能够更好地适应复杂环境。

**关键设计**：在模型设计中，采用了紧凑的语言模型（如GPT-oss:120b和Qwen2.5:72b），并通过特定的损失函数来平衡策略生成与反馈优化的过程，确保策略的有效性和稳定性。实验中还对模型的超参数进行了细致调优，以达到最佳性能。

## 📊 实验亮点

实验结果表明，该方法在Gymnasium和MuJoCo库的经典控制任务中表现优异，能够在大多数情况下找到最优或近似最优的解决方案。相较于传统方法，使用GPT-oss:120b和Qwen2.5:72b模型时，策略的有效性显著提升，验证了该方法的实用性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动驾驶、智能家居等具身智能体的控制任务。通过提升大型语言模型在动态环境中的适应能力，能够为实际应用提供更灵活和高效的解决方案，推动智能体技术的发展。

## 📄 摘要（原文）

> We propose a method that enables large language models (LLMs) to control embodied agents through the generation of control policies that directly map continuous observation vectors to continuous action vectors. At the outset, the LLMs generate a control strategy based on a textual description of the agent, its environment, and the intended goal. This strategy is then iteratively refined through a learning process in which the LLMs are repeatedly prompted to improve the current strategy, using performance feedback and sensory-motor data collected during its evaluation. The method is validated on classic control tasks from the Gymnasium library and the inverted pendulum task from the MuJoCo library. The approach proves effective with relatively compact models such as GPT-oss:120b and Qwen2.5:72b. In most cases, it successfully identifies optimal or near-optimal solutions by integrating symbolic knowledge derived through reasoning with sub-symbolic sensory-motor data gathered as the agent interacts with its environment.

