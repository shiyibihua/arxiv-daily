---
layout: default
title: "BOAD: Discovering Hierarchical Software Engineering Agents via Bandit Optimization"
---

# BOAD: Discovering Hierarchical Software Engineering Agents via Bandit Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23631" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23631v1</a>
  <a href="https://arxiv.org/pdf/2512.23631.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23631v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23631v1', 'BOAD: Discovering Hierarchical Software Engineering Agents via Bandit Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Iris Xu, Guangtao Zeng, Zexue He, Charles Jin, Aldo Pareja, Dan Gutfreund, Chuang Gan, Zhang-Wei Hong

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-29

**🔗 代码/项目**: [GITHUB](https://github.com/iamxjy/BOAD-SWE-Agent)

---

## 💡 一句话要点

**提出BOAD以自动发现层次化软件工程代理解决复杂问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `层次化代理` `多臂赌博机` `软件工程` `自动化协作` `模型泛化能力`

## 📋 核心要点

1. 现有软件工程代理通常依赖单一模型处理复杂任务，导致泛化能力差和上下文干扰。
2. 本文提出BOAD框架，通过多臂赌博机方法自动发现层次化代理，协调多个专门子代理处理不同子任务。
3. 实验结果显示，BOAD在多个基准测试中表现优异，显著提高了长时间跨度软件工程任务的泛化能力。

## 📝 摘要（中文）

大型语言模型（LLMs）在推理和编码能力上表现出色，但在处理长时间跨度和分布外的软件工程（SWE）问题时却难以泛化。现有系统通常依赖单一代理处理整个工作流程，导致模型保留无关上下文，从而产生虚假关联和较差的泛化能力。为此，本文提出将SWE代理结构化为协调专门子代理的指挥者，以处理定位、编辑和验证等子任务。我们将层次发现问题形式化为多臂赌博机（MAB）问题，通过奖励机制评估子代理的协作效果。BOAD框架在有限评估预算下高效探索子代理设计，实验结果表明其在SWE-bench-Verified上优于单代理和手动设计的多代理系统，并在SWE-bench-Live上取得了第二名的优异成绩，超越了GPT-4等更大模型。

## 🔬 方法详解

**问题定义**：本文旨在解决现有软件工程代理在处理复杂问题时的泛化能力不足，尤其是在长时间跨度和分布外问题上的表现。现有方法依赖单一代理，导致上下文干扰和虚假关联。

**核心思路**：论文提出将软件工程代理结构化为多个专门子代理的层次化系统，通过多臂赌博机（MAB）方法自动发现有效的代理层次，以便更好地分配任务和提高协作效率。

**技术框架**：整体架构包括一个指挥者代理和多个子代理，指挥者负责协调子代理的工作。每个子代理专注于特定任务，如代码定位、编辑和验证。通过MAB方法，系统能够在有限的评估预算内探索和优化子代理的组合。

**关键创新**：最重要的创新在于将层次发现问题形式化为MAB问题，使得在复杂的代理系统中能够有效地评估和优化子代理的协作效果。这一方法与传统的单一代理设计有本质区别。

**关键设计**：在设计中，采用了奖励机制来评估每个子代理的协作效果，确保在探索过程中能够快速识别出高效的代理组合。具体参数设置和损失函数的选择也经过精心设计，以适应软件工程任务的特点。

## 📊 实验亮点

在SWE-bench-Verified基准测试中，BOAD框架的表现优于传统的单代理和手动设计的多代理系统。在SWE-bench-Live上，BOAD的36B系统在评估时排名第二，超越了更大模型如GPT-4和Claude，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发、自动化测试和代码审查等。通过自动发现和协调层次化代理，能够显著提高软件工程任务的效率和准确性，减少人工干预的需求，未来可能对软件开发流程产生深远影响。

## 📄 摘要（原文）

> Large language models (LLMs) have shown strong reasoning and coding capabilities, yet they struggle to generalize to real-world software engineering (SWE) problems that are long-horizon and out of distribution. Existing systems often rely on a single agent to handle the entire workflow-interpreting issues, navigating large codebases, and implementing fixes-within one reasoning chain. Such monolithic designs force the model to retain irrelevant context, leading to spurious correlations and poor generalization. Motivated by how human engineers decompose complex problems, we propose structuring SWE agents as orchestrators coordinating specialized sub-agents for sub-tasks such as localization, editing, and validation. The challenge lies in discovering effective hierarchies automatically: as the number of sub-agents grows, the search space becomes combinatorial, and it is difficult to attribute credit to individual sub-agents within a team. We address these challenges by formulating hierarchy discovery as a multi-armed bandit (MAB) problem, where each arm represents a candidate sub-agent and the reward measures its helpfulness when collaborating with others. This framework, termed Bandit Optimization for Agent Design (BOAD), enables efficient exploration of sub-agent designs under limited evaluation budgets. On SWE-bench-Verified, BOAD outperforms single-agent and manually designed multi-agent systems. On SWE-bench-Live, featuring more recent and out-of-distribution issues, our 36B system ranks second on the leaderboard at the time of evaluation, surpassing larger models such as GPT-4 and Claude. These results demonstrate that automatically discovered hierarchical multi-agent systems significantly improve generalization on challenging long-horizon SWE tasks. Code is available at https://github.com/iamxjy/BOAD-SWE-Agent.

