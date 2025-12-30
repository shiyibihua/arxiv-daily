---
layout: default
title: "ClinDEF: A Dynamic Evaluation Framework for Large Language Models in Clinical Reasoning"
---

# ClinDEF: A Dynamic Evaluation Framework for Large Language Models in Clinical Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23440" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23440v1</a>
  <a href="https://arxiv.org/pdf/2512.23440.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23440v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23440v1', 'ClinDEF: A Dynamic Evaluation Framework for Large Language Models in Clinical Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuqi Tang, Jing Yu, Zichang Su, Kehua Feng, Zhihui Zhu, Libin Wang, Lei Liang, Qiang Zhang, Keyan Ding, Huajun Chen

**分类**: cs.CL

**发布日期**: 2025-12-29

**备注**: 23 pages, 4 figures, under review

---

## 💡 一句话要点

**提出ClinDEF动态评估框架，用于评估大型语言模型在临床推理中的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `临床推理` `动态评估` `医患对话` `知识图谱`

## 📋 核心要点

1. 现有LLM评估侧重静态问答，无法有效评估临床推理中动态交互的过程。
2. ClinDEF框架基于疾病知识图谱，动态生成病例，模拟医患多轮交互对话。
3. ClinDEF评估协议不仅关注诊断准确性，还包括效率分析和诊断质量评估。

## 📝 摘要（中文）

临床诊断始于医患互动，医生通过患者的反馈迭代地收集信息、确定检查并完善鉴别诊断。现有的LLM基准测试侧重于静态问答，难以体现这种动态的临床推理过程。为了弥补这些差距，最近的方法探索了涉及交互式临床对话的动态医学框架。尽管有效，但它们通常依赖于有限的、易受污染的数据集，并且缺乏细粒度的多层次评估。本文提出了ClinDEF，一个用于评估LLM在模拟诊断对话中临床推理能力的动态框架。该方法基于疾病知识图谱，动态生成病例，并促进基于LLM的医生与自动患者代理之间的多轮交互。我们的评估协议超越了诊断准确性，纳入了细粒度的效率分析和基于标准的诊断质量评估。实验表明，ClinDEF有效地揭示了最先进的LLM中关键的临床推理差距，提供了一种更细致和临床意义的评估范式。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLM）在临床推理方面的评估主要依赖于静态的问答形式，无法模拟真实的医患交互过程。这种静态评估方式忽略了医生在诊断过程中需要不断收集信息、调整诊断方向的动态性。此外，现有的动态医学框架依赖的数据集有限，容易受到污染，并且缺乏细粒度的多层次评估，难以全面反映LLM在临床推理中的能力。

**核心思路**：ClinDEF的核心思路是构建一个动态的评估框架，通过模拟医患之间的对话来评估LLM的临床推理能力。该框架基于疾病知识图谱，可以动态生成不同的病例，并允许LLM扮演医生角色与自动患者代理进行多轮交互。通过这种方式，可以更真实地模拟临床诊断过程，并对LLM的推理能力进行更全面的评估。

**技术框架**：ClinDEF框架主要包含以下几个模块：1) **疾病知识图谱**：用于存储疾病、症状、检查等相关信息，为病例生成和患者代理提供知识基础。2) **病例生成器**：基于疾病知识图谱，动态生成不同的患者病例，包括患者的基本信息、主诉、病史等。3) **患者代理**：模拟患者的行为，根据医生的提问提供相应的回答。4) **LLM医生**：扮演医生的角色，与患者代理进行对话，收集信息，进行诊断。5) **评估模块**：对LLM医生的诊断结果进行评估，包括诊断准确性、效率和诊断质量。

**关键创新**：ClinDEF的关键创新在于其动态的评估方式，能够模拟真实的医患交互过程，更全面地评估LLM在临床推理方面的能力。与现有的静态评估方法相比，ClinDEF能够更好地反映LLM在信息收集、诊断推理和决策制定方面的能力。此外，ClinDEF还引入了细粒度的评估指标，包括效率分析和基于标准的诊断质量评估，能够更深入地分析LLM的优势和不足。

**关键设计**：ClinDEF框架的关键设计包括：1) **疾病知识图谱的构建**：需要选择合适的知识图谱构建方法，并确保知识图谱的完整性和准确性。2) **患者代理的设计**：需要设计合理的患者行为模型，使其能够根据医生的提问提供真实、合理的回答。3) **评估指标的选择**：需要选择能够全面反映LLM临床推理能力的评估指标，包括诊断准确性、效率和诊断质量。4) **多轮对话的管理**：需要设计有效的对话管理机制，确保对话的流畅性和有效性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23440v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23440v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23440v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，ClinDEF能够有效地揭示现有LLM在临床推理方面的差距。例如，一些最先进的LLM在诊断准确性方面表现不佳，并且在信息收集和诊断推理方面存在明显的不足。ClinDEF的评估结果为改进LLM在医疗领域的应用提供了重要的参考。

## 🎯 应用场景

ClinDEF框架可用于评估和改进LLM在医疗领域的应用，例如辅助诊断、智能问诊等。通过该框架，可以发现LLM在临床推理方面的不足，并针对性地进行改进，提高LLM在医疗领域的实用性和可靠性。此外，该框架还可以用于医学教育，帮助医学生提高临床推理能力。

## 📄 摘要（原文）

> Clinical diagnosis begins with doctor-patient interaction, during which physicians iteratively gather information, determine examination and refine differential diagnosis through patients' response. This dynamic clinical-reasoning process is poorly represented by existing LLM benchmarks that focus on static question-answering. To mitigate these gaps, recent methods explore dynamic medical frameworks involving interactive clinical dialogues. Although effective, they often rely on limited, contamination-prone datasets and lack granular, multi-level evaluation. In this work, we propose ClinDEF, a dynamic framework for assessing clinical reasoning in LLMs through simulated diagnostic dialogues. Grounded in a disease knowledge graph, our method dynamically generates patient cases and facilitates multi-turn interactions between an LLM-based doctor and an automated patient agent. Our evaluation protocol goes beyond diagnostic accuracy by incorporating fine-grained efficiency analysis and rubric-based assessment of diagnostic quality. Experiments show that ClinDEF effectively exposes critical clinical reasoning gaps in state-of-the-art LLMs, offering a more nuanced and clinically meaningful evaluation paradigm.

