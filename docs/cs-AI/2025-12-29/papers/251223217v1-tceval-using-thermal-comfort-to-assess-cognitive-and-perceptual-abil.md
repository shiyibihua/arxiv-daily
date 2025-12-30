---
layout: default
title: "TCEval: Using Thermal Comfort to Assess Cognitive and Perceptual Abilities of AI"
---

# TCEval: Using Thermal Comfort to Assess Cognitive and Perceptual Abilities of AI

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23217" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23217v1</a>
  <a href="https://arxiv.org/pdf/2512.23217.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23217v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23217v1', 'TCEval: Using Thermal Comfort to Assess Cognitive and Perceptual Abilities of AI')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingming Li

**分类**: cs.AI

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**提出TCEval框架以评估AI的认知与感知能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `热舒适` `认知能力评估` `大型语言模型` `跨模态推理` `因果关联` `适应性决策` `智能建筑` `生态有效性`

## 📋 核心要点

1. 现有的LLM任务特定基准缺乏有效性，无法全面评估AI在真实环境中的认知能力。
2. 本文提出TCEval框架，通过热舒适场景评估AI的跨模态推理、因果关联和适应性决策能力。
3. 实验结果显示，LLM生成的反馈与人类数据存在显著差异，但在一定容忍度下，方向一致性有明显提升。

## 📝 摘要（中文）

在大型语言模型（LLM）任务特定基准中存在重要缺口。热舒适作为环境因素与个人感知之间复杂交互的理想范式，能够有效评估AI系统的真实世界认知能力。为此，本文提出了TCEval，这是第一个通过热舒适场景和LLM代理评估AI三大核心认知能力的评估框架。研究表明，尽管代理反馈与人类的精确对齐有限，但在1 PMV容忍度下，方向一致性显著提高。统计测试显示，LLM生成的PMV分布与人类数据显著偏离，代理在离散热舒适分类中的表现接近随机。这些结果确认了TCEval作为生态有效的认知图灵测试的可行性，展示了当前LLM具备基础的跨模态推理能力，但缺乏对热舒适变量之间非线性关系的精确因果理解。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLM评估方法在真实环境认知能力评估中的不足，特别是在热舒适领域的应用。现有方法未能有效捕捉AI在复杂环境中的感知与决策能力。

**核心思路**：TCEval框架通过模拟热舒适场景，结合LLM代理的虚拟个性特征，评估其在跨模态推理、因果关联和适应性决策方面的能力。这种设计旨在提供更真实的评估环境。

**技术框架**：TCEval的整体架构包括初始化LLM代理、生成服装绝缘选择和热舒适反馈，并将输出与ASHRAE全球数据库和中国热舒适数据库进行验证。主要模块包括数据收集、模型初始化、反馈生成和结果验证。

**关键创新**：TCEval的创新在于将热舒适作为评估AI认知能力的基准，首次将环境感知与决策能力结合，提供了一种新的评估视角，与传统基准方法形成鲜明对比。

**关键设计**：在模型设计中，采用了特定的参数设置和损失函数，以确保生成的反馈与真实数据的对齐。同时，使用了1 PMV的容忍度来提高方向一致性，增强了评估的生态有效性。

## 📊 实验亮点

实验结果显示，LLM生成的PMV分布与人类数据显著偏离，且在离散热舒适分类中表现接近随机。然而，在1 PMV容忍度下，代理的方向一致性显著提高，表明TCEval在评估AI认知能力方面具有潜力。

## 🎯 应用场景

TCEval框架的潜在应用领域包括智能建筑、环境监测和人机交互等。通过更准确地评估AI在复杂环境中的认知能力，能够推动AI在以人为中心的应用中的发展，提升用户体验和环境适应性。未来，该框架可能为智能系统的设计和优化提供重要参考。

## 📄 摘要（原文）

> A critical gap exists in LLM task-specific benchmarks. Thermal comfort, a sophisticated interplay of environmental factors and personal perceptions involving sensory integration and adaptive decision-making, serves as an ideal paradigm for evaluating real-world cognitive capabilities of AI systems. To address this, we propose TCEval, the first evaluation framework that assesses three core cognitive capacities of AI, cross-modal reasoning, causal association, and adaptive decision-making, by leveraging thermal comfort scenarios and large language model (LLM) agents. The methodology involves initializing LLM agents with virtual personality attributes, guiding them to generate clothing insulation selections and thermal comfort feedback, and validating outputs against the ASHRAE Global Database and Chinese Thermal Comfort Database. Experiments on four LLMs show that while agent feedback has limited exact alignment with humans, directional consistency improves significantly with a 1 PMV tolerance. Statistical tests reveal that LLM-generated PMV distributions diverge markedly from human data, and agents perform near-randomly in discrete thermal comfort classification. These results confirm the feasibility of TCEval as an ecologically valid Cognitive Turing Test for AI, demonstrating that current LLMs possess foundational cross-modal reasoning ability but lack precise causal understanding of the nonlinear relationships between variables in thermal comfort. TCEval complements traditional benchmarks, shifting AI evaluation focus from abstract task proficiency to embodied, context-aware perception and decision-making, offering valuable insights for advancing AI in human-centric applications like smart buildings.

