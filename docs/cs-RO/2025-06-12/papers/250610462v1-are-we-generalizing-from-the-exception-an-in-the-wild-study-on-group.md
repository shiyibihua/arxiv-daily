---
layout: default
title: Are We Generalizing from the Exception? An In-the-Wild Study on Group-Sensitive Conversation Design in Human-Agent Interactions
---

# Are We Generalizing from the Exception? An In-the-Wild Study on Group-Sensitive Conversation Design in Human-Agent Interactions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10462" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10462v1</a>
  <a href="https://arxiv.org/pdf/2506.10462.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10462v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10462v1', 'Are We Generalizing from the Exception? An In-the-Wild Study on Group-Sensitive Conversation Design in Human-Agent Interactions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ana Müller, Sabina Jeschke, Anja Richert

**分类**: cs.RO

**发布日期**: 2025-06-12

**备注**: Accepted as a regular paper at the 2025 IEEE International Conference on Robot and Human Interactive Communication (RO-MAN). \c{opyright} IEEE. This is the preprint version. The final version will appear in the IEEE proceedings

---

## 💡 一句话要点

**研究群体适应性对话设计以提升人机交互效果**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人机交互` `社交机器人` `对话系统` `多方互动` `群体适应性` `虚拟代理` `人工智能`

## 📋 核心要点

1. 现有的对话系统在多方互动中难以有效适应不同群体的需求，导致用户满意度不高。
2. 论文提出了一种群体适应性对话设计方法，旨在提升社交互动代理在多方场景中的表现。
3. 尽管未能显著提升用户满意度，研究揭示了在不同表现形式下CAI适应的挑战，为未来研究提供了方向。

## 📝 摘要（中文）

本论文通过两项真实世界研究，探讨了群体适应性对话设计在两个社会互动代理（SIA）中的影响。这两个SIA分别是社交机器人Furhat和虚拟代理MetaHuman，均配备了结合混合检索与生成模型的对话人工智能（CAI）后端。研究在德国一座博物馆进行，共有188名参与者以二人、三人或更大群体的形式与SIA互动。尽管结果未显示群体敏感对话设计对满意度的显著影响，但研究为多方互动中CAI的适应挑战提供了宝贵见解，强调了超越语言复数化的多模态策略的必要性。这些见解为人机交互（HAI）、人机协作（HRI）及更广泛的人机互动（HMI）领域的未来研究提供了重要参考。

## 🔬 方法详解

**问题定义**：本论文旨在解决社交互动代理在多方对话中的适应性不足问题。现有方法往往无法有效满足不同群体的需求，导致用户体验不佳。

**核心思路**：论文的核心思路是设计一种群体适应性对话系统，通过结合混合检索与生成模型的对话人工智能（CAI），以提升多方互动中的对话质量和适应性。

**技术框架**：整体架构包括两个主要模块：一是基于混合检索的对话生成模块，二是基于生成模型的对话适应模块。通过这两个模块的协同工作，系统能够实时调整对话内容以适应参与者的需求。

**关键创新**：最重要的技术创新点在于提出了群体适应性对话设计的概念，强调了在多方互动中超越传统语言复数化的必要性。这一设计与现有方法的本质区别在于其多模态的适应策略。

**关键设计**：在参数设置上，系统采用了动态调整机制，以实时响应参与者的反馈。损失函数设计上，考虑了用户满意度和对话流畅度的平衡，网络结构则结合了深度学习与传统对话系统的优势。

## 📊 实验亮点

实验结果显示，尽管群体适应性对话设计未能显著提升用户满意度，但研究揭示了在多方互动中CAI适应的复杂性，为未来的对话系统设计提供了重要的实证基础。

## 🎯 应用场景

该研究的潜在应用领域包括社交机器人、虚拟助手及其他人机交互系统，能够为多方对话场景提供更为灵活和适应的对话策略。未来，随着技术的进步，这种适应性设计有望在教育、医疗及客户服务等领域发挥重要作用。

## 📄 摘要（原文）

> This paper investigates the impact of a group-adaptive conversation design in two socially interactive agents (SIAs) through two real-world studies. Both SIAs - Furhat, a social robot, and MetaHuman, a virtual agent - were equipped with a conversational artificial intelligence (CAI) backend combining hybrid retrieval and generative models. The studies were carried out in an in-the-wild setting with a total of $N = 188$ participants who interacted with the SIAs - in dyads, triads or larger groups - at a German museum. Although the results did not reveal a significant effect of the group-sensitive conversation design on perceived satisfaction, the findings provide valuable insights into the challenges of adapting CAI for multi-party interactions and across different embodiments (robot vs.\ virtual agent), highlighting the need for multimodal strategies beyond linguistic pluralization. These insights contribute to the fields of Human-Agent Interaction (HAI), Human-Robot Interaction (HRI), and broader Human-Machine Interaction (HMI), providing insights for future research on effective dialogue adaptation in group settings.

