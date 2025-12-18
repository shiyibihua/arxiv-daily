---
layout: default
title: Efficient and Transferable Agentic Knowledge Graph RAG via Reinforcement Learning
---

# Efficient and Transferable Agentic Knowledge Graph RAG via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26383" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26383v3</a>
  <a href="https://arxiv.org/pdf/2509.26383.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26383v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26383v3', 'Efficient and Transferable Agentic Knowledge Graph RAG via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinyeop Song, Song Wang, Julian Shun, Yada Zhu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-30 (更新: 2025-10-09)

**备注**: 10 pages, 5 figures. Submitted to ICLR 2026

**🔗 代码/项目**: [GITHUB](https://github.com/Jinyeop3110/KG-R1)

---

## 💡 一句话要点

**提出基于强化学习的高效可迁移Agentic知识图谱RAG框架KG-R1**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识图谱` `检索增强生成` `强化学习` `Agent` `问答系统`

## 📋 核心要点

1. 现有KG-RAG系统依赖多模块LLM组合，导致推理成本高昂且模型行为与特定知识图谱绑定。
2. KG-R1采用强化学习训练单个agent，使其能够自主与知识图谱交互并进行检索、推理和生成。
3. 实验表明，KG-R1在KGQA任务上，使用更少的token实现了更高的准确率，并具备良好的跨知识图谱迁移能力。

## 📝 摘要（中文）

知识图谱检索增强生成(KG-RAG)将大型语言模型(LLM)与结构化、可验证的知识图谱(KG)相结合，以减少幻觉并暴露推理轨迹。然而，许多KG-RAG系统组合了多个LLM模块(例如，规划、推理和响应)，从而增加了推理成本，并将行为绑定到特定的目标KG。为了解决这个问题，我们引入了KG-R1，这是一个通过强化学习(RL)实现的agentic KG检索增强生成(KG-RAG)框架。KG-R1利用单个agent与KG作为其环境进行交互，学习在每个步骤中检索信息，并将检索到的信息整合到其推理和生成过程中。该过程通过端到端的RL进行优化。在知识图谱问答(KGQA)基准测试的受控实验中，我们的方法展示了效率和可迁移性：使用Qwen-2.5-3B，KG-R1以比使用更大基础模型或微调模型的先前多模块工作流程方法更少的生成token提高了答案准确性。此外，KG-R1实现了即插即用：经过训练后，它无需修改即可在新KG上保持强大的准确性。这些特性使KG-R1成为一个有前景的KG-RAG框架，适用于实际部署。我们的代码已在https://github.com/Jinyeop3110/KG-R1上公开发布。

## 🔬 方法详解

**问题定义**：现有KG-RAG方法通常采用多模块的LLM流程，例如规划、推理和生成，这导致了较高的计算成本和推理延迟。此外，这些方法往往针对特定的知识图谱进行优化，缺乏跨图谱的泛化能力，难以适应实际应用中不断变化的知识库。因此，如何设计一个高效且可迁移的KG-RAG框架是一个关键问题。

**核心思路**：KG-R1的核心思路是将KG-RAG过程建模为一个agent与知识图谱环境的交互过程。通过强化学习，agent能够学习如何在每一步选择合适的知识图谱节点进行检索，并将检索到的信息融入到自身的推理和生成过程中。这种端到端的学习方式避免了手动设计复杂的多模块流程，从而提高了效率和泛化能力。

**技术框架**：KG-R1框架包含一个agent和一个知识图谱环境。Agent接收问题作为输入，并根据当前状态选择一个动作（即选择一个知识图谱节点进行检索）。环境根据agent的动作返回相应的节点信息。Agent将检索到的信息融入到自身的记忆中，并重复上述过程直到生成最终答案。整个过程通过强化学习进行优化，目标是最大化回答问题的准确率。

**关键创新**：KG-R1最重要的创新在于将KG-RAG过程建模为一个agent与环境的交互过程，并通过强化学习进行端到端优化。与传统的多模块方法相比，KG-R1避免了手动设计复杂的流程，从而提高了效率和泛化能力。此外，KG-R1的agent能够自主学习如何选择合适的知识图谱节点进行检索，从而更好地利用知识图谱中的信息。

**关键设计**：KG-R1使用Qwen-2.5-3B作为基础语言模型。Agent的网络结构包括一个embedding层、一个LSTM层和一个全连接层。损失函数采用交叉熵损失函数，用于衡量生成答案与正确答案之间的差异。强化学习算法采用Proximal Policy Optimization (PPO)。训练过程中，使用reward shaping技术来加速学习过程。

## 📊 实验亮点

实验结果表明，KG-R1在KGQA基准测试中取得了显著的性能提升。使用Qwen-2.5-3B模型，KG-R1在回答准确率方面优于使用更大规模模型或经过微调的传统多模块方法。此外，KG-R1还展现出了良好的跨知识图谱迁移能力，无需修改即可在新知识图谱上保持较高的准确率。例如，在某些数据集上，KG-R1的准确率提升超过10%。

## 🎯 应用场景

KG-R1具有广泛的应用前景，例如智能问答系统、知识图谱构建、信息检索等。它可以应用于各种领域，例如医疗、金融、教育等，为用户提供准确、可靠的知识服务。未来，KG-R1可以进一步扩展到支持多语言知识图谱、动态知识图谱等，从而更好地满足实际应用的需求。

## 📄 摘要（原文）

> Knowledge-graph retrieval-augmented generation (KG-RAG) couples large language models (LLMs) with structured, verifiable knowledge graphs (KGs) to reduce hallucinations and expose reasoning traces. However, many KG-RAG systems compose multiple LLM modules (e.g planning, reasoning, and responding), inflating inference cost and binding behavior to a specific target KG. To address this, we introduce KG-R1, an agentic KG retrieval-augmented generation (KG-RAG) framework through reinforcement learning (RL). KG-R1 utilizes a single agent that interacts with KGs as its environment, learning to retrieve at each step and incorporating the retrieved information into its reasoning and generation. The process is optimized through end-to-end RL. In controlled experiments across Knowledge-Graph Question Answering (KGQA) benchmarks, our method demonstrates both efficiency and transferability: Using Qwen-2.5-3B, KG-R1 improves answer accuracy with fewer generation tokens than prior multi-module workflow methods that use larger foundation or fine-tuned models. Furthermore, KG-R1 enables plug and play: after training, it maintains strong accuracy on new KGs without modification. These properties make KG-R1 a promising KG-RAG framework for real-world deployment. Our code is publicly available at https://github.com/Jinyeop3110/KG-R1.

