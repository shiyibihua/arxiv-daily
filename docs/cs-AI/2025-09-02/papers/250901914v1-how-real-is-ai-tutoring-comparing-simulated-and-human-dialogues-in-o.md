---
layout: default
title: How Real Is AI Tutoring? Comparing Simulated and Human Dialogues in One-on-One Instruction
---

# How Real Is AI Tutoring? Comparing Simulated and Human Dialogues in One-on-One Instruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01914" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01914v1</a>
  <a href="https://arxiv.org/pdf/2509.01914.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01914v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01914v1', 'How Real Is AI Tutoring? Comparing Simulated and Human Dialogues in One-on-One Instruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruijia Li, Yuan-Hao Jiang, Jiatong Wang, Bo Jiang

**分类**: cs.AI, cs.CL, cs.MA

**发布日期**: 2025-09-02

**备注**: Proceedings of the 33rd International Conference on Computers in Education (ICCE 2025). Asia-Pacific Society for Computers in Education

---

## 💡 一句话要点

**对比AI与人类辅导对话，揭示当前AI在教学互动深度上的局限性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `AI辅导` `人机对话` `教育对话系统` `认知网络分析` `IRF编码`

## 📋 核心要点

1. 大型语言模型在生成教学互动方面存在挑战，无法有效促进学生高阶思维。
2. 通过对比AI模拟和人类辅导对话，分析结构和行为差异，揭示AI的局限性。
3. 研究发现人类对话在认知引导和教学循环上优于AI，为改进AI辅导系统提供指导。

## 📝 摘要（中文）

启发式和支架式师生对话被广泛认为是培养学生高阶思维和深度学习的关键。然而，大型语言模型（LLMs）目前在生成教学上丰富的互动方面面临挑战。本研究系统地调查了AI模拟和真实人类辅导对话之间的结构和行为差异。我们使用启动-响应-反馈（IRF）编码方案和认知网络分析（ENA）进行了定量比较。结果表明，人类对话在话语长度、提问（I-Q）和一般反馈（F-F）行为方面明显优于AI对话。更重要的是，ENA结果揭示了互动模式的根本差异：人类对话更具认知引导性和多样性，围绕着一个“问题-事实性回答-反馈”的教学循环，清晰地反映了教学指导和学生驱动的思考；相比之下，模拟对话表现出结构简化和行为收敛的模式，围绕着一个“解释-简单回答”的循环，本质上是教师和学生之间简单的信息传递。这些发现揭示了当前AI生成的辅导的关键局限性，并为设计和评估更具教学效果的生成式教育对话系统提供了经验指导。

## 🔬 方法详解

**问题定义**：论文旨在解决当前大型语言模型在模拟师生互动，特别是生成具有启发性和支架式教学对话方面的不足。现有方法难以有效模拟人类教师的提问、反馈和认知引导，导致学生难以进行深度学习和高阶思维培养。

**核心思路**：论文的核心思路是通过对比分析AI模拟的辅导对话和真实人类辅导对话，量化二者在结构和行为上的差异，从而揭示AI在教学互动方面的局限性。通过识别这些局限性，为未来设计更有效的AI辅导系统提供经验依据。

**技术框架**：研究采用以下技术框架：1) 数据收集：收集AI模拟和真实人类的辅导对话数据。2) IRF编码：使用启动-响应-反馈（IRF）编码方案对对话数据进行标注，提取关键的互动行为。3) 认知网络分析（ENA）：利用ENA分析对话中的互动模式，揭示不同类型的对话在认知层面的差异。4) 定量比较：对IRF编码和ENA的结果进行定量比较，分析AI模拟对话和人类对话在话语长度、提问、反馈等方面的差异。

**关键创新**：论文的关键创新在于：1) 系统性地对比分析了AI模拟和人类辅导对话的差异，揭示了AI在教学互动深度上的局限性。2) 使用IRF编码和ENA相结合的方法，从结构和行为两个层面深入分析了对话的互动模式。3) 发现了人类对话中“问题-事实性回答-反馈”的教学循环，而AI对话则倾向于“解释-简单回答”的简单信息传递模式。

**关键设计**：IRF编码方案用于标注对话中的启动（Initiation）、响应（Response）和反馈（Feedback）行为。认知网络分析（ENA）用于构建对话的认知网络，节点代表不同的互动行为，边代表行为之间的关联强度。通过比较不同对话的认知网络结构，可以揭示其互动模式的差异。研究中没有涉及特定的神经网络结构或损失函数，重点在于对话数据的分析和比较。

## 📊 实验亮点

研究结果表明，人类辅导对话在话语长度、提问（I-Q）和一般反馈（F-F）行为方面显著优于AI模拟对话。认知网络分析（ENA）揭示，人类对话围绕“问题-事实性回答-反馈”的教学循环，而AI对话则倾向于“解释-简单回答”的简单信息传递模式，表明AI在认知引导和教学深度上存在明显不足。

## 🎯 应用场景

该研究成果可应用于改进智能教育系统，例如个性化辅导机器人、在线学习平台等。通过理解人类教师的教学策略，可以设计更有效的AI辅导模型，提升学生的学习效果和高阶思维能力。研究结果也为评估和优化现有AI教育产品的教学质量提供了参考。

## 📄 摘要（原文）

> Heuristic and scaffolded teacher-student dialogues are widely regarded as critical for fostering students' higher-order thinking and deep learning. However, large language models (LLMs) currently face challenges in generating pedagogically rich interactions. This study systematically investigates the structural and behavioral differences between AI-simulated and authentic human tutoring dialogues. We conducted a quantitative comparison using an Initiation-Response-Feedback (IRF) coding scheme and Epistemic Network Analysis (ENA). The results show that human dialogues are significantly superior to their AI counterparts in utterance length, as well as in questioning (I-Q) and general feedback (F-F) behaviors. More importantly, ENA results reveal a fundamental divergence in interactional patterns: human dialogues are more cognitively guided and diverse, centered around a "question-factual response-feedback" teaching loop that clearly reflects pedagogical guidance and student-driven thinking; in contrast, simulated dialogues exhibit a pattern of structural simplification and behavioral convergence, revolving around an "explanation-simplistic response" loop that is essentially a simple information transfer between the teacher and student. These findings illuminate key limitations in current AI-generated tutoring and provide empirical guidance for designing and evaluating more pedagogically effective generative educational dialogue systems.

