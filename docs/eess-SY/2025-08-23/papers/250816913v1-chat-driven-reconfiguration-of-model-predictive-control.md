---
layout: default
title: Chat-Driven Reconfiguration of Model Predictive Control
---

# Chat-Driven Reconfiguration of Model Predictive Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.16913" class="toolbar-btn" target="_blank">📄 arXiv: 2508.16913v1</a>
  <a href="https://arxiv.org/pdf/2508.16913.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.16913v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.16913v1', 'Chat-Driven Reconfiguration of Model Predictive Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuya Miyaoka, Masaki Inoue, Jos'e M Maestre

**分类**: eess.SY

**发布日期**: 2025-08-23

---

## 💡 一句话要点

**提出ChatMPC以解决控制个性化与用户交互问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模型预测控制` `自然语言处理` `用户个性化` `机器人导航` `半自主驾驶` `实时性能` `环境适应`

## 📋 核心要点

1. 核心问题：现有控制个性化方法依赖用户的专业知识和重复反馈，限制了非专业用户的使用。
2. 方法要点：ChatMPC框架通过自然语言交互实现用户对控制系统的个性化和环境适应。
3. 实验或效果：实验表明，ChatMPC在机器人导航和半自主驾驶中实现了实时性能和有效的用户偏好适应。

## 📝 摘要（中文）

传统的控制个性化要求用户理解优化参数并提供重复的数值反馈，这对非专业用户构成了显著障碍。为了解决这一问题，本文提出了ChatMPC，一个通过自然语言交互使用户能够个性化控制系统并适应环境变化的模型预测控制框架。该框架有两种模式：个性化模式，用户可以迭代调整控制行为以符合其偏好；共同开发模式，用户提供实时环境信息以补充传感器数据。我们在不同用户行为模型下建立了收敛保证，证明了一致反馈下的指数收敛和基于容忍度用户的有限时间收敛。通过在机器人导航和半自主驾驶中的实验验证了ChatMPC的有效性，展示了其在实时性能和适应用户偏好及环境变化方面的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决传统控制个性化方法对用户专业知识的依赖，以及用户反馈的重复性问题。这些问题使得非专业用户难以有效参与控制系统的个性化调整。

**核心思路**：ChatMPC框架的核心思想是通过自然语言交互，使用户能够直观地个性化控制系统并适应环境变化。该框架分为个性化和共同开发两种模式，分别满足用户的不同需求。

**技术框架**：ChatMPC的整体架构包括用户交互模块、控制行为调整模块和环境信息补充模块。在个性化模式下，用户可以通过对话调整控制参数；在共同开发模式下，用户实时提供环境信息，增强系统的感知能力。

**关键创新**：最重要的技术创新在于将自然语言处理与模型预测控制相结合，使得用户能够以更直观的方式参与控制系统的个性化设计。这一设计与传统方法的本质区别在于用户交互的简化和反馈的实时性。

**关键设计**：在关键设计上，ChatMPC采用了多种用户行为模型来保证收敛性，包括一致反馈下的指数收敛和容忍度用户的有限时间收敛。此外，系统的参数设置和损失函数设计也经过精心调整，以确保在不同用户偏好下的有效性。

## 📊 实验亮点

实验结果显示，ChatMPC在机器人导航中实现了个性化障碍物避让，并在半自主驾驶中有效地进行对话式障碍物报告。两项实验均达到了实时性能，且在用户偏好适应和环境变化响应方面表现出色，验证了其实际应用的有效性。

## 🎯 应用场景

该研究的潜在应用场景包括机器人导航、智能驾驶和其他需要用户个性化控制的自动化系统。通过简化用户交互，ChatMPC能够使非专业用户更容易参与到控制系统的设计与调整中，从而提升系统的适应性和用户满意度。未来，这种方法可能会在更多领域推广应用，推动智能控制技术的发展。

## 📄 摘要（原文）

> Traditional control personalization requires users to understand optimization parameters and provide repetitive numerical feedback, creating significant barriers for non-expert users. To deal with this issue, we propose ChatMPC, a model predictive control framework that enables users to personalize control systems and adapt to environmental changes through natural language interaction. The framework operates in two modes: personalization, where users iteratively adjust control behavior to their preferences, and co-development, where users provide real-time environmental information that complements sensor data. We establish convergence guarantees under different user behavior models, demonstrating exponential convergence for consistent feedback and finite-time convergence with logarithmic interaction complexity for tolerance-based users. We validate ChatMPC through experiments in robot navigation with personalized obstacle avoidance and semi-autonomous driving with conversational obstacle reporting. Both experiments achieve real-time performance and demonstrate effective adaptation to user preferences and environmental changes.

