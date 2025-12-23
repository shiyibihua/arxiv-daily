---
layout: default
title: Evaluating Multimodal Large Language Models on Educational Textbook Question Answering
---

# Evaluating Multimodal Large Language Models on Educational Textbook Question Answering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21596" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21596v2</a>
  <a href="https://arxiv.org/pdf/2506.21596.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21596v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21596v2', 'Evaluating Multimodal Large Language Models on Educational Textbook Question Answering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hessa A. Alawwad, Anas Zafar, Areej Alhothali, Usman Naseem, Ali Alkhathlan, Amani Jamal

**分类**: cs.CL, cs.AI, cs.IR

**发布日期**: 2025-06-18 (更新: 2025-07-15)

**备注**: 8 Pages

---

## 💡 一句话要点

**评估多模态大语言模型在教材问答任务中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `教材问答` `检索增强生成` `灾难性上下文干扰` `教育技术` `模型微调` `复杂推理`

## 📋 核心要点

1. 现有的多模态大语言模型在处理复杂教育材料时的推理能力尚未得到充分验证，存在性能不稳定的问题。
2. 本文提出了一种多模态检索增强生成管道，以提供相关的课程段落和图表作为上下文，从而模拟真实学习场景。
3. 实验结果显示，LLaVA在文本问题上的表现有所提升，但LLaMA 3.2-Vision在图表任务上的准确性显著下降，揭示了灾难性上下文干扰现象。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）在视觉语言任务中取得了成功，但其在复杂教育材料上的推理能力尚未得到充分测试。本研究首次评估了LLaVA-1.5和LLaMA 3.2-Vision等最先进的MLLMs在教材问答（TQA）任务中的表现，使用CK12-QA数据集。我们引入了一种多模态检索增强生成（RAG）管道，以模拟真实学习环境。零-shot实验揭示了一个重要的权衡：虽然检索的上下文提高了LLaVA在文本问题上的表现，但显著降低了LLaMA 3.2-Vision在图表任务上的准确性，从74.07%降至25.93%。我们将这一显著现象称为“灾难性上下文干扰”。此外，微调结果显示架构差异：LLaMA 3.2-Vision在测试集上的表现提高至71.16%，而LLaVA的表现下降，表明其在泛化方面面临挑战。我们的结果强调了MLLMs在模态优先级和上下文整合方面的挑战，为开发更强大的AI驱动教育工具提供了基准和关键方向。

## 🔬 方法详解

**问题定义**：本研究旨在评估多模态大语言模型在教材问答任务中的表现，现有方法在复杂教育材料的推理能力上存在不足，尤其是在图表任务中的准确性显著下降。

**核心思路**：通过引入多模态检索增强生成（RAG）管道，提供相关的课程段落和图表作为上下文，以提升模型在教材问答任务中的表现。

**技术框架**：整体架构包括数据检索模块、上下文生成模块和问答生成模块。数据检索模块负责从CK12-QA数据集中提取相关信息，上下文生成模块整合文本和图表信息，问答生成模块则基于整合的上下文生成答案。

**关键创新**：提出了“灾难性上下文干扰”这一概念，揭示了在多模态任务中上下文检索对不同模型的影响，尤其是对LLaMA 3.2-Vision的负面影响。

**关键设计**：在实验中，采用了零-shot学习和微调策略，针对不同模型的架构进行了优化，LLaMA 3.2-Vision在微调后表现提升至71.16%，而LLaVA的表现则出现下降，反映出其在泛化能力上的挑战。

## 📊 实验亮点

实验结果显示，LLaVA在文本问题上的表现有所提升，而LLaMA 3.2-Vision在图表任务上的准确性从74.07%降至25.93%，揭示了灾难性上下文干扰现象。经过微调，LLaMA 3.2-Vision的表现提升至71.16%，显示出其在多模态整合能力上的潜力。

## 🎯 应用场景

该研究的成果可广泛应用于教育领域，尤其是在智能教育工具的开发中，能够帮助学生更有效地理解复杂的教材内容。未来，基于此研究的多模态大语言模型有望在个性化学习和自适应学习系统中发挥重要作用。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have shown success in vision-language tasks, but their ability to reason over complex educational materials remains largely untested. This work presents the first evaluation of state-of-the-art MLLMs, including LLaVA-1.5 and LLaMA 3.2-Vision, on the textbook question answering (TQA) task using the CK12-QA dataset. We introduce a multimodal retrieval-augmented generation (RAG) pipeline to simulate real-world learning by providing relevant lesson paragraphs and diagrams as context. Our zero-shot experiments reveal a critical trade-off: while retrieved context improves LLaVA's performance on text-based questions, it significantly degrades the accuracy of the more powerful LLaMA 3.2-Vision on diagram-based tasks, dropping its validation accuracy from 74.07% to 25.93%. We term this statistically significant phenomenon "catastrophic context interference." Furthermore, fine-tuning highlights architectural differences: LLaMA 3.2-Vision's performance improves to 71.16% on the test set, demonstrating its capacity to learn multimodal integration, whereas LLaVA's performance declines, indicating challenges with generalization. Our results underscore the challenges MLLMs face in modality prioritization and context integration, providing a benchmark and pointing to key directions for developing more robust AI-driven educational tools.

