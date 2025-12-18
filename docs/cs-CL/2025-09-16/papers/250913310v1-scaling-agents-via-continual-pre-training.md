---
layout: default
title: Scaling Agents via Continual Pre-training
---

# Scaling Agents via Continual Pre-training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13310" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13310v1</a>
  <a href="https://arxiv.org/pdf/2509.13310.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13310v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13310v1', 'Scaling Agents via Continual Pre-training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liangcai Su, Zhen Zhang, Guangyu Li, Zhuo Chen, Chenxi Wang, Maojia Song, Xinyu Wang, Kuan Li, Jialong Wu, Xuanzhong Chen, Zile Qiao, Zhongwang Zhang, Huifeng Yin, Shihao Cai, Runnan Fang, Zhengwei Tao, Wenbiao Yin, Chenxiong Qian, Yong Jiang, Pengjun Xie, Fei Huang, Jingren Zhou

**分类**: cs.CL

**发布日期**: 2025-09-16

**备注**: https://tongyi-agent.github.io/blog/introducing-tongyi-deep-research/

---

## 💡 一句话要点

**提出Agentic CPT，构建强大的Agentic基础模型，提升智能体任务性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `智能体` `持续预训练` `大语言模型` `工具使用` `Agentic CPT`

## 📋 核心要点

1. 现有智能体后训练方法在开源实现中表现不佳，主要原因是缺乏强大的智能体基础模型。
2. 论文提出Agentic持续预训练（Agentic CPT）方法，用于构建更强大的智能体基础模型。
3. 实验结果表明，AgentFounder在多个基准测试中取得了最先进的性能，并保持了强大的工具使用能力。

## 📝 摘要（中文）

大型语言模型（LLMs）已经发展成为具有自主工具使用和多步骤推理能力的智能体系统，可以解决复杂的难题。然而，在通用基础模型上进行后训练的方法在智能体任务中表现不佳，尤其是在开源实现中。我们发现根本原因是缺乏强大的智能体基础模型，这迫使模型在后训练期间同时学习各种智能体行为，并将其与专家演示对齐，从而造成根本的优化冲突。为此，我们首次提出将Agentic持续预训练（Agentic CPT）纳入深度研究智能体训练流程中，以构建强大的智能体基础模型。基于此方法，我们开发了一个名为AgentFounder的深度研究智能体模型。我们在10个基准测试中评估了我们的AgentFounder-30B，并取得了最先进的性能，同时保持了强大的工具使用能力，特别是在BrowseComp-en上达到39.9%，在BrowseComp-zh上达到43.3%，在HLE上达到31.5%的Pass@1。

## 🔬 方法详解

**问题定义**：现有方法在通用大语言模型的基础上进行后训练，以赋予模型智能体能力。然而，由于缺乏专门为智能体任务优化的基础模型，后训练过程需要同时学习多种智能体行为并对齐专家演示，导致优化困难，性能受限。尤其是在开源场景下，这一问题更加突出。

**核心思路**：论文的核心思路是先通过Agentic持续预训练（Agentic CPT）构建一个强大的智能体基础模型，然后再进行后续的微调或对齐。这样可以避免后训练阶段同时学习多种复杂行为的困难，从而提升智能体任务的整体性能。

**技术框架**：AgentFounder的训练流程包含Agentic CPT阶段和后续的微调阶段。Agentic CPT阶段利用大量的智能体交互数据，持续预训练语言模型，使其具备初步的智能体能力。后续的微调阶段则根据具体的任务需求，对模型进行进一步的优化和对齐。

**关键创新**：论文的关键创新在于提出了Agentic CPT的概念，并将其应用于智能体模型的训练中。与传统的后训练方法相比，Agentic CPT能够更有效地构建智能体基础模型，从而提升智能体任务的性能。这是首次将持续预训练的思想应用于智能体领域。

**关键设计**：Agentic CPT阶段的关键设计包括：1) 选择合适的预训练数据，涵盖各种智能体交互场景；2) 设计合适的预训练目标，例如模仿学习、奖励最大化等；3) 调整预训练的规模和迭代次数，以获得最佳的性能。

## 📊 实验亮点

AgentFounder-30B在10个基准测试中取得了最先进的性能。特别是在BrowseComp-en上达到39.9%，在BrowseComp-zh上达到43.3%，在HLE上达到31.5%的Pass@1。这些结果表明，Agentic CPT能够有效地提升智能体模型的性能，使其在复杂任务中表现出色。

## 🎯 应用场景

该研究成果可应用于各种需要智能体自主完成任务的场景，例如自动化研究、智能客服、自动化编程等。通过构建更强大的智能体基础模型，可以提升这些应用的智能化水平和效率，并降低开发成本。未来，该方法有望推动智能体技术在更广泛领域的应用。

## 📄 摘要（原文）

> Large language models (LLMs) have evolved into agentic systems capable of autonomous tool use and multi-step reasoning for complex problem-solving. However, post-training approaches building upon general-purpose foundation models consistently underperform in agentic tasks, particularly in open-source implementations. We identify the root cause: the absence of robust agentic foundation models forces models during post-training to simultaneously learn diverse agentic behaviors while aligning them to expert demonstrations, thereby creating fundamental optimization tensions. To this end, we are the first to propose incorporating Agentic Continual Pre-training (Agentic CPT) into the deep research agents training pipeline to build powerful agentic foundational models. Based on this approach, we develop a deep research agent model named AgentFounder. We evaluate our AgentFounder-30B on 10 benchmarks and achieve state-of-the-art performance while retains strong tool-use ability, notably 39.9% on BrowseComp-en, 43.3% on BrowseComp-zh, and 31.5% Pass@1 on HLE.

