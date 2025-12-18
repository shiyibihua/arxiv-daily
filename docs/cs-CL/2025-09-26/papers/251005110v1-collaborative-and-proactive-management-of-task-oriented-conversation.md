---
layout: default
title: Collaborative and Proactive Management of Task-Oriented Conversations
---

# Collaborative and Proactive Management of Task-Oriented Conversations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.05110" class="toolbar-btn" target="_blank">📄 arXiv: 2510.05110v1</a>
  <a href="https://arxiv.org/pdf/2510.05110.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.05110v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.05110v1', 'Collaborative and Proactive Management of Task-Oriented Conversations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arezoo Saedi, Afsaneh Fatemi, Mohammad Ali Nematbakhsh, Sophie Rosset, Anne Vilnat

**分类**: cs.CL

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出一种基于信息状态的协作式任务导向对话管理模型，提升对话成功率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `任务导向对话系统` `信息状态` `大型语言模型` `上下文学习` `对话管理`

## 📋 核心要点

1. 现有任务导向对话系统在主动规划方面存在不足，忽略了有效的目标感知规划。
2. 该模型以信息状态方法为核心，通过构建中间信息来辅助对话规划，提升任务完成效率。
3. 实验结果表明，该模型在MultiWOZ数据集上取得了更高的信息提供和对话成功率。

## 📝 摘要（中文）

本文提出了一种用于管理任务导向对话（TOD）的模型，该模型以信息状态方法为中心。该模型利用大型语言模型（LLM）的上下文学习能力，通过构建中间信息来辅助规划。首先，创建预定义的槽位和文本部分信息组件来建模用户偏好。然后，识别关键情况并创建相应的组件，这些组件的配置形成有限的信息状态。接着，设计对话动作，指示信息状态之间的转换以及执行的程序。最后，构建更新策略。该模型通过在MultiWOZ数据集上进行评估，结果表明，在信息提供和对话成功率方面均优于现有方法。

## 🔬 方法详解

**问题定义**：现有任务导向对话系统（TOD）虽然受益于大型语言模型（LLM）的能力，但在主动规划方面仍存在不足。许多系统未能有效地进行目标感知的规划，导致对话效率和成功率受限。本文旨在解决TOD系统中缺乏有效规划的问题，提升对话的协作性和主动性。

**核心思路**：本文的核心思路是采用信息状态方法来管理对话。通过显式地建模对话过程中的信息状态，系统可以更好地理解用户的意图和偏好，并主动地引导对话朝着完成任务的方向发展。关键在于构建中间信息，辅助规划，从而应对复杂对话场景。

**技术框架**：该模型的技术框架主要包含以下几个阶段：1) 用户偏好建模：利用预定义的槽位和文本部分信息组件来表示用户偏好。2) 关键情境识别：分析中间信息，识别对话中的关键情境。3) 信息状态构建：为每个关键情境创建相应的信息组件，并通过配置这些组件来形成有限的信息状态。4) 对话动作设计：设计对话动作，用于在不同的信息状态之间进行转换，并执行相应的程序。5) 更新策略构建：根据对话动作的结果，更新信息状态，并选择下一步的对话动作。

**关键创新**：该模型最重要的技术创新点在于将中间信息融入到信息状态的构建中。通过显式地建模对话过程中的中间状态，系统可以更好地理解用户的意图和偏好，并主动地引导对话朝着完成任务的方向发展。这与传统的TOD系统只关注最终目标不同，更注重对话过程中的协作和主动性。

**关键设计**：该模型利用LLM的上下文学习能力来实现。数据库查询基于预定义的槽位创建，检索到的实体排序基于文本部分。这种机制使得系统能够按照一致性顺序将所有相应的实体传递给偏好。具体参数设置和损失函数等细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，该模型在MultiWOZ数据集上取得了显著的性能提升。具体而言，该模型在信息提供和对话成功率方面均优于现有方法。虽然论文中没有给出具体的数值，但强调了在完整测试对话上的最大化信息提供和成功率，表明该模型具有较强的实用价值。

## 🎯 应用场景

该研究成果可应用于各种任务导向的对话系统，例如智能客服、虚拟助手、在线预订系统等。通过提升对话的协作性和主动性，可以提高用户满意度，降低人工干预的需求，并最终提高任务完成的效率。未来，该方法可以扩展到更复杂的对话场景，例如多领域对话和开放域对话。

## 📄 摘要（原文）

> Task oriented dialogue systems (TOD) complete particular tasks based on user preferences across natural language interactions. Considering the impressive performance of large language models (LLMs) in natural language processing (NLP) tasks, most of the latest TODs are centered on LLMs. While proactive planning is crucial for task completion, many existing TODs overlook effective goal-aware planning. This paper creates a model for managing task-oriented conversations, conceptualized centered on the information state approach to dialogue management. The created model incorporated constructive intermediate information in planning. Initially, predefined slots and text part informational components are created to model user preferences. Investigating intermediate information, critical circumstances are identified. Informational components corresponding to these circumstances are created. Possible configurations for these informational components lead to limited information states. Then, dialogue moves, which indicate movement between these information states and the procedures that must be performed in the movements, are created. Eventually, the update strategy is constructed. The created model is implemented leveraging in-context learning of LLMs. In this model,  database queries are created centered on indicated predefined slots and the order of retrieved entities is indicated centered on text part. This mechanism enables passing the whole corresponding entities to the preferences in the order of congruency. Evaluations exploiting the complete test conversations of MultiWOZ, with no more than a domain in a conversation, illustrate maximal inform and success, and improvement compared with previous methods.

