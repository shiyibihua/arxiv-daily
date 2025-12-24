---
layout: default
title: How Does a Virtual Agent Decide Where to Look? -- Symbolic Cognitive Reasoning for Embodied Head Rotation
---

# How Does a Virtual Agent Decide Where to Look? -- Symbolic Cognitive Reasoning for Embodied Head Rotation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08930" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08930v1</a>
  <a href="https://arxiv.org/pdf/2508.08930.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08930v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08930v1', 'How Does a Virtual Agent Decide Where to Look? -- Symbolic Cognitive Reasoning for Embodied Head Rotation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Juyeong Hwang, Seong-Eun Hon, JaeYoung Seon, Hyeongyeop Kang

**分类**: cs.GR

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出SCORE框架以解决虚拟代理头部旋转决策问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `虚拟代理` `头部旋转` `认知推理` `视觉-语言模型` `大型语言模型` `行为真实感` `多模态融合`

## 📋 核心要点

1. 现有的头部旋转预测方法主要关注视觉显著性，忽视了认知动机，导致虚拟代理的行为不够真实。
2. 提出SCORE框架，通过符号认知推理实现上下文感知的头部运动，避免了任务特定训练的需求。
3. 通过控制的虚拟现实实验，识别出五个头部运动的动机驱动因素，提升了代理的行为可信度和适应性。

## 📝 摘要（中文）

自然的头部旋转对于可信的虚拟代理至关重要，但这一微观行为仍然未得到充分研究。现有的头部旋转预测算法通常侧重于视觉显著性刺激，忽视了指导头部旋转的认知动机，导致代理只关注显眼物体而忽略障碍物或任务相关线索，从而降低了虚拟环境的真实感。本文提出了SCORE（Symbolic Cognitive Reasoning for Embodied Head Rotation），一个数据无关的框架，能够在没有任务特定训练或手动调整启发式的情况下生成上下文感知的头部运动。通过一项控制的虚拟现实研究，识别出人类头部运动的五个动机驱动因素：兴趣、信息寻求、安全、社会模式和习惯。SCORE将这些驱动因素编码为符号谓词，利用视觉-语言模型（VLM）感知场景，并通过大型语言模型（LLM）规划头部姿态。

## 🔬 方法详解

**问题定义**：本文旨在解决虚拟代理在头部旋转决策时缺乏认知动机的问题。现有方法往往只关注视觉显著性，导致代理行为缺乏真实感和合理性。

**核心思路**：SCORE框架通过符号认知推理，结合视觉-语言模型和大型语言模型，生成上下文感知的头部运动，能够解释代理的行为动机。

**技术框架**：该框架包括多个模块：首先，使用视觉-语言模型（VLM）感知场景；其次，利用大型语言模型（LLM）进行头部姿态规划；最后，采用轻量级的FastVLM进行在线验证，以抑制幻觉并保持对场景动态的响应。

**关键创新**：SCORE的主要创新在于其数据无关性和符号化的认知推理能力，使得代理不仅能预测“看哪里”，还能够解释“为什么看”。与传统方法相比，SCORE更具通用性和适应性。

**关键设计**：框架中采用的关键设计包括符号谓词的编码方式、VLM与LLM的结合策略，以及FastVLM的在线验证机制，这些设计确保了模型的高效性和实时性。

## 📊 实验亮点

实验结果表明，SCORE框架能够有效识别五个动机驱动因素，并在多种场景中保持行为的可信度。与传统方法相比，SCORE在处理未见场景和多代理人环境时表现出更高的适应性和合理性，显著提升了代理的行为表现。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、游戏开发和人机交互等。通过提升虚拟代理的行为真实感，SCORE框架能够增强用户体验，促进更自然的交互。同时，该框架的通用性使其在多种场景中具有广泛的适用性，未来可能推动智能代理的发展。

## 📄 摘要（原文）

> Natural head rotation is critical for believable embodied virtual agents, yet this micro-level behavior remains largely underexplored. While head-rotation prediction algorithms could, in principle, reproduce this behavior, they typically focus on visually salient stimuli and overlook the cognitive motives that guide head rotation. This yields agents that look at conspicuous objects while overlooking obstacles or task-relevant cues, diminishing realism in a virtual environment. We introduce SCORE, a Symbolic Cognitive Reasoning framework for Embodied Head Rotation, a data-agnostic framework that produces context-aware head movements without task-specific training or hand-tuned heuristics. A controlled VR study (N=20) identifies five motivational drivers of human head movements: Interest, Information Seeking, Safety, Social Schema, and Habit. SCORE encodes these drivers as symbolic predicates, perceives the scene with a Vision-Language Model (VLM), and plans head poses with a Large Language Model (LLM). The framework employs a hybrid workflow: the VLM-LLM reasoning is executed offline, after which a lightweight FastVLM performs online validation to suppress hallucinations while maintaining responsiveness to scene dynamics. The result is an agent that predicts not only where to look but also why, generalizing to unseen scenes and multi-agent crowds while retaining behavioral plausibility.

